# Graphics multimedia scientific and geospatial

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference: free, open-source 2D/3D engine with GDScript, C#, and C++; this project uses Godot 4 for its Android games. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing library (C++, Python, and more): the default toolbox for detection, tracking, and image pipelines — large, so link only the modules you need. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |

Project addition checked 2026-10-22:

| Resource | Useful for / constraints |
|---|---|
| [Qwt](https://qwt.sourceforge.io/) | Qt technical plotting widgets. Qwt License 1.0 (LGPL2.1 with exceptions); retain notices and evaluate Qt/runtime licenses. Pinned 6.3.0 built with Qt 6.12/MSVC x64 for DiffImg after the Qt5 baseline. Rebuilds pass, but MSVC anonymous-namespace RTTI makes DLL bytes vary with build path. |

Project reference checked 2026-10-22:

| Resource | Useful for / constraints |
|---|---|
| [three.js](https://github.com/mrdoob/three.js) | MIT JavaScript 3D renderer; bundle modules locally for offline WebGL2 games. Native Android wrappers still require current WebView and device-specific GPU, lifecycle and touch testing. Emberline project check: official documentation read; npm 0.186.1 MIT metadata/integrity and bundled LICENSE inspected; rendered touch UI and software-WebGL browser tests passed. Physical Android device untested. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) | Render vector maps in browsers; obtain tiles and data under suitable terms. |
| [MapLibre Native](https://github.com/maplibre/maplibre-native) | Embed map rendering in native applications; verify platform bindings and tile licensing. |
| [OpenLayers](https://github.com/openlayers/openlayers) | Build browser mapping applications with multiple data sources; manage projections and attribution. |
| [Leaflet](https://github.com/Leaflet/Leaflet) | Create interactive browser maps; evaluate plugins, tile providers and accessibility. |
| [deck.gl](https://github.com/visgl/deck.gl) | Render large geospatial datasets with GPU layers; budget browser memory and GPU capabilities. |
| [CesiumJS](https://github.com/CesiumGS/cesium) | Visualize globes and 3D geospatial scenes; distinguish engine licensing from hosted content services. |
| [TiTiler](https://github.com/developmentseed/titiler) | Serve raster tiles through Python web APIs; control remote-data access and caching. |
| [Shapely](https://github.com/shapely/shapely) | Analyze planar geometries in Python; understand coordinate-system and GEOS requirements. |
| [GeoPandas](https://github.com/geopandas/geopandas) | Work with geospatial dataframes; choose coordinate reference systems and compatible native dependencies. |
| [Rasterio](https://github.com/rasterio/rasterio) | Read and write geospatial rasters in Python; inspect GDAL drivers and binary compatibility. Repository license text uses BSD-style redistribution terms. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [transformers](https://github.com/huggingface/transformers) | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. |
| [effectcraft](https://github.com/storytold/effectcraft) | EffectCraft: An open-source motion graphics and compositing tool written by scratch in pure Rust |
| [thorvg](https://github.com/thorvg/thorvg) | A production-ready C++ vector graphics engine supporting SVG and Lottie formats, featuring advanced rendering backends such as WebGPU for high-performance graphics. |
| [Simd](https://github.com/ermig1979/Simd) | C++ image processing and machine learning library with using of SIMD: SSE, AVX, AVX-512, AMX for x86/x64, NEON, SVE for ARM, HVX for Hexagon |
| [libsndfile](https://github.com/libsndfile/libsndfile) | A C library for reading and writing sound files containing sampled audio data. |
| [rom](https://github.com/hanakai-rb/rom) | Data mapping and persistence toolkit for Ruby |
| [FluidAudio](https://github.com/FluidInference/FluidAudio) | Frontier CoreML audio models in your apps — text-to-speech, speech-to-text, voice activity detection, and speaker diarization. In Swift, powered by SOTA open source. |
| [metube](https://github.com/alexta69/metube) | Self-hosted video downloader for YouTube and other sites (web UI for yt-dlp) |

<!-- expansion-2026-11-10:begin -->
## Expansion — 2026-11-10

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-10.md).

| Resource | Useful for / constraints |
|---|---|
| [OBS Studio](https://github.com/obsproject/obs-studio) | Open-source capture and streaming studio with a plugin API. Useful for recording demos and test evidence; GPU encoders and capture sources depend on drivers. |
<!-- expansion-2026-11-10:end -->

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [aseprite](https://github.com/aseprite/aseprite) | Animated sprite editor & pixel art tool (Windows, macOS, Linux). No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [bokeh](https://github.com/bokeh/bokeh) | Interactive Data Visualization in the browser, from Python. |
| [d3](https://github.com/d3/d3) | Bring data to life with SVG, Canvas and HTML. :bar_chart::chart_with_upwards_trend::tada. |
| [digital video introduction](https://github.com/leandromoreira/digital_video_introduction) | A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding). Translations. |
| [editly](https://github.com/mifi/editly) | Slick, declarative command line video editing & API. |
| [engine (playcanvas)](https://github.com/playcanvas/engine) | Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF. |
| [ffmpeg libav tutorial](https://github.com/leandromoreira/ffmpeg-libav-tutorial) | FFmpeg libav tutorial - learn how media works from basic to transmuxing, transcoding and more. Translations. |
| [ffsubsync](https://github.com/smacke/ffsubsync) | Automagically synchronize subtitles with video. |
| [filament](https://github.com/google/filament) | Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS, WebGPU, and WebGL2. |
| [gfx](https://github.com/gfx-rs/gfx) | [maintenance mode] A low-overhead Vulkan-like GPU API for Rust. |
| [gifify](https://github.com/vvo/gifify) | Convert any video file to an optimized animated GIF. |
| [glTF](https://github.com/KhronosGroup/glTF) | glTF – Runtime 3D Asset Delivery. License not detected by GitHub; check the repository license before use. |
| [HandBrake](https://github.com/HandBrake/HandBrake) | HandBrake's development repository. License not detected by GitHub; check the repository license before use. |
| [inkscape](https://github.com/inkscape/inkscape) | Project Website: https://inkscape.org - Code Repository: https://gitlab.com/inkscape/inkscape - Draw freely. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [krita](https://github.com/KDE/krita) | Krita is a free and open source cross-platform application that offers an end-to-end solution for creating digital art files from scratch built on the KDE and Qt frameworks. GPL-3.0: derivative works must stay under the GPL. |
| [lossless cut](https://github.com/mifi/lossless-cut) | The swiss army knife of lossless video/audio editing. GPL-2.0: derivative works must stay under the GPL. |
| [lwjgl3](https://github.com/LWJGL/lwjgl3) | LWJGL is a Java library that enables cross-platform access to popular native APIs useful in the development of graphics (OpenGL, Vulkan, bgfx), audio (OpenAL, Opus), parallel computing (OpenCL, CUDA) and XR (OpenVR, LibOVR,. |
| [mapbox gl js](https://github.com/mapbox/mapbox-gl-js) | Interactive, thoroughly customizable maps in the browser, powered by vector tiles and WebGL. License not detected by GitHub; check the repository license before use. |
| [matplotlib](https://github.com/matplotlib/matplotlib) | matplotlib: plotting with Python. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [mini3d](https://github.com/skywind3000/mini3d) | 3D Software Renderer in 700 Lines !! |
| [model viewer](https://github.com/google/model-viewer) | Easily display interactive 3D models on the web and in AR! |
| [mpv](https://github.com/mpv-player/mpv) | Command line media player. License not detected by GitHub; check the repository license before use. |
| [mypaint](https://github.com/mypaint/mypaint) | MyPaint is a simple drawing and painting program that works well with Wacom-style graphics tablets. GPL-2.0: derivative works must stay under the GPL. |
| [proj4js](https://github.com/proj4js/proj4js) | JavaScript library to transform coordinates from one coordinate system to another, including datum transformations. License not detected by GitHub; check the repository license before use. |
| [pyvista](https://github.com/pyvista/pyvista) | 3D visualization and mesh analysis for science and engineering. |
| [QGIS](https://github.com/qgis/QGIS) | QGIS is a free, open source, cross platform (lin/win/mac) geographical information system (GIS). GPL-2.0: derivative works must stay under the GPL. |
| [react three fiber](https://github.com/pmndrs/react-three-fiber) | A React renderer for Three.js. |
| [SFML](https://github.com/SFML/SFML) | Simple and Fast Multimedia Library. |
| [SPIRV Cross](https://github.com/KhronosGroup/SPIRV-Cross) | SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V and disassembling SPIR-V back to high level languages. |
| [vega](https://github.com/vega/vega) | A visualization grammar. |
| [Vulkan Samples](https://github.com/KhronosGroup/Vulkan-Samples) | One stop solution for all Vulkan samples. |
| [Vulkan ValidationLayers](https://github.com/KhronosGroup/Vulkan-ValidationLayers) | Vulkan Validation Layers (VVL). License not detected by GitHub; check the repository license before use. |
| [wgpu](https://github.com/gfx-rs/wgpu) | A cross-platform, safe, pure-Rust graphics API. |
| [WickedEngine](https://github.com/turanszkij/WickedEngine) | 3D engine with modern graphics. |
<!-- expansion-2026-11-11:end -->
