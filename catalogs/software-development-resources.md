# Software development resource reference

Saved 2026-10-21 at Sean's request for future software development assistance.

**431 resource entries across 29 areas**, supplementing the existing 232-repository Windows reference. These counts overlap: do not sum them as unique projects.

Persistent master: (local research archive).
User-facing copy: (local research archive).
Machine-readable catalog: the adjacent `software-development-resources.csv` in both locations.

## How to use this reference

Consult only the sections relevant to the project. Preserve the project's established stack and constraints. Prefer the official API or supported SDK when it fits; direct HTTP, a smaller library, or existing dependencies may be simpler. Record concrete adoption decisions in the consuming project. This catalog is a broad starting map, not an exhaustive inventory of everything software development might ever need.

Before adoption, recheck upstream maintenance, license and redistribution terms, security advisories, OS/CPU support, runtime/compiler versions, package provenance, API deprecations, service availability, pricing and integration requirements. For Windows native code, verify x64/ARM64/x86, ABI, CRT linkage, symbols and runtime redistribution. Separate SDK packages from required runtimes, drivers, native DLLs and build tools. An inactive project can still justify a focused maintained fork when its benefit outweighs ownership costs; use the existing revival guidance.

For service APIs, establish authentication scopes, consent, rate limits, pagination, timeouts, cancellation, webhook signatures, retries, idempotency and data handling. Check SDK and API versions independently. Use sandbox environments when available. Do not place credentials in this reference. Listing a service does not mean the account is connected or authorized, and listing a tool does not install it.

## Task-to-resource shortcuts

| Need | Useful starting points |
|---|---|
| Native Windows app or DLL integration | Windows SDK, Windows App SDK, Win32, WebView2; existing Windows catalog for interop libraries |
| Web application | Existing framework first; React/Next.js, Vue/Nuxt, SvelteKit, Angular, Astro and Vite are candidates |
| HTTP service | ASP.NET Core, FastAPI, Django, Spring Boot, Laravel or Rails; OpenAPI for interface contracts |
| Third-party API client | Provider SDK first, then Kiota/OpenAPI Generator or an HTTP client; validate authentication and API version |
| Desktop or mobile UI | Qt, Avalonia, MAUI, Electron, Tauri, Flutter, React Native; native Android/Apple SDKs where needed |
| Embedded or robotics | Zephyr, ESP-IDF, FreeRTOS, ROS 2; match the exact board, chip and release |
| Local data or analytics | SQLite for embedded relational storage; DuckDB for analytical SQL; Arrow/Polars/pandas for processing |
| Server database | PostgreSQL, MySQL, MongoDB; choose schema, migrations, backup and concurrency deliberately |
| Search and retrieval | OpenSearch or Meilisearch for text; pgvector or Qdrant for vectors; benchmark actual queries |
| Async jobs | Existing queue first; Celery, BullMQ, Hangfire; Temporal when durable workflow semantics justify it |
| Tests | Stack-native unit tests; Playwright for browser behavior; Testcontainers for real dependencies; Pact for contracts |
| Performance issue | Measure first: OTel/Prometheus, native profiler, BenchmarkDotNet, k6, RenderDoc or Wireshark by symptom |
| Dependency or supply-chain review | OSV-Scanner, Trivy, Semgrep, Gitleaks; SBOM and Sigstore/SLSA as project needs warrant |
| Packaging and releases | Existing CI first; MSIX, WiX, Inno Setup or Velopack for Windows distribution |
| AI integration | Provider official SDK; ONNX Runtime/llama.cpp/Ollama for local candidates; measure quality, cost and hardware fit |

## Evidence and limits

Research used the Exa Search skill and official OpenAI documentation. There were 19 successful Exa searches requesting 110 result slots in total, including duplicates, plus one rate-limited search. Search results were filtered toward upstream/vendor sources. Eleven selected pages were fetched through Exa; the OpenAI SDK page was separately opened through web browsing. The initial 253-entry catalog also included curated primary-source pointers beyond those search results.

In the initial pass, every catalog URL received an HTTP reachability check. Initial outcome: 251 reachable and 2 access-limited (MySQL returned 403; Ansible returned 429). These restrictions do not establish that a project is unavailable. Two initially broken paths were corrected using follow-up searches and rechecked. Reachability and page titles do not establish maintenance, compatibility, licensing suitability, security, or correctness of every capability description. Most entries are discovery references, not adoption audits. No dependency was installed, built or benchmarked for this catalog. Revalidate when a project actually needs a candidate.

