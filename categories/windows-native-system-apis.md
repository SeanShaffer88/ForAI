# Windows / Native system APIs

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [winsiderss/phnt](https://github.com/winsiderss/phnt) | Native Windows API headers used by System Informer ; Headers; includes internal and reconstructed declarations; not a replacement for supported SDK contracts |
| [Chuyu-Team/MINT](https://github.com/Chuyu-Team/MINT) | User-mode internal API declarations for ntdll samlib and winsta ; Headers based on PHNT; internal API behavior can vary by Windows build |
| [KNSoft/KNSoft.NDK](https://github.com/KNSoft/KNSoft.NDK) | Windows NT declarations and supplemental DLL import libraries ; Headers and import libraries; includes undocumented APIs |
| [zodiacon/WinSys](https://github.com/zodiacon/WinSys) | Reusable C++ wrappers for low-level Windows development ; System library extracted from SystemExplorer; assess API surface and build requirements |
