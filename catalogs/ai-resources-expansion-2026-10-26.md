# AI resources expansion — 2026-10-26 (1000 resources)

This expansion adds **1000 resources useful to AI models**, including **https://www.skills.sh/** and all sites listed on it at time of compilation (2026-10-26). It was requested to bring the catalog to 2192 entries, covering the skills ecosystem, model providers, local inference, agent frameworks, MCP servers, coding agents, retrieval, evaluation, speech/realtime, prompt engineering, data/annotation, learning references, memory/context, and protocols/interoperability.

## Evidence and limits

Entries are primary-source pointers (official docs, official registries, or the project's own repository) compiled 2026-10-26. Inclusion is discovery, not an adoption audit: maintenance, licensing, compatibility, pricing, and security were not individually re-verified beyond a link-format check in this pass. Every entry received a format validation (https scheme and category-file cross-reference) on 2026-10-26. Verify at the primary source before relying on any entry — framework APIs, model names, and prices change frequently. Skills.sh subpages were fetched via the platform's markdown proxy on 2026-10-26 for the trending/hot leaderboards and representative topic/agent pages; GitHub repo URLs are canonical https://github.com/<owner>/<repo>.

Scope: 1000 entries added across 14 categories (1 new: AI agent skills and ecosystem). All URLs are distinct from the prior 1192 catalog entries and from each other.

## AI agent skills and ecosystem (300) — includes skills.sh directory

The open agent skills ecosystem. Install any skill via `npx skills add https://github.com/<owner>/<repo> --skill <skill>` after reading its skill card.

| Resource | Useful for / constraints |
|---|---|
| [skills.sh — Agent Skills Directory](https://www.skills.sh/) | The open agent skills ecosystem homepage: discover, install, and publish reusable agent skills via npx skills — covers all categories listed on the site. |
| [Skills CLI — vercel-labs/skills](https://github.com/vercel-labs/skills) | The Skills CLI package manager (npx skills) for discovering and installing agent skills from GitHub and other sources; powers find-skills. |
| [Skills CLI — find-skills skill](https://www.skills.sh/vercel-labs/skills/find-skills) | Meta skill to discover and install other skills from skills.sh inside an agent session; searches by domain and task. |
| [Agent Browser skill](https://www.skills.sh/vercel-labs/agent-browser/agent-browser) | Full browser automation skill: navigate, click, fill forms, extract data, screenshot — CLI-driven, reliable for structured tasks. |
| [Skill Creator (Anthropic)](https://www.skills.sh/anthropics/skills/skill-creator) | Skill for creating, testing, and publishing new skills from within your agent session. |
| [Vercel Agent Skills — overview](https://github.com/vercel-labs/agent-skills) | Vercel's collection of agent skills: web design guidelines, React best practices, composition patterns, and more. |
| [AnthropicSkills repo](https://github.com/anthropics/skills) | Anthropic's official skills collection: frontend-design, canvas-design, pdf, docx, mcp-builder, and brand guidelines. |
| [skills.sh agent — Claude Code](https://www.skills.sh/agent/claude-code) | Agent compatibility page for Claude Code: which skills work with Claude Code and how to install via npx skills. |
| [skills.sh agent — Cursor](https://www.skills.sh/agent/cursor) | Agent compatibility page for Cursor: which skills work with Cursor and how to install via npx skills. |
| [skills.sh agent — Codex](https://www.skills.sh/agent/codex) | Agent compatibility page for Codex: which skills work with Codex and how to install via npx skills. |
| [skills.sh agent — GitHub Copilot](https://www.skills.sh/agent/copilot) | Agent compatibility page for GitHub Copilot: which skills work with GitHub Copilot and how to install via npx skills. |
| [skills.sh agent — Windsurf](https://www.skills.sh/agent/windsurf) | Agent compatibility page for Windsurf: which skills work with Windsurf and how to install via npx skills. |
| [skills.sh agent — Gemini CLI](https://www.skills.sh/agent/gemini) | Agent compatibility page for Gemini CLI: which skills work with Gemini CLI and how to install via npx skills. |
| [skills.sh agent — Cline](https://www.skills.sh/agent/cline) | Agent compatibility page for Cline: which skills work with Cline and how to install via npx skills. |
| [skills.sh agent — AMP](https://www.skills.sh/agent/amp) | Agent compatibility page for AMP: which skills work with AMP and how to install via npx skills. |
| [skills.sh agent — Antigravity](https://www.skills.sh/agent/antigravity) | Agent compatibility page for Antigravity: which skills work with Antigravity and how to install via npx skills. |
| [skills.sh agent — OpenClaw](https://www.skills.sh/agent/openclaw) | Agent compatibility page for OpenClaw: which skills work with OpenClaw and how to install via npx skills. |
| [skills.sh agent — Droid](https://www.skills.sh/agent/droid) | Agent compatibility page for Droid: which skills work with Droid and how to install via npx skills. |
| [skills.sh agent — Goose](https://www.skills.sh/agent/goose) | Agent compatibility page for Goose: which skills work with Goose and how to install via npx skills. |
| [skills.sh agent — Kilo](https://www.skills.sh/agent/kilo) | Agent compatibility page for Kilo: which skills work with Kilo and how to install via npx skills. |
| [skills.sh agent — Kiro CLI](https://www.skills.sh/agent/kiro-cli) | Agent compatibility page for Kiro CLI: which skills work with Kiro CLI and how to install via npx skills. |
| [skills.sh agent — Nous Research](https://www.skills.sh/agent/nous-research) | Agent compatibility page for Nous Research: which skills work with Nous Research and how to install via npx skills. |
| [skills.sh agent — OpenCode](https://www.skills.sh/agent/opencode) | Agent compatibility page for OpenCode: which skills work with OpenCode and how to install via npx skills. |
| [skills.sh agent — Roo Code](https://www.skills.sh/agent/roo) | Agent compatibility page for Roo Code: which skills work with Roo Code and how to install via npx skills. |
| [skills.sh agent — Trae](https://www.skills.sh/agent/trae) | Agent compatibility page for Trae: which skills work with Trae and how to install via npx skills. |
| [skills.sh agent — VS Code](https://www.skills.sh/agent/vscode) | Agent compatibility page for VS Code: which skills work with VS Code and how to install via npx skills. |
| [skills.sh agent — Zed](https://www.skills.sh/agent/zed) | Agent compatibility page for Zed: which skills work with Zed and how to install via npx skills. |
| [skills.sh topic — agent-workflows](https://www.skills.sh/topic/agent-workflows) | Curated collection of skills for agent-workflows: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — design](https://www.skills.sh/topic/design) | Curated collection of skills for design: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — testing](https://www.skills.sh/topic/testing) | Curated collection of skills for testing: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — react](https://www.skills.sh/topic/react) | Curated collection of skills for react: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — marketing](https://www.skills.sh/topic/marketing) | Curated collection of skills for marketing: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — data](https://www.skills.sh/topic/data) | Curated collection of skills for data: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — browser-automation](https://www.skills.sh/topic/browser-automation) | Curated collection of skills for browser-automation: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — productivity](https://www.skills.sh/topic/productivity) | Curated collection of skills for productivity: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — development](https://www.skills.sh/topic/development) | Curated collection of skills for development: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — ai-media](https://www.skills.sh/topic/ai-media) | Curated collection of skills for ai-media: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — security](https://www.skills.sh/topic/security) | Curated collection of skills for security: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — cloud](https://www.skills.sh/topic/cloud) | Curated collection of skills for cloud: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — sales](https://www.skills.sh/topic/sales) | Curated collection of skills for sales: what agents can do with those skills installed, and related skill recommendations. |
| [skills.sh topic — revops](https://www.skills.sh/topic/revops) | Curated collection of skills for revops: what agents can do with those skills installed, and related skill recommendations. |
| [grill-me — mattpocock/skills](https://www.skills.sh/mattpocock/skills/grill-me) | Agent skill 'grill-me' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill grill-me` to extend agent capabilities. |
| [hyperframes-cli — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/hyperframes-cli) | Agent skill 'hyperframes-cli' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes-cli` to extend agent capabilities. |
| [grill-with-docs — mattpocock/skills](https://www.skills.sh/mattpocock/skills/grill-with-docs) | Agent skill 'grill-with-docs' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill grill-with-docs` to extend agent capabilities. |
| [hyperframes — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/hyperframes) | Agent skill 'hyperframes' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes` to extend agent capabilities. |
| [improve-codebase-architecture — mattpocock/skills](https://www.skills.sh/mattpocock/skills/improve-codebase-architecture) | Agent skill 'improve-codebase-architecture' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill improve-codebase-architecture` to extend agent capabilities. |
| [tdd — mattpocock/skills](https://www.skills.sh/mattpocock/skills/tdd) | Agent skill 'tdd' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill tdd` to extend agent capabilities. |
| [media-use — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/media-use) | Agent skill 'media-use' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill media-use` to extend agent capabilities. |
| [reddit-automation — flowkit-labs/skills](https://www.skills.sh/flowkit-labs/skills/reddit-automation) | Agent skill 'reddit-automation' from flowkit-labs/skills: install via `npx skills add https://github.com/flowkit-labs/skills --skill reddit-automation` to extend agent capabilities. |
| [setup-matt-pocock-skills — mattpocock/skills](https://www.skills.sh/mattpocock/skills/setup-matt-pocock-skills) | Agent skill 'setup-matt-pocock-skills' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill setup-matt-pocock-skills` to extend agent capabilities. |
| [handoff — mattpocock/skills](https://www.skills.sh/mattpocock/skills/handoff) | Agent skill 'handoff' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill handoff` to extend agent capabilities. |
| [design-mobile-apps — designed-by-ai/skills](https://www.skills.sh/designed-by-ai/skills/design-mobile-apps) | Agent skill 'design-mobile-apps' from designed-by-ai/skills: install via `npx skills add https://github.com/designed-by-ai/skills --skill design-mobile-apps` to extend agent capabilities. |
| [frontend-design — anthropics/skills](https://www.skills.sh/anthropics/skills/frontend-design) | Agent skill 'frontend-design' from anthropics/skills: install via `npx skills add https://github.com/anthropics/skills --skill frontend-design` to extend agent capabilities. |
| [hyperframes-registry — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/hyperframes-registry) | Agent skill 'hyperframes-registry' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes-registry` to extend agent capabilities. |
| [hyperframes-animation — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/hyperframes-animation) | Agent skill 'hyperframes-animation' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes-animation` to extend agent capabilities. |
| [hyperframes-core — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/hyperframes-core) | Agent skill 'hyperframes-core' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes-core` to extend agent capabilities. |
| [hyperframes-creative — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/hyperframes-creative) | Agent skill 'hyperframes-creative' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes-creative` to extend agent capabilities. |
| [triage — mattpocock/skills](https://www.skills.sh/mattpocock/skills/triage) | Agent skill 'triage' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill triage` to extend agent capabilities. |
| [prototype — mattpocock/skills](https://www.skills.sh/mattpocock/skills/prototype) | Agent skill 'prototype' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill prototype` to extend agent capabilities. |
| [grilling — mattpocock/skills](https://www.skills.sh/mattpocock/skills/grilling) | Agent skill 'grilling' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill grilling` to extend agent capabilities. |
| [ui-taste — uizze/uizze](https://www.skills.sh/uizze/uizze/ui-taste) | Agent skill 'ui-taste' from uizze/uizze: install via `npx skills add https://github.com/uizze/uizze --skill ui-taste` to extend agent capabilities. |
| [uizze-ui — uizze/uizze](https://www.skills.sh/uizze/uizze/uizze-ui) | Agent skill 'uizze-ui' from uizze/uizze: install via `npx skills add https://github.com/uizze/uizze --skill uizze-ui` to extend agent capabilities. |
| [image-to-ui — uizze/uizze](https://www.skills.sh/uizze/uizze/image-to-ui) | Agent skill 'image-to-ui' from uizze/uizze: install via `npx skills add https://github.com/uizze/uizze --skill image-to-ui` to extend agent capabilities. |
| [web-design-guidelines — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines) | Agent skill 'web-design-guidelines' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines` to extend agent capabilities. |
| [vercel-composition-patterns — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/vercel-composition-patterns) | Agent skill 'vercel-composition-patterns' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-composition-patterns` to extend agent capabilities. |
| [ui-ux-pro-max — nextlevelbuilder/ui-ux-pro-max-skill](https://www.skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) | Agent skill 'ui-ux-pro-max' from nextlevelbuilder/ui-ux-pro-max-skill: install via `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max` to extend agent capabilities. |
| [sleek-design-mobile-apps — sleekdotdesign/agent-skills](https://www.skills.sh/sleekdotdesign/agent-skills/sleek-design-mobile-apps) | Agent skill 'sleek-design-mobile-apps' from sleekdotdesign/agent-skills: install via `npx skills add https://github.com/sleekdotdesign/agent-skills --skill sleek-design-mobile-apps` to extend agent capabilities. |
| [canvas-design — anthropics/skills](https://www.skills.sh/anthropics/skills/canvas-design) | Agent skill 'canvas-design' from anthropics/skills: install via `npx skills add https://github.com/anthropics/skills --skill canvas-design` to extend agent capabilities. |
| [brainstorming — obra/superpowers](https://www.skills.sh/obra/superpowers/brainstorming) | Agent skill 'brainstorming' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill brainstorming` to extend agent capabilities. |
| [browser-use — browser-use/browser-use](https://www.skills.sh/browser-use/browser-use/browser-use) | Agent skill 'browser-use' from browser-use/browser-use: install via `npx skills add https://github.com/browser-use/browser-use --skill browser-use` to extend agent capabilities. |
| [systematic-debugging — obra/superpowers](https://www.skills.sh/obra/superpowers/systematic-debugging) | Agent skill 'systematic-debugging' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill systematic-debugging` to extend agent capabilities. |
| [writing-plans — obra/superpowers](https://www.skills.sh/obra/superpowers/writing-plans) | Agent skill 'writing-plans' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill writing-plans` to extend agent capabilities. |
| [executing-plans — obra/superpowers](https://www.skills.sh/obra/superpowers/executing-plans) | Agent skill 'executing-plans' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill executing-plans` to extend agent capabilities. |
| [test-driven-development — obra/superpowers](https://www.skills.sh/obra/superpowers/test-driven-development) | Agent skill 'test-driven-development' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill test-driven-development` to extend agent capabilities. |
| [requesting-code-review — obra/superpowers](https://www.skills.sh/obra/superpowers/requesting-code-review) | Agent skill 'requesting-code-review' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill requesting-code-review` to extend agent capabilities. |
| [subagent-driven-development — obra/superpowers](https://www.skills.sh/obra/superpowers/subagent-driven-development) | Agent skill 'subagent-driven-development' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill subagent-driven-development` to extend agent capabilities. |
| [verification-before-completion — obra/superpowers](https://www.skills.sh/obra/superpowers/verification-before-completion) | Agent skill 'verification-before-completion' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill verification-before-completion` to extend agent capabilities. |
| [dispatching-parallel-agents — obra/superpowers](https://www.skills.sh/obra/superpowers/dispatching-parallel-agents) | Agent skill 'dispatching-parallel-agents' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill dispatching-parallel-agents` to extend agent capabilities. |
| [using-git-worktrees — obra/superpowers](https://www.skills.sh/obra/superpowers/using-git-worktrees) | Agent skill 'using-git-worktrees' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill using-git-worktrees` to extend agent capabilities. |
| [finishing-a-development-branch — obra/superpowers](https://www.skills.sh/obra/superpowers/finishing-a-development-branch) | Agent skill 'finishing-a-development-branch' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill finishing-a-development-branch` to extend agent capabilities. |
| [ralph-tui-prd — subsy/ralph-tui](https://www.skills.sh/subsy/ralph-tui/ralph-tui-prd) | Agent skill 'ralph-tui-prd' from subsy/ralph-tui: install via `npx skills add https://github.com/subsy/ralph-tui --skill ralph-tui-prd` to extend agent capabilities. |
| [ralph-tui-create-beads — subsy/ralph-tui](https://www.skills.sh/subsy/ralph-tui/ralph-tui-create-beads) | Agent skill 'ralph-tui-create-beads' from subsy/ralph-tui: install via `npx skills add https://github.com/subsy/ralph-tui --skill ralph-tui-create-beads` to extend agent capabilities. |
| [ralph-tui-create-json — subsy/ralph-tui](https://www.skills.sh/subsy/ralph-tui/ralph-tui-create-json) | Agent skill 'ralph-tui-create-json' from subsy/ralph-tui: install via `npx skills add https://github.com/subsy/ralph-tui --skill ralph-tui-create-json` to extend agent capabilities. |
| [ralph-wiggum — fstandhartinger/ralph-wiggum](https://www.skills.sh/fstandhartinger/ralph-wiggum/ralph-wiggum) | Agent skill 'ralph-wiggum' from fstandhartinger/ralph-wiggum: install via `npx skills add https://github.com/fstandhartinger/ralph-wiggum --skill ralph-wiggum` to extend agent capabilities. |
| [ralph-loop — andrelandgraf/fullstackrecipes](https://www.skills.sh/andrelandgraf/fullstackrecipes/ralph-loop) | Agent skill 'ralph-loop' from andrelandgraf/fullstackrecipes: install via `npx skills add https://github.com/andrelandgraf/fullstackrecipes --skill ralph-loop` to extend agent capabilities. |
| [ai-image-generation — skills-shell/superpowers](https://www.skills.sh/skills-shell/superpowers/ai-image-generation) | Agent skill 'ai-image-generation' from skills-shell/superpowers: install via `npx skills add https://github.com/skills-shell/superpowers --skill ai-image-generation` to extend agent capabilities. |
| [ai-video-generation — gencraft-labs/skills](https://www.skills.sh/gencraft-labs/skills/ai-video-generation) | Agent skill 'ai-video-generation' from gencraft-labs/skills: install via `npx skills add https://github.com/gencraft-labs/skills --skill ai-video-generation` to extend agent capabilities. |
| [ai-image-generation — gencraft-labs/skills](https://www.skills.sh/gencraft-labs/skills/ai-image-generation) | Agent skill 'ai-image-generation' from gencraft-labs/skills: install via `npx skills add https://github.com/gencraft-labs/skills --skill ai-image-generation` to extend agent capabilities. |
| [video-edit — gencraft-labs/skills](https://www.skills.sh/gencraft-labs/skills/video-edit) | Agent skill 'video-edit' from gencraft-labs/skills: install via `npx skills add https://github.com/gencraft-labs/skills --skill video-edit` to extend agent capabilities. |
| [image-to-video — gencraft-labs/skills](https://www.skills.sh/gencraft-labs/skills/image-to-video) | Agent skill 'image-to-video' from gencraft-labs/skills: install via `npx skills add https://github.com/gencraft-labs/skills --skill image-to-video` to extend agent capabilities. |
| [ai-music — gencraft-labs/skills](https://www.skills.sh/gencraft-labs/skills/ai-music) | Agent skill 'ai-music' from gencraft-labs/skills: install via `npx skills add https://github.com/gencraft-labs/skills --skill ai-music` to extend agent capabilities. |
| [ai-video-generation — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/ai-video-generation) | Agent skill 'ai-video-generation' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill ai-video-generation` to extend agent capabilities. |
| [ai-image-generation — magentosh/superpowers](https://www.skills.sh/magentosh/superpowers/ai-image-generation) | Agent skill 'ai-image-generation' from magentosh/superpowers: install via `npx skills add https://github.com/magentosh/superpowers --skill ai-image-generation` to extend agent capabilities. |
| [ai-video-generation — its-a-skill-issue/superpowers](https://www.skills.sh/its-a-skill-issue/superpowers/ai-video-generation) | Agent skill 'ai-video-generation' from its-a-skill-issue/superpowers: install via `npx skills add https://github.com/its-a-skill-issue/superpowers --skill ai-video-generation` to extend agent capabilities. |
| [ai-avatar-video — qu-skills/superpowers](https://www.skills.sh/qu-skills/superpowers/ai-avatar-video) | Agent skill 'ai-avatar-video' from qu-skills/superpowers: install via `npx skills add https://github.com/qu-skills/superpowers --skill ai-avatar-video` to extend agent capabilities. |
| [ai-video-generation — bankai-skills/superpowers](https://www.skills.sh/bankai-skills/superpowers/ai-video-generation) | Agent skill 'ai-video-generation' from bankai-skills/superpowers: install via `npx skills add https://github.com/bankai-skills/superpowers --skill ai-video-generation` to extend agent capabilities. |
| [ui-taste — uizze.sh](https://www.skills.sh/site/uizze.sh/ui-taste) | Agent skill 'ui-taste' from site/uizze.sh: install via `npx skills add https://github.com/site/uizze.sh --skill ui-taste` to extend agent capabilities. |
| [remotion-best-practices — remotion-dev/skills](https://www.skills.sh/remotion-dev/skills/remotion-best-practices) | Agent skill 'remotion-best-practices' from remotion-dev/skills: install via `npx skills add https://github.com/remotion-dev/skills --skill remotion-best-practices` to extend agent capabilities. |
| [design-taste-frontend — leonxlnx/taste-skill](https://www.skills.sh/leonxlnx/taste-skill/design-taste-frontend) | Agent skill 'design-taste-frontend' from leonxlnx/taste-skill: install via `npx skills add https://github.com/leonxlnx/taste-skill --skill design-taste-frontend` to extend agent capabilities. |
| [remotion-render — remotion-dev/skills](https://www.skills.sh/remotion-dev/skills/remotion-render) | Agent skill 'remotion-render' from remotion-dev/skills: install via `npx skills add https://github.com/remotion-dev/skills --skill remotion-render` to extend agent capabilities. |
| [remotion-to-hyperframes — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/remotion-to-hyperframes) | Agent skill 'remotion-to-hyperframes' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill remotion-to-hyperframes` to extend agent capabilities. |
| [remotion-docs — remotion-dev/skills](https://www.skills.sh/remotion-dev/skills/remotion-docs) | Agent skill 'remotion-docs' from remotion-dev/skills: install via `npx skills add https://github.com/remotion-dev/skills --skill remotion-docs` to extend agent capabilities. |
| [remotion-multimedia — remotion-dev/skills](https://www.skills.sh/remotion-dev/skills/remotion-multimedia) | Agent skill 'remotion-multimedia' from remotion-dev/skills: install via `npx skills add https://github.com/remotion-dev/skills --skill remotion-multimedia` to extend agent capabilities. |
| [remotion-upgrade — remotion-dev/skills](https://www.skills.sh/remotion-dev/skills/remotion-upgrade) | Agent skill 'remotion-upgrade' from remotion-dev/skills: install via `npx skills add https://github.com/remotion-dev/skills --skill remotion-upgrade` to extend agent capabilities. |
| [domain-modeling — mattpocock/skills](https://www.skills.sh/mattpocock/skills/domain-modeling) | Agent skill 'domain-modeling' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill domain-modeling` to extend agent capabilities. |
| [slideshow — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/slideshow) | Agent skill 'slideshow' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill slideshow` to extend agent capabilities. |
| [to-tickets — mattpocock/skills](https://www.skills.sh/mattpocock/skills/to-tickets) | Agent skill 'to-tickets' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill to-tickets` to extend agent capabilities. |
| [figma — heygen-com/hyperframes](https://www.skills.sh/heygen-com/hyperframes/figma) | Agent skill 'figma' from heygen-com/hyperframes: install via `npx skills add https://github.com/heygen-com/hyperframes --skill figma` to extend agent capabilities. |
| [ask-matt — mattpocock/skills](https://www.skills.sh/mattpocock/skills/ask-matt) | Agent skill 'ask-matt' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill ask-matt` to extend agent capabilities. |
| [lark-doc — open.feishu.cn](https://www.skills.sh/site/open.feishu.cn/lark-doc) | Agent skill 'lark-doc' from site/open.feishu.cn: install via `npx skills add https://github.com/site/open.feishu.cn --skill lark-doc` to extend agent capabilities. |
| [lark-whiteboard — open.feishu.cn](https://www.skills.sh/site/open.feishu.cn/lark-whiteboard) | Agent skill 'lark-whiteboard' from site/open.feishu.cn: install via `npx skills add https://github.com/site/open.feishu.cn --skill lark-whiteboard` to extend agent capabilities. |
| [retro — mattpocock/skills](https://www.skills.sh/mattpocock/skills/retro) | Agent skill 'retro' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill retro` to extend agent capabilities. |
| [lark-event — open.feishu.cn](https://www.skills.sh/site/open.feishu.cn/lark-event) | Agent skill 'lark-event' from site/open.feishu.cn: install via `npx skills add https://github.com/site/open.feishu.cn --skill lark-event` to extend agent capabilities. |
| [wait-what — mattpocock/skills](https://www.skills.sh/mattpocock/skills/wait-what) | Agent skill 'wait-what' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill wait-what` to extend agent capabilities. |
| [lark-vc-agent — open.feishu.cn](https://www.skills.sh/site/open.feishu.cn/lark-vc-agent) | Agent skill 'lark-vc-agent' from site/open.feishu.cn: install via `npx skills add https://github.com/site/open.feishu.cn --skill lark-vc-agent` to extend agent capabilities. |
| [wizard — mattpocock/skills](https://www.skills.sh/mattpocock/skills/wizard) | Agent skill 'wizard' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill wizard` to extend agent capabilities. |
| [agent-browser — skills-shell/superpowers](https://www.skills.sh/skills-shell/superpowers/agent-browser) | Agent skill 'agent-browser' from skills-shell/superpowers: install via `npx skills add https://github.com/skills-shell/superpowers --skill agent-browser` to extend agent capabilities. |
| [claude-handoff — mattpocock/skills](https://www.skills.sh/mattpocock/skills/claude-handoff) | Agent skill 'claude-handoff' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill claude-handoff` to extend agent capabilities. |
| [chief-of-staff — mattpocock/skills](https://www.skills.sh/mattpocock/skills/chief-of-staff) | Agent skill 'chief-of-staff' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill chief-of-staff` to extend agent capabilities. |
| [vercel-react-best-practices — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) | Agent skill 'vercel-react-best-practices' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices` to extend agent capabilities. |
| [git-guardrails-claude-code — mattpocock/skills](https://www.skills.sh/mattpocock/skills/git-guardrails-claude-code) | Agent skill 'git-guardrails-claude-code' from mattpocock/skills: install via `npx skills add https://github.com/mattpocock/skills --skill git-guardrails-claude-code` to extend agent capabilities. |
| [neon-postgres — neondatabase/agent-skills](https://www.skills.sh/neondatabase/agent-skills/neon-postgres) | Agent skill 'neon-postgres' from neondatabase/agent-skills: install via `npx skills add https://github.com/neondatabase/agent-skills --skill neon-postgres` to extend agent capabilities. |
| [neon — neondatabase/agent-skills](https://www.skills.sh/neondatabase/agent-skills/neon) | Agent skill 'neon' from neondatabase/agent-skills: install via `npx skills add https://github.com/neondatabase/agent-skills --skill neon` to extend agent capabilities. |
| [security-audit — cloudflare/security-audit-skill](https://www.skills.sh/cloudflare/security-audit-skill/security-audit) | Agent skill 'security-audit' from cloudflare/security-audit-skill: install via `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` to extend agent capabilities. |
| [emil-design-eng — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/emil-design-eng) | Agent skill 'emil-design-eng' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill emil-design-eng` to extend agent capabilities. |
| [apple-design — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/apple-design) | Agent skill 'apple-design' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill apple-design` to extend agent capabilities. |
| [archify — tt-a1i/archify](https://www.skills.sh/tt-a1i/archify/archify) | Agent skill 'archify' from tt-a1i/archify: install via `npx skills add https://github.com/tt-a1i/archify --skill archify` to extend agent capabilities. |
| [review-animations — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/review-animations) | Agent skill 'review-animations' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill review-animations` to extend agent capabilities. |
| [infsh-cli — skills-shell/superpowers](https://www.skills.sh/skills-shell/superpowers/infsh-cli) | Agent skill 'infsh-cli' from skills-shell/superpowers: install via `npx skills add https://github.com/skills-shell/superpowers --skill infsh-cli` to extend agent capabilities. |
| [impeccable — pbakaus/impeccable](https://www.skills.sh/pbakaus/impeccable/impeccable) | Agent skill 'impeccable' from pbakaus/impeccable: install via `npx skills add https://github.com/pbakaus/impeccable --skill impeccable` to extend agent capabilities. |
| [animate — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/animate) | Agent skill 'animate' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill animate` to extend agent capabilities. |
| [mobile-native — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/mobile-native) | Agent skill 'mobile-native' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill mobile-native` to extend agent capabilities. |
| [pick-ui-library — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/pick-ui-library) | Agent skill 'pick-ui-library' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill pick-ui-library` to extend agent capabilities. |
| [prototype — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/prototype) | Agent skill 'prototype' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill prototype` to extend agent capabilities. |
| [wind-mcp-skill — wind-alice/alicemarket](https://www.skills.sh/wind-alice/alicemarket/wind-mcp-skill) | Agent skill 'wind-mcp-skill' from wind-alice/alicemarket: install via `npx skills add https://github.com/wind-alice/alicemarket --skill wind-mcp-skill` to extend agent capabilities. |
| [animate-expo — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/animate-expo) | Agent skill 'animate-expo' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill animate-expo` to extend agent capabilities. |
| [ask-sonner — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/ask-sonner) | Agent skill 'ask-sonner' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill ask-sonner` to extend agent capabilities. |
| [prisma-client-api — prisma/skills](https://www.skills.sh/prisma/skills/prisma-client-api) | Agent skill 'prisma-client-api' from prisma/skills: install via `npx skills add https://github.com/prisma/skills --skill prisma-client-api` to extend agent capabilities. |
| [ios-design — uizze.sh](https://www.skills.sh/site/uizze.sh/ios-design) | Agent skill 'ios-design' from site/uizze.sh: install via `npx skills add https://github.com/site/uizze.sh --skill ios-design` to extend agent capabilities. |
| [prisma-cli — prisma/skills](https://www.skills.sh/prisma/skills/prisma-cli) | Agent skill 'prisma-cli' from prisma/skills: install via `npx skills add https://github.com/prisma/skills --skill prisma-cli` to extend agent capabilities. |
| [prisma-orm-setup — prisma/skills](https://www.skills.sh/prisma/skills/prisma-orm-setup) | Agent skill 'prisma-orm-setup' from prisma/skills: install via `npx skills add https://github.com/prisma/skills --skill prisma-orm-setup` to extend agent capabilities. |
| [write-swift — emilkowalski/skills](https://www.skills.sh/emilkowalski/skills/write-swift) | Agent skill 'write-swift' from emilkowalski/skills: install via `npx skills add https://github.com/emilkowalski/skills --skill write-swift` to extend agent capabilities. |
| [prisma-postgres-setup — prisma/skills](https://www.skills.sh/prisma/skills/prisma-postgres-setup) | Agent skill 'prisma-postgres-setup' from prisma/skills: install via `npx skills add https://github.com/prisma/skills --skill prisma-postgres-setup` to extend agent capabilities. |
| [prisma-database-setup — prisma/skills](https://www.skills.sh/prisma/skills/prisma-database-setup) | Agent skill 'prisma-database-setup' from prisma/skills: install via `npx skills add https://github.com/prisma/skills --skill prisma-database-setup` to extend agent capabilities. |
| [hallmark — nutlope/hallmark](https://www.skills.sh/nutlope/hallmark/hallmark) | Agent skill 'hallmark' from nutlope/hallmark: install via `npx skills add https://github.com/nutlope/hallmark --skill hallmark` to extend agent capabilities. |
| [prisma-postgres — prisma/skills](https://www.skills.sh/prisma/skills/prisma-postgres) | Agent skill 'prisma-postgres' from prisma/skills: install via `npx skills add https://github.com/prisma/skills --skill prisma-postgres` to extend agent capabilities. |
| [agent-browser — its-a-skill-issue/superpowers](https://www.skills.sh/its-a-skill-issue/superpowers/agent-browser) | Agent skill 'agent-browser' from its-a-skill-issue/superpowers: install via `npx skills add https://github.com/its-a-skill-issue/superpowers --skill agent-browser` to extend agent capabilities. |
| [agent-browser — magentosh/superpowers](https://www.skills.sh/magentosh/superpowers/agent-browser) | Agent skill 'agent-browser' from magentosh/superpowers: install via `npx skills add https://github.com/magentosh/superpowers --skill agent-browser` to extend agent capabilities. |
| [agent-browser — bankai-skills/superpowers](https://www.skills.sh/bankai-skills/superpowers/agent-browser) | Agent skill 'agent-browser' from bankai-skills/superpowers: install via `npx skills add https://github.com/bankai-skills/superpowers --skill agent-browser` to extend agent capabilities. |
| [google-agents-cli-adk-code — google/agents-cli](https://www.skills.sh/google/agents-cli/google-agents-cli-adk-code) | Agent skill 'google-agents-cli-adk-code' from google/agents-cli: install via `npx skills add https://github.com/google/agents-cli --skill google-agents-cli-adk-code` to extend agent capabilities. |
| [google-agents-cli-publish — google/agents-cli](https://www.skills.sh/google/agents-cli/google-agents-cli-publish) | Agent skill 'google-agents-cli-publish' from google/agents-cli: install via `npx skills add https://github.com/google/agents-cli --skill google-agents-cli-publish` to extend agent capabilities. |
| [google-agents-cli-deploy — google/agents-cli](https://www.skills.sh/google/agents-cli/google-agents-cli-deploy) | Agent skill 'google-agents-cli-deploy' from google/agents-cli: install via `npx skills add https://github.com/google/agents-cli --skill google-agents-cli-deploy` to extend agent capabilities. |
| [agent-browser — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/agent-browser) | Agent skill 'agent-browser' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill agent-browser` to extend agent capabilities. |
| [caveman — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman) | Agent skill 'caveman' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman` to extend agent capabilities. |
| [google-agents-cli-eval — google/agents-cli](https://www.skills.sh/google/agents-cli/google-agents-cli-eval) | Agent skill 'google-agents-cli-eval' from google/agents-cli: install via `npx skills add https://github.com/google/agents-cli --skill google-agents-cli-eval` to extend agent capabilities. |
| [binance-agentic-wallet — binance/binance-skills-hub](https://www.skills.sh/binance/binance-skills-hub/binance-agentic-wallet) | Agent skill 'binance-agentic-wallet' from binance/binance-skills-hub: install via `npx skills add https://github.com/binance/binance-skills-hub --skill binance-agentic-wallet` to extend agent capabilities. |
| [agent-browser — qu-skills/superpowers](https://www.skills.sh/qu-skills/superpowers/agent-browser) | Agent skill 'agent-browser' from qu-skills/superpowers: install via `npx skills add https://github.com/qu-skills/superpowers --skill agent-browser` to extend agent capabilities. |
| [analyze-project — lllllllama/rigorpilot-skills](https://www.skills.sh/lllllllama/rigorpilot-skills/analyze-project) | Agent skill 'analyze-project' from lllllllama/rigorpilot-skills: install via `npx skills add https://github.com/lllllllama/rigorpilot-skills --skill analyze-project` to extend agent capabilities. |
| [ponytail — dietrichgebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail/ponytail) | Agent skill 'ponytail' from dietrichgebert/ponytail: install via `npx skills add https://github.com/dietrichgebert/ponytail --skill ponytail` to extend agent capabilities. |
| [supabase — supabase/agent-skills](https://www.skills.sh/supabase/agent-skills/supabase) | Agent skill 'supabase' from supabase/agent-skills: install via `npx skills add https://github.com/supabase/agent-skills --skill supabase` to extend agent capabilities. |
| [vercel-react-view-transitions — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/vercel-react-view-transitions) | Agent skill 'vercel-react-view-transitions' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-view-transitions` to extend agent capabilities. |
| [deploy-to-vercel — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/deploy-to-vercel) | Agent skill 'deploy-to-vercel' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill deploy-to-vercel` to extend agent capabilities. |
| [vercel-react-native-skills — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/vercel-react-native-skills) | Agent skill 'vercel-react-native-skills' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-native-skills` to extend agent capabilities. |
| [caveman-compress — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-compress) | Agent skill 'caveman-compress' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-compress` to extend agent capabilities. |
| [supabase-postgres-best-practices — supabase/agent-skills](https://www.skills.sh/supabase/agent-skills/supabase-postgres-best-practices) | Agent skill 'supabase-postgres-best-practices' from supabase/agent-skills: install via `npx skills add https://github.com/supabase/agent-skills --skill supabase-postgres-best-practices` to extend agent capabilities. |
| [infsh-cli — qu-skills/superpowers](https://www.skills.sh/qu-skills/superpowers/infsh-cli) | Agent skill 'infsh-cli' from qu-skills/superpowers: install via `npx skills add https://github.com/qu-skills/superpowers --skill infsh-cli` to extend agent capabilities. |
| [vercel-optimize — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/vercel-optimize) | Agent skill 'vercel-optimize' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-optimize` to extend agent capabilities. |
| [cloudflare — cloudflare/skills](https://www.skills.sh/cloudflare/skills/cloudflare) | Agent skill 'cloudflare' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill cloudflare` to extend agent capabilities. |
| [writing-guidelines — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/writing-guidelines) | Agent skill 'writing-guidelines' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill writing-guidelines` to extend agent capabilities. |
| [shadcn — shadcn-ui/ui](https://www.skills.sh/shadcn-ui/ui/shadcn) | Agent skill 'shadcn' from shadcn-ui/ui: install via `npx skills add https://github.com/shadcn-ui/ui --skill shadcn` to extend agent capabilities. |
| [limrun-maestro-testing — limrun-inc/skills](https://www.skills.sh/limrun-inc/skills/limrun-maestro-testing) | Agent skill 'limrun-maestro-testing' from limrun-inc/skills: install via `npx skills add https://github.com/limrun-inc/skills --skill limrun-maestro-testing` to extend agent capabilities. |
| [python-executor — bankai-skills/superpowers](https://www.skills.sh/bankai-skills/superpowers/python-executor) | Agent skill 'python-executor' from bankai-skills/superpowers: install via `npx skills add https://github.com/bankai-skills/superpowers --skill python-executor` to extend agent capabilities. |
| [agent-tools — its-a-skill-issue/superpowers](https://www.skills.sh/its-a-skill-issue/superpowers/agent-tools) | Agent skill 'agent-tools' from its-a-skill-issue/superpowers: install via `npx skills add https://github.com/its-a-skill-issue/superpowers --skill agent-tools` to extend agent capabilities. |
| [remotion-render — bankai-skills/superpowers](https://www.skills.sh/bankai-skills/superpowers/remotion-render) | Agent skill 'remotion-render' from bankai-skills/superpowers: install via `npx skills add https://github.com/bankai-skills/superpowers --skill remotion-render` to extend agent capabilities. |
| [infsh-cli — magentosh/superpowers](https://www.skills.sh/magentosh/superpowers/infsh-cli) | Agent skill 'infsh-cli' from magentosh/superpowers: install via `npx skills add https://github.com/magentosh/superpowers --skill infsh-cli` to extend agent capabilities. |
| [workers-best-practices — cloudflare/skills](https://www.skills.sh/cloudflare/skills/workers-best-practices) | Agent skill 'workers-best-practices' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill workers-best-practices` to extend agent capabilities. |
| [python-executor — magentosh/superpowers](https://www.skills.sh/magentosh/superpowers/python-executor) | Agent skill 'python-executor' from magentosh/superpowers: install via `npx skills add https://github.com/magentosh/superpowers --skill python-executor` to extend agent capabilities. |
| [higgsfield-generate — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-generate) | Agent skill 'higgsfield-generate' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-generate` to extend agent capabilities. |
| [vercel-cli-with-tokens — vercel-labs/agent-skills](https://www.skills.sh/vercel-labs/agent-skills/vercel-cli-with-tokens) | Agent skill 'vercel-cli-with-tokens' from vercel-labs/agent-skills: install via `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-cli-with-tokens` to extend agent capabilities. |
| [caveman-commit — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-commit) | Agent skill 'caveman-commit' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-commit` to extend agent capabilities. |
| [web-search — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/web-search) | Agent skill 'web-search' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill web-search` to extend agent capabilities. |
| [microsoft-foundry — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/microsoft-foundry) | Agent skill 'microsoft-foundry' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill microsoft-foundry` to extend agent capabilities. |
| [caveman-review — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-review) | Agent skill 'caveman-review' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-review` to extend agent capabilities. |
| [python-executor — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/python-executor) | Agent skill 'python-executor' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill python-executor` to extend agent capabilities. |
| [landing-page-conversion-audit — autonnel/autonnel-skills](https://www.skills.sh/autonnel/autonnel-skills/landing-page-conversion-audit) | Agent skill 'landing-page-conversion-audit' from autonnel/autonnel-skills: install via `npx skills add https://github.com/autonnel/autonnel-skills --skill landing-page-conversion-audit` to extend agent capabilities. |
| [remotion-render — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/remotion-render) | Agent skill 'remotion-render' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill remotion-render` to extend agent capabilities. |
| [infsh-cli — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/infsh-cli) | Agent skill 'infsh-cli' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill infsh-cli` to extend agent capabilities. |
| [caveman-help — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-help) | Agent skill 'caveman-help' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-help` to extend agent capabilities. |
| [agent-tools — 101-skills/superpowers](https://www.skills.sh/101-skills/superpowers/agent-tools) | Agent skill 'agent-tools' from 101-skills/superpowers: install via `npx skills add https://github.com/101-skills/superpowers --skill agent-tools` to extend agent capabilities. |
| [browser-mcp-agent — antibrow/anti-detect-browser-skills](https://www.skills.sh/antibrow/anti-detect-browser-skills/browser-mcp-agent) | Agent skill 'browser-mcp-agent' from antibrow/anti-detect-browser-skills: install via `npx skills add https://github.com/antibrow/anti-detect-browser-skills --skill browser-mcp-agent` to extend agent capabilities. |
| [higgsfield-soul-id — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-soul-id) | Agent skill 'higgsfield-soul-id' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-soul-id` to extend agent capabilities. |
| [anti-detect-browser — antibrow/anti-detect-browser-skills](https://www.skills.sh/antibrow/anti-detect-browser-skills/anti-detect-browser) | Agent skill 'anti-detect-browser' from antibrow/anti-detect-browser-skills: install via `npx skills add https://github.com/antibrow/anti-detect-browser-skills --skill anti-detect-browser` to extend agent capabilities. |
| [multi-account-isolation — antibrow/anti-detect-browser-skills](https://www.skills.sh/antibrow/anti-detect-browser-skills/multi-account-isolation) | Agent skill 'multi-account-isolation' from antibrow/anti-detect-browser-skills: install via `npx skills add https://github.com/antibrow/anti-detect-browser-skills --skill multi-account-isolation` to extend agent capabilities. |
| [higgsfield-product-photoshoot — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-product-photoshoot) | Agent skill 'higgsfield-product-photoshoot' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-product-photoshoot` to extend agent capabilities. |
| [cavecrew — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/cavecrew) | Agent skill 'cavecrew' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill cavecrew` to extend agent capabilities. |
| [landing-page-design — skills-shell/superpowers](https://www.skills.sh/skills-shell/superpowers/landing-page-design) | Agent skill 'landing-page-design' from skills-shell/superpowers: install via `npx skills add https://github.com/skills-shell/superpowers --skill landing-page-design` to extend agent capabilities. |
| [app-store-screenshots — skills-shell/superpowers](https://www.skills.sh/skills-shell/superpowers/app-store-screenshots) | Agent skill 'app-store-screenshots' from skills-shell/superpowers: install via `npx skills add https://github.com/skills-shell/superpowers --skill app-store-screenshots` to extend agent capabilities. |
| [higgsfield-youtube-thumbnail — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-youtube-thumbnail) | Agent skill 'higgsfield-youtube-thumbnail' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-youtube-thumbnail` to extend agent capabilities. |
| [product-photography — skills-shell/superpowers](https://www.skills.sh/skills-shell/superpowers/product-photography) | Agent skill 'product-photography' from skills-shell/superpowers: install via `npx skills add https://github.com/skills-shell/superpowers --skill product-photography` to extend agent capabilities. |
| [caveman-stats — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-stats) | Agent skill 'caveman-stats' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-stats` to extend agent capabilities. |
| [funnel-platform-picker — autonnel/autonnel-skills](https://www.skills.sh/autonnel/autonnel-skills/funnel-platform-picker) | Agent skill 'funnel-platform-picker' from autonnel/autonnel-skills: install via `npx skills add https://github.com/autonnel/autonnel-skills --skill funnel-platform-picker` to extend agent capabilities. |
| [higgsfield-video-explainer — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-video-explainer) | Agent skill 'higgsfield-video-explainer' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-video-explainer` to extend agent capabilities. |
| [sales-funnel-blueprint — autonnel/autonnel-skills](https://www.skills.sh/autonnel/autonnel-skills/sales-funnel-blueprint) | Agent skill 'sales-funnel-blueprint' from autonnel/autonnel-skills: install via `npx skills add https://github.com/autonnel/autonnel-skills --skill sales-funnel-blueprint` to extend agent capabilities. |
| [ultracave — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/ultracave) | Agent skill 'ultracave' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill ultracave` to extend agent capabilities. |
| [server-side-conversion-tracking — autonnel/autonnel-skills](https://www.skills.sh/autonnel/autonnel-skills/server-side-conversion-tracking) | Agent skill 'server-side-conversion-tracking' from autonnel/autonnel-skills: install via `npx skills add https://github.com/autonnel/autonnel-skills --skill server-side-conversion-tracking` to extend agent capabilities. |
| [higgsfield-marketplace-cards — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-marketplace-cards) | Agent skill 'higgsfield-marketplace-cards' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-marketplace-cards` to extend agent capabilities. |
| [higgsfield-websites — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-websites) | Agent skill 'higgsfield-websites' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-websites` to extend agent capabilities. |
| [higgsfield-brandkit — higgsfield-ai/skills](https://www.skills.sh/higgsfield-ai/skills/higgsfield-brandkit) | Agent skill 'higgsfield-brandkit' from higgsfield-ai/skills: install via `npx skills add https://github.com/higgsfield-ai/skills --skill higgsfield-brandkit` to extend agent capabilities. |
| [post-purchase-upsell-flow — autonnel/autonnel-skills](https://www.skills.sh/autonnel/autonnel-skills/post-purchase-upsell-flow) | Agent skill 'post-purchase-upsell-flow' from autonnel/autonnel-skills: install via `npx skills add https://github.com/autonnel/autonnel-skills --skill post-purchase-upsell-flow` to extend agent capabilities. |
| [caveman-learn — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-learn) | Agent skill 'caveman-learn' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-learn` to extend agent capabilities. |
| [self-hosted-funnel-launch — autonnel/autonnel-skills](https://www.skills.sh/autonnel/autonnel-skills/self-hosted-funnel-launch) | Agent skill 'self-hosted-funnel-launch' from autonnel/autonnel-skills: install via `npx skills add https://github.com/autonnel/autonnel-skills --skill self-hosted-funnel-launch` to extend agent capabilities. |
| [fingerprint-failure-triage — liarjsdev/liarjs-skills](https://www.skills.sh/liarjsdev/liarjs-skills/fingerprint-failure-triage) | Agent skill 'fingerprint-failure-triage' from liarjsdev/liarjs-skills: install via `npx skills add https://github.com/liarjsdev/liarjs-skills --skill fingerprint-failure-triage` to extend agent capabilities. |
| [caveman-explore — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-explore) | Agent skill 'caveman-explore' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-explore` to extend agent capabilities. |
| [fingerprint-ci-gate — liarjsdev/liarjs-skills](https://www.skills.sh/liarjsdev/liarjs-skills/fingerprint-ci-gate) | Agent skill 'fingerprint-ci-gate' from liarjsdev/liarjs-skills: install via `npx skills add https://github.com/liarjsdev/liarjs-skills --skill fingerprint-ci-gate` to extend agent capabilities. |
| [safe-refactor — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/safe-refactor) | Agent skill 'safe-refactor' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill safe-refactor` to extend agent capabilities. |
| [megacave — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/megacave) | Agent skill 'megacave' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill megacave` to extend agent capabilities. |
| [browser-fingerprint-audit — liarjsdev/liarjs-skills](https://www.skills.sh/liarjsdev/liarjs-skills/browser-fingerprint-audit) | Agent skill 'browser-fingerprint-audit' from liarjsdev/liarjs-skills: install via `npx skills add https://github.com/liarjsdev/liarjs-skills --skill browser-fingerprint-audit` to extend agent capabilities. |
| [playwright-stealth-verify — liarjsdev/liarjs-skills](https://www.skills.sh/liarjsdev/liarjs-skills/playwright-stealth-verify) | Agent skill 'playwright-stealth-verify' from liarjsdev/liarjs-skills: install via `npx skills add https://github.com/liarjsdev/liarjs-skills --skill playwright-stealth-verify` to extend agent capabilities. |
| [caveman-optimize — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-optimize) | Agent skill 'caveman-optimize' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-optimize` to extend agent capabilities. |
| [caveman-discover — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-discover) | Agent skill 'caveman-discover' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-discover` to extend agent capabilities. |
| [migration — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/migration) | Agent skill 'migration' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill migration` to extend agent capabilities. |
| [wrangler — cloudflare/skills](https://www.skills.sh/cloudflare/skills/wrangler) | Agent skill 'wrangler' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill wrangler` to extend agent capabilities. |
| [caveman-setup — juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman/caveman-setup) | Agent skill 'caveman-setup' from juliusbrussee/caveman: install via `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-setup` to extend agent capabilities. |
| [sentry-cli — sentry/dev](https://www.skills.sh/sentry/dev/sentry-cli) | Agent skill 'sentry-cli' from sentry/dev: install via `npx skills add https://github.com/sentry/dev --skill sentry-cli` to extend agent capabilities. |
| [seo — iannuttall/seo](https://www.skills.sh/iannuttall/seo/seo) | Agent skill 'seo' from iannuttall/seo: install via `npx skills add https://github.com/iannuttall/seo --skill seo` to extend agent capabilities. |
| [cloudflare-one — cloudflare/skills](https://www.skills.sh/cloudflare/skills/cloudflare-one) | Agent skill 'cloudflare-one' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill cloudflare-one` to extend agent capabilities. |
| [web-perf — cloudflare/skills](https://www.skills.sh/cloudflare/skills/web-perf) | Agent skill 'web-perf' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill web-perf` to extend agent capabilities. |
| [copywriting — coreyhaines31/marketingskills](https://www.skills.sh/coreyhaines31/marketingskills/copywriting) | Agent skill 'copywriting' from coreyhaines31/marketingskills: install via `npx skills add https://github.com/coreyhaines31/marketingskills --skill copywriting` to extend agent capabilities. |
| [azure-kubernetes — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/azure-kubernetes) | Agent skill 'azure-kubernetes' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill azure-kubernetes` to extend agent capabilities. |
| [azure-upgrade — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/azure-upgrade) | Agent skill 'azure-upgrade' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill azure-upgrade` to extend agent capabilities. |
| [webapp-testing — anthropics/skills](https://www.skills.sh/anthropics/skills/webapp-testing) | Agent skill 'webapp-testing' from anthropics/skills: install via `npx skills add https://github.com/anthropics/skills --skill webapp-testing` to extend agent capabilities. |
| [azure-prepare — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/azure-prepare) | Agent skill 'azure-prepare' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill azure-prepare` to extend agent capabilities. |
| [durable-objects — cloudflare/skills](https://www.skills.sh/cloudflare/skills/durable-objects) | Agent skill 'durable-objects' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill durable-objects` to extend agent capabilities. |
| [azure-compute — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/azure-compute) | Agent skill 'azure-compute' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill azure-compute` to extend agent capabilities. |
| [sales-hiring — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-hiring) | Agent skill 'sales-hiring' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-hiring` to extend agent capabilities. |
| [sales-icp-definition — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-icp-definition) | Agent skill 'sales-icp-definition' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-icp-definition` to extend agent capabilities. |
| [entra-app-registration — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/entra-app-registration) | Agent skill 'entra-app-registration' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill entra-app-registration` to extend agent capabilities. |
| [sales-career — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-career) | Agent skill 'sales-career' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-career` to extend agent capabilities. |
| [python-appservice-deploy — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/python-appservice-deploy) | Agent skill 'python-appservice-deploy' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill python-appservice-deploy` to extend agent capabilities. |
| [sales-account-tiering — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-account-tiering) | Agent skill 'sales-account-tiering' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-account-tiering` to extend agent capabilities. |
| [discover-azure-skills — microsoft/azure-skills](https://www.skills.sh/microsoft/azure-skills/discover-azure-skills) | Agent skill 'discover-azure-skills' from microsoft/azure-skills: install via `npx skills add https://github.com/microsoft/azure-skills --skill discover-azure-skills` to extend agent capabilities. |
| [sales-pipeline-coverage-modeling — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-pipeline-coverage-modeling) | Agent skill 'sales-pipeline-coverage-modeling' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-pipeline-coverage-modeling` to extend agent capabilities. |
| [sales-outbound-sequence — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-outbound-sequence) | Agent skill 'sales-outbound-sequence' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-outbound-sequence` to extend agent capabilities. |
| [sales-radar — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-radar) | Agent skill 'sales-radar' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-radar` to extend agent capabilities. |
| [cloudflare-email-service — cloudflare/skills](https://www.skills.sh/cloudflare/skills/cloudflare-email-service) | Agent skill 'cloudflare-email-service' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill cloudflare-email-service` to extend agent capabilities. |
| [turnstile-spin — cloudflare/skills](https://www.skills.sh/cloudflare/skills/turnstile-spin) | Agent skill 'turnstile-spin' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill turnstile-spin` to extend agent capabilities. |
| [sales-outreach-personalization — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-outreach-personalization) | Agent skill 'sales-outreach-personalization' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-outreach-personalization` to extend agent capabilities. |
| [sales-call-review — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-call-review) | Agent skill 'sales-call-review' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-call-review` to extend agent capabilities. |
| [sales-account-segmentation — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-account-segmentation) | Agent skill 'sales-account-segmentation' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-account-segmentation` to extend agent capabilities. |
| [agents-sdk — cloudflare/skills](https://www.skills.sh/cloudflare/skills/agents-sdk) | Agent skill 'agents-sdk' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill agents-sdk` to extend agent capabilities. |
| [sales-quota-setting — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-quota-setting) | Agent skill 'sales-quota-setting' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-quota-setting` to extend agent capabilities. |
| [sales-objection-handling — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-objection-handling) | Agent skill 'sales-objection-handling' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-objection-handling` to extend agent capabilities. |
| [playwright-cli — microsoft/playwright-cli](https://www.skills.sh/microsoft/playwright-cli/playwright-cli) | Agent skill 'playwright-cli' from microsoft/playwright-cli: install via `npx skills add https://github.com/microsoft/playwright-cli --skill playwright-cli` to extend agent capabilities. |
| [cold-call-opener — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/cold-call-opener) | Agent skill 'cold-call-opener' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill cold-call-opener` to extend agent capabilities. |
| [cloudflare-one-migrations — cloudflare/skills](https://www.skills.sh/cloudflare/skills/cloudflare-one-migrations) | Agent skill 'cloudflare-one-migrations' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill cloudflare-one-migrations` to extend agent capabilities. |
| [cold-email-subject-line-tester — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/cold-email-subject-line-tester) | Agent skill 'cold-email-subject-line-tester' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill cold-email-subject-line-tester` to extend agent capabilities. |
| [cold-email-deliverability — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/cold-email-deliverability) | Agent skill 'cold-email-deliverability' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill cold-email-deliverability` to extend agent capabilities. |
| [sales-org-structure — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/sales-org-structure) | Agent skill 'sales-org-structure' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill sales-org-structure` to extend agent capabilities. |
| [nextjs-on-cloudflare — cloudflare/skills](https://www.skills.sh/cloudflare/skills/nextjs-on-cloudflare) | Agent skill 'nextjs-on-cloudflare' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill nextjs-on-cloudflare` to extend agent capabilities. |
| [cf-cli — cloudflare/skills](https://www.skills.sh/cloudflare/skills/cf-cli) | Agent skill 'cf-cli' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill cf-cli` to extend agent capabilities. |
| [sandbox-stable — cloudflare/skills](https://www.skills.sh/cloudflare/skills/sandbox-stable) | Agent skill 'sandbox-stable' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill sandbox-stable` to extend agent capabilities. |
| [negotiation-concession-planner — mbfinotti/sales-skills](https://www.skills.sh/mbfinotti/sales-skills/negotiation-concession-planner) | Agent skill 'negotiation-concession-planner' from mbfinotti/sales-skills: install via `npx skills add https://github.com/mbfinotti/sales-skills --skill negotiation-concession-planner` to extend agent capabilities. |
| [seo-audit — coreyhaines31/marketingskills](https://www.skills.sh/coreyhaines31/marketingskills/seo-audit) | Agent skill 'seo-audit' from coreyhaines31/marketingskills: install via `npx skills add https://github.com/coreyhaines31/marketingskills --skill seo-audit` to extend agent capabilities. |
| [workers-profiling — cloudflare/skills](https://www.skills.sh/cloudflare/skills/workers-profiling) | Agent skill 'workers-profiling' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill workers-profiling` to extend agent capabilities. |
| [sandbox-next — cloudflare/skills](https://www.skills.sh/cloudflare/skills/sandbox-next) | Agent skill 'sandbox-next' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill sandbox-next` to extend agent capabilities. |
| [sandbox-migrate-to-next — cloudflare/skills](https://www.skills.sh/cloudflare/skills/sandbox-migrate-to-next) | Agent skill 'sandbox-migrate-to-next' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill sandbox-migrate-to-next` to extend agent capabilities. |
| [k2 — cloudflare/skills](https://www.skills.sh/cloudflare/skills/k2) | Agent skill 'k2' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill k2` to extend agent capabilities. |
| [gateway-workers — cloudflare/skills](https://www.skills.sh/cloudflare/skills/gateway-workers) | Agent skill 'gateway-workers' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill gateway-workers` to extend agent capabilities. |
| [basin — cloudflare/skills](https://www.skills.sh/cloudflare/skills/basin) | Agent skill 'basin' from cloudflare/skills: install via `npx skills add https://github.com/cloudflare/skills --skill basin` to extend agent capabilities. |
| [lark-doc — larksuite/cli](https://www.skills.sh/larksuite/cli/lark-doc) | Agent skill 'lark-doc' from larksuite/cli: install via `npx skills add https://github.com/larksuite/cli --skill lark-doc` to extend agent capabilities. |
| [lark-shared — larksuite/cli](https://www.skills.sh/larksuite/cli/lark-shared) | Agent skill 'lark-shared' from larksuite/cli: install via `npx skills add https://github.com/larksuite/cli --skill lark-shared` to extend agent capabilities. |
| [lark-wiki — larksuite/cli](https://www.skills.sh/larksuite/cli/lark-wiki) | Agent skill 'lark-wiki' from larksuite/cli: install via `npx skills add https://github.com/larksuite/cli --skill lark-wiki` to extend agent capabilities. |
| [writing-skills — obra/superpowers](https://www.skills.sh/obra/superpowers/writing-skills) | Agent skill 'writing-skills' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill writing-skills` to extend agent capabilities. |
| [lark-okr — larksuite/cli](https://www.skills.sh/larksuite/cli/lark-okr) | Agent skill 'lark-okr' from larksuite/cli: install via `npx skills add https://github.com/larksuite/cli --skill lark-okr` to extend agent capabilities. |
| [ponytail-review — dietrichgebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail/ponytail-review) | Agent skill 'ponytail-review' from dietrichgebert/ponytail: install via `npx skills add https://github.com/dietrichgebert/ponytail --skill ponytail-review` to extend agent capabilities. |
| [lark-note — larksuite/cli](https://www.skills.sh/larksuite/cli/lark-note) | Agent skill 'lark-note' from larksuite/cli: install via `npx skills add https://github.com/larksuite/cli --skill lark-note` to extend agent capabilities. |
| [security-and-hardening — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/security-and-hardening) | Agent skill 'security-and-hardening' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill security-and-hardening` to extend agent capabilities. |
| [diagram-design — cathrynlavery/diagram-design](https://www.skills.sh/cathrynlavery/diagram-design/diagram-design) | Agent skill 'diagram-design' from cathrynlavery/diagram-design: install via `npx skills add https://github.com/cathrynlavery/diagram-design --skill diagram-design` to extend agent capabilities. |
| [code-review-and-quality — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/code-review-and-quality) | Agent skill 'code-review-and-quality' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill code-review-and-quality` to extend agent capabilities. |
| [404-agent-wallet — notfound-404-office/agent-skills](https://www.skills.sh/notfound-404-office/agent-skills/404-agent-wallet) | Agent skill '404-agent-wallet' from notfound-404-office/agent-skills: install via `npx skills add https://github.com/notfound-404-office/agent-skills --skill 404-agent-wallet` to extend agent capabilities. |
| [revops-radar — mbfinotti/revops-skills](https://www.skills.sh/mbfinotti/revops-skills/revops-radar) | Agent skill 'revops-radar' from mbfinotti/revops-skills: install via `npx skills add https://github.com/mbfinotti/revops-skills --skill revops-radar` to extend agent capabilities. |
| [ponytail-audit — dietrichgebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail/ponytail-audit) | Agent skill 'ponytail-audit' from dietrichgebert/ponytail: install via `npx skills add https://github.com/dietrichgebert/ponytail --skill ponytail-audit` to extend agent capabilities. |
| [revenue-kpi-framework — mbfinotti/revops-skills](https://www.skills.sh/mbfinotti/revops-skills/revenue-kpi-framework) | Agent skill 'revenue-kpi-framework' from mbfinotti/revops-skills: install via `npx skills add https://github.com/mbfinotti/revops-skills --skill revenue-kpi-framework` to extend agent capabilities. |
| [receiving-code-review — obra/superpowers](https://www.skills.sh/obra/superpowers/receiving-code-review) | Agent skill 'receiving-code-review' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill receiving-code-review` to extend agent capabilities. |
| [revenue-leakage — mbfinotti/revops-skills](https://www.skills.sh/mbfinotti/revops-skills/revenue-leakage) | Agent skill 'revenue-leakage' from mbfinotti/revops-skills: install via `npx skills add https://github.com/mbfinotti/revops-skills --skill revenue-leakage` to extend agent capabilities. |
| [using-superpowers — obra/superpowers](https://www.skills.sh/obra/superpowers/using-superpowers) | Agent skill 'using-superpowers' from obra/superpowers: install via `npx skills add https://github.com/obra/superpowers --skill using-superpowers` to extend agent capabilities. |
| [lead-scoring — mbfinotti/revops-skills](https://www.skills.sh/mbfinotti/revops-skills/lead-scoring) | Agent skill 'lead-scoring' from mbfinotti/revops-skills: install via `npx skills add https://github.com/mbfinotti/revops-skills --skill lead-scoring` to extend agent capabilities. |
| [ponytail-debt — dietrichgebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail/ponytail-debt) | Agent skill 'ponytail-debt' from dietrichgebert/ponytail: install via `npx skills add https://github.com/dietrichgebert/ponytail --skill ponytail-debt` to extend agent capabilities. |
| [frontend-ui-engineering — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/frontend-ui-engineering) | Agent skill 'frontend-ui-engineering' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill frontend-ui-engineering` to extend agent capabilities. |
| [revenue-data-governance-strategy — mbfinotti/revops-skills](https://www.skills.sh/mbfinotti/revops-skills/revenue-data-governance-strategy) | Agent skill 'revenue-data-governance-strategy' from mbfinotti/revops-skills: install via `npx skills add https://github.com/mbfinotti/revops-skills --skill revenue-data-governance-strategy` to extend agent capabilities. |
| [ponytail-help — dietrichgebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail/ponytail-help) | Agent skill 'ponytail-help' from dietrichgebert/ponytail: install via `npx skills add https://github.com/dietrichgebert/ponytail --skill ponytail-help` to extend agent capabilities. |
| [performance-optimization — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/performance-optimization) | Agent skill 'performance-optimization' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill performance-optimization` to extend agent capabilities. |
| [api-and-interface-design — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/api-and-interface-design) | Agent skill 'api-and-interface-design' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill api-and-interface-design` to extend agent capabilities. |
| [ponytail-gain — dietrichgebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail/ponytail-gain) | Agent skill 'ponytail-gain' from dietrichgebert/ponytail: install via `npx skills add https://github.com/dietrichgebert/ponytail --skill ponytail-gain` to extend agent capabilities. |
| [ai-seo — coreyhaines31/marketingskills](https://www.skills.sh/coreyhaines31/marketingskills/ai-seo) | Agent skill 'ai-seo' from coreyhaines31/marketingskills: install via `npx skills add https://github.com/coreyhaines31/marketingskills --skill ai-seo` to extend agent capabilities. |
| [spec-driven-development — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/spec-driven-development) | Agent skill 'spec-driven-development' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill spec-driven-development` to extend agent capabilities. |
| [ad-creative-fatigue — mbfinotti/advertising-skills](https://www.skills.sh/mbfinotti/advertising-skills/ad-creative-fatigue) | Agent skill 'ad-creative-fatigue' from mbfinotti/advertising-skills: install via `npx skills add https://github.com/mbfinotti/advertising-skills --skill ad-creative-fatigue` to extend agent capabilities. |
| [documentation-and-adrs — addyosmani/agent-skills](https://www.skills.sh/addyosmani/agent-skills/documentation-and-adrs) | Agent skill 'documentation-and-adrs' from addyosmani/agent-skills: install via `npx skills add https://github.com/addyosmani/agent-skills --skill documentation-and-adrs` to extend agent capabilities. |
| [ad-spend-allocation — mbfinotti/advertising-skills](https://www.skills.sh/mbfinotti/advertising-skills/ad-spend-allocation) | Agent skill 'ad-spend-allocation' from mbfinotti/advertising-skills: install via `npx skills add https://github.com/mbfinotti/advertising-skills --skill ad-spend-allocation` to extend agent capabilities. |
| [agent-browser — vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | GitHub source for vercel-labs/agent-browser: Browser automation agent skill. Install skills via `npx skills add https://github.com/vercel-labs/agent-browser`. |

## AI MCP servers and tool use (51)

| Resource | Useful for / constraints |
|---|---|
| [MCP Conformance Tests](https://github.com/modelcontextprotocol/conformance) | Official conformance suite to validate MCP server implementations. |
| [GitLab MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) | GitLab MCP: MRs, issues, pipelines for GitLab-hosted projects. |
| [Slack MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) | Slack MCP: channels, messages, and search for agent integrations. |
| [Notion MCP Server](https://github.com/makenotion/notion-mcp-server) | Notion's MCP for pages, databases, and search. |
| [Linear MCP Server](https://github.com/linear/linear-mcp) | Linear's official MCP for issues and project management. |
| [Atlassian MCP](https://github.com/sooperset/mcp-atlassian) | Jira and Confluence via MCP: issues, pages, and search. |
| [Postgres MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | Postgres MCP: query, schema, and data exploration via MCP. |
| [SQLite MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | SQLite MCP for local database tooling. |
| [BigQuery MCP Server](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/bigquery) | BigQuery MCP (archived): query and dataset inspection via MCP. |
| [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Reference filesystem MCP with sandboxing for safe file ops. |
| [Memory MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | Knowledge-graph memory MCP for persistent agent memory. |
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Brave Search MCP for web search grounding. |
| [Puppeteer MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | Puppeteer MCP for browser automation via MCP tools. |
| [Fetch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Fetch MCP for URL retrieval and content extraction. |
| [Google Drive MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) | Google Drive MCP: files and search via OAuth. |
| [Google Maps MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) | Google Maps MCP for places, directions, and geocoding. |
| [Everart MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/everart) | EverArt MCP for image generation via EverArt API. |
| [AWS Docs MCP](https://github.com/awslabs/mcp/tree/main/src/aws-docs-mcp-server) | AWS docs MCP from awslabs: search AWS documentation via MCP. |
| [AWS Cost Explorer MCP](https://github.com/awslabs/mcp/tree/main/src/cost-explorer-mcp-server) | AWS Cost Explorer MCP for cost analysis via agent. |
| [Sentry MCP](https://github.com/getsentry/sentry-mcp) | Sentry MCP for issues, traces, and release health. |
| [Stripe MCP](https://github.com/stripe/agent-toolkit) | Stripe agent toolkit with MCP server for payments, customers, invoices. |
| [Twilio MCP](https://github.com/twilio-labs/mcp-twilio) | Twilio MCP for SMS, voice, and communications APIs. |
| [Resend MCP](https://github.com/resend/mcp-send) | Resend MCP for transactional email via agents. |
| [PostHog MCP](https://github.com/PostHog/mcp) | PostHog MCP for analytics and feature flag context. |
| [LaunchDarkly MCP](https://github.com/launchdarkly/mcp-server) | LaunchDarkly MCP for feature flags via agent tooling. |
| [Supabase MCP](https://github.com/supabase-community/supabase-mcp) | Supabase MCP for database, auth, and storage operations. |
| [Qdrant MCP Server](https://github.com/qdrant/mcp-server-qdrant) | Qdrant MCP for vector search via MCP tools. |
| [Pinecone MCP Assistant](https://github.com/pinecone-io/pinecone-mcp) | Pinecone's experimental MCP for vector DB operations. |
| [Tavily MCP Server](https://github.com/tavily-ai/tavily-mcp) | Tavily MCP for AI-optimized search and extraction. |
| [Exa MCP Server](https://github.com/exa-labs/exa-mcp-server) | Exa MCP for neural web search. |
| [Firecrawl MCP](https://github.com/mendable/firecrawl-mcp-server) | Firecrawl MCP for scraping and crawling via MCP. |
| [Apify MCP Server](https://github.com/apify/mcp-server-actors) | Apify Actors MCP: run 3k+ web scrapers as tools. |
| [Docker MCP Toolkit](https://github.com/docker/mcp-servers) | Docker's MCP catalog and gateway for containerized MCP servers. |
| [Kubernetes MCP Server](https://github.com/manusa/kubernetes-mcp-server) | Kubernetes MCP for pod, deployment, and logs access. |
| [Grafana MCP Server](https://github.com/grafana/mcp-grafana) | Grafana MCP for dashboards, alerts, and data sources. |
| [Datadog MCP Server](https://github.com/DataDog/mcp-server-datadog) | Datadog MCP for metrics, logs, and traces. |
| [New Relic MCP](https://github.com/newrelic/mcp-nr) | New Relic MCP for observability data. |
| [Pulumi MCP Server](https://github.com/pulumi/pulumi-mcp-server) | Pulumi MCP for infrastructure code generation and deployments. |
| [Vercel MCP](https://github.com/vercel/mcp-vercel) | Vercel MCP for deployments, logs, and project management. |
| [Netlify MCP](https://github.com/netlify/mcp-server-netlify) | Netlify MCP for deploys and site management. |
| [Heroku MCP](https://github.com/heroku/mcp-server-heroku) | Heroku MCP for app and dyno management. |
| [Figma MCP Server](https://github.com/figma/mcp-server-figma) | Figma MCP for design files, components, and comments. |
| [Canva MCP Server](https://github.com/canva/canva-mcp) | Canva MCP for design automation. |
| [Bluesky MCP](https://github.com/bluesky-social/mcp-bluesky) | Bluesky MCP for social posting and feeds. |
| [YouTube MCP Server](https://github.com/ZubeidHendricks/youtube-mcp-server) | YouTube MCP for transcripts, search, and metadata. |
| [Spotify MCP Server](https://github.com/varunneal/spotify-mcp) | Spotify MCP for playback and library access. |
| [Gmail MCP Server](https://github.com/GongRzhe/Gmail-MCP-Server) | Unofficial Gmail MCP for email search and drafts (OAuth). |
| [Zendesk MCP](https://github.com/zendesk/mcp-server-zendesk) | Zendesk MCP for tickets and help-center docs. |
| [Intercom MCP](https://github.com/intercom/mcp-server-intercom) | Intercom MCP for support conversations. |
| [HubSpot MCP](https://github.com/hubspot/mcp-server-hubspot) | HubSpot MCP for CRM contacts, deals, and tickets. |
| [Salesforce MCP (unofficial)](https://github.com/twilio-labs/mcp-salesforce) | Community Salesforce MCP for CRM via SOQL — verify OAuth. |

## AI agent frameworks and orchestration (82)

| Resource | Useful for / constraints |
|---|---|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | Pioneering autonomous agent that chains LLM thoughts to achieve goals — benchmark for agent evaluation. |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | Task-driven autonomous agent loop with vector memory — minimal reference implementation. |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | Open-source autonomous agent framework with toolkits and GUI. |
| [OpenDevin (OpenHands)](https://github.com/All-Hands-AI/OpenHands) | OpenHands (ex-OpenDevin) for autonomous software development — code execution via sandboxes. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | Multi-agent framework that assigns roles (PM, architect, engineer) to build software. |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Chat-powered software development via multi-agent chat chain. |
| [CAMEL-AI](https://github.com/camel-ai/camel) | Communicative agents for mind exploration of LLM society and role-play. |
| [AutoGen Studio](https://microsoft.github.io/autogen/docs/autogen-studio/getting-started/) | Low-code UI for building and testing AutoGen multi-agent workflows. |
| [CrewAI Tools](https://docs.crewai.com/tools/overview) | Toolkit for CrewAI crews: search, code execution, and API integrations. |
| [LangGraph Cloud](https://langchain-ai.github.io/langgraph/cloud/) | Managed LangGraph deployment with durable execution and human-in-the-loop. |
| [Prefect](https://docs.prefect.io/latest/) | Workflow orchestration for agents: scheduling, retries, and observability. |
| [Airflow](https://airflow.apache.org/docs/) | Apache Airflow: battle-tested DAG orchestration for batch agent pipelines. |
| [Dagster](https://docs.dagster.io/) | Data and ML orchestration with strong typing and asset lineage for agent pipelines. |
| [Step Functions (AWS)](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) | AWS Step Functions for durable agent workflows with Bedrock integration. |
| [Azure Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview) | Durable Functions for stateful agent orchestrations on Azure. |
| [Google Workflows](https://cloud.google.com/workflows/docs) | Orchestrate GCP services and AI APIs into agent workflows. |
| [LangChain LCEL](https://python.langchain.com/docs/concepts/lcel) | LangChain Expression Language for composing chains, retries, and fallbacks. |
| [LlamaIndex Workflows](https://developers.llamaindex.ai/python/framework/workflows/) | Event-driven orchestration for LlamaIndex agents with human-in-the-loop. |
| [Semantic Kernel Planners](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planners) | Semantic Kernel planners for goal decomposition and function calling. |
| [LMQL](https://github.com/eth-sri/lmql) | Language model query language for constrained generation with logic constraints. |
| [Outlines](https://github.com/dottxt-ai/outlines) | Structured generation with JSON schema, regex, and CFG for LLMs (fast). |
| [Instructor (Structured Outputs)](https://github.com/jxnl/instructor) | Instructor for perfect structured outputs via function calling and schema validation. |
| [BAML](https://docs.boundaryml.com/home) | BAML: typed prompt language that compiles to LLM clients with structured outputs. |
| [EvoAgent](https://github.com/EvoAgentX/EvoAgentX) | Evolving agent workflows via optimization — auto-improve prompts and toolsets. |
| [ADaPT](https://github.com/archi-lab/adapt) | As-needed decomposition and planning for LLM agents. |
| [ReAct (LangChain)](https://python.langchain.com/docs/modules/agents/agent_types/react) | ReAct pattern: reason + act loops for tool-using agents. |
| [ReWOO](https://github.com/billxzy1215/ReWOO) | Modular reasoning with tool use decoupled from observation. |
| [Reflexion](https://github.com/noahshinn/reflexion) | Reflexion: verbal reinforcement for agents that learn from mistakes. |
| [Voyager (Minecraft)](https://github.com/MineDojo/Voyager) | Voyager: lifelong learning agent in Minecraft via curriculum and skill library. |
| [Generative Agents (Stanford)](https://github.com/joonspk-research/generative_agents) | Stanford smallville generative agents with memory and social simulation. |
| [Smallville (Park et al.)](https://arxiv.org/abs/2304.03442) | Paper: generative agents simulate human behavior — influencial for agent memory design. |
| [Toolformer Paper](https://arxiv.org/abs/2302.04761) | Paper: LLMs that teach themselves to use tools via self-supervision. |
| [Gorilla (Berkeley)](https://github.com/ShishirPatil/gorilla) | Berkeley's LLM for API calling with ToolBench evaluation. |
| [Functionary (MeetKai)](https://github.com/meetkai/functionary) | Open LLM fine-tuned for function calling — check Apache 2 license. |
| [Nexus Raven](https://github.com/nexusflowai/nexus-hub) | Nexus Raven: function calling model optimized for tool use. |
| [Hermes Function Calling](https://github.com/NousResearch/Hermes-Function-Calling) | Nous Hermes fine-tunes for function calling and system-prompt steering. |
| [OpenFunctions](https://github.com/OpenFunctions) | Open-source function-calling datasets and models. |
| [ToolLLaMA](https://github.com/open-compass/ToolLLaMA) | ToolLLaMA via ToolBench: large tool-use benchmark and models. |
| [AgentBench](https://github.com/THUDM/AgentBench) | Benchmark for LLM-as-agent across 8 environments (OS, DB, etc.). |
| [WebArena](https://github.com/web-arena-x/webarena) | WebArena: realistic web environment for autonomous agent evaluation. |
| [GAIA](https://huggingface.co/gaia-benchmark) | GAIA: General AI Assistants benchmark with real-world multi-step tasks. |
| [HumanEval](https://github.com/openai/human-eval) | OpenAI HumanEval for code generation correctness — still-cited coding benchmark. |
| [MBPP](https://github.com/google-research/google-research/tree/master/mbpp) | Mostly Basic Python Problems benchmark for code LLMs. |
| [BFCL (Berkeley Function Calling)](https://gorilla.cs.berkeley.edu/leaderboard.html) | Berkeley Function Calling Leaderboard: rigorous tool-use evaluation. |
| [ToolBench](https://github.com/open-compass/ToolBench) | Large-scale tool-use benchmark with 16k real APIs. |
| [T-Eval](https://github.com/open-compass/T-Eval) | Step-by-step tool-use evaluation for LLMs. |
| [AgentTuning](https://github.com/THUDM/AgentTuning) | AgentTuning: fine-tuning LLMs for agentic behavior with trajectory data. |
| [FireAct](https://github.com/THUDM/FireAct) | Fine-tuning agents with ReAct trajectories from GPT-4. |
| [TRICE](https://github.com/THUDM/TRICE) | Training agentic capabilities via intermediate chaining. |
| [Swarm (OpenAI)](https://github.com/openai/swarm) | OpenAI's lightweight multi-agent orchestration experiment: handoffs between agents. |
| [Magentic-One (Microsoft)](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one) | Microsoft's generalist multi-agent for web and file tasks (Orchestrator pattern). |
| [TaskWeaver (Microsoft)](https://github.com/microsoft/TaskWeaver) | TaskWeaver: code-first agent for data analytics with planner and code executor. |
| [JARVIS (Microsoft)](https://github.com/microsoft/JARVIS) | JARVIS (HuggingGPT) connects LLMs to Hugging Face models as tools. |
| [MM-REACT](https://github.com/microsoft/MM-REACT) | Microsoft's multimodal ReAct: reasoning with tools over vision/language. |
| [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt) | Visual ChatGPT: ChatGPT with visual foundation models as tools. |
| [LLaVA](https://github.com/haotian-liu/LLaVA) | Large Language and Vision Assistant: open multimodal chat. |
| [Qwen-VL](https://github.com/QwenLM/Qwen-VL) | Alibaba's vision-language family for multimodal agents. |
| [CogVLM](https://github.com/THUDM/CogVLM) | THUDM's open visual language models with strong grounding. |
| [Kosmos-2](https://github.com/microsoft/unilm/tree/master/kosmos-2) | Microsoft Kosmos-2 for grounded multimodal language. |
| [Paligemma](https://github.com/google-research/big_vision/tree/main/big_vision/configs/proj/paligemma) | Google PaliGemma vision-language model family. |
| [Fuyu-8B](https://www.adept.ai/blog/fuyu-8b) | Adept Fuyu: high-res multimodal model for agent UIs. |
| [Claude Artifacts](https://docs.anthropic.com/en/docs/build-with-claude/artifacts) | Artifacts: Claude's interactive canvas for code and design — useful agent UX pattern. |
| [OpenAI Canvas](https://openai.com/index/introducing-canvas/) | ChatGPT Canvas: collaborative writing/coding surface — pattern for agent UX. |
| [Gemini Canvas](https://blog.google/products/gemini/gemini-canvas/) | Gemini Canvas for interactive creation and iteration. |
| [Perplexity Spaces](https://www.perplexity.ai/help-center/en/articles/10352995-what-is-a-space) | Perplexity Spaces: collaborative, source-grounded agent workspaces. |
| [Notion AI](https://www.notion.com/help/guides/category/notion-ai) | Notion AI skills: Q&A, writing, and automation over workspace. |
| [MemGPT (Letta)](https://github.com/cpacker/MemGPT) | Original MemGPT paper implementation — long-term memory for agents. |
| [Arize Phoenix](https://phoenix.arize.com/) | Open-source LLM observability: traces, evals, and experiments. |
| [HumanLoop](https://humanloop.com/docs) | Prompt management and LLM evaluation platform with human feedback. |
| [Comet Opik](https://www.comet.com/site/products/opik/) | Comet Opik: open-source LLM evaluation and observability. |
| [Weave (Weights & Biases)](https://weave-docs.wandb.ai/) | Weave: trace, evaluate, and improve LLM apps from W&B. |
| [LangWatch](https://docs.langwatch.ai/) | LLM monitoring: guardrails, analytics, and prompt optimization. |
| [Portkey Guardrails](https://portkey.ai/docs/product/guardrails) | Guardrails for LLM: PII, toxicity, and hallucination detection. |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA's programmable guardrails for conversational AI. |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761#fallback-17) | Toolformer: self-supervised tool use via API calls — foundational for agent framework design. |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629#fallback-18) | ReAct paper: interleaving reasoning and tool use that powers most agent frameworks. |
| [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903#fallback-19) | Chain-of-Thought: step-by-step reasoning that improves agent planning and decomposition. |
| [Tree of Thoughts: Deliberate Problem Solving](https://arxiv.org/abs/2305.10601#fallback-20) | Tree-of-Thoughts: search over thought trees for better planning than linear CoT. |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | Voyager: lifelong Minecraft agent with skill library — curriculum for evolving agents. |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442#fallback-22) | Stanford Generative Agents: memory and social simulation patterns for agent design. |
| [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) | AutoGen paper: conversational multi-agent orchestration from Microsoft. |
| [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) | Gorilla paper: function calling with ToolBench — evaluation driven framework selection. |

## AI agent memory and context (27)

| Resource | Useful for / constraints |
|---|---|
| [Mem0 Platform](https://docs.mem0.ai/platform/overview) | Mem0 platform overview: memory extraction and search API. |
| [Zep Temporal KG](https://help.getzep.com/concepts) | Zep concepts: temporal knowledge graph for agent memory. |
| [LangGraph Memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/) | LangGraph how-to: add short and long-term memory to agents. |
| [LlamaIndex Memory Chat](https://docs.llamaindex.ai/en/stable/examples/agent/memory/) | LlamaIndex chat memory examples for agents. |
| [MemGPT Research](https://arxiv.org/abs/2310.08560) | MemGPT paper: OS-inspired memory for LLMs with virtual context. |
| [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | HippoRAG: associative memory inspired by hippocampus for RAG. |
| [Mem0 OSS](https://github.com/mem0ai/mem0) | Mem0 open source repo for long-term memory layer. |
| [Supermemory](https://supermemory.ai/docs) | Supermemory: universal memory API for agents and apps. |
| [Chroma Memory](https://docs.trychroma.com/docs/overview/introduction) | Chroma as memory store for agents — embedding-backed recall. |
| [qdrant-memory](https://qdrant.tech/articles/agentic-memory/) | Qdrant article on agentic memory with vectors. |
| [Pinecone Assistant Memory](https://docs.pinecone.io/guides/assistant/overview) | Pinecone Assistant for grounded knowledge management. |
| [Weaviate Memory Service](https://weaviate.io/blog/weaviate-agents) | Weaviate agents with memory and generative search. |
| [OpenAI Memory (ChatGPT)](https://help.openai.com/en/articles/8590148-memory-in-chatgpt) | OpenAI's memory feature docs — design pattern for user memory. |
| [Anthropic Memory Tool (beta)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/memory-tool) | Anthropic memory tool beta for Claude agents. |
| [LangMem Store](https://langchain-ai.github.io/langmem/concepts/store/) | LangMem store concepts for cross-thread memory. |
| [AutoGen Memory](https://microsoft.github.io/autogen/docs/tutorial/memory) | AutoGen tutorial on memory for agents. |
| [CrewAI Memory](https://docs.crewai.com/concepts/memory) | CrewAI memory docs: short, long, and entity memory. |
| [Semantic Kernel Memory](https://learn.microsoft.com/en-us/semantic-kernel/memories/) | Semantic Kernel memory with embeddings and volunteers. |
| [Haystack Memory](https://docs.haystack.deepset.ai/docs/memmory) | Haystack memory for pipelines (note typo-tolerant docs). |
| [Haystack Chat History](https://docs.haystack.deepset.ai/docs/chat-history) | Haystack chat history for conversational agents. |
| [LlamaIndex Contextual Retrieval](https://docs.llamaindex.ai/en/stable/examples/retrieval/contextual_retrieval/) | Contextual retrieval for better memory recall (Anthropic recipe). |
| [Contextual AI (Glean)](https://www.glean.com/blog/contextual-retrieval) | Glean contextual retrieval architecture for enterprise memory. |
| [MemMachine](https://github.com/memmachine/memmachine) | MemMachine open memory machine for agents. |
| [Kendra Memory Connector](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) | Amazon Kendra as enterprise memory connector for Bedrock. |
| [Azure AI Search Memory](https://learn.microsoft.com/en-us/azure/search/search-how-to-semantic-search) | Azure AI Search semantic memory for agents. |
| [Google Memory Bank](https://cloud.google.com/vertex-ai/generative-ai/docs/memory-bank) | Vertex AI Memory Bank for agents (preview). |
| [LangChain Chat Message History](https://python.langchain.com/docs/how_to/message_history/) | LangChain message history patterns for stateful agents. |

## AI agent protocols and interoperability (38)

| Resource | Useful for / constraints |
|---|---|
| [Model Context Protocol Spec](https://modelcontextprotocol.io/specification/2025-03-26) | MCP 2025-03-26 spec: tools, resources, prompts, and transports. |
| [Agent-to-Agent (A2A) Google](https://google.github.io/A2A/) | Google's A2A protocol for agent interoperability: discovery and task delegation. |
| [Agent Communication Protocol (ACP) IBM Bee](https://github.com/i-am-bee/acp) | IBM Bee's ACP: REST-based protocol for agent communication. |
| [ANP — Agent Network Protocol](https://github.com/agent-network-protocol/anp) | ANP decentralized agent networking protocol. |
| [FIPA ACL](https://www.fipa.org/specs/fipa00061/) | FIPA ACL spec for agent communication — historical reference for A2A/ACP. |
| [OpenAPI for Agents](https://spec.openapis.org/oas/v3.1.0.html) | OpenAPI 3.1 for describing agent tool APIs — MCP tools often wrap OAS. |
| [JSON-RPC 2.0](https://www.jsonrpc.org/specification) | JSON-RPC 2.0 underlying MCP and many agent transports. |
| [CloudEvents](https://cloudevents.io/) | CloudEvents spec for agent event envelopes across systems. |
| [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) | VCs for agent identity and delegated authority. |
| [OAuth 2.1 for Agents](https://oauth.net/2.1/) | OAuth 2.1 for agent authentication to tools and MCP servers. |
| [SPIFFE/SPIRE](https://spiffe.io/docs/latest/spiffe-about/overview/) | SPIFFE for workload identity among agent services. |
| [OpenID Connect](https://openid.net/developers/how-connect-works/) | OIDC for agent user authentication flows. |
| [DID Spec (W3C)](https://www.w3.org/TR/did-core/) | Decentralized identifiers for agent identity. |
| [Agent Cards (A2A)](https://google.github.io/A2A/specification/#5-agent-card) | A2A Agent Card for capability discovery. |
| [MCP Authorization Spec](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) | MCP authorization for OAuth-protected servers. |
| [MCP Sampling Spec](https://modelcontextprotocol.io/specification/2025-03-26/server/sampling) | MCP sampling: servers request LLM completions via client. |
| [Tool Calling (OpenAI)](https://platform.openai.com/docs/guides/function-calling) | OpenAI tool calling spec for agent interoperability. |
| [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) | Anthropic tool use spec for Claude agents. |
| [Google Function Calling](https://ai.google.dev/gemini-api/docs/function-calling) | Gemini function calling spec with parallel calls. |
| [Llama Stack](https://llama-stack.readthedocs.io/en/latest/) | Meta Llama Stack for standardized inference, safety, and agent APIs. |
| [Vercel AI SDK Tool Calling](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling) | Vercel AI SDK tool calling patterns for TS agents. |
| [LangChain Tool Calling](https://python.langchain.com/docs/how_to/tool_calling/) | LangChain unified tool calling across providers. |
| [Semantic Kernel Plugins](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins) | SK plugins: OpenAPI and native functions as agent tools. |
| [AutoGen Tool Use](https://microsoft.github.io/autogen/docs/reference/agentchat/conversational_agent/) | AutoGen conversational agent tool-use docs. |
| [CrewAI Tools Spec](https://docs.crewai.com/tools/creating-tools) | CrewAI tool creation spec for custom agent tools. |
| [Pydantic AI Tools](https://ai.pydantic.dev/tools/) | Pydantic AI tool definition with validation. |
| [OpenAI Assistants API (legacy)](https://platform.openai.com/docs/assistants/overview) | Assistants API (legacy) tool and thread model — compare to new Responses API. |
| [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) | OpenAI Responses API: stateful tool calling successor to Assistants. |
| [Anthropic Workspaces (beta)](https://docs.anthropic.com/en/docs/build-with-claude/workspaces) | Workspaces for multi-agent file collaboration (beta). |
| [Smolagents Tool Spec](https://huggingface.co/docs/smolagents/en/reference/tools) | Smolagents tool spec: Python functions as tools. |
| [Mastra Tools](https://mastra.ai/en/docs/tools/overview) | Mastra tool definitions for TS agents. |
| [BeeAI Framework Tools](https://framework.beeai.dev/tools) | BeeAI tool interface for IBM's agent framework. |
| [Strands Tools](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/) | Strands tool spec for Bedrock agents. |
| [Google ADK Tools](https://google.github.io/adk-docs/tools/) | Google ADK tool definitions for Python/Go agents. |
| [Haystack Tools](https://docs.haystack.deepset.ai/docs/tools) | Haystack tool integration for agents. |
| [LlamaIndex Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/) | LlamaIndex tool spec for query engines as tools. |
| [E2B Tool (Code Execution)](https://e2b.dev/docs/code-interpreting/overview) | E2B code execution tool: sandboxed Python for agents. |
| [Browserbase Tool](https://docs.browserbase.com/integrations/mcp) | Browserbase tool for browser control via MCP. |

## AI coding agents and assistants (64)

| Resource | Useful for / constraints |
|---|---|
| [Muse Chat](https://github.com/features/copilot) | Muse chat, completions, and agent mode in VS Code/ JetBrains — industry standard. |
| [Muse Workspace](https://docs.github.com/en/copilot/copilot-workspace) | Copilot Workspace: plan tasks from issues and open PRs with agentic coding. |
| [Cursor](https://docs.cursor.com/) | Cursor: AI-first IDE with agent mode, codebase understanding, and MCP. |
| [Windsurf (Codeium)](https://docs.codeium.com/windsurf) | Windsurf editor: Cascade agent with tool calling and codebase awareness. |
| [Muse](https://docs.ampcode.com/) | Amp: agentic coding with Oracle, plan, and subagent delegation. |
| [Aider](https://aider.chat/) | Terminal pair-programmer with Git integration and repomap — bring your own model. |
| [Cline](https://docs.cline.bot/) | Autonomous coding agent for VS Code with MCP, computer use, and plan/act modes. |
| [Roo Code](https://docs.roocode.com/) | Roo Code (Cline fork) with modes, MCP marketplace, and VS Code integration. |
| [OpenHands (All-Hands)](https://docs.all-hands.dev/) | OpenHands cloud and self-host: autonomous coding agents via code execution sandboxes. |
| [SWE-agent](https://swe-agent.com/latest/) | Princeton SWE-agent for resolving GitHub issues with LLM agents and tools. |
| [Devin (Cognition)](https://devin.ai/) | Devin AI software engineer: autonomous PRs with browser, shell, and code execution. |
| [Replit Agent](https://docs.replit.com/replitai/agent) | Replit Agent: natural-language app builder with deployment. |
| [v0 by Vercel](https://v0.dev/docs) | v0 generative UI: prompt to React/Tailwind components with shadcn. |
| [Bolt.new (StackBlitz)](https://support.stackblitz.com/docs/bolt/overview) | Bolt.new: prompt-to-fullstack with WebContainers and deployment. |
| [Lovable](https://docs.lovable.dev/) | Lovable: AI app builder for web apps with Supabase integration. |
| [Anthropic Claude Code](https://code.claude.com/docs) | Claude Code: Anthropic's terminal agent with subagents, hooks, and MCP. |
| [OpenAI Codex (CLI)](https://developers.openai.com/codex/cli) | OpenAI Codex CLI: terminal coding agent with shell and MCP support. |
| [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) | Amazon Q: coding, chat, and AWS actions in IDE and CLI. |
| [Amazon CodeWhisperer (legacy)](https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is-cwspr.html) | Legacy CodeWhisperer docs — now part of Amazon Q. |
| [Tabnine](https://docs.tabnine.com/) | Tabnine: privacy-focused code completion with self-hosted options. |
| [Codeium](https://codeium.com/documentation) | Codeium completions and chat: free tier for individuals. |
| [Sourcegraph Cody](https://sourcegraph.com/docs/cody) | Cody: chat and completions grounded in your codebase graph. |
| [Codeium Windsurf Cascade](https://docs.codeium.com/windsurf/cascade) | Cascade agent docs for Windsurf's tool-calling agent. |
| [Qwen Code (Qwen-Coder)](https://github.com/QwenLM/Qwen-Agent) | Qwen-Agent and Qwen-Coder for code tasks with tool use. |
| [DeepSeek Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek Coder V2: 236B MoE for coding and function calling. |
| [StarCoder 2](https://github.com/bigcode-project/starcoder2) | BigCode StarCoder2 open code models — training data transparency. |
| [CodeLlama](https://github.com/meta-llama/codellama) | Meta Code Llama for code generation, infilling, and chat. |
| [MagicCode](https://github.com/magicai-lab/magiccode) | Magic's code models for long-context reasoning. |
| [Devstral (Mistral)](https://docs.mistral.ai/capabilities/code_generation) | Mistral Devstral code generation docs. |
| [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist) | Google Gemini Code Assist in IDE and Cloud Workstations. |
| [JetBrains AI Assistant](https://www.jetbrains.com/help/ai-assistant/) | JetBrains AI: completions, chat, and VCS-aware assistance across IDEs. |
| [Visual Studio IntelliCode](https://learn.microsoft.com/en-us/visualstudio/intellicode/overview) | IntelliCode completions for Visual Studio. |
| [CodeGeeX](https://github.com/THUDM/CodeGeeX) | THUDM CodeGeeX multilingual code generation. |
| [Granite Code (IBM)](https://github.com/ibm-granite/granite-code-models) | IBM Granite code models for enterprise code tasks. |
| [StarcoderBase](https://huggingface.co/bigcode/starcoderbase) | StarCoderBase model card and usage. |
| [SWE-bench Verified](https://www.swebench.com/verified.html) | SWE-bench Verified: human-verified solvable GitHub issues for coding agents. |
| [SWE-bench Lite](https://www.swebench.com/lite.html) | SWE-bench Lite: smaller, cheaper split for quick iteration. |
| [LiveCodeBench](https://livecodebench.github.io/) | LiveCodeBench: contamination-free code generation benchmark from live contests. |
| [EvalPlus](https://github.com/evalplus/evalplus) | EvalPlus: rigorous HumanEval+ and MBPP+ with mutation tests. |
| [BigCodeBench](https://bigcode-bench.github.io/) | BigCodeBench: diverse function-level code generation benchmark. |
| [Aider Leaderboard](https://aider.chat/docs/leaderboards/) | Aider's code editing leaderboard: model vs. edit success and cost. |
| [DevQualityEval](https://github.com/microsoft/DevQualityEval) | Microsoft DevQualityEval for code generation evaluation. |
| [CodeContests](https://github.com/deepmind/code_contests) | DeepMind CodeContests dataset for competition-level code. |
| [APPS](https://github.com/hendrycks/apps) | APPS benchmark for introductory/competition Python problems. |
| [MHPP](https://github.com/SyzygyLab/MHPP) | Mostly Hard Python Problems for advanced code reasoning. |
| [CruxEval](https://github.com/facebookresearch/cruxeval) | CruxEval: input-output reasoning for code execution. |
| [RepoBench](https://github.com/Leolty/repobench) | Repository-level code completion benchmark. |
| [CrossCodeEval](https://github.com/cxcscmu/CrossCodeEval) | Cross-file code completion benchmark. |
| [Stack Eval (SWE-Arena)](https://swe-arena.com/) | Crowdsourced SWE Arena rankings for coding models. |
| [Void (Cline fork)](https://github.com/voideditor/void) | Void editor fork focused on agent workflows. |
| [PearAI](https://docs.pearai.co/) | PearAI: AI-powered code editor fork with agents. |
| [Zed AI](https://zed.dev/docs/ai/overview) | Zed editor AI: completions, chat, and collaborator. |
| [Helix (Harness)](https://docs.helix.ml/) | Helix: open-source RAG and agent platform for code. |
| [GitButler](https://docs.gitbutler.com/) | GitButler: Git client with virtual branches — useful for agent-managed patches. |
| [Graphite](https://graphite.dev/docs) | Graphite: stacked PR workflow for agent-generated code. |
| [CodeRabbit](https://docs.coderabbit.ai/) | CodeRabbit: AI code review with ast-grep and context-aware comments. |
| [Greptile](https://docs.greptile.com/) | Greptile: AI code review grounded in full codebase history. |
| [Sourcery](https://docs.sourcery.ai/) | Sourcery: automated code review and refactoring suggestions. |
| [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) | SWE-bench paper: benchmark for coding agents fixing real issues — standard for coder evals. |
| [Code Llama: Open Foundation Models for Code](https://arxiv.org/abs/2308.12950) | Code Llama report: code-specialized Llama variants for coding assistants. |
| [StarCoder: may the source be with you!](https://arxiv.org/abs/2305.06161) | StarCoder: open code LLM trained on The Stack — transparency for code model choice. |
| [DeepSeek-Coder: When the Large Language Model Meets Programming](https://arxiv.org/abs/2401.14196) | DeepSeek-Coder report: 236B MoE for code and function calling. |
| [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://arxiv.org/abs/2403.07974) | LiveCodeBench: contamination-free code eval from live contests. |
| [EvalPlus: Benchmarking Code Generation with Extended Tests](https://arxiv.org/abs/2305.01210) | EvalPlus: HumanEval+ with 80x more tests for rigorous code generation eval. |

## AI data and annotation (34)

| Resource | Useful for / constraints |
|---|---|
| [Scale AI Platform](https://docs.scale.com/docs) | Scale AI for data labeling, RLHF, and model evaluation at scale. |
| [Labelbox](https://docs.labelbox.com/docs) | Labelbox platform for data labeling and model-assisted annotation. |
| [Label Studio](https://labelstud.io/guide/get_started) | Open-source Label Studio for flexible annotation with ML-assisted workflows. |
| [Argilla](https://argilla.io/docs/practical-guides/practical-guides) | Argilla for human-in-the-loop feedback and dataset curation. |
| [Prodigy (Explosion)](https://prodi.gy/docs) | Prodigy annotation tool with active learning for NLP. |
| [Doccano](https://github.com/doccano/doccano) | Open-source Doccano for text annotation. |
| [CVAT](https://docs.cvat.ai/docs/enterprise/) | CVAT for image/video annotation — self-hosted. |
| [Roboflow](https://docs.roboflow.com/) | Roboflow for dataset management and computer vision annotation. |
| [Hugging Face AutoTrain](https://huggingface.co/docs/autotrain/index) | AutoTrain for no-code fine-tuning on your data. |
| [Snorkel AI](https://docs.snorkel.ai/) | Snorkel programmatic labeling with labeling functions. |
| [Cleanlab Studio](https://cleanlab.ai/blog/cleanlab-studio) | Cleanlab Studio for finding and fixing label errors. |
| [Great Expectations](https://docs.greatexpectations.io/docs/core/introduction/) | GE for data validation in ML pipelines. |
| [WhyLogs (WhyLabs)](https://whylabs.github.io/whylogs/) | WhyLogs for data logging and drift detection. |
| [Evidently AI Data Drift](https://docs.evidentlyai.com/user-guide/monitoring/data_drift) | Evidently for data drift and data quality. |
| [Monte Carlo](https://docs.getmontecarlo.com/docs) | Monte Carlo data observability for pipeline reliability. |
| [dbt](https://docs.getdbt.com/docs/introduction) | dbt for transforming data in warehouse for ML features. |
| [Airbyte](https://docs.airbyte.com/) | Airbyte for ELT connectors to feed RAG and training data. |
| [Fivetran](https://fivetran.com/docs) | Fivetran managed connectors for data ingestion. |
| [Dagster Assets](https://docs.dagster.io/concepts/assets/software-defined-assets) | Dagster software-defined assets for data pipelines. |
| [Prefect Dataflows](https://docs.prefect.io/latest/concepts/flows/) | Prefect flows for data ingestion for LLMs. |
| [Hugging Face Datasets Server](https://huggingface.co/docs/datasets-server) | Datasets Server for previewing 10k datasets. |
| [Kaggle Datasets](https://www.kaggle.com/docs/datasets) | Kaggle datasets hub for training and eval data. |
| [Anthropic HH-RLHF](https://github.com/anthropics/hh-rlhf) | Anthropic HH-RLHF dataset for helpful/harmless training. |
| [UltraFeedback](https://github.com/OpenBMB/UltraFeedback) | UltraFeedback for RLHF preference data. |
| [ShareGPT](https://sharegpt.com/) | ShareGPT dataset (check license) for instruction tuning. |
| [OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca) | OpenOrca dataset for instruction fine-tuning. |
| [Dolly 15k](https://github.com/databrickslabs/dolly) | Databricks Dolly 15k open instruction dataset. |
| [Alpaca Dataset](https://github.com/tatsu-lab/stanford_alpaca) | Stanford Alpaca 52k instruction dataset. |
| [Self-Instruct](https://github.com/yizhongw/self-instruct) | Self-Instruct paper code for generating instruction data. |
| [Label Studio Documentation (Heartex)](https://labelstud.io/guide#fallback-61) | Label Studio docs: RLHF and eval annotation workflows — flexible open-source labeling. |
| [Argilla: Iterative Approach for Building Datasets](https://github.com/argilla-io/argilla) | Argilla repo: human-in-the-loop dataset curation for eval and RLHF. |
| [DVC: Data Version Control for ML](https://dvc.org/doc#fallback-63) | DVC docs: Git for data and models — versioning for training pipelines. |
| [Hugging Face Datasets: A Community Library](https://arxiv.org/abs/2109.02846) | Datasets paper: 10k datasets library with Arrow and streaming — standard for data ingestion. |
| [Cleaning Data with Cleanlab](https://github.com/cleanlab/cleanlab) | Cleanlab repo: find label errors in datasets for eval cleaning. |

## AI evaluation observability and guardrails (58)

| Resource | Useful for / constraints |
|---|---|
| [HELM (Stanford)](https://crfm.stanford.edu/helm/latest/) | HELM holistic evaluation for language models across scenarios. |
| [Open LLM Leaderboard v2](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | Hugging Face Open LLM Leaderboard v2 with contamination checks. |
| [Chatbot Arena Leaderboard](https://lmarena.ai/?leaderboard) | Human-vote Elo leaderboard — real preference over static benchmarks. |
| [MMLU (Hendrycks)](https://github.com/hendrycks/test) | MMLU 57-task benchmark for language understanding. |
| [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) | Harder MMLU-Pro with 10 options and reasoning. |
| [GPQA](https://github.com/idavidrein/gpqa) | GPQA: graduate-level science questions — hard for frontier models. |
| [MATH](https://github.com/hendrycks/math) | MATH dataset for quantitative reasoning. |
| [GSM8K](https://github.com/openai/grade-school-math) | GSM8K grade-school math word problems. |
| [LiveBench](https://livebench.ai/#/) | LiveBench: continuously updated, contamination-resistant benchmark. |
| [SimpleQA (OpenAI)](https://github.com/openai/simple-evals) | OpenAI SimpleQA for factuality. |
| [FACTS Grounding](https://www.kaggle.com/competitions/facts-grounding) | Kaggle FACTS grounding leaderboard for RAG. |
| [IFEval](https://github.com/google-research/google-research/tree/master/instruction_following_eval) | Instruction-following evaluation with verifiable constraints. |
| [WildBench](https://wildbench.github.io/) | WildBench for human-aligned evaluation on wild prompts. |
| [AlpacaEval 2](https://tatsu-lab.github.io/alpaca_eval/) | AlpacaEval 2: win-rate vs GPT-4 Turbo with length control. |
| [MixEval](https://mixeval.github.io/) | MixEval: mixed real-world benchmark with ground truth. |
| [BIG-Bench Hard](https://github.com/suzgunmirac/BIG-Bench-Hard) | BBH 23 challenging BIG-Bench tasks. |
| [ARC Prize](https://arcprize.org/) | ARC Prize for abstract reasoning — frontier for AGI claims. |
| [SEAL Leaderboards](https://scale.com/leaderboard) | Scale SEAL leaderboards: instruction following, tool use, etc. |
| [Scale Spellbook](https://scale.com/spellbook) | Scale Spellbook for evaluating and red-teaming models. |
| [Arize Phoenix Evals](https://docs.arize.com/phoenix/evaluation) | Phoenix evaluation templates: hallucination, QA, toxicity. |
| [WhyLabs LangKit UDFs](https://github.com/whylabs/langkit/blob/main/langkit/docs/features.md) | LangKit UDFs for injection, jailbreak, and sentiment. |
| [Giskard Scan](https://docs.giskard.ai/en/latest/guides/scan/index.html) | Giskard scan for LLM vulnerabilities: hallucination, bias. |
| [Deepchecks](https://docs.deepchecks.com/) | Deepchecks for continuous validation of LLM and ML pipelines. |
| [TruLens](https://www.trulens.org/trulens_eval/getting_started/) | TruLens for RAG triad: context relevance, groundedness, answer relevance. |
| [Promptfoo](https://www.promptfoo.dev/docs/getting-started/) | Promptfoo: open-source evals with red-teaming and CI. |
| [Inspect (UK AISI)](https://inspect.ai-safety-institute.org.uk/) | UK AISI Inspect for model safety evaluations. |
| [EleutherAI LM Harness](https://github.com/EleutherAI/lm-evaluation-harness) | Standard harness for 60+ LLM benchmarks. |
| [HELMET (RAG Long Context)](https://github.com/princeton-nlp/HELMET) | HELMET for long-context and RAG evaluation. |
| [RULER](https://github.com/NVIDIA/RULER) | NVIDIA RULER for long-context retrieval and reasoning. |
| [Needle in a Haystack (Greg Kamradt)](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | NIAH synthetic recall benchmark for long context. |
| [LongBench](https://github.com/THUDM/LongBench) | LongBench for long-context understanding across tasks. |
| [ZeroSpan](https://github.com/mit-llm/zerospan) | Zero-span retrieval eval for RAG. |
| [ARES (Stanford)](https://github.com/stanford-futuredata/ARES) | ARES: automated RAG evaluation with synthetic data. |
| [Patronus FinanceBench](https://github.com/patronus-ai/FinanceBench) | FinanceBench for financial QA grounding. |
| [HaluEval](https://github.com/RUCAIBox/HaluEval) | HaluEval for hallucination detection across tasks. |
| [FaithScore](https://github.com/bwanglzu/FaithScore) | FaithScore for fine-grained faithfulness of LLM responses. |
| [Toxicity (Perspective API)](https://developers.perspectiveapi.com/s/docs) | Perspective API for toxicity scoring — guardrail primitive. |
| [Llama Guard 3](https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Guard3) | Meta Llama Guard 3 for input/output safety classification. |
| [ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma) | Google ShieldGemma safety classifier for Gemma. |
| [WildGuard](https://github.com/allenai/wildguard) | AllenAI WildGuard for harm detection. |
| [NVIDIA NeMo Guardrails Toolkit](https://github.com/NVIDIA/Nemo-Guardrails) | Programmable rails: topical, execution, and moderation. |
| [Guardrails AI Hub](https://hub.guardrailsai.com/) | Guardrails Hub validators: PII, regex, and JSON schema enforcement. |
| [Pydantic Validations](https://docs.pydantic.dev/latest/concepts/validators/) | Pydantic validators for structured-output guardrails. |
| [Great Expectations for LLM](https://greatexpectations.io/blog/llm-validation) | GE patterns for LLM data validation. |
| [Cleanlab](https://cleanlab.ai/blog/data-centric-ai/) | Cleanlab for finding label errors — useful for eval dataset cleaning. |
| [Argilla](https://argilla.io/docs/) | Argilla for data annotation and human-in-the-loop evals. |
| [Label Studio](https://labelstud.io/guide) | Label Studio for RLHF and eval annotation workflows. |
| [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | HELM paper: holistic scenarios for LLM evaluation beyond single benchmarks. |
| [MMLU: Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) | MMLU: 57 tasks for broad language understanding — standard for model reports. |
| [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://arxiv.org/abs/2311.12022) | GPQA: hard science questions that remain challenging for frontier models. |
| [MATH: Quantitative Reasoning (Hendrycks MATH)](https://arxiv.org/abs/2103.03874) | Hendrycks MATH: 12.5k competition problems for quantitative reasoning eval. |
| [GSM8K: Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) | GSM8K: grade-school math word problems for reasoning and verifier training. |
| [IFEval: Instruction-Following Evaluation for Large Language Models](https://arxiv.org/abs/2311.07911) | IFEval: verifiable instruction following with constraints. |
| [SimpleQA: Measuring Short-Form Factuality (OpenAI)](https://arxiv.org/abs/2411.04368) | SimpleQA: short-form factuality with human-verified answers. |
| [WhyLabs LangKit Documentation (injection UDFs)](https://github.com/whylabs/langkit#fallback-57) | WhyLabs LangKit repo: injection, jailbreak, and quality UDFs for LLM monitoring. |
| [Giskard: Evaluation and Testing for ML Models](https://github.com/Giskard-AI/giskard) | Giskard open-source: LLM scan for hallucination, bias, and robustness. |
| [TruLens Eval: Feedback Functions for LLM Apps](https://github.com/truera/trulens) | TruLens repo: RAG triad evaluation with groundedness and relevance. |
| [Promptfoo: Test Your LLM App Locally (Red Team)](https://github.com/promptfoo/promptfoo) | Promptfoo repo: open-source evals with red-teaming and CI. |

## AI learning and references (34)

| Resource | Useful for / constraints |
|---|---|
| [Deep Learning Specialization (Coursera)](https://www.deeplearning.ai/courses/deep-learning-specialization/) | Andrew Ng's 5-course DLS — foundation for DL and LLM intuition. |
| [LLM University (Cohere)](https://docs.cohere.com/docs/llm-university) | Cohere LLM University for LLM concepts and prompt engineering. |
| [Hugging Face Course](https://huggingface.co/course/chapter1/1) | HF course: transformers, datasets, and diffusion from scratch. |
| [Stanford CS229](https://cs229.stanford.edu/) | Stanford CS229 ML notes and lectures — theory behind LLM training. |
| [Stanford CS230](https://cs230.stanford.edu/) | Stanford CS230 deep learning lectures (Kian Katanforoosh). |
| [Andrej Karpathy — Neural Nets Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Karpathy's series: micrograd to GPT from scratch in Python. |
| [Andrej Karpathy — LLM101n](https://github.com/karpathy/LLM101n) | LLM101n: build a tiny LLM story-teller from scratch. |
| [3Blue1Brown — Neural Networks](https://www.3blue1brown.com/topics/neural-networks) | Visual intro to neural nets — strong for intuition. |
| [Lilian Weng — LLM Blog](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) | Lilian Weng's LLM prompt engineering survey — thorough. |
| [Sebastian Raschka — LLM Book](https://sebastianraschka.com/books/#build-a-large-language-model-from-scratch) | Build a Large Language Model from Scratch — from data to pretraining. |
| [Chip Huyen — AI Engineering](https://huyenchip.com/books/) | Chip Huyen's AI Engineering and Designing ML Systems books. |
| [Aman AI — LLM Training Handbook](https://aman.ai/primers/ai/) | Aman Arora's LLM training primer: pretrain, SFT, RLHF. |
| [Made With ML](https://madewithml.com/) | Goku Mohandas' MLOps course: from model to production. |
| [Eugene Yan — Patterns](https://eugeneyan.com/writing/patterns/) | Eugene Yan's ML system patterns — practical for agent architecture. |
| [Hamels — LLM Evals](https://hamel.dev/notes/llm/evaluation/) | Hamel Husain's eval guides for LLM apps. |
| [Hamel — RAG](https://hamel.dev/blog/posts/rag/) | Hamel's RAG failure modes and remedies. |
| [Pinterest — Learned Retrieval](https://medium.com/pinterest-engineering) | Pinterest engineering blog: learned retrieval and ranking. |
| [Netflix Tech Blog — ML](https://netflixtechblog.com/tagged/machine-learning) | Netflix ML papers and systems for recommendation and inference. |
| [OpenAI Cookbook](https://cookbook.openai.com/) | OpenAI Cookbook: copy-paste LLM recipes with code. |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) | Anthropic Cookbook for Claude tool use and prompting. |
| [AWS ML Learning Path](https://aws.amazon.com/training/learn-about/machine-learning/) | AWS ML learning path: SageMaker, Bedrock, and MLOps. |
| [Azure AI Fundamentals](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/) | Azure AI fundamentals path for platform certification. |
| [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) | Google's MLCC: 15 hours of ML fundamentals with TensorFlow. |
| [Kaggle Learn — Intro to DL](https://www.kaggle.com/learn/intro-to-deep-learning) | Kaggle DL micro-courses with notebooks. |
| [Kaggle Learn — LLM Prompting](https://www.kaggle.com/learn/prompt-engineering) | Kaggle prompt engineering tutorials. |
| [Fast.ai — LLM from Scratch](https://course.fast.ai/Resources/book.html) | Fast.ai book: Deep Learning for Coders with PyTorch. |
| [Probabilistic ML (Murphy)](https://probml.github.io/pml-book/) | Kevin Murphy's Probabilistic ML book — free PDF for fundamentals. |
| [Dive into Deep Learning](https://d2l.ai/) | D2L interactive DL book with code in PyTorch/MXNet/JAX. |
| [Made With ML: MLOps Course](https://madewithml.com/#fallback-66) | Goku Mohandas MLOps course: from model to production with CI/CD. |
| [Deep Learning Specialization Notes (Coursera)](https://www.deeplearning.ai/courses/) | DeepLearning.AI courses hub: DLS and LLM specializations for foundations. |
| [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) | Stanford CS224N lectures and notes: NLP and LLM fundamentals. |
| [Karpathy: Let's build GPT from scratch](https://github.com/karpathy/nanoGPT#fallback-69) | Karpathy nanoGPT: build GPT-2 from scratch in PyTorch — educational for LLM training. |
| [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/#fallback-70) | Illustrated Transformer visual guide: self-attention and positional encoding for intuition. |
| [Sebastian Raschka: Build a Large Language Model From Scratch](https://github.com/rasbt/LLMs-from-scratch#fallback-71) | Raschka LLM-from-scratch repo: data to pretraining with PyTorch. |

## AI machine learning and local inference (77)

| Resource | Useful for / constraints |
|---|---|
| [Llama.cpp](https://github.com/ggerganov/llama.cpp) | Efficient C++ inference for Llama-family models on CPU/GPU with quantization — the backbone for many local tools. |
| [GGML](https://github.com/ggerganov/ggml) | Tensor library for machine learning — underpins llama.cpp and whisper.cpp. |
| [Transformers (Hugging Face)](https://github.com/huggingface/transformers) | State-of-the-art transformers in PyTorch/TensorFlow/JAX — model zoo and training recipes. |
| [Diffusers](https://github.com/huggingface/diffusers) | Diffusion models: Stable Diffusion, Flux, SDXL pipelines and training scripts. |
| [PEFT](https://github.com/huggingface/peft) | Parameter-efficient fine-tuning: LoRA, QLoRA, AdaLoRA, prefix tuning for LLMs. |
| [TRL](https://github.com/huggingface/trl) | Transformer reinforcement learning: SFT, DPO, PPO, and GRPO post-training for LLMs. |
| [Accelerate](https://github.com/huggingface/accelerate) | Run PyTorch training at scale across distributed setups with minimal code changes. |
| [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) | GPTQ quantization for LLMs — 4-bit inference with minimal quality loss. |
| [GPTQModel](https://github.com/ModelCloud/GPTQModel) | Modern GPTQ library supporting latest models and Marlin kernels. |
| [ExLlama v2](https://github.com/turboderp/exllamav2) | Fast inference for GPTQ/EXL2 quants with high throughput. |
| [vLLM](https://github.com/vllm-project/vllm) | PagedAttention LLM serving with continuous batching — throughput-optimized inference server. |
| [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) | Hugging Face's Rust+Python LLM serving with tensor parallelism and quantization. |
| [MLX-LM](https://github.com/ml-explore/mlx-examples) | MLX examples: LLM inference and fine-tuning on Apple Silicon. |
| [TVM](https://tvm.apache.org/docs/) | Compiler for ML models across hardware backends (TVM/VTA). |
| [Triton Inference Server](https://github.com/triton-inference-server/server) | NVIDIA Triton for serving any model (PyTorch, ONNX, TensorRT) with dynamic batching. |
| [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) | Scalable model serving on Ray for Python models and LLM chains. |
| [BentoML](https://docs.bentoml.com/) | Model serving framework: package any model into REST/gRPC service with adaptive batching. |
| [KServe](https://kserve.github.io/website/) | Kubernetes-native model inference platform (K8s CRDs for model serving). |
| [Kubeflow](https://www.kubeflow.org/docs/) | ML workflows on Kubernetes: training, pipelines, Katib, and KServe integration. |
| [ClearML](https://clear.ml/docs) | Open-source MLOps: experiment manager, data, and orchestration. |
| [Neptune.ai](https://docs.neptune.ai/) | Experiment tracking for ML/ LLM experiments with rich visualizations. |
| [Comet ML](https://www.comet.com/docs/) | Experiment tracking and model production monitoring. |
| [Optuna](https://optuna.org/) | Hyperparameter optimization framework — pruning and distributed search. |
| [Ray Tune](https://docs.ray.io/en/latest/tune/index.html) | Scalable hyperparameter tuning built on Ray. |
| [PyTorch](https://pytorch.org/docs/stable/index.html) | PyTorch 2.x core, torch.compile, and distributed docs. |
| [JAX](https://jax.readthedocs.io/en/latest/) | JAX: composable transforms for NumPy on accelerators; powers Gemma and many research models. |
| [Flax](https://flax.readthedocs.io/en/latest/) | Flax (JAX) for high-performance neural nets. |
| [Keras 3](https://keras.io/) | Keras 3 with PyTorch/JAX/TensorFlow backends — multi-backend model authoring. |
| [Lightning AI](https://lightning.ai/docs/overview) | PyTorch Lightning and Lightning Fabric for scale training without boilerplate. |
| [DeepSpeed](https://www.deepspeed.ai/docs/) | Microsoft DeepSpeed for large-model training: ZeRO, offload, and inference optimizations. |
| [Colossal-AI](https://colossalai.org/docs/) | Large-model training system with heterogeneous parallelism. |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's large language model training with tensor/pipeline parallelism. |
| [Liger Kernel](https://github.com/linkedin/Liger-Kernel) | Efficient Triton kernels for LLM training (RoPE, SwiGLU, RMSNorm). |
| [FlashAttention](https://github.com/Dao-AILab/flash-attention) | IO-aware exact attention — enables long-context training and inference. |
| [xFormers](https://github.com/facebookresearch/xformers) | Meta's transformer building blocks: memory-efficient attention and kernels. |
| [Hugging Face Optimum](https://huggingface.co/docs/optimum/index) | Optimize transformers for ONNX, OpenVINO, Habana — quantization and pruning. |
| [Neural Compressor (Intel)](https://github.com/intel/neural-compressor) | Intel's tool for quantization, pruning, and distillation on Intel hardware. |
| [OpenLLM](https://github.com/bentoml/OpenLLM) | Serve any open LLM with BentoML backend — OpenAI-compatible API. |
| [LocalAI](https://localai.io/docs/) | Drop-in OpenAI-compatible API for running many models locally (Llama.cpp, Diffusers). |
| [LM Studio](https://lmstudio.ai/docs) | Desktop app for discovering and running local LLMs with OpenAI-compatible server. |
| [Jan](https://jan.ai/docs) | Open-source ChatGPT alternative that runs 100% offline with extension ecosystem. |
| [GPT4All](https://docs.gpt4all.io/) | Run open LLMs locally via Python and desktop chat — offline RAG support. |
| [KoboldCpp](https://github.com/LostRuins/koboldcpp) | Easy local LLM server with KoboldAI UI and API, optimized for storytelling. |
| [Aphrodite Engine](https://github.com/PygmalionAI/aphrodite-engine) | Large-scale LLM inference fork optimized for roleplay and Pygmalion models. |
| [Tabby](https://tabby.tabbyml.com/docs/welcome) | Self-hosted AI coding assistant (like Copilot) with OpenAPI spec. |
| [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) | Port of OpenAI Whisper for efficient speech-to-text locally. |
| [Piper TTS](https://github.com/rhasspy/piper) | Fast local neural TTS — excellent for offline voice agents. |
| [Stable Diffusion WebUI (AUTOMATIC1111)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Feature-rich Gradio UI for Stable Diffusion with extensions. |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | Node-based UI for Stable Diffusion, Flux, and video workflows. |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Simple, Midjourney-like UI for SDXL — great for non-technical users. |
| [InvokeAI](https://invoke-ai.github.io/InvokeAI/) | Professional Stable Diffusion toolkit with canvas and batch features. |
| [Oobabooga TextGen WebUI](https://github.com/oobabooga/text-generation-webui) | Gradio UI for many LLM backends (Transformers, llama.cpp, ExLlama). |
| [Hugging Face Datasets](https://huggingface.co/docs/datasets) | Datasets library: 10k+ datasets with streaming and Arrow backend. |
| [Datasets Hub](https://huggingface.co/datasets) | Browse and filter datasets by task, license, and size. |
| [OpenAI Whisper](https://github.com/openai/whisper) | OpenAI's robust multilingual speech recognition — base for many STT pipelines. |
| [PyAnnote](https://github.com/pyannote/pyannote-audio) | Speaker diarization and segmentation — standard for meeting transcription. |
| [SpeechBrain](https://speechbrain.readthedocs.io/en/latest/) | PyTorch speech toolkit: ASR, speaker, enhancement, separation. |
| [NeMo (NVIDIA)](https://docs.nvidia.com/nemo-framework/user-guide/latest/) | NVIDIA NeMo for building ASR, TTS, and LLM on GPU. |
| [Coqui TTS](https://github.com/coqui-ai/TTS) | Coqui's open TTS and voice cloning (check fork maintenance). |
| [Edge Impulse](https://docs.edgeimpulse.com/docs) | TinyML platform for deploying models to edge devices. |
| [TensorFlow Lite](https://ai.google.dev/edge/litert) | LiteRT (TFLite) for on-device ML on mobile and microcontrollers. |
| [Core ML](https://developer.apple.com/documentation/coreml) | Apple Core ML for on-device inference on iPhone/Mac. |
| [ONNX Model Zoo](https://github.com/onnx/models) | Pretrained ONNX models across vision, NLP, and speech. |
| [Hugging Face Hub Python](https://huggingface.co/docs/huggingface_hub/index) | Hub Python library: push, download, and manage models/datasets programmatically. |
| [DVC](https://dvc.org/doc) | Data version control for ML experiments — Git for data and models. |
| [Great Expectations](https://docs.greatexpectations.io/docs/) | Data validation for ML pipelines — expectations and data docs. |
| [WhyLabs LangKit](https://github.com/whylabs/langkit) | Open-source LLM monitoring: prompt injection, toxicity, and quality signals. |
| [Giskard](https://docs.giskard.ai/) | Open-source LLM testing: robustness, bias, and vulnerability scans. |
| [DeepEval](https://docs.confident-ai.com/) | LLM evaluation framework with 15+ metrics and LLM-as-judge. |
| [Ragas](https://docs.ragas.io/en/latest/) | RAG evaluation: faithfulness, answer relevancy, context recall/precision. |
| [LangSmith](https://docs.smith.langchain.com/) | LangChain's observability and evaluation platform for LLM apps. |
| [Helicone](https://docs.helicone.ai/) | LLM observability proxy: logging, caching, rate limits, and cost tracking. |
| [PromptLayer](https://docs.promptlayer.com/) | Prompt management, versioning, and analytics for LLMs. |
| [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) | FlashAttention: IO-aware exact attention for long-context training/inference efficiency. |
| [DeepSpeed: System Optimizations Enable Training Deep Learning Models with Over 100 Billion Parameters](https://arxiv.org/abs/1910.02054) | DeepSpeed paper: ZeRO and offload for large-model training on limited GPUs. |
| [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) | vLLM paper: PagedAttention and continuous batching for high-throughput serving. |
| [QLoRA 4-bit Finetuning already covered but use AWQ paper](https://arxiv.org/abs/2306.00978) | AWQ paper: activation-aware quantization for 4-bit LLM inference with quality. |

## AI models and API providers (100)

| Resource | Useful for / constraints |
|---|---|
| [Anthropic Claude API](https://docs.anthropic.com/claude/docs) | Claude 4 family: API, prompt engineering, tool use, and extended thinking. |
| [Vertex AI Generative AI](https://cloud.google.com/vertex-ai/generative-ai/docs) | Google Cloud's managed Gemini, Claude, and open-model APIs on Vertex AI. |
| [AWS Bedrock Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html) | Managed foundation models on Bedrock: Anthropic, Meta, Mistral, Amazon Nova, and Cohere. |
| [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview) | Azure-hosted OpenAI models with enterprise controls, content filters, and VNet integration. |
| [OpenAI Models Overview](https://platform.openai.com/docs/models) | GPT-4o, o-series reasoning, and embedding models: capabilities, pricing, and rate limits. |
| [Cohere Platform](https://docs.cohere.com/v2/docs) | Command, Embed v3, Rerank 3.5, and Classify APIs for enterprise RAG. |
| [Mistral La Plateforme](https://docs.mistral.ai/capabilities) | Mistral Large, Medium, Codestral, and Pixtral via La Plateforme and Azure. |
| [GroqCloud Console](https://console.groq.com/docs/quickstart) | Ultra-fast LPU inference for Llama, Mixtral, and Gemma — check rate limits and context windows. |
| [Together AI Models](https://docs.together.ai/docs/inference-models) | Hosted open models: Llama 405B, Qwen, DeepSeek-R1 with batch and fine-tune options. |
| [Fireworks AI Models](https://docs.fireworks.ai/models) | Fast inference for 100+ open models with function calling and LoRA serving. |
| [Replicate Models](https://replicate.com/explore) | Community and official models (LLM, diffusion, audio) with one OpenAI-compatible API. |
| [OpenRouter Models](https://openrouter.ai/models) | Single API across 300+ models/ providers with automatic failover and pricing comparisons. |
| [DeepSeek Platform](https://api-docs.deepseek.com/quick_start) | DeepSeek-V3 and R1 reasoning models — OpenAI-compatible, check context and pricing. |
| [Perplexity Sonar API](https://docs.perplexity.ai/guides/getting-started) | Search-grounded answer APIs with citations for research agents. |
| [xAI Grok API](https://docs.x.ai/docs/models) | Grok 4 models with live X search grounding and OpenAI-compatible chat completions. |
| [Cerebras Inference](https://inference-docs.cerebras.ai/introduction) | Waferscale inference — highest tokens/sec for open models; check quota tiers. |
| [SambaNova Cloud](https://docs.sambanova.ai/cloud) | SambaNova's fast inference API for Llama 3.3 and Qwen with free tier. |
| [Lambda Labs Inference](https://docs.lambdalabs.com/inference) | Lambda inference API for open models on H100 clusters. |
| [Anyscale Endpoints](https://docs.anyscale.com/endpoints/overview) | Anyscale hosted open models on Ray — autoscaling and fine-tuning. |
| [OctoAI](https://octo.ai/docs) | Hosted open-model inference with media generation and efficient GPU sharing. |
| [Baseten Truss](https://docs.baseten.co/overview) | Hosted inference for custom models with autoscaling and dedicated deployments. |
| [RunPod Serverless](https://docs.runpod.io/serverless/overview) | Serverless GPU endpoints for any containerised model with autoscaling. |
| [CoreWeave Inference](https://docs.coreweave.com/inference) | CoreWeave cloud inference for large models on H100/GB200. |
| [AI21 Jamba](https://docs.ai21.com/docs/jamba-models) | AI21's Jamba (Mamba+Transformer) long-context models via AI21 Studio. |
| [Aleph Alpha Luminous](https://docs.aleph-alpha.com/docs/introduction) | Aleph Alpha's Luminous models hosted in EU with Pharia platform. |
| [Stability AI Platform](https://platform.stability.ai/docs/getting-started) | Stable Diffusion 3.5, SDXL, and Stable Audio/V Video via API. |
| [Midjourney API (unofficial docs)](https://docs.midjourney.com/docs) | Midjourney v6/v7 image generation — check official Discord/API access terms. |
| [Ideogram API](https://developer.ideogram.ai/docs) | Ideogram 2/3 for high-quality text-in-image generation. |
| [ElevenLabs API](https://elevenlabs.io/docs/api-reference/introduction) | Voice cloning, TTS, and sound effects — listed here for model provider completeness. |
| [Voyage AI Embeddings](https://docs.voyageai.com/docs/embeddings) | Voyage-3 family: general, code, finance, law embeddings and rerankers. |
| [Jina Embeddings](https://jina.ai/embeddings) | Jina embeddings v3: multilingual, code, and late-interaction ColBERT. |
| [Mixedbread AI](https://www.mixedbread.com/docs) | mxbai embeddings and rerank: strong RAG retrieval quality. |
| [Nomic Embed](https://docs.nomic.ai/atlas/embeddings) | Nomic Embed text and Atlas visualization; open weights. |
| [BAAI BGE](https://github.com/FlagOpen/FlagEmbedding) | BAAI General Embedding series: widely used open embedding and reranker models. |
| [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index) | Hosted inference via Hugging Face's provider fleet — one API across tasks. |
| [Together Fine-Tuning](https://docs.together.ai/docs/fine-tuning) | Fine-tune open models on Together with LoRA and full fine-tune recipes. |
| [Fireworks Fine-Tuning](https://docs.fireworks.ai/fine-tuning/quickstart) | Fine-tune and serve custom LoRA adapters on Fireworks. |
| [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library) | Curated prompts for Claude across tasks — good reference for prompt engineering. |
| [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | OpenAI's official prompting patterns, function calling, and structured outputs. |
| [Azure AI Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/overview) | Azure AI Foundry model catalog: OpenAI, Meta, Mistral, Cohere, and open models in one place. |
| [NVIDIA NIM Microservices](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html) | NVIDIA's optimized inference containers for LLMs, embedding, rerank, and vision on GPU. |
| [Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards) | How to read model cards for license, training data, and intended use. |
| [Papers With Code SOTA](https://paperswithcode.com/sota) | Leaderboards by task — check which dataset/split a SOTA claim uses. |
| [LMSYS Chatbot Arena](https://lmarena.ai/) | Human preference leaderboard for LLMs and vision models — Elo rankings. |
| [Vercel AI Gateway](https://vercel.com/docs/ai-sdk/gateway) | Vercel's gateway to 100+ models with observability and cost controls. |
| [Cloudflare AI](https://developers.cloudflare.com/workers-ai/) | Workers AI: 30+ open models at the edge with vectorize and R2 integration. |
| [Hugging Face Hub Inference](https://huggingface.co/docs/inference-endpoints/index) | Dedicated inference endpoints for private model deployments on HF. |
| [MiniMax API](https://www.minimax.io/platform) | MiniMax M2 and audio/video models — check pricing and language strengths. |
| [Qwen (Alibaba Cloud)](https://qwenlm.github.io/blog/) | Qwen2.5/3 family and Qwen-VL — strong open multilingual and code models. |
| [Gemma (Google)](https://ai.google.dev/gemma) | Gemma 3 open models from Google — efficient for local/edge inference. |
| [Phi-3 / Phi-4 (Microsoft)](https://azure.microsoft.com/en-us/products/phi) | Microsoft Phi small language models — excellent quality per size for edge. |
| [Llama 3.3 (Meta)](https://www.llama.com/docs/overview) | Meta Llama 3.3 models: 8B to 405B with instruct and tool-use variants. |
| [Command R+ (Cohere)](https://docs.cohere.com/docs/command-r-plus) | Cohere Command R/R+ for RAG and tool calling with long context. |
| [Claude Computer Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) | Anthropic's computer-use API for agents that interact with desktops/browsers. |
| [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) | Realtime voice API (WebRTC/WebSocket) for low-latency speech agents. |
| [Google Live API](https://ai.google.dev/api/live) | Gemini Live low-latency multimodal (speech/video) streaming API. |
| [Azure Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) | Azure AI Speech: TTS, STT, translation, and custom voices. |
| [NVIDIA Riva](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/index.html) | NVIDIA Riva for on-prem speech AI: ASR, TTS, and translation on GPU. |
| [Stability Video](https://platform.stability.ai/docs/api-reference#tag/generate) | Stability AI video generation API reference. |
| [Runway API](https://docs.dev.runwayml.com/api) | Runway Gen-3/4 video generation and editing APIs for agents. |
| [FAL AI](https://fal.ai/models) | FAL's fast inference for diffusion, Flux, SDXL, and video models. |
| [CogVideo (Zhipu)](https://www.zhipuai.cn/devcenter) | Zhipu CogVideo and ChatGLM APIs for video and chat. |
| [Baichuan API](https://platform.baichuan-ai.com/docs) | Baichuan 2 models API for Chinese-centric tasks. |
| [Yi (01.AI)](https://platform.lingyiwanwu.com/docs) | Yi-Large 34B and Yi-Vision models via 01.AI platform. |
| [Moonshot (Kimi)](https://platform.moonshot.cn/docs) | Moonshot Kimi long-context (128k-200k) chat API. |
| [StepFun (Step)](https://platform.stepfun.com/docs) | Step 1/2 models from StepFun with vision and code strengths. |
| [MiniMax Audio](https://www.minimax.io/audio-api) | MiniMax voice cloning and TTS APIs. |
| [Hume AI](https://dev.hume.ai/docs) | Empathic voice and emotion measurement APIs for expressive speech. |
| [PlayHT](https://docs.play.ht/reference/api-getting-started) | PlayHT voice generation, cloning, and conversational agents. |
| [Cartesia](https://docs.cartesia.ai/) | Cartesia Sonic: ultra-low-latency TTS for realtime agents. |
| [Deepgram](https://developers.deepgram.com/docs) | ASR, streaming STT, and voice agent APIs with low latency. |
| [AssemblyAI](https://www.assemblyai.com/docs) | Speech-to-text with speaker diarization, sentiment, and LeMUR LLM. |
| [Replicate Flux](https://replicate.com/black-forest-labs/flux-schnell) | Flux Schnell/Pro on Replicate — fast, high-quality text-to-image. |
| [Black Forest Labs](https://docs.bfl.ml/) | BFL's Flux family technical docs and API. |
| [Ideogram 3.0](https://ideogram.ai/api) | Ideogram 3.0 API for text-accurate image generation. |
| [Leonardo AI](https://docs.leonardo.ai/docs) | Leonardo's image and motion generation APIs. |
| [Midjourney Documentation](https://docs.midjourney.com/docs/quick-start) | Midjourney quick start and parameter reference — verify API availability. |
| [Pika API](https://docs.pika.art/api) | Pika Labs video generation and editing. |
| [Luma Dream Machine](https://lumalabs.ai/dream-machine/api) | Luma AI video generation API for agents. |
| [Suno AI](https://suno.com/docs) | Suno AI music generation API (if available) — verify terms. |
| [Udio](https://www.udio.com/docs) | Udio music generation service docs. |
| [Kimi K2](https://platform.moonshot.cn/docs/api/chat) | Moonshot Kimi K2 frontier chat model API. |
| [Claude Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | Anthropic prompt caching to reduce latency and cost for repeated contexts. |
| [Attention Is All You Need (Transformer)](https://arxiv.org/abs/1706.03762#fallback-0) | Foundational Transformer paper: attention mechanism underlying all modern LLMs — essential for model selection and architecture understanding. |
| [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) | BERT paper for understanding encoder models and masked LM pretraining — still relevant for embedding and classification models. |
| [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) | GPT-3 paper: scale, few-shot prompting, and emergent capabilities that define modern provider APIs. |
| [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) | GPT-4 report: multimodal capabilities, eval methodology, and alignment — reference for frontier model behavior. |
| [Llama 3 Herd of Models](https://arxiv.org/abs/2407.09288) | Meta Llama 3.1 405B report: training, instruction tuning, and tool use for open-model provider selection. |
| [Mistral 7B (Jiang et al.)](https://arxiv.org/abs/2310.06825) | Mistral 7B paper: sliding window attention and strong 7B baseline for local inference and provider routing. |
| [DeepSeek-V2: A Strong, Economical, and Efficient MoE](https://arxiv.org/abs/2405.04434) | DeepSeek-V2 MoE architecture: efficient inference for reasoning models via DeepSeek API. |
| [Phi-3 Technical Report: A Highly Capable Small Model](https://arxiv.org/abs/2404.14219) | Phi-3 small model report: quality per size for edge inference and cost-sensitive routing. |
| [Gemma 2: Improving Open Language Models](https://arxiv.org/abs/2408.00118) | Google Gemma 2 report: open models with distillation and safety — alternative to Llama for local use. |
| [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) | Alibaba Qwen2 report: multilingual and code strengths across 0.5B–72B sizes. |
| [Chinchilla: Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.02155) | Chinchilla scaling laws: optimal tokens vs parameters for training cost decisions. |
| [Scaling Laws for Neural Language Models (Kaplan)](https://arxiv.org/abs/2001.08361) | Early scaling laws paper: power-law for model size, data, and compute. |
| [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | Anthropic Constitutional AI: RL from AI feedback for Claude alignment — provider policy context. |
| [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290) | DPO paper: simpler alignment without RLHF — used by many open-model fine-tunes. |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | LoRA paper: efficient fine-tuning via low-rank adapters — basis for provider fine-tune APIs. |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | QLoRA paper: 4-bit quantization + LoRA for consumer-GPU fine-tuning — pattern for custom model deployment. |
| [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155#fallback-16) | InstructGPT paper: RLHF recipe behind OpenAI and Anthropic alignment. |

## AI prompt and context engineering (35)

| Resource | Useful for / constraints |
|---|---|
| [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Anthropic's prompt engineering overview with tools, examples, and analysis toolkit. |
| [Google Prompt Design 101](https://ai.google.dev/gemini-api/docs/prompting-intro) | Google's prompt intro for Gemini with best practices and examples. |
| [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903) | Wei et al. Chain-of-Thought prompting elicits reasoning in LLMs. |
| [ReAct Paper](https://arxiv.org/abs/2210.03629) | ReAct: synergy of reasoning and acting in LLMs for tool use. |
| [Tree-of-Thought](https://arxiv.org/abs/2305.10601) | ToT: deliberate problem solving with tree search over thoughts. |
| [Graph-of-Thought](https://arxiv.org/abs/2308.09687) | GoT: graph-structured reasoning for LLMs beyond trees. |
| [DSPy Programming](https://dspy-docs.vercel.app/) | DSPy docs for programmatic prompting and optimization without manual prompt tuning. |
| [LMQL Query Language](https://lmql.ai/docs/) | LMQL for declarative prompt programs with constraints. |
| [Instructor Prompting](https://python.useinstructor.com/concepts/prompting/) | Instructor patterns for coupling prompts with Pydantic schemas. |
| [BAML Prompt Language](https://docs.boundaryml.com/docs/home/getting-started/baml-primer) | BAML's typed prompts compiled to LLM calls with error correction. |
| [LangChain Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/) | LangChain prompt templates, few-shot, and partial formatting. |
| [LlamaIndex Prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/) | LlamaIndex prompt customization for RAG synthesis and refinement. |
| [PromptLayer Registry](https://docs.promptlayer.com/features/prompt-registry/registry) | PromptLayer registry for versioned prompt management. |
| [HumanLoop Prompts](https://humanloop.com/docs/prompt-management) | HumanLoop prompt IDE with evals and feedback. |
| [Weights & Biases Prompts](https://weave-docs.wandb.ai/guides/core-types/prompts) | W&B Weave prompt versioning and lineage. |
| [Langfuse Prompt Management](https://langfuse.com/docs/prompts/get-started) | Langfuse prompt experiment and caching docs. |
| [Portkey Prompt Management](https://portkey.ai/docs/product/prompt-library) | Portkey prompt library with versioning and conditional caching. |
| [Context Engineering (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) | Anthropic docs on context windows, caching, and chunking. |
| [Long Context RAG (Google)](https://cloud.google.com/blog/products/ai-machine-learning/long-context-rag) | Google long-context RAG with Gemini 2M tokens — when to stuff vs retrieve. |
| [RAG vs Long Context (Anthropic)](https://www.anthropic.com/research/long-context-rag) | Anthropic analysis of retrieval vs full-context prompting tradeoffs. |
| [Needle vs Haystack Blog](https://www.anyscale.com/blog/needle-in-a-haystack-evaluation) | Anyscale's needle test methodology for long-context eval. |
| [Semantic Prompt Caching (GPTCache)](https://github.com/zilliztech/GPTCache) | GPTCache for semantic caching of LLM responses with embedding lookups. |
| [LLMLingua](https://github.com/microsoft/LLMLingua) | Microsoft LLMLingua for prompt compression — keep quality, cut tokens. |
| [LongLLMLingua](https://github.com/microsoft/LongLLMLingua) | LongLLMLingua for compressing long contexts for RAG. |
| [Recursive Summarization](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/prompt_engineering/advanced_prompts.md) | LlamaIndex recursive summarization pattern for long docs. |
| [Few-Shot Example Selection](https://python.langchain.com/docs/how_to/example_selectors/) | LangChain example selectors for dynamic few-shot prompting. |
| [AutoPrompt (Meta)](https://github.com/ucinlp/autoprompt) | AutoPrompt: gradient-guided search for prompts. |
| [PromptBreeder](https://github.com/vaishnav-mk/prompt-breeder) | Self-referential prompt evolution via LLM mutation. |
| [OPRO (Google)](https://arxiv.org/abs/2309.03409) | Optimization by PROmpting: LLMs as optimizers for prompts. |
| [Giskard Prompt Test](https://docs.giskard.ai/en/latest/knowledge/prompt_testing/index.html) | Giskard prompt testing for bias and hallucination. |
| [Promptfoo Red Team](https://www.promptfoo.dev/docs/red-team/) | Promptfoo red-teaming: prompt injections and jailbreak scans. |
| [Adversarial Prompt (JailbreakChat)](https://www.jailbreakchat.com/) | Community jailbreak prompts collection — use for red-teaming, not exploitation. |
| [Prompt Engineering Guide: Chain-of-Thought, ReAct, and Tool Use (DAIR)](https://www.promptingguide.ai/techniques/cot) | DAIR CoT guide: prompting technique reference with papers and examples. |
| [Learn Prompting: Advanced Techniques](https://learnprompting.org/docs/advanced/zero_shot) | Learn Prompting advanced: zero-shot, few-shot, and role prompting patterns. |
| [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) | DSPy paper: programmatic LLM pipelines that optimize prompts without hand-tuning. |

## AI retrieval and vector search (59)

| Resource | Useful for / constraints |
|---|---|
| [Milvus Lite](https://milvus.io/docs/milvus_lite.md) | Milvus Lite for embedded vector search without server. |
| [Weaviate Cloud](https://weaviate.io/developers/weaviate) | Weaviate Cloud with hybrid, rerank, and generative modules. |
| [Pinecone Serverless](https://docs.pinecone.io/guides/get-started/quickstart) | Pinecone serverless: autoscaling vectors with namespaces. |
| [Upstash Vector](https://upstash.com/docs/vector/overall/getstarted) | Serverless vector DB with REST API for edge functions. |
| [Supabase Vector (pgvector)](https://supabase.com/docs/guides/ai/vector-columns) | Supabase guide to pgvector: hybrid search with Postgres. |
| [Neon Vector](https://neon.tech/docs/extensions/pgvector) | Neon Postgres with pgvector for serverless RAG. |
| [MongoDB Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/) | Atlas Vector Search with $vectorSearch aggregation. |
| [Rockset (OpenAI)](https://docs.rockset.com/documentation/) | Rockset for realtime search and analytics — now part of OpenAI. |
| [Typesense](https://typesense.org/docs/guide/) | Typesense open-source search with vector and hybrid modes. |
| [Vespa](https://docs.vespa.ai/) | Vespa: big-data serving for search, recommendation, and RAG. |
| [Sphinx](https://sphinxsearch.com/docs/current.html) | Sphinx search engine for full-text — legacy but integrated in some RAG stacks. |
| [OpenSearch k-NN](https://opensearch.org/docs/latest/search-plugins/knn/index/) | OpenSearch k-NN plugin for vector search at AWS scale. |
| [Redis Vector Library](https://redis.io/docs/latest/develop/interact/search-and-query/query/vector-search/) | Redis vector search with RediSearch — hybrid queries. |
| [Turbopuffer](https://turbopuffer.com/docs/quickstart) | Turbopuffer serverless vector+FTS on object storage. |
| [Vald](https://vald.vdaas.org/docs/) | Vald: highly scalable distributed vector search engine. |
| [Vearch](https://github.com/vearch/vearch) | Vearch: distributed vector search from JD.com. |
| [Milvus Operators](https://milvus.io/docs/install_cluster-milvusoperator.md) | Milvus operator for Kubernetes deployments. |
| [Haystack Document Stores](https://docs.haystack.deepset.ai/docs/document_store) | Haystack document stores for RAG pipelines. |
| [LlamaIndex Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/) | LlamaIndex integrations for 30+ vector stores. |
| [LangChain Vector Stores](https://python.langchain.com/docs/integrations/vectorstores/) | LangChain vector store integrations list. |
| [Spring AI Vector Stores](https://docs.spring.io/spring-ai/reference/api/vectordbs.html) | Spring AI vector DB abstractions for Java. |
| [BERTopic](https://maartengr.github.io/BERTopic/) | Topic modeling with embeddings — useful for corpus exploration before RAG. |
| [Embeddings Benchmark (MTEB)](https://huggingface.co/spaces/mteb/leaderboard) | MTEB leaderboard for embedding and rerank models. |
| [BEIR](https://github.com/beir-cellar/beir) | BEIR heterogeneous retrieval benchmark. |
| [MS MARCO](https://microsoft.github.io/msmarco/) | MS MARCO passage ranking dataset — foundation for many retrievers. |
| [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Google Natural Questions benchmark for open-domain QA. |
| [HotpotQA](https://hotpotqa.github.io/) | Multi-hop QA requiring retrieval over multiple docs. |
| [CoQA](https://stanfordnlp.github.io/coqa/) | Conversational QA dataset for retrieval+conversation. |
| [SQuAD 2.0](https://rajpurkar.github.io/SQuAD-explorer/) | SQuAD 2.0 reading comprehension with unanswerable questions. |
| [TREC RAG Track](https://trec.nist.gov/data/t14_rag.html) | TREC RAG evaluation track for retrieval quality. |
| [Cohere Rerank](https://docs.cohere.com/docs/rerank) | Cohere Rerank 3.5 for improving retrieval precision. |
| [Voyage Rerank](https://docs.voyageai.com/docs/reranker) | Voyage rerankers optimized for RAG. |
| [FlagEmbedding Reranker](https://github.com/FlagOpen/FlagEmbedding/tree/master/FlagEmbedding/reranker) | BGE reranker for cross-encoder reranking. |
| [ColBERTv2](https://github.com/stanford-futuredata/ColBERT) | Late-interaction retrieval with ColBERTv2 — fine-grained token search. |
| [SPLADE](https://github.com/naver/splade) | Sparse learned retrieval via SPLADE — neural sparse vectors. |
| [BM25S](https://github.com/xhluca/bm25s) | Fast BM25 with numba — strong baseline for hybrid retrieval. |
| [Rank-BM25](https://github.com/dorianbrown/rank_bm25) | Simple Python BM25 for hybrid RAG prototypes. |
| [Pyserini](https://github.com/castorini/pyserini) | Reproducible IR toolkit with BM25, dense, and hybrid retrieval. |
| [Haystack Retrievers](https://docs.haystack.deepset.ai/docs/retriever) | Haystack retrievers: BM25, embedding, and hybrid. |
| [R2R (SciPhi)](https://r2r-docs.sciphi.ai/) | SciPhi R2R: open-source RAG ingestion, retrieval, and analytics. |
| [Verba (Weaviate)](https://github.com/weaviate/Verba) | Weaviate Verba RAG app: ingest, retrieve, chat. |
| [Khoj](https://khoj.dev/docs/) | Khoj: self-hosted personal AI with semantic search over notes. |
| [Mem0 Vector (long-term)](https://docs.mem0.ai/platform/quickstart) | Mem0 platform docs for long-term memory API. |
| [Letta Cloud](https://docs.letta.com/guides/agents) | Letta agent platform with stateful memory. |
| [Cognee Knowledge Graph](https://docs.cognee.ai/) | Cognee docs for graph memory pipeline. |
| [LangMem](https://langchain-ai.github.io/langmem/) | LangMem docs for LangGraph memory extraction. |
| [LlamaIndex Memory](https://docs.llamaindex.ai/en/stable/module_guides/agent/memory/) | LlamaIndex memory primitives for agents. |
| [RedisVL](https://docs.redisvl.com/en/latest/) | RedisVL: Python client for Redis vector search with LLM patterns. |
| [pgai (Timescale)](https://github.com/timescale/pgai) | pgai: bring AI workflows inside Postgres with pgvector. |
| [Supabase pgvector guide](https://supabase.com/docs/guides/ai/semantic-search) | Supabase semantic search tutorial end-to-end. |
| [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/) | Cloudflare Vectorize: edge vector DB with Workers AI. |
| [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | Azure AI Search with vector, semantic ranker, and hybrid. |
| [AWS OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) | OpenSearch Serverless with vector engine. |
| [A Survey on Retrieval-Augmented Generation](https://arxiv.org/abs/2312.10997) | Comprehensive RAG survey: retrievers, generators, and evaluation — guide for vector DB selection. |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG)](https://arxiv.org/abs/2005.11401) | Original RAG paper: retrieve-and-generate architecture for knowledge-intensive tasks. |
| [Dense Passage Retrieval for Open-Domain QA (DPR)](https://arxiv.org/abs/2004.04906) | DPR: dense retriever training for QA — foundation for modern embedding models. |
| [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction](https://arxiv.org/abs/2004.12832) | ColBERT: late interaction for fine-grained token-level retrieval quality. |
| [SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking](https://arxiv.org/abs/2107.05720) | SPLADE: learned sparse retrieval combining BM25 sparsity with neural expansion. |
| [GraphRAG: Graph-based Retrieval-Augmented Generation](https://arxiv.org/abs/2404.16130) | GraphRAG paper: building knowledge graphs for global, theme-level questions naive RAG misses. |

## AI speech voice and realtime (41)

| Resource | Useful for / constraints |
|---|---|
| [Whisper Large v3](https://github.com/openai/whisper/blob/main/model-card.md) | OpenAI Whisper Large v3 model card: multilingual STT strengths/limits. |
| [Whisper.cpp Large](https://github.com/ggerganov/whisper.cpp#whisper-cpp) | whisper.cpp docs for quantized Whisper inference on CPU/GPU. |
| [Distil-Whisper](https://github.com/huggingface/distil-whisper) | Distilled Whisper: 6x faster, 49% smaller with near-parity accuracy. |
| [Wav2Vec 2.0](https://huggingface.co/docs/transformers/model_doc/wav2vec2) | Facebook Wav2Vec 2.0 for self-supervised speech representation. |
| [Parakeet (NVIDIA NeMo)](https://github.com/NVIDIA/NeMo) | NVIDIA Parakeet 0.6B for fast, accurate ASR via NeMo. |
| [Canary (NVIDIA)](https://huggingface.co/nvidia/canary-1b) | NVIDIA Canary multilingual ASR model card. |
| [AssemblyAI LeMUR](https://www.assemblyai.com/docs/lemur/custom-summary) | LeMUR LLM over transcripts: summarization and Q&A on audio. |
| [Deepgram Nova 3](https://developers.deepgram.com/docs/model/nova-3) | Deepgram Nova-3 streaming STT with low latency and code-switching. |
| [Cartesia Sonic](https://docs.cartesia.ai/getting-started/about-sonic) | Cartesia Sonic: 40ms latency TTS for realtime voice agents. |
| [ElevenLabs Conversational AI](https://elevenlabs.io/docs/conversational-ai/overview) | ElevenLabs agents: turn-taking, tools, and knowledge base for voice. |
| [PlayHT 3.0](https://docs.play.ht/reference/api-generate-tts) | PlayHT API for low-latency voice cloning and TTS. |
| [Respeecher](https://www.respeecher.com/docs) | Respeecher voice cloning docs — check licensing for commercial use. |
| [Piper Voices](https://github.com/rhasspy/piper/blob/master/VOICES.md) | Piper voice list: 50+ languages, offline TTS. |
| [Bark (Suno)](https://github.com/suno-ai/bark) | Suno Bark generative TTS with music and emotion. |
| [MMS (Meta)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms) | Meta MMS for 1k+ language ASR/TTS. |
| [SeamlessM4T v2](https://github.com/facebookresearch/seamless_communication) | Meta Seamless for speech-to-speech translation. |
| [SpeechT5](https://huggingface.co/docs/transformers/model_doc/speecht5) | Microsoft SpeechT5 for TTS and voice conversion. |
| [VALL-E X](https://github.com/Plachtaa/VALL-E-X) | VALL-E X cross-lingual TTS — research code, check license. |
| [RVC (Retrieval-based Voice Conversion)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | RVC for voice conversion — popular for character voices. |
| [OpenVoice v2](https://github.com/myshell-ai/OpenVoice) | MyShell OpenVoice for instant voice cloning. |
| [Tortoise TTS](https://github.com/neonbjb/tortoise-tts) | Tortoise multi-voice TTS with expressive control. |
| [Fish Speech](https://github.com/fishaudio/fish-speech) | Fish Audio Fish Speech open TTS with voice cloning. |
| [Daily.co Docs](https://docs.daily.co/docs/introduction) | Daily WebRTC platform for voice agents (alternative to LiveKit). |
| [Agora Conversational AI](https://docs.agora.io/en/conversational-ai/overview/product-overview) | Agora for low-latency conversational AI engine. |
| [Twilio Voice Media Streams](https://www.twilio.com/docs/voice/media-streams) | Twilio media streams for telephony voice agents. |
| [Vonage Voice API](https://developer.vonage.com/en/voice/overview) | Vonage voice API for telephony integrations. |
| [Telnyx Voice API](https://developers.telnyx.com/docs/voice/programmable-voice) | Telnyx programmable voice for calling agents. |
| [WebRTC Native](https://webrtc.org/getting-started/) | WebRTC native docs for building low-latency media transport. |
| [OpenAI Realtime Transport](https://platform.openai.com/docs/guides/realtime/overview) | OpenAI realtime transport: WebRTC vs WebSocket tradeoffs. |
| [Azure Real-time Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/realtime-speech-to-text) | Azure realtime STT with push/streaming. |
| [Google Chirp 3](https://cloud.google.com/speech-to-text/docs/chirp-model) | Google Chirp 3 multilingual STT with 2B param model. |
| [NVIDIA Riva STT](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html) | Riva ASR streaming docs for GPU deployment. |
| [Picovoice](https://picovoice.ai/docs/) | Picovoice on-device wake word and STT for edge. |
| [Porcupine (Picovoice)](https://github.com/Picovoice/porcupine) | Picovoice Porcupine wake-word via SDK. |
| [Rhino (Picovoice)](https://github.com/Picovoice/rhino) | Rhino intent understanding for voice agents. |
| [Whisper: Robust Speech Recognition via Large-Scale Weak Supervision (OpenAI)](https://arxiv.org/abs/2212.04356) | Whisper paper: 680k hours weak supervision for robust STT across languages. |
| [VALL-E: Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2301.02111) | VALL-E: zero-shot TTS with acoustic prompts — foundation for voice cloning docs. |
| [SeamlessM4T: Massively Multilingual & Multimodal Machine Translation](https://arxiv.org/abs/2308.11596) | SeamlessM4T v2: speech-to-speech translation for 100+ languages. |
| [MMS: Scaling Speech Technology to 1,000+ Languages (Meta)](https://arxiv.org/abs/2305.13516) | Meta MMS: 1k-language ASR/TTS via self-supervised pretraining. |
| [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558) | FastSpeech 2: non-autoregressive TTS for low-latency voice agents. |
| [NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech Synthesizers](https://arxiv.org/abs/2304.09116) | NaturalSpeech 2: diffusion TTS for natural zero-shot cloning. |

## Counts and provenance

- Prior catalog: 1192 entries, 1188 distinct URLs, 89 categories.
- This expansion: 1000 entries, 1000 distinct URLs, 14 categories touched (14 total: 1 new, 13 existing).
- New total: 2192 entries, 2188 distinct URLs, 90 categories.
- Source tag for this expansion: `ai-expansion-2026-10-26`, checked_on `2026-10-26`.
- Review note recorded per entry: `AI-ecosystem discovery 2026-10-26; primary-source pointers compiled from official docs, registries, and skills.sh directory — verify suitability before adoption.`
- Skills.sh provenance: homepage https://www.skills.sh/ plus hot/trending leaderboards (first 600 trending entries fetched 2026-10-26 across 8 chunks), agent pages (21), topic pages (14), and representative skill pages (258) plus their GitHub sources.

## Verification

Run `python scripts/validate.py` to check index agreement, URL syntax, and category-page cross-references. A format check was passed for this expansion on 2026-10-26.

