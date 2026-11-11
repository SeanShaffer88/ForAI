# Expansion — 2026-11-10

**82 additions across 20 categories (1 new category).** A verification-first
pass: every GitHub entry was checked through the GitHub REST repository
endpoint on 2026-11-10 (HTTP 200), and every documentation entry was fetched on the
same date. That is reachability and metadata evidence only — **not** a README
review, release or maintenance audit, licensing opinion, security assessment,
compatibility test, or adoption recommendation.

Why these entries: the catalog was strong on breadth but had gaps where a
developer starts a project rather than finishes one. Missing pieces this pass
adds include the mainstream browser-test and unit-test frameworks (Cypress,
Selenium, WebdriverIO, Jest, Robot Framework), everyday HTTP and mocking
clients, the editors and shells people actually use, Windows package managers,
GitHub Actions and Git workflows, Kubernetes operating tools, secrets
management, AI-supply-chain security, the observability and BI tools most teams
reach for, and the written conventions that keep a repository coherent —
versioning, changelogs, commit messages, licensing, decision records, docs
structure, and codes of conduct.

The new category is [Software engineering foundations and standards](../categories/software-engineering-foundations-and-standards.md):
specifications and conventions (SemVer, Conventional Commits, Keep a Changelog,
REUSE, SPDX, Twelve-Factor, C4, Diátaxis) that are not libraries and do not fit
a technology bucket.

## Evidence and limits

- **Scope of each entry:** the `review` field in `resources.json` records exactly
  what was checked, with the repository id or page URL in
  [`docs/expansion-2026-11-10-checks.json`](../docs/expansion-2026-11-10-checks.json).
- **GitHub entries** use the REST repository endpoint: repository id, detected
  license, primary language, topics, archive/fork flags, and last push. GitHub
  license detection is often `NOASSERTION`; where a license matters for
  redistribution the individual entry says so and you must read the license.
- **Documentation entries** were fetched and summarized from the page as
  published. That check does not extend to future versions of the page.
- **No package was installed, no build was run, and no service was exercised.**
  Star counts and push timestamps are time-bound signals, not quality scores.
- Dual-use security tools in this list (fuzzers, scanners, forensics, NDR) are
  for systems and data you own or are explicitly authorized to assess.
- Several entries are deliberately *not* recommended: they are listed with
  their real trade-off (license restrictions, hosted dependency, operational
  weight) so you can decide. A catalog entry is not an endorsement.

## How to use this page

Read the category heading, then the entry's constraint sentence. If a
constraint conflicts with your project (for example an AGPL component in a
closed product, or a hosted service where you need self-hosting), stop there
and look at the alternative named in the same row instead of adopting first and
discovering the problem later.

| Category | Additions |
|---|---|
| Software engineering foundations and standards | 11 |
| Testing verification and performance | 5 |
| API contracts clients and networking | 3 |
| Language tooling and repository automation | 8 |
| Builds packages and environments | 6 |
| CI version control and releases | 4 |
| Cloud infrastructure and deployment | 5 |
| Infrastructure as code and cloud-native operations | 7 |
| Feature flags configuration and secrets | 1 |
| Security identity and supply chain | 1 |
| Security testing, defense, and supply-chain assurance | 10 |
| Observability debugging and operations | 4 |
| Databases data access and analytics | 2 |
| Data science and engineering tools | 5 |
| AI coding agents and assistants | 1 |
| AI MCP servers and tool use | 1 |
| Web interfaces and application frameworks | 2 |
| Graphics multimedia scientific and geospatial | 1 |
| Game creation assets and automation | 1 |
| Windows / Binary tooling additions | 4 |

## Software engineering foundations and standards

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

## Testing verification and performance

