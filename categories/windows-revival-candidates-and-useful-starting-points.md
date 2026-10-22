# Windows / Revival candidates and useful starting points

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Microsoft IPC](https://github.com/microsoft/IPC) | Existing C++/.NET applications need the same shared-memory protocol and low-copy behavior. ; Restore current MSVC/.NET builds; run cross-process tests for crashes, shutdown, message ownership and permissions; audit Boost and optional Bond. ; Named pipes or an existing supported messaging library; benchmark using the actual payloads. |
| [Tx](https://github.com/microsoft/Tx) | LINQ-style ETW queries provide reusable analysis that would otherwise be rewritten. ; Port only needed readers/operators to the chosen .NET and Rx versions; replay known trace fixtures. ; TraceEvent/PerfView APIs or KrabsETW plus a small query layer. |
| [SharpDX](https://github.com/sharpdx/SharpDX) | A working legacy application needs narrow fixes and migration would be disproportionately large. ; Isolate required assemblies; verify COM lifetime, ABI, architecture and current Windows behavior. ; Vortice.Windows and current generated bindings; avoid restoring unused API families. |
| [CrashRpt3](https://github.com/crashrpt3/crashrpt3) | An application needs their Windows exception-handler behavior or existing report format. ; Compare patch lineage; build a crash-type test matrix including fail-fast, stack overflow, thread handling and dump integrity. ; Crashpad integration or application-specific WER/minidump handling. |
| [CrashRpt2](https://github.com/CrashRpt/crashrpt2) | An application needs their Windows exception-handler behavior or existing report format. ; Compare patch lineage; build a crash-type test matrix including fail-fast, stack overflow, thread handling and dump integrity. ; Crashpad integration or application-specific WER/minidump handling. |
| [Microsoft PDB](https://github.com/microsoft/microsoft-pdb) | A missing debug-record definition or parser behavior blocks a symbol tool. ; Extract the minimum needed record definitions and tests; README explicitly says the full source does not currently build. ; RawPDB, DIA SDK or LLVM PDB tooling. |
| [C++ REST SDK](https://github.com/microsoft/cpprestsdk) | Existing code depends heavily on its asynchronous API and migration cost is substantial. ; Scope transport/TLS dependencies and regression tests; restore only the application-required functionality. ; libcurl or Boost.Beast, as suggested by the archived upstream. |
| [Bond](https://github.com/microsoft/bond) | Existing stored data or deployed peers require Bond wire compatibility. ; Test binary-format fixtures and schema evolution; audit parser/compiler dependencies and own necessary security fixes. ; A maintained serialization format for new protocols, with a migration bridge for existing data. |
