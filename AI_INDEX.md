# AI Resource Index

## 1. Win32 APIs & Native Windows Systems
* **Scope**: Low-level Windows integration, hooks, registry manipulation, and window management.
* **Key Files**: 
  * `modules/win32-apis/process_monitor.rs` - Real-time process creation/termination tracking.
  * `modules/win32-apis/window_hooks.cpp` - Low-level keyboard/mouse hooks and subclassing templates.

## 2. Rust Tooling & Portable Utilities
* **Scope**: Zero-dependency, lightweight, high-performance systems engineering.
* **Key Files**:
  * `modules/rust-tooling/installer_tracker/` - Filesystem change capture engine (akin to InstallScope core logic).
  * `modules/rust-tooling/portable_packager/` - Automated PortableApps structure generator.

## 3. Automation & Scripting
* **Scope**: Native batch utilities, PowerShell deployment scripts, and zero-telemetry environment tweaks.
* **Key Files**:
  * `modules/automation/win11_debloat.ps1` - Safe, modular component removal script.
  * `modules/automation/env_setup.bat` - Portable developer workstation initialization.

## 4. Agent Skills & Manifests
* **Scope**: Reusable modular prompts, context tokens, and capability definitions.
* **Key Files**:
  * `modules/agent-skills/npx-skills/` - Executable capability integrations.
  * `modules/agent-skills/manifests/` - Structured capability schemas.

## 5. UI/UX & Design Systems
* **Scope**: High-contrast interfaces, dark mode templates, and clean aesthetic layouts.
* **Key Files**:
  * `modules/ui-ux/red_black_theme.json` - High-contrast visual styling configuration.