# AGENTHON 2026: Feyles brand and product kit specification

<!-- (2026-11-21) -->

Verified product data, visual identity specifications, packaging fidelity rules, and tone-of-voice guardrails distilled from the official Track 2 client kit (`00_LEGGIMI.pdf`, `Feyles_guida-identita.pdf`, `Feyles_presentazione-aziendale.pdf`, and `Feyles_testi-e-informazioni.pdf`).

> **IP and usage conditions:** All brand marks, packaging files, official texts, and product photographs in the client kit belong to Feyles Srl and are licensed **exclusively for Agenthon 2026 submissions**.
> They may be passed to generative AI tools as reference inputs for competition deliverables, and raw proprietary binaries or print masters must not be committed to public repositories or redistributed outside the event.

## Source-of-truth hierarchy

When creating prompts, copy, or layouts, resolve any discrepancy in this strict order:

1. **Official client kit** (flat 1:1 print fronts for pack graphics/names, Identity Guide sRGB HEX values, and `Feyles_testi-e-informazioni.pdf` copy rules).
2. **[Track 2 concept lock](track2-concept-lock.md)** (WP0 creative lock).
3. **[Feyles company research](feyles-company-research.md)** and **[Feyles deep research](feyles-deep-research.md)** (background context only; never pull undeclared facts into copy).

## Protagonist, supporting cast, and exclusions

From `00_LEGGIMI.pdf` and `Feyles_testi-e-informazioni.pdf`:

- **Protagonist:** `Il Classico` Rubatà in the **200 g light sky blue carton** (`#8DC6E8`), the flavour _"da cui è cominciato tutto"_.
- **Supporting cast:** `Brichet` 200 g trays for aperitivo; `Cioccorubatà` 150 g cartons and configurable gift boxes (**Large** `47 × 35.5 × 11.5 cm`, **Medium** `30.5 × 27 × 11 cm`) for gifting.
- **Out of scope for the brief (`05_IMMAGINI/Altro/`):** 1.5 kg and 3 kg bulk cartons, 750 g boxes, 280 g biscuit _casette_, and `Lo Speziato` (which has no dedicated pack graphic in the kit; its mockup depicts `Lo Speciale`).
- **Mockup warnings:** Ignore contact strings printed on `Altro/` mockups and do not reuse the cursive `Merry Christmas` script shown on the two gift-box mockups (it is not a brand typeface).

## Verified product catalog (19 retail SKUs)

All Feyles products contain **gluten** and are baked in the same Cambiano plant, so traces of **tree nuts, sesame, soy, and mustard** are possible across the range.
No product is certified or labelled "vegan".
Shelf life: **4 months** loose grissini, **6 months** packaged grissini, **3 months** biscuits (stored cool, dry, away from light).

### Rubatà (8 flavours)

Base ingredients across all Rubatà: soft wheat flour from a trusted mill, malt, salt, and brewer's yeast.
Available formats: `200 g`, `750 g`, `1.5 kg`, `3 kg` (plus `2 kg` single-serve sachets for `L'Extravergine`).

| SKU                        | Pack alias       | Distinguishing ingredients (kit + verified shop labels)                        | 200 g price | 750 g price |
| -------------------------- | ---------------- | ------------------------------------------------------------------------------ | ----------- | ----------- |
| Rubatà Classici            | `Il Classico`    | Lard (`strutto`, 6.8% per shop label); the only flavour containing lard        | €2.90       | €6.90       |
| Rubatà Olio EVO            | `L'Extravergine` | Extra virgin olive oil (5.5%) and olive oil (5.5%)                             | €3.20       | €7.90       |
| Rubatà Polentini           | `Il Polentino`   | Maize flour (26%) and high-oleic sunflower oil                                 | €3.20       | €7.90       |
| Rubatà Light               | `Il Light`       | Type-0 soft wheat flour (92%), malted wheat flour, sea salt, yeast (no fat)    | €2.90       | €6.90       |
| Rubatà Integrali           | `L'Integrale`    | Wholemeal wheat flour and extra virgin olive oil                               | €3.20       | €7.90       |
| Grissini Tre Semi          | `I Tre Semi`     | Sesame, flax, and chia seeds, high-oleic sunflower oil                         | €3.40       | €9.50       |
| Rubatà Speziati            | `Lo Speziato`    | Turmeric (2.3%) and dried rosemary (2.3%), high-oleic sunflower oil (seasonal) | €3.40       | €9.50       |
| Grissini Nocciole Piemonte | `Lo Speciale`    | `Nocciole Piemonte IGP` hazelnut grains and flour, olive oil (tree nuts)       | €3.40       | €9.50       |

