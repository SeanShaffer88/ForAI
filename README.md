# Useful Development Resources

## TL;DR

A curated pointer library of **2,937 development resources** — repositories, SDKs, APIs, libraries, tools, standards, and long-form references — organized into **101 purpose-based categories** and **13 domains**, built so an AI assistant can find the right resource for a project without reading the whole library.

**AI assistants: start with [AI_INDEX.md](AI_INDEX.md).** It is one page, maps a task to the few category files worth opening, and lists the machine-readable entry points. If you need a single file to ingest, use [llms-full.txt](llms-full.txt); if you need structured data, load one shard from `index/by-category/`.

<!-- BEGIN GENERATED STATS -->
**2,937 catalog entries** · **2,931 distinct URLs** · **101 categories** · **13 domains** · **2,328 project identities**
<!-- END GENERATED STATS -->

Those numbers are generated from `resources.json` by `scripts/catalog_stats.py --write`, never hand-edited. Entries overlap: a project can appear once per interface or audience, so distinct URLs do not mean distinct projects.

## Point your AI here

Copy this into your coding assistant:

> Use https://github.com/SeanShaffer88/ForAI as a resource reference for my project. Read its AGENTS.md and AI_INDEX.md, then open only the categories relevant to my task. My project is: [describe the goal, existing stack, target platforms, and constraints]. Recommend a focused shortlist, explain why each resource fits, compare alternatives, and verify current upstream maintenance, licensing, compatibility, and integration requirements. Link your evidence and identify anything unverified. Do not install or change my project merely because a resource is listed.

An assistant needs browsing, repository access, or a downloaded copy to read these files. A link alone does not give it persistent memory or automatic access. If it cannot follow repository links, provide [AI_INDEX.md](AI_INDEX.md) and the relevant category files directly, or hand it `index/resources.compact.json`.

## Reading paths

| You want | Open | Size |
|---|---|---|
| Task → category map, in one page | [AI_INDEX.md](AI_INDEX.md) | 3 KB |
| Everything, one shot, for a long-context model | [llms-full.txt](llms-full.txt) | 1.8 MB |
| All records, shortlisting fields only | [index/resources.compact.json](index/resources.compact.json) | 1.2 MB (35% of canonical) |
| One topic | `index/by-category/<category_id>.json` or `categories/<category_id>.md` | 1–30 KB |
| Counts and rollups | [index/catalog-stats.json](index/catalog-stats.json), [index/category-groups.json](index/category-groups.json) | small |
| Provenance for one record | [resources.json](resources.json) | 3.3 MB |
| Spreadsheet / SQL import | [resources.csv](resources.csv) | 1.6 MB |

Every artifact above is derived from `resources.json` by a script in `scripts/`. Nothing is hand-maintained twice.

## Explore

