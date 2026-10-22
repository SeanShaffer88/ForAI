# Android APK development, analysis and preservation reference

Researched 2026-10-22. A practical reference for future APK projects: inspect first, identify the engine and missing components, make the smallest necessary change, then validate the actual installed behavior. This is a broad working reference, not a claim to cover every Android technology.

The research used nine Exa searches requesting 90 results across formats, compilation, reverse engineering, native/game engines, compatibility, diagnostics, security and offline preservation. Search results were filtered for primary upstream sources; duplicate and third-party results are not counted as independently verified authorities. The resource index below contains 57 selected references. GitHub metadata was separately checked for 23 projects. Documentation excerpts and repository metadata establish discovery and scoped review, not a full license/security audit or universal tool compatibility.

## Fast path for the next request

1. Preserve the input and record its SHA-256, source, package ID, version, SDK requirements, signing certificate and archive inventory. Keep originals read-only.
2. Determine whether the input is an APK, AAB, APKS, XAPK, split set, installer stub or a package plus external data. Inventory every supplied file before selecting tools.
3. Record the actual target device OS/API level, ABI list and page size when available. A marketing model name and “latest Android” are insufficient to determine all compatibility properties.
4. Identify the engine/backend. Java/smali, Unity Mono, Unity IL2CPP, native C/C++, Flutter AOT, Hermes and Godot require different analysis paths.
5. Reproduce and collect a full log before changing the build. Distinguish installation, Java startup, native loading, assets, login, simulation, UI, persistence and gameplay failures.
6. Prefer original source if supplied. Otherwise establish an unmodified decode/rebuild baseline, then patch one identified cause at a time.
7. Retain the update signing key, package ID and increasing versionCode for iterative builds. Keep signing secrets outside distributable archives and public repositories.
8. Rebuild, align, sign, verify and hash. Then test first launch, upgrade, relaunch, offline behavior, representative actions and save/load on a device.

A successful install establishes package acceptance. A successful launch establishes startup. Neither proves gameplay, progress persistence or full offline completeness.

## Package formats and contents

| Artifact | Meaning | Common mistake |
|---|---|---|
| APK | Installable Android package: compiled manifest, resource table, DEX, native libraries and assets | Treating its Java-like decompilation as the original source tree |
| AAB | Publishing bundle used to generate device APKs | Attempting to install the AAB directly or merely renaming it |
| APKS | bundletool APK-set archive | Installing only one random APK without required splits |
| XAPK/APKM | Distributor container conventions, often holding APKs plus metadata/OBBs | Assuming one standard schema or that downloaded game data is included |
| OBB | Legacy expansion payload; often a ZIP or custom archive | Assuming every custom CDN cache is an OBB |
| Asset pack | Play Asset Delivery content with install-time, fast-follow or on-demand delivery | Assuming base installation implies all content is present |
| OTA APK update | Replacement package with compatible identity/signing and version rules | Changing signing key or application ID and expecting existing private data to follow |

