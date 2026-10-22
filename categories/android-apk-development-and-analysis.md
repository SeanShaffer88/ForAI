# Android APK development and analysis

[All categories](README.md) · [AI selection guide](../AGENTS.md) · [Practical APK guide](../docs/android-apk-development.md)

Selected primary documentation, README excerpts and repository metadata reviewed 2026-10-22. Version, license, maintenance and device-support checks remain project-specific; this is not a comprehensive adoption audit. No tool was automatically installed for this research.

| Resource | Useful for / constraints |
|---|---|
| [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) | Inspect manifest, DEX, resources and package size in Android Studio. |
| [apkanalyzer](https://developer.android.com/tools/apkanalyzer) | Scriptable package, manifest, DEX and resource inspection. |
| [Android CLI](https://developer.android.com/tools/android-cli) | Current command-line Android project and SDK workflows; recheck availability before replacing existing tooling. |
| [sdkmanager](https://developer.android.com/tools/sdkmanager) | SDK package management reference; fetched page marks it deprecated in favor of Android CLI, while existing SDK installations still use it. |
| [Android command-line builds](https://developer.android.com/build/building-cmdline) | Gradle-wrapper builds of APKs and app bundles from source. |
| [Android Gradle Plugin](https://developer.android.com/build/releases/about-agp) | Build-system compatibility and release guidance; pin compatible AGP, Gradle and JDK versions. |
| [Android build JDKs](https://developer.android.com/build/jdks) | Distinguish Gradle runtime JDK, toolchains, source levels and Android API availability. |
| [AAPT2](https://developer.android.com/tools/aapt2) | Compile/link Android resources and inspect packaging problems. |
| [D8](https://developer.android.com/tools/d8) | Convert Java bytecode to Android DEX; preserve minSdk and library/desugaring inputs. |
| [Apksigner](https://developer.android.com/tools/apksigner) | Sign and verify APKs; every subsequent byte modification invalidates signatures. |
| [Zipalign](https://developer.android.com/tools/zipalign) | Verify APK entry alignment; align before apksigner signing. |
| [App bundle format](https://developer.android.com/guide/app-bundle/app-bundle-format) | Understand base, feature and configuration splits versus distributable APKs. |
| [Bundletool](https://developer.android.com/tools/bundletool) | Generate and install device-specific APK sets from AABs; not a universal arbitrary-APK merger. |
| [Android app updates](https://developer.android.com/google/play/app-updates) | Package identity, signing compatibility and version rules for preserving installed data. |
| [APK signature v4](https://source.android.com/docs/security/features/apksigning/v4) | Understand incremental-install idsig sidecars and their relationship to APK signing. |
| [Android ABIs](https://developer.android.com/ndk/guides/abis) | Native architectures, calling conventions and packaging requirements. |
| [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes) | Separate native ELF alignment, ZIP alignment and runtime page-size assumptions. |
| [Android compatibility](https://developer.android.com/guide/app-compatibility) | Separate behavior changes affecting all apps from changes gated by target SDK. |
| [Android storage](https://developer.android.com/training/data-storage) | App-specific files, shared storage and permissions; scoped-storage implications. |
| [ADB](https://developer.android.com/tools/adb) | Install, inspect, launch and debug on authorized devices and emulators. |
| [Logcat](https://developer.android.com/tools/logcat) | Capture complete startup exceptions and correlate package/process logs. |
| [NDK stack symbolization](https://developer.android.com/ndk/guides/ndk-stack) | Symbolize native crash traces with exact matching unstripped libraries. |
| [Android testing](https://developer.android.com/studio/test) | Source-level and device test workflows; complement package checks with gameplay tests. |
| [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) | Understand install-time, fast-follow and on-demand game assets. |
| [APK expansion files](https://developer.android.com/google/play/expansion-files) | Legacy OBB naming, storage and downloader model; distinguish from custom caches. |
| [Offline-first architecture](https://developer.android.com/topic/architecture/data-layer/offline-first) | Local data sources, persistence and synchronization architecture; server-dependent games may need more than cached assets. |
| [Unity IL2CPP](https://docs.unity3d.com/Manual/IL2CPP.html) | AOT managed-to-native scripting backend; metadata stubs are not recovered game source. |
| [Unity AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html) | Runtime asset archives; match platform, engine and serialized type compatibility. |
| [Apktool](https://github.com/iBotPeaches/Apktool) | Decode/rebuild Android resources and smali; framework packages and exact tool version matter. |
| [JADX](https://github.com/skylot/jadx) | Java-like DEX decompilation for analysis; output is not a guaranteed recompilable source project. |
| [Google smali/baksmali](https://github.com/google/smali) | DEX assembler/disassembler and dexlib2; maintained fork, mixed component licenses require review. |
| [APKEditor](https://github.com/REAndroid/APKEditor) | Alternative resource decode/build, split merging and resource repair; validate merged manifests, ABIs and signatures. |
| [ARSCLib](https://github.com/REAndroid/ARSCLib) | Programmatic Android resource-table/binary-XML editing without aapt2. |
| [Androguard](https://github.com/androguard/androguard) | Python APK/DEX/resource inspection and analysis; select supported Python/tool version. |
| [APKiD](https://github.com/rednaga/APKiD) | Identify packers, protectors and obfuscators; heuristic classification, not decryption or a security verdict. |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Local static/dynamic mobile security analysis; separate service requirements and report false positives. |
| [OWASP MASTG](https://mas.owasp.org/MASTG/) | Mobile testing/reverse-engineering methodology and tool references. |
| [Frida Android](https://frida.re/docs/android/) | Runtime instrumentation on controlled devices; server/gadget, ABI and version compatibility matter. |
| [Objection](https://github.com/sensepost/objection) | Frida-based runtime exploration; gadget patching changes package and signing behavior. |
| [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) | Recover IL2CPP metadata/type/method maps and dummy assemblies; older maintenance, exact metadata-version limits. |
| [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) | Work-in-progress IL2CPP analysis and reconstruction; validate output against native instructions. |
| [UnityPy](https://github.com/K0lb3/UnityPy) | Script extraction and modification of Unity serialized assets; preserve references and re-read written output. |
| [AssetRipper](https://github.com/AssetRipper/AssetRipper) | Unity game-file analysis/export; exported projects do not imply complete recoverable source or behavior. |
| [UABEA](https://github.com/nesrak1/UABEA) | Unity bundle/serialized asset inspection and editing; upstream points to UABEANext as work in progress. |
| [UABEANext](https://github.com/nesrak1/UABEANext) | New multi-bundle Unity editor; work-in-progress successor, not a compatibility guarantee. |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Native ELF disassembly/decompilation; apply exact architecture, symbols and relocations. |
| [Keystone](https://github.com/keystone-engine/keystone) | Assemble architecture-specific native patches; GPL/commercial and component licensing require review. |
| [Unicorn](https://github.com/unicorn-engine/unicorn) | CPU-level execution of native patch tests; mocked framework boundaries do not test Android runtime behavior. |
| [pyelftools](https://github.com/eliben/pyelftools) | Read ELF headers, segments and symbols; translate RVAs through PT_LOAD segments rather than assuming file offsets. |
| [APKLab](https://github.com/APKLab/APKLab) | VS Code integration of APK analysis, smali and rebuild workflows; inspect bundled tools and AGPL license obligations. |
| [Flutter build modes](https://docs.flutter.dev/testing/build-modes) | Distinguish Flutter debug/JIT from release AOT artifacts before choosing an analysis path. |
| [React Native Android releases](https://reactnative.dev/docs/signed-apk-android) | Understand JS/assets, native packaging and signing of React Native Android builds. |
| [Godot Android export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html) | Godot Android toolchain, templates, package data and signing requirements. |
| [Perfetto](https://perfetto.dev/docs/) | System/app tracing for startup, scheduling and performance investigation. |
| [Android Monkey](https://developer.android.com/studio/test/monkey) | Device UI event stress testing; bound runs and inspect results rather than treating no crash as correctness. |
