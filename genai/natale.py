# Layout functions place many elements by coordinates; splitting them would hurt readability.
# Deliberate copies of a few campaign.py and compose.py layouts, tuned for Christmas.
# pylint: disable=too-many-locals,too-many-arguments,too-many-positional-arguments,duplicate-code
"""WP2 Christmas and Cioccorubatà extension: new files only, next to the existing set.

The Christmas spot tells the 1968-2026 story with Il Cioccorubatà fondente. This script adds
Christmas equivalents of the campaign pieces and the chocolate range, without touching any
file that campaign.py writes (every output name contains "natale", "cioccorubata" or
"gamma-completa"):

    uv run natale.py              # everything
    uv run natale.py gamma choco  # groups: gamma, choco, storia, ad, social, web, print

Same rules as campaign.py: packs, logo and text come from the client kit; the AI plates
(prompts/natale-*.txt) are text-free scenes.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import campaign as K
import compose as C
from compose import BLACK, CREAM, GOLD, cover, font, lockup, pill

HERE = Path(__file__).parent
MOCK = C.KIT / "05_IMMAGINI" / "Mockup confezioni"
FOTO = C.KIT / "05_IMMAGINI" / "Foto"

BURGUNDY = "#7B2838"  # Cioccorubatà fondente (identity guide)
NAVY = "#0A254A"  # Cioccorubatà al latte
PRUSSIAN = "#023556"  # Cioccorubatà al gianduia

FONDENTE = MOCK / "feyles_mockup_astuccio-150g_Cioccorubata-Fondente.png"
BOX = MOCK / "feyles_mockup_box-regalo-media_30-5x27x11cm.png"
CHOCO = [  # pack colour and kit mockup
    (NAVY, MOCK / "feyles_mockup_astuccio-150g_Cioccorubata-al-Latte.png"),
    (BURGUNDY, FONDENTE),
    (PRUSSIAN, MOCK / "feyles_mockup_astuccio-150g_Cioccorubata-al-Gianduia.png"),
]
RUBATA = [(c, MOCK / f"feyles_mockup_astuccio-200g_Rubata-{n}.png") for c, n in K.RANGE]

CTA_ONLINE = "Ordinate online: spediamo in tutta Italia"
SAFE = K.STORY_SAFE_BOTTOM
SIZES = {"9x16": (1080, 1920), "4x5": (1080, 1350), "1x1": (1080, 1080)}

K.PLATES.update(
    {
        "n-hero": "natale-hero4_",
        "n-regalo": "natale-regalo_",
        "n-tavola": "natale-tavola_",
    }
)


def item(canvas: Image.Image, path: Path, height: int, xy: tuple[int, int], anchor="mb") -> None:
    """Any kit mockup at a given height, with the same soft contact shadow as the packshot."""
    im = Image.open(path).convert("RGBA")
    im = im.resize((round(im.width * height / im.height), height), Image.Resampling.LANCZOS)
    x = xy[0] - {"l": 0, "m": im.width // 2, "r": im.width}[anchor[0]]
    y = xy[1] - {"t": 0, "m": im.height // 2, "b": im.height}[anchor[1]]
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse(
        (x + 8, y + im.height - 14, x + im.width - 8, y + im.height + 14),
        fill=(0, 0, 0, 90),
    )
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    canvas.alpha_composite(im, (x, y))


def gift_pair(canvas: Image.Image, height: int, right: int, bottom: int) -> int:
    """Gift box with the fondente pack standing in front of it; returns the left edge."""
    box_h = round(height * 0.62)
    box_w = round(box_h * 800 / 628)
    item(canvas, BOX, box_h, (right, bottom - round(height * 0.04)), "rb")
    pack_w = round(height * 408 / 1148)
    item(canvas, FONDENTE, height, (right - box_w + pack_w // 3, bottom), "mb")
    return right - box_w - pack_w // 6


def stripes(items: list, w: int, h: int, fill: float = 0.8, max_h: float = 0.86) -> Image.Image:
    """Colour stripes, each with its real pack standing on a soft contact shadow."""
    c = Image.new("RGBA", (w, h), CREAM)
    d = ImageDraw.Draw(c)
    sw = w / len(items)
    for i, (colour, path) in enumerate(items):
        x0, x1 = round(i * sw), round((i + 1) * sw)
        d.rectangle((x0, 0, x1, h), fill=colour)
        im = Image.open(path).convert("RGBA")
        ph = min(round(im.height * sw * fill / im.width), round(h * max_h))
        base = h - round(h * 0.06)
        item(c, path, ph, ((x0 + x1) // 2, base))
    return c


def cta(canvas, label, xy, size, bg=BURGUNDY, fg=CREAM, pad=(44, 22), left=True):
    """Pill; with left=True, xy is the pill's left-centre point instead of its centre."""
    f = font("body-bold", size)
    if left:
        w = ImageDraw.Draw(canvas).textlength(label, font=f)
        xy = (xy[0] + round(w / 2) + pad[0], xy[1])
    pill(canvas, label, xy, f, bg, fg, pad)


