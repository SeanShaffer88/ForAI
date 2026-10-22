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
