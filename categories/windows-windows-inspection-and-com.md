# Windows / Windows inspection and COM

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [hakril/PythonForWindows](https://github.com/hakril/PythonForWindows) | Python abstractions over Windows native APIs ALPC RPC and execution ; ctypes-based Python library for x86 and x64 |
| [tyranid/oleviewdotnet](https://github.com/tyranid/oleviewdotnet) | Inspect COM registrations interfaces type libraries and objects ; OleView.NET tool; useful for COM activation and interop investigation |
| [googleprojectzero/sandbox-attacksurface-analysis-tools](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools) | Inspect Windows tokens access checks and sandbox exposure ; PowerShell and .NET tools including NtObjectManager; use for isolation and permissions testing |
| [m417z/winapiexec](https://github.com/m417z/winapiexec) | Invoke Windows API functions from command-line arguments ; Small diagnostic and experimentation utility; GPL |
| [hfiref0x/WinObjEx64](https://github.com/hfiref0x/WinObjEx64) | Browse Object Manager namespaces and object properties ; x64 Windows tool; some inspection requires elevated access |
