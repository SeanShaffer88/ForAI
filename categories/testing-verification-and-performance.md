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
