# AGENTHON 2026: Track 2 project sheet

<!-- (2026-11-21) -->

Deliverable 5 of our submission for AGENTHON 2026, Track 2 (GenAI for marketing): the creative idea, the concept, the tools we used and the role of AI in our work.
The other deliverables are in the folders `01-spot` to `06-tools-list` of this submission.

## Project

| Item   | Detail                                                                                 |
| ------ | -------------------------------------------------------------------------------------- |
| Name   | **Si divide. Si condivide.**                                                           |
| Track  | 2, GenAI for marketing (sponsor: Demetra)                                              |
| Client | Feyles – Grissinificio, Rubatà breadsticks                                             |
| Hero   | Il Classico 200 g, the sky-blue carton with the wheat-ear window                       |
| Target | 25 to 40 year-olds: aperitivo at home with friends, and a gift to bring to their place |
| Team   | Team Macario: Gianpaolo Macario, Alessio Chessa, Luca Frigato                          |

## The idea

In Italian, **«dividere»** means two things at once: **to break** and **to share**.
A Rubatà does both in a single gesture: snap one in half, and you are already handing the other half to someone.

So the campaign does not have to explain sharing.
It only has to show the snap: one breadstick becomes two, and the aperitivo begins.

**Claim:** _«Si divide. Si condivide.»_ (It breaks. It's shared.)

## The concept

The spot, about 26 seconds long, follows one Rubatà from the snap back to its origins and forward to the table:

1. **The snap.** Two people's hands break one knobbly Rubatà on a flat sky-blue background. Only the sound of the crunch, no music.
2. **Where it comes from.** A golden ear of wheat, then Rubatà leaving the oven: each piece different from the next.
3. **Where it goes.** Under the Turin arcades, someone carries the carton to friends; at home, the breadsticks slide out of the wheat-ear window and pass from hand to hand.
4. **The end.** A chain of snaps and laughter, then the carton among empty glasses, its window empty: _«Uno diventa due. Poi finiscono.»_
5. **End card.** Logo, packshot, claim and CTA: _«Scoprite gli otto gusti.»_

The same gesture carries the whole campaign: one recognizable idea (the snap), one consistent look (flat colour blocks, split in two), one clear message (made to be shared).

## How it answers the brief

| The brief asks for                         | Our answer                                                                                                       |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Make the grissino the protagonist          | The breadstick is the only hero; people appear as hands passing it on                                            |
| Its shape                                  | Knobbly, irregular Rubatà, echoed by the real wheat ear and the die-cut wheat-ear window on the pack             |
| Its crunch                                 | The spot opens on the snap with no music, and the crunch returns as the rhythm of the aperitivo                  |
| The act of sharing                         | Breaking it _is_ sharing it: the claim plays on the double meaning of «dividere»                                 |
| Artisanal character, contemporary language | Craft shown through the oven and the irregular pieces, never stated; bright daylight, flat colour, split layouts |
| Aperitivo at home and gift idea            | Home aperitivo scenes, plus a gift line: _«Portate qualcosa da dividere.»_                                       |
| Packaging and product faithful             | Official pack photos used as references for every image; logo and text never generated                           |

## Campaign system

| Deliverable                 | What we made                                                                                                                                                                                                                                        | Formats         | Folder             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------ |
| 1. Commercial               | A spot of about 26 seconds in 8 beats, with AI voiceover, music and native snap sounds                                                                                                                                                              | 16:9, 9:16      | `01-spot`          |
| 2. Social media content set | Five post concepts: the aperitivo table with the friend-tag prompt _«A chi va l'altra metà?»_, the pack window and its ingredients, Turin's arcades, the gift, the full range. Plus a six-slide carousel that retells the spot                      | 9:16, 4:5, 1:1  | `02-social`        |
| 3. Web and print visuals    | Web banners, a home page hero for desktop and mobile, four display ad sizes; a poster with the claim split in two, a 6×3 m billboard, a bus-shelter poster, an A4 magazine page and a gift tag, each as a print-ready PDF; three in-context mockups | Several         | `03-web-print`     |
| 4. Advertising image        | A snapped Rubatà between two hands: _«Spezzatelo. È fatto apposta.»_ and _«Scoprite gli otto gusti»_; plus a range ad                                                                                                                               | 4:5, 1:1, 9:16  | `04-ad-image`      |
| 5. Project sheet            | This document                                                                                                                                                                                                                                       | PDF, Google Doc | `05-project-sheet` |
| 6. Tools list               | Every platform and model we used, and what for                                                                                                                                                                                                      | PDF, Google Doc | `06-tools-list`    |

**Look:** bright natural daylight on flat colour blocks taken from the pack: sky blue #8DC6E8, cream #F9F2E9, yellow #F9C86A.
Layouts split in two halves, mirroring the act of dividing.
Playfair Display for titles and Lato for text, standing in for the brand's commercial typeface.

**Voice:** the brand's own register: plural «voi», short sentences, concrete nouns, no hype words.

## The role of AI

AI made the image plates, video clips, voiceover, music and sound effects in the campaign.
People made every decision about the idea, the brand and the final cut.

| Step              | What AI did                                                                                                                                               | What the team did                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Research          | Summarized the client kit, the brand's tone of voice and its public presence                                                                              | Checked every fact against the official kit; kept only verified claims                                                          |
| Concept           | Explored narrative options and copy variants                                                                                                              | Chose one idea at the 12:00 concept lock and dropped the rest                                                                   |
| Images            | Generated keyframes and text-free plates with Nano Banana 2 on Vertex AI, using the official pack photos as references                                    | Wrote the prompts, picked the takes, rejected warped packs; used the real Classico photo for the pack-window post               |
| Video             | Generated the clips and the snap sounds with Google Veo 3.1 on Vertex AI; checked frames with Gemini                                                      | Directed the 8 beats, chose the takes, edited the spot with HeyGen HyperFrames and FFmpeg                                       |
| Voice and music   | Italian voiceover, music bed and extra sound effects with ElevenLabs                                                                                      | Wrote the voiceover lines in the brand's voice; built a pronunciation dictionary for «Rubatà» and other Piedmontese words       |
| Text and logo     | None                                                                                                                                                      | Added logo, packshots, claim, headlines and CTAs in code with Python and Pillow, from the official kit files, so they are exact |
| Planning and docs | Drafted the plan, the work breakdown and these documents with Claude; Claude Code wrote the compositing scripts and image prompts and checked brand rules | Reviewed, corrected and approved them                                                                                           |

### Rules we gave the AI

- **Faithful product:** always knobbly, irregular Rubatà, never thin smooth breadsticks; never show hands shaping dough, never claim "hand-rolled".
- **Faithful pack:** official pack fronts and 3D mockups as references; if a model distorts the pack, fall back to a still or to compositing the real photo.
- **No generated text:** plates stay text-free, and the real logo is composited, never redrawn or animated.
- **Verified claims only:** no awards, founders, volumes or other facts that the client kit does not state.

## Tools

The full list, with the exact model or version of each tool and what it was used for, is in the tools list (deliverable 6, folder `06-tools-list`).
In short: Nano Banana 2 for keyframes and plates, Google Veo 3.1 for video, ElevenLabs for voiceover, music and sound effects, HeyGen HyperFrames, FFmpeg and Python with Pillow for editing and compositing, Claude for research, planning and the compositing code, and GitHub and Google Drive for collaboration.

## Beyond the prototype

- **A reusable format.** The gesture works for every Rubatà flavour: one snap per flavour, same layout, same claim. The other seven flavours are new spots and posts, not a new campaign.
- **Built for social.** The friend-tag prompt _«A chi va l'altra metà?»_ invites people to post their own snap, giving the brand user-generated content for free.
- **Cheap to extend.** Text-free plates and a fixed layout mean new headlines, seasons or gift boxes are a post-production change, not a new shoot.
- **Grounded in the brand.** Copy uses the brand's tone-of-voice guide and approved CTAs, so the client can run it as it is.

<!-- EOF -->
