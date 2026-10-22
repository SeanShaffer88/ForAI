# Windows development GitHub reference

Saved 2026-10-21 at Sean's request for use in future Windows software projects.

Current catalog: **232 unique repositories** (92 original, 54 first expansion, 52 specialized expansion, 31 revival and systems expansion, 3 development-start expansion). Updated 2026-10-21.

This catalog preserves the original list and adds specialized repositories discovered through four Exa search workstreams (48 search-result slots, including duplicates), with targeted repository-page retrieval. Additional entries were checked against repository descriptions or README content. This is a discovery reference, not a compatibility, license, security, or build audit. Search indexes can lag repository changes. Original entries were carried forward and were not all revalidated in this follow-up.

Use relevant entries as candidates when a project needs them. Recheck maintenance, supported Windows versions and CPU architectures, license, package provenance, and integration requirements before adopting. Inclusion does not authorize installing dependencies. Header-only libraries, DLL-capable libraries, source references, runtimes, and standalone tools are identified by purpose rather than treated as interchangeable downloads.

## Selection shortcuts

- DLL load troubleshooting: Dependencies; PE inspection: LIEF, pefile; native assembly: Zydis, Capstone.
- System performance: UIforETW, PerfView, PresentMon; instrumentation: Tracy, Optick, DynamoRIO, Dr. Memory.
- Explorer integration: MSF, ShellAnything; registry: WinReg; scheduled tasks: TaskScheduler.
- Hardware and virtual drives: HIDAPI, libusb, libserialport, WinFsp, Dokany.
- Native/.NET/Python interoperability: CsWin32, ClangSharp, Vanara, pywin32, pythonnet, DNNE.
- Embeddable interfaces and scripting: webview, saucer, ClearScript, QuickJS-NG, LuaJIT.
- Build and distribution: vcpkg, CMake, Ninja, vswhere, WiX, Inno Setup, Velopack, winget-create.

## Maintenance and canonical-location notes

- UIforETW: use randomascii/UIforETW; google/UIforETW is archived.
- ClearScript: current repository resolves to ClearFoundry/ClearScript.
- ClangSharp: current repository resolves to dotnet/ClangSharp.
- WTL and libserialport entries are GitHub mirrors; consult the stated upstream.
- dotnet/pinvoke and alphaleonis/AlphaFS are unmaintained legacy references. Prefer CsWin32 and current .NET APIs when suitable.
- Windows SDK, MSVC compiler/runtime redistributables, and WebView2 runtime distribution are separate from simply cloning GitHub source. This catalog is not a substitute for their supported installers.

## Development-start expansion (3)

Added 2026-10-21 after focused process/pipe searches and repository README retrieval. Archive flags and last-push dates were checked against the GitHub API. These are dormant candidates, not confirmed abandoned projects. The actionable backlog is windows-development-todo.md. WR-007 begins development on the already-cataloged goodtrailer/win-pipe; WR-008 through WR-010 cover these three additions.