Useful locations: `AndroidManifest.xml`, `resources.arsc`, `classes.dex`, `classes2.dex`, `res/`, `assets/`, `lib/arm64-v8a/`, `lib/armeabi-v7a/`, `META-INF/`. APK v2/v3 signing data is in a signing block, so looking only at `META-INF/` is insufficient. DEX numbering, compression methods, duplicate entries and ZIP local-header consistency matter during repacking. See [bundle format](https://developer.android.com/guide/app-bundle/app-bundle-format) and [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer).

## Build from source

Use the existing Gradle wrapper and project dependency choices. Record AGP, Gradle, JDK runtime, Java/Kotlin language levels, compileSdk, targetSdk, minSdk, NDK, CMake and ABI filters. These settings solve different problems. Raising targetSdk changes behavior obligations; it does not rewrite deprecated code or rebuild old native libraries.

Typical pipeline: Java/Kotlin compilation -> D8/R8 DEX processing; resource compilation/linking with AAPT2; native compilation/linking through the selected NDK; packaging; alignment; signing. A normal Android source build should let AGP manage this. Manual `javac`/D8 integration is useful for tightly scoped injected bootstrap code, but requires correct Android stubs, minSdk/desugaring inputs and multidex initialization.

Example commands from a configured source checkout:

```powershell
.\gradlew.bat :app:assembleDebug
.\gradlew.bat :app:assembleRelease
.\gradlew.bat :app:bundleRelease
```

These are templates, not promises that a project has those modules/tasks. Inspect its Gradle files first. Do not hard-code “latest” JDK or plugin versions independently: use the [JDK guide](https://developer.android.com/build/jdks) and [AGP compatibility information](https://developer.android.com/build/releases/about-agp). The fetched [sdkmanager reference](https://developer.android.com/tools/sdkmanager) now marks it deprecated in favor of Android CLI; retain compatibility with existing installed toolchains and verify CLI availability before migrating.

### Observed Windows asset-path pitfall (2026-10-22)

An original offline WebView game built with Windows AAPT2/build-tools 35.0.0 contained raw backslashes in nested vendor ZIP entries. Android AssetManager could not open the corresponding forward-slash paths, leaving the module graph unable to start. Desktop-browser tests and signature/CRC checks alone had not caught it. The failure was reproduced on an AOSP Android 15 emulator, and normalizing ZIP entry names before alignment/signing restored startup. This is evidence for that manual build pipeline, not a claim that all AAPT2/Gradle packages are affected.

Inspect `ZipInfo.orig_filename` when using Python on Windows: `filename` can conceal the raw backslashes. The inventory script now reports `nonportable_archive_paths` separately from traversal-style unsafe paths. Verify raw archive names, bundled-file bytes, and actual Android asset reads; then cold-launch without connectivity. Keep `resources.arsc` uncompressed when rebuilding. The regression and fix are recorded in [Emberline 0.1.1](https://github.com/SeanShaffer88/emberline/releases/tag/v0.1.1). No new dependency or catalog entry was added for this correction.

## Decode, edit and rebuild an existing APK

[Apktool](https://github.com/iBotPeaches/Apktool) is a primary path for resources plus smali. [JADX](https://github.com/skylot/jadx) is primarily for reading and navigating Java-like code. Edit smali or use an appropriate bytecode library for changes; recompiling all JADX output is usually a poor baseline.

```powershell
java -jar apktool.jar d original.apk -o decoded
java -jar apktool.jar b -f decoded -o rebuilt-unsigned.apk
zipalign -f -P 16 4 rebuilt-unsigned.apk rebuilt-aligned.apk
apksigner sign --ks private-development.p12 --out rebuilt-signed.apk rebuilt-aligned.apk
apksigner verify --verbose --print-certs rebuilt-signed.apk
zipalign -c -P 16 4 rebuilt-signed.apk
```

Keep passwords out of committed commands; use supported environment/file mechanisms. Align before signing with apksigner. Never change the signed ZIP afterward. The `-P 16` check covers ZIP entry placement; it does not repair incompatible ELF segments or runtime page assumptions. See [zipalign](https://developer.android.com/tools/zipalign), [apksigner](https://developer.android.com/tools/apksigner) and [16 KB guidance](https://developer.android.com/guide/practices/page-sizes).

Rebuild concerns: framework resources, vendor-specific IDs, compiled resource tables, nine-patch images, register counts, invoke argument widths, wide values, try/catch regions, exception flow and resource-ID stability. When Apktool cannot round-trip a resource table, investigate [APKEditor](https://github.com/REAndroid/APKEditor) or [ARSCLib](https://github.com/REAndroid/ARSCLib), preserve the baseline and compare the resulting manifest/resources. Their ability to merge splits does not guarantee a semantically complete, installable universal APK.

When changing package identity, review providers/authorities, permission names, deep links, explicit component references, package-bound file paths and third-party SDK configuration. Renaming the manifest package alone can leave conflicts or broken integrations. Re-signing cannot preserve update access to an original publisher's installed app without a signing identity accepted by Android. A separate experimental package is a separate data sandbox. See [Android update rules](https://developer.android.com/google/play/app-updates).

## Engine-specific analysis

| Backend | Typical evidence | Practical route |
|---|---|---|
| Java/Kotlin | DEX and application classes | JADX for understanding; smali/dexlib2 for modifications |
| Unity Mono | Unity data plus managed assemblies | Match engine version and inspect managed IL and serialized assets |
| Unity IL2CPP | `libil2cpp.so` plus `global-metadata.dat` | Match exact metadata/native pair; recover types/method maps; inspect native instructions |
| Native C/C++ | `.so` libraries and JNI bridges | ELF loader/ABI analysis, symbols, JNI registration, disassembly and native logs |
| Flutter release | `libflutter.so`, `libapp.so`, flutter assets | Dart AOT/engine analysis; Java patching may only affect platform glue |
| React Native | JS bundle/Hermes and native libraries | Identify plain JS versus Hermes bytecode plus versioned native integration |
| Godot | Godot libraries and packaged project data | Match engine/export format and source availability |
| WebView/Cordova | HTML/JS assets plus platform wrappers | Inspect local content, service calls and Android bridge behavior |

For Unity, [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) produces metadata maps/dummy assemblies, not reconstructed original method bodies. Its last repository push observed in this research was August 2024; it can still fit older games, but newer metadata support must be checked. [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) explicitly describes itself as work in progress. Validate inferred types, generic sharing and calling conventions against native instructions.

[UnityPy](https://github.com/K0lb3/UnityPy), [AssetRipper](https://github.com/AssetRipper/AssetRipper) and [UABEA/UABEANext](https://github.com/nesrak1/UABEA) address assets, not missing server gameplay. Match engine/platform, serialized formats, external references, bundle manifests and hashes. Re-read every edited serialized asset. TextAsset bytes may need lossless handling rather than ordinary UTF-8 replacement. An exported Unity project may lack original scripts, shaders, licenses and editor settings. Consult version-specific documentation instead of applying current Unity instructions blindly to legacy builds.

## Native patching and verification

Translate virtual addresses through ELF `PT_LOAD` segments: file offset = virtual address - segment virtual base + segment file base. Text offsets sometimes coincide with RVAs while data offsets differ; never extrapolate from one matching function. Account for relocations, load bias and ASLR. Use [pyelftools](https://github.com/eliben/pyelftools) or [LIEF](https://github.com/lief-project/LIEF) for structure inspection.

Keep exact-input hashes and expected original bytes for every patch. Refuse mismatched builds. Respect function extent, branch range, instruction alignment, return ABI, managed-object layouts, hidden generic MethodInfo arguments, GC-managed references, exception paths, callee-saved registers and stack alignment. Compare patch ranges to reject overlaps, including code caves. A code cave must be demonstrably unreachable through ordinary entry, alternate branches and callbacks; it is not merely a run of convenient bytes.

[Capstone](https://github.com/capstone-engine/capstone), [Keystone](https://github.com/keystone-engine/keystone) and [Unicorn](https://github.com/unicorn-engine/unicorn) support disassembly, assembly and CPU tests. Unit emulation is useful for arguments, branches, state-machine paths and ABI preservation. Mocked IL2CPP/JNI boundaries do not validate the real runtime, collector or serialized save format.

For numeric modifications, distinguish signed integer widths from fixed-point raw representations. Target resource prototypes/inventory categories rather than every number: globally maximizing values can corrupt timers, array indices, health, damage, experience or state enums. Test arithmetic headroom, reads/writes, costs, refunds, collection events, UI updates and save/reload. Record any classifier assumptions and device-test gaps.

## Modern Android compatibility

Check the actual device instead of assuming all phones of one model have identical firmware behavior. [ABI documentation](https://developer.android.com/ndk/guides/abis) explains architecture and calling conventions; an ARM32 library does not become ARM64 by moving it to another directory. Translation availability is device-dependent. APK ZIP alignment does not change native ELF alignment. A missing symbol, unsupported instruction, page-size assumption or absent library can require native source/rebuild or a substantive port.

Separate all-app behavior changes from target-SDK-gated changes using the [compatibility guide](https://developer.android.com/guide/app-compatibility). Examine install target restrictions, exported components, pending intent mutability, cleartext networking, permissions, notification/background-service rules, dynamic code loading, package visibility and scoped storage as applicable. Do not “fix” compatibility by raising SDK numbers without testing the resulting obligations.

App-private data, external app-specific data, shared media and user-selected documents have different access rules. Private saves are not generally accessible through ordinary ADB on production non-debuggable apps. `run-as` requires an eligible debuggable package; `adb backup` is not a general modern backup solution. Preserve working installations and offer an in-app export/import facility when the authorized application can support one. See [storage guidance](https://developer.android.com/training/data-storage).

## Offline game preservation

Inventory code, static rules/tables, localization, textures/audio, bundles, manifests, player state, time and random state, quests/tutorial flags and service dependencies separately. A cache can restore assets while leaving login, account lookup, purchases, analytics, advertisements, clock synchronization, session creation or command execution waiting on retired services.

Prefer existing local simulation/storage branches when present. Otherwise an offline port may need a new local backend or reconstruction of server-owned gameplay; cached textures cannot supply that logic. Keep local identity separate from an online account. Removing network permission is an effective enforcement boundary for a deliberately offline build, but SDK startup must still handle unavailable services without exceptions or endless waits.

Trace callback and coroutine state machines through initial, resumed, error and repeated-start states. A status check can report signed out while a resumed coroutine still performs an unconditional current-user lookup. Verify the whole continuation reaches the title/tutorial, not merely that an exception disappeared.

For recovered caches, preserve provenance and hashes; compare the app/engine/metadata revision; validate archive CRC, manifest dependencies, every required bundle and parsed assets. Zero-length marker files can be legitimate completion markers. Manifest download size may differ from decoded cache size. Retain irreplaceable assets instead of running an online cleanup policy that deletes content it cannot re-download. Never import another player's account/session credentials as part of content recovery.

Safe installation of embedded content requires path confinement, free-space estimation, CRC/size checks, temporary files plus atomic completion, interruption repair and an independent content revision marker. Upgrading launcher/code alone should not re-extract gigabytes or erase saves. Treat archive content as data and preserve app-owned progress. Test airplane-mode launch, restart, purchases/costs, dungeon completion, rewards, failure recovery and save/load. See [offline-first architecture](https://developer.android.com/topic/architecture/data-layer/offline-first), [PAD](https://developer.android.com/guide/playcore/asset-delivery) and [OBBs](https://developer.android.com/google/play/expansion-files).

## Diagnostics and a minimum test record

Useful read-only diagnostics on an authorized connected device:

```powershell
adb devices -l
adb shell getprop ro.build.version.release
adb shell getprop ro.build.version.sdk
adb shell getprop ro.product.cpu.abilist
adb shell getconf PAGE_SIZE
adb shell pm path com.example.app
adb shell dumpsys package com.example.app
adb logcat -d -v threadtime > startup-log.txt
```

Capture complete exceptions, nested causes and native tombstones. PID filters miss logs after a process restart; UID filtering and package context can help. Some log options vary by Android version. Diagnostic copies can contain sensitive data; collect the relevant app scope and keep logs private. Vendor warnings that precede successful Unity startup are not automatically the cause of a later hang. Use [logcat](https://developer.android.com/tools/logcat), exact-build [ndk-stack](https://developer.android.com/ndk/guides/ndk-stack), [Perfetto](https://perfetto.dev/docs/) and device observation as appropriate.

Record input/output hashes; tool versions; patch manifest; certificate fingerprint; package/version/min/target SDK; ABIs; permissions; ZIP integrity; DEX/asset/native-code comparisons; signature verification; ZIP/ELF alignment; device model/OS/API/page size; tested routes; save/load results and known limitations. Distinguish static checks, CPU emulation, emulator tests, physical-device tests and user-reported results.

| Symptom | First investigation |
|---|---|
| Update rejected | Signing certificate, application ID, versionCode, split consistency |
| “Not compatible” or install blocked | Full installer error, SDK restrictions, ABI and missing splits |
| `UnsatisfiedLinkError` / dlopen failure | Library ABI/dependencies/symbols, compression/alignment, JNI path |
| Resource rebuild failure | Framework resources, IDs, aapt2 version, table obfuscation |
| Background or endless loading | Full callback/coroutine flow, first exception, missing content/service waits |
| Post-login crash | Local simulation/state completeness and residual social/account SDK calls |
| Game runs but progression disappears | Actual local command path, serialization, save timing and upgrade identity |
| Fine on emulator, broken on phone | ARM versus x86, graphics/API/extensions, drivers, page size, storage and OS behavior |

## Tool selection and license/maintenance limits

Use canonical upstream releases and pinned checksums; match Python/JDK/.NET versions and CPU architecture. A Python package's pure-Python source can still depend on native wheels that are unavailable for the newest interpreter. On Windows use literal paths and native PowerShell file operations, short controlled work directories when path limits matter, and named per-project tool roots. Do not shadow Python modules with filenames such as `inspect.py`, `dis.py`, `json.py` or `typing.py`.

GitHub metadata on 2026-10-22 identified Apache-2.0 for Apktool, JADX, APKEditor, ARSCLib, Androguard, Ghidra and LIEF; MIT for Il2CppDumper, Cpp2IL, UnityPy and UABEA variants; GPL-family metadata for MobSF, Objection, Keystone and Unicorn; AGPL-3.0 for APKLab. Some projects returned mixed/unknown license metadata (including smali, APKiD, Capstone, pyelftools and Frida): inspect actual license files and components before redistribution. Metadata is a starting point, not a complete compliance assessment. Tool licenses do not grant redistribution rights to an analyzed game's code/assets. Preserve provenance; publish reusable original tooling/references separately from proprietary packages and signing material.

## Primary source and tool index

The following entries were selected from primary platform/engine documentation, upstream repositories and repository metadata. Purposes are original summaries. Recheck versions, maintenance, licenses and device support before adopting a tool. Some documentation URLs redirect and should be refreshed for a future project. No research-only tool here was automatically installed.

| Resource | Purpose and constraints |
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
| [Capstone](https://github.com/capstone-engine/capstone) | Scriptable disassembly for exact native instruction review; review component license files. |
| [Keystone](https://github.com/keystone-engine/keystone) | Assemble architecture-specific native patches; GPL/commercial and component licensing require review. |
| [Unicorn](https://github.com/unicorn-engine/unicorn) | CPU-level execution of native patch tests; mocked framework boundaries do not test Android runtime behavior. |
| [LIEF](https://github.com/lief-project/LIEF) | Inspect/modify ELF, DEX and other binaries; validate loader-visible structure after changes. |
| [pyelftools](https://github.com/eliben/pyelftools) | Read ELF headers, segments and symbols; translate RVAs through PT_LOAD segments rather than assuming file offsets. |
| [APKLab](https://github.com/APKLab/APKLab) | VS Code integration of APK analysis, smali and rebuild workflows; inspect bundled tools and AGPL license obligations. |
| [Flutter build modes](https://docs.flutter.dev/testing/build-modes) | Distinguish Flutter debug/JIT from release AOT artifacts before choosing an analysis path. |
| [React Native Android releases](https://reactnative.dev/docs/signed-apk-android) | Understand JS/assets, native packaging and signing of React Native Android builds. |
| [Godot Android export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html) | Godot Android toolchain, templates, package data and signing requirements. |
| [Perfetto](https://perfetto.dev/docs/) | System/app tracing for startup, scheduling and performance investigation. |
| [Android Monkey](https://developer.android.com/studio/test/monkey) | Device UI event stress testing; bound runs and inspect results rather than treating no crash as correctness. |
