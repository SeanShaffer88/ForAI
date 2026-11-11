# Desktop mobile and device SDKs

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Qt](https://doc.qt.io/) | C++ GUI and platform framework; evaluate module licensing and distribution. Qt 6.12.0 MSVC2022 x64 shared SDK tested with DiffImg; open-source LGPLv3/GPL module terms and commercial LTS patch availability are distinct. |
| [Avalonia](https://docs.avaloniaui.net/) | Cross-platform .NET desktop UI framework (Windows, macOS, Linux) with XAML and a WPF-like model; the main WPF alternative when Linux/macOS support matters. |
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | Cross-platform .NET applications; check target-specific toolchains. |
| [Electron](https://www.electronjs.org/docs/latest/) | Desktop apps using Chromium and Node.js; isolate privileged host APIs. |
| [Tauri](https://v2.tauri.app/) | Desktop and mobile application host with web UI; check native prerequisites. |
| [Flutter](https://docs.flutter.dev/) | Dart UI framework and platform integration. |
| [React Native](https://reactnative.dev/docs/getting-started) | Native mobile UI with React and platform modules. |
| [Android SDK](https://developer.android.com/develop) | Android APIs, Jetpack, tooling and device behavior. |
| [Apple Developer](https://developer.apple.com/documentation/) | Apple platform SDKs and frameworks; shipping requires platform toolchain checks. |
| [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/get-started.html) | Shared Kotlin code across Android, iOS, desktop, and web targets; share logic first — shared UI (Compose Multiplatform) is the younger, riskier layer. |
| [Zephyr](https://docs.zephyrproject.org/latest/) | Embedded RTOS and device tooling; select release and supported board. |
| [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | Espressif device SDK; select the exact chip and SDK release. |
| [FreeRTOS](https://www.freertos.org/Documentation/00-Overview) | Embedded real-time kernel and supporting libraries. |
| [ROS 2](https://docs.ros.org/) | Robotics middleware, packages and distribution documentation. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [kivy](https://github.com/kivy/kivy) | Open source UI framework written in Python, running on Windows, Linux, macOS, Android and iOS |
| [Magisk](https://github.com/topjohnwu/Magisk) | The Magic Mask for Android: systemless root and module framework; powerful device modification — expect SafetyNet/Play Integrity and warranty implications. |
| [Pake](https://github.com/tw93/Pake) | Turn any website into a lightweight desktop app with one command, on macOS, Windows and Linux. |
| [OpenBitFun](https://github.com/GCWing/OpenBitFun) | OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development. |
| [JUCE](https://github.com/juce-framework/JUCE) | JUCE is an open-source cross-platform C++ application framework for desktop and mobile applications, including VST, VST3, AU, AUv3, LV2 and AAX audio plug-ins. |
| [HorizonCalendar](https://github.com/airbnb/HorizonCalendar) | A declarative, performant, iOS calendar UI component that supports use cases ranging from simple date pickers all the way up to fully-featured calendar apps. |
| [Valet](https://github.com/square/Valet) | Valet lets you securely store data in the iOS, tvOS, watchOS, or macOS Keychain without knowing a thing about how the Keychain works. It’s easy. We promise. |
| [PinLayout](https://github.com/layoutBox/PinLayout) | Fast Swift Views layouting without auto layout. No magic, pure code, full control and blazing fast. Concise syntax, intuitive, readable & chainable. [iOS/macOS/tvOS/CALayer] |
| [MotionBook](https://github.com/younatics/MotionBook) | 📖 103 open-source iOS motion, transition and UI libraries, catalogued for people and agents (catalog.json + llms.txt); 59 run live in the MotionBook app |
| [swift-markdown-engine](https://github.com/nodes-app/swift-markdown-engine) | A native AppKit Markdown editor for macOS, built on TextKit 2 and bridged to SwiftUI. |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is the AI collaborative workspace where you achieve more without losing control of your data. The leading open source Notion alternative. |
| [bloc](https://github.com/felangel/bloc) | A predictable state management library that helps implement the BLoC design pattern |
| [flutter_architecture_samples](https://github.com/brianegan/flutter_architecture_samples) | TodoMVC for Flutter |
| [samples](https://github.com/flutter/samples) | A collection of Flutter examples and demos |
| [flutter_roadmap](https://github.com/olexale/flutter_roadmap) | Highly Subjective Roadmap to Flutter Development |
| [flutter-go](https://github.com/alibaba/flutter-go) | flutter 开发者帮助 APP，包含 flutter 常用 140+ 组件的demo 演示与中文文档 |
| [drift](https://github.com/simolus3/drift) | Drift is an easy to use, reactive, typesafe persistence library for Dart & Flutter. |
| [flutter_form_builder](https://github.com/flutter-form-builder-ecosystem/flutter_form_builder) | Simple form maker for the Flutter framework: prebuilt form fields with validation on top of Flutter's Form, cutting form boilerplate. |
| [authpass](https://github.com/authpass/authpass) | AuthPass - Password Manager based on Flutter for all platforms. Keepass 2.x (KDBX 3 and KDBX 4) compatible. |
| [dynamic_widget](https://github.com/dengyin2000/dynamic_widget) | A Backend-Driven UI toolkit, build your dynamic UI with json, and the json format is very similar with flutter widget code. |
| [mobx.dart](https://github.com/mobxjs/mobx.dart) | MobX for the Dart language. Hassle-free, reactive state-management for your Dart and Flutter apps. |
| [NativeScript](https://github.com/NativeScript/NativeScript) | ⚡ Write Native with TypeScript ✨ Best of all worlds (TypeScript, Swift, Objective C, Kotlin, Java, Dart). Use what you love ❤️ Angular, React, Solid, Svelte, Vue with: iOS (UIKit, SwiftUI), Android (View, Jetpack Compose), Flutter and you name it compatible. |
| [react-hook-form](https://github.com/react-hook-form/react-hook-form) | 📋 React Hooks for form state management and validation (Web + React Native) |
| [swiper](https://github.com/nolimits4web/swiper) | Most modern mobile touch slider with hardware accelerated transitions |
| [framework7](https://github.com/framework7io/framework7) | Full featured HTML framework for building iOS & Android apps |
| [react-native-maps](https://github.com/react-native-maps/react-native-maps) | React Native Mapview component for iOS + Android |
| [OnsenUI](https://github.com/OnsenUI/OnsenUI) | Mobile app development framework and SDK using HTML5 and JavaScript. Create beautiful and performant cross-platform mobile apps. Based on Web Components, and provides bindings for Angular 1, 2, React and Vue.js. |
| [marktext](https://github.com/marktext/marktext) | 📝A simple and elegant markdown editor, available for Linux, macOS and Windows. |
| [electron-react-boilerplate](https://github.com/electron-react-boilerplate/electron-react-boilerplate) | A Foundation for Scalable Cross-Platform Apps |
| [Mailspring](https://github.com/Foundry376/Mailspring) | :love_letter: A beautiful, fast and fully open source mail client for Mac, Windows and Linux. |
| [Signal-Desktop](https://github.com/signalapp/Signal-Desktop) | A private messenger for Windows, macOS, and Linux. |
| [reactotron](https://github.com/infinitered/reactotron) | A desktop app for inspecting your React JS and React Native projects. macOS, Linux, and Windows. |
| [electron-vite](https://github.com/alex8088/electron-vite) | Next generation Electron build tooling based on Vite 新一代 Electron 开发构建工具，支持源代码保护 |
| [webtorrent-desktop](https://github.com/webtorrent/webtorrent-desktop) | ❤️ Streaming torrent app for Mac, Windows, and Linux |
| [min](https://github.com/minbrowser/min) | A fast, minimal browser that protects your privacy |
| [menubar](https://github.com/max-mapper/menubar) | ➖ high level way to create menubar desktop applications with electron |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [arduino esp32](https://github.com/espressif/arduino-esp32) | Arduino core for the ESP32 family of SoCs. LGPL-2.1: dynamic linking is permitted, static linking has obligations. |
| [arduino ide](https://github.com/arduino/arduino-ide) | Arduino IDE 2.x. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [capacitor](https://github.com/ionic-team/capacitor) | Build cross-platform Native Progressive Web Apps for iOS, Android, and the Web. |
| [cordova android](https://github.com/apache/cordova-android) | Apache Cordova Android. |
| [create react native app](https://github.com/expo/create-react-native-app) | Create React Native apps that run on iOS, Android, and web. |
| [egui](https://github.com/emilk/egui) | egui: an easy-to-use immediate mode GUI in Rust that runs on both web and native. |
| [engine](https://github.com/flutter-team-archive/engine) | The Flutter engine. |
| [expo](https://github.com/expo/expo) | An open-source framework for making universal native apps with React. Expo runs on Android, iOS, and the web. |
| [fiddle](https://github.com/electron/fiddle) | electron: The easiest way to get started with Electron. |
| [flet](https://github.com/flet-dev/flet) | Build realtime web, mobile and desktop apps in Python only. No frontend experience required. |
| [fluent reader](https://github.com/yang991178/fluent-reader) | Modern desktop RSS reader built with Electron, React, and Fluent UI. |
| [flutter boost](https://github.com/alibaba/flutter_boost) | FlutterBoost is a Flutter plugin which enables hybrid integration of Flutter for your existing native apps with minimum efforts. |
| [flutter server box](https://github.com/lollipopkit/flutter_server_box) | ServerBox - high performance server toolbox app & server written in Flutter & Rust. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [flutter webrtc](https://github.com/flutter-webrtc/flutter-webrtc) | WebRTC plugin for Flutter Mobile/Desktop/Web. |
| [go flutter](https://github.com/go-flutter-desktop/go-flutter) | Flutter on Windows, MacOS and Linux - based on Flutter Embedding, Go and GLFW. |
| [iced](https://github.com/iced-rs/iced) | A cross-platform GUI library for Rust, inspired by Elm. |
| [micropython](https://github.com/micropython/micropython) | MicroPython - a lean and efficient Python implementation for microcontrollers and constrained systems. License not detected by GitHub; check the repository license before use. |
| [PakePlus](https://github.com/Sjj1024/PakePlus) | Turn any webpage/HTML/Vue/React and so on into desktop and mobile app under 5M with easy in few minutes. 轻松将任意网站/HTML/Vue/React等项目构建为轻量级(小于5M)多端桌面应用和手机应用仅需几分钟. https://ppofficial.netlify.app. |
| [pico sdk](https://github.com/raspberrypi/pico-sdk) | Repository with no description on GitHub. |
| [platformio core](https://github.com/platformio/platformio-core) | Your Gateway to Embedded Software Development Excellence :alien. |
| [pyglet](https://github.com/pyglet/pyglet) | pyglet is a cross-platform windowing and multimedia library for Python, for developing games and other visually rich applications. |
| [pyside setup](https://github.com/pyside/pyside-setup) | Git super project for PySide. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [qtbase](https://github.com/qt/qtbase) | Qt Base (Core, Gui, Widgets, Network, ...). No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [react native (facebook)](https://github.com/react/react-native) | A framework for building native applications using React. |
| [react native windows](https://github.com/microsoft/react-native-windows) | A framework for building native Windows apps with React. License not detected by GitHub; check the repository license before use. |
| [rubick](https://github.com/rubickCenter/rubick) | Electron based open source toolbox, free integration of rich plug-ins. 基于 electron 的开源工具箱，自由集成丰富插件。. |
| [slint](https://github.com/slint-ui/slint) | Slint is an open-source declarative GUI toolkit to build native user interfaces for Rust, C++, JavaScript, or Python apps. License not detected by GitHub; check the repository license before use. |
| [termux app](https://github.com/termux/termux-app) | Termux - a terminal emulator application for Android OS extendible by variety of packages. License not detected by GitHub; check the repository license before use. |
<!-- expansion-2026-11-11:end -->
