# Documents OCR and file formats

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [Apache Tika](https://tika.apache.org/) | Extract file metadata and text; isolate untrusted parsers and verify format support. |
| [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/) | OCR engine and language data; measure accuracy on representative scans. |
| [PDFium](https://pdfium.googlesource.com/pdfium/) | PDF rendering engine; evaluate build complexity, bindings and security updates. |
| [MuPDF](https://mupdf.readthedocs.io/en/latest/) | PDF rendering and document toolkit; evaluate AGPL/commercial licensing. |
| [Apache PDFBox](https://pdfbox.apache.org/) | Java PDF creation, extraction and manipulation; test layout and font behavior. |
| [Apache POI](https://poi.apache.org/) | JVM Office file processing; validate document-feature fidelity. |
| [Open XML SDK](https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk) | Typed .NET Office document parts; does not provide Office layout rendering. |
| [ClosedXML](https://docs.closedxml.io/en/latest/) | .NET spreadsheet authoring; evaluate formula and workbook-feature support. |
| [python-docx](https://python-docx.readthedocs.io/) | Python Word document creation and editing; rendering requires another engine. |
| [pypdf](https://pypdf.readthedocs.io/en/stable/) | Python PDF structure manipulation and extraction; not a PDF renderer. |
| [Pillow](https://pillow.readthedocs.io/en/stable/) | Python raster-image processing; check codecs and decompression limits. |
| [libvips](https://www.libvips.org/) | Image-processing library for large images and pipelines; bindings require native runtime support. |

## Additions checked 2026-10-22

2026-10-22 canonical GitHub metadata, README and license identification reviewed; source documentation only. No build, runtime/architecture validation, release audit, benchmark or security audit; not adopted.

| Resource | Purpose and constraints |
|---|---|
| [Camelot PDF table extraction](https://github.com/camelot-dev/camelot) | MIT Python table-extraction library and CLI. Current source documents text-table parsers and optional ML/OCR for scans; Python >=3.10, PDFium default backend. Unarchived, repository pushed 2026-10-14. Pin a released version; benchmark accuracy, Windows wheels and optional model/dependency licenses before packaging. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Pandoc](https://github.com/jgm/pandoc) | Convert documents among markup and publishing formats; complex layouts need output inspection. |
| [qpdf](https://github.com/qpdf/qpdf) | Inspect and transform PDF structure; structural processing does not render or OCR pages. |
| [pdfcpu](https://github.com/pdfcpu/pdfcpu) | Go-based PDF inspection and manipulation; validate output against representative files. |
| [PDF.js](https://github.com/mozilla/pdf.js) | Render PDFs in web applications; keep the viewer patched and isolate untrusted documents. |
| [Mammoth.js](https://github.com/mwilliamson/mammoth.js) | Convert DOCX semantic content into HTML; sanitize output and expect layout differences. |
| [Sharp](https://github.com/lovell/sharp) | Resize and transform images in Node.js; check native binary support and codec availability. |
| [ImageMagick](https://github.com/ImageMagick/ImageMagick) | Command-line and library image transformations; configure resource limits and security policy. |
| [ExifTool](https://github.com/exiftool/exiftool) | Inspect and edit file metadata; preserve originals and confirm format-specific write support. |
| [Gotenberg](https://github.com/gotenberg/gotenberg) | Containerized document-to-PDF conversion API; sandbox inputs and plan browser resources. |
| [unified](https://github.com/unifiedjs/unified) | Compose syntax-tree processing pipelines; select parsers and sanitizers for each content format. |
| [Apache Avro](https://github.com/apache/avro) | Define and exchange schema-based data; plan reader-writer schema compatibility. |
| [MessagePack for C/C++](https://github.com/msgpack/msgpack-c) | Encode compact binary data for native applications; define schema and cross-language conventions. |
| [FlatBuffers](https://github.com/google/flatbuffers) | Generate efficient binary data access code; manage schema evolution and generated-code versions. |
| [Cap'n Proto](https://github.com/capnproto/capnproto) | Structured serialization and RPC; the fetched README identifies a breaking v2 development branch. Use the stable branch or release for production evaluation. |
| [simdjson](https://github.com/simdjson/simdjson) | Parse JSON efficiently in C++; check CPU dispatch and input lifetime requirements. |
| [Sonic](https://github.com/bytedance/sonic) | Encode and decode JSON in Go; verify architecture and Go-version support. |
| [yyjson](https://github.com/ibireme/yyjson) | Parse and write JSON in C; validate ownership and parser option choices. |
| [simdutf](https://github.com/simdutf/simdutf) | Validate and convert Unicode text efficiently; distinguish encoding validity from text normalization. |
| [fast_float](https://github.com/fastfloat/fast_float) | Parse floating-point numbers in C++; test accepted formats and edge cases. |
| [RE2](https://github.com/google/re2) | Match regular expressions with bounded resource behavior; adapt patterns that use unsupported features. |
