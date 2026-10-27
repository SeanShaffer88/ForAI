# API contracts clients and networking

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Describe HTTP API contracts; generator support can lag specification versions. |
| [AsyncAPI](https://www.asyncapi.com/docs) | Describe event-driven interfaces and message contracts. |
| [JSON Schema](https://json-schema.org/learn) | Data validation contracts; pin the schema dialect. |
| [gRPC](https://grpc.io/docs/) | Typed RPC and streaming; assess browser proxy and language support. |
| [Protocol Buffers](https://protobuf.dev/) | Schema-based serialization and code generation. |
| [GraphQL](https://graphql.org/learn/) | Typed query schemas and API execution concepts. |
| [OpenAPI Generator](https://openapi-generator.tech/docs/usage/) | Generate clients and server stubs; assess each language generator independently. |
| [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) | Generate typed API clients from OpenAPI. |
| [Buf](https://buf.build/docs/) | Protobuf linting, breaking-change checks and code generation. |
| [Connect RPC](https://connectrpc.com/docs/) | RPC libraries and protocols with browser-oriented integration. |
| [curl and libcurl](https://curl.se/docs/) | HTTP and other protocol transfers from CLI or native code. |
| [HTTPX](https://www.python-httpx.org/) | Python synchronous and asynchronous HTTP clients. |
| [Requests](https://requests.readthedocs.io/) | Python synchronous HTTP integration. |
| [WebSockets](https://websockets.readthedocs.io/) | Python WebSocket client and server implementation. |
| [WebRTC](https://webrtc.org/) | Real-time browser and native audio, video and data. |
| [Postman](https://learning.postman.com/) | API exploration, collections and collaboration; hosted features may require plans. |
| [Bruno](https://docs.usebruno.com/) | File-based API collections and local API workflows. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Inspect and script HTTP traffic in authorized environments; manage interception certificates carefully. |
| [grpcurl](https://github.com/fullstorydev/grpcurl) | Call gRPC endpoints from the command line; provide reflection or matching descriptors. |
| [Hurl](https://github.com/Orange-OpenSource/hurl) | Write text-based HTTP request and response checks; isolate credentials and mutable test data. |
| [Vegeta](https://github.com/tsenart/vegeta) | Generate HTTP loads and analyze results; control rate and use authorized test targets. |
| [oha](https://github.com/hatoo/oha) | Benchmark HTTP services from the terminal; choose realistic concurrency and request patterns. |
| [HTTPie CLI](https://github.com/httpie/cli) | Explore HTTP APIs from the terminal; protect authentication data and saved sessions. GitHub reports its last push as 2024-12-17; maintenance responsiveness was not established. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [socketcluster](https://github.com/SocketCluster/socketcluster) | Highly scalable realtime pub/sub and RPC framework |
| [micro](https://github.com/vercel/micro) | Asynchronous HTTP microservices |
| [type-graphql](https://github.com/MichalLytek/type-graphql) | Create GraphQL schema and resolvers with TypeScript, using classes and decorators! |
| [undici](https://github.com/nodejs/undici) | An HTTP/1.1 client, written from scratch for Node.js |
| [textual](https://github.com/Textualize/textual) | The lean application framework for Python. Build sophisticated user interfaces with a simple Python API. Run your apps in the terminal and a web browser. |
| [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | A standard API for single-agent reinforcement learning environments, with popular reference environments and related utilities (formerly Gym) |
| [xberg](https://github.com/xberg-io/xberg) | Polyglot document intelligence with a Rust core: extract text, metadata, images, tables, and structured data from 106 formats across 140 file extensions, plus code intelligence for 371 languages. Fifteen bindings, with CLI, REST API, and MCP server. |
| [FluxDown](https://github.com/zerx-lab/FluxDown) | Rust 驱动的多协议下载管理器，支持 HTTP/FTP/BitTorrent 磁力链接及 HLS/DASH 流媒体，智能多线程加速与浏览器无缝集成。精美界面，极致性能，永久免费，零广告。 |
| [rama](https://github.com/plabayo/rama) | modular service framework to move and transform network packets |
| [gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
| [kitex](https://github.com/cloudwego/kitex) | Go RPC framework with high-performance and strong-extensibility for building micro-services. |
| [sftpgo](https://github.com/drakkan/sftpgo) | Full-featured and highly configurable SFTP, HTTP/S, FTP/S and WebDAV server - S3, Google Cloud Storage, Azure Blob |
| [kubo](https://github.com/ipfs/kubo) | IPFS implementation in Go: a daemon that stores and serves content-addressed data, with a CLI, HTTP Gateway, and RPC API |
| [keto](https://github.com/ory/keto) | The most scalable and customizable permission server on the market. Fix your slow or broken permission system with Google's proven "Zanzibar" approach. Supports ACL, RBAC, and more. Written in Go, cloud native, headless, API-first. Available as a service on Ory Network and for self-hosters. |
| [ziti](https://github.com/openziti/ziti) | The parent project for OpenZiti. Here you will find the executables for a fully zero-trust, programmable network @OpenZiti |
| [nbio](https://github.com/lesismal/nbio) | Pure Go 1000k+ connections solution, support tls/http1.x/websocket and basically compatible with net/http, with high-performance and low memory cost, non-blocking, event-driven, easy-to-use. |
| [go-doudou](https://github.com/unionj-cloud/go-doudou) | go-doudou（doudou pronounce /dəudəu/）is OpenAPI 3.0 (for REST) spec and Protobuf v3 (for grpc) based lightweight microservice framework. It supports monolith service application as well. |
| [circuit](https://github.com/gocircuit/circuit) | Circuit: Dynamic cloud orchestration http://gocircuit.org |
| [go-guardian](https://github.com/shaj13/go-guardian) | Go-Guardian is a golang library that provides a simple, clean, and idiomatic way to create powerful modern API and web authentication. |
| [webgo](https://github.com/naughtygopher/webgo) | A microframework to build web apps; with handler chaining, middleware support, and most of all; standard library compliant HTTP handlers(i.e. http.HandlerFunc). |
| [jOOL](https://github.com/jOOQ/jOOL) | jOOλ - The Missing Parts in Java 8 jOOλ improves the JDK libraries in areas where the Expert Group's focus was elsewhere. It adds tuple support, function support, and a lot of additional functionality around sequential Streams. The JDK 8's main efforts (default methods, lambdas, and the Stream API) were focused around maintaining backwards compatibility and implementing a functional API for parallelism. |
| [jetty.project](https://github.com/jetty/jetty.project) | Eclipse Jetty® - Web Container & Clients - supports HTTP/3, HTTP/2, HTTP/1, websocket, servlets, and more |
| [google-http-java-client](https://github.com/googleapis/google-http-java-client) | Google HTTP Client Library for Java |
| [FastEndpoints](https://github.com/FastEndpoints/FastEndpoints) | A light-weight REST API development framework for ASP.NET 8 and newer. |
| [grpcui](https://github.com/fullstorydev/grpcui) | An interactive web UI for gRPC, along the lines of postman |
| [piranha.core](https://github.com/PiranhaCMS/piranha.core) | Piranha CMS is the friendly editor-focused CMS for .NET that can be used both as an integrated CMS or as a headless API. |
| [WebApiClient](https://github.com/dotnetcore/WebApiClient) | A REST API library with better functionality, performance, and scalability than refit |
| [brpc](https://github.com/apache/brpc) | brpc is an Industrial-grade RPC framework using C++ Language, which is often used in high performance system such as Search, Storage, Machine learning, Advertisement, Recommendation etc. "brpc" means "better RPC". |
| [OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO) | Reading, writing, and processing images in a wide variety of file formats, using a format-agnostic API, aimed at VFX applications. |
| [CppServer](https://github.com/chronoxor/CppServer) | Ultra fast and low latency asynchronous socket server & client C++ library with support TCP, SSL, UDP, HTTP, HTTPS, WebSocket protocols and 10K connections problem solution |
| [Mobile-Detect](https://github.com/serbanghita/Mobile-Detect) | Mobile_Detect is a lightweight PHP class for detecting mobile devices (including tablets). It uses the User-Agent string combined with specific HTTP headers to detect the mobile environment. |
| [client](https://github.com/openai-php/client) | ⚡️ OpenAI PHP is a supercharged community-maintained PHP API client that allows you to interact with OpenAI API. |
| [webpack-encore](https://github.com/symfony/webpack-encore) | A simple but powerful API for processing & compiling assets built around Webpack |
| [BetterReflection](https://github.com/Roave/BetterReflection) | :crystal_ball: Better Reflection is a reflection API that aims to improve and provide more features than PHP's built-in reflection API. |
| [faraday](https://github.com/lostisland/faraday) | Simple, but flexible HTTP client library, with support for multiple backends. |
| [flutter-permission-handler](https://github.com/Baseflow/flutter-permission-handler) | Permission plugin for Flutter. This plugin provides a cross-platform (iOS, Android) API to request and check permissions. |
| [netshoot](https://github.com/nicolaka/netshoot) | a Docker + Kubernetes network trouble-shooting swiss-army container |
| [flannel](https://github.com/flannel-io/flannel) | flannel is a network fabric for containers, designed for Kubernetes |
| [aria2](https://github.com/aria2/aria2) | aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. It supports HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink. |
| [homepage](https://github.com/gethomepage/homepage) | A highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations. |
| [iris](https://github.com/kataras/iris) | The fastest HTTP/2 Go Web Framework. New, modern and easy to learn. Fast development with Code you control. Unbeatable cost-performance ratio :rocket: |
| [scalar](https://github.com/scalar/scalar) | Scalar is an open-source API platform: 🌐 Modern REST API Client 📖 Beautiful API References ✨ 1st-Class OpenAPI/Swagger Support |
| [connexion](https://github.com/spec-first/connexion) | Connexion is a modern Python web framework that makes spec-first and api-first development easy. |
| [cowboy](https://github.com/ninenines/cowboy) | Small, fast, modern HTTP server for Erlang/OTP. |
| [tarpc](https://github.com/google/tarpc) | An RPC framework for Rust with a focus on ease of use. |
| [preact](https://github.com/preactjs/preact) | ⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM. |
| [react-admin](https://github.com/marmelab/react-admin) | A frontend Framework for single-page applications on top of REST/GraphQL APIs, using TypeScript, React and Material Design |
| [vue3-dnd](https://github.com/hcg1023/vue3-dnd) | React Dnd implementation in Vue Composition-api. |
| [pocket-mocker](https://github.com/tianchangNorth/pocket-mocker) | In-page HTTP controller for frontend development. Intercept, modify, and simulate API responses directly in the browser. |
| [insomnia](https://github.com/Kong/insomnia) | The open-source, cross-platform API client for GraphQL, REST, WebSockets, SSE and gRPC. With Cloud, Local and Git storage. |

## Niche expansion — 2026-10-27

Additional entries from a focused discovery pass; see the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-27-round-2.md). Repository API metadata was checked, but these links are not README, license, security, compatibility, or adoption audits.

| Resource | Useful for / constraints |
|---|---|
| [json-server](https://github.com/typicode/json-server) | Get a full fake REST API with zero coding in less than 30 seconds (seriously) |
| [API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist) | Checklist of the most important security countermeasures when designing, testing, and releasing your API |
| [jq](https://github.com/jqlang/jq) | Command-line JSON processor |
| [swagger-codegen](https://github.com/swagger-api/swagger-codegen) | swagger-codegen contains a template-driven engine to generate documentation, API clients and server stubs in different languages by parsing your OpenAPI / Swagger definition. |
| [api-guidelines](https://github.com/microsoft/api-guidelines) | Microsoft REST API Guidelines |
| [resty](https://github.com/go-resty/resty) | Simple HTTP, REST, and SSE client library for Go |
| [RestSharp](https://github.com/restsharp/RestSharp) | Simple REST and HTTP API Client for .NET |
| [nango](https://github.com/NangoHQ/nango) | Connect your agents & product to 1,000 APIs. |
| [rest-assured](https://github.com/rest-assured/rest-assured) | Java DSL for easy testing of REST services |
| [tyk](https://github.com/TykTechnologies/tyk) | Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol) |
| [http-api-design](https://github.com/interagent/http-api-design) | HTTP API design guide extracted from work on the Heroku Platform API |
| [httparty](https://github.com/jnunemaker/httparty) | :tada: Makes http fun again! |
| [crud](https://github.com/nestjsx/crud) | NestJs CRUD for RESTful APIs |
| [rest-client](https://github.com/rest-client/rest-client) | Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions. |
| [restangular](https://github.com/mgonto/restangular) | AngularJS service to handle Rest API Restful Resources properly and easily |
| [cortex](https://github.com/cortex-docs/cortex) | Cortex - Generates interactive API documentation, typed SDKs, and MCP servers from OpenAPI, AsyncAPI, GraphQL, gRPC, OpenRPC, and Markdown. |
| [restful-api-guidelines](https://github.com/zalando/restful-api-guidelines) | A model set of guidelines for RESTful APIs and Events, created by Zalando |
| [FOSRestBundle](https://github.com/FriendsOfSymfony/FOSRestBundle) | This Bundle provides various tools to rapidly develop RESTful API's with Symfony |
| [NelmioApiDocBundle](https://github.com/nelmio/NelmioApiDocBundle) | Generates documentation for your REST API from attributes |
| [api-umbrella](https://github.com/NatLabRockies/api-umbrella) | Open source API management platform |
| [fusio](https://github.com/apioo/fusio) | Self-Hosted API Management for Builders |
| [ng-admin](https://github.com/marmelab/ng-admin) | Add an AngularJS admin GUI to any RESTful API |
| [Buzz](https://github.com/kriswallsmith/Buzz) | PHP's lightweight HTTP client |
| [stepci](https://github.com/stepci/stepci) | Automated API Testing and Quality Assurance |
| [milkman](https://github.com/warmuuh/milkman) | An Extensible Request/Response Workbench |
| [sandman](https://github.com/jeffknupp/sandman) | Sandman "makes things REST". |
| [excon](https://github.com/excon/excon) | Usable, fast, simple HTTP 1.1 for Ruby |
| [shadcn-admin-kit](https://github.com/marmelab/shadcn-admin-kit) | Component kit to build your Admin app with shadcn/ui |
| [unirest-php](https://github.com/Kong/unirest-php) | Unirest in PHP: Simplified, lightweight HTTP client library. |
| [jsend](https://github.com/omniti-labs/jsend) | JSend is a specification for a simple, no-frills, JSON based format for application-level communication. |
| [product-apim](https://github.com/wso2/product-apim) | Welcome to the WSO2 API Manager source code! For info on working with the WSO2 API Manager repository and contributing code, click the link below. |
| [zato](https://github.com/zatosource/zato) | ESB, SOA, REST, APIs and Cloud Integrations in Python |
| [Negotiation](https://github.com/willdurand/Negotiation) | Content Negotiation tools for PHP. |
| [restler](https://github.com/danwrong/restler) | REST client library for node.js |
| [unirest-nodejs](https://github.com/Kong/unirest-nodejs) | Unirest in Node.js: Simplified, lightweight HTTP client library. |
| [rest-hapi](https://github.com/JKHeadley/rest-hapi) | 🚀 A RESTful API generator for Node.js |
