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
