# Windows / Networking and virtual devices

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [basil00/WinDivert](https://github.com/basil00/WinDivert) | Capture filter modify and reinject packets from user-mode code ; WinDivert.dll plus kernel driver; assess redistribution driver signing and platform support |
| [WireGuard/wintun](https://github.com/WireGuard/wintun) | Expose a layer-3 virtual network adapter through wintun.dll ; GitHub mirror; official upstream git.zx2c4.com/wintun; obtain architecture-matched supported binaries |
| [winfsp/winspd](https://github.com/winfsp/winspd) | Implement user-mode storage devices that appear as SCSI disks ; Storage proxy framework distinct from file-level WinFsp; assess driver deployment and license |
