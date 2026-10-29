# Vocca Engineering blog

Articles for vocca.com/en/engineering, written in Markdown and synced to the Webflow CMS (collection "📄 Engineering").

## Write a post

1. Copy `posts/_template.md` to `posts/YYYY-MM-short-title.md` and write.
2. Keep `status: draft` and open a PR. CI checks the front matter.
3. On merge, the post lands in Webflow as a draft so it can be previewed in the Designer.
4. When it is ready, switch to `status: published` in a new PR. It goes live at the next site publish.

## Rules

- No patient data, ever: no names, phone numbers, transcripts or screenshots from real calls. Use made-up examples.
- No customer names without their written agreement.
- Your author entry must exist in the Webflow Authors collection; ask Hugo if it doesn't.

## How the sync works

`scripts/sync.py` upserts every file in `posts/` (except `_*.md`), matching on the `source-path` CMS field. Deleting a file does not delete the Webflow item. The sync never publishes the site.

Local run: `pip install -r requirements.txt && python scripts/sync.py --check`.
