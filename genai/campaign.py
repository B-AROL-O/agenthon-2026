"""WP2 full campaign build: every static deliverable, in every format, into out/drive/.

Builds on compose.py (same helpers, brand rules and plates). One command rebuilds the whole
submission set, so a late copy fix is a single re-run:

    uv run campaign.py            # everything
    uv run campaign.py social     # one group: hero, social, carousel, web, print, mockups

Plates are picked up as the newest out/<prefix>_*.png for each name in PLATES.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import compose as C
from compose import BLACK, CREAM, GOLD, SKY, WHITE, cover, font, lockup, packshot, pill

HERE = Path(__file__).parent
DRIVE = HERE / "out" / "drive"

PLATES = {  # name -> file prefix in out/ (newest wins)
    "hero": "hero-full_",
    "story": "story-full2_",
    "torino": "torino-full_",
    "web": "web-full_",  # web-full2 was rejected (planky sticks); keep the approved plate
    "spiga": "poster-spiga-full_",
    "rubata": "poster-rubata-full_",
    "shelter": "mock-shelter_",
    "billboard": "mock-billboard_",
    "phone": "mock-phone_",
}
FORNO = C.KIT / "05_IMMAGINI" / "Foto" / "feyles_foto_rubata-all-uscita-del-forno.jpg"
NEGOZIO = C.KIT / "05_IMMAGINI" / "Foto" / "feyles_foto_negozio-di-piazza-castello.jpg"
SPIGA_ORO = C.SPIGA / "feyles_spiga_oro_1200px.png"

CTA_GUSTI = "Scoprite gli otto gusti"
CTA_REGALO = "Componete la vostra box regalo"
CTA_NEGOZIO = "Venite a trovarci in piazza Castello"
STORY_SAFE_BOTTOM = 340  # Instagram/TikTok reply bar


def plate(name: str) -> Image.Image:
    """Newest plate file for a name, as RGB."""
    files = sorted((HERE / "out").glob(PLATES[name] + "*"), key=lambda p: p.stat().st_mtime)
    if not files:
        sys.exit(f"missing plate {name!r}: render out/{PLATES[name]}*.png first")
    return Image.open(files[-1]).convert("RGB")


def save(img: Image.Image, rel: str, pdf: bool = False) -> None:
    """Save into the Drive tree (PNG, plus a 300 dpi PDF for print)."""
    path = DRIVE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    rgb = img.convert("RGB")
    rgb.save(path, optimize=True)
    if pdf:
        rgb.save(path.with_suffix(".pdf"), resolution=300, quality=95)
    print(f"saved {path.relative_to(HERE)}")


def fit(draw: ImageDraw.ImageDraw, lines: list[str], kind: str, size: int, max_w: int):
    """Largest font <= size whose longest line fits max_w."""
    while size > 10:
        f = font(kind, size)
        if max(draw.textlength(t, font=f) for t in lines) <= max_w:
            return f
        size -= 2
    return font(kind, size)


def text_lines(draw, lines, fnt, x, y, fill=BLACK, leading=1.15, anchor="la") -> int:
    """Draw lines from top y; return the y under the last line."""
    step = round(fnt.size * leading)
    for i, t in enumerate(lines):
        draw.text((x, y + i * step), t, font=fnt, fill=fill, anchor=anchor)
    return y + len(lines) * step


def feather(img: Image.Image, px: int) -> Image.Image:
    """Fade all four edges of a flat-backdrop plate to transparent over px pixels."""
    a = Image.new("L", img.size, 0)
    ImageDraw.Draw(a).rectangle((px, px, img.width - px, img.height - px), fill=255)
    img.putalpha(a.filter(ImageFilter.GaussianBlur(px / 2)))
    return img


def extend_top(img: Image.Image, extra: int) -> Image.Image:
    """Grow a flat-backdrop plate upwards by stretching its top row (clean sky)."""
    out = Image.new("RGB", (img.width, img.height + extra))
    out.paste(img.crop((0, 0, img.width, 1)).resize((img.width, extra)), (0, 0))
    out.paste(img, (0, extra))
    return out


def hero_photo(w: int) -> tuple[Image.Image, int]:
    """Hero plate at width w, plus the row where the leaked dark backdrop starts."""
    p = plate("hero")
    p = p.resize((w, round(p.height * w / p.width)), Image.LANCZOS)
    return p, C.first_dark_row(p.convert("RGBA"), p.height * 2 // 3)


# --- Social: one concept, three formats ------------------------------------------------
def scene_post(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals
    src: Image.Image,
    size: tuple[int, int],
    photo_h: int,
    focus: tuple[float, float],
    headline: list[str],
    cta: str | None,
    sticker: str | None = None,
    with_lockup: bool = True,
) -> Image.Image:
    """Photo on top, cream block below: headline, CTA pill, lockup, packshot on the right."""
    w, h = size
    m = round(w * 0.06)
    bottom = h - (STORY_SAFE_BOTTOM if h / w > 1.7 else m)
    c = Image.new("RGBA", size, CREAM)
    c.alpha_composite(cover(src, w, photo_h, focus).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)

    pack_h = min(round((bottom - photo_h) * 0.95), round(h * 0.33))
    pack_w = round(pack_h * 0.44)
    text_w = w - 2 * m - pack_w - m // 2
    y = photo_h + (round(w * 0.085) if sticker else m)
    hf = fit(d, headline, "title-bold", round(w * 0.07), text_w)
    y = text_lines(d, headline, hf, m, y, leading=1.15)
    if cta:
        cf = font("body-bold", round(w * 0.028))
        cw = d.textlength(cta, font=cf)
        pad = (round(w * 0.04), round(w * 0.02))
        ph = round(cf.size + 2 * pad[1])
        pill(
            c,
            cta,
            (m + round(cw / 2) + pad[0], y + round(w * 0.025) + ph // 2),
            cf,
            SKY,
            BLACK,
            pad,
        )
        y += round(w * 0.025) + ph
    logo_w = max(160, round(w * 0.17))
    if with_lockup:
        lockup(c, "oro", logo_w, (m, bottom), anchor="lb")
    else:
        C.paste_width(c, C.logo_path("oro"), logo_w, (m, bottom), anchor="lb")
    packshot(c, pack_h, (w - m - pack_w // 2, bottom))
    if sticker:
        sf = font("body-black", round(w * 0.04))
        pill(c, sticker, (w // 2, photo_h), sf, SKY, BLACK, (round(w * 0.06), round(w * 0.028)))
    return c


def hero_post(size: tuple[int, int]) -> Image.Image:
    """Deliverable 4 adapted: sky photo with headline, cream band with CTA and lockup."""
    w, h = size
    p, dark = hero_photo(w)
    tall = h / w > 1.7
    band = 640 if tall else (h - dark if h / w > 1.2 else 300)
    vis = h - band  # visible photo height
    if vis > dark:  # 9:16: grow the sky upwards
        p = extend_top(p.crop((0, 0, w, dark)), vis - dark)
        dark = vis
    top_crop = dark - vis
    c = Image.new("RGBA", size, CREAM)
    c.alpha_composite(p.crop((0, top_crop, w, dark)).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    head_y = (320 if tall else 96) if h / w >= 1.2 else 44
    s = 104 if h / w >= 1.2 else 88
    y = text_lines(
        d, ["Spezzatelo."], font("title-bold", s), w // 2, head_y, anchor="ma", leading=1.08
    )
    d.text(
        (w // 2, y),
        "È fatto apposta.",
        font=font("title-italic", round(s * 0.73)),
        fill=BLACK,
        anchor="ma",
    )
    cf = font("body-bold", 36)
    pill(c, CTA_GUSTI, (w // 2, vis + 83), cf, SKY, BLACK)
    lockup(c, "oro", 220, (w // 2, vis + 219))
    return c


def finestra_vertical(size: tuple[int, int]) -> Image.Image:
    """social-finestra in 4:5 / 9:16: real pack window on top, copy in the cream block."""
    w, h = size
    tall = h / w > 1.7
    photo_h = round(h * (0.52 if tall else 0.56))
    pack = C.pack_with_sticks()
    l, t, r, b = C.PACK_WINDOW
    cx, cy = (l + r) // 2, (t + b) // 2
    ch = (b - t) + 140
    cw = round(ch * w / photo_h)
    crop = pack.crop((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2))
    c = Image.new("RGBA", size, CREAM)
    bg = Image.new("RGBA", (w, photo_h), SKY)
    bg.alpha_composite(cover(crop, w, photo_h))
    c.alpha_composite(bg, (0, 0))
    d = ImageDraw.Draw(c)
    m = 72
    y = text_lines(
        d, ["Dentro c’è quello", "che deve esserci."], font("title-bold", 58), m, photo_h + 64
    )
    d.line((m, y + 26, m + 90, y + 26), fill=GOLD, width=4)
    items = ["farina di grano tenero · strutto", "malto · sale · lievito di birra"]
    text_lines(d, items, font("body", 34), m, y + 56, leading=1.45)
    bottom = h - (STORY_SAFE_BOTTOM if tall else 64)
    lockup(c, "oro", 200, (m, bottom), anchor="lb")
    return c


def build_social() -> None:
    """Every concept in 9:16, 4:5 and 1:1 (deliverable 2 + adaptations of deliverable 4)."""
    sizes = {"9x16": (1080, 1920), "4x5": (1080, 1350), "1x1": (1080, 1080)}
    photo = {"9x16": 1100, "4x5": 820, "1x1": 600}
    for k, sz in sizes.items():
        save(hero_post(sz), f"04-ad-image/hero-ad-{k}.png")
        save(
            scene_post(
                plate("story"),
                sz,
                photo[k],
                (0.5, 0.6),
                ["Si divide.", "Si condivide."],
                None,
                "A chi va l’altra metà?",
                with_lockup=False,
            ),
            f"02-social/condivisione/social-condivisione-{k}.png",
        )
        save(
            scene_post(
                plate("torino"),
                sz,
                photo[k],
                (0.5, 0.45),
                ["A Torino le cose buone", "non si dicono in giro."],
                CTA_NEGOZIO,
            ),
            f"02-social/torino/social-torino-{k}.png",
        )
        save(
            scene_post(
                plate("web"),
                sz,
                photo[k],
                (0.34, 0.45),
                ["Portate qualcosa", "da dividere."],
                CTA_REGALO,
            ),
            f"02-social/regalo/social-regalo-{k}.png",
        )
        if k == "1x1":
            save(C.social_finestra_1x1([], ""), "02-social/finestra/social-finestra-1x1.png")
        else:
            save(finestra_vertical(sz), f"02-social/finestra/social-finestra-{k}.png")


# --- Carousel: the spot's story in six slides ------------------------------------------
def slide(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    top: Image.Image, n: int, lines: list[str], cta: str | None = None
) -> Image.Image:
    """4:5 carousel slide: picture 0-1000, cream band with the line, counter and spiga mark."""
    w, h, ph = 1080, 1350, 1000
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(top.convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    f = fit(d, lines, "title-bold", 60, 820)
    y = text_lines(d, lines, f, 72, ph + (52 if cta else 70 if len(lines) > 1 else 110))
    if cta:
        cf = font("body-bold", 30)
        cw = d.textlength(cta, font=cf)
        pill(c, cta, (72 + round(cw / 2) + 44, y + 52), cf, SKY, BLACK, (44, 22))
    C.paste_width(c, SPIGA_ORO, 44, (w - 72, ph + 70), anchor="rt")
    d.text((w - 72, h - 56), f"{n}/6", font=font("body", 26), fill=BLACK, anchor="rs")
    return c


def build_carousel() -> None:
    """Six 4:5 slides that retell the spot (beats 02-07) with two real kit photos."""
    w, ph = 1080, 1000
    s1 = Image.new("RGBA", (w, ph), SKY)
    C.tile(s1, C.PATTERN / "feyles_pattern-spiga_bianco-su-azzurro.png", (0, 0, w, ph), 520, 0.18)
    ear = C.key_out(plate("spiga"))
    ear = ear.crop(ear.getchannel("A").getbbox())
    ear = ear.resize((round(ear.width * 900 / ear.height), 900), Image.LANCZOS)
    s1.alpha_composite(ear, (w // 2 - ear.width // 2, 60))
    forno = ImageEnhance.Brightness(Image.open(FORNO).convert("RGB")).enhance(1.12)
    p, dark = hero_photo(w)
    s3 = p.crop((0, max(0, dark - ph), w, dark))
    shop = cover(Image.open(NEGOZIO).convert("RGB"), w, ph, (0.5, 0.42))

    end = Image.new("RGBA", (w, ph), CREAM)
    ImageDraw.Draw(end).rectangle((0, 0, w // 2, ph), fill=SKY)
    packshot(end, 760, (w // 2, 900))
    slides = [
        (s1, ["Comincia da una spiga."], None),
        (
            cover(forno, w, ph, (0.5, 0.5)),
            ["Rubatà vuol dire arrotolato.", "Ogni pezzo è diverso."],
            None,
        ),
        (s3, ["Spezzatelo. È fatto apposta."], None),
        (cover(plate("story"), w, ph, (0.5, 0.6)), ["Si passano di mano."], None),
        (shop, ["A Torino le cose buone", "non si dicono in giro."], CTA_NEGOZIO),
    ]
    for i, (img, lines, cta) in enumerate(slides, 1):
        save(slide(img, i, lines, cta), f"02-social/carousel/carousel-{i}.png")
    last = Image.new("RGBA", (w, 1350), CREAM)
    last.alpha_composite(end, (0, 0))
    d = ImageDraw.Draw(last)
    d.text((72, ph + 52), "Uno diventa due.", font=font("title-bold", 60), fill=BLACK)
    pill(last, CTA_GUSTI, (72 + 200, ph + 170), font("body-bold", 30), SKY, BLACK, (44, 22))
    lockup(last, "oro", 170, (w - 72, ph + 170), anchor="rm")
    d.text((w - 72, 1350 - 56), "6/6", font=font("body", 26), fill=BLACK, anchor="rs")
    save(last, "02-social/carousel/carousel-6.png")


# --- Web: banner, display set, homepage hero -------------------------------------------
def display(size: tuple[int, int]) -> Image.Image:  # pylint: disable=too-many-locals
    """IAB display ads with the gift message. Where the full logo can't keep its clear space
    (90-100 px tall formats), the brand's own rule allows the spiga mark alone."""
    web = plate("web")
    c = Image.new("RGBA", size, CREAM)
    d = ImageDraw.Draw(c)
    if size == (300, 250):
        c.alpha_composite(cover(web, 300, 80, (0.34, 0.42)).convert("RGBA"), (0, 0))
        d.text(
            (150, 90),
            "Portate qualcosa da dividere.",
            font=font("title-bold", 18),
            fill=BLACK,
            anchor="ma",
        )
        pill(c, CTA_REGALO, (150, 140), font("body-bold", 12), SKY, BLACK, (14, 7))
        C.paste_width(c, C.logo_path("oro"), 120, (150, 220), anchor="mb")
    elif size == (300, 600):
        c.alpha_composite(cover(web, 300, 330, (0.3, 0.45)).convert("RGBA"), (0, 0))
        y = text_lines(d, ["Portate", "qualcosa", "da dividere."], font("title-bold", 30), 20, 350)
        packshot(c, 170, (250, 420))
        pill(c, CTA_REGALO, (150, y + 32), font("body-bold", 13), SKY, BLACK, (16, 9))
        C.paste_width(c, C.logo_path("oro"), 130, (20, 565), anchor="lb")
    elif size == (728, 90):
        c.alpha_composite(cover(web, 200, 90, (0.34, 0.42)).convert("RGBA"), (0, 0))
        d.text((220, 14), "Portate qualcosa da dividere.", font=font("title-bold", 24), fill=BLACK)
        pill(c, CTA_REGALO, (220 + 110, 63), font("body-bold", 12), SKY, BLACK, (14, 7))
        packshot(c, 76, (620, 83))
        C.paste_width(c, SPIGA_ORO, 40, (690, 45))
    elif size == (320, 100):
        packshot(c, 84, (32, 92))
        text_lines(d, ["Portate qualcosa", "da dividere."], font("title-bold", 16), 62, 12)
        pill(c, CTA_REGALO, (62 + 88, 74), font("body-bold", 10), SKY, BLACK, (9, 6))
        C.paste_width(c, SPIGA_ORO, 40, (296, 50))
    return c


