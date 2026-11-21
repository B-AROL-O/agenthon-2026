# AGENTHON 2026: Track 2 tools list

<!-- (2026-11-21) -->

Draft of **deliverable 6** for the [Track 2 challenge brief](track2-challenge.md): the platforms and software we used, and what we used them for.
It is tracked in [WP3](https://github.com/B-AROL-O/agenthon-2026/issues/10) of the [timeline and WBS](track2-wbs.md).

How to keep it current:

- Whoever uses a tool adds or updates its row straight away, including the exact model or version.
- Rows marked **To confirm** are planned but not yet used; delete any we end up not using.
- Before 16:45, export the final table to `06-tools-list` in the submission Drive folder.

## Generative AI

| Tool                                                                                                                   | Used for                                                                                                                                 | Deliverables | Owner         | Status |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------- | ------ |
| Nano Banana 2 on Vertex AI: `gemini-3.1-flash-lite-image` for 1K drafts, `gemini-3.1-flash-image` for 2K and 4K finals | Keyframes for the spot and text-free plates for the static visuals, conditioned on the official Feyles product and pack photos           | 1, 2, 3, 4   | Luca, Alessio | Used   |
| Google Veo 3.1 on Vertex AI: `veo-3.1-fast-generate-001` for drafts, `veo-3.1-generate-001` for finals                 | Video clips for the spot, with native audio for the breadstick snaps (beats 01 and 06)                                                   | 1            | Luca          | Used   |
| ElevenLabs API, voiceover: `eleven_v3`                                                                                 | Italian voiceover for the spot (beats 02 to 08), with a custom Piedmontese pronunciation dictionary and word timestamps for the captions | 1            | Luca          | Used   |
| ElevenLabs API, music: `music_v1`                                                                                      | Music bed from beat 02                                                                                                                   | 1            | Luca          | Used   |
| ElevenLabs API, sound effects: `eleven_text_to_sound_v3`                                                               | Extra sound effects for the spot                                                                                                         | 1            | Luca          | Used   |
| `gemini-3.8-flash` on Vertex AI                                                                                        | Multimodal quality check of the generated images and clips                                                                               | 1            | Luca          | Used   |
| Claude (Claude Code)                                                                                                   | Brand research, concept lock drafting, copy variants, planning documents and this repository                                             | 5, 6         | Gianpaolo     | Used   |

## Editing and design

| Tool                                    | Used for                                                                                                                                                                                              | Deliverables | Owner         | Status |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------- | ------ |
| HeyGen HyperFrames (HTML, CSS and GSAP) | Kinetic captions and the animated end card of the spot                                                                                                                                                | 1            | Luca          | Used   |
| FFmpeg and Python                       | Final assembly of the spot, exports in 16:9 and 9:16, audio mastered to −14 LUFS                                                                                                                      | 1            | Luca          | Used   |
| Python and Pillow                       | Deterministic compositing from the official kit files: logo, packshot line-up, claim, headlines and CTA. Spot overlays and end card (Luca); social, web and print layouts with `compose.py` (Alessio) | 1, 2, 3, 4   | Luca, Alessio | Used   |
| Google Fonts: Playfair Display, Lato    | Titles and body copy, in place of the brand's commercial typeface                                                                                                                                     | 1, 2, 3, 4   | Alessio, Luca | Used   |
| Google Maps Places API                  | Real Turin locations as references for the arcade scenes                                                                                                                                              | 1            | Luca          | Used   |

## Collaboration and delivery

| Tool                         | Used for                                                                                 | Deliverables | Owner     | Status |
| ---------------------------- | ---------------------------------------------------------------------------------------- | ------------ | --------- | ------ |
| Google Drive                 | Client brand kit (kept out of Git) and the submission folder                             | All          | Gianpaolo | Used   |
| GitHub                       | Repository for research, brief, concept lock and plan; issues to track the work packages | 5, 6         | Gianpaolo | Used   |
| GitHub Actions, Super-Linter | Automatic checks on every change to the documentation                                    | None         | Gianpaolo | Used   |
| Docsify                      | Browsable site built from the `docs/` folder                                             | None         | Gianpaolo | Used   |
| Telegram                     | Team chat                                                                                | None         | All       | Used   |

## Role of AI, in one paragraph

To reuse in the [project sheet](https://github.com/B-AROL-O/agenthon-2026/issues/10) (deliverable 5):

> Generative AI made the image plates, video clips, voiceover, music and sound effects in the campaign, always starting from the official Feyles pack photos so the product stays faithful.
> All brand text, the logo, the packshots and the CTAs are added afterwards in code from the official kit files, never generated, so they are exact.
> An AI assistant also helped with brand research, the concept and the planning, while the creative choices and the final edit stayed with the team.

<!-- EOF -->