| Repository | Purpose | Notes |
|---|---|---|
| [Krzmbrzl/NamedPipe](https://github.com/Krzmbrzl/NamedPipe) | Small Windows and POSIX named-pipe abstraction with CMake integration | Not archived; GitHub last push 2023-06-27; BSD-3-Clause; WR-008 compares portable semantics and forks before revival |
| [end2endzone/protobuf-pbop-plugin](https://github.com/end2endzone/protobuf-pbop-plugin) | Generate protobuf client and server interfaces over Windows named pipes | Not archived; GitHub last push 2020-07-25; MIT; WR-009 covers current protoc compatibility; historical README transport claims need re-evaluation |
| [martona/mhook](https://github.com/martona/mhook) | Windows function interception library with a small integration surface | Not archived; GitHub last push 2021-04-28; verify full license and decoder terms; WR-010 conditional on a demonstrated advantage over alternatives |

## Revival and systems expansion (31)

Added 2026-10-21. Four Exa search workstreams requested 40 results in total, including duplicate and rejected results. Selected upstream repository pages and READMEs were retrieved. GitHub API metadata independently confirmed archive flags for Microsoft IPC, SharpDX, microsoft-pdb, cpprestsdk and Bond, and confirmed Tx is not archived (last push 2022-10-05). These are discovery and feasibility notes, not build results. Dormancy does not establish abandonment. Descriptions below are paraphrased from linked repository sources; revival priority and scope are our engineering judgments.

### Revival candidates and useful starting points

| Project | When revival could pay off | First feasibility work | Alternative to compare |
|---|---|---|---|
| [Microsoft IPC](https://github.com/microsoft/IPC) | Existing C++/.NET applications need the same shared-memory protocol and low-copy behavior. | Restore current MSVC/.NET builds; run cross-process tests for crashes, shutdown, message ownership and permissions; audit Boost and optional Bond. | Named pipes or an existing supported messaging library; benchmark using the actual payloads. |
| [Tx](https://github.com/microsoft/Tx) | LINQ-style ETW queries provide reusable analysis that would otherwise be rewritten. | Port only needed readers/operators to the chosen .NET and Rx versions; replay known trace fixtures. | TraceEvent/PerfView APIs or KrabsETW plus a small query layer. |
| [SharpDX](https://github.com/sharpdx/SharpDX) | A working legacy application needs narrow fixes and migration would be disproportionately large. | Isolate required assemblies; verify COM lifetime, ABI, architecture and current Windows behavior. | Vortice.Windows and current generated bindings; avoid restoring unused API families. |
| [CrashRpt3](https://github.com/crashrpt3/crashrpt3) and [CrashRpt2](https://github.com/CrashRpt/crashrpt2) | An application needs their Windows exception-handler behavior or existing report format. | Compare patch lineage; build a crash-type test matrix including fail-fast, stack overflow, thread handling and dump integrity. | Crashpad integration or application-specific WER/minidump handling. |
| [Microsoft PDB](https://github.com/microsoft/microsoft-pdb) | A missing debug-record definition or parser behavior blocks a symbol tool. | Extract the minimum needed record definitions and tests; README explicitly says the full source does not currently build. | RawPDB, DIA SDK or LLVM PDB tooling. |
| [C++ REST SDK](https://github.com/microsoft/cpprestsdk) | Existing code depends heavily on its asynchronous API and migration cost is substantial. | Scope transport/TLS dependencies and regression tests; restore only the application-required functionality. | libcurl or Boost.Beast, as suggested by the archived upstream. |
| [Bond](https://github.com/microsoft/bond) | Existing stored data or deployed peers require Bond wire compatibility. | Test binary-format fixtures and schema evolution; audit parser/compiler dependencies and own necessary security fixes. | A maintained serialization format for new protocols, with a migration bridge for existing data. |

ChakraCore is listed separately as a community runtime continuation. Its engine breadth makes a full independent revival substantially more demanding than a small compatibility fork. Confirm current community maintenance and required security fixes before choosing it.

### Native crash and heap diagnostics

| Repository | Purpose | Notes |
|---|---|---|
| [ssbssa/heob](https://github.com/ssbssa/heob) | Detect heap buffer overruns and leaks in native Windows applications | Tool; MSVC and MinGW builds; PDB uses DbgHelp and DWARF can use dwarfstack |
| [jrfonseca/drmingw](https://github.com/jrfonseca/drmingw) | Capture unhandled exceptions and symbolize MinGW or MSVC stacks | Debugger and embeddable symbol/backtrace DLLs; supports DWARF and PDB |
| [ssbssa/dwarfstack](https://github.com/ssbssa/dwarfstack) | Resolve MinGW executable addresses to source files and lines | Native Windows library focused on GCC DWARF information; stack completeness depends on compiler options |
| [VerySleepy/verysleepy](https://github.com/VerySleepy/verysleepy) | Sample CPU usage in Windows applications with symbol resolution | GUI and command-line profiler; evaluate current compiler and Windows compatibility |

### Binary and build analysis

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/SizeBench](https://github.com/microsoft/SizeBench) | Analyze and compare code and data size in Windows PE binaries | Tool using binary and PDB pairs; useful for EXE DLL and SYS size regressions |
| [microsoft/binskim](https://github.com/microsoft/binskim) | Check compiler linker and security-relevant binary characteristics | Binary analyzer with SARIF output; rules and supported formats depend on version |
| [microsoft/vcperf](https://github.com/microsoft/vcperf) | Capture MSVC compiler and linker performance traces | C++ Build Insights tool; integrates with Windows Performance Analyzer |
| [microsoft/cpp-build-insights-samples](https://github.com/microsoft/cpp-build-insights-samples) | Examples of finding compilation and code-generation bottlenecks | SDK sample resource rather than a standalone runtime |
| [microsoft/clrmd](https://github.com/microsoft/clrmd) | Inspect .NET processes and memory dumps programmatically | Microsoft.Diagnostics.Runtime.dll; validate supported CLR and library major version |
| [rainers/cv2pdb](https://github.com/rainers/cv2pdb) | Convert supported CodeView or DWARF debug information to PDB | Specialized converter; validate compiler output and debug-record coverage |

### Shared memory and pipes

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/IPC](https://github.com/microsoft/IPC) | Windows shared-memory IPC with native C++ and .NET interoperability | ARCHIVED; WR-001 native foundation in progress at https://github.com/SeanShaffer88/ipc-revival ; Boost 1.92/CMake and worker tests, managed interop still pending; no stable release |
| [goodtrailer/win-pipe](https://github.com/goodtrailer/win-pipe) | Small single-file C++ wrapper for Windows named pipes | Upstream unfinished; scoped ISC revival 0.2.0 published at https://github.com/SeanShaffer88/win-pipe-revival with x86/x64 CI, resource-failure tests and PipeLog consumer; both peers must upgrade; see WR-007 |

### Trace query revival

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/Tx](https://github.com/microsoft/Tx) | Query event and trace streams using LINQ to Events | Not archived in GitHub API; last push 2022-10-05; dormant candidate rather than confirmed abandoned; review current .NET and Rx compatibility |

### Graphics binding options

| Repository | Purpose | Notes |
|---|---|---|
| [sharpdx/SharpDX](https://github.com/sharpdx/SharpDX) | Legacy .NET bindings for DirectX graphics and multimedia APIs | ARCHIVED; README says development ended in 2019; targeted compatibility revival may suit existing applications |
| [amerkoleci/Vortice.Windows](https://github.com/amerkoleci/Vortice.Windows) | Modern .NET bindings for Direct3D Direct2D audio input and related Windows APIs | Compare supported target frameworks and API coverage before reviving SharpDX |

### Embedded runtime revival

| Repository | Purpose | Notes |
|---|---|---|
| [chakra-core/ChakraCore](https://github.com/chakra-core/ChakraCore) | Embed a JavaScript engine through a native C API | Community continuation after Microsoft support ended; not automatically abandoned; expensive revival candidate requiring current security and build assessment |

### Networking and virtual devices

| Repository | Purpose | Notes |
|---|---|---|
| [basil00/WinDivert](https://github.com/basil00/WinDivert) | Capture filter modify and reinject packets from user-mode code | WinDivert.dll plus kernel driver; assess redistribution driver signing and platform support |
| [WireGuard/wintun](https://github.com/WireGuard/wintun) | Expose a layer-3 virtual network adapter through wintun.dll | GitHub mirror; official upstream git.zx2c4.com/wintun; obtain architecture-matched supported binaries |
| [winfsp/winspd](https://github.com/winfsp/winspd) | Implement user-mode storage devices that appear as SCSI disks | Storage proxy framework distinct from file-level WinFsp; assess driver deployment and license |

### Projected files and shell

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/ProjFS-Managed-API](https://github.com/microsoft/ProjFS-Managed-API) | Implement Windows projected-file providers in C# | Wrapper for ProjFS; Windows optional feature must be enabled; projects can project data on demand |
| [dwmkerr/sharpshell](https://github.com/dwmkerr/sharpshell) | Implement Explorer context menus previews thumbnails and other shell extensions in .NET Framework | Canonical SharpShell project; assess CLR hosting architecture registration and supported extension types |

### Crash reporting revival

| Repository | Purpose | Notes |
|---|---|---|
| [CrashRpt/crashrpt2](https://github.com/CrashRpt/crashrpt2) | Collection of fixes and extensions to the older CrashRpt crash-reporting library | Historical patch source; evaluate maintained descendants before undertaking an independent fork |
| [crashrpt3/crashrpt3](https://github.com/crashrpt3/crashrpt3) | Community continuation of native Windows CrashRpt with additional crash handlers | README presents it as collecting newer patches; candidate revival base; independently test crash coverage instead of relying on comparison claims |

### Archived PDB reference

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/microsoft-pdb](https://github.com/microsoft/microsoft-pdb) | Microsoft PDB format source definitions and historical tools | ARCHIVED verified; README says source will not currently build; prioritize extracting tested format knowledge over reviving the entire toolchain |

### Offline Windows formats

| Repository | Purpose | Notes |
|---|---|---|
| [libyal/libregf](https://github.com/libyal/libregf) | Read offline Windows Registry hive files in REGF format | Native library and tools; project reports alpha status; check license thread safety and Windows build instructions |
| [libyal/libevtx](https://github.com/libyal/libevtx) | Read Windows EVTX event-log files without relying on a live log service | Native library and tools; README reports alpha status and planned multithreading |
| [libyal/libesedb](https://github.com/libyal/libesedb) | Read Extensible Storage Engine EDB database files | Native library and tools; useful for offline analysis; verify supported ESE versions and Windows build requirements |

### Small native utility additions

| Repository | Purpose | Notes |
|---|---|---|
| [vimpunk/mio](https://github.com/vimpunk/mio) | Memory-map files through a C++11 header-only API | Canonical location redirected from mandreyel/mio; supports existing handles and non-page-aligned logical offsets |
| [marzer/tomlplusplus](https://github.com/marzer/tomlplusplus) | Parse and serialize TOML configuration in C++17 | Header-oriented library with MSVC support; suitable for native tool configuration |

### Archived service libraries

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/cpprestsdk](https://github.com/microsoft/cpprestsdk) | Asynchronous C++ HTTP JSON URI WebSocket and task APIs | ARCHIVED verified; revival can preserve an existing API surface; upstream suggests libcurl or Boost.Beast as alternatives |
| [microsoft/bond](https://github.com/microsoft/bond) | Schema-based serialization and C++/.NET data interchange | ARCHIVED; project ended March 2025 with no further fixes; revival mainly justified by existing wire-format compatibility |

## Specialized expansion (52)

Added 2026-10-21. Research used four targeted Exa searches (40 result slots including duplicates), one five-result Windows-runtime verification search, and targeted repository/README retrieval. Entries below were deduplicated against the prior 146. Repository descriptions and documentation were checked; these projects have not been built or integration-tested for this catalog.

### Maintenance and revival preference

Maintenance status is a tradeoff, not an automatic exclusion. Sean explicitly welcomes reviving or maintaining a fork when it materially benefits a project. Compare functional advantage, alternatives, license and fork rights, repair effort, Windows/compiler compatibility, test coverage, security fixes, dependency health, and ongoing ownership. Prefer a scoped feasibility check, identify a suitable base or existing maintained fork, and validate the required behavior before relying on a revived project. This preference authorizes consideration; choose implementation scope according to the actual project request.

### Useful selection shortcuts

- Native NT definitions and DLL imports: PHNT, MINT, KNSoft.NDK; CRT compatibility: YY-Thunks and VC-LTL5.
- Stack traces and crash capture: StackWalker, stackwalkerc, cpptrace, backward-cpp, Crashpad fork.
- PDB and PE analysis: RawPDB, pdbex, PDB Insight, pdbparse, pe-parse.
- Heap and objects: MTuner, WinObjEx64; COM activation: OleView.NET.
- Embedded runtimes: WAMR, Wasm3, Duktape, Wren, Squirrel, ChaiScript; JIT assemblers: AsmJit and Xbyak.

### Native system APIs

| Repository | Purpose | Notes |
|---|---|---|
| [winsiderss/phnt](https://github.com/winsiderss/phnt) | Native Windows API headers used by System Informer | Headers; includes internal and reconstructed declarations; not a replacement for supported SDK contracts |
| [Chuyu-Team/MINT](https://github.com/Chuyu-Team/MINT) | User-mode internal API declarations for ntdll samlib and winsta | Headers based on PHNT; internal API behavior can vary by Windows build |
| [KNSoft/KNSoft.NDK](https://github.com/KNSoft/KNSoft.NDK) | Windows NT declarations and supplemental DLL import libraries | Headers and import libraries; includes undocumented APIs |
| [zodiacon/WinSys](https://github.com/zodiacon/WinSys) | Reusable C++ wrappers for low-level Windows development | System library extracted from SystemExplorer; assess API surface and build requirements |

### CRT and compatibility

| Repository | Purpose | Notes |
|---|---|---|
| [Chuyu-Team/YY-Thunks](https://github.com/Chuyu-Team/YY-Thunks) | Compatibility thunks for APIs absent on older Windows versions | Native compatibility library; validate each target OS and API fallback |
| [Chuyu-Team/VC-LTL5](https://github.com/Chuyu-Team/VC-LTL5) | CRT linking support aimed at reducing binary size and runtime dependencies | Specialized CRT strategy using system msvcrt or ucrtbase; check compiler ABI and deployment constraints |
| [fancycode/MemoryModule](https://github.com/fancycode/MemoryModule) | Load supported DLL images from an in-process memory buffer | Specialized loader library; normal LoadLibrary behavior and compatibility are not guaranteed |

### Crash reporting and stacks

| Repository | Purpose | Notes |
|---|---|---|
| [JochenKalmbach/StackWalker](https://github.com/JochenKalmbach/StackWalker) | Walk and symbolize Windows thread call stacks | C++ library; symbol quality depends on matching binaries and PDBs |
| [septag/stackwalkerc](https://github.com/septag/stackwalkerc) | Single-header C stack walking through DbgHelp.dll | C or C++ embeddable source; supports module and symbol reporting |
| [jeremy-rifkin/cpptrace](https://github.com/jeremy-rifkin/cpptrace) | Portable stack traces and exception tracing for C++ | C++11 library with Windows and MinGW support; check chosen symbol backend |
| [bombela/backward-cpp](https://github.com/bombela/backward-cpp) | Format C++ stack traces and available source context | Header-oriented library; platform backends differ |
| [backtrace-labs/crashpad](https://github.com/backtrace-labs/crashpad) | Crash capture with CMake integration and attachment improvements | Vendor fork of Crashpad; compare fork maintenance and upstream before adoption |

### PDB and PE tooling

| Repository | Purpose | Notes |
|---|---|---|
| [MolecularMatters/raw_pdb](https://github.com/MolecularMatters/raw_pdb) | Read Microsoft PDB streams directly from C++ | Low-level C++11 library; callers construct higher-level symbol abstractions |
| [wbenny/pdbex](https://github.com/wbenny/pdbex) | Reconstruct C structure and union declarations from PDB symbols | Tool; symbol information can omit details needed for exact source reconstruction |
| [moyix/pdbparse](https://github.com/moyix/pdbparse) | Parse Microsoft PDB debug information using Python | Library; GPL; verify compatibility with required PDB streams and Python version |
| [StackAndPointer/PDB-Insight](https://github.com/StackAndPointer/PDB-Insight) | Browse PDB types and functions and export symbol information | Win32 and DIA SDK tool; supports symbol-server downloads |
| [trailofbits/pe-parse](https://github.com/trailofbits/pe-parse) | Parse Windows PE imports exports sections and relocations | C++ library intended for robust executable analysis |
| [zodiacon/PEExplorer](https://github.com/zodiacon/PEExplorer) | Inspect Portable Executable structure in a GUI | Desktop tool and parser reference; inspect repository branch and project requirements |

### Windows inspection and COM

| Repository | Purpose | Notes |
|---|---|---|
| [hakril/PythonForWindows](https://github.com/hakril/PythonForWindows) | Python abstractions over Windows native APIs ALPC RPC and execution | ctypes-based Python library for x86 and x64 |
| [tyranid/oleviewdotnet](https://github.com/tyranid/oleviewdotnet) | Inspect COM registrations interfaces type libraries and objects | OleView.NET tool; useful for COM activation and interop investigation |
| [googleprojectzero/sandbox-attacksurface-analysis-tools](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools) | Inspect Windows tokens access checks and sandbox exposure | PowerShell and .NET tools including NtObjectManager; use for isolation and permissions testing |
| [m417z/winapiexec](https://github.com/m417z/winapiexec) | Invoke Windows API functions from command-line arguments | Small diagnostic and experimentation utility; GPL |
| [hfiref0x/WinObjEx64](https://github.com/hfiref0x/WinObjEx64) | Browse Object Manager namespaces and object properties | x64 Windows tool; some inspection requires elevated access |

### Heap and debugger extensions

| Repository | Purpose | Notes |
|---|---|---|
| [RudjiGames/MTuner](https://github.com/RudjiGames/MTuner) | Capture allocation histories and analyze C++ memory usage and leaks | Memory profiler; current location redirects from milostosic/MTuner |
| [goldshtn/windbg-extensions](https://github.com/goldshtn/windbg-extensions) | Trace paired resource acquisition and release in WinDbg | Extension DLL source; historical breakpoint examples require architecture-specific adaptation |
| [chrisnas/DebuggingExtensions](https://github.com/chrisnas/DebuggingExtensions) | Analyze .NET dumps threads tasks and parallel call stacks | Standalone tools and WinDbg extensions; check CLR and debugger compatibility |
| [KindDragon/vld](https://github.com/KindDragon/vld) | Visual Leak Detector for legacy Visual C++ applications | INACTIVE per README; legacy reference only; not a default for current MSVC |
| [kubo/funchook](https://github.com/kubo/funchook) | Function-call interception library with Windows support | ARCHIVED and unmaintained per README; legacy instrumentation reference only |

### Embeddable runtimes

| Repository | Purpose | Notes |
|---|---|---|
| [wasm-micro-runtime/wasm-micro-runtime](https://github.com/wasm-micro-runtime/wasm-micro-runtime) | Embed WebAssembly interpreter and AOT execution in native programs | WAMR current location; Windows MSVC and MinGW documentation exists; modes and WASI support differ by configuration |
| [wasm3/wasm3](https://github.com/wasm3/wasm3) | Compact WebAssembly interpreter for native applications | Minimal-maintenance phase per README; check required Wasm and WASI features |
| [svaarala/duktape](https://github.com/svaarala/duktape) | Compact JavaScript interpreter embeddable in C and C++ | Master tracks incompatible 3.x changes; README points 2.x users to v2-maintenance |
| [wren-lang/wren](https://github.com/wren-lang/wren) | Small class-based scripting VM for embedding | C runtime; check host integration and Windows build tooling |
| [albertodemichelis/squirrel](https://github.com/albertodemichelis/squirrel) | Embeddable scripting language with native integration | Official Squirrel repository; README documents Windows x86 and amd64 |
| [ChaiScript/ChaiScript](https://github.com/ChaiScript/ChaiScript) | Header-based scripting integration designed for C++ | C++ embedded language; evaluate compile time and supported toolchains |

### JIT code generation

| Repository | Purpose | Notes |
|---|---|---|
| [asmjit/asmjit](https://github.com/asmjit/asmjit) | Generate native machine code at runtime | C++ JIT assembler library; select backend matching target architecture |
| [herumi/xbyak](https://github.com/herumi/xbyak) | Generate x86 and x64 instructions with C++ assembly syntax | Header-only JIT assembler; x86 and x64 architecture focus |

### Processes and console

| Repository | Purpose | Notes |
|---|---|---|
| [rprichard/winpty](https://github.com/rprichard/winpty) | Bridge Windows console programs to Unix-style pseudo terminals | Native library plus agent executable; legacy console approach; compare ConPTY on current Windows |
| [daandemeyer/reproc](https://github.com/daandemeyer/reproc) | Start stop and communicate with child processes from C and C++ | C99 library plus C++11 wrapper; cross-platform process and redirected I/O support |

### Native platform integration

| Repository | Purpose | Notes |
|---|---|---|
| [mohabouje/WinToast](https://github.com/mohabouje/WinToast) | Display Windows toast notifications from C++ | Native library; app identity and notification setup affect integration |
| [vslavik/winsparkle](https://github.com/vslavik/winsparkle) | Provide automatic update UI and appcast processing | Native C API and WinSparkle.dll; check signed-update configuration |
| [btzy/nativefiledialog-extended](https://github.com/btzy/nativefiledialog-extended) | Open native file folder and save dialogs through C or C++ | Small static library using Windows native dialogs; MSVC MinGW and Clang supported |

### Native networking and data

| Repository | Purpose | Notes |
|---|---|---|
| [libevent/libevent](https://github.com/libevent/libevent) | Asynchronous event notification and buffered network I/O | C library with Windows CMake build instructions |
| [nanomsg/nng](https://github.com/nanomsg/nng) | Brokerless messaging with request reply and other communication patterns | Native C library; NNG 2 introduces API changes from NNG 1 |
| [an-tao/trantor](https://github.com/an-tao/trantor) | Event-driven nonblocking TCP networking and thread pools | C++ library with Windows MSVC build support |
| [libssh2/libssh2](https://github.com/libssh2/libssh2) | Embed SSH2 client functionality | Native C library; select and configure Windows crypto backend |
| [zeux/pugixml](https://github.com/zeux/pugixml) | Parse modify and query XML using XPath | Native C++ library; Unicode conversion support |
| [weidai11/cryptopp](https://github.com/weidai11/cryptopp) | Native cryptographic algorithms and supporting utilities | C++ library; inspect integration and algorithm choices for project needs |
| [abdes/cryptopp-cmake](https://github.com/abdes/cryptopp-cmake) | Integrate Crypto++ using modern CMake targets | Build integration repository rather than the Crypto++ implementation |

### Native audio and images

| Repository | Purpose | Notes |
|---|---|---|
| [mackron/miniaudio](https://github.com/mackron/miniaudio) | Capture play mix and process audio from C | Single-source audio library with Windows backends |
| [PortAudio/portaudio](https://github.com/PortAudio/portaudio) | Portable real-time audio input and output | Native C library; choose appropriate Windows host API and build options |
| [libjpeg-turbo/libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo) | Encode and decode JPEG with SIMD acceleration | Native codec library including TurboJPEG API; DLL deployment available |

### Static analysis additions

| Repository | Purpose | Notes |
|---|---|---|
| [cppcheck-opensource/cppcheck](https://github.com/cppcheck-opensource/cppcheck) | Analyze C and C++ code for defects | Current repository location redirects from danmar/cppcheck; Windows tooling available |

## Additional repositories (54)

### Native integration

| Repository | Purpose | Notes |
|---|---|---|
| [rodrigocfd/winlamb](https://github.com/rodrigocfd/winlamb) | Thin Win32 C++ wrapper with lambda message handlers | Library |
| [GiovanniDicanio/WinReg](https://github.com/GiovanniDicanio/WinReg) | Higher-level C++ Windows Registry access | Library |
| [vbaderks/msf](https://github.com/vbaderks/msf) | ATL-based C++ framework for Explorer shell extensions | Library; LGPL terms |
| [end2endzone/ShellAnything](https://github.com/end2endzone/ShellAnything) | Configurable dynamic Explorer context menus | Tool and integration reference |
| [Win32-WTL/WTL](https://github.com/Win32-WTL/WTL) | Windows Template Library for ATL-based desktop interfaces | GitHub mirror; upstream is SourceForge |
| [dahall/TaskScheduler](https://github.com/dahall/TaskScheduler) | .NET wrapper and editor controls for Windows Task Scheduler | Library |
| [mhammond/pywin32](https://github.com/mhammond/pywin32) | Python access to Win32 COM services and Windows APIs | Python extension modules |
| [pythonnet/pythonnet](https://github.com/pythonnet/pythonnet) | Interoperability between Python and .NET | Runtime bridge |
| [dotnet/ClangSharp](https://github.com/dotnet/ClangSharp) | Clang .NET bindings and native P/Invoke generation | Native binding tooling; redirected from microsoft/ClangSharp |
| [AaronRobinsonMSFT/DNNE](https://github.com/AaronRobinsonMSFT/DNNE) | Expose native entry points from .NET assemblies | Prototype; assess against current NativeAOT needs |

### Diagnostics additions

| Repository | Purpose | Notes |
|---|---|---|
| [randomascii/UIforETW](https://github.com/randomascii/UIforETW) | Record and manage ETW performance traces | Current project location; google/UIforETW is archived |
| [GameTechDev/PresentMon](https://github.com/GameTechDev/PresentMon) | Capture frame timings and graphics presentation metrics | Tool and analysis library |
| [zodiacon/AllTools](https://github.com/zodiacon/AllTools) | Collection of Windows internals diagnostic utilities | Tool collection; individual tools vary |
| [zodiacon/ProcMonXv2](https://github.com/zodiacon/ProcMonXv2) | ETW-based process and system event inspection | Diagnostic tool |
| [DynamoRIO/dynamorio](https://github.com/DynamoRIO/dynamorio) | Build dynamic binary instrumentation and analysis tools | Instrumentation runtime |
| [DynamoRIO/drmemory](https://github.com/DynamoRIO/drmemory) | Detect memory errors leaks and Windows handle misuse | Binary instrumentation tool |
| [wolfpld/tracy](https://github.com/wolfpld/tracy) | Instrument CPU GPU allocations locks and frame performance | Profiler |
| [bombomby/optick](https://github.com/bombomby/optick) | C++ profiling with instrumentation and sampling | Profiler |
| [DavidXanatos/TaskExplorer](https://github.com/DavidXanatos/TaskExplorer) | Detailed live inspection of process and thread activity | Diagnostic tool |

### Devices and filesystems

| Repository | Purpose | Notes |
|---|---|---|
| [winfsp/winfsp](https://github.com/winfsp/winfsp) | Implement Windows filesystems in user mode | Native filesystem framework; driver deployment applies |
| [dokan-dev/dokany](https://github.com/dokan-dev/dokany) | User-mode Windows filesystem library and FUSE wrapper | Native filesystem framework; driver deployment applies |
| [libusb/hidapi](https://github.com/libusb/hidapi) | Communicate with USB and Bluetooth HID-class devices | Native library; DLL or embedded source |
| [libusb/libusb](https://github.com/libusb/libusb) | User-space USB device access | Native library; Windows backend and device driver matter |
| [pbatard/libwdi](https://github.com/pbatard/libwdi) | Generate and install Windows USB driver packages | Native installer library; GPL terms |
| [sigrokproject/libserialport](https://github.com/sigrokproject/libserialport) | Enumerate and communicate with serial ports | C library; GitHub mirror |

### Drivers

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/DMF](https://github.com/microsoft/DMF) | Reusable modules extending Windows Driver Frameworks | Driver Module Framework |
| [microsoft/Windows-Driver-Frameworks](https://github.com/microsoft/Windows-Driver-Frameworks) | KMDF and UMDF source for understanding and debugging WDF | Framework source reference |
| [microsoft/windows-drivers-rs](https://github.com/microsoft/windows-drivers-rs) | Rust crates and build tooling for Windows drivers | Check current supported WDK and driver models |

### Embedded runtimes and UI

| Repository | Purpose | Notes |
|---|---|---|
| [webview/webview](https://github.com/webview/webview) | Small C/C++ webview abstraction using WebView2 on Windows | Requires appropriate WebView2 deployment |
| [saucer/saucer](https://github.com/saucer/saucer) | Modern C++ desktop webview with JavaScript interoperability | Webview UI library |
| [ClearFoundry/ClearScript](https://github.com/ClearFoundry/ClearScript) | Embed V8 and other scripting engines in .NET apps | Current location; redirected from microsoft/ClearScript |
| [quickjs-ng/quickjs](https://github.com/quickjs-ng/quickjs) | Small embeddable JavaScript engine | Runtime; check Windows build configuration |
| [LuaJIT/LuaJIT](https://github.com/LuaJIT/LuaJIT) | Embeddable Lua JIT compiler and FFI | GitHub mirror |

### .NET application helpers

| Repository | Purpose | Notes |
|---|---|---|
| [reactiveui/ReactiveUI](https://github.com/reactiveui/ReactiveUI) | Reactive MVVM and application state composition | Cross-platform .NET library |
| [CommunityToolkit/dotnet](https://github.com/CommunityToolkit/dotnet) | MVVM generators diagnostics and performance helpers | Cross-platform .NET toolkit |
| [Cysharp/MemoryPack](https://github.com/Cysharp/MemoryPack) | Source-generated binary serialization | Check schema evolution and runtime requirements |

### Native utility additions

| Repository | Purpose | Notes |
|---|---|---|
| [leethomason/tinyxml2](https://github.com/leethomason/tinyxml2) | Small embeddable C++ XML parser | Native library |
| [nemtrif/utfcpp](https://github.com/nemtrif/utfcpp) | Portable UTF-8 validation iteration and conversion | C++ library |
| [randy408/libspng](https://github.com/randy408/libspng) | PNG decoding and encoding library | Native library |

### Graphics additions

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/Win2D](https://github.com/microsoft/Win2D) | GPU-accelerated 2D drawing with Direct2D and XAML integration | Check control support for chosen WinUI version |
| [microsoft/DirectXMesh](https://github.com/microsoft/DirectXMesh) | Geometry processing normals adjacency and meshlets | Native library |
| [microsoft/UVAtlas](https://github.com/microsoft/UVAtlas) | Create and pack mesh texture atlases | Native library |

### Binary tooling additions

| Repository | Purpose | Notes |
|---|---|---|
| [capstone-engine/capstone](https://github.com/capstone-engine/capstone) | Multi-architecture instruction disassembly | Native library |
| [zyantific/zydis](https://github.com/zyantific/zydis) | Fast x86 and x64 disassembly and instruction encoding | Native library |
| [rizinorg/cutter](https://github.com/rizinorg/cutter) | Graphical binary analysis and reverse engineering | Desktop tool |
| [EasyHook/EasyHook](https://github.com/EasyHook/EasyHook) | Bridge managed and unmanaged API interception | Check supported .NET and OS versions |
| [stevemk14ebr/PolyHook_2_0](https://github.com/stevemk14ebr/PolyHook_2_0) | C++ x86 and x64 function interception | Native instrumentation library |

### Build and deployment additions

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/vswhere](https://github.com/microsoft/vswhere) | Discover installed Visual Studio and Build Tools instances | Redistributable discovery CLI |
| [microsoft/winget-create](https://github.com/microsoft/winget-create) | Generate and update WinGet application manifests | Packaging CLI |

### Reference additions

| Repository | Purpose | Notes |
|---|---|---|
| [lowleveldesign/debug-recipes](https://github.com/lowleveldesign/debug-recipes) | Practical WinDbg ETW COM and .NET troubleshooting guides | Resource |
| [nasbench/EVTX-ETW-Resources](https://github.com/nasbench/EVTX-ETW-Resources) | ETW provider manifests event catalogs and examples | Resource |
| [microsoft/ETW](https://github.com/microsoft/ETW) | ETW tools libraries and samples | Resource |

### Legacy references

| Repository | Purpose | Notes |
|---|---|---|
| [dotnet/pinvoke](https://github.com/dotnet/pinvoke) | Historical hand-maintained Windows P/Invoke declarations | Unmaintained; project recommends CsWin32 |
| [alphaleonis/AlphaFS](https://github.com/alphaleonis/AlphaFS) | Additional Windows filesystem operations for older .NET apps | Unmaintained; reference and legacy maintenance only |

## Original repositories (92)

### Windows APIs

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/WindowsAppSDK](https://github.com/microsoft/WindowsAppSDK) | Modern Windows desktop APIs and lifecycle | Carried forward from original list; recheck before adoption |
| [microsoft/wil](https://github.com/microsoft/wil) | C++ resource management and Win32 helpers | Carried forward from original list; recheck before adoption |
| [microsoft/cppwinrt](https://github.com/microsoft/cppwinrt) | C++ Windows Runtime bindings | Carried forward from original list; recheck before adoption |
| [microsoft/windows-rs](https://github.com/microsoft/windows-rs) | Rust bindings for Windows APIs | Carried forward from original list; recheck before adoption |
| [microsoft/CsWin32](https://github.com/microsoft/CsWin32) | C# Win32 P/Invoke source generator | Carried forward from original list; recheck before adoption |
| [microsoft/win32metadata](https://github.com/microsoft/win32metadata) | Win32 API metadata and generation tooling | Carried forward from original list; recheck before adoption |
| [dahall/Vanara](https://github.com/dahall/Vanara) | .NET wrappers for Windows APIs | Carried forward from original list; recheck before adoption |
| [microsoft/STL](https://github.com/microsoft/STL) | MSVC C++ Standard Library source | Carried forward from original list; recheck before adoption |

### Build tools

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/vcpkg](https://github.com/microsoft/vcpkg) | Native C++ dependency manager | Carried forward from original list; recheck before adoption |
| [conan-io/conan](https://github.com/conan-io/conan) | C++ package and binary dependency manager | Carried forward from original list; recheck before adoption |
| [Kitware/CMake](https://github.com/Kitware/CMake) | Cross-platform build configuration | Carried forward from original list; recheck before adoption |
| [ninja-build/ninja](https://github.com/ninja-build/ninja) | Fast build executor | Carried forward from original list; recheck before adoption |
| [llvm/llvm-project](https://github.com/llvm/llvm-project) | Clang clang-cl LLD and analysis tools | Carried forward from original list; recheck before adoption |
| [dotnet/msbuild](https://github.com/dotnet/msbuild) | Visual Studio and .NET build engine | Carried forward from original list; recheck before adoption |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | C# and Visual Basic compiler APIs | Carried forward from original list; recheck before adoption |
| [mesonbuild/meson](https://github.com/mesonbuild/meson) | Cross-platform build configuration | Carried forward from original list; recheck before adoption |
| [msys2/MSYS2-packages](https://github.com/msys2/MSYS2-packages) | MSYS2 package recipes | Carried forward from original list; recheck before adoption |
| [msys2/MINGW-packages](https://github.com/msys2/MINGW-packages) | Native Windows toolchain and library recipes | Carried forward from original list; recheck before adoption |

### Runtimes

| Repository | Purpose | Notes |
|---|---|---|
| [dotnet/runtime](https://github.com/dotnet/runtime) | .NET runtime and core libraries | Carried forward from original list; recheck before adoption |
| [dotnet/sdk](https://github.com/dotnet/sdk) | .NET SDK and CLI build tools | Carried forward from original list; recheck before adoption |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | Automation shell and runtime | Carried forward from original list; recheck before adoption |
| [python/cpython](https://github.com/python/cpython) | Python interpreter and embedding APIs | Carried forward from original list; recheck before adoption |
| [nodejs/node](https://github.com/nodejs/node) | JavaScript runtime | Carried forward from original list; recheck before adoption |
| [rust-lang/rust](https://github.com/rust-lang/rust) | Rust compiler and standard library | Carried forward from original list; recheck before adoption |
| [libuv/libuv](https://github.com/libuv/libuv) | Native asynchronous I/O and event loops | Carried forward from original list; recheck before adoption |

### Desktop UI

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/microsoft-ui-xaml](https://github.com/microsoft/microsoft-ui-xaml) | WinUI controls and framework | Carried forward from original list; recheck before adoption |
| [dotnet/wpf](https://github.com/dotnet/wpf) | WPF desktop UI framework | Carried forward from original list; recheck before adoption |
| [dotnet/winforms](https://github.com/dotnet/winforms) | Windows Forms desktop UI framework | Carried forward from original list; recheck before adoption |
| [AvaloniaUI/Avalonia](https://github.com/AvaloniaUI/Avalonia) | Cross-platform .NET desktop UI | Carried forward from original list; recheck before adoption |
| [wxWidgets/wxWidgets](https://github.com/wxWidgets/wxWidgets) | C++ GUI with native controls | Carried forward from original list; recheck before adoption |
| [ocornut/imgui](https://github.com/ocornut/imgui) | Immediate-mode developer interfaces | Carried forward from original list; recheck before adoption |
| [electron/electron](https://github.com/electron/electron) | Chromium and Node desktop framework | Carried forward from original list; recheck before adoption |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | Rust and web desktop framework | Carried forward from original list; recheck before adoption |
| [CommunityToolkit/Windows](https://github.com/CommunityToolkit/Windows) | Windows controls and helpers | Carried forward from original list; recheck before adoption |
| [lepoco/wpfui](https://github.com/lepoco/wpfui) | Fluent-style WPF controls | Carried forward from original list; recheck before adoption |

### Native libraries

| Repository | Purpose | Notes |
|---|---|---|
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | C++ formatting | Carried forward from original list; recheck before adoption |
| [gabime/spdlog](https://github.com/gabime/spdlog) | C++ logging | Carried forward from original list; recheck before adoption |
| [nlohmann/json](https://github.com/nlohmann/json) | C++ JSON | Carried forward from original list; recheck before adoption |
| [boostorg/boost](https://github.com/boostorg/boost) | C++ utility libraries | Carried forward from original list; recheck before adoption |
| [chriskohlhoff/asio](https://github.com/chriskohlhoff/asio) | Asynchronous networking and I/O | Carried forward from original list; recheck before adoption |
| [curl/curl](https://github.com/curl/curl) | libcurl networking protocols and CLI | Carried forward from original list; recheck before adoption |
| [openssl/openssl](https://github.com/openssl/openssl) | TLS and cryptography | Carried forward from original list; recheck before adoption |
| [libarchive/libarchive](https://github.com/libarchive/libarchive) | Archive reading and writing | Carried forward from original list; recheck before adoption |
| [madler/zlib](https://github.com/madler/zlib) | Compression | Carried forward from original list; recheck before adoption |
| [facebook/zstd](https://github.com/facebook/zstd) | Zstandard compression | Carried forward from original list; recheck before adoption |
| [libgit2/libgit2](https://github.com/libgit2/libgit2) | Embeddable Git | Carried forward from original list; recheck before adoption |
| [libffi/libffi](https://github.com/libffi/libffi) | Foreign function interface | Carried forward from original list; recheck before adoption |
| [microsoft/mimalloc](https://github.com/microsoft/mimalloc) | Memory allocator | Carried forward from original list; recheck before adoption |

### Diagnostics

| Repository | Purpose | Notes |
|---|---|---|
| [lucasg/Dependencies](https://github.com/lucasg/Dependencies) | EXE and DLL dependency inspection | Carried forward from original list; recheck before adoption |
| [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | Native x86 and x64 debugger | Carried forward from original list; recheck before adoption |
| [winsiderss/systeminformer](https://github.com/winsiderss/systeminformer) | Processes handles modules and services | Carried forward from original list; recheck before adoption |
| [microsoft/perfview](https://github.com/microsoft/perfview) | CPU memory and ETW analysis | Carried forward from original list; recheck before adoption |
| [dotnet/diagnostics](https://github.com/dotnet/diagnostics) | .NET dumps traces and counters | Carried forward from original list; recheck before adoption |
| [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy) | .NET assembly browser and decompiler | Carried forward from original list; recheck before adoption |
| [microsoft/WinDbg-Samples](https://github.com/microsoft/WinDbg-Samples) | WinDbg scripts extensions and API examples | Carried forward from original list; recheck before adoption |
| [microsoft/krabsetw](https://github.com/microsoft/krabsetw) | C++ and .NET ETW consumption wrappers | Carried forward from original list; recheck before adoption |
| [lief-project/LIEF](https://github.com/lief-project/LIEF) | Executable parsing and modification including PE | Carried forward from original list; recheck before adoption |
| [erocarrera/pefile](https://github.com/erocarrera/pefile) | Python PE inspection | Carried forward from original list; recheck before adoption |
| [microsoft/Detours](https://github.com/microsoft/Detours) | Windows API instrumentation | Carried forward from original list; recheck before adoption |
| [TsudaKageyu/minhook](https://github.com/TsudaKageyu/minhook) | Lightweight Windows API hooking | Carried forward from original list; recheck before adoption |

### Graphics

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/DirectX-Headers](https://github.com/microsoft/DirectX-Headers) | DirectX headers | Carried forward from original list; recheck before adoption |
| [microsoft/DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler) | HLSL shader compiler | Carried forward from original list; recheck before adoption |
| [microsoft/DirectXTK](https://github.com/microsoft/DirectXTK) | Direct3D 11 helpers | Carried forward from original list; recheck before adoption |
| [microsoft/DirectXTK12](https://github.com/microsoft/DirectXTK12) | Direct3D 12 helpers | Carried forward from original list; recheck before adoption |
| [microsoft/DirectXTex](https://github.com/microsoft/DirectXTex) | Texture processing | Carried forward from original list; recheck before adoption |
| [microsoft/DirectXMath](https://github.com/microsoft/DirectXMath) | SIMD graphics math | Carried forward from original list; recheck before adoption |
| [libsdl-org/SDL](https://github.com/libsdl-org/SDL) | Window input audio and graphics integration | Carried forward from original list; recheck before adoption |
| [glfw/glfw](https://github.com/glfw/glfw) | Graphics windows contexts and input | Carried forward from original list; recheck before adoption |
| [baldurk/renderdoc](https://github.com/baldurk/renderdoc) | Graphics frame capture debugger | Carried forward from original list; recheck before adoption |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | Machine learning inference runtime | Carried forward from original list; recheck before adoption |

### Testing

| Repository | Purpose | Notes |
|---|---|---|
| [google/googletest](https://github.com/google/googletest) | C++ testing and mocking | Carried forward from original list; recheck before adoption |
| [catchorg/Catch2](https://github.com/catchorg/Catch2) | C++ test framework | Carried forward from original list; recheck before adoption |
| [google/benchmark](https://github.com/google/benchmark) | C++ microbenchmarking | Carried forward from original list; recheck before adoption |
| [FlaUI/FlaUI](https://github.com/FlaUI/FlaUI) | .NET Windows UI automation | Carried forward from original list; recheck before adoption |
| [pywinauto/pywinauto](https://github.com/pywinauto/pywinauto) | Python Windows UI automation | Carried forward from original list; recheck before adoption |
| [nunit/nunit](https://github.com/nunit/nunit) | .NET test framework | Carried forward from original list; recheck before adoption |
| [xunit/xunit](https://github.com/xunit/xunit) | .NET test framework | Carried forward from original list; recheck before adoption |

### Deployment

| Repository | Purpose | Notes |
|---|---|---|
| [wixtoolset/wix](https://github.com/wixtoolset/wix) | Windows Installer authoring | Carried forward from original list; recheck before adoption |
| [jrsoftware/issrc](https://github.com/jrsoftware/issrc) | Inno Setup installer builder | Carried forward from original list; recheck before adoption |
| [microsoft/msix-packaging](https://github.com/microsoft/msix-packaging) | MSIX SDK | Carried forward from original list; recheck before adoption |
| [velopack/velopack](https://github.com/velopack/velopack) | Application packaging and updates | Carried forward from original list; recheck before adoption |
| [winsw/winsw](https://github.com/winsw/winsw) | Windows service executable wrapper | Carried forward from original list; recheck before adoption |
| [microsoft/winget-cli](https://github.com/microsoft/winget-cli) | Windows Package Manager client | Carried forward from original list; recheck before adoption |
| [microsoft/winget-pkgs](https://github.com/microsoft/winget-pkgs) | WinGet package manifests | Carried forward from original list; recheck before adoption |

### Resources

| Repository | Purpose | Notes |
|---|---|---|
| [microsoft/Windows-classic-samples](https://github.com/microsoft/Windows-classic-samples) | Win32 API examples | Carried forward from original list; recheck before adoption |
| [microsoft/WindowsAppSDK-Samples](https://github.com/microsoft/WindowsAppSDK-Samples) | Windows App SDK examples | Carried forward from original list; recheck before adoption |
| [microsoft/WinUI-Gallery](https://github.com/microsoft/WinUI-Gallery) | WinUI control demonstrations | Carried forward from original list; recheck before adoption |
| [microsoft/Windows-driver-samples](https://github.com/microsoft/Windows-driver-samples) | WDK driver samples | Carried forward from original list; recheck before adoption |
| [MicrosoftDocs/win32](https://github.com/MicrosoftDocs/win32) | Win32 documentation source | Carried forward from original list; recheck before adoption |
| [MicrosoftDocs/windows-driver-docs](https://github.com/MicrosoftDocs/windows-driver-docs) | Driver documentation source | Carried forward from original list; recheck before adoption |
| [microsoft/terminal](https://github.com/microsoft/terminal) | Terminal and console source reference | Carried forward from original list; recheck before adoption |
| [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | Desktop integration source reference | Carried forward from original list; recheck before adoption |


