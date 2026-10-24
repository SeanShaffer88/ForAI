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
