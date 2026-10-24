# Testing verification and performance

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
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

Project discovery checked 2026-10-22 (source inspection only; no tested revival):

| Resource | Useful for / constraints |
|---|---|
| [DiffImg community fork](https://github.com/arbruijn/diffimg) | Standalone Qt/C++ screenshot-difference GUI. arbruijn fork descends from sandsmark/lingo/xbee; independent Windows Qt 6.12 x64 revival: https://github.com/SeanShaffer88/DiffImg-Windows/releases/tag/v2.6.0 . Adds JSON/JUnit CI reports, failure-file navigation, scoped HTML exports and RGB pixel inspection atop folder comparisons, profiles/masks and recoverable baseline approval. GPLv3 binary distribution with corresponding sources/notices; self-signed Authenticode is not public Windows trust. Equal dimensions and 8-bit white-matte RGB; compare WinMerge. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [fast-check](https://github.com/dubzzz/fast-check) | Generate and shrink JavaScript/TypeScript property tests; retain seeds for reproducibility. |
| [Mock Service Worker](https://github.com/mswjs/msw) | Intercept network requests in browser and Node tests; keep mocks aligned with real contracts. |
| [tox](https://github.com/tox-dev/tox) | Run Python checks across isolated environments; provision the required interpreter versions. |
| [Nox](https://github.com/wntrblm/nox) | Define Python test sessions as code; manage interpreter and dependency matrices explicitly. |
| [StrykerJS](https://github.com/stryker-mutator/stryker-js) | Mutation testing for JavaScript and TypeScript; budget runtime and inspect equivalent mutants. |
| [mutmut](https://github.com/boxed/mutmut) | Find Python test gaps through mutation; upstream requires WSL on Windows. Run against committed test code and inspect surviving mutations. |
| [jqwik](https://github.com/jqwik-team/jqwik) | Property-based tests on the JUnit Platform. Upstream reports maintenance mode and an additional Anti-AI Usage Clause from v1.10; review those terms before use. |
| [TLA+ tools](https://github.com/tlaplus/tlaplus) | Model concurrent protocols and check invariants; bounded models do not prove implementation correctness. |
| [cargo-nextest](https://github.com/nextest-rs/nextest) | Run Rust test binaries with scheduling and retries; confirm differences from cargo test. |
| [proptest](https://github.com/proptest-rs/proptest) | Property-based Rust tests with shrinking; persist regressions and constrain generators. |
