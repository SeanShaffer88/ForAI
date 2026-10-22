# Windows / Native crash and heap diagnostics

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [ssbssa/heob](https://github.com/ssbssa/heob) | Detect heap buffer overruns and leaks in native Windows applications ; Tool; MSVC and MinGW builds; PDB uses DbgHelp and DWARF can use dwarfstack |
| [jrfonseca/drmingw](https://github.com/jrfonseca/drmingw) | Capture unhandled exceptions and symbolize MinGW or MSVC stacks ; Debugger and embeddable symbol/backtrace DLLs; supports DWARF and PDB |
| [ssbssa/dwarfstack](https://github.com/ssbssa/dwarfstack) | Resolve MinGW executable addresses to source files and lines ; Native Windows library focused on GCC DWARF information; stack completeness depends on compiler options |
| [VerySleepy/verysleepy](https://github.com/VerySleepy/verysleepy) | Sample CPU usage in Windows applications with symbol resolution ; GUI and command-line profiler; evaluate current compiler and Windows compatibility |
