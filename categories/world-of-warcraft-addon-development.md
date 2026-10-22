# World of Warcraft addon development

[All categories](README.md) · [AI selection guide](../AGENTS.md)

## World of Warcraft addon development — added 2026-10-22

2026-10-22 scoped primary/project-source inspection; Forever 1.60.1 addon development; not a complete API, security or license audit.

| Resource | Purpose and constraints |
|---|---|
| [Lua 5.1 reference manual](https://www.lua.org/manual/5.1/) | Language reference for legacy Lua syntax used by WoW addon hosts. Lua is MIT; this is documentation, not an installed runtime. Modern Forever host APIs are separate from the language version. |
| [Lupa](https://pypi.org/project/lupa/) | Python wrapper for Lua/LuaJIT. Development-only Lua 5.1 execution for addon behavior tests. Lupa 2.8 Windows x64 CPython 3.12 wheel and lua51 runtime exercised locally; MIT-style wrapper license; retain component notices if redistributing. Host mocks do not reproduce WoW taint or secret values. |
| [WoW UI source mirror](https://github.com/Gethe/wow-ui-source) | Third-party mirror of Blizzard UI and generated API documentation. Forever branch inspected at ca8368f2f2380cbe696854f7f2646387c278a61b. Useful for modern namespaced APIs despite interface 16001; Blizzard material retains its terms, not a permissive code dependency or guaranteed exact local-build match. |
| [Tweaks Forever](https://github.com/cjber/tweaks-forever) | Active Forever QoL addon reference for optional modules and conflicts. Author README and installed v0.15.2 metadata inspected; GPL-3.0-or-later with separately attributed data and libraries. Verify exact source, assets and current client support before any port or reuse. |
