# Accessibility internationalization and documentation

[All categories](README.md) · [AI selection guide](../AGENTS.md)

Historical discovery notes dated 2026-10-21. Verify suitability before adoption.

| Resource | Useful for / constraints |
|---|---|
| [WCAG](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria; combine automation with manual assessment. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rule engine used by most web accessibility testers; catches roughly the machine-checkable half of WCAG issues — manual testing still required. |
| [ICU](https://unicode-org.github.io/icu/) | Unicode, locale-sensitive formatting and collation. |
| [i18next](https://www.i18next.com/) | Application translation and locale resource management. |
| [Docusaurus](https://docusaurus.io/docs) | Documentation websites and versioned content. |
| [MkDocs](https://www.mkdocs.org/) | Markdown documentation sites with fast builds and the Material theme; a good default for project docs that live in the repo. |
| [Sphinx](https://www.sphinx-doc.org/) | Technical documentation, cross-references and API reference tooling. |
| [Mermaid](https://mermaid.js.org/) | Text-based diagrams embedded in documentation. |

## Expansion — 2026-10-23

Scoped metadata and README checks. See the [full expansion and evidence limits](../catalogs/development-expansion-2026-10-23.md); licensing notes and source identifiers are recorded there.

| Resource | Useful for / constraints |
|---|---|
| [Pa11y](https://github.com/pa11y/pa11y) | Automate web accessibility checks; supplement machine findings with manual interaction testing. |
| [Accessibility Insights for Web](https://github.com/microsoft/accessibility-insights-web) | Browser-based accessibility assessment tools; manual checks remain part of the workflow. |
| [Lighthouse](https://github.com/GoogleChrome/lighthouse) | Audit web performance and quality; control test conditions and inspect individual findings. |
| [FormatJS](https://github.com/formatjs/formatjs) | Internationalize JavaScript messages; the inspected intl package license is MIT. Confirm licenses for the exact packages and maintain locale extraction. |
| [Fluent.js](https://github.com/projectfluent/fluent.js) | JavaScript implementation of Fluent localization; review message fallback and translator workflows. |
| [Lingui](https://github.com/lingui/js-lingui) | Application message extraction and translation tooling; integrate locale loading and build steps. |
| [TypeDoc](https://github.com/TypeStrong/typedoc) | Generate API documentation from TypeScript; configure public API boundaries. |
| [VitePress](https://github.com/vuejs/vitepress) | Build documentation sites with Vite and Vue; check hosting paths and search integration. |
| [Starlight](https://github.com/withastro/starlight) | Astro documentation framework; customize navigation and verify accessibility after changes. |
| [Vale](https://github.com/vale-cli/vale) | Lint prose against configurable style rules; curate rules to avoid noisy feedback. |

## Expansion — 2026-10-27

A further 500-resource development discovery pass. Entries below were selected from curated project indexes and checked against GitHub repository API metadata only; see the [expansion notes and evidence limits](../catalogs/development-expansion-2026-10-27.md).

| Resource | Useful for / constraints |
|---|---|
| [scramble](https://github.com/dedoc/scramble) | Modern Laravel OpenAPI (Swagger) documentation generator. No PHPDoc annotations required. |
| [SwiftUICharts](https://github.com/willdale/SwiftUICharts) | A charts / plotting library for SwiftUI. Works on macOS, iOS, watchOS, and tvOS and has accessibility features built in. |
| [redoc](https://github.com/Redocly/redoc) | 📘 OpenAPI/Swagger-generated API Reference Documentation |

<!-- expansion-2026-11-11:begin -->
## Expansion — 2026-11-11

Repository metadata and primary documentation pages checked, not read end to end: latest release, license, and current maintenance are yours to verify before adopting. See the [expansion notes and evidence limits](../catalogs/expansion-2026-11-11.md).

| Resource | Useful for / constraints |
|---|---|
| [a11y.css](https://github.com/ffoodd/a11y.css) | This CSS file intends to warn developers about possible risks and mistakes that exist in HTML code. It can also be used to roughly evaluate a site's quality by simply including it as an external stylesheet. |
| [a11yproject.com](https://github.com/a11yproject/a11yproject.com) | The A11Y Project is a community-driven effort to make digital accessibility easier. |
| [aria practices](https://github.com/w3c/aria-practices) | WAI-ARIA Authoring Practices Guide (APG). License not detected by GitHub; check the repository license before use. |
| [babel](https://github.com/python-babel/babel) | The official repository for Babel, the Python Internationalization Library. |
| [content](https://github.com/mdn/content) | The official source for MDN Web Docs content. Home to over 14,000 pages of documentation about HTML, CSS, JS, HTTP, Web APIs, and more. License not detected by GitHub; check the repository license before use. |
| [docsify](https://github.com/docsifyjs/docsify) | A magical documentation site generator. |
| [ever traduora](https://github.com/ever-co/ever-traduora) | Ever® Traduora™ - Open Translation Management Platform - https://traduora.co. AGPL-3.0: network use can trigger source-disclosure obligations. |
| [fluent](https://github.com/projectfluent/fluent) | Fluent — planning, spec and documentation. |
| [fluent rs](https://github.com/projectfluent/fluent-rs) | Rust implementation of Project Fluent. |
| [globalize](https://github.com/globalizejs/globalize) | A JavaScript library for internationalization and localization that leverages the official Unicode CLDR JSON data. |
| [go i18n](https://github.com/nicksnyder/go-i18n) | Translate your Go program into multiple languages. |
| [gt](https://github.com/generaltranslation/gt) | Full-stack localization for every framework. |
| [hugo](https://github.com/gohugoio/hugo) | The world’s fastest framework for building websites. |
| [intl](https://github.com/symfony/intl) | Provides access to the localization data of the ICU library. |
| [jupyter book](https://github.com/jupyter-book/jupyter-book) | Create beautiful, publication-quality books and documents from computational content. |
| [just the docs](https://github.com/just-the-docs/just-the-docs) | A modern, high customizable, responsive Jekyll theme for documentation with built-in search. |
| [lyricist](https://github.com/adrielcafe/lyricist) | The missing I18N/L10N (internationalization/localization) multiplatform library for Compose Multiplatform! |
| [mkdocs material](https://github.com/squidfunk/mkdocs-material) | Documentation that simply works. |
| [mystmd](https://github.com/jupyter-book/mystmd) | Command line tools for working with MyST Markdown. |
| [readthedocs.org](https://github.com/readthedocs/readthedocs.org) | The source code that powers readthedocs.org. |
| [svelte i18n](https://github.com/kaisermann/svelte-i18n) | Internationalization library for Svelte. |
| [transloco](https://github.com/jsverse/transloco) | The internationalization (i18n) library for Angular. |
| [www](https://github.com/writethedocs/www) | The main website for Write the Docs. License not detected by GitHub; check the repository license before use. |
<!-- expansion-2026-11-11:end -->
