# AI index — fastest path through this repository

This repository is a curated pointer library: 2,937 entries, 2,931 distinct
URLs, 101 categories, 13 domains. It contains references and original notes,
not third-party code. Entries are discovery hints, not endorsements — verify
maintenance, license, and compatibility at the primary source.

<!-- BEGIN GENERATED STATS -->
**2,937 catalog entries** · **2,931 distinct URLs** · **101 categories** · **13 domains** · **2,328 project identities**
<!-- END GENERATED STATS -->

## Read in this order (smallest first)

1. **This file** — pick a domain below.
2. **`index/category-groups.json`** — the 101 categories rolled up into
   13 domains, with counts and category IDs.
3. **One category shard** — `index/by-category/<category_id>.json` holds
   only that category's records (name, URL, purpose, facets). Most shards
   are a few KB; load one, not the whole catalog.
4. **Only if you need provenance** — `resources.json` is the canonical
   full catalog (3.3 MB, adds source, check date, review notes per record).
   `index/resources.compact.json` is the same catalog at ~35% of the size
   when you genuinely need every category at once.

Single-file alternative: `llms-full.txt` concatenates every category page and catalog for one-shot ingestion.
Counts and rollups live in `index/catalog-stats.json`; it is generated, so
quote it instead of counting records yourself.
Local alternative: `python scripts/search.py "your query"` with
`--topic`, `--type`, `--use-case`, `--language`, `--platform`, or `--category`.

## Domains

| Domain | Resources | Start with |
|---|---|---|
| ai | 431 | `ai-mcp-servers-and-tool-use`, `ai-machine-learning-and-local-inference`, `ai-agent-frameworks-and-orchestration` |
| windows | 249 | `windows-native-libraries`, `windows-diagnostics`, `windows-desktop-ui` (46 small Windows categories — most hold under 10 entries) |
| languages-runtimes | 360 | `python-rust-and-go-building-blocks`, `languages-and-runtimes`, `niche-language-ecosystems` |
| web-api-architecture | 307 | `api-contracts-clients-and-networking`, `web-interfaces-and-application-frameworks` |
| cloud-infra-devops | 305 | `infrastructure-as-code-and-cloud-native-operations`, `cloud-infrastructure-and-deployment` |
| media-games-docs | 234 | `game-creation-assets-and-automation`, `graphics-multimedia-scientific-and-geospatial`, `documents-ocr-and-file-formats` |
| data | 222 | `databases-data-access-and-analytics`, `data-science-and-engineering-tools` |
| desktop-mobile | 184 | `desktop-mobile-and-device-sdks`, `android-apk-development-and-analysis` |
| operations-tools | 175 | `observability-debugging-and-operations`, `search-messaging-and-durable-work` |
| design-ux | 162 | `design-systems-and-design-engineering`, `ui-design-inspiration-and-reference` |
| security | 154 | `security-identity-and-supply-chain`, `security-testing-defense-and-supply-chain-assurance` |
| testing-quality | 135 | `test-automation-and-quality-engineering`, `testing-verification-and-performance` |
| foundations | 19 | `software-engineering-foundations-and-standards`, `standards-and-discovery` |

Full category list with counts: `categories/README.md` or `llms.txt`.
Human-readable category pages: `categories/<category_id>.md`.
Long-form catalogs with provenance and cautions: `catalogs/`.

## Machine-readable entry points

| File | What it is |
|---|---|
| `resources.json` | canonical records: identity, purpose, source, check date, review scope, facets |
| `resources.csv` | lossless tabular export of the same records |
| `index/resources.compact.json` | every record, shortlisting fields only (~35% of canonical size) |
| `index/by-category/<category_id>.json` | one category's compact records |
| `index/categories.json` | category IDs, titles, counts, paths, membership |
| `index/category-groups.json` | the 13 domains with counts and category IDs |
| `index/catalog-stats.json` | generated counts, rollups, source and type breakdowns |
| `index/resource-schema.json` | the record contract |
| `index/taxonomy.json` | the controlled facet vocabulary |
| `llms.txt` | compact navigation index |
| `llms-full.txt` | every category page and catalog in one file |

## Do not use

`archive/legacy-template/` holds generated placeholder manifests and an
old index describing files that never existed. Never cite or merge it.
