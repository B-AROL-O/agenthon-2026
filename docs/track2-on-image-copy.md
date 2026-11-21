# AGENTHON 2026: Track 2 on-image catchphrases

<!-- (2026-11-21) -->

Every catchphrase that appears on the static visuals in the [submission Drive folder](https://drive.google.com/drive/folders/1mL-yWZ0gsObf_6VHV3TmJgGfv0_Wswkp) (`02-social/`, `03-web-print/`, `04-ad-image/`).
The AI plates are text-free: all the text is added by `genai/campaign.py` and `genai/compose.py`, so this list comes from the code that rendered the uploaded files.
The copy strings have not changed since the commit that built the full set, and the local renders match the Drive files byte for byte.

Phrases are written as they appear on the images: curly apostrophes, and CTAs without the final full stop (the [concept lock](track2-concept-lock.md) writes the CTAs with one).
Line breaks change by format, so each phrase is given on one line.
For each file, the [static visuals catalogue](track2-wp2-deliverables.md) describes the visual, and the [social copy deck](track2-social-copy-deck.md) gives the post caption.

## Claim and headlines

| Phrase                                          | Role                   | Where it appears                                                                                                                                                                       |
| ----------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| «Si divide. Si condivide.»                      | Campaign claim         | Headline of `social-condivisione-{9x16,4x5,1x1}`; split across the two halves of `print-poster-2x3` and `billboard-6x3m` («Si divide.» \| «Si condivide.»); back of `gift-tag-55x95mm` |
| «Spezzatelo. È fatto apposta.»                  | Hero ad headline       | `hero-ad-{4x5,1x1,9x16}`, `bus-shelter-120x176`, `carousel-3`                                                                                                                          |
| «Portate qualcosa da dividere.»                 | Gift headline          | `social-regalo-{9x16,4x5,1x1}`, `web-banner-16x9`, `homepage-hero-{desktop,mobile}`, `display-{300x250,300x600,728x90,320x100}`, `magazine-a4`                                         |
| «A Torino le cose buone non si dicono in giro.» | Local headline         | `social-torino-{9x16,4x5,1x1}`, `carousel-5`                                                                                                                                           |
| «Dentro c’è quello che deve esserci.»           | Product truth (window) | `social-finestra-{9x16,4x5,1x1}` (verbatim line from the client's site)                                                                                                                |
| «Qual è il vostro?»                             | Range headline         | `social-gamma-{9x16,4x5,1x1}`, `range-ad-4x5`, `web-banner-gamma-16x9`                                                                                                                 |
| «A chi va l’altra metà?»                        | Friend-tag sticker     | `social-condivisione-{9x16,4x5,1x1}` (sky blue pill on the seam between photo and cream block)                                                                                         |
| «Da dividere con ______»                        | Gift tag prompt        | Back of `gift-tag-55x95mm`, with two gold lines to write the name on                                                                                                                   |

## Carousel lines

The six slides in `02-social/carousel/` retell the spot.
Slides 3 and 5 reuse headlines from the table above; the other four lines appear only here.

| Slide        | Line                                                                 |
| ------------ | -------------------------------------------------------------------- |
| `carousel-1` | «Comincia da una spiga.»                                             |
| `carousel-2` | «Rubatà vuol dire arrotolato. Ogni pezzo è diverso.»                 |
| `carousel-3` | «Spezzatelo. È fatto apposta.»                                       |
| `carousel-4` | «Si passano di mano.»                                                |
| `carousel-5` | «A Torino le cose buone non si dicono in giro.» + the shop CTA       |
| `carousel-6` | «Uno diventa due.» + «Scoprite gli otto gusti» + the sign-off lockup |

## Calls to action

All three are sky blue pills.

| CTA                                    | Where it appears                                                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| «Scoprite gli otto gusti»              | `hero-ad-{4x5,1x1,9x16}`, `bus-shelter-120x176`, `social-gamma-{9x16,4x5,1x1}`, `range-ad-4x5`, `web-banner-gamma-16x9`, `carousel-6` |
| «Componete la vostra box regalo»       | `social-regalo-{9x16,4x5,1x1}`, `web-banner-16x9`, `homepage-hero-{desktop,mobile}`, all four `display-*`, `magazine-a4`              |
| «Venite a trovarci in piazza Castello» | `social-torino-{9x16,4x5,1x1}`, `carousel-5`                                                                                          |

## Sign-off lockup

«Feyles | Si divide. Si condivide.»: the gold logo, a thin divider, then the claim in italics on two lines, copied from the layout of the piazza Castello shop sign.

- **With the lockup:** `hero-ad-*`, `social-torino-*`, `social-regalo-*`, `social-finestra-{9x16,4x5}`, `social-gamma-*`, `range-ad-4x5`, `carousel-6`, `web-banner-16x9`, `web-banner-gamma-16x9`, `homepage-hero-*`, `magazine-a4`, `bus-shelter-120x176`.
- **Logo only, no lockup:** `social-condivisione-*` and `print-poster-2x3` (the claim is already the headline), `billboard-6x3m`, `social-finestra-1x1`, `display-300x250` and `display-300x600`.
- **Spiga mark only:** `display-728x90`, `display-320x100` (too short for the full logo's clear space), the gift tag back and `carousel-1` to `carousel-5`.

The three files in `03-web-print/mockups/` place `bus-shelter-120x176`, `billboard-6x3m` and `social-condivisione-9x16` into scenes, so they carry the same text as those files.

## Other text on the images

Not catchphrases, listed so the set is complete.

- **Ingredients** (`social-finestra-*`): «farina di grano tenero · strutto · malto · sale · lievito di birra».
- **Homepage subline** (`homepage-hero-*`): «Il Classico, il Rubatà da cui è cominciato tutto.»
- **Homepage menu** (`homepage-hero-desktop`): Rubatà, Brichet, Regali, Il laboratorio, Negozio.
- **Magazine body copy** (`magazine-a4`): «Il Classico è il Rubatà da cui è cominciato tutto: farina, strutto, malto, sale e lievito, arrotolato e sfornato ogni giorno. Ogni pezzo è diverso. Si spezza con le mani e si passa a chi è accanto.»
- **URL** `grissinificiofeyles.it`: `magazine-a4`, `print-poster-2x3`.
- **Slide counters** `1/6` to `6/6` on the carousel.

## Copy not on any image

These lines come from the same copy system but are not rendered on any static visual:

- the backup claims «L’aperitivo si passa di mano.», «Fatti per essere divisi.» and «Il primo crac della serata.» (the last one is used as the TikTok and Reels caption);
- the spot's voiceover sign-off «Feyles. Si divide, si condivide.»;
- the post captions and hashtags in the [social copy deck](track2-social-copy-deck.md).

<!-- EOF -->
