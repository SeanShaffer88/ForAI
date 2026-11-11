# Optimization scheduling and operational tooling

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OR-Tools](https://developers.google.com/optimization) | Constraint programming, routing and optimization; solver choice affects deployment. |
| [Z3](https://github.com/Z3Prover/z3) | SMT solving for constraints and program analysis; model correctness remains application-specific. |
| [NetworkX](https://networkx.org/documentation/stable/) | Python graph algorithms; assess memory use on large graphs. |
| [APScheduler](https://apscheduler.readthedocs.io/) | Python scheduling; select version and coordinate persistence across workers. |
| [Quartz.NET](https://www.quartz-scheduler.net/documentation/) | .NET scheduling with persistence and clustering options; configure misfires and time zones. |
| [Fluent Bit](https://docs.fluentbit.io/manual) | Telemetry collection and forwarding; check buffering, loss and plugin support. |
| [Vector](https://vector.dev/docs/) | Telemetry processing pipelines; configure delivery, buffering and sensitive-data handling. |
| [Toxiproxy](https://github.com/Shopify/toxiproxy) | Inject network failures into integration tests; route test traffic explicitly. |
| [MockServer](https://www.mock-server.com/) | HTTP mocking and verification; isolate expectations between concurrent tests. |
| [Schemathesis](https://schemathesis.readthedocs.io/) | Property-based API testing from schemas; run against authorized test environments. |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [autoscaler](https://github.com/kubernetes/autoscaler) | Autoscaling components for Kubernetes. |
| [cron](https://github.com/robfig/cron) | a cron library for go. |
| [descheduler](https://github.com/kubernetes-sigs/descheduler) | Descheduler for Kubernetes. |
| [gocron](https://github.com/jasonlvhit/gocron) | A Golang Job Scheduling Package. |
| [gronx](https://github.com/adhocore/gronx) | Lightweight, fast and dependency-free Cron expression parser (due checker, next/prev due date finder), task runner, job scheduler and/or daemon for Golang (tested on v1.13+) and standalone usage. |
| [healthchecks](https://github.com/healthchecks/healthchecks) | Open-source cron job and background task monitoring service, written in Python & Django. |
<!-- expansion-2026-11-11:end -->
