# Collaboration local state and rich text

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Yjs](https://docs.yjs.dev/) | CRDT shared data for collaborative apps; persistence, transport and authorization are separate. |
| [Automerge](https://automerge.org/docs/hello/) | Local-first collaborative data structures and synchronization; assess storage growth and language support. |
| [ProseMirror](https://prosemirror.net/docs/) | Structured rich-text editing toolkit; application owns schema and collaboration policy. |
| [Tiptap](https://tiptap.dev/docs) | Rich-text editor built on ProseMirror; distinguish open-source extensions from paid services. |
| [Lexical](https://lexical.dev/docs/intro) | Extensible text-editor framework; evaluate import/export and accessibility. |
| [CodeMirror](https://codemirror.net/docs/) | Embeddable code editor and language extensions. |
| [Monaco Editor](https://microsoft.github.io/monaco-editor/) | Browser code editor; integrate web workers and bundling. Upstream states mobile browsers/frameworks are unsupported. |
| [Dexie](https://dexie.org/docs/) | IndexedDB wrapper for browser persistence; handle upgrades and storage limits. |
| [RxDB](https://rxdb.info/) | Reactive local database and replication; distinguish open-source and premium plugins. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [PouchDB](https://github.com/apache/pouchdb) | Client-side document storage and replication; the canonical repository is now Apache PouchDB in incubation. Design conflict handling explicitly. |
| [RxJS](https://github.com/ReactiveX/rxjs) | Compose asynchronous event streams; the default branch describes prerelease RxJS 9 work. Use documentation matching the released package you select. |
| [Zustand](https://github.com/pmndrs/zustand) | Small application state stores for React and other consumers; isolate server-side state per request. |
| [Jotai](https://github.com/pmndrs/jotai) | Atomic React state management; design atom lifetimes and async dependencies. |
| [Valtio](https://github.com/pmndrs/valtio) | Proxy-based JavaScript state with React integration; understand snapshots and mutation boundaries. |
| [XState](https://github.com/statelyai/xstate) | Model application behavior with state machines and actors; test transitions and persistence. |
| [Immer](https://github.com/immerjs/immer) | Produce immutable updates using mutation-style recipes; understand draft and freezing semantics. |
| [localForage](https://github.com/localForage/localForage) | Asynchronous browser storage abstraction; account for quotas, eviction and supported value types. GitHub reports its last push as 2024-07-30; maintenance responsiveness was not established. |
| [Electric](https://github.com/electric-sql/electric) | Synchronize PostgreSQL data into applications; design authorization and client write paths. |
| [Y-Sweet](https://github.com/jamsocket/y-sweet) | Host synchronization for Yjs documents; plan authentication, persistence and deployment operations. |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [AFFiNE](https://github.com/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use. License not detected by GitHub; check the repository license before use. |
| [ckeditor5](https://github.com/ckeditor/ckeditor5) | Powerful rich text editor framework with a modular architecture, modern integrations, and features like collaborative editing. License not detected by GitHub; check the repository license before use. |
| [commonmark spec](https://github.com/commonmark/commonmark-spec) | CommonMark spec, with reference implementations in C and JavaScript. License not detected by GitHub; check the repository license before use. |
| [excalidraw](https://github.com/excalidraw/excalidraw) | Virtual whiteboard for sketching hand-drawn like diagrams. |
| [foam](https://github.com/foambubble/foam) | A personal knowledge management and sharing system for VSCode. License not detected by GitHub; check the repository license before use. |
| [freeplane](https://github.com/freeplane/freeplane) | Application for Mind Mapping, Knowledge Management, Project Management. Develop, organize and communicate your ideas and knowledge in the most effective way. GPL-2.0: derivative works must stay under the GPL. |
| [GitJournal](https://github.com/GitJournal/GitJournal) | Mobile first Note Taking integrated with Git. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [hedgedoc](https://github.com/hedgedoc/hedgedoc) | HedgeDoc - Ideas grow better together. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [joplin](https://github.com/laurent22/joplin) | Joplin - the privacy-focused note taking app with sync capabilities for Windows, macOS, Linux, Android and iOS. License not detected by GitHub; check the repository license before use. |
| [jupytext](https://github.com/jupytext/jupytext) | Jupyter Notebooks as Markdown Documents, Julia, Python or R scripts. |
| [logseq](https://github.com/logseq/logseq) | A privacy-first, open-source platform for knowledge management and collaboration. Download link: http://github.com/logseq/logseq/releases. roadmap: https://logseq.io/p/NX4mc_ggEV. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [markdown it](https://github.com/markdown-it/markdown-it) | Markdown parser, done right. 100% CommonMark support, extensions, syntax plugins & high speed. |
| [marksman](https://github.com/artempyanykh/marksman) | Write Markdown with code assist and intelligence in the comfort of your favourite editor. |
| [markup](https://github.com/github/markup) | Determines which markup library to use to render a content file (e.g. README) on GitHub. |
| [mdast](https://github.com/syntax-tree/mdast) | Markdown Abstract Syntax Tree format. No license detected by GitHub; default copyright applies, so treat reuse as unsupported. |
| [MiaoYan](https://github.com/tw93/MiaoYan) | A light, native Markdown notebook for Mac, iPhone and iPad. |
| [Notepads](https://github.com/0x7c13/Notepads) | A modern, lightweight text editor with a minimalist design. |
| [overleaf](https://github.com/overleaf/overleaf) | A web-based collaborative LaTeX editor. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [penpot](https://github.com/penpot/penpot) | Penpot: The open-source design platform for Product teams that need scalable collaboration. MPL-2.0: file-level copyleft; modified files must be published. |
| [plantuml](https://github.com/plantuml/plantuml) | Generate diagrams from textual description. LGPL-3.0: dynamic linking is permitted, static linking has obligations. |
| [QOwnNotes](https://github.com/pbek/QOwnNotes) | QOwnNotes is a plain-text file notepad and todo-list manager with Markdown support and Nextcloud / ownCloud integration. GPL-2.0: derivative works must stay under the GPL. |
| [quill](https://github.com/slab/quill) | Quill is a modern WYSIWYG editor built for compatibility and extensibility. |
| [remark](https://github.com/remarkjs/remark) | markdown processor powered by plugins part of the @unifiedjs collective. |
| [roomGPT](https://github.com/Nutlope/roomGPT) | Upload a photo of your room to generate your dream room with AI. |
| [sharelatex](https://github.com/overleaf/overleaf) | A web-based collaborative LaTeX editor. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [silverbullet](https://github.com/silverbulletmd/silverbullet) | The malleable knowledge base for you and your team. Powered by Markdown and Lua. |
| [tldraw](https://github.com/tldraw/tldraw) | Build infinite canvas apps in React with the tldraw SDK. World's best, top-most agent recommended #1 five star SDK. License not detected by GitHub; check the repository license before use. |
| [vnote](https://github.com/vnotex/vnote) | A pleasant note-taking platform with native speed, majoring in Markdown, MindMap, Typst, and plain text. LGPL-3.0: dynamic linking is permitted, static linking has obligations. |
| [Zettlr](https://github.com/Zettlr/Zettlr) | Your One-Stop Publication Workbench. GPL-3.0: derivative works must stay under the GPL. |
<!-- expansion-2026-11-11:end -->