Selected deeper checks: [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/), [OpenAPI](https://spec.openapis.org/oas/latest.html), [GitHub REST](https://docs.github.com/en/rest), [OpenTelemetry](https://opentelemetry.io/docs/), [Pact](https://docs.pact.io/), [Sigstore overview](https://docs.sigstore.dev/about/overview/), [Temporal](https://docs.temporal.io/), [Testcontainers](https://docs.docker.com/testcontainers/), [Microsoft Graph SDKs](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview), [Stripe SDKs](https://docs.stripe.com/sdks), and [OpenAI SDKs](https://developers.openai.com/api/docs/libraries).

### Expansion 1 — 2026-10-21

Added **108 entries across 10 additional areas**. This pass used 17 Exa searches requesting 79 result slots, including duplicates and follow-up path repairs. Upstream page excerpts were retrieved for all 108 additions, plus four supporting pages for licensing, hosted-service terms, usage policy and document structure. Excerpts establish discovery context, not a full compatibility, maintenance or license audit. Three obsolete documentation paths were replaced and rechecked. WAMR's canonical repository has moved to the `wasm-micro-runtime` organization.

HTTP checks for the additions: **106 normal reachable pages, one HTTP 200 maintenance page (FRED), and one HTTP 403 access restriction (Europe PMC)**. Europe PMC's documentation was readable through Exa; direct-access failure is retained in the CSV. The initial 253 links were carried forward without another full check. The expanded CSV records addition batch, check date and review level per entry. Counts are unique catalog entries by name/URL, not unique upstream projects across all references: specialized interfaces such as the SQLite backup API are separate resources.

New selection shortcuts:

| Need | Candidates and decision point |
|---|---|
| Editor, refactoring or source analysis | LSP, DAP, Tree-sitter, ast-grep, Comby; parsing, language intelligence and debugging are separate layers |
| Smaller .NET building blocks | Polly, Refit, Dapper, FluentValidation, MVVM Toolkit, Noda Time and CsvHelper |
| Python/Rust/Go service tooling | Pydantic/msgspec/AnyIO; Tokio/Axum/Serde; pgx/sqlc/goose; select by language and existing stack |
| Sandboxed plugins | Wasmtime, Wasmer, Extism or WAMR; match WASI/component versions and restrict exposed host capabilities |
| Collaborative or offline editing | Yjs/Automerge plus an editor and persistence layer; CRDT convergence does not supply authorization |
| Feature flags and secrets | OpenFeature with a provider; SOPS/age or a secrets service according to credential lifecycle needs |
| Backups and recovery | restic/Kopia for snapshots; rclone for transfers; Litestream or SQLite backup API for SQLite-specific needs |
| OCR, Office or PDF work | Tesseract, Tika, PDFium/MuPDF/PDFBox, Open XML SDK/POI/ClosedXML; editing and rendering are different capabilities |
| Public data integrations | Open-Meteo, Census, World Bank, NOAA, NASA, USGS, OpenAlex, Crossref and Europe PMC; data rights and hosted quotas vary |
| Scheduling, optimization or resilience tests | APScheduler/Quartz.NET, OR-Tools/Z3/NetworkX, Toxiproxy/MockServer/Schemathesis |

Important upstream distinctions retained:

- [Open-Meteo terms](https://open-meteo.com/en/terms) restrict the free hosted API to noncommercial use. Data licensing and hosted API access terms are distinct.
- [Nominatim public-server policy](https://operations.osmfoundation.org/policies/nominatim/) applies to the OSMF service, with a maximum of one request per second and application identification/attribution requirements. It does not define the capacity of a separately hosted deployment.
- [MuPDF licensing](https://mupdf.readthedocs.io/en/latest/license.html) offers AGPL and commercial licensing routes; review the actual distribution model before selection.
- [Monaco's upstream page](https://microsoft.github.io/monaco-editor/) states mobile browsers and mobile web frameworks are unsupported.
- [OpenFeature](https://openfeature.dev/docs/reference/intro/) standardizes the SDK interface; a provider supplies the feature-flag backend.
- [Extism host SDKs](https://extism.org/docs/concepts/host-sdk/) run plugins; plugin development kits create plugins. Choose both sides of the integration deliberately.
- [FRED documentation](https://fred.stlouisfed.org/docs/api/fred/) returned a maintenance page during review. Its catalog entry is a follow-up candidate, not a verified working integration.

## Maintenance and integration findings

- The [Fern public repository](https://github.com/fern-api/fern) currently says its open-source project is no longer maintained and directs users to its commercial platform. Treat the public repository and hosted product separately; a targeted revival remains an option if a real project justifies ownership. It is not included as a default maintained generator candidate.
- OpenAPI schema versions and generator support are separate choices. Pin a version the selected generator and consumers can handle.
- Testcontainers needs a compatible container runtime; verify that the CI runner can start and clean up dependencies.
- Microsoft Graph SDK release status and the selected API endpoint are separate: a stable SDK does not make beta endpoints stable. Check consent and least-privilege scopes.
- Stripe versions its SDKs and APIs separately. Verify the API version and retry/idempotency behavior used by the application.
- Redis, Terraform, Qt, Docker Desktop, media codecs, game engines and hosted products warrant project-specific license/terms review. This is not a claim that they share a license or commercial model.
- Latest documentation may describe development branches or newly released APIs. Select documentation matching the version actually used.

## Catalog

HTTP status in the CSV is discovery evidence, not an endorsement. Official docs often link to language-specific SDKs, source repositories, examples and migration guides.


### Platform SDKs and Windows

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |


Project additions checked 2026-10-21:

| Resource | Project use and evidence limits |
|---|---|
| [Windows Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects) | Windows process-tree lifetime and resource limits; suspended creation plus assignment prevents child escape before containment. Kill-on-close stops owned descendants; persistent build daemons need explicit handling. Check: Microsoft API documentation read for BuildTrail; suspended assignment, cancellation, timeout and normal-exit child cleanup tested on Windows 11 x64. Not an independent security audit. |

### Languages and runtimes

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Builds packages and environments

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### API contracts clients and networking

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Web interfaces and application frameworks

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Desktop mobile and device SDKs

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Databases data access and analytics

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Search messaging and durable work

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Cloud infrastructure and deployment

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### CI version control and releases

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Testing verification and performance

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Security identity and supply chain

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Observability debugging and operations

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |


Project additions checked 2026-10-21:

| Resource | Project use and evidence limits |
|---|---|
| [AppTrail](https://github.com/SeanShaffer88/AppTrail) | Local Windows folder snapshots, named project checkpoints, Git details, saved source diffs and HTML change reports. MIT; unsigned x64 portable release; snapshots are observations, not backups. Check: First-party project: v0.16.0 source, 136 local tests, Edge reports, standalone launch and exact-commit GitHub Windows CI checked. Windows 11 x64 validated; not an independent audit. |
| [BuildTrail](https://github.com/SeanShaffer88/BuildTrail) | Local Windows build recipes, compiler/tool probes, dependency-manifest evidence, logs, output hashes and AppTrail source comparisons. MIT; unsigned x64 portable app; manifests are not a complete installed dependency graph. Check: First-party project: 0.1.0 source, Python/Tk and real MSVC consumer tests, offline browser report and exact frozen-EXE success/failure checks. Windows 11 x64 validated; release/CI status must be checked at adoption. Not an independent audit. |

### Integration APIs and business SDKs

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### AI machine learning and local inference

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Graphics multimedia scientific and geospatial

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Accessibility internationalization and documentation

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |

### Standards and discovery

| Resource / official source | When useful and what to check |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Python](https://docs.python.org/3/) | Language, standard library, packaging interfaces and embedding. |
| [TypeScript](https://www.typescriptlang.org/docs/) | Static checking for JavaScript; match compiler and library types. |
| [Node.js](https://nodejs.org/api/) | Server JavaScript APIs and runtime behavior. |
| [Rust and Cargo](https://doc.rust-lang.org/) | Systems programming, ownership and package/build tooling. |
| [Go](https://go.dev/doc/) | Services, concurrency and standard tooling. |
| [Java](https://dev.java/learn/) | JVM language and platform development resources. |
| [Kotlin](https://kotlinlang.org/docs/home.html) | JVM and multiplatform language development. |
| [Swift](https://www.swift.org/documentation/) | Language and toolchain reference; target platform capabilities differ. |
| [PHP](https://www.php.net/docs.php) | Web backend language and runtime reference. |
| [Ruby](https://www.ruby-lang.org/en/documentation/) | Language and standard runtime reference. |
| [Dart](https://dart.dev/guides) | Language and tooling used with Flutter and standalone apps. |
| [Zig](https://ziglang.org/documentation/) | Native language and toolchain candidate; verify compiler-version compatibility. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | Browser HTML, CSS, JavaScript and Web API reference. |
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Python linting and formatting. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Execute generated native build graphs. |
| [vcpkg](https://learn.microsoft.com/en-us/vcpkg/) | C and C++ dependency management; select triplet and linkage. |
| [Conan](https://docs.conan.io/2/) | C and C++ packages, profiles and binary dependency management. |
| [LLVM](https://llvm.org/docs/) | Compiler infrastructure, optimization and binary tooling. |
| [Clang tooling](https://clang.llvm.org/docs/) | C-family compiler, diagnostics and source analysis. |
| [Meson](https://mesonbuild.com/) | Native project configuration and dependency integration. |
| [Bazel](https://bazel.build/docs) | Build graphs, caching and multi-language build infrastructure. |
| [Gradle](https://docs.gradle.org/) | JVM, Android and extensible build automation. |
| [Maven](https://maven.apache.org/guides/) | JVM builds, dependency coordinates and publishing. |
| [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/) | Microsoft project build engine and task extension. |
| [Dev Containers](https://containers.dev/) | Portable development-environment specification. |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |
| [React](https://react.dev/learn) | Component-based web interfaces. |
| [Next.js](https://nextjs.org/docs) | React application framework with rendering and server features. |
| [Vue](https://vuejs.org/guide/) | Reactive component framework. |
| [Nuxt](https://nuxt.com/docs) | Vue application framework. |
| [Svelte and SvelteKit](https://svelte.dev/docs) | Compiled components and application framework. |
| [Angular](https://angular.dev/overview) | Web application framework with integrated tooling. |
| [Astro](https://docs.astro.build/) | Content sites and selective client interactivity. |
| [Vite](https://vite.dev/guide/) | Frontend development server and production build tooling. |
| [Tailwind CSS](https://tailwindcss.com/docs) | Utility-based CSS styling. |
| [Storybook](https://storybook.js.org/docs) | Component development, documentation and UI verification. |
| [Zod](https://zod.dev/) | TypeScript-oriented runtime schema validation. |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Client data fetching, caching and synchronization. |
| [FastAPI](https://fastapi.tiangolo.com/) | Python API framework with type-based validation. |
| [Django](https://docs.djangoproject.com/) | Python web framework with ORM, authentication and administration. |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python web application framework. |
| [Spring Boot](https://docs.spring.io/spring-boot/) | JVM application and service framework. |
| [Laravel](https://laravel.com/docs) | PHP web application framework. |
| [Ruby on Rails](https://guides.rubyonrails.org/) | Ruby web applications and conventions. |
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across targets. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |
| [PostgreSQL](https://www.postgresql.org/docs/) | Relational database, SQL, indexing and operational reference. |
| [SQLite](https://www.sqlite.org/docs.html) | Embedded relational storage; consider concurrency and backup strategy. |
| [DuckDB](https://duckdb.org/docs/) | Embedded analytical SQL and local data processing. |
| [MySQL](https://dev.mysql.com/doc/) | Relational database reference and connectors. HTTP access limited during verification; recheck directly. |
| [MongoDB](https://www.mongodb.com/docs/) | Document database and driver documentation. |
| [Redis](https://redis.io/docs/latest/) | In-memory data structures; evaluate release-specific licensing and persistence. |
| [Valkey](https://valkey.io/) | In-memory key-value service candidate and Redis-ecosystem compatibility reference. |
| [SQLAlchemy](https://docs.sqlalchemy.org/) | Python SQL expression layer and ORM. |
| [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) | .NET ORM, migrations and provider behaviors. |
| [Prisma](https://www.prisma.io/docs) | Typed data access and database migration workflows. |
| [Drizzle](https://orm.drizzle.team/docs/overview) | TypeScript SQL-oriented ORM and migrations. |
| [Flyway](https://documentation.red-gate.com/fd) | Versioned database migrations; check edition-specific features. |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy-oriented schema migrations. |
| [Apache Arrow](https://arrow.apache.org/docs/) | Columnar interchange and cross-language data tooling. |
| [Polars](https://docs.pola.rs/) | Dataframes and analytical transformations. |
| [pandas](https://pandas.pydata.org/docs/) | Python tabular data processing. |
| [ClickHouse](https://clickhouse.com/docs) | Columnar analytical database. |
| [OpenSearch](https://docs.opensearch.org/) | Search, indexing and analytics. |
| [Meilisearch](https://www.meilisearch.com/docs) | Application search APIs and indexing. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector similarity search service and clients. |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL vector storage and similarity indexing. |
| [NATS](https://docs.nats.io/) | Messaging and JetStream persistence; choose delivery semantics. |
| [Apache Kafka](https://kafka.apache.org/documentation/) | Distributed event streaming and clients. |
| [RabbitMQ](https://www.rabbitmq.com/docs) | Message broker, routing and delivery acknowledgments. |
| [Temporal](https://docs.temporal.io/) | Durable workflows; handle replay determinism, retries and external side effects. |
| [Celery](https://docs.celeryq.dev/) | Python task queues and workers. |
| [BullMQ](https://docs.bullmq.io/) | Redis-backed Node.js job processing. |
| [Hangfire](https://docs.hangfire.io/) | Persistent background work for .NET. |
| [Dapr](https://docs.dapr.io/) | Distributed application APIs and components; adds runtime infrastructure. |
| [AWS SDKs](https://aws.amazon.com/developer/tools/) | Official cloud SDKs and tooling; use workload-appropriate credentials. |
| [Azure SDKs](https://azure.github.io/azure-sdk/) | Official Azure client libraries and design guidance. |
| [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) | Language clients for Google Cloud APIs. |
| [Cloudflare API](https://developers.cloudflare.com/api/) | Cloudflare service management APIs. |
| [Cloudflare Workers](https://developers.cloudflare.com/workers/) | Edge application runtime and deployment tooling. |
| [Docker](https://docs.docker.com/) | Container builds and execution; check Desktop licensing where relevant. |
| [Podman](https://docs.podman.io/) | Container management; Windows development uses additional VM integration. |
| [Kubernetes](https://kubernetes.io/docs/) | Container orchestration and operational APIs. |
| [Helm](https://helm.sh/docs/) | Kubernetes packaging and release configuration. |
| [OpenTofu](https://opentofu.org/docs/) | Declarative infrastructure provisioning. |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | Infrastructure provisioning and provider ecosystem; review licensing. |
| [Pulumi](https://www.pulumi.com/docs/) | Infrastructure definitions using programming languages. |
| [Ansible](https://docs.ansible.com/) | Configuration automation and remote orchestration. HTTP access limited during verification; recheck directly. |
| [Render](https://render.com/docs) | Managed application hosting and deployment configuration. |
| [Vercel](https://vercel.com/docs) | Web application hosting and deployment. |
| [Supabase](https://supabase.com/docs) | Managed Postgres, auth, storage and realtime; evaluate RLS per application. |
| [Firebase](https://firebase.google.com/docs) | Application backend SDKs and managed services. |
| [Git](https://git-scm.com/doc) | Version control and repository operations. |
| [GitHub Actions](https://docs.github.com/en/actions) | Repository CI and automation; constrain workflow token permissions. |
| [GitLab CI](https://docs.gitlab.com/ci/) | Pipeline configuration and runners. |
| [Renovate](https://docs.renovatebot.com/) | Automated dependency updates with configurable policies. |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | GitHub dependency alerts and update workflows. |
| [Changesets](https://github.com/changesets/changesets) | Multi-package versioning and changelogs. |
| [semantic-release](https://semantic-release.gitbook.io/semantic-release/) | Automated release versioning and publishing. |
| [WiX Toolset](https://docs.firegiant.com/wix/) | Windows Installer packaging; review toolchain and commercial-service terms. |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Windows installer authoring and distribution. |
| [MSIX](https://learn.microsoft.com/en-us/windows/msix/) | Windows package format and deployment. |
| [Velopack](https://docs.velopack.io/) | Application packaging and updates; verify target support. |
| [Playwright](https://playwright.dev/docs/intro) | Browser end-to-end testing; install matching browser binaries. |
| [pytest](https://docs.pytest.org/) | Python unit and integration tests. |
| [Hypothesis](https://hypothesis.readthedocs.io/) | Property-based tests and shrinking for Python. |
| [Vitest](https://vitest.dev/guide/) | JavaScript and TypeScript test runner. |
| [Testing Library](https://testing-library.com/docs/) | UI tests using observable user-facing behavior. |
| [JUnit](https://junit.org/) | JVM testing framework. |
| [xUnit.net](https://xunit.net/) | .NET testing framework. |
| [GoogleTest](https://google.github.io/googletest/) | C++ unit tests and mocking. |
| [Catch2](https://github.com/catchorg/Catch2) | C++ test and benchmark framework. |
| [Testcontainers](https://docs.docker.com/testcontainers/) | Run real service dependencies in tests; needs a compatible container runtime. |
| [Pact](https://docs.pact.io/) | Consumer/provider contracts for HTTP and messages. |
| [WireMock](https://wiremock.org/docs/) | HTTP service stubs and integration simulations. |
| [k6](https://grafana.com/docs/k6/latest/) | Load and performance tests with explicit thresholds. |
| [Locust](https://docs.locust.io/) | Python-programmed load testing. |
| [BenchmarkDotNet](https://benchmarkdotnet.org/) | .NET microbenchmarking with controlled execution. |
| [Google Benchmark](https://github.com/google/benchmark) | C++ microbenchmarks; representative workload selection remains essential. |
| [LLVM sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html) | Native memory-error detection; support depends on platform and compiler. |
| [libFuzzer](https://llvm.org/docs/LibFuzzer.html) | Coverage-guided native fuzzing. |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance for authentication, validation and other security controls. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements. |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | API threat and review reference. |
| [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security guidance; read alongside applicable protocol specifications. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | Identity layer and interoperable authentication. |
| [WebAuthn](https://www.w3.org/TR/webauthn-3/) | Public-key authentication and passkey protocol reference; check implementation support. |
| [Keycloak](https://www.keycloak.org/documentation) | Self-hosted identity and federation. |
| [OpenFGA](https://openfga.dev/docs) | Relationship-based authorization modeling and SDKs. |
| [Open Policy Agent](https://www.openpolicyagent.org/docs) | Policy evaluation and authorization building block. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Dependency vulnerability discovery using OSV data. |
| [Trivy](https://trivy.dev/) | Container, dependency and configuration scanning. |
| [Semgrep](https://semgrep.dev/docs/) | Static code analysis and custom rules; edition features differ. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Detect committed secrets; rotate exposed credentials separately. |
| [Sigstore](https://docs.sigstore.dev/) | Artifact signing, verification and transparency tooling. |
| [SLSA](https://slsa.dev/) | Supply-chain provenance and assurance framework. |
| [CycloneDX](https://cyclonedx.org/) | Software bill of materials formats and ecosystem. |
| [SPDX](https://spdx.dev/) | Software inventory and license metadata standards. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Repository security-practice signals; not a security guarantee. |
| [libsodium](https://doc.libsodium.org/) | High-level cryptographic library; use supported primitives and key handling. |
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
| [GitHub REST API](https://docs.github.com/en/rest) | Repository, issue, pull-request and automation integration. |
| [GitHub Octokit](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api) | Official GitHub SDK entry point; select supported language and authentication. |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview) | Microsoft 365 and identity-backed APIs; scopes, consent and beta stability matter. |
| [Google Workspace](https://developers.google.com/workspace) | Docs, Sheets, Drive, Gmail and Calendar integration entry point. |
| [Stripe](https://docs.stripe.com/sdks) | Payments SDKs; align API version, webhook validation and idempotency. |
| [Twilio](https://www.twilio.com/docs/libraries) | Messaging, voice and communications SDKs. |
| [SendGrid](https://www.twilio.com/docs/sendgrid) | Transactional email APIs and deliverability integration. |
| [Resend](https://resend.com/docs) | Email API and SDK documentation. |
| [Slack API](https://api.slack.com/) | Workplace integration, events and bot interfaces. |
| [Discord](https://discord.com/developers/docs/intro) | Bot and application interfaces. |
| [Notion](https://developers.notion.com/) | Workspace content integration. |
| [Shopify](https://shopify.dev/docs) | Commerce applications, APIs and extensions. |
| [Mapbox](https://docs.mapbox.com/) | Maps, geocoding and navigation SDKs; review usage and data terms. |
| [Google Maps Platform](https://developers.google.com/maps/documentation) | Mapping, routing and places APIs; billing and retention rules vary. |
| [S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) | Object storage protocol reference; compatible providers can differ. |
| [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) | Official API clients and SDK entry point; recheck API and SDK support before implementation. |
| [Anthropic API](https://docs.anthropic.com/) | Model API and client integration reference. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Google model APIs and SDK documentation. |
| [Hugging Face Transformers](https://huggingface.co/docs/transformers/) | Model loading, tokenization and inference tooling. |
| [PyTorch](https://docs.pytorch.org/docs/stable/index.html) | Tensor operations, training and inference. |
| [ONNX Runtime](https://onnxruntime.ai/docs/) | Portable inference runtime; choose execution provider and architecture. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model inference; model licenses and hardware requirements are separate. |
| [Ollama](https://docs.ollama.com/) | Local model runtime and API. |
| [vLLM](https://docs.vllm.ai/) | Model serving and batching; verify supported hardware and OS. |
| [MLflow](https://mlflow.org/docs/latest/) | Experiment tracking, model lifecycle and evaluation. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs) | Tool and context integration protocol; authentication and trust need explicit design. |
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |
| [IETF RFC Editor](https://www.rfc-editor.org/) | Canonical internet protocol specifications and errata. |
| [W3C specifications](https://www.w3.org/TR/) | Web platform standards and maturity status. |
| [WHATWG](https://spec.whatwg.org/) | Living browser platform standards. |
| [CNCF Landscape](https://landscape.cncf.io/) | Infrastructure discovery map; listing is not endorsement. |
| [Apache projects](https://projects.apache.org/) | Discovery of Apache software and project status. |
| [Awesome lists](https://github.com/sindresorhus/awesome) | Broad discovery index; independently verify each candidate upstream. |


## Expansion 1 catalog additions

### Language tooling and repository automation

| Resource / official source | When useful and what to check |
|---|---|
| [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) | Editor-to-language-server protocol for completion, navigation and diagnostics; negotiate capabilities. |
| [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) | Debugger frontend/backend protocol; implementation capabilities vary. |
| [Tree-sitter](https://tree-sitter.github.io/tree-sitter/) | Incremental parsing for editors and code analysis; grammar versions matter. |
| [libgit2](https://libgit2.org/docs/) | Embed Git operations; check bindings, threading, transport and licensing exceptions. |
| [ripgrep](https://github.com/BurntSushi/ripgrep) | Fast repository text search respecting ignore rules. |
| [ast-grep](https://ast-grep.github.io/) | Structural code search and rewriting; test rewrite rules on real syntax. |
| [Comby](https://comby.dev/) | Structural source transformations using lightweight matching templates. |
| [just](https://just.systems/man/en/) | Repository command runner; shell and Windows recipe compatibility matter. |
| [mise](https://mise.jdx.dev/) | Development-tool version management and task execution; verify Windows feature support. |
| [sccache](https://github.com/mozilla/sccache) | Cache native and Rust compiler work; environment and compiler compatibility affect reuse. |
| [pre-commit](https://pre-commit.com/) | Manage repository hooks in isolated tool environments; CI should enforce required checks too. |
| [EditorConfig](https://editorconfig.org/) | Shared editor whitespace and formatting conventions. |

### .NET application building blocks

| Resource / official source | When useful and what to check |
|---|---|
| [Polly](https://www.pollydocs.org/) | Resilience pipelines for timeouts, retries and circuit breaking; avoid retrying unsafe operations. |
| [Refit](https://github.com/reactiveui/refit) | Typed interface-based .NET HTTP clients; verify serializer and AOT support. |
| [Dapper](https://github.com/DapperLib/Dapper) | Lightweight .NET SQL mapping; application owns SQL and schema evolution. |
| [FluentValidation](https://docs.fluentvalidation.net/en/latest/) | Typed .NET validation rules; confirm framework and async integration support. |
| [CommunityToolkit MVVM](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/) | Observable models, commands and source generators for .NET UI architectures. |
| [Noda Time](https://nodatime.org/) | Explicit .NET date/time types; distinguish instants, time zones and local times. |
| [Humanizer](https://github.com/Humanizr/Humanizer) | Human-readable text, quantities and relative times; check culture behavior. |
| [CsvHelper](https://joshclose.github.io/CsvHelper/) | .NET CSV parsing and writing; configure dialects and malformed-data handling. |
| [System.IO.Pipelines](https://learn.microsoft.com/en-us/dotnet/standard/io/pipelines) | High-performance .NET streaming buffers; manage ownership and backpressure. |

### Python Rust and Go building blocks

| Resource / official source | When useful and what to check |
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

### WebAssembly and plugin runtimes

| Resource / official source | When useful and what to check |
|---|---|
| [Wasmtime](https://docs.wasmtime.dev/) | Embed WebAssembly/WASI execution; expose only needed host capabilities. |
| [Wasmer](https://docs.wasmer.io/) | WebAssembly runtime and embedding ecosystem; verify bindings and target support. |
| [WASI](https://wasi.dev/) | System-interface specifications for WebAssembly; preview versions are not interchangeable. |
| [WebAssembly Component Model](https://component-model.bytecodealliance.org/) | Cross-language component interfaces and WIT; check runtime/toolchain interoperability. |
| [Extism](https://extism.org/docs/concepts/host-sdk/) | WebAssembly plugin SDKs and host integration; define permissions and plugin ABI. |
| [WAMR](https://github.com/wasm-micro-runtime/wasm-micro-runtime) | WebAssembly runtime for constrained and embedded hosts; upstream moved from bytecodealliance to wasm-micro-runtime. Check engines and architectures. |

### Collaboration local state and rich text

| Resource / official source | When useful and what to check |
|---|---|
| [Yjs](https://docs.yjs.dev/) | CRDT shared data for collaborative apps; persistence, transport and authorization are separate. |
| [Automerge](https://automerge.org/docs/hello/) | Local-first collaborative data structures and synchronization; assess storage growth and language support. |
| [ProseMirror](https://prosemirror.net/docs/) | Structured rich-text editing toolkit; application owns schema and collaboration policy. |
| [Tiptap](https://tiptap.dev/docs) | Rich-text editor built on ProseMirror; distinguish open-source extensions from paid services. |
| [Lexical](https://lexical.dev/docs/intro) | Extensible text-editor framework; evaluate import/export and accessibility. |
| [CodeMirror](https://codemirror.net/docs/) | Embeddable code editor and language extensions. |
| [Monaco Editor](https://microsoft.github.io/monaco-editor/) | Browser code editor; integrate web workers and bundling. Upstream states mobile browsers/frameworks are unsupported. |
| [Dexie](https://dexie.org/docs/) | IndexedDB wrapper for browser persistence; handle upgrades and storage limits. |
| [RxDB](https://rxdb.info/) | Reactive local database and replication; distinguish open-source and premium plugins. |

### Feature flags configuration and secrets

| Resource / official source | When useful and what to check |
|---|---|
| [OpenFeature](https://openfeature.dev/docs/reference/intro/) | Vendor-neutral feature-flag SDK interfaces; a provider supplies evaluation. |
| [Unleash](https://docs.getunleash.io/) | Feature-flag server and client SDKs; choose server/client evaluation boundaries. |
| [LaunchDarkly SDKs](https://launchdarkly.com/docs/sdk) | Hosted feature management SDKs; review account, pricing and data exposure. |
| [SOPS](https://getsops.io/) | Encrypted configuration files using key-management backends; plan key access and recovery. |
| [age](https://age-encryption.org/) | File encryption and recipient-based key tooling; manage private keys separately. |
| [Infisical](https://infisical.com/docs) | Secrets management and SDKs; review deployment model and edition boundaries. |
| [OpenBao](https://openbao.org/docs/) | Secrets and identity-based credential services; plan storage, unsealing and recovery. |
| [External Secrets Operator](https://external-secrets.io/) | Synchronize external secrets into Kubernetes; check refresh behavior and permissions. |
| [1Password SDKs](https://developer.1password.com/docs/sdks/) | Application access to vault items; confirm supported language and service-account scope. |

### Backup storage transfer and resilience

| Resource / official source | When useful and what to check |
|---|---|
| [restic](https://restic.readthedocs.io/en/stable/) | Encrypted versioned backups; test restores and protect repository credentials. |
| [rclone](https://rclone.org/docs/) | Transfer and synchronize data across storage providers; distinguish sync from versioned backup. |
| [Kopia](https://kopia.io/docs/) | Snapshot backup and encryption; validate retention and restore behavior. |
| [Litestream](https://litestream.io/) | Continuous SQLite replication for recovery; not multi-writer database replication. |
| [SQLite Online Backup API](https://www.sqlite.org/backup.html) | Consistent SQLite backup mechanism for application integration. |
| [Apache Iceberg](https://iceberg.apache.org/docs/latest/) | Analytical table format with schema/snapshot evolution; needs compatible engines and catalog. |
| [Delta Lake](https://docs.delta.io/) | Transactional analytical tables; check reader/writer protocol compatibility. |
| [Apache Parquet](https://parquet.apache.org/docs/) | Columnar file format and interoperability reference; check logical types and codecs. |

### Documents OCR and file formats

| Resource / official source | When useful and what to check |
|---|---|
| [Apache Tika](https://tika.apache.org/) | Extract file metadata and text; isolate untrusted parsers and verify format support. |
| [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/) | OCR engine and language data; measure accuracy on representative scans. |
| [PDFium](https://pdfium.googlesource.com/pdfium/) | PDF rendering engine; evaluate build complexity, bindings and security updates. |
| [MuPDF](https://mupdf.readthedocs.io/en/latest/) | PDF rendering and document toolkit; evaluate AGPL/commercial licensing. |
| [Apache PDFBox](https://pdfbox.apache.org/) | Java PDF creation, extraction and manipulation; test layout and font behavior. |
| [Apache POI](https://poi.apache.org/) | JVM Office file processing; validate document-feature fidelity. |
| [Open XML SDK](https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk) | Typed .NET Office document parts; does not provide Office layout rendering. |
| [ClosedXML](https://docs.closedxml.io/en/latest/) | .NET spreadsheet authoring; evaluate formula and workbook-feature support. |
| [python-docx](https://python-docx.readthedocs.io/) | Python Word document creation and editing; rendering requires another engine. |
| [pypdf](https://pypdf.readthedocs.io/en/stable/) | Python PDF structure manipulation and extraction; not a PDF renderer. |
| [Pillow](https://pillow.readthedocs.io/en/stable/) | Python raster-image processing; check codecs and decompression limits. |
| [libvips](https://www.libvips.org/) | Image-processing library for large images and pipelines; bindings require native runtime support. |

### Public data research and location APIs

| Resource / official source | When useful and what to check |
|---|---|
| [Open-Meteo](https://open-meteo.com/en/docs) | Forecast API; free hosted endpoint is for noncommercial use under its current terms. Review paid/commercial access, attribution, limits and units. |
| [US Census API](https://www.census.gov/data/developers.html) | US demographic and economic datasets; select vintage, geography and variables. |
| [FRED API](https://fred.stlouisfed.org/docs/api/fred/) | Economic-series API reference; the documentation served a maintenance page during this review. Recheck availability, API-key requirements and series usage terms before integration. |
| [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) | Development indicators API; review pagination, revisions and dataset licenses. |
| [NASA APIs](https://api.nasa.gov/) | Space and Earth-data API directory; service-specific keys, limits and availability vary. |
| [NOAA weather API](https://www.weather.gov/documentation/services-web-api) | US forecasts, alerts and observations; follow service identification and cache guidance. |
| [USGS water APIs](https://api.waterdata.usgs.gov/) | Water measurements and geospatial data; check endpoint lifecycle and units. |
| [OpenAlex](https://docs.openalex.org/) | Scholarly graph API; verify current key, quota and snapshot terms. |
| [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Scholarly metadata and DOI lookup; identify client and respect rate limits. |
| [Europe PMC](https://europepmc.org/RestfulWebService) | Literature metadata and available full text; full-text rights differ by article. Direct HTTP check returned 403; documentation excerpt reviewed through Exa. |
| [Wikidata Query Service](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service) | SPARQL over structured public knowledge; respect public-endpoint limits. |
| [OpenStreetMap Overpass](https://wiki.openstreetmap.org/wiki/Overpass_API) | Query OSM features; public instances have usage limits and ODbL obligations. |
| [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) | OSM geocoding software API; the OSMF public server has a separate policy including a 1 request/second maximum, identification and attribution. Check self-hosting or providers for heavier use. |
| [OSRM](https://project-osrm.org/docs/) | Routing engine and HTTP API; production hosting differs from public demos. |

### Optimization scheduling and operational tooling

| Resource / official source | When useful and what to check |
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


## Project-linked reference additions — 2026-10-22

Added for GitHub support, native DLL deployment and updater trust work. Only these three primary documentation pages were checked on this date; this is not a fresh audit of the complete catalog. No package, runtime installer or model was adopted. Linked documentation retains upstream terms.

| Category | Resource | Purpose and scoped verification |
|---|---|---|
| Platform SDKs and Windows | [WinHTTP request and redirect options](https://learn.microsoft.com/en-us/windows/win32/winhttp/option-flags) | Configure WinHTTP redirect, timeout and request options. Check option-setting return values; TLS downgrade refusal does not establish publisher authenticity or freshness. Primary option semantics read for UpdateKit trust review; loopback transport tested separately, not a TLS downgrade/certificate matrix. |
| Platform SDKs and Windows | [Microsoft Visual C++ runtime deployment](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) | Identify supported MSVC runtime packages and architecture/version requirements from Microsoft. Preserve redistribution terms; do not obtain individual runtime DLLs from arbitrary sites. Primary deployment/version and architecture guidance read for an x64 DLL import-table review; no installer downloaded or installed and clean-host acceptance not performed. |
| CI version control and releases | [GitHub private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository) | Provide a repository-specific private security-reporting route separate from public bug reports. Requires appropriate public-repository administration; notification delivery depends on account preferences. Primary configuration guidance read; enabled and read back on authorized project repositories. No test vulnerability submitted or notification-delivery guarantee. |

## Related persistent references

- (local research archive): 232 Windows-focused repositories, maintenance notes and revival candidates.
- (local research archive): stable WR-001 through WR-010 revival backlog; update its established user-facing copy when statuses change.

## Future upkeep

Add resources when a real task exposes a missing capability. Preserve canonical links, purpose, practical constraints and the evidence level. Update factual maintenance changes honestly. Refresh only relevant entries before adoption. No scheduled monitoring has been configured.

## Windows change investigation additions — 2026-10-22

Primary README and MIT license text reviewed for these entries only. No software executed, dependency adopted, or comprehensive maintenance/security audit performed. Linked projects retain upstream licensing.

| Resource | Purpose and limits |
|---|---|
| [Microsoft Attack Surface Analyzer](https://github.com/microsoft/AttackSurfaceAnalyzer) | Compare system security configuration snapshots with broad collectors and local SQLite evidence. MIT; README and license read 2026-10-22. Runtime, release maintenance and Windows compatibility need validation; not executed. |
| [WinLedger](https://github.com/fanyqe/winledger) | Local Windows before/after sessions for registry, services, tasks, startup, environment, firewall and selected files; conservative rollback. MIT license and README read 2026-10-22; Windows 11 x64/.NET 10 documented, not independently tested or adopted. |

## Project addition — 2026-10-22: GUI regression investigation

| Resource | Purpose and review scope |
|---|---|
| [DiffImg community fork](https://github.com/arbruijn/diffimg) | Standalone Qt/C++ image-difference GUI for screenshot/regression investigation. Community fork of sandsmark/lingo/xbee DiffImg, not the canonical original; has 2026 code activity. Qt5 Widgets/Qwt; GPLv2-or-later source and component notices require review. Compare WinMerge; Scoped Windows x64 revival: https://github.com/SeanShaffer88/DiffImg-Windows/releases/tag/v2.3.0-win1; legacy Qt baseline, no clean-VM/security-audit claim. |

Provenance: [xbee original on SourceForge](https://sourceforge.net/projects/diffimg/), [lingo fork](https://github.com/lingo/diffimg-xbee), [sandsmark fork](https://github.com/sandsmark/diffimg), then the linked arbruijn fork. GitHub default-branch commit inspected: `7c5715f89fb152c0d12a76a3e46a86122d7641bd` (2026-08-05). 2026-10-22 GitHub metadata/default-branch commit, SourceForge provenance, README, CMake/qmake and sampled component license notices inspected; no build, complete license audit or vulnerability review. Initial discovery did not validate a revival; see the follow-up build milestone below.

## Free Windows application research additions — 2026-10-22

2026-10-22 canonical GitHub metadata, README and license identification reviewed; source documentation only. No build, runtime/architecture validation, release audit, benchmark or security audit; not adopted. Linked projects retain their upstream licenses. These are implementation/reference candidates, not claims that a new product has been built.

| Resource | Purpose and constraints |
|---|---|
| [Dumpling (.NET heap analysis)](https://github.com/CoreyKaylor/dotnet-dumpling) | Apache-2.0 CLI and MCP candidate for .NET heap comparisons, retention paths and dominator analysis. Upstream documents .gcdump and ClrMD process-dump support; unarchived, repository pushed 2026-08-14. Validate format fidelity, memory use, distribution and supported runtimes before reuse. |
| [dotnet-heapview](https://github.com/1hub/dotnet-heapview) | MIT desktop heap viewer, shared heap model and MCP source example. Upstream lists .gcdump, .hprof and .mono-heap inputs; unarchived, repository pushed 2026-09-21. Compare PerfView and Dumpling; GUI completeness, packaging and Windows runtime support remain untested. |
| [Camelot PDF table extraction](https://github.com/camelot-dev/camelot) | MIT Python table-extraction library and CLI. Current source documents text-table parsers and optional ML/OCR for scans; Python >=3.10, PDFium default backend. Unarchived, repository pushed 2026-10-14. Pin a released version; benchmark accuracy, Windows wheels and optional model/dependency licenses before packaging. |


## Android APK development and analysis additions — 2026-10-22

Primary documentation/README excerpts and selected upstream repository metadata reviewed. See [practical APK guide](../docs/android-apk-development.md). No comprehensive adoption, security or license audit and no automatic dependency installation.

| Category | Resource | Purpose and review scope |
|---|---|---|
| Android APK development and analysis | [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) | Inspect manifest, DEX, resources and package size in Android Studio. |
| Android APK development and analysis | [apkanalyzer](https://developer.android.com/tools/apkanalyzer) | Scriptable package, manifest, DEX and resource inspection. |
| Android APK development and analysis | [Android CLI](https://developer.android.com/tools/android-cli) | Current command-line Android project and SDK workflows; recheck availability before replacing existing tooling. |
| Android APK development and analysis | [sdkmanager](https://developer.android.com/tools/sdkmanager) | SDK package management reference; fetched page marks it deprecated in favor of Android CLI, while existing SDK installations still use it. |
| Android APK development and analysis | [Android command-line builds](https://developer.android.com/build/building-cmdline) | Gradle-wrapper builds of APKs and app bundles from source. |
| Android APK development and analysis | [Android Gradle Plugin](https://developer.android.com/build/releases/about-agp) | Build-system compatibility and release guidance; pin compatible AGP, Gradle and JDK versions. |
| Android APK development and analysis | [Android build JDKs](https://developer.android.com/build/jdks) | Distinguish Gradle runtime JDK, toolchains, source levels and Android API availability. |
| Android APK development and analysis | [AAPT2](https://developer.android.com/tools/aapt2) | Compile/link Android resources and inspect packaging problems. |
| Android APK development and analysis | [D8](https://developer.android.com/tools/d8) | Convert Java bytecode to Android DEX; preserve minSdk and library/desugaring inputs. |
| Android APK development and analysis | [Apksigner](https://developer.android.com/tools/apksigner) | Sign and verify APKs; every subsequent byte modification invalidates signatures. |
| Android APK development and analysis | [Zipalign](https://developer.android.com/tools/zipalign) | Verify APK entry alignment; align before apksigner signing. |
| Android APK development and analysis | [App bundle format](https://developer.android.com/guide/app-bundle/app-bundle-format) | Understand base, feature and configuration splits versus distributable APKs. |
| Android APK development and analysis | [Bundletool](https://developer.android.com/tools/bundletool) | Generate and install device-specific APK sets from AABs; not a universal arbitrary-APK merger. |
| Android APK development and analysis | [Android app updates](https://developer.android.com/google/play/app-updates) | Package identity, signing compatibility and version rules for preserving installed data. |
| Android APK development and analysis | [APK signature v4](https://source.android.com/docs/security/features/apksigning/v4) | Understand incremental-install idsig sidecars and their relationship to APK signing. |
| Android APK development and analysis | [Android ABIs](https://developer.android.com/ndk/guides/abis) | Native architectures, calling conventions and packaging requirements. |
| Android APK development and analysis | [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes) | Separate native ELF alignment, ZIP alignment and runtime page-size assumptions. |
| Android APK development and analysis | [Android compatibility](https://developer.android.com/guide/app-compatibility) | Separate behavior changes affecting all apps from changes gated by target SDK. |
| Android APK development and analysis | [Android storage](https://developer.android.com/training/data-storage) | App-specific files, shared storage and permissions; scoped-storage implications. |
| Android APK development and analysis | [ADB](https://developer.android.com/tools/adb) | Install, inspect, launch and debug on authorized devices and emulators. |
| Android APK development and analysis | [Logcat](https://developer.android.com/tools/logcat) | Capture complete startup exceptions and correlate package/process logs. |
| Android APK development and analysis | [NDK stack symbolization](https://developer.android.com/ndk/guides/ndk-stack) | Symbolize native crash traces with exact matching unstripped libraries. |
| Android APK development and analysis | [Android testing](https://developer.android.com/studio/test) | Source-level and device test workflows; complement package checks with gameplay tests. |
| Android APK development and analysis | [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) | Understand install-time, fast-follow and on-demand game assets. |
| Android APK development and analysis | [APK expansion files](https://developer.android.com/google/play/expansion-files) | Legacy OBB naming, storage and downloader model; distinguish from custom caches. |
| Android APK development and analysis | [Offline-first architecture](https://developer.android.com/topic/architecture/data-layer/offline-first) | Local data sources, persistence and synchronization architecture; server-dependent games may need more than cached assets. |
| Android APK development and analysis | [Unity IL2CPP](https://docs.unity3d.com/Manual/IL2CPP.html) | AOT managed-to-native scripting backend; metadata stubs are not recovered game source. |
| Android APK development and analysis | [Unity AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html) | Runtime asset archives; match platform, engine and serialized type compatibility. |
| Android APK development and analysis | [Apktool](https://github.com/iBotPeaches/Apktool) | Decode/rebuild Android resources and smali; framework packages and exact tool version matter. |
| Android APK development and analysis | [JADX](https://github.com/skylot/jadx) | Java-like DEX decompilation for analysis; output is not a guaranteed recompilable source project. |
| Android APK development and analysis | [Google smali/baksmali](https://github.com/google/smali) | DEX assembler/disassembler and dexlib2; maintained fork, mixed component licenses require review. |
| Android APK development and analysis | [APKEditor](https://github.com/REAndroid/APKEditor) | Alternative resource decode/build, split merging and resource repair; validate merged manifests, ABIs and signatures. |
| Android APK development and analysis | [ARSCLib](https://github.com/REAndroid/ARSCLib) | Programmatic Android resource-table/binary-XML editing without aapt2. |
| Android APK development and analysis | [Androguard](https://github.com/androguard/androguard) | Python APK/DEX/resource inspection and analysis; select supported Python/tool version. |
| Android APK development and analysis | [APKiD](https://github.com/rednaga/APKiD) | Identify packers, protectors and obfuscators; heuristic classification, not decryption or a security verdict. |
| Android APK development and analysis | [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Local static/dynamic mobile security analysis; separate service requirements and report false positives. |
| Android APK development and analysis | [OWASP MASTG](https://mas.owasp.org/MASTG/) | Mobile testing/reverse-engineering methodology and tool references. |
| Android APK development and analysis | [Frida Android](https://frida.re/docs/android/) | Runtime instrumentation on controlled devices; server/gadget, ABI and version compatibility matter. |
| Android APK development and analysis | [Objection](https://github.com/sensepost/objection) | Frida-based runtime exploration; gadget patching changes package and signing behavior. |
| Android APK development and analysis | [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) | Recover IL2CPP metadata/type/method maps and dummy assemblies; older maintenance, exact metadata-version limits. |
| Android APK development and analysis | [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) | Work-in-progress IL2CPP analysis and reconstruction; validate output against native instructions. |
| Android APK development and analysis | [UnityPy](https://github.com/K0lb3/UnityPy) | Script extraction and modification of Unity serialized assets; preserve references and re-read written output. |
| Android APK development and analysis | [AssetRipper](https://github.com/AssetRipper/AssetRipper) | Unity game-file analysis/export; exported projects do not imply complete recoverable source or behavior. |
| Android APK development and analysis | [UABEA](https://github.com/nesrak1/UABEA) | Unity bundle/serialized asset inspection and editing; upstream points to UABEANext as work in progress. |
| Android APK development and analysis | [UABEANext](https://github.com/nesrak1/UABEANext) | New multi-bundle Unity editor; work-in-progress successor, not a compatibility guarantee. |
| Android APK development and analysis | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Native ELF disassembly/decompilation; apply exact architecture, symbols and relocations. |
| Android APK development and analysis | [Keystone](https://github.com/keystone-engine/keystone) | Assemble architecture-specific native patches; GPL/commercial and component licensing require review. |
| Android APK development and analysis | [Unicorn](https://github.com/unicorn-engine/unicorn) | CPU-level execution of native patch tests; mocked framework boundaries do not test Android runtime behavior. |
| Android APK development and analysis | [pyelftools](https://github.com/eliben/pyelftools) | Read ELF headers, segments and symbols; translate RVAs through PT_LOAD segments rather than assuming file offsets. |
| Android APK development and analysis | [APKLab](https://github.com/APKLab/APKLab) | VS Code integration of APK analysis, smali and rebuild workflows; inspect bundled tools and AGPL license obligations. |
| Android APK development and analysis | [Flutter build modes](https://docs.flutter.dev/testing/build-modes) | Distinguish Flutter debug/JIT from release AOT artifacts before choosing an analysis path. |
| Android APK development and analysis | [React Native Android releases](https://reactnative.dev/docs/signed-apk-android) | Understand JS/assets, native packaging and signing of React Native Android builds. |
| Android APK development and analysis | [Godot Android export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html) | Godot Android toolchain, templates, package data and signing requirements. |
| Android APK development and analysis | [Perfetto](https://perfetto.dev/docs/) | System/app tracing for startup, scheduling and performance investigation. |
| Android APK development and analysis | [Android Monkey](https://developer.android.com/studio/test/monkey) | Device UI event stress testing; bound runs and inspect results rather than treating no crash as correctness. |

## Project follow-up — 2026-10-22: DiffImg Windows build milestone

[DiffImg Windows x64 revival milestone](https://github.com/SeanShaffer88/DiffImg-Windows/releases/tag/v2.3.0-win1) published with GUI/CLI, corresponding application/Qtbase/Qwt sources and verified uploaded asset digests. 17 native cases and 30 CLI checks passed; repeated from relocated/Unicode paths with SDK paths removed. GUI/CLI executables were byte-identical across clean build directories. Qwt DLL bytes vary with MSVC anonymous-namespace names tied to the build path. No clean-VM validation, full codec audit, Qt6 port, x86 or ARM64 support is claimed. Existing WR task IDs are unchanged.

| Resource | Purpose and checks |
|---|---|
| [aqtinstall](https://github.com/miurahr/aqtinstall) | Install explicitly selected Qt SDK archive versions and architectures without a global Qt setup. MIT installer; Qt SDK/runtime licenses remain separate. Used aqtinstall 3.3.0 to obtain pinned Qt 5.15.2 MSVC2019 x64 archives for DiffImg; archive SHA256 values recorded. |
| [Qwt](https://qwt.sourceforge.io/) | Qt technical plotting widgets. Qwt License 1.0 (LGPL2.1 with exceptions); retain notices and evaluate Qt/runtime licenses. Built pinned Qwt 6.3.0 source with Qt5/MSVC x64 for DiffImg. Rebuilds worked, but MSVC anonymous-namespace RTTI makes DLL bytes vary with build path. |

## HeapTrail for .NET preview — 2026-10-22

| Resource | Purpose and constraints |
|---|---|
| [HeapTrail for .NET](https://github.com/SeanShaffer88/HeapTrail) | Free MIT Windows x64 .NET heap investigation desktop: compare .gcdump counts/shallow bytes, inspect root/incoming/outgoing paths, save notes and export local HTML. Unsigned self-contained preview; no live attachment, retained-size/dominator analysis or allocation stacks. |

First-party scope: [v0.1.0-preview.1](https://github.com/SeanShaffer88/HeapTrail/releases/tag/v0.1.0-preview.1), source commit `0ba60bc84c4727147723b6c275eeae4cbd5336fc`. Fifteen graph/persistence/report checks include a real event leak growing 1 → 25 → 1 after a fix and a cache staying at 4. Four additional importer checks cover success, failure, cancellation and cleanup. Desktop workflow and extracted portable runtime were exercised. [Windows CI passed on this source](https://github.com/SeanShaffer88/HeapTrail/actions/runs/39753330962). Uses Microsoft's MIT diagnostics reader; dependency/license provenance is recorded in the project. This is an unsigned preview, not a complete profiler or security audit. Capture completeness, large/sampled heaps, ARM64/x86 and older runtimes remain limits; paths show reachability, not exclusive retained size.
