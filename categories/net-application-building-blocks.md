# .NET application building blocks

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Polly](https://www.pollydocs.org/) | Resilience pipelines for timeouts, retries and circuit breaking; avoid retrying unsafe operations. |
| [Refit](https://github.com/reactiveui/refit) | Typed interface-based .NET HTTP clients; verify serializer and AOT support. |
| [Dapper](https://github.com/DapperLib/Dapper) | Lightweight .NET SQL mapping; application owns SQL and schema evolution. |
| [FluentValidation](https://docs.fluentvalidation.net/en/latest/) | Typed .NET validation rules; confirm framework and async integration support. |
| [CommunityToolkit MVVM](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/) | Observable models, commands and source generators for .NET UI architectures. |
| [Noda Time](https://nodatime.org/) | Explicit .NET date/time types; distinguish instants, time zones and local times. |
| [Humanizer](https://github.com/Humanizr/Humanizer) | Human-readable text, quantities and relative times; check culture behavior. |
| [CsvHelper](https://joshclose.github.io/CsvHelper/) | .NET CSV parsing and writing; configure dialects and malformed-data handling. |
| [System.IO.Pipelines](https://learn.microsoft.com/en-us/dotnet/standard/io/pipelines) | High-performance .NET streaming buffers; manage ownership and backpressure. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Spectre.Console](https://github.com/spectreconsole/spectre.console) | Build rich .NET terminal interfaces; provide plain output modes for redirected streams. |
| [CliWrap](https://github.com/Tyrrrz/CliWrap) | Launch and pipe child processes from .NET; the README states additional political terms of use alongside the MIT license. Review terms and cancellation behavior. |
| [Verify](https://github.com/VerifyTests/Verify) | Snapshot testing for .NET; upstream describes a maintenance-fee policy for official binaries released after September 1, 2026, separate from MIT source licensing. |
| [Bogus](https://github.com/bchavez/Bogus) | Generate synthetic .NET test data; seed generation and avoid treating fake data as anonymization. |
| [AutoFixture](https://github.com/AutoFixture/AutoFixture) | Create .NET test objects automatically; customize meaningful domain constraints. |
| [NSubstitute](https://github.com/nsubstitute/NSubstitute) | Create .NET test substitutes; keep assertions focused on observable behavior. |
| [Shouldly](https://github.com/shouldly/shouldly) | Readable .NET assertions and failure messages; confirm supported test runtimes. |
| [RecyclableMemoryStream](https://github.com/microsoft/Microsoft.IO.RecyclableMemoryStream) | Pool .NET stream buffers to reduce allocation pressure; dispose streams and set memory limits. |
| [Sprache](https://github.com/sprache/Sprache) | Compose small parsers in C#; assess grammar complexity and error-reporting requirements. GitHub reports its last push as 2024-04-18; maintenance responsiveness was not established. |
| [Superpower](https://github.com/datalust/superpower) | Build C# parsers with tokenization and diagnostics; design token and grammar rules explicitly. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [Lean](https://github.com/QuantConnect/Lean) | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) |
| [reactive](https://github.com/dotnet/reactive) | The Reactive Extensions for .NET (Rx.NET): compose asynchronous, event-based programs with LINQ-style operators; a learning curve, best for genuinely event-heavy code. |
| [SimplCommerce](https://github.com/simplcommerce/SimplCommerce) | A simple, cross platform, modulith ecommerce system built on .NET |
| [FusionCache](https://github.com/ZiggyCreatures/FusionCache) | FusionCache is an easy to use, fast and robust hybrid cache with advanced resiliency features. |
| [AspectCore-Framework](https://github.com/dotnetcore/AspectCore-Framework) | AspectCore is an AOP-based cross platform framework for .NET Standard. |
| [Papercut-SMTP](https://github.com/ChangemakerStudios/Papercut-SMTP) | Papercut SMTP -- The Simple Desktop Email Server |
| [Serenity](https://github.com/serenity-is/Serenity) | Business Apps Made Simple with Asp.Net Core MVC / TypeScript |
| [sharpcompress](https://github.com/adamhathcock/sharpcompress) | SharpCompress is a fully managed C# library to deal with many compression types and formats. |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [abp](https://github.com/abpframework/abp) | Open-source web application framework for ASP.NET Core! Offers an opinionated architecture to build enterprise software solutions with best practices on top of the .NET. LGPL-3.0: dynamic linking is permitted, static linking has obligations. |
| [aspnet api versioning](https://github.com/dotnet/aspnet-api-versioning) | Provides a set of libraries which add service API versioning to ASP.NET Core Minimal APIs, Controllers, gRPC, OData, and Web API (Classic). |
| [aspnetcore](https://github.com/dotnet/aspnetcore) | ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web applications on Windows, Mac, or Linux. |
| [AutoMapper](https://github.com/LuckyPennySoftware/AutoMapper) | A convention-based object-object mapper in .NET. License not detected by GitHub; check the repository license before use. |
| [CleanArchitecture](https://github.com/ardalis/CleanArchitecture) | Clean Architecture Solution Template: A proven Clean Architecture Template for ASP.NET Core 10. |
| [CleanArchitecture (jasontaylordev)](https://github.com/jasontaylordev/CleanArchitecture) | Clean Architecture Solution Template for ASP.NET Core. |
| [command line api](https://github.com/dotnet/command-line-api) | Command line parsing, invocation, and rendering of terminal output. |
| [DotNetCorePlugins](https://github.com/natemcmaster/DotNetCorePlugins) | .NET Core library for dynamically loading code. |
| [efcore](https://github.com/dotnet/efcore) | EF Core is a modern object-database mapper for .NET. It supports LINQ queries, change tracking, updates, and schema migrations. |
| [elsa core](https://github.com/elsa-workflows/elsa-core) | The Workflow Engine for .NET. |
| [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers) | Cross-platform .NET sample microservices and container based application that runs on Linux Windows and macOS. Powered by .NET 7, Docker Containers and Azure Kubernetes Services. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb) | Sample ASP.NET Core 8.0 reference application, now community supported: https://github.com/NimblePros/eShopOnWeb. |
| [jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API. GPL-2.0: derivative works must stay under the GPL. |
| [LiteDB](https://github.com/litedb-org/LiteDB) | LiteDB - A .NET NoSQL Document Store in a single data file. |
| [maui](https://github.com/dotnet/maui) | .NET MAUI is the .NET Multi-platform App UI, a framework for building native device applications spanning mobile, tablet, and desktop. |
| [maui samples](https://github.com/dotnet/maui-samples) | Samples for .NET Multi-Platform App UI (.NET MAUI). |
| [MediatR](https://github.com/LuckyPennySoftware/MediatR) | Simple, unambitious mediator implementation in .NET. License not detected by GitHub; check the repository license before use. |
| [mono](https://github.com/mono/mono) | Mono open source ECMA CLI, C# and .NET implementation. License not detected by GitHub; check the repository license before use. |
| [MQTTnet](https://github.com/dotnet/MQTTnet) | MQTTnet is a high performance .NET library for MQTT based communication. It provides a MQTT client and a MQTT server (broker). The implementation is based on the documentation from http://mqtt.org/. |
| [nlog](https://github.com/NLog/NLog) | NLog - Flexible and Structured Logging for various .NET Platforms. |
| [NSwag](https://github.com/RicoSuter/NSwag) | The Swagger/OpenAPI toolchain for .NET, ASP.NET Core and TypeScript. |
| [NuGet.Client](https://github.com/NuGet/NuGet.Client) | Client Tools for NuGet - including Visual Studio extensions, command line tools, and msbuild support. (Open issues on https://github.com/nuget/home/issues). License not detected by GitHub; check the repository license before use. |
| [Ocelot](https://github.com/ThreeMammals/Ocelot) | .NET API Gateway. |
| [OrchardCore](https://github.com/OrchardCMS/OrchardCore) | Orchard Core is an open-source modular and multi-tenant application framework built with ASP.NET Core, and a content management system (CMS) built on top of that framework. |
| [reverse proxy](https://github.com/dotnet/yarp) | A toolkit for developing high-performance HTTP reverse proxy applications. |
| [Silk.NET](https://github.com/dotnet/Silk.NET) | The high-speed OpenGL, OpenCL, OpenAL, OpenXR, GLFW, SDL, Vulkan, Assimp, WebGPU, and DirectX bindings library your mother warned you about. |
| [Templates](https://github.com/Dotnet-Boxed/Templates) | .NET project templates with batteries included, providing the minimum amount of code required to get you going faster. |
<!-- expansion-2026-11-11:end -->
