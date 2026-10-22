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
