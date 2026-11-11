# Software engineering foundations and standards

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Verify current upstream documentation, supported versions, license, security, and fit before adoption; catalog checks are not adoption audits.

| Resource | Useful for / constraints |
|---|---|

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Specifications and written conventions rather than libraries, kept together because they define how a repository communicates versioning, licensing, decisions, documentation, and conduct. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [Architecture Decision Records](https://adr.github.io/) | Practices and templates for recording architectural decisions with context and consequences. Cheap to adopt; value comes from writing them at decision time, not retroactively. |
| [C4 model](https://c4model.com/) | Hierarchical approach to architecture diagrams: context, container, component, code. Notation- and tool-independent, which helps when diagrams must survive tool changes. |
| [Choose a License](https://choosealicense.com/) | Short decision guide to common open-source licenses and what happens with none. Guidance, not legal advice; confirm obligations with counsel for commercial or mixed-license projects. |
| [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) | Widely adopted code of conduct with enforcement guidelines. Fill in the reporting contact and review the enforcement section before publishing it. |
| [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) | Commit-message specification (feat/fix/scope/!) that maps to SemVer and enables automated changelogs and releases. Requires team agreement and a linter to be worth anything. |
| [Diátaxis](https://diataxis.fr/) | Documentation framework separating tutorials, how-to guides, reference, and explanation. Useful structure test for docs that mix four different reader needs into one page. |
| [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) | Convention for human-readable CHANGELOG.md files grouped by Added/Changed/Deprecated/Removed/Fixed/Security. Pairs naturally with SemVer; it rejects raw commit-log dumps as changelogs. |
| [REUSE Specification](https://reuse.software/spec-3.3/) | File-level licensing metadata via SPDX headers and a LICENSES/ directory, plus a linting tool. Makes per-file provenance auditable in mixed-license repositories. |
| [Semantic Versioning](https://semver.org/) | Version-numbering rules (MAJOR.MINOR.PATCH) that let tools and consumers infer compatibility. A specification, not a release policy: it only means something once your project declares what its public API is. |
| [SPDX License List](https://spdx.org/licenses/) | Canonical short identifiers, names, and license texts used in package metadata and SBOMs. Use SPDX IDs in manifests instead of free-text license names. |
| [The Twelve-Factor App](https://12factor.net/) | Methodology for portable, operable services: config in the environment, stateless processes, logs as streams. Guidance from the Heroku era; some factors need reinterpretation for serverless and Kubernetes. |
<!-- expansion-2026-11-10:end -->
