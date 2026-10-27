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

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [oclif](https://github.com/oclif/oclif) | CLI for generating, building, and releasing oclif CLIs. Built by Salesforce. |
| [nyc](https://github.com/istanbuljs/nyc) | the Istanbul command line interface |
| [atuin](https://github.com/atuinsh/atuin) | ✨ Making your shell magical |
| [aichat](https://github.com/sigoden/aichat) | All-in-one LLM CLI tool featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents, with access to OpenAI, Claude, Gemini, Ollama, Groq, and more. |
| [skills-manager](https://github.com/xingkongliang/skills-manager) | A lightweight desktop app to manage, sync, and organize AI agent skills across 50+ coding tools — Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. |
| [Kaku](https://github.com/tw93/Kaku) | A fast, good-looking, AI-friendly terminal for the Mac. |
| [nostr-vpn](https://github.com/mmalmi/nostr-vpn) | Private mesh VPN for humans and agents. Local keys, signed enrollment, no provider account. Native apps and CLI. |
| [kong](https://github.com/alecthomas/kong) | Kong is a command-line parser for Go |
| [upterm](https://github.com/owenthereal/upterm) | Instant Terminal Sharing |
| [SSH.NET](https://github.com/sshnet/SSH.NET) | SSH.NET is a Secure Shell (SSH) library for .NET, optimized for parallelism. |
| [commandline](https://github.com/commandlineparser/commandline) | The best C# command line parser that brings standardized *nix getopt style, for .NET. Includes F# support |
| [assimp](https://github.com/assimp/assimp) | The official Open-Asset-Importer-Library Repository. Loads 40+ 3D-file-formats into one unified and clean data structure. |
| [phpggc](https://github.com/ambionics/phpggc) | PHPGGC is a library of PHP unserialize() payloads along with a tool to generate them, from command line or programmatically. |
| [fvm](https://github.com/btwld/fvm) | Flutter Version Management: A simple CLI to manage Flutter SDK versions. |
| [starship](https://github.com/starship/starship) | ☄🌌️ The minimal, blazing-fast, and infinitely customizable prompt for any shell! |
| [gitui](https://github.com/gitui-org/gitui) | Blazing 💥 fast terminal-ui for git written in rust 🦀 |
| [nnn](https://github.com/jarun/nnn) | n³ The unorthodox terminal file manager |
| [asciinema](https://github.com/asciinema/asciinema) | Terminal session recorder, streamer and player 📹 |
| [gotty](https://github.com/yudai/gotty) | Share your terminal as a web application |
| [sshuttle](https://github.com/sshuttle/sshuttle) | Transparent proxy server that works as a poor man's VPN. Forwards over ssh. Doesn't require admin. Works with Linux and MacOS. Supports DNS tunneling. |
| [npm-check-updates](https://github.com/raineorshine/npm-check-updates) | Find newer versions of package dependencies than what your package.json allows |
| [visidata](https://github.com/saulpw/visidata) | A terminal spreadsheet multitool for discovering and arranging data |
| [release-it](https://github.com/release-it/release-it) | 🚀 Automate versioning and package publishing |
| [skim](https://github.com/skim-rs/skim) | Fuzzy Finder in rust! |
| [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt) | An informative and fancy bash prompt for Git users |
| [git-standup](https://github.com/nilbuild/git-standup) | Recall what you or your team did on the last working day |
| [xxh](https://github.com/xxh/xxh) | 🚀 Bring your favorite shell wherever you go through the ssh. Xonsh shell, fish, zsh, osquery and so on. |
| [themer](https://github.com/mjswensen/themer) | 🎨 themer takes a set of colors and outputs themes for your apps (editors, terminals, wallpapers, and more). |
| [git-stats](https://github.com/IonicaBizau/git-stats) | 🍀 Local git statistics including GitHub-like contributions calendars. |
| [emacs](https://github.com/emacs-mirror/emacs) | Mirror of GNU Emacs |
| [freeze](https://github.com/charmbracelet/freeze) | Generate images of code and terminal output 📸 |
| [musikcube](https://github.com/clangen/musikcube) | a cross-platform, terminal-based music player, audio engine, metadata indexer, and server in c++ |
