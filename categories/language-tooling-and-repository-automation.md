# Language tooling and repository automation

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
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

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [fd](https://github.com/sharkdp/fd) | Find filesystem paths with convenient filtering; account for hidden and ignored-file defaults. |
| [fzf](https://github.com/junegunn/fzf) | Interactive fuzzy selection for terminal workflows; inspect commands bound to selected input. |
| [bat](https://github.com/sharkdp/bat) | Inspect source with syntax highlighting and Git context; configure paging for automation. |
| [eza](https://github.com/eza-community/eza) | Explore filesystem listings with extra metadata; verify support on the intended platform. |
| [delta](https://github.com/dandavison/delta) | Improve terminal diff presentation; preserve raw patches for programmatic processing. |
| [Watchexec](https://github.com/watchexec/watchexec) | Run commands when files change; control watch scope and restart behavior. |
| [entr](https://github.com/eradman/entr) | Trigger commands from changed files on Unix-like systems; use alternatives where native support is absent. |
| [Task](https://github.com/go-task/task) | Define repeatable tasks in YAML; verify shell behavior across target platforms. |
| [Hyperfine](https://github.com/sharkdp/hyperfine) | Benchmark command-line programs statistically; control warmup, caches and background load. |
| [git-cliff](https://github.com/orhun/git-cliff) | Generate changelogs from Git history; configure grouping and release boundaries. |
