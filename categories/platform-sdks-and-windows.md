# Platform SDKs and Windows

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/) | Win32 and WinRT headers, libraries and build tools; choose the target OS and SDK deliberately. |
| [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/) | Modern Windows application APIs; check deployment model and runtime requirements. |
| [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) | Native Windows platform reference, including COM and system services. |
| [WDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/) | Driver development, signing and debugging; requires a dedicated compatibility plan. |
| [.NET](https://learn.microsoft.com/en-us/dotnet/) | Managed runtime, C#, base libraries and application frameworks. |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | HTTP APIs, authentication, web applications and real-time services. |
| [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) | Embed Edge web content; account for runtime distribution and host boundaries. |
| [PowerShell SDK](https://learn.microsoft.com/en-us/powershell/scripting/developer/) | Automation modules and hosting PowerShell within applications. |
| [Windows UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) | Accessibility and application automation through supported control patterns. |
| [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Process, filesystem and system diagnostics. |
| [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) | Native crash dumps, symbols and kernel or user-mode debugging. |
| [WSL](https://learn.microsoft.com/en-us/windows/wsl/) | Linux development environment on Windows; distinguish host and guest paths. |
| [Windows Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects) | Windows process-tree lifetime and resource limits; suspended creation plus assignment prevents child escape before containment. Kill-on-close stops owned descendants; persistent build daemons need explicit handling. |

Project additions checked 2026-10-21: see the machine-readable index for scoped evidence and first-party testing limits.

Project additions checked 2026-10-22 (primary documentation only):

| Resource | Useful for / constraints |
|---|---|
| [WinHTTP request and redirect options](https://learn.microsoft.com/en-us/windows/win32/winhttp/option-flags) | Configure WinHTTP redirect, timeout and request options. Check option-setting return values; TLS downgrade refusal does not establish publisher authenticity or freshness. |
| [Microsoft Visual C++ runtime deployment](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) | Identify supported MSVC runtime packages and architecture/version requirements from Microsoft. Preserve redistribution terms; do not obtain individual runtime DLLs from arbitrary sites. |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [AutoHotkey](https://github.com/AutoHotkey/AutoHotkey) | AutoHotkey - macro-creation and automation-oriented scripting utility for Windows. GPL-2.0: derivative works must stay under the GPL. |
| [calculator](https://github.com/microsoft/calculator) | Windows Calculator: A simple yet powerful calculator that ships with Windows. |
| [DevHome](https://github.com/microsoft/devhome) | The new Dev Home experience for Windows! |
| [Files](https://github.com/files-community/Files) | A modern file manager that helps users organize their files and folders. |
| [fluentui system icons](https://github.com/microsoft/fluentui-system-icons) | Fluent System Icons are a collection of familiar, friendly and modern icons from Microsoft. |
| [MicaForEveryone](https://github.com/MicaForEveryone/MicaForEveryone) | Mica For Everyone is a tool to enable backdrop effects on the title bars of Win32 apps on Windows 11. |
| [nappgui src](https://github.com/frang75/nappgui_src) | SDK for building cross-platform desktop apps in ANSI-C. |
| [qwindowkit](https://github.com/stdware/qwindowkit) | Cross-platform frameless window framework for Qt. Support Windows, macOS, Linux. |
| [swift win32](https://github.com/compnerd/swift-win32) | A Windows application framework for Swift. |
| [windigo](https://github.com/rodrigocfd/windigo) | Windows API and GUI in idiomatic Go. |
| [Windows.UI.Composition Win32 Samples](https://github.com/microsoft/Windows.UI.Composition-Win32-Samples) | Windows.UI.Composition Win32 Samples. |
| [winsafe](https://github.com/rodrigocfd/winsafe) | Windows API and GUI in safe, idiomatic Rust. |
| [workspacer](https://github.com/workspacer/workspacer) | a tiling window manager for Windows. |
<!-- expansion-2026-11-11:end -->
