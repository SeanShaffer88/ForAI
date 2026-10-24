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
