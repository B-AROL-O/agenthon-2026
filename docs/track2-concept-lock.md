# AGENTHON 2026: Track 2 concept lock (Si divide. Si condivide)

<!-- (2026-11-21) -->

Locked creative direction for **WP0: Concept and creative direction** ([Track 2 timeline and WBS](track2-wbs.md)), resolving [issue #7](https://github.com/B-AROL-O/agenthon-2026/issues/7) and defining the handoff for WP1 (advertising spot) and WP2 (static visuals).
All brand constraints follow the official Feyles brand kit, which was shared with participants for the event only and is not published here.

## The core idea in one sentence

In Italian, **«dividere»** means two things at once: **to break apart** and **to share**.
A Feyles Rubatà performs both in a single gesture — and on the 200 g carton, the die-cut wheat ear (`spiga`) acts as a window from which that shared breadstick emerges.

## Why it fits the Track 2 brief

| Brief requirement ([challenge brief](track2-challenge.md)) | Concept lock response                                                                                   |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Shape                                                      | Real golden wheat ear first, then the die-cut `spiga` window on `Il Classico` showing knobbly Rubatà    |
| Crunch                                                     | Dry, crisp breadstick _crack_ opens the film (ASMR hook, no music) and punctuates the aperitivo passes  |
| Act of sharing                                             | Snapping one Rubatà in half already hands the other half to someone else                                |
| Artisanal character in contemporary language               | Shown through the oven exit and irregular pieces (no two alike), then lively 25–40 friends at aperitivo |
| One recognisable idea                                      | One becomes two (`Uno diventa due`). Immediately readable even with sound muted and no on-screen text   |

## Scope lock vs. earlier research

Early research proposed three Christmas-themed concepts spanning multiple gift lines and seasons (see [Feyles background research](feyles-background-research.md)).
To respect the 12:00 WP0 lock and the 20–30 s runtime budget:

- **One hero pack, one gesture:** `Il Classico` 200 g sky-blue carton (`#8DC6E8`) is the visual anchor instead of a full catalog tour (`1.5 kg`/`3 kg` bulk boxes and biscuit _casette_ stay out of frame).
- **Year-round aperitivo and gift framing:** Drops Christmas decorations and holiday jargon, targeting 25–40 year-old friends at home and hosts bringing something to share.

## Locked copy system and portal description

- **Campaign claim:** _«Si divide. Si condivide.»_ (pairs alongside, never replaces, the pack descriptor _«Tradizione dal 1968»_; backup options: _«L'aperitivo si passa di mano.»_, _«Fatti per essere divisi.»_, _«Il primo crac della serata.»_)
- **Hero ad headline:** _«Spezzatelo. È fatto apposta.»_
- **Gift headline:** _«Portate qualcosa da dividere.»_
- **Social mechanic:** _«A chi va l'altra metà?»_ (friend tag prompt)
- **Window macro headline:** _«Dentro c'è quello che deve esserci.»_ (verbatim site line)
- **Approved kit CTAs (`grissinificiofeyles.it`):** _«Scoprite gli otto gusti.»_ (spot and hero ad) and _«Componete la vostra box regalo.»_ (gifting placements).

### Portal project name and summary

**Project name:** `Si divide. Si condivide.`

Italian portal description:

> In italiano «dividere» vuol dire due cose: spezzare e condividere. Il Rubatà Feyles le fa con un gesto solo.
> Lo spot parte da lì, dal crac di un grissino spezzato tra due mani, risale alla spiga e al forno
> e torna sul tavolo dell'aperitivo, dove i grissini escono dalla finestra a spiga dell'astuccio e passano di mano in mano, finché finiscono.
> Un suono, una forma, un gesto, per chi ha tra i 25 e i 40 anni
> e a casa degli amici vuole portare qualcosa da dividere.

English portal description:

> In Italian, "dividere" means both to break and to share. A Feyles Rubatà does both in one gesture.
> The spot starts from the snap of a breadstick broken between two hands, goes back to the ear of wheat and the oven,
> and returns to the aperitivo table, where the breadsticks leave the wheat-ear window of the pack and pass from hand to hand until they are gone.
> One sound, one shape, one gesture, for 25 to 40 year-olds who want to bring friends something to share.

## Locked visual direction and compliance checklist

- **Palette and lighting:** Bright, clean natural daylight on solid flat colour-block backdrops — sky blue `#8DC6E8` (`Il Classico`) primary, cream `#F9F2E9` secondary (end-card and light grounds), yellow `#F9C86A` accent. Never use dark moody "gourmet" lighting.
- **Layout grammar:** Split two-block colour composition (one half per side) mirroring the act of dividing; optional wheat-ear pattern (`02_BRAND/Pattern/`) for graphic backgrounds.
- **Typography and logo placement:** `Playfair Display` or `Didot` for titles (substituting commercial `Alga`), `Lato` for body and CTAs. White logo on colour/photo, Gold `#C9B37A` on `#F9F2E9` cream, clear space >= `F` height.
- **Production compliance guardrails:**
  - Never prompt dough-rolling hands or say _"hand-rolled"_ / _"a mano"_; show oven-exit Rubatà (`nodoso, irregolare, friabile`) and explicitly exclude thin smooth `stirato` sticks.
  - Pass official packaging fronts and 3D mockups as references (`--ref`); fall back to still-only motion or clean compositing if a video model warps pack typography.
  - Keep generated image/video plates text-free with a clean lower third (`9:16` safe zone) so logos, claims, captions, and CTA pills are composited deterministically in post-production.
  - Never reinterpret or animate the logo `y`/`spiga` as a snapped breadstick; keep the official logo whole and static on the end-card only.

## First-step production handoff (WP1 and WP2)

### WP1: Commercial spot beat sheet (26.5 s target, 9:16 and 16:9)

| #   | Shot ID       | Dur   | Visual beat                                                                             | Audio and VO (ElevenLabs / Vertex + Veo snaps)                        |
| --- | ------------- | ----- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 01  | `01-hook`     | 3.0 s | Solid `#8DC6E8` backdrop; two hands of two people snap one knobbly Rubatà, crumbs fly   | Veo native crisp snap only (`veo_audio: true`), no music, no VO       |
| 02  | `02-spiga`    | 2.5 s | Real golden ear of wheat on `#8DC6E8` sky blue                                          | Music enters; VO: _«Comincia da una spiga.»_                          |
| 03  | `03-forno`    | 3.5 s | Freshly baked Rubatà exiting the oven (referenced to official oven photo, no hands)     | VO: _«Rubatà vuol dire arrotolato. Ogni pezzo è diverso.»_            |
| 04  | `04-portici`  | 4.0 s | Early evening under Turin stone arcades; ~30-year-old carrying `Il Classico` under arm  | VO: _«A Torino le cose buone non si dicono in giro.»_                 |
| 05  | `05-tavolo`   | 3.5 s | Home aperitivo with friends; `Il Classico` carton on table, hand slides a Rubatà out    | VO: _«Si passano di mano.»_                                           |
| 06  | `06-crac`     | 3.5 s | Chain of snaps over the table: break, pass half, break again, laughter                  | Three crisp snaps + soft laughter (`veo_audio: true`) on music, no VO |
| 07  | `07-finestra` | 3.0 s | Carton standing among empty glasses and crumbs; die-cut `spiga` window now empty        | Still-only push-in; VO: _«Uno diventa due. Poi finiscono.»_           |
| 08  | `endcard`     | 3.5 s | Cream `#F9F2E9` card, static gold logo PNG, `Il Classico` packshot, claim, and CTA pill | VO: _«Feyles. Si divide, si condivide.»_                              |

### WP2: Coordinated static deliverables plan

| Deliverable ID        | Channel (`docs/track2-wbs.md`) | Ratio  | Visual and copy focus                                                                                          |
| --------------------- | ------------------------------ | ------ | -------------------------------------------------------------------------------------------------------------- |
| `hero-ad-4x5`         | Deliverable 4 (Ad image)       | `4:5`  | Snapped Rubatà between two hands on `#8DC6E8`; _«Spezzatelo. È fatto apposta.»_ + _«Scoprite gli otto gusti»_  |
| `social-story-9x16`   | Deliverable 2 (Social set)     | `9:16` | Aperitivo hands passing Rubatà around `Il Classico`; _«Si divide. Si condivide.»_ / _«A chi va l'altra metà?»_ |
| `social-finestra-1x1` | Deliverable 2 (Social set)     | `1:1`  | Macro on die-cut `spiga` window; _«Dentro c'è quello che deve esserci.»_ + four base ingredients               |
| `social-torino-4x5`   | Deliverable 2 (Social set)     | `4:5`  | Turin arcades handover; _«A Torino le cose buone non si dicono in giro.»_ + Piazza Castello CTA                |
| `web-banner-16x9`     | Deliverable 3 (Web visual)     | `16:9` | Apartment doorway gift handover; _«Portate qualcosa da dividere.»_ + _«Componete la vostra box regalo»_        |
| `print-poster-2x3`    | Deliverable 3 (Print poster)   | `2:3`  | Two-block colour diptych (wheat ear on `#8DC6E8` left, snapped Rubatà on `#F9F2E9` right) + claim              |

<!-- EOF -->