| Resource | Useful for / constraints |
|---|---|
| [Cypress](https://github.com/cypress-io/cypress) | Browser end-to-end and component testing with time-travel debugging and an interactive runner. Great developer experience; Cypress-specific architecture and per-seat cloud pricing are trade-offs against WebDriver-based suites. |
| [Jest](https://github.com/jestjs/jest) | JavaScript and TypeScript unit testing with snapshots, fake timers, and built-in coverage. CJS/ESM interop and transform configuration are the usual friction points; Vitest is the common Vite-native alternative. |
| [Robot Framework](https://github.com/robotframework/robotframework) | Keyword-driven acceptance testing and RPA with a plain-text syntax and a large library ecosystem. Strong for cross-team readable tests; less natural for developer-first unit-level TDD. |
| [Selenium](https://github.com/seleniumhq/selenium) | WebDriver implementations and Grid for browser automation in Java, Python, JavaScript, .NET, Ruby, and Rust. The W3C-protocol baseline with the widest browser and language coverage; you assemble the test framework yourself. |
| [WebdriverIO](https://github.com/webdriverio/webdriverio) | Node.js test framework on WebDriver and Chrome DevTools protocols, with runner, assertions, and mobile support. Choose it when you want a batteries-included JS suite that can also drive native apps. |

## API contracts clients and networking

| Resource | Useful for / constraints |
|---|---|
| [Hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open-source API client for REST, GraphQL, WebSocket, SSE, and MQTT in the browser or self-hosted. Test and debug requests without an account depending on deployment; check self-hosted feature limits. |
| [Mockoon](https://github.com/mockoon/mockoon) | Desktop and CLI mock servers defined from OpenAPI or hand-built routes, with templating and proxy mode. Useful for offline and CI work where hosted mocks are not acceptable. |
| [xh](https://github.com/ducaale/xh) | Fast HTTP client CLI with HTTPie-style syntax, translating to familiar curl-like flags. Small single binary for scripts and containers; check auth and multipart coverage against your needs. |

## Language tooling and repository automation

| Resource | Useful for / constraints |
|---|---|
| [difftastic](https://github.com/Wilfred/difftastic) | Structural diff that parses supported languages with tree-sitter and reports syntax-aware changes. Reduces noise in refactors; language coverage and speed differ from line diffs. |
| [Helix](https://github.com/helix-editor/helix) | Modal editor with multiple selections and built-in LSP/DAP, configured through files rather than plugins. MPL-2.0; plugin story is thinner than Neovim's. |
| [lazygit](https://github.com/jesseduffield/lazygit) | Terminal UI for staging, rebasing, bisecting, and resolving conflicts. Faster than memorising plumbing for many daily flows; long-running operations can be harder to script. |
| [Neovim](https://github.com/neovim/neovim) | Vim-fork editor with Lua configuration, a built-in LSP client, and a remote plugin API. Apache-2.0 plus Vim-license portions; verify the license mix before redistributing a bundled build. |
| [tmux](https://github.com/tmux/tmux) | Terminal multiplexer for persistent sessions, panes, and remote pair work. Indispensable over SSH; runs under WSL or MSYS rather than natively on Windows. |
| [Visual Studio Code](https://github.com/microsoft/vscode) | Source for the editor that most extensions target, useful when you need extension APIs or behavior details. Distributed binaries carry Microsoft's license terms even though the repository is MIT. |
| [Zed](https://github.com/zed-industries/zed) | Rust GPU-accelerated editor with collaborative editing, LSP, and agent panels. Dual Apache-2.0/GPL-3.0 files and platform coverage that moves quickly; confirm licensing for anything you redistribute. |
| [zoxide](https://github.com/ajeetdsouza/zoxide) | Smarter cd command with a frecency-ranked directory database for bash, zsh, fish, PowerShell, and Nushell. Small binary; ranking data is per-user and disposable. |

## Builds packages and environments

| Resource | Useful for / constraints |
|---|---|
| [asdf](https://github.com/asdf-vm/asdf) | Pluggable version manager for many runtimes through one `.tool-versions` file. Compare with mise for speed and task running; plugin quality and Windows support vary. |
| [Chocolatey](https://github.com/chocolatey/choco) | Machine-wide Windows package manager using NuGet-style packages and PowerShell scripts. Apache-2.0 for the client; review package scripts and licensing before installing with elevated rights. |
| [conda](https://github.com/conda/conda) | Cross-language binary package and environment manager, historically important for scientific and native Python stacks. BSD-3-Clause; channel and solver choice materially change reproducibility. |
| [Devbox](https://github.com/jetify-com/devbox) | Reproducible per-project development shells built on Nix, with a JSON manifest and lockfile. Nice ergonomics; the Nix store is a real dependency and Windows support is not native. |
| [Poetry](https://github.com/python-poetry/poetry) | Python dependency management and packaging with lockfiles and a pyproject-based workflow. Compare against uv and pip-tools for speed and lock resolution policy; both formats differ. |
| [Scoop](https://github.com/ScoopInstaller/Scoop) | User-scope Windows package manager driven by Git manifests, requiring no administrator rights. Convenient for developer tooling; per-user installs and manifest freshness differ from winget or Chocolatey. |

## CI version control and releases

| Resource | Useful for / constraints |
|---|---|
| [act](https://github.com/nektos/act) | Run GitHub Actions workflows locally in containers to iterate on CI changes. Emulation is close but not identical to hosted runners; secrets, services, and matrix specifics can differ. |
| [Dagger](https://github.com/dagger/dagger) | Container-native pipelines defined in code, run locally or in CI with content-addressed caching. Solves CI lock-in and caching; requires container runtime and a real migration of existing pipelines. |
| [Git LFS](https://github.com/git-lfs/git-lfs) | Large-file storage extension that replaces big binaries with pointer files. Needed for game/ML assets; hosting quotas, mirroring, and clone behavior must be planned. |
| [GitHub CLI](https://github.com/cli/cli) | Official `gh` client covering pull requests, issues, releases, Actions, and the API. Scriptable with `--json` and `--jq`; token scopes determine what it can read or change. |

## Cloud infrastructure and deployment

| Resource | Useful for / constraints |
|---|---|
| [Backstage](https://github.com/backstage/backstage) | Framework for internal developer portals: software catalog, templates, and docs with plugins. Powerful and heavy; budget for upgrade churn and a dedicated owner. |
| [Dokploy](https://github.com/Dokploy/dokploy) | Self-hosted PaaS for deploying apps and databases over Docker with backups and a UI. Source is Apache-2.0 with a proprietary directory; read the license before offering it as a service. |
| [Encore](https://github.com/encoredev/encore) | Go/TypeScript backend framework and CLI that derives infrastructure from application code and provisions it locally or in your cloud. MPL-2.0; it is an opinionated platform, not a library you adopt partially. |
| [flyctl](https://github.com/superfly/flyctl) | CLI for deploying and operating apps and machines on Fly.io. Hosted platform with account and billing requirements; keep deployment state out of repositories. |
| [SST](https://github.com/sst/sst) | TypeScript framework for deploying full-stack apps on your own cloud account, now centered on its own infra primitives. Fast iteration; check which version and provider model the docs describe. |

## Infrastructure as code and cloud-native operations

| Resource | Useful for / constraints |
|---|---|
| [Atlantis](https://github.com/runatlantis/atlantis) | Pull-request automation for Terraform: plan on change, apply on approval. Adds a privileged service to secure and operate; scope credentials per repository. |
| [Conftest](https://github.com/open-policy-agent/conftest) | Write Rego policy tests against configuration files and manifests, runnable in CI. Policy coverage is yours to build; start with a small set of high-value rules. |
| [Infracost](https://github.com/infracost/infracost) | Cloud cost estimates for Terraform and related IaC changes, usable as a pull-request check. Pricing data and free-tier limits come from a hosted service. |
| [k9s](https://github.com/derailed/k9s) | Terminal UI for browsing and operating Kubernetes clusters. Fast for live debugging; write actions still need RBAC and review discipline. |
| [kubeconform](https://github.com/yannh/kubeconform) | Validates Kubernetes manifests against schemas, including custom resources. Catches typos and version drift in CI; it does not check cluster state or policy. |
| [kubectx and kubens](https://github.com/ahmetb/kubectx) | Fast context and namespace switching for kubectl, with fzf integration. Reduces wrong-cluster mistakes only if the prompt is also labeled. |
| [stern](https://github.com/stern/stern) | Multi-pod and multi-container log tailing for Kubernetes with regex selectors. Useful during rollouts; output is unstructured unless you add formatting. |

## Feature flags configuration and secrets

| Resource | Useful for / constraints |
|---|---|
| [HashiCorp Vault](https://github.com/hashicorp/vault) | Secrets management, dynamic credentials, encryption as a service, and PKI. Business Source License since 2023 with OpenBao as the open fork; evaluate licensing before embedding it in a product. |

## Security identity and supply chain

| Resource | Useful for / constraints |
|---|---|
| [Cosign](https://github.com/sigstore/cosign) | Sign and verify container images and artifacts, with keyless OIDC signing and transparency-log evidence. Signature verification only proves provenance for keys you trust; define that policy first. |

## Security testing, defense, and supply-chain assurance

| Resource | Useful for / constraints |
|---|---|
| [Bandit](https://github.com/PyCQA/bandit) | AST-based Python security linter for common unsafe patterns. Fast CI gate; tune the profile or it will drown you in low-signal findings. |
| [DefectDojo](https://github.com/DefectDojo/django-DefectDojo) | Vulnerability management and AppSec orchestration: import scanner findings, deduplicate, track remediation. Operationally non-trivial to self-host, and data quality depends on consistent imports. |
| [ffuf](https://github.com/ffuf/ffuf) | Fast HTTP fuzzer for content discovery and parameter testing with flexible filters. Dual-use: only run it against systems you own or are explicitly authorized to test. |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | Checks whether Kubernetes nodes and control-plane components match CIS benchmark recommendations. Requires cluster access and produces configuration findings, not exploitability proof. |
| [Kubescape](https://github.com/kubescape/kubescape) | Kubernetes posture scanning against NSA/CISA and MITRE frameworks for clusters, manifests, and images. Scans are a starting point; triage roles and exceptions explicitly. |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Free, lab-based training on injection, access control, request smuggling, and LLM attacks. Labs are hosted targets; do not reproduce the techniques against systems you do not own or have written authorization to test. |
| [Suricata](https://github.com/OISF/suricata) | IDS/IPS engine with rule-based detection, protocol parsing, and PCAP output. GPL-2.0; rule sources and false-positive tuning determine whether it is useful. |
| [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Memory-forensics framework for analyzing RAM captures with a plugin architecture and symbol tables. The license is source-available (Volatility Software License), not OSI-approved; confirm terms before redistribution. |
| [Wazuh](https://github.com/wazuh/wazuh) | Open-source XDR/SIEM platform: log analysis, file integrity monitoring, compliance checks, and response. GPL-2.0 core with separate agent licensing details; expect real operational work to run it. |
| [Zeek](https://github.com/zeek/zeek) | Network security monitor that turns traffic into structured logs and events. Deep analysis requires sensor placement and storage planning; licensing mixes BSD-style terms with the University of California notice. |

## Observability debugging and operations

| Resource | Useful for / constraints |
|---|---|
| [lnav](https://github.com/tstack/lnav) | Terminal log viewer with SQL queries, time-shifted merges of multiple files, and format detection. Excellent for incident archaeology on local logs; Windows builds run under WSL or MSYS. |
| [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) | Vendor-neutral agent and gateway for receiving, processing, and exporting telemetry. Configure sampling, memory limits, and batching deliberately; it is infrastructure, not a library. |
| [SigNoz](https://github.com/SigNoz/signoz) | OpenTelemetry-native observability backend for traces, metrics, and logs with a single UI. Self-hosting needs storage sizing; enterprise directories sit under a separate license. |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | Self-hosted uptime and latency monitoring with many notification integrations. Perfect for small teams; it is not a distributed prober, so check it from more than one vantage point. |

## Databases data access and analytics

| Resource | Useful for / constraints |
|---|---|
| [Trino](https://github.com/trinodb/trino) | Distributed SQL query engine over lakehouse, relational, and object-storage sources. Powerful for federated analytics; requires a cluster and connector-specific knowledge. |
| [Turso Database](https://github.com/tursodatabase/turso) | Rust rewrite of SQLite aiming for compatibility, with vector search and Postgres wire protocol as experimental work in progress. MIT; treat compatibility claims as target-state, not a drop-in guarantee. |

## Data science and engineering tools

| Resource | Useful for / constraints |
|---|---|
| [Apache Superset](https://github.com/apache/superset) | Apache BI platform for SQL-backed dashboards and exploration. Strong SQL editor and charts; embed/enterprise features vary and operational overhead is real. |
| [Evidence](https://github.com/evidence-dev/evidence) | Business intelligence as code: SQL and Markdown compiled into a static site with charts. Great for versioned, code-reviewed reports; less interactive than a BI server. |
| [JupyterLab](https://github.com/jupyterlab/jupyterlab) | Web IDE for notebooks, terminals, and data inspection. Check server extension security and multi-user deployment options before exposing it. |
| [Metabase](https://github.com/metabase/metabase) | Self-hosted BI with a question-builder aimed at non-SQL users, plus dashboards and alerts. AGPL or commercial licensing depending on distribution and features. |
| [Plotly.py](https://github.com/plotly/plotly.py) | Interactive plotting for Python with WebGL rendering and Dash integration. Larger output than static charts; consider bundle size for embedded reports. |

## AI coding agents and assistants

| Resource | Useful for / constraints |
|---|---|
| [Claude Code](https://github.com/anthropics/claude-code) | Anthropic's terminal coding agent: repository-aware edits, commands, and MCP tools. The repository is issue/tracking surface, not the product source; usage requires an account and follows Anthropic's terms. |

## AI MCP servers and tool use

| Resource | Useful for / constraints |
|---|---|
| [Context7](https://github.com/upstash/context7) | MCP server and service that injects version-specific library documentation into coding assistants. Hosted service with self-host option; verify docs freshness and data-handling terms. |

## Web interfaces and application frameworks

| Resource | Useful for / constraints |
|---|---|
| [Can I use](https://caniuse.com/) | Browser support tables for HTML, CSS, and Web API features with notes and known issues. Data is sourced from browser vendors and maintained by contributors; confirm critical features against target browsers. |
| [web.dev](https://web.dev/) | Guidance from the Chrome team on Core Web Vitals, performance, accessibility, and modern web APIs. Authoritative for Chrome behavior; cross-check Safari and Firefox compatibility before relying on a feature. |

## Graphics multimedia scientific and geospatial

| Resource | Useful for / constraints |
|---|---|
| [OBS Studio](https://github.com/obsproject/obs-studio) | Open-source capture and streaming studio with a plugin API. Useful for recording demos and test evidence; GPU encoders and capture sources depend on drivers. |

## Game creation assets and automation

| Resource | Useful for / constraints |
|---|---|
| [Blender](https://github.com/blender/blender) | 3D modeling, animation, and asset pipeline with a Python API and glTF/FBX export. GPL for the application; exported assets remain yours, but bundled add-ons have their own terms. |

## Windows / Binary tooling additions

| Resource | Useful for / constraints |
|---|---|
| [Detect It Easy (DIE)](https://github.com/horsicq/DIE-engine) | Signature and heuristic detection for packers, compilers, and file formats. Good first triage on unknown binaries; signatures need maintenance to stay current. |
| [dnSpyEx](https://github.com/dnSpyEx/dnSpy) | Community revival of the .NET debugger and assembly editor: decompile, edit, and debug IL. GPL-3.0; validate output against original assemblies and never patch third-party binaries you lack rights to. |
| [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language, data inspectors, and binary diffing. GPL-2.0; useful for structure discovery before writing parsers. |
| [radare2](https://github.com/radareorg/radare2) | Reverse-engineering framework and CLI toolset for disassembly, analysis, and binary patching. Steep learning curve; license mixes LGPL components with the project's own terms. |