# --- Gamma completa: 7 Rubatà + 3 Cioccorubatà --------------------------------------------
def gamma_completa(size: tuple[int, int]) -> Image.Image:
    """«Qual è il vostro?» for the full range: savoury tier on top, chocolate tier below."""
    w, h = size
    c = Image.new("RGBA", size, CREAM)
    d = ImageDraw.Draw(c)
    if w / h > 1.5:  # 16:9: tiers left, cream panel right
        sw = round(w * 0.64)
        top = round(h * 0.55)
        c.alpha_composite(stripes(RUBATA, sw, top), (0, 0))
        c.alpha_composite(stripes(CHOCO, sw, h - top, 0.34), (0, top))
        x = sw + 72
        y = text_lines(d, ["Qual è", "il vostro?"], 96, x, 170)
        d.text(
            (x, y + 30),
            "Otto Rubatà, tre Cioccorubatà.",
            font=font("body", 30),
            fill=BLACK,
        )
        cta(c, CTA_ONLINE, (x, y + 90), 26, K.SKY, BLACK)
        lockup(c, "oro", 190, (x, h - 90), anchor="lb")
        return c
    tall = h / w > 1.7
    band = {True: 760, False: 400 if h / w > 1.2 else 330}[tall]
    area = h - band
    top = round(area * 0.56)
    c.alpha_composite(stripes(RUBATA, w, top), (0, 0))
    c.alpha_composite(stripes(CHOCO, w, area - top, 0.3), (0, top))
    m = 72
    y = text_lines(d, ["Qual è il vostro?"], 92, m, area + 56)
    cta(c, CTA_ONLINE, (m, y + 64), 30, K.SKY, BLACK)
    bottom = h - (SAFE if tall else 56)
    lockup(c, "oro", 190, (w - m, bottom), anchor="rb")
    return c


def text_lines(d, lines, size, x, y, fill=BLACK, italic=False, anchor="la") -> int:
    """Title lines in Playfair; returns the y under the last line."""
    return K.text_lines(
        d,
        lines,
        font("title-italic" if italic else "title-bold", size),
        x,
        y,
        fill,
        1.1,
        anchor,
    )


def build_gamma() -> None:
    """Full-range set: social in three formats, a range ad and a 16:9 web banner."""
    for k, sz in SIZES.items():
        K.save(
            gamma_completa(sz),
            f"02-social/gamma-completa/social-gamma-completa-{k}.png",
        )
    K.save(gamma_completa((1080, 1350)), "04-ad-image/range-completa-ad-4x5.png")
    K.save(
        gamma_completa((1920, 1080)),
        "03-web-print/web/web-banner-gamma-completa-16x9.png",
    )


# --- Cioccorubatà: the three chocolate flavours ------------------------------------------
def choco_post(size: tuple[int, int]) -> Image.Image:
    """«Anche il dolce si divide.»: the three cartons on their colours, product truth below."""
    w, h = size
    tall = h / w > 1.7
    band = {True: 820, False: 520 if h / w > 1.2 else 420}[tall]
    c = Image.new("RGBA", size, CREAM)
    c.alpha_composite(stripes(CHOCO, w, h - band, 0.62), (0, 0))
    d = ImageDraw.Draw(c)
    m = 72
    y = text_lines(d, ["Anche il dolce si divide."], 74 if w >= h * 0.99 else 76, m, h - band + 52)
    facts = [
        "Rubatà all’olio d’oliva ricoperti di cioccolato.",
        "Fondente · al Latte · al Gianduia",
    ]
    y = K.text_lines(d, facts, font("body", 32), m, y + 18, BLACK, 1.45)
    cta(c, K.CTA_REGALO, (m, y + 58), 30)
    bottom = h - (SAFE if tall else 56)
    lockup(c, "oro", 180, (w - m, bottom), anchor="rb")
    return c


