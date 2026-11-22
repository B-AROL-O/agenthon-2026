# AGENTS.md

This file provides guidance to AI coding agents working in this repository.

## What this repository is

Entry of the B-AROL-O team to the GDG Torino "Build with AI" Agenthon (21 November 2026, Track 2: GenAI for marketing, client Feyles / Rubatà breadsticks).
The hackathon is over: the repository now documents what was delivered, for third-party readers.
It holds the documentation, the HTML pitch deck (`docs/slides/`), the image generation and compositing pipeline (`genai/`, Python with `uv`) and helper scripts (`scripts/`).
The `.devcontainer/` image (Node, Python, uv, Claude Code, Docker-in-Docker, gh) is described in [docs/devcontainer.md](docs/devcontainer.md).

Start from [README.md](README.md) for the project overview and team, then:

- [docs/track2-challenge.md](docs/track2-challenge.md): the official Track 2 brief and deliverables
- [docs/track2-project-sheet.md](docs/track2-project-sheet.md): the idea, the concept and the role of AI
- [docs/deliverables.md](docs/deliverables.md): index of the six deliverables
- [docs/hackathon-notes.md](docs/hackathon-notes.md): event logistics and working documents from the day

## Public repository

The repository is public.
Do not commit content from the client's brand kit (licensed to participants for Agenthon 2026 submissions only), private links such as team chat invites, credentials or billing account IDs.
Link to the client's public channels instead.

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
