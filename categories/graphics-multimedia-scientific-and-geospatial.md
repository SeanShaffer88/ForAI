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
