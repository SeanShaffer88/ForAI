# Windows / Heap and debugger extensions

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [RudjiGames/MTuner](https://github.com/RudjiGames/MTuner) | Capture allocation histories and analyze C++ memory usage and leaks ; Memory profiler; current location redirects from milostosic/MTuner |
| [goldshtn/windbg-extensions](https://github.com/goldshtn/windbg-extensions) | Trace paired resource acquisition and release in WinDbg ; Extension DLL source; historical breakpoint examples require architecture-specific adaptation |
| [chrisnas/DebuggingExtensions](https://github.com/chrisnas/DebuggingExtensions) | Analyze .NET dumps threads tasks and parallel call stacks ; Standalone tools and WinDbg extensions; check CLR and debugger compatibility |
| [KindDragon/vld](https://github.com/KindDragon/vld) | Visual Leak Detector for legacy Visual C++ applications ; INACTIVE per README; legacy reference only; not a default for current MSVC |
| [kubo/funchook](https://github.com/kubo/funchook) | Function-call interception library with Windows support ; ARCHIVED and unmaintained per README; legacy instrumentation reference only |
