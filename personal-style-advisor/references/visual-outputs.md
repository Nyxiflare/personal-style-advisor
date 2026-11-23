# Visual outputs: palette cards and mood boards

Written 2026-11. Pick the best option the environment supports. Always offer a visual; never force one.

## Contents
1. Choosing the format
2. Palette card
3. Mood board
4. Outfit sketch (flat lay)
5. Accessibility rules for every visual
6. Privacy rules for visuals

## 1. Choosing the format

| Environment | Palette card | Mood board |
|---|---|---|
| Claude Code / desktop with Python | `python palette_tools.py card --season "<season>" --label "<first name or 'you'>" --out palette.html`, then open or share the file | write a single HTML file (grid of colour blocks, garment descriptions, texture words) |
| claude.ai with artifacts | an HTML artifact with the swatches (same layout as the script's card) | an HTML artifact mood board |
| Plain chat (mobile, API, no artifacts) | a markdown table: name, hex, role, words; plus "save these hex codes in your phone notes" | a text board: 3 lines of mood words, 5 colour names with hex, 5 garments, 3 textures, 2 style-twin recipes |
| Image generation available | optional; describe garments and colours, never generate the user's face or body, never edit their photo | same |

## 2. Palette card

Content, in this order:
1. Title: "<Season or direction> palette" plus the person's first name only if they want it.
2. One line summary (e.g. "Deep, rich and warm-leaning").
3. 12-16 swatches with name, hex, role (face colour / neutral / accent) and the words from
   `palette_tools.py describe` (e.g. "deep, muted orange / rust").
4. Best neutrals (their "black", "white", "navy" substitutes).
5. Metals.
6. Three colours to keep away from the face, with why.
7. Confidence line: "Reading confidence: Medium (photos in warm indoor light). Check in daylight."
8. Footer: "Screens differ from fabric; check colours in daylight."

Wallet version: 8 swatches in two rows, names under each, for a phone lock screen or a printed card.

For between-season results: two half-palettes and a shared row ("works in both").

## 3. Mood board

Build from the person's chosen style families, occasion and palette:
- **Mood words** (3-5): e.g. "regal, warm, rooted".
- **Colour story**: 2 neutrals, 2-3 core colours, 1 accent, in proportions (60 / 30 / 10).
- **Silhouettes**: 3-5 garment descriptions (e.g. "silk-cotton saree with a slim zari border,
  elbow-sleeve sweetheart blouse").
- **Textures**: handloom cotton, raw silk, velvet, linen, knit.
- **Accessories**: jewellery type and metal, footwear, bag, glasses, headwear.
- **Hair and grooming** in one line.
- **Style-twin recipe** cards (one or two).
- **Do-not list** (things that clash with their culture, comfort or palette).

HTML layout tips: CSS grid of cards, colour blocks drawn as divs with the hex as background and
the name printed on top, text in contrasting ink (dark text on light colours, light on dark). No
external images are needed; avoid hotlinking copyrighted photos. If they want reference images,
give search terms instead (e.g. "mustard Kanjivaram maroon border").

## 4. Outfit sketch (flat lay)

A simple HTML or text "flat lay": stacked blocks for top, bottom, outer layer, shoes, jewellery,
each a colour block with its garment name. Useful for checking colour proportions at a glance.

## 5. Accessibility rules

- Every swatch shows its **name and hex in text**. No information is carried by colour alone.
- Text contrast at least 4.5:1 against the swatch (the card generator switches ink by lightness).
- Works on a phone (single column at narrow widths) and in dark mode.

## 6. Privacy rules

- Don't embed the person's photo in a card or board unless they ask, and then only locally.
- Don't upload their photo to third-party image services.
- Use first names only, and only if they want a name on it.
