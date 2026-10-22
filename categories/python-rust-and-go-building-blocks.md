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