def build_choco() -> None:
    """Cioccorubatà concept in the three social formats, plus a 4:5 ad."""
    for k, sz in SIZES.items():
        K.save(choco_post(sz), f"02-social/cioccorubata/social-cioccorubata-{k}.png")
    K.save(choco_post((1080, 1350)), "04-ad-image/cioccorubata-ad-4x5.png")


# --- Storia: Christmas carousel, 1968 to today, real kit photos only -------------------
def slide(top: Image.Image, n: int, total: int, lines: list[str], button=None) -> Image.Image:
    """4:5 slide: picture 0-1000, cream band with the line, counter and spiga mark."""
    w, h, ph = 1080, 1350, 1000
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(top.convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    f = K.fit(d, lines, "title-bold", 60, 860)
    y = K.text_lines(d, lines, f, 72, ph + (52 if button else 70 if len(lines) > 1 else 110))
    if button:
        cta(c, button, (72, y + 52), 30)
    C.paste_width(c, K.SPIGA_ORO, 44, (w - 72, ph + 70), anchor="rt")
    d.text((w - 72, h - 56), f"{n}/{total}", font=font("body", 26), fill=BLACK, anchor="rs")
    return c


def photo(name: str, focus=(0.5, 0.5), lift=1.08) -> Image.Image:
    """Kit photo, cropped to the 1080x1000 slide picture and lifted to campaign daylight."""
    im = ImageEnhance.Brightness(Image.open(FOTO / name).convert("RGB")).enhance(lift)
    return cover(im, 1080, 1000, focus)


def build_storia() -> None:
    """Five 4:5 slides: the long story behind the Christmas spot, in the brand's own words."""
    slides: list[tuple] = [
        (
            photo("feyles_foto_forno-del-vecchio-laboratorio.jpg"),
            ["Grissini Rubatà, dal 1968."],
        ),
        (
            photo("feyles_foto_rubata-all-uscita-del-forno.jpg", lift=1.12),
            [
                "Una famiglia, un laboratorio,",
                "lo stesso grissino da più di cinquant’anni.",
            ],
        ),
        (
            photo("feyles_foto_stabilimento-di-cambiano.jpg"),
            ["Dal laboratorio di Cambiano,", "alle porte di Torino, a casa vostra."],
        ),
        (
            photo("feyles_foto_negozio-di-piazza-castello.jpg", (0.5, 0.42)),
            ["E in piazza Castello, a Torino."],
            K.CTA_NEGOZIO,
        ),
    ]
    total = len(slides) + 1
    for i, s in enumerate(slides, 1):
        K.save(
            slide(s[0], i, total, s[1], s[2] if len(s) > 2 else None),
            f"02-social/carousel-natale/carousel-natale-{i}.png",
        )
    w, ph = 1080, 1000
    end = Image.new("RGBA", (w, 1350), CREAM)
    ImageDraw.Draw(end).rectangle((0, 0, w, ph), fill=BURGUNDY)
    C.tile(
        end,
        C.PATTERN / "feyles_pattern-spiga_bianco-su-oro.png",
        (0, 0, w, ph),
        520,
        0.10,
    )
    gift_pair(end, 760, w - 150, 900)
    d = ImageDraw.Draw(end)
    d.text((72, ph + 40), "Da regalare a chi", font=font("title-bold", 56), fill=BLACK)
    d.text(
        (72, ph + 108),
        "apparecchia per tutti.",
        font=font("title-bold", 56),
        fill=BLACK,
    )
    cta(end, K.CTA_REGALO, (72, ph + 230), 28)
    C.paste_width(end, C.logo_path("oro"), 150, (w - 72, ph + 230), anchor="rm")
    d.text(
        (w - 72, 1350 - 40),
        f"{total}/{total}",
        font=font("body", 26),
        fill=BLACK,
        anchor="rs",
    )
    K.save(end, f"02-social/carousel-natale/carousel-natale-{total}.png")


# --- Christmas ad: grandparent and grandchild snap one Cioccorubatà ----------------------
def natale_ad(size: tuple[int, int]) -> Image.Image:
    """«Dal 1968 si passa di mano.» on the burgundy plate, cream band with CTA and lockup."""
    w, h = size
    k = w / 1080  # the bus-shelter poster reuses this layout at 2400 px wide
    tall = h / w > 1.7
    band = round(k * (640 if tall else (420 if h / w > 1.2 else 300)))
    vis = h - band
    head_y = round(k * ((300 if tall else 80) if h / w >= 1.2 else 44))
    s = round(k * (100 if h / w >= 1.2 else 84))
    head_bottom = head_y + round(s * 1.1) + round(s * 0.78 * 1.1)
    p = K.plate("n-hero")
    p = p.resize((w, round(p.height * w / p.width)), Image.Resampling.LANCZOS)
    # flying crumbs start ~37% down the plate: keep them clear under the headline
    top = round(p.height * 0.36) - head_bottom - round(40 * k)
    if top < 0:
        p, top = K.extend_top(p, -top), 0
    if p.height < top + vis:  # plate bottom is flat burgundy: stretch its last row
        ext = Image.new("RGB", (w, top + vis))
        ext.paste(p, (0, 0))
        ext.paste(
            p.crop((0, p.height - 1, w, p.height)).resize((w, top + vis - p.height)),
            (0, p.height),
        )
        p = ext
    c = Image.new("RGBA", size, CREAM)
    c.alpha_composite(p.crop((0, top, w, top + vis)).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    y = text_lines(d, ["Dal 1968"], s, w // 2, head_y, CREAM, anchor="ma")
    text_lines(d, ["si passa di mano."], round(s * 0.78), w // 2, y, CREAM, True, "ma")
    cta(
        c,
        K.CTA_REGALO,
        (w // 2, vis + round(80 * k)),
        round(34 * k),
        left=False,
        pad=(round(44 * k), round(22 * k)),
    )
    lockup(
        c,
        "oro",
        round(210 * k),
        (w // 2 - round(70 * k), vis + round(k * (210 if band > 300 * k else 200))),
    )
    pack = band - round(70 * k) if band <= 420 * k else round(380 * k)
    item(c, FONDENTE, pack, (w - round(90 * k), h - (SAFE if tall else round(36 * k))))
    return c


def build_ad() -> None:
    """Deliverable 4, Christmas: the ad in 4:5, 1:1 and 9:16."""
    for k, sz in SIZES.items():
        K.save(natale_ad(sz), f"04-ad-image/natale-ad-{k}.png")


# --- Christmas social scenes ------------------------------------------------------------
def scene(src, size, photo_h, focus, headline, button, sticker=None, gift=False) -> Image.Image:
    """Photo on top, cream block below: headline, CTA, lockup, fondente pack or gift pair."""
    w, h = size
    m = round(w * 0.06)
    bottom = h - (SAFE if h / w > 1.7 else m)
    c = Image.new("RGBA", size, CREAM)
    c.alpha_composite(cover(src, w, photo_h, focus).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    pack_h = min(round((bottom - photo_h) * 0.92), round(h * 0.3))
    pack_w = round(pack_h * (1.1 if gift else 0.36))
    text_w = w - 2 * m - pack_w - m // 2
    y = photo_h + (round(w * 0.085) if sticker else m)
    hf = K.fit(d, headline, "title-bold", round(w * 0.066), text_w)
    y = K.text_lines(d, headline, hf, m, y, leading=1.15)
    if button:
        cta(
            c,
            button,
            (m, y + round(w * 0.05)),
            round(w * 0.026),
            pad=(round(w * 0.035), round(w * 0.018)),
        )
    lockup(c, "oro", max(160, round(w * 0.16)), (m, bottom), anchor="lb")
    if gift:
        gift_pair(c, pack_h, w - m, bottom)
    else:
        item(c, FONDENTE, pack_h, (w - m - pack_w // 2, bottom))
    if sticker:
        pill(
            c,
            sticker,
            (w // 2, photo_h),
            font("body-black", round(w * 0.04)),
            BURGUNDY,
            CREAM,
            (round(w * 0.06), round(w * 0.028)),
        )
    return c


def build_social() -> None:
    """Christmas table and Christmas gift concepts in 9:16, 4:5 and 1:1."""
    photo_h = {"9x16": 1100, "4x5": 800, "1x1": 580}
    for k, sz in SIZES.items():
        K.save(
            scene(
                K.plate("n-tavola"),
                sz,
                photo_h[k],
                (0.5, 0.55),
                ["Si divide.", "Si condivide."],
                None,
                "A chi va l’altra metà?",
            ),
            f"02-social/natale-tavola/social-natale-tavola-{k}.png",
        )
        K.save(
            scene(
                K.plate("n-regalo"),
                sz,
                photo_h[k],
                (0.3, 0.45),
                ["Da regalare a chi", "apparecchia per tutti."],
                K.CTA_REGALO,
                gift=True,
            ),
            f"02-social/natale-regalo/social-natale-regalo-{k}.png",
        )


# --- Web --------------------------------------------------------------------------------
def banner(size: tuple[int, int]) -> Image.Image:
    """16:9 web banner: Christmas doorway left, cream block right with gift pair and CTA."""
    w, h = size
    split = round(w * 0.6)
    c = Image.new("RGBA", size, CREAM)
    c.alpha_composite(cover(K.plate("n-regalo"), split, h, (0.3, 0.5)).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    cx = split + (w - split) // 2
    y = text_lines(d, ["Da regalare a chi", "apparecchia per tutti."], 58, cx, 90, anchor="ma")
    gift_pair(c, 430, cx + 230, y + 470)
    cta(c, K.CTA_REGALO, (cx, y + 545), 30, left=False)
    lockup(c, "oro", 200, (cx, h - 90))
    return c


def display(size: tuple[int, int]) -> Image.Image:
    """IAB display set, Christmas gift message (spiga mark where the logo can't fit)."""
    src = K.plate("n-regalo")
    c = Image.new("RGBA", size, CREAM)
    d = ImageDraw.Draw(c)
    head = "Da regalare a chi apparecchia per tutti."
    if size == (300, 250):
        c.alpha_composite(cover(src, 300, 90, (0.3, 0.42)).convert("RGBA"), (0, 0))
        text_lines(d, ["Da regalare a chi", "apparecchia per tutti."], 17, 150, 98, anchor="ma")
        pill(c, K.CTA_REGALO, (150, 166), font("body-bold", 12), BURGUNDY, CREAM, (14, 7))
        C.paste_width(c, C.logo_path("oro"), 110, (150, 228), anchor="mb")
    elif size == (300, 600):
        c.alpha_composite(cover(src, 300, 300, (0.28, 0.45)).convert("RGBA"), (0, 0))
        y = text_lines(d, ["Da regalare", "a chi apparecchia", "per tutti."], 26, 20, 320)
        item(c, FONDENTE, 170, (262, 560))
        pill(
            c,
            K.CTA_REGALO,
            (130, y + 34),
            font("body-bold", 12),
            BURGUNDY,
            CREAM,
            (14, 9),
        )
        C.paste_width(c, C.logo_path("oro"), 120, (20, 570), anchor="lb")
    elif size == (728, 90):
        c.alpha_composite(cover(src, 200, 90, (0.3, 0.42)).convert("RGBA"), (0, 0))
        d.text((216, 12), head, font=font("title-bold", 21), fill=BLACK)
        pill(
            c,
            K.CTA_REGALO,
            (216 + 108, 64),
            font("body-bold", 12),
            BURGUNDY,
            CREAM,
            (14, 7),
        )
        item(c, FONDENTE, 80, (636, 86))
        C.paste_width(c, K.SPIGA_ORO, 36, (695, 45))
    elif size == (320, 100):
        item(c, FONDENTE, 88, (26, 95))
        text_lines(d, ["Da regalare a chi", "apparecchia per tutti."], 15, 52, 12)
        pill(
            c,
            K.CTA_REGALO,
            (52 + 86, 76),
            font("body-bold", 10),
            BURGUNDY,
            CREAM,
            (8, 6),
        )
        C.paste_width(c, K.SPIGA_ORO, 36, (296, 50))
    return c


def build_web() -> None:
    """Deliverable 3, web: Christmas banner and display set."""
    K.save(banner((1920, 1080)), "03-web-print/web/web-banner-natale-16x9.png")
    for sz in [(300, 250), (300, 600), (728, 90), (320, 100)]:
        K.save(display(sz), f"03-web-print/web/display-natale-{sz[0]}x{sz[1]}.png")


# --- Print ------------------------------------------------------------------------------
def magazine() -> Image.Image:
    """A4 page (2480x3508, 300 dpi): the Christmas gift message with body copy."""
    w, h = 2480, 3508
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(cover(K.plate("n-regalo"), w, 1900, (0.32, 0.45)).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    m = 200
    y = text_lines(d, ["Da regalare a chi", "apparecchia per tutti."], 170, m, 2040)
    body = [
        "Grissini Rubatà, dal 1968.",
        "Il Cioccorubatà fondente è il nostro Rubatà all’olio d’oliva",
        "ricoperto di cioccolato con almeno il 70% di cacao.",
        "A Natale si spezza a tavola e si passa a chi è accanto.",
    ]
    y = K.text_lines(d, body, font("body", 50), m, y + 60, BLACK, 1.45)
    cta(c, K.CTA_REGALO, (m, y + 110), 56, pad=(70, 36))
    d.text((m, y + 240), "grissinificiofeyles.it", font=font("body-bold", 46), fill=BLACK)
    lockup(c, "oro", 500, (m, h - 170), anchor="lb")
    gift_pair(c, 700, w - 180, h - 170)
    return c


def gift_tag() -> Image.Image:
    """Christmas gift tag 55x95 mm, front and back (300 dpi): gold spiga pattern on burgundy."""
    tw, th = 650, 1122
    front = Image.new("RGBA", (tw, th), BURGUNDY)
    C.tile(
        front,
        C.PATTERN / "feyles_pattern-spiga_bianco-su-oro.png",
        (0, 0, tw, th),
        260,
        0.16,
    )
    C.paste_width(front, C.logo_path("bianco"), 420, (tw // 2, th // 2))
    back = Image.new("RGBA", (tw, th), CREAM)
    d = ImageDraw.Draw(back)
    text_lines(d, ["Buon Natale", "da dividere con"], 64, tw // 2, 220, anchor="ma")
    for y in (560, 680):
        d.line((90, y, tw - 90, y), fill=GOLD, width=3)
    d.text(
        (tw // 2, 850),
        "Si divide. Si condivide.",
        font=font("title-italic", 42),
        fill=BLACK,
        anchor="ma",
    )
    C.paste_width(back, K.SPIGA_ORO, 46, (tw // 2, 1000))
    for side in (front, back):
        ImageDraw.Draw(side).ellipse(
            (tw // 2 - 26, 50, tw // 2 + 26, 102), fill=C.WHITE, outline=GOLD, width=3
        )
    sheet = Image.new("RGBA", (tw * 2 + 60, th), C.WHITE)
    sheet.alpha_composite(front, (0, 0))
    sheet.alpha_composite(back, (tw + 60, 0))
    return sheet


def build_print() -> None:
    """Deliverable 3, traditional: Christmas bus shelter, magazine page and gift tag."""
    K.save(
        natale_ad((2400, 3520)),
        "03-web-print/print/bus-shelter-natale-120x176.png",
        pdf=True,
    )
    K.save(magazine(), "03-web-print/print/magazine-natale-a4.png", pdf=True)
    K.save(gift_tag(), "03-web-print/print/gift-tag-natale-55x95mm.png", pdf=True)


GROUPS = {
    "gamma": build_gamma,
    "choco": build_choco,
    "storia": build_storia,
    "ad": build_ad,
    "social": build_social,
    "web": build_web,
    "print": build_print,
}


def main() -> None:
    """Build the groups named on the command line, or all of them."""
    for group in sys.argv[1:] or list(GROUPS):
        GROUPS[group]()


if __name__ == "__main__":
    main()