- [Dev Resource Explorer](https://seanshaffer88.github.io/dev-resource-explorer/): search the catalog, filter discovery topics, save resources in your browser, and read the original research notes. Uses a reviewed snapshot; [application source and releases](https://github.com/SeanShaffer88/dev-resource-explorer).
- [Browse all categories](categories/README.md): links grouped by purpose, with practical notes.
- [UI design inspiration and reference](catalogs/design-inspiration-resources.md): visual research and interface discovery links, with usage cautions.
- [General development catalog](catalogs/software-development-resources.md): platform SDKs, languages, web, mobile, APIs, data, AI, testing, infrastructure, security, and more.
- [AI resources expansion](catalogs/ai-resources-expansion.md): toolchains, MCP servers and SDKs, agent frameworks, local inference, model providers, retrieval, evaluation, coding agents, and learning references.
- [Development resources expansion (2026-10-23)](catalogs/development-expansion-2026-10-23.md): 200 additions across 18 existing categories, with scoped source checks.
- [Software development expansion (2026-10-27)](catalogs/development-expansion-2026-10-27.md): 500 additional tools and references across implementation, design, testing, security, infrastructure, and more.
- [Niche software development expansion (2026-10-27, round 2)](catalogs/development-expansion-2026-10-27-round-2.md): 500 curated additions emphasizing specialized languages, test automation, infrastructure, architecture, design systems, data science, and security.
- [Software engineering foundations expansion (2026-11-10)](catalogs/expansion-2026-11-10.md): 82 additions covering versioning, changelogs, commit conventions, licensing, decision records, documentation structure, codes of conduct, plus the mainstream browser-test and unit-test frameworks and everyday API clients.
- [Topic and hidden-gem expansion (2026-11-11)](catalogs/expansion-2026-11-11.md): 653 additions found through GitHub topic search, [gittrend.io/hidden-gems](https://gittrend.io/hidden-gems), and [awesomehub.js.org](https://awesomehub.js.org/): AI agent skills and memory, MCP servers and clients, guardrails and red teaming, reverse-engineering tooling, ORMs and database servers, message queues, OpenTelemetry SDKs, i18n, OCR and document extraction, editor ecosystems, .NET application blocks, and Android libraries.
- [Windows development catalog](catalogs/windows-development-repositories.md): native APIs, interop, DLLs, diagnostics, UI, graphics, devices, build and packaging, plus revival candidates.
- [Windows revival backlog](catalogs/windows-development-todo.md): historical WR-001 through WR-010 snapshot.
- [JSON catalog](resources.json) / [CSV export](resources.csv): all entries with stable IDs, typed facets, and provenance.
- [Resource schema](index/resource-schema.json) / [facet taxonomy](index/taxonomy.json): the current record and facet contract.
- [Generated category index](index/categories.json): category IDs, counts, paths, and resource membership.
- [llms.txt](llms.txt): AI-readable navigation index of the whole library.
- [AI selection workflow](AGENTS.md) and [contribution guide](CONTRIBUTING.md).

## Search locally

Requires Python 3, with no third-party packages:

```sh
python scripts/search.py "named pipes"
python scripts/search.py "testing" --category Windows --topic testing
python scripts/search.py "SQLite" --type repository --limit 10
python scripts/search.py "browser test" --use-case test-and-verify-software --json

# Regenerate everything after a catalog edit, in this order:
python scripts/enrich_resources.py --apply   # IDs and facets for new records
python scripts/export_csv.py                 # resources.csv
python scripts/generate_indexes.py           # categories/README.md, index/categories.json, llms.txt nav
python scripts/generate_ai_views.py          # compact catalog, shards, domain rollup, llms-full.txt
python scripts/catalog_stats.py --write      # index/catalog-stats.json + the counts below
python scripts/validate.py                   # offline consistency gate
python -m unittest discover -s tests -v
```

`scripts/catalog_stats.py --check` fails when a quoted count drifts, and `scripts/validate.py` covers schema conformity, stable IDs, related-link symmetry, category coverage, CSV/JSON agreement, generated navigation, and local Markdown links. Neither script touches the network; reachability is the separate, opt-in `scripts/link_check.py`.

Search requires every query term to match a descriptive field or curated facet, then ranks name matches above purpose, category, and facet matches. Exact facet filters: `--topic`, `--type`, `--use-case`, `--language`, `--platform`; `--category` is a category-name substring. Search is a local discovery aid, not a suitability, freshness, or security audit.

## Evidence and provenance

Imported from Sean's saved research on October 21, 2026, and extended in dated, self-describing batches. Every batch records what was actually checked: `source` names the batch, `checked_on` the date, `review` the scope of the check, and `verification_level` the strength of the evidence. Per-entry evidence for the larger batches lives in `docs/*-checks.json` (repository IDs, licenses as detected by GitHub, topics, and last push at check time).

That is metadata and reachability evidence only. It is not a README review, release or maintenance audit, licensing opinion, security assessment, compatibility test, or adoption recommendation. Local machine paths have been removed. Archived or dormant projects can remain useful for a specific requirement; compare alternatives and the cost of owning a fork before adopting one. Listing a service does not connect an account or authorize access. This repository contains references and original notes, not third-party project source code.

Original catalog prose and tooling are available under [MIT](LICENSE). Referenced projects, documentation, APIs, data, and trademarks retain their own licenses and terms. The monthly link-check workflow opens an issue with its findings; it does not validate suitability or keep entries current.
