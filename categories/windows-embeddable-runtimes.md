# Windows / Embeddable runtimes

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [wasm-micro-runtime/wasm-micro-runtime](https://github.com/wasm-micro-runtime/wasm-micro-runtime) | Embed WebAssembly interpreter and AOT execution in native programs ; WAMR current location; Windows MSVC and MinGW documentation exists; modes and WASI support differ by configuration |
| [wasm3/wasm3](https://github.com/wasm3/wasm3) | Compact WebAssembly interpreter for native applications ; Minimal-maintenance phase per README; check required Wasm and WASI features |
| [svaarala/duktape](https://github.com/svaarala/duktape) | Compact JavaScript interpreter embeddable in C and C++ ; Master tracks incompatible 3.x changes; README points 2.x users to v2-maintenance |
| [wren-lang/wren](https://github.com/wren-lang/wren) | Small class-based scripting VM for embedding ; C runtime; check host integration and Windows build tooling |
| [albertodemichelis/squirrel](https://github.com/albertodemichelis/squirrel) | Embeddable scripting language with native integration ; Official Squirrel repository; README documents Windows x86 and amd64 |
| [ChaiScript/ChaiScript](https://github.com/ChaiScript/ChaiScript) | Header-based scripting integration designed for C++ ; C++ embedded language; evaluate compile time and supported toolchains |
