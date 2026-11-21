# AGENTHON 2026: Track 2 tools list

<!-- (2026-11-21) -->

Deliverable 6 of our submission for AGENTHON 2026, Track 2 (GenAI for marketing): every platform, model and piece of software we used, what we used it for, and which deliverables it fed.

The Deliverables column refers to the folders of this submission: 1 commercial (`01-spot`), 2 social media content set (`02-social`), 3 web and print visuals (`03-web-print`), 4 advertising image (`04-ad-image`), 5 project sheet (`05-project-sheet`), 6 this tools list (`06-tools-list`).

## Generative AI

| Tool                                                                                                                   | Used for                                                                                                                                                                  | Deliverables  | Owner              |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------ |
| Nano Banana 2 on Vertex AI: `gemini-3.1-flash-lite-image` for 1K drafts, `gemini-3.1-flash-image` for 2K and 4K finals | Spot keyframes; text-free plates (scenes, wheat ear, snapped Rubatà) and green-screen mockup backgrounds, conditioned on the official product photos                      | 1, 2, 3, 4    | Luca, Alessio      |
| Google Veo 3.1 on Vertex AI: `veo-3.1-fast-generate-001` for drafts, `veo-3.1-generate-001` for finals                 | Video clips for the spot, with native audio for the breadstick snaps (beats 01 and 06)                                                                                    | 1             | Luca               |
| ElevenLabs API, voiceover: `eleven_v3`                                                                                 | Italian voiceover for the spot (beats 02 to 08), with a custom Piedmontese pronunciation dictionary and word timestamps for the captions                                  | 1             | Luca               |
| ElevenLabs API, music: `music_v1`                                                                                      | Music bed from beat 02                                                                                                                                                    | 1             | Luca               |
| ElevenLabs API, sound effects: `eleven_text_to_sound_v3`                                                               | Extra sound effects for the spot                                                                                                                                          | 1             | Luca               |
| `gemini-3.8-flash` on Vertex AI                                                                                        | Multimodal quality check of the generated images and clips                                                                                                                | 1             | Luca               |
| Claude (Claude Code)                                                                                                   | Research, concept, copy, planning docs and this repository; for the static visuals, wrote the scripts and prompts and checked clear space, safe zones and lettering leaks | 2, 3, 4, 5, 6 | Gianpaolo, Alessio |

## Editing and design

| Tool                                    | Used for                                                                                                                                                                                                               | Deliverables | Owner         |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------- |
| HeyGen HyperFrames (HTML, CSS and GSAP) | Kinetic captions and the animated end card of the spot                                                                                                                                                                 | 1            | Luca          |
| FFmpeg and Python                       | Final assembly of the spot, exports in 16:9 and 9:16, audio mastered to −14 LUFS                                                                                                                                       | 1            | Luca          |
| Python and Pillow                       | Compositing kit logos, packshots, claim, headlines and CTA. Luca: spot overlays and end card. Alessio (`compose.py`, `campaign.py`): social, web and print layouts, range ad, bus shelter, billboard and phone mockups | 1, 2, 3, 4   | Luca, Alessio |
| Google Fonts: Playfair Display, Lato    | Titles (Playfair Display, in place of the brand's commercial typeface Alga, as the identity guide allows) and body copy and CTAs (Lato); both under the SIL Open Font License                                          | 1, 2, 3, 4   | Alessio, Luca |
| Google Maps Places API                  | Real Turin locations as references for the arcade scenes                                                                                                                                                               | 1            | Luca          |

## Collaboration and delivery

| Tool                                   | Used for                                                                                 | Deliverables | Owner     |
| -------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ | --------- |
| Google Drive                           | Client brand kit and the submission folder                                               | All          | Gianpaolo |
| GitHub                                 | Repository for research, brief, concept lock and plan; issues to track the work packages | 5, 6         | Gianpaolo |
| GitHub Actions, Super-Linter           | Automatic checks on changes to the documentation                                         | None         | Gianpaolo |
| Docsify                                | Browsable site of the team's working documents                                           | None         | Gianpaolo |
| publish-md-pdf (pandoc and WeasyPrint) | PDF and Google Doc versions of the project sheet and this tools list                     | 5, 6         | Gianpaolo |
| Telegram                               | Team chat                                                                                | None         | All       |

## The role of AI, in short

Generative AI made the image plates, video clips, voiceover, music and sound effects in the campaign, always starting from the official Feyles pack photos so the product stays faithful.
All brand text, the logo, the packshots and the CTAs are added afterwards in code from the official kit files, never generated, so they are exact.
An AI assistant also helped with brand research, the concept and the planning, while the creative choices and the final edit stayed with the team.
The project sheet (deliverable 5) explains each step in detail.

<!-- EOF -->
