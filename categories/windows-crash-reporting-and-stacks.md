# Windows / Crash reporting and stacks

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [JochenKalmbach/StackWalker](https://github.com/JochenKalmbach/StackWalker) | Walk and symbolize Windows thread call stacks ; C++ library; symbol quality depends on matching binaries and PDBs |
| [septag/stackwalkerc](https://github.com/septag/stackwalkerc) | Single-header C stack walking through DbgHelp.dll ; C or C++ embeddable source; supports module and symbol reporting |
| [jeremy-rifkin/cpptrace](https://github.com/jeremy-rifkin/cpptrace) | Portable stack traces and exception tracing for C++ ; C++11 library with Windows and MinGW support; check chosen symbol backend |
| [bombela/backward-cpp](https://github.com/bombela/backward-cpp) | Format C++ stack traces and available source context ; Header-oriented library; platform backends differ |
| [backtrace-labs/crashpad](https://github.com/backtrace-labs/crashpad) | Crash capture with CMake integration and attachment improvements ; Vendor fork of Crashpad; compare fork maintenance and upstream before adoption |
