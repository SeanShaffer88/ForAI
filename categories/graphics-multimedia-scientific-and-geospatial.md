# Graphics multimedia scientific and geospatial

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Vulkan](https://docs.vulkan.org/) | Cross-platform graphics and compute APIs; confirm driver and feature support. |
| [WebGPU](https://www.w3.org/TR/webgpu/) | Browser graphics and compute API specification. |
| [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) | Windows graphics and multimedia platform APIs. |
| [SDL](https://wiki.libsdl.org/) | Cross-platform windows, input, audio and multimedia support. |
| [Godot](https://docs.godotengine.org/en/stable/) | Game engine and scripting reference. |
| [Unity](https://docs.unity3d.com/) | Game engine and deployment reference; review licensing. |
| [Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine) | Game and real-time engine documentation; review project-specific terms. |
| [OpenXR](https://www.khronos.org/openxr/) | Portable XR interface standard and SDK ecosystem. |
| [FFmpeg](https://ffmpeg.org/documentation.html) | Audio/video processing; build configuration changes licensing and codecs. |
| [GStreamer](https://gstreamer.freedesktop.org/documentation/) | Streaming media pipelines and plugin framework. |
| [OpenCV](https://docs.opencv.org/) | Computer vision and image processing. |
| [NumPy](https://numpy.org/doc/) | Numerical arrays and native extension interfaces. |
| [SciPy](https://docs.scipy.org/doc/scipy/) | Scientific algorithms, optimization and signal processing. |
| [GDAL](https://gdal.org/) | Geospatial data formats and transformation. |
| [PROJ](https://proj.org/) | Coordinate reference systems and transformations. |

Project addition checked 2026-10-22:

| Resource | Useful for / constraints |
|---|---|
| [Qwt](https://qwt.sourceforge.io/) | Qt technical plotting widgets. Qwt License 1.0 (LGPL2.1 with exceptions); retain notices and evaluate Qt/runtime licenses. Built pinned Qwt 6.3.0 source with Qt5/MSVC x64 for DiffImg. Rebuilds worked, but MSVC anonymous-namespace RTTI makes DLL bytes vary with build path. |