def homepage(size: tuple[int, int]) -> Image.Image:
    """Homepage hero section concept (desktop or mobile) for grissinificiofeyles.it."""
    w, h = size
    mobile = w < 800
    c = Image.new("RGBA", size, CREAM)
    d = ImageDraw.Draw(c)
    nav = 72 if mobile else 88
    C.paste_width(
        c, C.logo_path("oro"), 120 if mobile else 150, (24 if mobile else 64, nav // 2), anchor="lm"
    )
    if mobile:
        for i in range(3):
            d.line(
                (w - 56, nav // 2 - 10 + i * 10, w - 24, nav // 2 - 10 + i * 10),
                fill=BLACK,
                width=3,
            )
    else:
        items = ["Rubatà", "Brichet", "Regali", "Il laboratorio", "Negozio"]
        x = w - 64
        for t in reversed(items):
            d.text((x, nav // 2), t, font=font("body", 18), fill=BLACK, anchor="rm")
            x -= d.textlength(t, font=font("body", 18)) + 36
    if mobile:
        c.alpha_composite(cover(plate("web"), w, 420, (0.34, 0.45)).convert("RGBA"), (0, nav))
        y = text_lines(
            d, ["Portate qualcosa", "da dividere."], font("title-bold", 34), 24, nav + 452
        )
        d.text(
            (24, y + 10),
            "Il Classico, il Rubatà da cui è cominciato tutto.",
            font=font("body", 15),
            fill=BLACK,
        )
        pill(c, CTA_REGALO, (24 + 128, y + 82), font("body-bold", 16), SKY, BLACK, (20, 14))
        lockup(c, "oro", 120, (24, h - 40), anchor="lb")
    else:
        split = round(w * 0.58)
        c.alpha_composite(
            cover(plate("web"), split, h - nav, (0.32, 0.5)).convert("RGBA"), (0, nav)
        )
        x0 = split + 64
        y = text_lines(
            d, ["Portate qualcosa", "da dividere."], font("title-bold", 52), x0, nav + 90
        )
        d.text(
            (x0, y + 14),
            "Il Classico, il Rubatà da cui è cominciato tutto.",
            font=font("body", 18),
            fill=BLACK,
        )
        packshot(c, 340, (w - 95, h - 120))
        pill(c, CTA_REGALO, (x0 + 175, y + 100), font("body-bold", 20), SKY, BLACK, (28, 16))
        lockup(c, "oro", 140, (x0, h - 48), anchor="lb")
    return c


def build_web() -> None:
    """Deliverable 3, web: banner, IAB display set, homepage hero (desktop + mobile)."""
    save(C.web_banner_16x9([plate("web")], ""), "03-web-print/web/web-banner-16x9.png")
    for sz in [(300, 250), (300, 600), (728, 90), (320, 100)]:
        save(display(sz), f"03-web-print/web/display-{sz[0]}x{sz[1]}.png")
    save(homepage((1440, 810)), "03-web-print/web/homepage-hero-desktop.png")
    save(homepage((390, 844)), "03-web-print/web/homepage-hero-mobile.png")


# --- Print / traditional ----------------------------------------------------------------
def billboard() -> Image.Image:
    """6x3 m billboard (2:1 proof at 4000x2000): wheat ear | snapped Rubatà, claim, packshot."""
    w, h = 4000, 2000
    col = w // 2
    c = Image.new("RGBA", (w, h), SKY)
    c.paste(CREAM, (col, 0, w, h))
    C.tile(c, C.PATTERN / "feyles_pattern-spiga_bianco-su-azzurro.png", (0, 0, col, h), 600, 0.18)
    ear = C.key_out(plate("spiga"))
    ear = ear.crop(ear.getchannel("A").getbbox())
    ear = ear.resize((round(ear.width * 1700 / ear.height), 1700), Image.LANCZOS)
    c.alpha_composite(ear, (420 - ear.width // 2, 150))
    rub = plate("rubata")
    box = C.key_out(rub, 18, 40).getchannel("A").getbbox()
    focus = ((box[0] + box[2]) / 2 / rub.width, (box[1] + box[3]) / 2 / rub.height)
    r = cover(C.match_backdrop(rub, CREAM), 900, h, focus).rotate(90, expand=True)
    r = feather(cover(r, 1300, 820).convert("RGBA"), 140)
    c.alpha_composite(r, (w - 1300 - 120, 100))
    d = ImageDraw.Draw(c)
    claim = font("title-bold", 200)
    d.text((col - 120, 1150), "Si divide.", font=claim, fill=BLACK, anchor="rs")
    d.text((col + 120, 1150), "Si condivide.", font=claim, fill=BLACK, anchor="ls")
    packshot(c, 760, (col + 1700, h - 110))
    C.paste_width(c, C.logo_path("oro"), 620, (col + 120, h - 230), anchor="lb")
    return c


def magazine() -> Image.Image:
    """A4 magazine page (2480x3508, 300 dpi): the gift message with body copy."""
    w, h = 2480, 3508
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(cover(plate("web"), w, 1900, (0.36, 0.45)).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    m = 200
    y = text_lines(
        d, ["Portate qualcosa", "da dividere."], font("title-bold", 190), m, 2060, leading=1.08
    )
    body = [
        "Il Classico è il Rubatà da cui è cominciato tutto:",
        "farina, strutto, malto, sale e lievito, arrotolato",
        "e sfornato ogni giorno. Ogni pezzo è diverso.",
        "Si spezza con le mani e si passa a chi è accanto.",
    ]
    y = text_lines(d, body, font("body", 54), m, y + 70, leading=1.45)
    pill(c, CTA_REGALO, (m + 520, y + 120), font("body-bold", 58), SKY, BLACK, (70, 36))
    d.text((m, y + 260), "grissinificiofeyles.it", font=font("body-bold", 48), fill=BLACK)
    lockup(c, "oro", 520, (m, h - 170), anchor="lb")
    packshot(c, 1150, (w - 420, h - 170))
    return c


def mupi() -> Image.Image:
    """Bus-shelter poster 120x176 cm (2400x3520 proof): the hero gesture, claim lockup."""
    w, h = 2400, 3520
    p, dark = hero_photo(w)
    band = 900
    vis = h - band
    if vis > dark:
        p = extend_top(p.crop((0, 0, w, dark)), vis - dark)
        dark = vis
    c = Image.new("RGBA", (w, h), CREAM)
    c.alpha_composite(p.crop((0, dark - vis, w, dark)).convert("RGBA"), (0, 0))
    d = ImageDraw.Draw(c)
    d.text((w // 2, 300), "Spezzatelo.", font=font("title-bold", 250), fill=BLACK, anchor="ma")
    d.text(
        (w // 2, 580), "È fatto apposta.", font=font("title-italic", 180), fill=BLACK, anchor="ma"
    )
    pill(c, CTA_GUSTI, (w // 2, vis + 200), font("body-bold", 80), SKY, BLACK, (120, 56))
    lockup(c, "oro", 480, (w // 2, vis + 560))
    return c


def gift_tag() -> Image.Image:
    """Shop gift tag 55x95 mm, front and back side by side (300 dpi), for piazza Castello."""
    tw, th = 650, 1122
    front = Image.new("RGBA", (tw, th), SKY)
    C.tile(
        front, C.PATTERN / "feyles_pattern-spiga_bianco-su-azzurro.png", (0, 0, tw, th), 260, 0.25
    )
    C.paste_width(front, C.logo_path("bianco"), 420, (tw // 2, th // 2))
    back = Image.new("RGBA", (tw, th), CREAM)
    d = ImageDraw.Draw(back)
    text_lines(d, ["Da dividere", "con"], font("title-bold", 76), tw // 2, 230, anchor="ma")
    for y in (560, 680):
        d.line((90, y, tw - 90, y), fill=GOLD, width=3)
    d.text(
        (tw // 2, 850),
        "Si divide. Si condivide.",
        font=font("title-italic", 42),
        fill=BLACK,
        anchor="ma",
    )
    C.paste_width(back, SPIGA_ORO, 46, (tw // 2, 1000))
    for side in (front, back):  # hole for the string
        ImageDraw.Draw(side).ellipse(
            (tw // 2 - 26, 50, tw // 2 + 26, 102), fill=WHITE, outline=GOLD, width=3
        )
    sheet = Image.new("RGBA", (tw * 2 + 60, th), WHITE)
    sheet.alpha_composite(front, (0, 0))
    sheet.alpha_composite(back, (tw + 60, 0))
    return sheet


def build_print() -> None:
    """Deliverable 3, traditional: poster, billboard, magazine page, bus shelter, gift tag."""
    save(
        C.print_poster_2x3([plate("spiga"), plate("rubata")], ""),
        "03-web-print/print/print-poster-2x3.png",
        pdf=True,
    )
    # Viewing copy under the Drive connector's 10 MB upload limit (the PDF is the print master)
    Image.open(DRIVE / "03-web-print/print/print-poster-2x3.png").convert("RGB").save(
        DRIVE / "03-web-print/print/print-poster-2x3.jpg", quality=95, dpi=(300, 300)
    )
    save(billboard(), "03-web-print/print/billboard-6x3m.png", pdf=True)
    save(magazine(), "03-web-print/print/magazine-a4.png", pdf=True)
    save(mupi(), "03-web-print/print/bus-shelter-120x176.png", pdf=True)
    save(gift_tag(), "03-web-print/print/gift-tag-55x95mm.png", pdf=True)


# --- Mockups: our real files placed into green-screen scenes ----------------------------
def solve(a: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination for the 8x8 perspective system (no numpy needed)."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        for r in range(n):
            if r != col:
                f = m[r][col] / m[col][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [m[i][n] / m[i][i] for i in range(n)]


def green_quad(scene: Image.Image) -> tuple[Image.Image, list[tuple[int, int]]]:
    """Mask of the chroma-green area and its 4 corners (tl, tr, br, bl)."""
    px = scene.load()
    w, h = scene.size
    mask = Image.new("L", (w, h), 0)
    mp = mask.load()
    pts = []
    for y in range(h):
        for x in range(w):
            rr, gg, bb = px[x, y]
            if gg > 150 and gg > rr + 60 and gg > bb + 60:
                mp[x, y] = 255
                pts.append((x, y))
    tl = min(pts, key=lambda p: p[0] + p[1])
    br = max(pts, key=lambda p: p[0] + p[1])
    tr = max(pts, key=lambda p: p[0] - p[1])
    bl = min(pts, key=lambda p: p[0] - p[1])
    return mask.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1)), [
        tl,
        tr,
        br,
        bl,
    ]


def place(scene_name: str, art: Image.Image) -> Image.Image:
    """Warp art onto the green panel of a scene, keeping occluders and edges natural."""
    scene = plate(scene_name)
    mask, quad = green_quad(scene)
    aw, ah = art.size
    src = [(0, 0), (aw, 0), (aw, ah), (0, ah)]
    rows, rhs = [], []
    for (x, y), (u, v) in zip(quad, src):  # map output (x, y) -> input (u, v)
        rows.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        rhs.append(u)
        rows.append([0, 0, 0, x, y, 1, -v * x, -v * y])
        rhs.append(v)
    coeffs = solve(rows, rhs)
    warped = art.convert("RGB").transform(scene.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    out = scene.copy()
    out.paste(warped, (0, 0), mask)
    return out


def build_mockups() -> None:
    """In-context mockups for the pitch and the project sheet."""
    shelter = Image.open(DRIVE / "03-web-print/print/bus-shelter-120x176.png")
    save(place("shelter", shelter), "03-web-print/mockups/mockup-bus-shelter-torino.png")
    bb = Image.open(DRIVE / "03-web-print/print/billboard-6x3m.png")
    save(place("billboard", bb), "03-web-print/mockups/mockup-billboard.png")
    story = Image.open(DRIVE / "02-social/condivisione/social-condivisione-9x16.png")
    save(place("phone", story), "03-web-print/mockups/mockup-phone-story.png")


# --- Range ad: the seven Rubatà packs on their own colours ------------------------------
MOCKUPS = C.KIT / "05_IMMAGINI" / "Mockup confezioni"
RANGE = [  # pack colour (identity guide) and kit mockup, in shelf order
    ("#8DC6E8", "Il-Classico"),
    ("#92B6BC", "Il-Light"),
    ("#FCC358", "Il-Polentino"),
    ("#D7A285", "Il-Tre-Semi"),
    ("#AAC27E", "L-Extravergine"),
    ("#B1A77E", "L-Integrale"),
    ("#43695B", "Lo-Speciale-Nocciole-IGP"),
]


def stripes(w: int, h: int) -> Image.Image:
    """Seven colour stripes, each with its real pack standing on a soft contact shadow."""
    c = Image.new("RGBA", (w, h), CREAM)
    d = ImageDraw.Draw(c)
    sw = w / len(RANGE)
    for i, (colour, name) in enumerate(RANGE):
        x0, x1 = round(i * sw), round((i + 1) * sw)
        d.rectangle((x0, 0, x1, h), fill=colour)
        im = Image.open(MOCKUPS / f"feyles_mockup_astuccio-200g_Rubata-{name}.png").convert("RGBA")
        pw = round(sw * 0.8)
        ph = round(im.height * pw / im.width)
        im = im.resize((pw, ph), Image.LANCZOS)
        cx = (x0 + x1) // 2
        base = round(h * 0.7) if h > w * 1.05 else h - round(h * 0.08)
        sh = Image.new("RGBA", c.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).ellipse(
            (cx - pw // 2 + 4, base - 10, cx + pw // 2 - 4, base + 10), fill=(0, 0, 0, 80)
        )
        c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
        c.alpha_composite(im, (cx - pw // 2, base - ph))
    return c


def range_ad(size: tuple[int, int]) -> Image.Image:
    """«Qual è il vostro?»: one block divided into seven, one per flavour."""
    w, h = size
    c = Image.new("RGBA", size, CREAM)
    d = ImageDraw.Draw(c)
    if w / h > 1.5:  # 16:9: stripes left, cream panel right
        sw = round(w * 0.64)
        c.alpha_composite(stripes(sw, h), (0, 0))
        x = sw + 72
        y = text_lines(d, ["Qual è", "il vostro?"], font("title-bold", 96), x, 170, leading=1.08)
        pill(c, CTA_GUSTI, (x + 190, y + 90), font("body-bold", 32), SKY, BLACK, (44, 22))
        lockup(c, "oro", 190, (x, h - 90), anchor="lb")
        return c
    tall = h / w > 1.7
    band = {True: 760, False: 400 if h / w > 1.2 else 330}[tall]
    c.alpha_composite(stripes(w, h - band), (0, 0))
    m = 72
    y = text_lines(d, ["Qual è il vostro?"], font("title-bold", 92), m, h - band + 56)
    pill(c, CTA_GUSTI, (m + 190, y + 64), font("body-bold", 32), SKY, BLACK, (44, 22))
    bottom = h - (STORY_SAFE_BOTTOM if tall else 56)
    lockup(c, "oro", 190, (w - m, bottom), anchor="rb")
    return c


def build_range() -> None:
    """Range ad in the three social formats, plus a 16:9 web version and the 4:5 as an ad image."""
    for k, sz in {"9x16": (1080, 1920), "4x5": (1080, 1350), "1x1": (1080, 1080)}.items():
        save(range_ad(sz), f"02-social/gamma/social-gamma-{k}.png")
    save(range_ad((1080, 1350)), "04-ad-image/range-ad-4x5.png")
    save(range_ad((1920, 1080)), "03-web-print/web/web-banner-gamma-16x9.png")


GROUPS = {
    "social": build_social,
    "carousel": build_carousel,
    "range": build_range,
    "web": build_web,
    "print": build_print,
    "mockups": build_mockups,
}

if __name__ == "__main__":
    for name in sys.argv[1:] or list(GROUPS):
        GROUPS[name]()
