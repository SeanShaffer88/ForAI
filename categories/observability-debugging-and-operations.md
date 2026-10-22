# Observability debugging and operations

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OpenTelemetry](https://opentelemetry.io/docs/) | Vendor-neutral traces, metrics and logs with SDKs and collectors. |
| [Prometheus](https://prometheus.io/docs/introduction/overview/) | Metrics collection, querying and alerting. |
| [Grafana](https://grafana.com/docs/grafana/latest/) | Operational dashboards and visualization. |
| [Loki](https://grafana.com/docs/loki/latest/) | Log aggregation and querying. |
| [Jaeger](https://www.jaegertracing.io/docs/) | Distributed trace storage and inspection. |
| [Sentry](https://docs.sentry.io/) | Error reporting and application performance tooling. |
| [Serilog](https://serilog.net/) | Structured logging for .NET. |
| [structlog](https://www.structlog.org/) | Structured Python logging. |
| [Pino](https://getpino.io/) | Structured JavaScript logging. |
| [Tracy](https://github.com/wolfpld/tracy) | Native and real-time application profiling. |
| [RenderDoc](https://renderdoc.org/) | Graphics frame capture and debugging. |
| [Wireshark](https://www.wireshark.org/docs/) | Network protocol inspection and troubleshooting. |
| [AppTrail](https://github.com/SeanShaffer88/AppTrail) | Local Windows folder snapshots, named project checkpoints, Git details, saved source diffs and HTML change reports. MIT; unsigned x64 portable release; snapshots are observations, not backups. |
| [BuildTrail](https://github.com/SeanShaffer88/BuildTrail) | Local Windows build recipes, compiler/tool probes, dependency-manifest evidence, logs, output hashes and AppTrail source comparisons. MIT; unsigned x64 portable app; manifests are not a complete installed dependency graph. |

Project additions checked 2026-10-21: see the machine-readable index for scoped evidence and first-party testing limits.

## Windows change investigation additions — 2026-10-22

Primary README and MIT license text reviewed for these entries only. No software executed, dependency adopted, or comprehensive maintenance/security audit performed. Linked projects retain upstream licensing.

| Resource | Purpose and limits |
|---|---|
| [Microsoft Attack Surface Analyzer](https://github.com/microsoft/AttackSurfaceAnalyzer) | Compare system security configuration snapshots with broad collectors and local SQLite evidence. MIT; README and license read 2026-10-22. Runtime, release maintenance and Windows compatibility need validation; not executed. |
| [WinLedger](https://github.com/fanyqe/winledger) | Local Windows before/after sessions for registry, services, tasks, startup, environment, firewall and selected files; conservative rollback. MIT license and README read 2026-10-22; Windows 11 x64/.NET 10 documented, not independently tested or adopted. |
