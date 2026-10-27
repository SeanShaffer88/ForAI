# Builds packages and environments

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
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

Project addition checked 2026-10-22:

| Resource | Useful for / constraints |
|---|---|
| [aqtinstall](https://github.com/miurahr/aqtinstall) | Install explicitly selected Qt SDK archive versions and architectures without a global Qt setup. MIT installer; Qt SDK/runtime licenses remain separate. Used aqtinstall 3.3.0 to obtain pinned Qt 5.15.2 MSVC2019 x64 archives for DiffImg; archive SHA256 values recorded. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Pants](https://github.com/pantsbuild/pants) | Coordinate builds and tests in multi-language repositories; adopt incrementally around supported backends. |
| [Buck2](https://github.com/facebook/buck2) | Build large dependency graphs with caching; plan toolchains and build-rule ownership. |
| [Please](https://github.com/thought-machine/please) | Reproducible multi-language builds; upstream lists Linux, macOS and FreeBSD as actively supported. Verify other platforms before adoption. |
| [Xmake](https://github.com/xmake-io/xmake) | Configure native builds using Lua; inspect toolchain and package integration. |
| [ccache](https://github.com/ccache/ccache) | Cache C and C++ compilation results; configure cache keys and shared-storage trust. |
| [mold](https://github.com/rui314/mold) | Accelerate native linking on supported platforms; verify linker compatibility and deployment licenses. |
| [esbuild](https://github.com/evanw/esbuild) | Bundle and transform JavaScript and TypeScript quickly; run type checking separately. |
| [SWC](https://github.com/swc-project/swc) | Compile and transform JavaScript/TypeScript with Rust tooling; verify plugin and syntax compatibility. |
| [Oxc](https://github.com/oxc-project/oxc) | Rust-based JavaScript tooling components; evaluate individual parser, lint and transform maturity. |
| [Biome](https://github.com/biomejs/biome) | Format and lint web code with unified tooling; check language and rule coverage before migration. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [xo](https://github.com/xojs/xo) | ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults |
| [Nuitka](https://github.com/Nuitka/Nuitka) | Nuitka is a Python compiler written in Python. It's fully compatible with Python 2.6, 2.7, 3.4-3.14. You feed it your Python app, it does a lot of clever things, and spits out an executable or extension module. |
| [turborepo](https://github.com/vercel/turborepo) | Build system optimized for JavaScript and TypeScript, written in Rust |
| [golangci-lint](https://github.com/golangci/golangci-lint) | Fast linters runner for Go |
| [peachpie](https://github.com/peachpiecompiler/peachpie) | PeachPie - the PHP compiler and runtime for .NET and .NET Core |
| [Caliburn.Micro](https://github.com/Caliburn-Micro/Caliburn.Micro) | A small, yet powerful framework, designed for building applications across all XAML platforms. Its strong support for MV* patterns will enable you to build your solution quickly, without the need to sacrifice code quality or testability. |
| [hadolint](https://github.com/hadolint/hadolint) | Dockerfile linter, validate inline bash, written in Haskell |
