# Python Rust and Go building blocks

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Pydantic](https://docs.pydantic.dev/latest/) | Python data validation and serialization; distinguish coercion from strict validation. |
| [msgspec](https://msgspec.dev/) | Typed Python serialization and validation; check format and schema support. |
| [AnyIO](https://anyio.readthedocs.io/en/stable/) | Structured async concurrency across supported Python backends. |
| [Tenacity](https://tenacity.readthedocs.io/en/latest/) | Configurable Python retries; set time bounds and operation-specific retry conditions. |
| [Typer](https://typer.tiangolo.com/) | Python command-line interfaces using type annotations. |
| [Rich](https://rich.readthedocs.io/en/stable/) | Python terminal formatting and progress displays; test noninteractive output. |
| [orjson](https://github.com/ijl/orjson) | Python JSON serialization; verify wheel availability and serialization semantics. |
| [Tokio](https://tokio.rs/) | Rust async runtime; blocking work and cancellation need explicit handling. |
| [Axum](https://docs.rs/axum/latest/axum/) | Rust HTTP routing and middleware using the Tokio/Tower ecosystem. |
| [Serde](https://serde.rs/) | Rust serialization framework; choose a format crate and compatibility policy. |
| [Rayon](https://docs.rs/rayon/latest/rayon/) | Rust data parallelism; benchmark contention and task sizes. |
| [Clap](https://docs.rs/clap/latest/clap/) | Rust command-line argument parsing and help generation. |
| [reqwest](https://docs.rs/reqwest/latest/reqwest/) | Rust HTTP clients; select TLS backend, timeouts and feature flags. |
| [tracing](https://docs.rs/tracing/latest/tracing/) | Structured Rust diagnostics and spans; select subscribers/exporters. |
| [pgx](https://github.com/jackc/pgx) | Go PostgreSQL driver and toolkit; check pooling and cancellation behavior. |
| [sqlc](https://docs.sqlc.dev/en/stable/) | Generate typed data access from SQL; database and language support differ. |
| [goose](https://pressly.github.io/goose/) | SQL and Go database migrations; validate locking and rollback strategy. |
| [Cobra](https://cobra.dev/) | Go CLI commands, flags and completion. |
| [Bubble Tea](https://github.com/charmbracelet/bubbletea) | Go terminal application framework; test Windows terminals and redirected I/O. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [attrs](https://github.com/python-attrs/attrs) | Define Python data classes with validation and conversion; distinguish runtime validation from typing. |
| [cattrs](https://github.com/python-attrs/cattrs) | Convert Python objects to and from structured data; configure hooks for domain types. |
| [Pendulum](https://github.com/python-pendulum/pendulum) | Work with Python dates, durations and time zones; test daylight-saving transitions. |
| [python-dateutil](https://github.com/dateutil/dateutil) | Extend Python date parsing and recurrence handling; avoid ambiguous input formats. |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Load development environment settings from files; keep secrets out of version control. |
| [platformdirs](https://github.com/tox-dev/platformdirs) | Resolve platform-appropriate application directories; validate packaging and service-account behavior. |
| [watchfiles](https://github.com/samuelcolvin/watchfiles) | Watch filesystem changes from Python using a Rust backend; control scope and debounce behavior. |
| [DiskCache](https://github.com/grantjenks/python-diskcache) | Use disk-backed Python caching; define eviction, contention and cache invalidation behavior. GitHub reports its last push as 2024-08-10; maintenance responsiveness was not established. |
| [joblib](https://github.com/joblib/joblib) | Cache computations and parallelize Python work; never load serialized objects from untrusted sources. |
| [Loguru](https://github.com/Delgan/loguru) | Configure Python application logging; review sensitive-data filtering and multiprocess behavior. |
| [anyhow](https://github.com/dtolnay/anyhow) | Propagate contextual errors in Rust applications; retain typed errors where callers need recovery. |
| [thiserror](https://github.com/dtolnay/thiserror) | Derive structured Rust error implementations; design stable public error contracts. |
| [bytes](https://github.com/tokio-rs/bytes) | Manage byte buffers for Rust networking; understand ownership and shared-buffer retention. |
| [DashMap](https://github.com/xacrimon/dashmap) | Concurrent Rust maps with familiar operations; avoid holding guards across conflicting accesses. |
| [SQLx](https://github.com/transact-rs/sqlx) | Async Rust database access with checked-query tooling; match database features and runtime integration. |
| [SeaORM](https://github.com/SeaQL/sea-orm) | Async Rust relational data access; inspect generated queries and migration strategy. |
| [chi](https://github.com/go-chi/chi) | Compose Go HTTP routing and middleware; preserve request context and timeout handling. |
| [Echo](https://github.com/labstack/echo) | Build Go HTTP applications with routing and middleware; review middleware order and trusted proxies. |
| [zerolog](https://github.com/rs/zerolog) | Structured Go logging with low-allocation APIs; design log schema and sensitive-data handling. |
| [Zap](https://github.com/uber-go/zap) | Structured Go logging with typed fields; manage sampling and shutdown flushing. |
