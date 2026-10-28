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
| [Cobra](https://cobra.dev/) | Go CLI library for commands, flags, and shell completion (used by kubectl and Hugo); pair with Viper for configuration files and environment variables. |
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

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [Scrapling](https://github.com/D4Vinci/Scrapling) | 🕷️ The BEST Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here: https://discord.gg/EMgGbDceNQ and follow here for daily tips and tricks: https://x.com/Scrapling_dev |
| [whisper](https://github.com/openai/whisper) | Robust Speech Recognition via Large-Scale Weak Supervision |
| [AstrBot](https://github.com/AstrBotDevs/AstrBot) | AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨ |
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 ready-to-use validated skills plus 100+ scientific databases covering biology, chemistry, medicine, and drug discovery. Compatible with Cursor, Claude Code, Codex, Pi, Antigravity, and the open Agent Skills standard. |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | scikit-learn: machine learning in Python |
| [keras](https://github.com/keras-team/keras) | Deep learning for humans: the high-level Keras 3 API for building and training neural networks across TensorFlow, JAX, and PyTorch backends. |
| [agents](https://github.com/wshobson/agents) | Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi |
| [jax](https://github.com/jax-ml/jax) | Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more |
| [timesfm](https://github.com/google-research/timesfm) | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
| [spaCy](https://github.com/explosion/spaCy) | 💫 Industrial-strength Natural Language Processing (NLP) in Python |
| [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes. |
| [optuna](https://github.com/optuna/optuna) | A hyperparameter optimization framework for ML: define-by-run trial APIs, pruners, and samplers; framework-agnostic across training stacks. |
| [reflex](https://github.com/reflex-dev/reflex) | 🕸️ Web apps in pure Python 🐍 |
| [stagehand](https://github.com/browserbase/stagehand) | The SDK to extract data and interact with any site on the web. Get started with Claude Code, Codex, Eve, Mastra, and more. |
| [starlette](https://github.com/Kludex/starlette) | The little ASGI framework that shines. 🌟 |
| [dash](https://github.com/plotly/dash) | Data Apps & Dashboards for Python. No JavaScript Required. |
| [akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 |
| [adk-python](https://github.com/google/adk-python) | An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [prophet](https://github.com/facebook/prophet) | Tool for producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth. |
| [sktime](https://github.com/sktime/sktime) | A unified framework for machine learning with time series |
| [trl](https://github.com/huggingface/trl) | Train transformer language models with reinforcement learning. |
| [bottle](https://github.com/bottlepy/bottle) | bottle.py is a fast and simple micro-framework for python web-applications. |
| [pipx](https://github.com/pypa/pipx) | Install and Run Python Applications in Isolated Environments |
| [fiftyone](https://github.com/voxel51/fiftyone) | Refine high-quality datasets and visual AI models |
| [openhuman](https://github.com/tinyhumansai/openhuman) | The fastest, cheapest, most efficient open-source agent harness. Run more than 500 agents on a $10 VPS. |
| [azul](https://github.com/fschutt/azul) | Desktop GUI Framework |
| [rerun](https://github.com/rerun-io/rerun) | Visualize, query, and stream to train on multimodal robotics data. |
| [kata-containers](https://github.com/kata-containers/kata-containers) | Kata Containers is an open source project and community working to build a standard implementation of lightweight Virtual Machines (VMs) that feel and perform like containers, but provide the workload isolation and security advantages of VMs. https://katacontainers.io/ |
| [fff](https://github.com/dmtrKovalenko/fff) | The fastest and the most accurate file search SDK for AI agents, Neovim, Rust, C, Python, Bun and NodeJS |
| [sui](https://github.com/MystenLabs/sui) | Sui, a next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Move programming language |
| [koharu](https://github.com/koharu-rs/koharu) | ML-powered manga translator, written in Rust. |
| [iii](https://github.com/iii-hq/iii) | Effortlessly compose, extend, and observe every service in real-time for the first time ever. |
| [sail](https://github.com/lakehq/sail) | Drop-in Apache Spark replacement written in Rust, unifying batch processing, stream processing, and compute-intensive AI workloads. |
| [rustviz](https://github.com/rustviz/rustviz) | Interactively Visualizing Ownership and Borrowing for Rust |
| [markdown-oxide](https://github.com/Feel-ix-343/markdown-oxide) | PKM Markdown Language Server |
| [creusot](https://github.com/creusot-rs/creusot) | Creusot helps you prove your Rust code is correct. |
| [pegainfer](https://github.com/pegainfer-project/pegainfer) | Pure Rust + CUDA LLM inference engine — no PyTorch, OpenAI-compatible, serves Qwen3 to Kimi-K2 |
| [satteri](https://github.com/bruits/satteri) | High-performance Markdown and MDX processing for the JavaScript ecosystem |
| [hydra](https://github.com/ja7ad/hydra) | A fast, resilient, multi-source file retriever and download engine |
| [uefi-rs](https://github.com/rust-osdev/uefi-rs) | Rusty wrapper for the Unified Extensible Firmware Interface (UEFI). This crate makes it easy to develop Rust software that leverages safe, convenient, and performant abstractions for UEFI functionality. |
| [project-layout](https://github.com/golang-standards/project-layout) | Standard Go Project Layout |
| [watermill](https://github.com/ThreeDotsLabs/watermill) | Building event-driven applications the easy way in Go. |
| [dasel](https://github.com/TomWright/dasel) | Unified querying, transformation, and modification of JSON, TOML, YAML, XML, INI, HCL, KDL and CSV. |
| [tendermint](https://github.com/tendermint/tendermint) | ⟁ Tendermint Core (BFT Consensus) in Go |
| [tau](https://github.com/taubyte/tau) | Fullstack Workspace for Humans & Machines |
| [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) | An idiomatic Go (golang) validation package. Supports configurable and extensible validation rules (validators) using normal language constructs instead of error-prone struct tags. |
| [nutsdb](https://github.com/nutsdb/nutsdb) | A simple, fast, embeddable, persistent key/value store written in pure Go. It supports fully serializable transactions and many data structures such as list, set, sorted set. |
| [gleam](https://github.com/chrislusf/gleam) | Fast, efficient, and scalable distributed map/reduce system, DAG execution, in memory or on disk, written in pure Go, runs standalone or distributedly. |
| [dicedb](https://github.com/dicedb/dicedb) | Open-source, low-latency key/value engine built on Valkey with query subscriptions and hierarchical storage tiers. |
| [easeprobe](https://github.com/megaease/easeprobe) | A simple, standalone, and lightweight tool that can do health/status checking, written in Go. |
| [tfgo](https://github.com/galeone/tfgo) | Tensorflow + Go, the gopher way |
| [flamingo](https://github.com/i-love-flamingo/flamingo) | Flamingo Framework and Core Library. Flamingo is a go based framework to build pluggable applications. Focus is on clean architecture, maintainability and operation readiness. |
| [omniparser](https://github.com/jf-tech/omniparser) | omniparser: a native Golang ETL streaming parser and transform library for CSV, JSON, XML, EDI, text, etc. |
