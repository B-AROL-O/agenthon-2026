# AGENTS.md

This file provides guidance to AI coding agents working in this repository.

## What this repository is

Team workspace of the B-AROL-O team for the GDG Torino "Build with AI" Agenthon (21 November 2026, Track 2: GenAI for marketing, client Feyles / Rubatà breadsticks).
It currently holds **documentation only** — no application code, build tool or tests.
The `.devcontainer/` image (Node, Python, uv, Claude Code, Docker-in-Docker, gh) is there for whatever gets built during the event.

Start from [README.md](README.md) for event details and team, then:

- [docs/track2-challenge.md](docs/track2-challenge.md): the official Track 2 brief and deliverables
- [docs/track2-wbs.md](docs/track2-wbs.md): timeline, hard deadlines (submission freeze 17:00, pitch 17:15) and task split
- [docs/feyles-company-research.md](docs/feyles-company-research.md): public research on the client
- [docs/brainstorm-track2.md](docs/brainstorm-track2.md): team brainstorm

## Docs site

`docs/` is a [Docsify](https://docsify.js.org/) site (`docs/index.html`, `loadSidebar: true`, `docs/.nojekyll`).
When adding a page under `docs/`, also add it to [docs/_sidebar.md](docs/_sidebar.md), or it will not be reachable from the site.
To preview locally: `npx docsify-cli serve docs`.

## Linting (CI)

CI runs [Super-Linter](.github/workflows/linter.yml) on every push and PR, with Prettier as the formatter (Biome format, JSON and Black validators are disabled).
Checks that have actually failed on this repo's Markdown: Prettier formatting, markdownlint, textlint and codespell.

- markdownlint rules: [.github/linters/.markdown-lint.yml](.github/linters/.markdown-lint.yml) (root `.markdownlint.yaml` extends it for the Visual Studio Code extension). Line length limit is 400; inline HTML allowed.
- codespell: Italian words that trigger false positives go in `ignore-words-list` in [.github/linters/.codespellrc](.github/linters/.codespellrc).
- Before committing, run at least `npx prettier --check .` (or `--write`) and `npx markdownlint-cli2 "**/*.md"`.

## Markdown conventions

- Every Markdown file ends with `<!-- EOF -->` (YAML/config files end with `# EOF`).
- Dated docs put an HTML comment with the date right under the title, e.g. `<!-- (2026-11-21) -->`.
- Write one sentence per line in prose paragraphs.
- Documentation is CC BY-SA 4.0; code is MIT ([LICENSE](LICENSE)).

<!-- EOF -->
