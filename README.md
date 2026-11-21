# Preparation to Agenthon-2026

- Link: <https://agenthon.gdgtorino.it/>
- Where: [Feat. House](https://feat.house/), Via Giuseppe Giacosa 15, 10125 Torino
- When: 2026-11-21
- Event: "Build with AI" Agenthon, hackathon organised by [GDG Torino](https://gdg.community.dev/gdg-torino/) (waiting for DevFest Alps)
- Participant portal: <(participant portal)>
- Sponsors: Ariete Tech, demetra
- Our track: [Track 2 challenge brief](docs/track2-challenge.md), GenAI for marketing (deliverables due at 17:00)
- Client research: [Feyles company research](docs/feyles-company-research.md), public info on the Track 2 client
- Market benchmark: [Feyles deep research and benchmark](docs/feyles-deep-research.md), competitive positioning, unit economics, and early discoveries
- Brand specification: [Feyles brand and product kit](docs/feyles-brand-and-product-kit.md), verified 19-SKU catalog, HEX palette, logo rules, and tone of voice ([raw brand kit on Google Drive](https://drive.google.com/drive/folders/1GuPyFJ_Vz8jqk0EnZyB6Sah404fuGxk6), >1 GB, not stored in Git)
- Concept lock (WP0): [Track 2 concept lock](docs/track2-concept-lock.md), «Si divide. Si condivide.» creative direction and WP1/WP2 handoff
- Pitch deck: [Track 2 pitch deck](docs/slides/track2-pitch-deck.html) (HTML, 10 slides with speaker notes; see [Showing the pitch deck](#showing-the-pitch-deck)), with its [slide text](docs/track2-pitch-slides.md)
- Participants: @gmacario, @aleche28, @FrigaZzz
- See Group "[Agenthon-2026]((private Telegram group))" on Telegram

## Showing the pitch deck

The [pitch deck](docs/slides/track2-pitch-deck.html) is a single HTML page with its images in `docs/slides/img/`.
GitHub only shows its source, so serve it over HTTP and open it in a browser.

From a terminal inside the devcontainer (Visual Studio Code or GitHub Codespaces), at the root of the repository:

```bash
python3 -m http.server 8000 --directory docs/slides
```

Visual Studio Code forwards port 8000 automatically: click **Open in Browser** in the notification, or open the **Ports** panel and click the globe icon next to port 8000.
Then add `track2-pitch-deck.html` to the address, for example <http://localhost:8000/track2-pitch-deck.html>.
Stop the server with <kbd>Ctrl</kbd>+<kbd>C</kbd>.

In the browser:

- <kbd>→</kbd>, <kbd>↓</kbd> or <kbd>Space</kbd>: next slide; <kbd>←</kbd> or <kbd>↑</kbd>: previous slide; <kbd>Home</kbd> and <kbd>End</kbd>: first and last slide
- <kbd>P</kbd>: presentation mode, one slide per screen without speaker notes; <kbd>F</kbd>: full screen; <kbd>Esc</kbd>: back to the scrolling view with notes
- Add `#N` to the address to open slide N, for example `track2-pitch-deck.html#5`

## Useful links

Suggested by Luca during the team call:

- Google AI Studio, Gemini model guide: <https://aistudio.google.com/docs/models/gemini-decision-1>
- Modal: <https://modal.com/>
- Gemini: <https://gemini.google.com/>
- Jevai: <https://jevai.net/>
- Claude design skills: Markdown files (`SKILL.md`) with specialised instructions,
  aesthetic rules and reusable workflows that guide Claude (through Claude Code or claude.ai)
  in building interfaces, prototypes and UI/UX designs that do not look AI-generated.
- Impeccable: <https://impeccable.style/>
- Artlist toolkit, video mode: <https://toolkit.artlist.io/new?mode=video>

## The Team

| [Team Member](https://www.linkedin.com/)                            | [GitHub](https://github.com/)           | [Hugging Face](https://huggingface.co/)     |
| ------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------- |
| [Alessio Chessa](https://www.linkedin.com/in/alessiochessa/)        | [aleche28](https://github.com/aleche28) | [aleche28](https://huggingface.co/aleche28) |
| [Gianpaolo Macario](https://www.linkedin.com/in/gmacario/)          | [gmacario](https://github.com/gmacario) | [gmacario](https://huggingface.co/gmacario) |
| [Luca Frigato](https://www.linkedin.com/in/luca-frigato-72a64b155/) | [FrigaZzz](https://github.com/FrigaZzz) | [frigazzz](https://huggingface.co/frigazzz) |

## Copyright and license

Copyright (C) 2026, [B-AROL-O Team](https://github.com/B-AROL-O), all rights reserved.

### Source code license

The source code contained in this repository and the executable distributions are licensed under the terms of the MIT license as detailed in the [LICENSE](LICENSE) file.

### Documentation license

![CC BY-SA 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

Please note that your contribution to the project Documentation is licensed under a Creative Commons Attribution-Share Alike 4.0 License. see <https://creativecommons.org/licenses/by-sa/4.0/>

<!-- EOF -->
