"""WP2 compositor: put real logos, brand typography and CTAs on text-free AI plates.

Generated plates never contain text or logos (see docs/track2-concept-lock.md).
Everything readable is drawn here, deterministically, from the official kit files.

Usage:
    uv run compose.py hero-ad-4x5 --plate out/hero_123_0.png
    uv run compose.py hero-ad-4x5 --plate out/hero_123_0.png --variant band
    uv run compose.py print-poster-2x3 --plate out/spiga.png --plate out/rubata.png
    uv run compose.py social-finestra-1x1
    uv run compose.py --list

Outputs land in out/final/ (gitignored: they contain Feyles marks).
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
KIT = HERE.parent / "assets" / "feyles"
FONTS = HERE / "fonts"
OUT = HERE / "out" / "final"

# --- Brand palette (Feyles identity guide, sRGB) ----------------------------
SKY = "#8DC6E8"  # Il Classico
CREAM = "#F9F2E9"  # Panna
YELLOW = "#F9C86A"  # Giallo
GOLD = "#C9B37A"  # Oro Feyles
BLACK = "#1D1D1B"  # Nero
WHITE = "#FFFFFF"

LOGO = KIT / "01_LOGO" / "Logo esteso" / "PNG"
SPIGA = KIT / "01_LOGO" / "Spiga" / "PNG"
PATTERN = KIT / "02_BRAND" / "Pattern"
PACK_FRONT = (
    KIT
    / "05_IMMAGINI"
    / "Grafiche confezioni"
    / "feyles_astuccio-200g_Il-Classico_fronte-finestra.png"
)
PACK_WINDOW = (181, 1181, 1178, 2660)  # transparent die-cut spiga window on PACK_FRONT (l, t, r, b)
PACKSHOT = (
    KIT / "05_IMMAGINI" / "Mockup confezioni" / "feyles_mockup_astuccio-200g_Rubata-Il-Classico.png"
)
CLASSICO_PHOTO = KIT / "05_IMMAGINI_2048" / "Grissini" / "CLASSICO_MAX1896.jpg"


def logo_path(colour: str) -> Path:
    """Official extended logo, 2400 px PNG; colour in {bianco, oro, nero}."""
    return LOGO / f"feyles_logo-esteso_{colour}_2400px.png"


# --- Fonts (Alga is commercial and not in the kit: Playfair Display stands in) ---
def font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    """Return a brand font. kind: title, title-italic, body, body-bold, body-black."""
    files = {
        "title": ("PlayfairDisplay[wght].ttf", "Regular"),
        "title-bold": ("PlayfairDisplay[wght].ttf", "Bold"),
        "title-italic": ("PlayfairDisplay-Italic[wght].ttf", "Italic"),
        "body": ("Lato-Regular.ttf", None),
        "body-bold": ("Lato-Bold.ttf", None),
        "body-black": ("Lato-Black.ttf", None),
    }
    name, variation = files[kind]
    f = ImageFont.truetype(str(FONTS / name), size)
    if variation:
        f.set_variation_by_name(variation)
    return f


# --- Drawing primitives -----------------------------------------------------
def cover(img: Image.Image, w: int, h: int, focus: tuple[float, float] = (0.5, 0.5)) -> Image.Image:
    """Scale and crop img to fill w x h, keeping the focus point (fractions) in frame."""
    scale = max(w / img.width, h / img.height)
    r = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    x = min(max(round(r.width * focus[0] - w / 2), 0), r.width - w)
    y = min(max(round(r.height * focus[1] - h / 2), 0), r.height - h)
    return r.crop((x, y, x + w, y + h))


def paste_width(canvas: Image.Image, path: Path, width: int, xy: tuple[int, int], anchor="mm"):
    """Paste a transparent PNG scaled to width; anchor like Pillow text anchors (l/m/r + t/m/b)."""
    im = Image.open(path).convert("RGBA")
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    x, y = xy
    x -= {"l": 0, "m": im.width // 2, "r": im.width}[anchor[0]]
    y -= {"t": 0, "m": im.height // 2, "b": im.height}[anchor[1]]
    canvas.alpha_composite(im, (x, y))
    return im.size


def lockup(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    canvas: Image.Image,
    colour: str,
    logo_w: int,
    xy: tuple[int, int],
    anchor: str = "mm",
    ink: str = BLACK,
) -> tuple[int, int, int, int]:
    """Campaign sign-off, modelled on the piazza Castello shop sign: logo | stacked claim.

    Logo and claim are separated by a thin divider with clear space >= F height on both
    sides (F is ~25% of the logo width). Returns the bounding box (l, t, r, b).
    """
    logo = Image.open(logo_path(colour)).convert("RGBA")
    logo = logo.resize((logo_w, round(logo.height * logo_w / logo.width)), Image.LANCZOS)
    f_h = round(logo_w * 0.25)
    claim = font("title-italic", round(logo_w * 0.135))
    lines = ["Si divide.", "Si condivide."]
    d = ImageDraw.Draw(canvas)
    text_w = max(round(d.textlength(t, font=claim)) for t in lines)
    total_w = logo.width + 2 * f_h + 2 + text_w
    h = logo.height
    x = xy[0] - {"l": 0, "m": total_w // 2, "r": total_w}[anchor[0]]
    y = xy[1] - {"t": 0, "m": h // 2, "b": h}[anchor[1]]
    canvas.alpha_composite(logo, (x, y))
    div_x = x + logo.width + f_h
    rule = GOLD if colour == "oro" else ink
    d.line((div_x, y, div_x, y + h), fill=rule, width=2)
    tx = div_x + 2 + f_h
    step = round(claim.size * 1.12)
    top = y + (h - 2 * step) // 2
    for i, t in enumerate(lines):
        d.text((tx, top + i * step), t, font=claim, fill=ink, anchor="la")
    return (x, y, x + total_w, y + h)


def text_block(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    fnt: ImageFont.FreeTypeFont,
    xy: tuple[int, int],
    fill: str,
    align: str = "center",
    leading: float = 1.15,
):
    """Draw explicit lines (no auto-wrap: line breaks are a copy decision). xy = top centre/left."""
    x, y = xy
    step = round(fnt.size * leading)
    for i, line in enumerate(lines):
        anchor = {"center": "ma", "left": "la", "right": "ra"}[align]
        draw.text((x, y + i * step), line, font=fnt, fill=fill, anchor=anchor)
    return y + len(lines) * step


def pill(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    canvas: Image.Image,
    label: str,
    centre: tuple[int, int],
    fnt: ImageFont.FreeTypeFont,
    bg: str,
    fg: str,
    pad: tuple[int, int] = (56, 26),
):
    """CTA button: rounded pill with centred label."""
    draw = ImageDraw.Draw(canvas)
    l, t, r, b = draw.textbbox((0, 0), label, font=fnt, anchor="lt")
    w, h = r - l + 2 * pad[0], b - t + 2 * pad[1]
    x0, y0 = centre[0] - w // 2, centre[1] - h // 2
    draw.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=h // 2, fill=bg)
    draw.text(centre, label, font=fnt, fill=fg, anchor="mm")


def border_colour(img: Image.Image, margin: int = 12) -> tuple[int, int, int]:
    """Median colour of a thin frame around the image (the flat backdrop of a plate)."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    strips = [(0, 0, w, margin), (0, h - margin, w, h), (0, 0, margin, h), (w - margin, 0, w, h)]
    px = [p for box in strips for p in rgb.crop(box).get_flattened_data()]
    return tuple(sorted(c[i] for c in px)[len(px) // 2] for i in range(3))


def hex_rgb(colour: str) -> tuple[int, int, int]:
    """'#RRGGBB' -> (r, g, b)."""
    return tuple(int(colour[i : i + 2], 16) for i in (1, 3, 5))


def match_backdrop(img: Image.Image, target: str) -> Image.Image:
    """Shift each channel so the plate's flat backdrop lands exactly on the brand colour."""
    src, dst = border_colour(img), hex_rgb(target)
    bands = [
        b.point(lambda v, d=d - s_: max(0, min(255, v + d)))
        for b, s_, d in zip(img.convert("RGB").split(), src, dst)
    ]
    return Image.merge("RGB", bands)


def key_out(img: Image.Image, lo: int = 28, hi: int = 70) -> Image.Image:
    """Remove a flat backdrop: alpha ramps from 0 at colour distance lo to 255 at hi."""
    rgb = img.convert("RGB")
    diff = ImageChops.difference(rgb, Image.new("RGB", rgb.size, border_colour(rgb)))
    r, g, b = diff.split()
    dist = ImageChops.lighter(ImageChops.lighter(r, g), b)
    alpha = dist.point(lambda v: 0 if v <= lo else 255 if v >= hi else (v - lo) * 255 // (hi - lo))
    out = rgb.convert("RGBA")
    out.putalpha(alpha.filter(ImageFilter.GaussianBlur(1)))
    return out


def tile(
    canvas: Image.Image, path: Path, box: tuple[int, int, int, int], width: int, opacity: float
):
    """Tile a pattern PNG into box at the given tile width and opacity."""
    t = Image.open(path).convert("RGBA")
    t = t.resize((width, round(t.height * width / t.width)), Image.LANCZOS)
    t.putalpha(t.getchannel("A").point(lambda v: round(v * opacity)))
    layer = Image.new("RGBA", (box[2] - box[0], box[3] - box[1]), (0, 0, 0, 0))
    for y in range(0, layer.height, t.height):
        for x in range(0, layer.width, t.width):
            layer.alpha_composite(t, (x, y))
    canvas.alpha_composite(layer, box[:2])


# --- Layouts ----------------------------------------------------------------
@dataclass
class Spec:
    """Output size and a short description for --list."""

    size: tuple[int, int]
    about: str


SPECS = {
    "hero-ad-4x5": Spec((1080, 1350), "Snapped Rubatà on sky blue, headline + CTA [plate]"),
    "print-poster-2x3": Spec(
        (3600, 5400), "Diptych: wheat ear | snapped Rubatà + claim [spiga, rubata]"
    ),
    "social-finestra-1x1": Spec((1080, 1080), "Real pack window macro + ingredients [no plate]"),
    "web-banner-16x9": Spec(
        (1920, 1080), "Doorway handover | cream block, packshot, gift CTA [plate]"
    ),
    "social-story-9x16": Spec(
        (1080, 1920), "Aperitivo hands over cream block, claim + friend tag [plate]"
    ),
    "social-torino-4x5": Spec(
        (1080, 1350), "Arcades handover over cream block, piazza Castello CTA [plate]"
    ),
}


def first_dark_row(img: Image.Image, start: int, drop: float = 0.94) -> int:
    """First row below start whose mean luminance falls under drop x the start row's (leaked backdrop)."""
    grey = img.convert("L")

    def lum(y: int) -> float:
        return sum(grey.crop((0, y, img.width, y + 1)).get_flattened_data()) / img.width

    ref = lum(start)
    for y in range(start, img.height):
        if lum(y) < ref * drop:
            return y
    return img.height


def extend_down(c: Image.Image, top: int) -> None:
    """Repaint rows from top down with the clean row just above, keeping its horizontal falloff."""
    clean = c.crop((0, top - 6, c.width, top - 5))
    c.paste(clean.resize((c.width, c.height - top)), (0, top))


def hero_ad_4x5(plates: list[Image.Image], variant: str) -> Image.Image:
    """Deliverable 4: headline top, plate middle, CTA pill and logo bottom.

    Variants: "band" = cream base block with gold logo (split two-block grammar),
    "patch" = sky blue extended down, white logo. Both hide any leaked dark backdrop.
    """
    w, h = SPECS["hero-ad-4x5"].size
    c = cover(plates[0], w, h).convert("RGBA")
    d = ImageDraw.Draw(c)
    dark = first_dark_row(c, h * 2 // 3)

    y = text_block(d, ["Spezzatelo."], font("title-bold", 104), (w // 2, 96), BLACK)
    text_block(d, ["È fatto apposta."], font("title-italic", 76), (w // 2, y - 4), BLACK)

    cta = font("body-bold", 36)
    if variant == "band":
        top = min(dark, h - 300)
        d.rectangle((0, top, w, h), fill=CREAM)
        # clear space >= F height (F is ~25% of logo width): gap pill->logo 62 px, F 55 px
        pill(c, "Scoprite gli otto gusti", (w // 2, top + 83), cta, SKY, BLACK)
        lockup(c, "oro", 220, (w // 2, top + 219))
    else:
        if dark < h:
            extend_down(c, dark)
        pill(c, "Scoprite gli otto gusti", (w // 2, h - 230), cta, CREAM, BLACK)
        paste_width(c, logo_path("bianco"), 300, (w // 2, h - 96))
    return c


def print_poster_2x3(plates: list[Image.Image], _variant: str) -> Image.Image:
    """Deliverable 3 (print): 12x18 in at 300 dpi. Left: wheat ear on sky blue + faint official
    pattern. Right: snapped Rubatà on cream. Claim split across the seam, gold logo on cream."""
    w, h = SPECS["print-poster-2x3"].size
    col = w // 2
    c = Image.new("RGBA", (w, h), SKY)
    c.paste(CREAM, (col, 0, w, h))
    tile(c, PATTERN / "feyles_pattern-spiga_bianco-su-azzurro.png", (0, 0, col, h), 900, 0.18)

    spiga = key_out(plates[0])
    spiga = spiga.crop(spiga.getchannel("A").getbbox())
    sh = 3500
    spiga = spiga.resize((round(spiga.width * sh / spiga.height), sh), Image.LANCZOS)
    c.alpha_composite(spiga, (col // 2 - spiga.width // 2, 420))

    box = key_out(plates[1], 18, 40).getchannel("A").getbbox()
    focus = ((box[0] + box[2]) / 2 / plates[1].width, (box[1] + box[3]) / 2 / plates[1].height)
    rubata = cover(match_backdrop(plates[1], CREAM), col, 4300, focus).convert("RGBA")
    fade = 700  # feather the plate's lower edge into the flat cream so no seam shows
    mask = Image.linear_gradient("L").resize((col, fade)).transpose(Image.FLIP_TOP_BOTTOM)
    alpha = Image.new("L", rubata.size, 255)
    alpha.paste(mask, (0, rubata.height - fade))
    rubata.putalpha(alpha)
    c.alpha_composite(rubata, (col, 0))

    d = ImageDraw.Draw(c)
    claim = font("title-bold", 220)
    base = 4560
    d.text((col // 2, base), "Si divide.", font=claim, fill=BLACK, anchor="ms")
    d.text((col + col // 2, base), "Si condivide.", font=claim, fill=BLACK, anchor="ms")
    d.text(
        (col + col // 2, 4800),
        "grissinificiofeyles.it",
        font=font("body", 64),
        fill=BLACK,
        anchor="ms",
    )
    paste_width(c, logo_path("oro"), 720, (col + col // 2, 5110))  # >= F (180 px) clear space
    return c


def classico_sticks() -> Image.Image:
    """Tight crop of the kit's Classico photo: the 7 sticks with almost no slate around them."""
    photo = Image.open(CLASSICO_PHOTO).convert("RGB")
    k = photo.width / 640
    return photo.crop((round(78 * k), round(140 * k), round(565 * k), round(292 * k)))


def pack_with_sticks() -> Image.Image:
    """Official Il Classico front with real Classico sticks seen through the die-cut window.

    The kit photo (7 sticks on slate) is cropped tight to the sticks, turned vertical and laid
    twice side by side, so the window is filled like the 3D mockup.
    """
    front = Image.open(PACK_FRONT).convert("RGBA")
    l, t, r, b = PACK_WINDOW
    sticks = classico_sticks().rotate(90, expand=True)
    pair = Image.new("RGB", (sticks.width * 2, sticks.height))
    pair.paste(sticks, (0, 0))
    pair.paste(sticks.transpose(Image.FLIP_TOP_BOTTOM), (sticks.width, 0))
    # kit photo is low-key; match campaign daylight
    pair = ImageEnhance.Brightness(pair).enhance(1.15)
    fill = cover(pair, r - l + 60, b - t + 60).convert("RGBA")
    base = Image.new("RGBA", front.size, BLACK)
    base.alpha_composite(fill, (l - 30, t - 30))
    # inner shadow along the cut edge, so the window reads as a hole in the carton
    edge = front.getchannel("A").filter(ImageFilter.GaussianBlur(22))
    shadow = Image.new("RGBA", front.size, (0, 0, 0, 0))
    shadow.putalpha(edge.point(lambda v: round(v * 0.55)))
    base.alpha_composite(shadow, (10, 16))
    base.alpha_composite(front)
    return base


def social_finestra_1x1(_plates: list[Image.Image], _variant: str) -> Image.Image:
    """Deliverable 2: left = macro on the real pack window, right = cream block with copy."""
    w, h = SPECS["social-finestra-1x1"].size
    left = 620
    c = Image.new("RGBA", (w, h), CREAM)
    pack = pack_with_sticks()
    l, t, r, b = PACK_WINDOW
    cx, cy = (l + r) // 2, (t + b) // 2
    cw = (r - l) + 160  # whole window plus a margin of carton
    ch = round(cw * h / left)
    crop = pack.crop((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2))
    c.alpha_composite(crop.resize((left, h), Image.LANCZOS), (0, 0))

    d = ImageDraw.Draw(c)
    x = left + 64  # logo clear space >= F (62 px) from the image edge
    y = text_block(
        d,
        ["Dentro c’è", "quello che", "deve esserci."],
        font("title-bold", 54),
        (x, 150),
        BLACK,
        "left",
        1.2,
    )
    d.line((x, y + 40, x + 90, y + 40), fill=GOLD, width=4)
    items = ["farina di grano tenero", "strutto", "malto", "sale", "lievito di birra"]
    text_block(d, items, font("body", 30), (x, y + 84), BLACK, "left", 1.55)
    paste_width(c, logo_path("oro"), 250, (x, h - 110), anchor="lm")
    return c


def packshot(canvas: Image.Image, height: int, xy: tuple[int, int], anchor: str = "mb") -> None:
    """Real Il Classico 3D mockup with a soft contact shadow (on the product, never the logo)."""
    im = Image.open(PACKSHOT).convert("RGBA")
    im = im.resize((round(im.width * height / im.height), height), Image.LANCZOS)
    x = xy[0] - {"l": 0, "m": im.width // 2, "r": im.width}[anchor[0]]
    y = xy[1] - {"t": 0, "m": im.height // 2, "b": im.height}[anchor[1]]
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse(
        (x + 10, y + im.height - 18, x + im.width - 10, y + im.height + 18), fill=(0, 0, 0, 90)
    )
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    canvas.alpha_composite(im, (x, y))


def web_banner_16x9(plates: list[Image.Image], _variant: str) -> Image.Image:
    """Deliverable 3 (web): photo left 60%, cream block right with headline, packshot, gift CTA."""
    w, h = SPECS["web-banner-16x9"].size
    split = 1152
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(cover(plates[0], split, h, (0.32, 0.5)).convert("RGBA"), (0, 0))

    d = ImageDraw.Draw(c)
    cx = split + (w - split) // 2
    text_block(d, ["Portate qualcosa", "da dividere."], font("title-bold", 70), (cx, 100), BLACK)
    packshot(c, 470, (cx, 770))
    pill(c, "Componete la vostra box regalo", (cx, 860), font("body-bold", 32), SKY, BLACK)
    lockup(c, "oro", 210, (cx, 985))
    return c


def social_story_9x16(plates: list[Image.Image], _variant: str) -> Image.Image:
    """Deliverable 2: aperitivo photo on top, cream block below. Bottom ~340 px kept free for the
    Instagram reply bar; friend-tag sticker straddles the seam."""
    w, h = SPECS["social-story-9x16"].size
    seam = 1100
    c = Image.new("RGBA", (w, h), CREAM)
    # focus 0.6: the final plate (story-full2) has a branded glass at the very top; this crop drops it
    c.alpha_composite(cover(plates[0], w, seam, (0.5, 0.6)).convert("RGBA"), (0, 0))

    d = ImageDraw.Draw(c)
    text_block(
        d,
        ["Si divide.", "Si condivide."],
        font("title-bold", 92),
        (72, seam + 90),
        BLACK,
        "left",
        1.12,
    )
    paste_width(c, logo_path("oro"), 250, (72, seam + 370), anchor="lt")  # bottom 1542 < 1580
    packshot(c, 400, (w - 190, seam + 460))
    pill(c, "A chi va l’altra metà?", (w // 2, seam), font("body-black", 44), SKY, BLACK, (64, 30))
    return c


def social_torino_4x5(plates: list[Image.Image], _variant: str) -> Image.Image:
    """Deliverable 2: arcades photo on top, cream block with headline, packshot and shop CTA."""
    w, h = SPECS["social-torino-4x5"].size
    seam = 900
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(cover(plates[0], w, seam).convert("RGBA"), (0, 0))

    d = ImageDraw.Draw(c)
    y = text_block(
        d,
        ["A Torino le cose buone", "non si dicono in giro."],
        font("title-bold", 56),
        (64, seam + 56),
        BLACK,
        "left",
        1.18,
    )
    cta = "Venite a trovarci in piazza Castello"
    f = font("body-bold", 30)
    l, _, r, _ = d.textbbox((0, 0), cta, font=f)
    pill(c, cta, (64 + (r - l) // 2 + 44, y + 60), f, SKY, BLACK, (44, 22))
    lockup(c, "oro", 180, (64, h - 69), anchor="lb")  # gap to pill >= F (45 px)
    packshot(c, 400, (w - 150, h - 40))
    return c


LAYOUTS = {
    "hero-ad-4x5": hero_ad_4x5,
    "print-poster-2x3": print_poster_2x3,
    "social-finestra-1x1": social_finestra_1x1,
    "web-banner-16x9": web_banner_16x9,
    "social-story-9x16": social_story_9x16,
    "social-torino-4x5": social_torino_4x5,
}


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("layout", nargs="?", choices=sorted(LAYOUTS))
    p.add_argument(
        "--plate",
        type=Path,
        action="append",
        default=[],
        help="text-free plate(s), in layout order",
    )
    p.add_argument("--variant", default="default", help="layout variant (hero: white = white ink)")
    p.add_argument("--list", action="store_true")
    p.add_argument("--make-refs", action="store_true", help="write out/refs/ reference crops")
    a = p.parse_args()

    if a.make_refs:
        refs = HERE / "out" / "refs"
        refs.mkdir(parents=True, exist_ok=True)
        classico_sticks().save(refs / "classico-sticks-crop.jpg", quality=92)
        print(f"saved {refs / 'classico-sticks-crop.jpg'}")
        return

    if a.list or not a.layout:
        for k, s in SPECS.items():
            print(f"{k:22} {s.size[0]}x{s.size[1]}  {s.about}")
        return
    plates = [Image.open(pl).convert("RGB") for pl in a.plate]
    try:
        out = LAYOUTS[a.layout](plates, a.variant).convert("RGB")
    except IndexError:
        sys.exit(f"{a.layout} needs more --plate inputs: {SPECS[a.layout].about}")
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{a.layout}_{a.variant}.png"
    out.save(path, optimize=True)
    print(f"saved {path}")
    if a.layout.startswith("print-"):
        pdf = path.with_suffix(".pdf")
        out.save(pdf, resolution=300, quality=95)
        print(f"saved {pdf}")


if __name__ == "__main__":
    main()
