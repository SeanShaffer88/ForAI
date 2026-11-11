# Builds packages and environments

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [uv](https://docs.astral.sh/uv/) | Python environment, package, tool and project management. |
| [Ruff](https://docs.astral.sh/ruff/) | Extremely fast Python linter and formatter written in Rust; replaces Flake8/Black/isort in one tool — check rule coverage against your existing lint setup. |
| [PyPA Packaging Guide](https://packaging.python.org/) | Python distribution, build metadata and publishing. |
| [npm](https://docs.npmjs.com/) | JavaScript packages, registry and lockfile workflows. |
| [pnpm](https://pnpm.io/) | JavaScript workspace and package management. |
| [NuGet](https://learn.microsoft.com/en-us/nuget/) | .NET dependency packaging and restore: the standard package manager and feed format for .NET libraries; private feeds need their own hosting or Azure Artifacts/GitHub Packages. |
| [CMake](https://cmake.org/documentation/) | Generate native build systems and manage target configuration. |
| [Ninja](https://ninja-build.org/manual.html) | Executes generated native build graphs: a tiny, very fast build executor meant to be driven by a generator such as CMake or Meson, not hand-written. |
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
| [golangci-lint](https://github.com/golangci/golangci-lint) | Fast linters runner for Go: runs dozens of linters in parallel with one config; the standard Go lint gate in CI. |
| [peachpie](https://github.com/peachpiecompiler/peachpie) | PeachPie - the PHP compiler and runtime for .NET and .NET Core |
| [Caliburn.Micro](https://github.com/Caliburn-Micro/Caliburn.Micro) | A small, yet powerful framework, designed for building applications across all XAML platforms. Its strong support for MV* patterns will enable you to build your solution quickly, without the need to sacrifice code quality or testability. |
| [hadolint](https://github.com/hadolint/hadolint) | Dockerfile linter, validate inline bash, written in Haskell |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [asdf](https://github.com/asdf-vm/asdf) | Pluggable version manager for many runtimes through one `.tool-versions` file. Compare with mise for speed and task running; plugin quality and Windows support vary. |
| [Chocolatey](https://github.com/chocolatey/choco) | Machine-wide Windows package manager using NuGet-style packages and PowerShell scripts. Apache-2.0 for the client; review package scripts and licensing before installing with elevated rights. |
| [conda](https://github.com/conda/conda) | Cross-language binary package and environment manager, historically important for scientific and native Python stacks. BSD-3-Clause; channel and solver choice materially change reproducibility. |
| [Devbox](https://github.com/jetify-com/devbox) | Reproducible per-project development shells built on Nix, with a JSON manifest and lockfile. Nice ergonomics; the Nix store is a real dependency and Windows support is not native. |
| [Poetry](https://github.com/python-poetry/poetry) | Python dependency management and packaging with lockfiles and a pyproject-based workflow. Compare against uv and pip-tools for speed and lock resolution policy; both formats differ. |
| [Scoop](https://github.com/ScoopInstaller/Scoop) | User-scope Windows package manager driven by Git manifests, requiring no administrator rights. Convenient for developer tooling; per-user installs and manifest freshness differ from winget or Chocolatey. |
<!-- expansion-2026-11-10:end -->

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [babel (babel)](https://github.com/babel/babel) | Babel is a compiler for writing next generation JavaScript. |
| [berry](https://github.com/yarnpkg/berry) | Active development trunk for Yarn. |
| [brew](https://github.com/Homebrew/brew) | The Package Manager for Everywhere. |
| [cargo](https://github.com/rust-lang/cargo) | The Rust package manager. |
| [farm](https://github.com/farm-fe/farm) | Extremely fast Vite-compatible web build tool written in Rust. |
| [grunt](https://github.com/gruntjs/grunt) | Grunt: The JavaScript Task Runner. |
| [hatch](https://github.com/pypa/hatch) | Modern, extensible Python project management. |
| [home manager](https://github.com/nix-community/home-manager) | Manage a user environment using Nix [maintainer=@khaneliman, @rycee]. |
| [lightningcss](https://github.com/parcel-bundler/lightningcss) | An extremely fast CSS parser, transformer, bundler, and minifier written in Rust. MPL-2.0: file-level copyleft; modified files must be published. |
| [miniforge](https://github.com/conda-forge/miniforge) | A conda-forge distribution. License not detected by GitHub; check the repository license before use. |
| [nix](https://github.com/NixOS/nix) | Nix, the purely functional package manager. LGPL-2.1: dynamic linking is permitted, static linking has obligations. |
| [nixpkgs](https://github.com/NixOS/nixpkgs) | Nix Packages collection & NixOS. |
| [parcel](https://github.com/parcel-bundler/parcel) | The zero configuration build tool for the web. |
| [pdm](https://github.com/pdm-project/pdm) | A modern Python package and dependency manager supporting the latest PEP standards. |
| [peru](https://github.com/buildinspace/peru) | a generic package manager, for including other people's code in your projects. |
| [pip](https://github.com/pypa/pip) | The Python package installer. |
| [pyenv](https://github.com/pyenv/pyenv) | Simple Python version management. |
| [rollup](https://github.com/rollup/rollup) | Next-generation ES module bundler. License not detected by GitHub; check the repository license before use. |
| [rspack](https://github.com/web-infra-dev/rspack) | Fast Rust-based bundler for the web with a modernized webpack API. |
| [sbt](https://github.com/sbt/sbt) | sbt, the interactive build tool. |
| [spack](https://github.com/spack/spack) | A flexible package manager that supports multiple versions, configurations, platforms, and compilers. |
| [webpack](https://github.com/webpack/webpack) | A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. |
<!-- expansion-2026-11-11:end -->
