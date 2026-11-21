# AGENTHON 2026: Track 2 static visuals catalogue

<!-- (2026-11-21) -->

Catalogue of every static visual submitted for the «Si divide. Si condivide.» campaign: deliverables 2, 3 and 4 of the [Track 2 challenge brief](track2-challenge.md), produced for [issue #9](https://github.com/B-AROL-O/agenthon-2026/issues/9).
The files are in the [submission Drive folder](https://drive.google.com/drive/folders/1mL-yWZ0gsObf_6VHV3TmJgGfv0_Wswkp), under `02-social/`, `03-web-print/` and `04-ad-image/`.
The concept, copy and guardrails come from the [concept lock](track2-concept-lock.md); the captions for each post are in the [social copy deck](track2-social-copy-deck.md).
Every phrase written on the images, with the files it appears on, is listed in the [on-image catchphrases](track2-on-image-copy.md).

## How the files were made

Every file comes from one command, `uv run campaign.py` in `genai/` (see [genai/README.md](../genai/README.md)), so the whole set can be rebuilt in about 40 seconds after a copy change.

- **AI plates:** Nano Banana 2 on Vertex AI generated text-free photographs only: scenes with people, the wheat ear, the snapped breadstick and empty mockup scenes with a green panel.
  The client's Classico photo was passed as a reference so the breadsticks keep their real knobbly shape.
- **Everything else comes from the client kit:** the logo files, the 3D pack mockups used as packshots, the die-cut pack window, the spiga pattern, the pack colours and two real photos (the oven and the piazza Castello shop).
  The model never draws the pack, the logo or any text.
- **Typography:** Playfair Display for titles, as the stand-in for the commercial brand font Alga that the identity guide allows, and Lato for body text and buttons.

### One look across every file

- **Layout:** a photo or a sky blue `#8DC6E8` block on top, a cream `#F9F2E9` block below.
  The split itself shows the idea: one thing divided in two.
- **Buttons:** sky blue pills with the kit's own CTAs, without the final full stop.
- **Sign-off:** «Feyles | Si divide. Si condivide.», the logo and the claim side by side.
  It copies the layout of the real shop sign («Feyles | Piazza Castello»), which appears on carousel slide 5.
- **Brand rules checked on every file:** gold logo on cream, clear space around the logo at least the height of its «F», the bottom 340 px of 9:16 files left free for the reply bar, and Il Classico ingredients including strutto.

## 04-ad-image: advertising image (deliverable 4)

| File               | Size      | What it shows                                                                                                                   | Purpose                                                                                                     |
| ------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `hero-ad-4x5.png`  | 1080×1350 | Two hands of two different people snapping one Rubatà on sky blue; «Spezzatelo. È fatto apposta.» and «Scoprite gli otto gusti» | **The main ad image.** The whole idea in one frame: breaking the breadstick already shares it. Feed format. |
| `hero-ad-1x1.png`  | 1080×1080 | The same ad, square                                                                                                             | Facebook feed and square placements                                                                         |
| `hero-ad-9x16.png` | 1080×1920 | The same ad, vertical, with the sky extended above the hands                                                                    | Stories, Reels and TikTok ad placements                                                                     |
| `range-ad-4x5.png` | 1080×1350 | The seven 200 g packs, each on a stripe of its own pack colour; «Qual è il vostro?»                                             | A second ad for the whole range. One block divided into seven, like a breadstick passed around a table.     |

## 02-social: social media content set (deliverable 2)

Six concepts, each in the three formats the main channels use: 9:16 (Instagram and Facebook stories, Reels, TikTok), 4:5 (Instagram feed) and 1:1 (Facebook feed, square placements).
The [copy deck](track2-social-copy-deck.md) maps each file to its channel and gives the caption.

| Folder          | Files                                    | What it shows                                                                                                                                         | Purpose                                                                        | Made with                        |
| --------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------- |
| `condivisione/` | `social-condivisione-{9x16,4x5,1x1}.png` | An aperitivo table from above, four friends' hands snapping and passing Rubatà; claim and the «A chi va l'altra metà?» sticker                        | The campaign claim as a post, plus a friend-tag mechanic that spreads the post | AI scene + kit                   |
| `finestra/`     | `social-finestra-{9x16,4x5,1x1}.png`     | The real Il Classico pack with real breadsticks seen through its die-cut spiga window; «Dentro c'è quello che deve esserci.» and the five ingredients | The product truth post: what is inside, said plainly in the brand's own words  | **No AI:** kit pack + kit photo  |
| `torino/`       | `social-torino-{9x16,4x5,1x1}.png`       | Two friends sharing a snapped Rubatà under Turin's arcades; «A Torino le cose buone non si dicono in giro.»                                           | Local pride and footfall: the CTA sends people to the piazza Castello shop     | AI scene + kit                   |
| `regalo/`       | `social-regalo-{9x16,4x5,1x1}.png`       | A guest handing a linen-wrapped bundle of Rubatà to the host at the door; «Portate qualcosa da dividere.»                                             | The gift angle of the brief: what to bring to friends, and the gift box CTA    | AI scene + kit                   |
| `gamma/`        | `social-gamma-{9x16,4x5,1x1}.png`        | The seven 200 g packs on stripes of their own colours; «Qual è il vostro?»                                                                            | Shows the full range and invites comments on favourite flavours                | **No AI:** kit mockups + palette |

### carousel: the spot in six slides (4:5)

The carousel retells the spot's story with its own voiceover lines, so a viewer who never sees the video still gets the story.

| File             | What it shows                                                                        | Made with               |
| ---------------- | ------------------------------------------------------------------------------------ | ----------------------- |
| `carousel-1.png` | A golden wheat ear over the brand's spiga pattern; «Comincia da una spiga.»          | AI plate + kit pattern  |
| `carousel-2.png` | Rubatà coming out of the oven; «Rubatà vuol dire arrotolato. Ogni pezzo è diverso.»  | **Real kit photo**      |
| `carousel-3.png` | The snap between two hands; «Spezzatelo. È fatto apposta.»                           | AI plate (hero)         |
| `carousel-4.png` | The aperitivo table, hands passing halves; «Si passano di mano.»                     | AI plate (condivisione) |
| `carousel-5.png` | The real piazza Castello shop front; «A Torino le cose buone...» and the shop CTA    | **Real kit photo**      |
| `carousel-6.png` | Il Classico packshot; «Uno diventa due.», «Scoprite gli otto gusti» and the sign-off | Kit packshot            |

## 03-web-print: web and print visuals (deliverable 3)

### web

| File                        | Size      | What it shows                                                                                                   | Purpose                                                                                                                                                   |
| --------------------------- | --------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `web-banner-16x9.png`       | 1920×1080 | The doorway handover, with headline, packshot and gift box CTA in the cream block                               | Main web visual: site banners, YouTube and Facebook covers                                                                                                |
| `web-banner-gamma-16x9.png` | 1920×1080 | The seven colour stripes with «Qual è il vostro?»                                                               | Range banner for the shop pages of the site                                                                                                               |
| `homepage-hero-desktop.png` | 1440×810  | A concept for the top of the grissinificiofeyles.it home page, with menu, campaign photo, headline and gift CTA | Shows how the campaign would land on the client's own site                                                                                                |
| `homepage-hero-mobile.png`  | 390×844   | The same home page hero on a phone                                                                              | The mobile layout of the same section                                                                                                                     |
| `display-300x250.png`       | 300×250   | Gift message: photo, headline, CTA, logo                                                                        | Standard display ad (medium rectangle)                                                                                                                    |
| `display-300x600.png`       | 300×600   | The same message with packshot                                                                                  | Standard display ad (half page)                                                                                                                           |
| `display-728x90.png`        | 728×90    | Photo, headline, CTA, packshot, spiga mark                                                                      | Standard display ad (leaderboard). Too short for the full logo's clear space, so it uses the spiga mark, as the brand guide allows when space is minimal. |
| `display-320x100.png`       | 320×100   | Packshot, headline, CTA, spiga mark                                                                             | Standard mobile banner                                                                                                                                    |

### print

Every print file has a PNG for viewing and a PDF for printing.

| File                              | Size                          | What it shows                                                                                                       | Purpose                                                                                                                                                                 |
| --------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `print-poster-2x3.pdf`, `.jpg`    | 3600×5400 (12×18 in, 300 dpi) | Diptych: a wheat ear on sky blue with the spiga pattern, «Si divide.» \| a snapped Rubatà on cream, «Si condivide.» | **The campaign poster.** The claim split across the two halves, like the breadstick. The JPEG is the viewing copy (the PNG is over the Drive connector's upload limit). |
| `billboard-6x3m.pdf`, `.png`      | 4000×2000 (proof)             | The same diptych laid out wide, with packshot and logo                                                              | Roadside billboard (6×3 m): a few words, readable from a car                                                                                                            |
| `bus-shelter-120x176.pdf`, `.png` | 2400×3520 (proof)             | The hero snap with «Spezzatelo. È fatto apposta.», CTA and sign-off                                                 | Bus-shelter poster (120×176 cm) for the city street                                                                                                                     |
| `magazine-a4.pdf`, `.png`         | 2480×3508 (A4, 300 dpi)       | The doorway handover, «Portate qualcosa da dividere.», a short body text, gift CTA, packshot                        | Full-page magazine ad: the only piece with room for a few lines of body copy                                                                                            |
| `gift-tag-55x95mm.pdf`, `.png`    | 1360×1122 (two sides)         | Front: white logo on the sky blue spiga pattern. Back: «Da dividere con ______» and the claim                       | A tag for the piazza Castello shop to tie on gift packs: the campaign in the customer's hand                                                                            |

### mockups

These are not deliverables in themselves: they show the finished files in place, for the pitch and the project sheet.
Each scene was generated with a pure green panel; the code keys out the green and warps our real file onto it, so the AI never draws our ad.

| File                            | What it shows                                                     |
| ------------------------------- | ----------------------------------------------------------------- |
| `mockup-bus-shelter-torino.png` | The bus-shelter poster under Turin's arcades, with a tram passing |
| `mockup-billboard.png`          | The billboard on a Turin street                                   |
| `mockup-phone-story.png`        | The condivisione story on a phone at an aperitivo                 |

## Christmas and Cioccorubatà extension

The spot tells a Christmas story with Il Cioccorubatà fondente, to carry the company's long story (1968 to today) with an emotional message.
The year-round set above stays as it is; these files add a Christmas campaign and the chocolate line next to it, in the same folders, with `natale`, `cioccorubata` or `gamma-completa` in every name.
They come from `uv run natale.py` in `genai/`, which reuses the helpers of `campaign.py` and never overwrites its files.

- **Look:** the same cream block, with burgundy `#7B2838` (the Cioccorubatà fondente pack colour) in place of sky blue, and burgundy pills with cream text.
- **Packs:** the kit's 150 g Cioccorubatà mockups and the real gift box (its «Merry Christmas» is printed on the client's box; we never set our own text in that script).
- **AI plates:** three new text-free Nano Banana 2 scenes (`genai/prompts/natale-*.txt`): a grandparent and a grandchild snapping one chocolate-coated Rubatà on burgundy, a three-generation Christmas table from above, and a Christmas doorway handover.
- **Product truth:** Cioccorubatà is Rubatà made with olive oil, coated in chocolate (the fondente has at least 70% cocoa), so the strutto check does not apply; every fact is from the kit's texts.

### 04-ad-image

| File                           | What it shows                                                                                                     | Purpose                                                                           |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `natale-ad-{4x5,1x1,9x16}.png` | A grandparent's hand and a child's hand snap one Cioccorubatà on burgundy; «Dal 1968 si passa di mano.», gift CTA | **The Christmas ad.** The same gesture as the hero ad, passed between generations |
| `cioccorubata-ad-4x5.png`      | The three Cioccorubatà cartons on their pack colours; «Anche il dolce si divide.»                                 | Ad for the chocolate line                                                         |
| `range-completa-ad-4x5.png`    | The seven 200 g Rubatà on top, the three Cioccorubatà below; «Qual è il vostro?»                                  | Full-range ad, including the chocolate line                                       |

### 02-social

| Folder             | Files                                      | What it shows                                                                                          | Made with                  |
| ------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------- |
| `natale-tavola/`   | `social-natale-tavola-{9x16,4x5,1x1}.png`  | A Christmas table from above, three generations passing halves; claim and «A chi va l'altra metà?»     | AI scene + kit             |
| `natale-regalo/`   | `social-natale-regalo-{9x16,4x5,1x1}.png`  | A guest hands a Rubatà bundle to a grandmother at the door; «Da regalare a chi apparecchia per tutti.» | AI scene + kit             |
| `cioccorubata/`    | `social-cioccorubata-{9x16,4x5,1x1}.png`   | The three Cioccorubatà on their colours; «Anche il dolce si divide.» and the product facts             | **No AI:** kit mockups     |
| `gamma-completa/`  | `social-gamma-completa-{9x16,4x5,1x1}.png` | Seven Rubatà and three Cioccorubatà, in two tiers; «Qual è il vostro?»                                 | **No AI:** kit mockups     |
| `carousel-natale/` | `carousel-natale-{1..5}.png`               | The story from 1968: the old oven, the oven exit, Cambiano, piazza Castello, the gift box              | **No AI:** real kit photos |

The carousel lines are the brand's own sentences: «Grissini Rubatà, dal 1968.», «Una famiglia, un laboratorio, lo stesso grissino da più di cinquant'anni.», «Dal laboratorio di Cambiano, alle porte di Torino, a casa vostra.»

### 03-web-print

| File                                                      | What it shows                                                             |
| --------------------------------------------------------- | ------------------------------------------------------------------------- |
| `web/web-banner-natale-16x9.png`                          | The Christmas doorway, gift box and fondente pack, gift CTA               |
| `web/web-banner-gamma-completa-16x9.png`                  | The full range in two tiers                                               |
| `web/display-natale-{300x250,300x600,728x90,320x100}.png` | The Christmas gift message in the four IAB sizes                          |
| `print/bus-shelter-natale-120x176.pdf`, `.png`            | The Christmas ad as a bus-shelter poster                                  |
| `print/magazine-natale-a4.pdf`, `.png`                    | The Christmas doorway with body copy on the Cioccorubatà fondente         |
| `print/gift-tag-natale-55x95mm.pdf`, `.png`               | Front: white logo on burgundy. Back: «Buon Natale da dividere con ______» |

<!-- EOF -->
