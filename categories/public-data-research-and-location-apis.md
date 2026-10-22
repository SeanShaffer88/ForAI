# Public data research and location APIs

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Open-Meteo](https://open-meteo.com/en/docs) | Forecast API; free hosted endpoint is for noncommercial use under its current terms. Review paid/commercial access, attribution, limits and units. |
| [US Census API](https://www.census.gov/data/developers.html) | US demographic and economic datasets; select vintage, geography and variables. |
| [FRED API](https://fred.stlouisfed.org/docs/api/fred/) | Economic-series API reference; the documentation served a maintenance page during this review. Recheck availability, API-key requirements and series usage terms before integration. |
| [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) | Development indicators API; review pagination, revisions and dataset licenses. |
| [NASA APIs](https://api.nasa.gov/) | Space and Earth-data API directory; service-specific keys, limits and availability vary. |
| [NOAA weather API](https://www.weather.gov/documentation/services-web-api) | US forecasts, alerts and observations; follow service identification and cache guidance. |
| [USGS water APIs](https://api.waterdata.usgs.gov/) | Water measurements and geospatial data; check endpoint lifecycle and units. |
| [OpenAlex](https://docs.openalex.org/) | Scholarly graph API; verify current key, quota and snapshot terms. |
| [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Scholarly metadata and DOI lookup; identify client and respect rate limits. |
| [Europe PMC](https://europepmc.org/RestfulWebService) | Literature metadata and available full text; full-text rights differ by article. |
| [Wikidata Query Service](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service) | SPARQL over structured public knowledge; respect public-endpoint limits. |
| [OpenStreetMap Overpass](https://wiki.openstreetmap.org/wiki/Overpass_API) | Query OSM features; public instances have usage limits and ODbL obligations. |
| [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) | OSM geocoding software API; the OSMF public server has a separate policy including a 1 request/second maximum, identification and attribution. Check self-hosting or providers for heavier use. |
| [OSRM](https://project-osrm.org/docs/) | Routing engine and HTTP API; production hosting differs from public demos. |
