# AI index — fastest path through this repository

This repository is a curated pointer library: 2,202 entries, 2,198 distinct
URLs, 97 categories. It contains references and original notes, not
third-party code. Entries are discovery hints, not endorsements — verify
maintenance, license, and compatibility at the primary source.

## Read in this order (smallest first)

1. **This file** — pick a domain below.
2. **`index/category-groups.json`** — the 97 categories rolled up into
   12 domains, with counts and category IDs.
3. **One category shard** — `index/by-category/<category_id>.json` holds
   only that category's records (name, URL, purpose, facets). Most shards
   are a few KB; load one, not the whole catalog.
4. **Only if you need provenance** — `resources.json` is the canonical
   full catalog (2.3 MB, adds source, check date, review notes per record).
   `index/resources.compact.json` is the same catalog at ~38% of the size
   when you genuinely need every category at once.

Single-file alternative: `llms-full.txt` concatenates every category page and catalog for one-shot ingestion.
Local alternative: `python scripts/search.py "your query"` with
`--topic`, `--type`, `--use-case`, `--language`, or `--platform` filters.

## Domains

| Domain | Resources | Start with |
|---|---|---|
| ai | 343 | `ai-mcp-servers-and-tool-use`, `ai-machine-learning-and-local-inference`, `ai-agent-frameworks-and-orchestration` |
| windows | 232 | `windows-native-libraries`, `windows-diagnostics`, `windows-desktop-ui` (47 small Windows categories — most hold under 10 entries) |
| languages-runtimes | 328 | `python-rust-and-go-building-blocks`, `languages-and-runtimes`, `niche-language-ecosystems` |
| web-api-architecture | 245 | `api-contracts-clients-and-networking`, `web-interfaces-and-application-frameworks` |
| cloud-infra-devops | 211 | `infrastructure-as-code-and-cloud-native-operations`, `cloud-infrastructure-and-deployment` |
| security | 143 | `security-identity-and-supply-chain`, `security-testing-defense-and-supply-chain-assurance` |
| data | 141 | `databases-data-access-and-analytics`, `data-science-and-engineering-tools` |
| design-ux | 125 | `design-systems-and-design-engineering`, `ui-design-inspiration-and-reference` |
| media-games-docs | 125 | `game-creation-assets-and-automation`, `documents-ocr-and-file-formats`, `world-of-warcraft-addon-development` |
| desktop-mobile | 121 | `android-apk-development-and-analysis`, `desktop-mobile-and-device-sdks` |
| testing-quality | 109 | `test-automation-and-quality-engineering`, `testing-verification-and-performance` |
| operations-tools | 79 | `observability-debugging-and-operations`, `backup-storage-transfer-and-resilience` |

Full category list with counts: `categories/README.md` or `llms.txt`.
Human-readable category pages: `categories/<category_id>.md`.
Long-form catalogs with provenance and cautions: `catalogs/`.

## Do not use

`archive/legacy-template/` holds generated placeholder manifests and an
old index describing files that never existed. Never cite or merge it.
