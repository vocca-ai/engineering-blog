# Vocca Engineering blog

Articles for vocca.com/en/engineering, written in Markdown and synced to the Webflow CMS (collection "📄 Engineering").

## Write a post

1. Copy `posts/_template.md` to `posts/YYYY-MM-short-title.md` and write.
2. Keep `status: draft` and open a PR. CI checks the front matter.
3. On merge, the post lands in Webflow as a draft so it can be previewed in the Designer.
4. When it is ready, switch to `status: published` in a new PR. It goes live at the next site publish.

## Images

Put images in `posts/images/` and reference them with a relative path: `![Alt text](images/my-diagram.png)`, or `cover: images/my-cover.png` in the front matter. On sync, Webflow copies them to its CDN. This repo is public, so anything committed here is visible to everyone, drafts included.

## Rules

- No patient data, ever: no names, phone numbers, transcripts or screenshots from real calls. Use made-up examples.
- No customer names without their written agreement.
- No screenshots of real calls, customer dashboards or patient conversations. Diagrams and made-up data only.
- Your author entry must exist in the Webflow Authors collection; ask Hugo if it doesn't.

## How the sync works

`scripts/sync.py` upserts every file in `posts/` (except `_*.md`), matching on the `source-path` CMS field. Deleting a file does not delete the Webflow item. The sync never publishes the site.

Local run: `pip install -r requirements.txt && python scripts/sync.py --check`.
