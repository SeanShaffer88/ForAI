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
