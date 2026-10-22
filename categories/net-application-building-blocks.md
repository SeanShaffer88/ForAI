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
