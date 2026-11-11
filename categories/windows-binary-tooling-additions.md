# Windows / Binary tooling additions

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [capstone-engine/capstone](https://github.com/capstone-engine/capstone) | Multi-architecture instruction disassembly ; Native library |
| [zyantific/zydis](https://github.com/zyantific/zydis) | Fast x86 and x64 disassembly and instruction encoding ; Native library |
| [rizinorg/cutter](https://github.com/rizinorg/cutter) | Graphical binary analysis and reverse engineering ; Desktop tool |
| [EasyHook/EasyHook](https://github.com/EasyHook/EasyHook) | Bridge managed and unmanaged API interception ; Check supported .NET and OS versions |
| [stevemk14ebr/PolyHook_2_0](https://github.com/stevemk14ebr/PolyHook_2_0) | C++ x86 and x64 function interception ; Native instrumentation library |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [Detect It Easy (DIE)](https://github.com/horsicq/DIE-engine) | Signature and heuristic detection for packers, compilers, and file formats. Good first triage on unknown binaries; signatures need maintenance to stay current. |
| [dnSpyEx](https://github.com/dnSpyEx/dnSpy) | Community revival of the .NET debugger and assembly editor: decompile, edit, and debug IL. GPL-3.0; validate output against original assemblies and never patch third-party binaries you lack rights to. |
| [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language, data inspectors, and binary diffing. GPL-2.0; useful for structure discovery before writing parsers. |
| [radare2](https://github.com/radareorg/radare2) | Reverse-engineering framework and CLI toolset for disassembly, analysis, and binary patching. Steep learning curve; license mixes LGPL components with the project's own terms. |
<!-- expansion-2026-11-10:end -->