### Brichet, Cioccorubatà, and Biscotti (11 SKUs)

| Family         | Pack format                       | Flavours and verified details                                                                                                                                               | Price                            |
| -------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| `Brichet`      | `200 g` aperitivo tray            | `Aglio Olio e Peperoncino`, `Cacio e Pepe` (contains milk), `Cipolla`, `Mediterraneo`                                                                                       | €3.90                            |
| `Cioccorubatà` | `150 g` carton                    | Olive-oil Rubatà coated in **65% chocolate by weight**: `Fondente` (>=70% cocoa), `al Latte` (>=32%), `al Gianduia` (30% hazelnut); all contain soy                         | €6.50                            |
| `Biscotti`     | `280 g` _casetta_, `1 kg`, `2 kg` | Butter and eggs pastry: `Il Granin Gentile` (hazelnut grains/paste), `Il Melighiotto` (maize + lemon peel), `Il Nettarino` (wholemeal + 15% chestnut honey), `Il Vanilloso` | €6.00 (`280 g`), €14.00 (`1 kg`) |

## Visual identity system

### Logo rules (`01_LOGO`)

- The **`y` in Feyles is a drawn wheat ear (`spiga`)**, not a font glyph: never reconstruct the logotype using a typeface.
- **Official variants:** Extended logo (`Logo esteso`), extended logo with descriptor `Tradizione dal 1968` (packaging), `Spiga` alone (only when the Feyles name already appears or space is minimal), and round seal (`Sigillo`: _"Grissinificio Feyles · Tradizione dal 1968"_).
- **Approved logo colours:** White `#FFFFFF` on solid colour blocks or dark photos; Gold `#C9B37A` on white, cream (`panna`), or light backgrounds; Black `#1D1D1B` only for monochrome contexts.
- **Clear space and minimum size:** Maintain free margin at least equal to the height of the `F`. Minimum width: `25 mm` / `120 px` for extended logo, `8 mm` / `40 px` for `Spiga`.
- **Strict prohibitions:** Never deform, tilt, rotate, animate in pieces, morph, add drop shadows/outlines/gradients/effects, place on low-contrast backgrounds, invent custom seals, or depict the `y`/`spiga` as a broken breadstick.

### Official sRGB colour palette (from print masters)

Print-master HEX values take precedence over lighting-shifted photographs and 3D mockups.

| Group         | Label                      | HEX       | Notes                                                               |
| ------------- | -------------------------- | --------- | ------------------------------------------------------------------- |
| Brand         | Oro Feyles                 | `#C9B37A` | Logo on white or cream                                              |
| Brand         | Nero                       | `#1D1D1B` | Monochrome logo and dark ink                                        |
| Brand         | Bianco                     | `#FFFFFF` | Logo and type on solid packaging colours                            |
| Rubatà 200 g  | `Il Classico`              | `#8DC6E8` | Protagonist pack; primary campaign colour                           |
| Rubatà 200 g  | `L'Extravergine`           | `#AAC27E` | Olive green                                                         |
| Rubatà 200 g  | `Il Polentino`             | `#FCC358` | Warm maize yellow                                                   |
| Rubatà 200 g  | `Il Light`                 | `#92B6BC` | Muted blue-grey                                                     |
| Rubatà 200 g  | `L'Integrale`              | `#B1A77E` | Warm taupe                                                          |
| Rubatà 200 g  | `Il Tre Semi`              | `#D7A285` | Terracotta sand                                                     |
| Rubatà 200 g  | `Lo Speciale`              | `#43695B` | Deep forest green                                                   |
| Brichet 200 g | `Aglio Olio e Peperoncino` | `#CF1F34` | Pepper red                                                          |
| Brichet 200 g | `Cacio e Pepe`             | `#EFB787` | Warm peach                                                          |
| Brichet 200 g | `Cipolla`                  | `#B17EB9` | Canonical violet (renders pink in 3D mockups; always use `#B17EB9`) |
| Brichet 200 g | `Mediterraneo`             | `#68916E` | Herb green                                                          |
| Cioccorubatà  | `Fondente`                 | `#7B2838` | Burgundy                                                            |
| Cioccorubatà  | `al Latte`                 | `#0A254A` | Deep navy                                                           |
| Cioccorubatà  | `al Gianduia`              | `#023556` | Prussian blue                                                       |
| Communication | `Giallo`                   | `#F9C86A` | Shop/stand colour block                                             |
| Communication | `Azzurro`                  | `#9BC5E5` | Shop/stand colour block                                             |
| Communication | `Verde salvia`             | `#B0C286` | Shop/stand colour block                                             |
| Communication | `Viola`                    | `#A285A2` | Shop/stand colour block                                             |
| Communication | `Pesca`                    | `#E2BC96` | Shop/stand colour block                                             |
| Communication | `Rosso mattone`            | `#C54F36` | Shop/stand colour block                                             |
| Communication | `Panna`                    | `#F9F2E9` | Cream neutral ground for gold logo                                  |

