"""Sync posts/*.md to the Webflow CMS collection "📄 Engineering".

Each Markdown file maps to one CMS item, matched on the `source-path` field.
`status: draft` keeps the item as a Webflow draft; `status: published` marks it
ready, so it goes live at the next site publish. This script never publishes
the site itself.

Usage:
  python scripts/sync.py --check      # validate front matter, no API call
  python scripts/sync.py              # upsert every post (needs WEBFLOW_API_TOKEN)
"""

import argparse
import math
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

import markdown
import requests
import yaml

COLLECTION_ID = "6ae34bd6bc65ae4e3a16ea1a"  # 📄 Engineering
AUTHORS_COLLECTION_ID = "6aacf8cd6040b2551bc01b6e"  # Authors (shared with the marketing blog)
API = "https://api.webflow.com/v2"
ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"

TEAMS = {"AI", "Platform", "Interop", "Product"}
STATUSES = {"draft", "published"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
WORDS_PER_MINUTE = 220


class PostError(Exception):
    pass


def post_files():
    # Files starting with "_" (templates) are never synced.
    return sorted(p for p in POSTS_DIR.glob("*.md") if not p.name.startswith("_"))


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise PostError("missing front matter (--- ... ---)")
    meta = yaml.safe_load(m.group(1)) or {}
    body_md = m.group(2).strip()

    def require(key):
        if not meta.get(key):
            raise PostError(f"missing `{key}`")
        return meta[key]

    title = require("title")
    summary = require("summary")
    status = meta.get("status", "draft")
    if status not in STATUSES:
        raise PostError(f"`status` must be one of {sorted(STATUSES)}")
    team = require("team")
    if team not in TEAMS:
        raise PostError(f"`team` must be one of {sorted(TEAMS)}")
    published = require("date")
    if not isinstance(published, date):
        raise PostError("`date` must be YYYY-MM-DD")
    updated = meta.get("updated")
    if updated is not None and not isinstance(updated, date):
        raise PostError("`updated` must be YYYY-MM-DD")
    if status == "published" and not meta.get("author"):
        raise PostError("`author` is required before publishing")
    if status == "published" and not meta.get("cover"):
        raise PostError("`cover` is required before publishing")

    # Default slug: file name without its YYYY-MM- prefix.
    slug = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-", "", path.stem)
    if not SLUG_RE.match(slug):
        raise PostError(f"invalid slug `{slug}` (lowercase letters, digits, hyphens)")
    if re.search(r"^# ", body_md, re.M):
        raise PostError("body must not contain a level-1 heading; the title comes from `title`")

    words = len(re.findall(r"\w+", body_md))
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "status": status,
        "author": meta.get("author"),
        "co_author": meta.get("co_author"),
        "field_data": {
            "name": title,
            "slug": slug,
            "summary": summary,
            "body": markdown.markdown(body_md, extensions=["fenced_code"]),
            "team": team,  # option name, resolved to its id later
            "published-date": f"{published.isoformat()}T00:00:00.000Z",
            "last-update": f"{updated.isoformat()}T00:00:00.000Z" if updated else None,
            "date-displayed": f"{published:%b} {published.day}, {published.year}",
            "reading-time-min": max(1, math.ceil(words / WORDS_PER_MINUTE)),
            "featured": bool(meta.get("featured", False)),
            "cover-image": {"url": meta["cover"], "alt": meta.get("cover_alt", title)} if meta.get("cover") else None,
            "seo---title": meta.get("seo_title") or title,
            "seo---description": meta.get("seo_description") or summary,
            "source-path": path.relative_to(ROOT).as_posix(),
        },
    }


class Webflow:
    def __init__(self, token):
        self.s = requests.Session()
        self.s.headers.update({"Authorization": f"Bearer {token}", "accept": "application/json"})

    def call(self, method, path, **kwargs):
        for _ in range(5):
            r = self.s.request(method, f"{API}{path}", timeout=30, **kwargs)
            if r.status_code == 429:
                time.sleep(int(r.headers.get("Retry-After", "10")))
                continue
            if not r.ok:
                raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text}")
            return r.json() if r.content else None
        raise RuntimeError(f"{method} {path}: still rate limited after retries")

    def items(self, collection_id):
        out, offset = [], 0
        while True:
            page = self.call("GET", f"/collections/{collection_id}/items", params={"limit": 100, "offset": offset})
            out += page["items"]
            offset += len(page["items"])
            if offset >= page["pagination"]["total"] or not page["items"]:
                return out


def sync(posts, wf):
    schema = wf.call("GET", f"/collections/{COLLECTION_ID}")
    team_field = next(f for f in schema["fields"] if f["slug"] == "team")
    team_ids = {o["name"]: o["id"] for o in team_field["validations"]["options"]}
    author_ids = {i["fieldData"]["slug"]: i["id"] for i in wf.items(AUTHORS_COLLECTION_ID)}
    existing = {i["fieldData"].get("source-path"): i for i in wf.items(COLLECTION_ID)}

    failed = False
    for post in posts:
        fd = dict(post["field_data"])
        fd["team"] = team_ids[fd["team"]]
        try:
            for key, field in (("author", "author"), ("co_author", "co-author")):
                if post[key]:
                    if post[key] not in author_ids:
                        raise PostError(f"unknown author `{post[key]}` (known: {', '.join(sorted(author_ids))})")
                    fd[field] = author_ids[post[key]]
                else:
                    fd[field] = None
            payload = {"isDraft": post["status"] == "draft", "isArchived": False, "fieldData": fd}
            item = existing.get(post["path"])
            if item:
                wf.call("PATCH", f"/collections/{COLLECTION_ID}/items/{item['id']}", json=payload)
                print(f"updated  {post['path']} ({post['status']})")
            else:
                wf.call("POST", f"/collections/{COLLECTION_ID}/items", json=payload)
                print(f"created  {post['path']} ({post['status']})")
        except (PostError, RuntimeError) as e:
            print(f"FAILED   {post['path']}: {e}", file=sys.stderr)
            failed = True

    orphans = set(existing) - {p["path"] for p in posts} - {None}
    for path in sorted(orphans):
        print(f"warning  {path} is in Webflow but not in the repo (left untouched)")
    return not failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate posts without calling Webflow")
    args = ap.parse_args()

    posts, ok = [], True
    for path in post_files():
        try:
            posts.append(parse(path))
        except PostError as e:
            print(f"INVALID  {path.relative_to(ROOT)}: {e}", file=sys.stderr)
            ok = False
    if not ok:
        sys.exit(1)
    if args.check:
        print(f"{len(posts)} post(s) valid")
        return

    token = os.environ.get("WEBFLOW_API_TOKEN")
    if not token:
        sys.exit("WEBFLOW_API_TOKEN is not set")
    if not sync(posts, Webflow(token)):
        sys.exit(1)


if __name__ == "__main__":
    main()
