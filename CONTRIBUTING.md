# Contributing

Add resources that solve a concrete development need. Prefer canonical upstream links and concise original descriptions: what it is useful for, where it fits, and meaningful constraints. Inclusion is not an endorsement or adoption audit.

Update the appropriate full catalog and `resources.json`, preserving each existing record and its provenance. For new records, provide the original evidence and descriptions; generate stable IDs and conservative derived facets with `python scripts/enrich_resources.py --apply`, then regenerate `resources.csv` with `python scripts/export_csv.py`, navigation with `python scripts/generate_indexes.py`, and the AI views (compact catalog, category shards, domain rollup) with `python scripts/generate_ai_views.py`, and the shared counts with `python scripts/catalog_stats.py --write`. Use `index/resource-schema.json` and `index/taxonomy.json` as the active metadata contract. Do not assign unsupported language/platform claims; leave uncertain facets empty or flag them for review. `scripts/enrich_resources.py --check` verifies the derived metadata is present; the explicit `--refresh-topics`, `--refresh-types`, and `--refresh-verification` modes recalculate only those derived fields when their rules change. Preserve different interfaces to the same project when they serve different purposes; do not count raw entries as unique projects. Category page names should be lowercase hyphenated names.

Record the date, source, and scope of actual verification. A successful HTTP request only verifies reachability. Label archived, dormant, unmaintained, mirrored, or service-bound resources honestly and cite upstream evidence. Describe a potential revival separately from a tested release. Keep existing WR task IDs stable; the included backlog is a dated snapshot, not a promise of ongoing project work.

### Finding new candidates

Topic sweeps are repeatable and cheap:

```sh
gh api -X GET search/repositories -f 'q=topic:mcp-server stars:>=200 archived:false fork:false' \
  -f sort=stars -f per_page=50 --jq '.items[] | "\(.stargazers_count)\t\(.full_name)\t\(.license.spdx_id)"'
python3 scripts/search.py "model context protocol" --topic mcp     # check what is already covered
```

Also useful: `https://gittrend.io/hidden-gems` (repositories under 2,000 stars with
strong engagement) and the topic indexes at `https://awesomehub.js.org/`. Before
adding a candidate, deduplicate on GitHub `owner/repository` identity, normalized
URL, and repository name, and drop archived, forked, or unlicensed repositories
unless there is a specific reason to keep them with an inline license caveat.

Do not include credentials, private account information, local machine paths, copied upstream documentation, or dependencies themselves. Linked projects keep their own licenses.

Run `python scripts/validate.py` before proposing a change. It checks index agreement, required fields, URL syntax, category coverage, local Markdown links, accidental local paths, the generated `index/catalog-stats.json`, and the generated count block in `README.md`, `AI_INDEX.md`, and `llms.txt`. It does not perform network or adoption audits.
