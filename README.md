# Useful Development Resources

A project-aware resource library for developers and their AI assistants, curated by Sean Shaffer. Find useful repositories, SDKs, APIs, libraries, diagnostics, build tools, and deployment resources for the work you are actually doing.

**690 catalog entries · 686 distinct URLs · 77 purpose-based categories.** Includes the complete saved collections of 458 general resources and 232 Windows repositories. Entries overlap; distinct URLs do not necessarily mean distinct projects.

## Point your AI here

Copy this into your coding assistant:

> Use https://github.com/SeanShaffer88/useful-dev-resources as a resource reference for my project. Read its AGENTS.md and categories/README.md, then inspect only relevant categories. My project is: [describe the goal, existing stack, target platforms, and constraints]. Recommend a focused shortlist, explain why each resource fits, compare alternatives, and verify current upstream maintenance, licensing, compatibility, and integration requirements. Link your evidence and identify anything unverified. Do not install or change my project merely because a resource is listed.

An assistant needs browsing, repository access, or a downloaded copy to read these files. A link alone does not give it persistent memory or automatic access. If it cannot follow repository links, provide [AGENTS.md](AGENTS.md) and the relevant category files directly.

## Explore

- [Dev Resource Explorer](https://seanshaffer88.github.io/dev-resource-explorer/): search the catalog, filter discovery topics, save resources in your browser, and read the original research notes. Uses a reviewed snapshot; [application source and releases](https://github.com/SeanShaffer88/dev-resource-explorer).
- [Browse all categories](categories/README.md): links grouped by purpose, with practical notes.
- [General development catalog](catalogs/software-development-resources.md): platform SDKs, languages, web, mobile, APIs, data, AI, testing, infrastructure, security, and more.
- [Windows development catalog](catalogs/windows-development-repositories.md): native APIs, interop, DLLs, diagnostics, UI, graphics, devices, build and packaging, plus revival candidates.
- [Windows revival backlog](catalogs/windows-development-todo.md): historical WR-001 through WR-010 snapshot, including completed win-pipe work and Microsoft IPC development status.
- [JSON index](resources.json) / [CSV index](resources.csv): all entries for searching or ingestion.
- [AI selection workflow](AGENTS.md) and [contribution guide](CONTRIBUTING.md).

- [Android APK development and analysis](docs/android-apk-development.md): build, decode/rebuild, signing, engines, offline preservation and diagnostics; includes a read-only inventory script.

- [Game creation, assets and automation](categories/game-creation-assets-and-automation.md): engine/MCP tools, asset sources, music authoring and Android QA.

## Search locally

Requires Python 3, with no third-party packages:

```sh
python scripts/search.py "named pipes"
python scripts/search.py "testing" --category Windows
python scripts/search.py "SQLite" --json
python scripts/validate.py
```

Search matches words across names, categories, URLs, and notes. Use shorter queries for broader results. It is a discovery tool, not a ranking or suitability engine.

## Evidence and provenance

Imported from Sean's saved research on October 21, 2026. Original purpose, maintenance, evidence, and revival notes are retained in the full catalogs; local machine paths have been removed. Index category pages are derived from those collections. Search and HTTP checks recorded in the research are historical observations, not fresh audits or guarantees of maintenance, security, license suitability, or compatibility. The index `checked_on` date refers to the research snapshot and must be interpreted alongside `review`; Windows entries were not all individually rechecked that day. Some resources are official documentation or service APIs rather than GitHub repositories.

Archived or dormant projects can remain useful for a specific requirement. Compare alternatives and the cost of owning a fork before adopting one. Listing a service does not connect an account or authorize access. This repository contains references and original notes, not third-party project source code.

Original catalog prose and tooling are available under [MIT](LICENSE). Referenced projects, documentation, APIs, data, and trademarks retain their own licenses and terms. No scheduled monitoring is implied.