### Typography and pattern

- **Display / Headlines:** `Alga` (commercial license, not bundled — use high-contrast serif substitutes `Didot` or `Playfair Display`, italicising the article as on packs: _Il_ Classico).
- **Body / Captions / Addresses:** `Lato` (SIL Open Font License, Google Fonts).
- **Background pattern (`02_BRAND/Pattern/`):** Outline wheat ear repeated in quincunx (`a quinconce`), provided in SVG and PNG (`oro-su-bianco`, `bianco-su-azzurro`, `bianco-su-oro`).

### Packaging and product fidelity protocol

- **Shape rule:** Always describe Rubatà as **knobbly, irregular, crumbly, rolled Piedmontese breadsticks, each piece slightly different**, and exclude thin, smooth, uniform `stirato` sticks.
- **Process rule:** Show oven exits or finished breadsticks; **never say "hand-rolled" / "a mano" or show hands shaping dough** (Feyles declares rested, worked, daily-baked dough, not hand-making).
- **Pack rule:** Pass the flat front (`*_fronte.png` / `*-finestra.png`) and 3D mockup together as references. On 200 g cartons, the `spiga` is a **die-cut window** showing real breadsticks behind it. Tone-on-tone `G` marks sit on a separate print varnish plate and are absent from flat fronts.
- **No AI typography or logos:** Keep generated image/video plates text-free and composite real PNG logos and Pillow/vector typography in post-production.

## Tone of voice, copy guardrails, and pronunciation

- **Register:** Address the audience with plural `"voi"` (_«Scriveteci»_, _«Venite a trovarci»_) and refer to the bakery as `"noi"`. Use short sentences and concrete nouns (_farina, strutto, malto, sale, lievito, forno, laboratorio_).
- **Modesty and transparency:** Never brag; the highest pride is a plain statement of fact (_«Il grissino è rimasto lo stesso.»_). Explain Piedmontese terms immediately (_«"Rubatà" vuol dire arrotolato»_). State uncertainty openly (_1679 court story is «tramandata più che documentata»_).
- **Show craft without adjectives:** Convey artisanal care through actions and timing (_l'impasto riposa, arrotolato, si sforna ogni giorno_), never hype labels.
- **Approved words:** `arrotolato`, `nodoso`, `irregolare`, `friabile`, `fragrante`, `sfizioso`, `sgranocchiare`, `si sforna`, `il laboratorio`, `la squadra`, `di fiducia`, `della tradizione`, `di una volta`.
- **Forbidden words (never use):** `eccellenza`, `passione`, `segreto di famiglia`, `unico`, `premium`, `gourmet`, `esperienza`, `autentico`, `artigianalità`.
- **Forbidden unverified claims:** Never attribute awards, certifications, founders' names, employee counts, production volumes, or export activity to Feyles.
- **Approved kit CTAs (destination `grissinificiofeyles.it`):**
  - _«Scoprite gli otto gusti.»_
  - _«Ordinate online: spediamo in tutta Italia.»_
  - _«Venite a trovarci in piazza Castello.»_
  - _«Componete la vostra box regalo.»_
- **Voiceover pronunciation guide:** `Rubatà` = **ru-ba-TÀ** (stress on final syllable); `Brichet` = **bri-KÈT** (`ch` pronounced hard `k`).

<!-- EOF -->
