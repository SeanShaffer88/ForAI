# Windows / Native networking and data

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [libevent/libevent](https://github.com/libevent/libevent) | Asynchronous event notification and buffered network I/O ; C library with Windows CMake build instructions |
| [nanomsg/nng](https://github.com/nanomsg/nng) | Brokerless messaging with request reply and other communication patterns ; Native C library; NNG 2 introduces API changes from NNG 1 |
| [an-tao/trantor](https://github.com/an-tao/trantor) | Event-driven nonblocking TCP networking and thread pools ; C++ library with Windows MSVC build support |
| [libssh2/libssh2](https://github.com/libssh2/libssh2) | Embed SSH2 client functionality ; Native C library; select and configure Windows crypto backend |
| [zeux/pugixml](https://github.com/zeux/pugixml) | Parse modify and query XML using XPath ; Native C++ library; Unicode conversion support |
| [weidai11/cryptopp](https://github.com/weidai11/cryptopp) | Native cryptographic algorithms and supporting utilities ; C++ library; inspect integration and algorithm choices for project needs |
| [abdes/cryptopp-cmake](https://github.com/abdes/cryptopp-cmake) | Integrate Crypto++ using modern CMake targets ; Build integration repository rather than the Crypto++ implementation |
