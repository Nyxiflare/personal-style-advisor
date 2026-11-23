#!/usr/bin/env python3
"""palette_tools.py - small, offline colour helpers for personal-style-advisor.

Standard library only. No network. No image decoding: colours come in as hex
codes (read from a colour-picker app, a product page, or estimated by the model).

Commands
  describe HEX [HEX ...]          lightness, chroma, hue family in plain words
  match HEX --season NAME         nearest colours in a season palette, with distance
  wb --white HEX --sample HEX     correct a sampled colour using a white reference
  contrast --skin HEX --hair HEX [--eyes HEX]   value contrast level
  card --season NAME [--out F]    write a self-contained HTML palette card
  seasons                         list season names in palettes.json

Every result is a measurement of the hex codes given, not a verdict about a
person. Screens, cameras and fabric dyes all shift colour; see the skill's
colour-analysis reference for how to state confidence.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PALETTE_FILE = os.path.join(HERE, "palettes.json")
HEX_RE = re.compile(r"^#?([0-9a-fA-F]{6})$")


# ---------------------------------------------------------------- conversions
def parse_hex(value: str) -> str:
    """Return '#RRGGBB' upper-case or raise ValueError."""
    m = HEX_RE.match(value.strip())
    if not m:
        raise ValueError(f"not a 6-digit hex colour: {value!r}")
    return "#" + m.group(1).upper()


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    h = parse_hex(value)[1:]
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(rgb) -> str:
    return "#" + "".join(f"{max(0, min(255, round(c))):02X}" for c in rgb)


def _srgb_to_linear(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def rgb_to_lab(rgb) -> tuple[float, float, float]:
    """sRGB (0-255) -> CIE L*a*b* (D65 white)."""
    r, g, b = (_srgb_to_linear(c) for c in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.00000
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116

    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def hex_to_lab(value: str):
    return rgb_to_lab(hex_to_rgb(value))


def lab_to_lch(lab):
    L, a, b = lab
    C = math.hypot(a, b)
    h = math.degrees(math.atan2(b, a)) % 360
    return L, C, h


def delta_e_2000(lab1, lab2) -> float:
    """CIEDE2000 colour difference (Sharma, Wu & Dalal 2005 formulation)."""
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cbar = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cbar ** 7 / (Cbar ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if C1p else 0.0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if C2p else 0.0
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    else:
        dhp = h2p - h1p
        if dhp > 180:
            dhp -= 360
        elif dhp < -180:
            dhp += 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp) / 2)
    Lbp = (L1 + L2) / 2
    Cbp = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hbp = (h1p + h2p + 360) / 2
    else:
        hbp = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hbp - 30))
         + 0.24 * math.cos(math.radians(2 * hbp))
         + 0.32 * math.cos(math.radians(3 * hbp + 6))
         - 0.20 * math.cos(math.radians(4 * hbp - 63)))
    d_theta = 30 * math.exp(-(((hbp - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    Sl = 1 + (0.015 * (Lbp - 50) ** 2) / math.sqrt(20 + (Lbp - 50) ** 2)
    Sc = 1 + 0.045 * Cbp
    Sh = 1 + 0.015 * Cbp * T
    Rt = -math.sin(math.radians(2 * d_theta)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2
                     + Rt * (dCp / Sc) * (dHp / Sh))


# ---------------------------------------------------------------- plain words
HUE_FAMILIES = [  # (upper bound of LCh hue angle, name)
    (20, "pink-red"), (45, "red / coral"), (70, "orange / rust"),
    (95, "gold / mustard"), (115, "yellow / olive"), (165, "green"),
    (200, "teal"), (250, "blue / turquoise"), (290, "blue / navy"),
    (330, "purple / plum"), (360, "magenta / berry"),
]


def lightness_word(L: float) -> str:
    if L >= 80:
        return "very light"
    if L >= 65:
        return "light"
    if L >= 45:
        return "medium"
    if L >= 28:
        return "deep"
    return "very deep"


def chroma_word(C: float) -> str:
    if C < 8:
        return "neutral (almost no colour)"
    if C < 25:
        return "muted / soft"
    if C < 45:
        return "moderate"
    return "clear / bright"


def hue_word(h: float, C: float) -> str:
    if C < 8:
        return "neutral"
    for bound, name in HUE_FAMILIES:
        if h < bound:
            return name
    return "magenta / berry"


def describe(value: str) -> dict:
    hx = parse_hex(value)
    L, C, h = lab_to_lch(hex_to_lab(hx))
    return {
        "hex": hx,
        "L": round(L, 1), "C": round(C, 1), "h": round(h, 1),
        "lightness": lightness_word(L),
        "chroma": chroma_word(C),
        "hue_family": hue_word(h, C),
        "words": f"{lightness_word(L)}, {chroma_word(C)} {hue_word(h, C)}",
    }


# ---------------------------------------------------------------- palettes
def load_palettes(path: str = PALETTE_FILE) -> dict:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data["seasons"]


def find_season(name: str, palettes: dict) -> str:
    key = name.strip().lower().replace("_", " ").replace("-", " ")
    aliases = {
        "true spring": "warm spring", "true summer": "cool summer",
        "true autumn": "warm autumn", "true winter": "cool winter",
        "dark autumn": "deep autumn", "dark winter": "deep winter",
        "clear spring": "bright spring", "clear winter": "bright winter",
        "true fall": "warm autumn", "soft fall": "soft autumn", "dark fall": "deep autumn",
    }
    key = aliases.get(key, key)
    for season in palettes:
        if season.lower() == key:
            return season
    raise KeyError(f"unknown season {name!r}; try: {', '.join(palettes)}")


def match(value: str, season: str, palettes: dict, top: int = 3) -> dict:
    hx = parse_hex(value)
    lab = hex_to_lab(hx)
    name = find_season(season, palettes)
    scored = []
    for item in palettes[name]["colours"]:
        scored.append((delta_e_2000(lab, hex_to_lab(item["hex"])), item))
    scored.sort(key=lambda t: t[0])
    best = scored[0][0]
    if best <= 6:
        verdict = "in palette (very close to a palette colour)"
    elif best <= 12:
        verdict = "near palette (same family; check in daylight)"
    elif best <= 20:
        verdict = "borderline (wear away from the face, or test first)"
    else:
        verdict = "off palette (far from every palette colour)"
    return {
        "hex": hx, "season": name, "verdict": verdict,
        "nearest": [{"hex": it["hex"], "name": it["name"], "delta_e": round(d, 1)}
                    for d, it in scored[:top]],
        "note": "Delta E 2000 between hex codes; screen and dye differences can add 5-10.",
    }


# ---------------------------------------------------------------- white balance
def white_balance(white: str, sample: str) -> dict:
    """Correct `sample` by the per-channel gains that turn `white` neutral.

    `white` is how a known white object (printer paper, a white wall) appears in
    the same photo. Returns the corrected sample, the cast found, and a
    confidence level for anything read from the photo.
    """
    wr, wg, wb = hex_to_rgb(white)
    if min(wr, wg, wb) < 40:
        raise ValueError("white reference is too dark to correct from; reshoot with more light")
    target = max(wr, wg, wb)
    gains = (target / wr, target / wg, target / wb)
    sr, sg, sb = hex_to_rgb(sample)
    corrected = rgb_to_hex((sr * gains[0], sg * gains[1], sb * gains[2]))

    L, a, b = hex_to_lab(white)
    cast_strength = math.hypot(a, b)  # how far the "white" is from neutral
    casts = []
    if b > 4:
        casts.append("yellow/orange (warm bulb or golden hour)")
    if b < -4:
        casts.append("blue (shade, overcast, cool LED or screen light)")
    if a > 4:
        casts.append("magenta/pink (some LEDs, beauty filters)")
    if a < -4:
        casts.append("green (fluorescent tubes, foliage bounce)")
    clipped = max(hex_to_rgb(corrected)) >= 254
    if cast_strength <= 5 and L >= 75:
        confidence = "high"
    elif cast_strength <= 15 and L >= 60:
        confidence = "medium"
    else:
        confidence = "low"
    if clipped and confidence == "high":
        confidence = "medium"
    return {
        "white_seen": parse_hex(white), "sample": parse_hex(sample),
        "corrected_sample": corrected,
        "cast": casts or ["none detected"],
        "cast_strength": round(cast_strength, 1),
        "white_lightness": round(L, 1),
        "confidence": confidence,
        "clipped": clipped,
        "note": ("Correction is a simple per-channel gain. It cannot recover detail lost to "
                 "beauty filters, heavy compression or mixed light from two sources."),
    }


# ---------------------------------------------------------------- contrast
def value_contrast(skin: str, hair: str, eyes: str | None = None) -> dict:
    Ls = hex_to_lab(skin)[0]
    Lh = hex_to_lab(hair)[0]
    values = [Ls, Lh] + ([hex_to_lab(eyes)[0]] if eyes else [])
    spread = max(values) - min(values)
    if spread >= 45:
        level = "high"
    elif spread >= 25:
        level = "medium"
    else:
        level = "low"
    return {"skin_L": round(Ls, 1), "hair_L": round(Lh, 1),
            "eyes_L": round(values[2], 1) if eyes else None,
            "spread": round(spread, 1), "contrast": level}


# ---------------------------------------------------------------- card
def card_html(season: str, palettes: dict, person_label: str = "") -> str:
    name = find_season(season, palettes)
    info = palettes[name]
    cells = []
    for item in info["colours"]:
        d = describe(item["hex"])
        text_colour = "#111111" if d["L"] > 60 else "#FFFFFF"
        cells.append(
            f'<div class="sw" style="background:{item["hex"]};color:{text_colour}">'
            f'<b>{html.escape(item["name"])}</b><span>{item["hex"]}</span>'
            f'<small>{html.escape(item["role"])} · {html.escape(d["words"])}</small></div>'
        )
    title = html.escape(f"{name} palette" + (f" for {person_label}" if person_label else ""))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} palette card</title>
<style>
:root{{--bg:#FAFAF7;--ink:#1C1C1C;--muted:#5B5B5B}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151515;--ink:#EDEDED;--muted:#A8A8A8}}}}
body{{margin:0;padding:16px;background:var(--bg);color:var(--ink);font:15px/1.4 system-ui,sans-serif}}
h1{{font-size:20px;margin:0 0 4px}} p{{color:var(--muted);margin:0 0 16px;max-width:60ch}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}}
.sw{{border-radius:10px;padding:12px;min-height:96px;display:flex;flex-direction:column;gap:2px}}
.sw span{{font-family:ui-monospace,monospace;font-size:13px}} .sw small{{font-size:12px;opacity:.9}}
</style></head><body>
<h1>{title}</h1>
<p>{html.escape(info["summary"])} Colours on screens differ from fabric: check in daylight. Each swatch is labelled in words so it can be used without relying on colour vision.</p>
<div class="grid">{''.join(cells)}</div>
</body></html>
"""


