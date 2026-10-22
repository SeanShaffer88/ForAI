# Windows / PDB and PE tooling

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [MolecularMatters/raw_pdb](https://github.com/MolecularMatters/raw_pdb) | Read Microsoft PDB streams directly from C++ ; Low-level C++11 library; callers construct higher-level symbol abstractions |
| [wbenny/pdbex](https://github.com/wbenny/pdbex) | Reconstruct C structure and union declarations from PDB symbols ; Tool; symbol information can omit details needed for exact source reconstruction |
| [moyix/pdbparse](https://github.com/moyix/pdbparse) | Parse Microsoft PDB debug information using Python ; Library; GPL; verify compatibility with required PDB streams and Python version |
| [StackAndPointer/PDB-Insight](https://github.com/StackAndPointer/PDB-Insight) | Browse PDB types and functions and export symbol information ; Win32 and DIA SDK tool; supports symbol-server downloads |
| [trailofbits/pe-parse](https://github.com/trailofbits/pe-parse) | Parse Windows PE imports exports sections and relocations ; C++ library intended for robust executable analysis |
| [zodiacon/PEExplorer](https://github.com/zodiacon/PEExplorer) | Inspect Portable Executable structure in a GUI ; Desktop tool and parser reference; inspect repository branch and project requirements |
