# WebAssembly and plugin runtimes

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Wasmtime](https://docs.wasmtime.dev/) | Embed WebAssembly/WASI execution; expose only needed host capabilities. |
| [Wasmer](https://docs.wasmer.io/) | WebAssembly runtime and embedding ecosystem; verify bindings and target support. |
| [WASI](https://wasi.dev/) | System-interface specifications for WebAssembly; preview versions are not interchangeable. |
| [WebAssembly Component Model](https://component-model.bytecodealliance.org/) | Cross-language component interfaces and WIT; check runtime/toolchain interoperability. |
| [Extism](https://extism.org/docs/concepts/host-sdk/) | WebAssembly plugin SDKs and host integration; define permissions and plugin ABI. |
| [WAMR](https://github.com/wasm-micro-runtime/wasm-micro-runtime) | WebAssembly runtime for constrained and embedded hosts; upstream moved from bytecodealliance to wasm-micro-runtime. Check engines and architectures. |
