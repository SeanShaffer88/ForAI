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
