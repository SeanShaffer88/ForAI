# Observability debugging and operations

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OpenTelemetry](https://opentelemetry.io/docs/) | Vendor-neutral traces, metrics and logs with SDKs and collectors. |
| [Prometheus](https://prometheus.io/docs/introduction/overview/) | Metrics collection, querying and alerting. |
| [Grafana](https://grafana.com/docs/grafana/latest/) | Operational dashboards and visualization. |
| [Loki](https://grafana.com/docs/loki/latest/) | Log aggregation and querying from Grafana Labs: indexes log labels rather than full text, so it is cheaper than Elasticsearch for logs but weaker at full-text search. |
| [Jaeger](https://www.jaegertracing.io/docs/) | Distributed trace storage and inspection. |
| [Sentry](https://docs.sentry.io/) | Error reporting and application performance tooling. |
| [Serilog](https://serilog.net/) | Structured logging for .NET with sinks to files, consoles, and log services; the de facto standard .NET logging library. |
| [structlog](https://www.structlog.org/) | Structured Python logging that produces machine-readable (JSON) log events; pairs with standard-library logging or as a standalone pipeline. |
| [Pino](https://getpino.io/) | Structured JavaScript/Node.js logging built for speed, emitting JSON in production; transports run out-of-process to keep the event loop free. |
| [Tracy](https://github.com/wolfpld/tracy) | Native and real-time application profiling. |
| [RenderDoc](https://renderdoc.org/) | Graphics frame capture and debugging for Vulkan, D3D, and OpenGL: inspect draw calls, resources, and pipeline state frame by frame; not a profiler for CPU code. |
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

## Additions checked 2026-10-22

2026-10-22 canonical GitHub metadata, README and license identification reviewed; source documentation only. No build, runtime/architecture validation, release audit, benchmark or security audit; not adopted.

| Resource | Purpose and constraints |
|---|---|
| [Dumpling (.NET heap analysis)](https://github.com/CoreyKaylor/dotnet-dumpling) | Apache-2.0 CLI and MCP candidate for .NET heap comparisons, retention paths and dominator analysis. Upstream documents .gcdump and ClrMD process-dump support; unarchived, repository pushed 2026-08-14. Validate format fidelity, memory use, distribution and supported runtimes before reuse. |
| [dotnet-heapview](https://github.com/1hub/dotnet-heapview) | MIT desktop heap viewer, shared heap model and MCP source example. Upstream lists .gcdump, .hprof and .mono-heap inputs; unarchived, repository pushed 2026-09-21. Compare PerfView and Dumpling; GUI completeness, packaging and Windows runtime support remain untested. |

## HeapTrail for .NET preview — 2026-10-22

| Resource | Purpose and constraints |
|---|---|
| [HeapTrail for .NET](https://github.com/SeanShaffer88/HeapTrail) | Free MIT Windows x64 .NET heap investigation desktop: compare .gcdump counts/shallow bytes, inspect root/incoming/outgoing paths, save notes and export local HTML. Unsigned self-contained preview; no live attachment, retained-size/dominator analysis or allocation stacks. |

First-party scope: [v0.1.0-preview.1](https://github.com/SeanShaffer88/HeapTrail/releases/tag/v0.1.0-preview.1), source commit `0ba60bc84c4727147723b6c275eeae4cbd5336fc`. Fifteen graph/persistence/report checks include a real event leak growing 1 → 25 → 1 after a fix and a cache staying at 4. Four additional importer checks cover success, failure, cancellation and cleanup. Desktop workflow and extracted portable runtime were exercised. [Windows CI passed on this source](https://github.com/SeanShaffer88/HeapTrail/actions/runs/39753330962). Uses Microsoft's MIT diagnostics reader; dependency/license provenance is recorded in the project. This is an unsigned preview, not a complete profiler or security audit. Capture completeness, large/sampled heaps, ARM64/x86 and older runtimes remain limits; paths show reachability, not exclusive retained size.

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [OpenObserve](https://github.com/openobserve/openobserve) | Store and query operational telemetry; review resource sizing and edition licensing. |
| [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) | Store and query time-series metrics; compare single-node, cluster and enterprise capabilities. |
| [Pyroscope](https://github.com/grafana/pyroscope) | Collect and explore continuous profiles; account for language-agent support and sampling overhead. |
| [Tempo](https://github.com/grafana/tempo) | Store distributed traces; plan object storage and telemetry ingestion limits. |
| [Parca](https://github.com/parca-dev/parca) | Profile workloads continuously; confirm platform and symbolization support. |
| [bpftrace](https://github.com/bpftrace/bpftrace) | Trace Linux behavior with eBPF scripts; validate kernel features and required privileges. |
| [Pixie](https://github.com/pixie-io/pixie) | Observe Kubernetes workloads through automatic instrumentation; assess eBPF and cluster requirements. |
| [Glances](https://github.com/nicolargo/glances) | Inspect host and container metrics; configure authentication for exposed monitoring endpoints. |
| [bottom](https://github.com/ClementTsang/bottom) | View system utilization in a terminal; compare per-platform metric availability. |
| [bandwhich](https://github.com/imsnif/bandwhich) | Attribute network bandwidth to local processes; inspect operating-system and privilege requirements. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [memray](https://github.com/bloomberg/memray) | Memray is a memory profiler for Python (from Bloomberg): tracks allocations to find leaks and hot spots in long-running processes. |
| [GoModel](https://github.com/ENTERPILOT/GoModel) | AI gateway / AI control plane / AI proxy written in Go. Unified OpenAI-compatible and Anthropic-compatible API for OpenAI, Anthropic, Gemini, Groq, xAI, Ollama, vLLM and more. A LiteLLM alternative with observability, guardrails, streaming, cost tracking, intelligent routing, sticky sessions, failover, real-time logs and usage tracking. Prod ready. |
| [zipkin](https://github.com/openzipkin/zipkin) | Zipkin is a distributed tracing system: collects and visualises request traces across services (OpenZipkin); OpenTelemetry is the newer instrumentation standard feeding it. |
| [flogger](https://github.com/google/flogger) | A Fluent Logging API for Java |
| [rustnet](https://github.com/domcyrus/rustnet) | Per-process network monitoring for your terminal with deep packet inspection. Cross-platform, sandboxed. |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [lnav](https://github.com/tstack/lnav) | Terminal log viewer with SQL queries, time-shifted merges of multiple files, and format detection. Excellent for incident archaeology on local logs; Windows builds run under WSL or MSYS. |
| [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) | Vendor-neutral agent and gateway for receiving, processing, and exporting telemetry. Configure sampling, memory limits, and batching deliberately; it is infrastructure, not a library. |
| [SigNoz](https://github.com/SigNoz/signoz) | OpenTelemetry-native observability backend for traces, metrics, and logs with a single UI. Self-hosting needs storage sizing; enterprise directories sit under a separate license. |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | Self-hosted uptime and latency monitoring with many notification integrations. Perfect for small teams; it is not a distributed prober, so check it from more than one vantage point. |
<!-- expansion-2026-11-10:end -->

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [btrace](https://github.com/btraceio/btrace) | Production-safe dynamic tracing and diagnostics for Java applications—attach to live JVMs with no restart or recompilation. |
| [coroot](https://github.com/coroot/coroot) | Coroot is an open-source observability and APM tool with AI-powered Root Cause Analysis. It combines metrics, logs, traces, continuous profiling, and SLO-based alerting with predefined dashboards and inspections. |
| [datadog agent](https://github.com/DataDog/datadog-agent) | Main repository for Datadog Agent. |
| [FlameGraph](https://github.com/brendangregg/FlameGraph) | Stack trace visualizer. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [fluent bit (fluent)](https://github.com/fluent/fluent-bit) | Fast and Lightweight Logs, Metrics and Traces processor for Linux, BSD, OSX and Windows. |
| [highlight](https://github.com/highlight/highlight) | highlight.io: The open source, full-stack monitoring platform. Error monitoring, session replay, logging, distributed tracing, and more. License not detected by GitHub; check the repository license before use. |
| [kibana](https://github.com/elastic/kibana) | Your window into all of your data. License not detected by GitHub; check the repository license before use. |
| [logstash](https://github.com/elastic/logstash) | Logstash - transport and process your logs, events, or other data. License not detected by GitHub; check the repository license before use. |
| [minitrace rust](https://github.com/tikv/minitrace-rust) | Extremely fast tracing library for Rust. |
| [netdata](https://github.com/netdata/netdata) | The fastest path to AI-powered full stack observability, even for lean teams. GPL-3.0: derivative works must stay under the GPL. |
| [opentelemetry cpp](https://github.com/open-telemetry/opentelemetry-cpp) | The OpenTelemetry C++ Client. |
| [opentelemetry dotnet](https://github.com/open-telemetry/opentelemetry-dotnet) | The OpenTelemetry .NET Client. |
| [opentelemetry go](https://github.com/open-telemetry/opentelemetry-go) | OpenTelemetry Go API and SDK. |
| [opentelemetry java](https://github.com/open-telemetry/opentelemetry-java) | OpenTelemetry Java SDK. |
| [opentelemetry js](https://github.com/open-telemetry/opentelemetry-js) | OpenTelemetry JavaScript Client. |
| [opentelemetry python](https://github.com/open-telemetry/opentelemetry-python) | OpenTelemetry Python API and SDK. |
| [opentelemetry rust](https://github.com/open-telemetry/opentelemetry-rust) | The Rust OpenTelemetry implementation. |
| [pprof](https://github.com/google/pprof) | pprof is a tool for visualization and analysis of profiling data. |
| [self hosted](https://github.com/getsentry/self-hosted) | Sentry, feature-complete and packaged up for low-volume deployments and proofs-of-concept. License not detected by GitHub; check the repository license before use. |
| [uptrace](https://github.com/uptrace/uptrace) | Open source APM: OpenTelemetry traces, metrics, and logs. AGPL-3.0: network use can trigger source-disclosure obligations. |
<!-- expansion-2026-11-11:end -->
