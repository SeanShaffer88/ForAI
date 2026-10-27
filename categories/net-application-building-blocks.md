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
| [reactive](https://github.com/dotnet/reactive) | The Reactive Extensions for .NET |
| [SimplCommerce](https://github.com/simplcommerce/SimplCommerce) | A simple, cross platform, modulith ecommerce system built on .NET |
| [FusionCache](https://github.com/ZiggyCreatures/FusionCache) | FusionCache is an easy to use, fast and robust hybrid cache with advanced resiliency features. |
| [AspectCore-Framework](https://github.com/dotnetcore/AspectCore-Framework) | AspectCore is an AOP-based cross platform framework for .NET Standard. |
| [Papercut-SMTP](https://github.com/ChangemakerStudios/Papercut-SMTP) | Papercut SMTP -- The Simple Desktop Email Server |
| [Serenity](https://github.com/serenity-is/Serenity) | Business Apps Made Simple with Asp.Net Core MVC / TypeScript |
| [sharpcompress](https://github.com/adamhathcock/sharpcompress) | SharpCompress is a fully managed C# library to deal with many compression types and formats. |
