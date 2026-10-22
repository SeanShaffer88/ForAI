# Windows / Binary and build analysis

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [microsoft/SizeBench](https://github.com/microsoft/SizeBench) | Analyze and compare code and data size in Windows PE binaries ; Tool using binary and PDB pairs; useful for EXE DLL and SYS size regressions |
| [microsoft/binskim](https://github.com/microsoft/binskim) | Check compiler linker and security-relevant binary characteristics ; Binary analyzer with SARIF output; rules and supported formats depend on version |
| [microsoft/vcperf](https://github.com/microsoft/vcperf) | Capture MSVC compiler and linker performance traces ; C++ Build Insights tool; integrates with Windows Performance Analyzer |
| [microsoft/cpp-build-insights-samples](https://github.com/microsoft/cpp-build-insights-samples) | Examples of finding compilation and code-generation bottlenecks ; SDK sample resource rather than a standalone runtime |
| [microsoft/clrmd](https://github.com/microsoft/clrmd) | Inspect .NET processes and memory dumps programmatically ; Microsoft.Diagnostics.Runtime.dll; validate supported CLR and library major version |
| [rainers/cv2pdb](https://github.com/rainers/cv2pdb) | Convert supported CodeView or DWARF debug information to PDB ; Specialized converter; validate compiler output and debug-record coverage |
