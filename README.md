# Useful Development Resources

A project-aware resource library for developers and their AI assistants, curated by Sean Shaffer. Find useful repositories, SDKs, APIs, libraries, diagnostics, build tools, and deployment resources for the work you are actually doing.

**2202 catalog entries · 2198 distinct URLs · 97 purpose-based categories.** Includes 459 general resources, 232 Windows repositories, 301 AI resources, 200 development resources added 2026-10-23, two 500-resource development expansions added 2026-10-27, and 10 user-requested design-reference links. Entries overlap; distinct URLs do not necessarily mean distinct projects.

## Point your AI here

Copy this into your coding assistant:

> Use https://github.com/SeanShaffer88/ForAI as a resource reference for my project. Read its AGENTS.md and categories/README.md, then inspect only relevant categories. My project is: [describe the goal, existing stack, target platforms, and constraints]. Recommend a focused shortlist, explain why each resource fits, compare alternatives, and verify current upstream maintenance, licensing, compatibility, and integration requirements. Link your evidence and identify anything unverified. Do not install or change my project merely because a resource is listed.

An assistant needs browsing, repository access, or a downloaded copy to read these files. A link alone does not give it persistent memory or automatic access. If it cannot follow repository links, provide [AGENTS.md](AGENTS.md) and the relevant category files directly.

## Explore

- [Dev Resource Explorer](https://seanshaffer88.github.io/dev-resource-explorer/): search the catalog, filter discovery topics, save resources in your browser, and read the original research notes. Uses a reviewed snapshot; [application source and releases](https://github.com/SeanShaffer88/dev-resource-explorer).
- [Browse all categories](categories/README.md): links grouped by purpose, with practical notes.
- [UI design inspiration and reference](catalogs/design-inspiration-resources.md): visual research and interface discovery links, with usage cautions.
- [General development catalog](catalogs/software-development-resources.md): platform SDKs, languages, web, mobile, APIs, data, AI, testing, infrastructure, security, and more.
- [AI resources expansion](catalogs/ai-resources-expansion.md): toolchains, MCP servers and SDKs, agent frameworks, local inference, model providers, retrieval, evaluation, coding agents, and learning references, added 2026-10-23.
- [Development resources expansion (2026-10-23)](catalogs/development-expansion-2026-10-23.md): 200 additions across 18 existing categories, with scoped source checks.
- [Software development expansion (2026-10-27)](catalogs/development-expansion-2026-10-27.md): 500 additional tools and references across implementation, design, testing, security, infrastructure, and more; includes evidence limits and a metadata snapshot.
- [Niche software development expansion (2026-10-27, round 2)](catalogs/development-expansion-2026-10-27-round-2.md): 500 curated additions emphasizing specialized languages, test automation, infrastructure, architecture, design systems, data science, and security; includes the metadata snapshot and verification limits.
- [Windows development catalog](catalogs/windows-development-repositories.md): native APIs, interop, DLLs, diagnostics, UI, graphics, devices, build and packaging, plus revival candidates.
- [Windows revival backlog](catalogs/windows-development-todo.md): historical WR-001 through WR-010 snapshot, including completed win-pipe work and Microsoft IPC development status.
- [JSON catalog](resources.json) / [CSV export](resources.csv): all entries with stable IDs, typed facets, and provenance.
- [Resource schema](index/resource-schema.json) / [facet taxonomy](index/taxonomy.json): the current record and facet contract.
- [Generated category index](index/categories.json): category IDs, counts, paths, and resource membership.
- [llms.txt](llms.txt): AI-readable index of the whole library.
- [AI selection workflow](AGENTS.md) and [contribution guide](CONTRIBUTING.md).

- [Android APK development and analysis](docs/android-apk-development.md): build, decode/rebuild, signing, engines, offline preservation and diagnostics; includes a read-only inventory script.

- [Game creation, assets and automation](categories/game-creation-assets-and-automation.md): engine/MCP tools, asset sources, music authoring and Android QA.

## Search locally

Requires Python 3, with no third-party packages:

```sh
python scripts/search.py "named pipes"
python scripts/search.py "testing" --category Windows --topic testing
python scripts/search.py "SQLite" --type repository --limit 10
python scripts/search.py "browser test" --use-case test-and-verify-software --json
python scripts/export_csv.py       # after editing resources.json
python scripts/generate_indexes.py # after changing catalog categories/resources
python scripts/validate.py
python -m unittest discover -s tests -v
```

Search requires every query term to match a descriptive field or curated facet, then ranks name matches above purpose, category, and facet matches. Review/status/provenance boilerplate is excluded. Exact facet filters include `--topic`, `--type`, `--use-case`, `--language`, and `--platform`; `--category` is a category-name substring. Search is a local discovery aid, not a suitability, freshness, or security audit.

## Evidence and provenance

Imported from Sean's saved research on October 21, 2026. Original purpose, maintenance, evidence, and revival notes are retained in the full catalogs; local machine paths have been removed. Index category pages are derived from those collections. Search and HTTP checks recorded in the research are historical observations, not fresh audits or guarantees of maintenance, security, license suitability, or compatibility. The index `checked_on` date refers to the research snapshot and must be interpreted alongside `review`; Windows entries were not all individually rechecked that day. Some resources are official documentation or service APIs rather than GitHub repositories.

Archived or dormant projects can remain useful for a specific requirement. Compare alternatives and the cost of owning a fork before adopting one. Listing a service does not connect an account or authorize access. This repository contains references and original notes, not third-party project source code.

The [October 23 development expansion](catalogs/development-expansion-2026-10-23.md) records its own metadata/README checks and limits; it does not upgrade the evidence level of older entries.

Original catalog prose and tooling are available under [MIT](LICENSE). Referenced projects, documentation, APIs, data, and trademarks retain their own licenses and terms. No scheduled monitoring is implied.