# ---------------------------------------------------------------- CLI
def _print(obj) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("describe")
    d.add_argument("hex", nargs="+")
    m = sub.add_parser("match")
    m.add_argument("hex")
    m.add_argument("--season", required=True)
    m.add_argument("--top", type=int, default=3)
    w = sub.add_parser("wb")
    w.add_argument("--white", required=True)
    w.add_argument("--sample", required=True)
    c = sub.add_parser("contrast")
    c.add_argument("--skin", required=True)
    c.add_argument("--hair", required=True)
    c.add_argument("--eyes")
    k = sub.add_parser("card")
    k.add_argument("--season", required=True)
    k.add_argument("--label", default="")
    k.add_argument("--out")
    sub.add_parser("seasons")
    a = p.parse_args(argv)
    try:
        if a.cmd == "describe":
            _print([describe(h) for h in a.hex])
        elif a.cmd == "match":
            _print(match(a.hex, a.season, load_palettes(), a.top))
        elif a.cmd == "wb":
            _print(white_balance(a.white, a.sample))
        elif a.cmd == "contrast":
            _print(value_contrast(a.skin, a.hair, a.eyes))
        elif a.cmd == "card":
            page = card_html(a.season, load_palettes(), a.label)
            if a.out:
                with open(a.out, "w", encoding="utf-8") as fh:
                    fh.write(page)
                print(f"wrote {a.out}")
            else:
                print(page)
        elif a.cmd == "seasons":
            print("\n".join(load_palettes()))
    except (ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
