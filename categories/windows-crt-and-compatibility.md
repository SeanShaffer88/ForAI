# Windows / CRT and compatibility

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Chuyu-Team/YY-Thunks](https://github.com/Chuyu-Team/YY-Thunks) | Compatibility thunks for APIs absent on older Windows versions ; Native compatibility library; validate each target OS and API fallback |
| [Chuyu-Team/VC-LTL5](https://github.com/Chuyu-Team/VC-LTL5) | CRT linking support aimed at reducing binary size and runtime dependencies ; Specialized CRT strategy using system msvcrt or ucrtbase; check compiler ABI and deployment constraints |
| [fancycode/MemoryModule](https://github.com/fancycode/MemoryModule) | Load supported DLL images from an in-process memory buffer ; Specialized loader library; normal LoadLibrary behavior and compatibility are not guaranteed |
