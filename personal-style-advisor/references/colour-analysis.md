# Colour analysis

Written 2026-11. The method and lighting rules are general colour science and common analyst
practice. The four-dimension order, the check-in and the adjacent-season comparison are ideas
adapted from TrueHue (MIT, see NOTICE.md). Palettes are original.

## Contents
1. What photo colour analysis can and can't do
2. Photo quality gate
3. Lighting and camera correction table (with confidence)
4. The four dimensions
5. Deep-skin protocol
6. Olive protocol
7. At-home draping tests; 7a words-only questions; 7b "washed out" map
8. From dimensions to a season (12-season map, neighbours)
9. Other systems people may mention (16-season, Korean, Sci\ART, Munsell, Monk)
10. Season palettes (hex)
11. Colour-blind and low-vision format
12. Cultural colour meanings
13. Makeup and grooming colour

## 1. What it can and can't do

- In one published hands-on test, a UK colour brand photographed one warm-coloured person under
  daylight-mimicking studio light. It found AI tools had about a 50% chance of naming the right broad
  season (kettlewellcolours.com, "Does AI Colour Analysis Work?"). That is a small, commercially
  interested test, but no vendor has published an independent test showing much better.
- A Washington Post reporter (April 2024) got four different seasons from ChatGPT, TikTok filters,
  an online analyst and an in-person analyst. A style coach in that piece said ChatGPT seemed to call
  darker skin warm by default.
- So: from photos, give **directions** (lighter or deeper, clearer or softer, warmer or cooler) with
  confidence, and name a season only as a working hypothesis with its neighbours. The person's
  lived experience (compliments, foundation history, what jewellery glows) counts as much as photos.

Say this in plain words when you give a photo-based reading, for example: "This is my best reading
from your photos. Cameras shift skin colour, so treat it as a starting point and check it with the
two-minute draping test."

## 2. Photo quality gate

Ask for (all optional):
- 2-3 selfies in **daylight from a window** (not direct sun), facing the window, camera at eye
  level, no flash, no beauty filter, no makeup or only their usual minimum, hair off the face.
- A sheet of **plain white printer paper** held under the jaw in at least one photo. It is the
  reference for correcting the camera.
- Neutral top (grey, white or black) or a towel over coloured clothes; coloured clothes reflect onto
  the face.
- Optional: inner wrist in the same light; natural hair roots if hair is dyed.

Check each photo:
| Check | Pass | Fail → what to say |
|---|---|---|
| Light source | soft daylight, even on both cheeks | "Half your face is in shadow; turn to face the window." |
| White paper | looks close to neutral white | "The paper looks yellow/blue, so the light is tinting your skin too." |
| Filter / smoothing | skin texture visible, eyes normal size | "This looks filtered; please turn off beauty mode." |
| Flash | no hard highlight or red-eye | "Flash flattens and cools skin; please retake without it." |
| Coloured reflections | neutral clothing, plain wall | "The green wall is reflecting onto your skin." |
| Makeup | none or light | "Foundation changes the undertone reading; bare skin works best." |

Partial pass: use the good photos and lower confidence. Never refuse to help someone who can't
reshoot (mobility, no daylight, privacy); switch to the words-only path and say so.

## 3. Lighting and camera correction table

Use the white paper (or any white object in the same light) to judge the cast. When the person can
read hex values (a free colour-picker app, or Claude estimating from the image), run
`palette_tools.py wb --white <paper hex> --sample <cheek hex>`. It returns the corrected sample, the
cast and a confidence level.

| Situation | What it does to skin | Correction | Max confidence for undertone |
|---|---|---|---|
| North-facing window, overcast day, no paper | close to neutral | none needed | Medium (High only with paper check) |
| Window daylight with white paper reading neutral | true-ish | none | High |
| Direct midday sun | blown highlights, deep shadows, warm cast | move to shade by a window | Low |
| Golden hour / sunset | strong yellow-orange | reshoot; or white-balance from paper | Low |
| Warm indoor bulbs (2700-3000 K) | yellow-orange; everyone reads warm | white-balance from paper, then still lower one level | Low-Medium |
| Cool LED / office tubes (5000-6500 K) | blue or green; skin reads cool or sallow | white-balance from paper | Medium |
| Fluorescent | green cast; olive misread | white-balance; check inner wrist | Low-Medium |
| Mixed light (window + bulb) | different casts on each side | can't be corrected by one gain; reshoot | Low |
| Flash | cool, flat, removes depth | reshoot | Low |
| Phone beauty mode / portrait filters | smooths, lightens, warms or pinks | reshoot without filter | Low (do not use) |
| Heavy JPEG compression / screenshot of a photo | blocky skin gradients | ask for original | Medium at best |
| Coloured wall, clothes or foliage near face | reflects that colour onto skin; the paper may not show it the same way | reshoot with a neutral top and plain wall; `wb --reflection` | Low (use for lightness and contrast only) |
| Warm bulbs and **no** white paper | yellow-orange; nothing to correct from | don't read undertone; ask for one daylight reshoot or use words-only signals | Low for undertone; Medium at most for value and contrast |
| Light from directly above (ceiling lights) | shadows under eyes, nose and chin; deepens value | turn to face a window | Medium at most for value; Low for face shape |
| Very deep skin in dim light | camera brightens and adds noise or a grey cast | more light, expose for the face (tap face on screen) | Low-Medium |

A wall or background behind the person is **not** a white reference: it is lit differently from
the face. It can show which way the colour is off, but don't correct from it. Only white paper held
at the jaw counts.

What a flawed photo can still tell you:
| Problem | Undertone | Value (lightness) | Chroma | Contrast | Face shape |
|---|---|---|---|---|---|
| Colour cast, no reference | no | yes, Medium | weak | yes, Medium | yes |
| Coloured reflection | no | yes | no | yes | yes |
| Filter / beauty mode | no | no | no | weak | no (geometry altered) |
| Light from above or one side | weak | weak | yes | weak | no |
| Close-up front camera | yes | yes | yes | yes | no (lens distortion) |

Camera quirks: many phones auto-warm skin and lift shadows ("smart HDR" or scene modes). Front
cameras on some phones smooth skin by default. Ask the person to turn off beauty or portrait modes.
Screens also differ, so hex codes on screen are approximations of fabric colour.

## 4. The four dimensions (do them in this order, each with evidence and confidence)

1. **Undertone:** the hue under the surface. *Warm* (golden, peach, yellow), *cool* (pink, rosy,
   blue-red), *neutral* (neither clearly), *olive* (a green-grey cast that sits on a warm, neutral or
   cool base). Undertone is independent of depth: very fair and very deep skin can each be warm,
   cool, neutral or olive.
2. **Value:** overall lightness of skin, hair and eyes together. *Light*, *medium*, *deep*.
3. **Chroma:** clarity. *Clear / bright* colouring has crisp eye whites, vivid iris colour and skin
   that looks fresh in saturated colour; *muted / soft* colouring has blended features and looks best
   in greyed or toned-down colour.
4. **Contrast:** the difference in lightness between skin, hair and eyes (and brows). Low (all
   similar), medium, high (for example deep hair and eyes with light skin, or very deep skin with
   bright eye whites and white teeth). `palette_tools.py contrast` measures the lightness spread when
   hex values are known.

Signals and how reliable they are:
| Signal | Light skin | Medium | Deep | Notes |
|---|---|---|---|---|
| Skin against white paper in daylight | good | good | good | best photo signal if paper is neutral |
| Gold vs silver next to bare skin | good | good | good | ask which makes skin look alive, not which they like |
| White vs cream fabric at the face | good | good | best | the standard drape test |
| Compliment / tired-colour memory | good | good | best | years of real feedback |
| Foundation history (orange, ashy, pink) | good | good | best | which shades oxidise or look grey |
| Sun reaction (burns vs tans) | good | fair | weak | deep skin rarely burns, so it says little |
| Vein colour on inner wrist | fair | weak | skip | unreliable and often invisible; don't rely on it |

High confidence for undertone needs at least three signals that agree, including one non-photo signal.

Heritage doesn't predict colouring. Every season occurs in every population, and mixed heritage
tells you nothing about which way someone's colouring leans. Read the person, not their ancestry.

## 5. Deep-skin protocol

- Skip the vein test and the sun test; say why instead of apologising.
- Lead with: white vs cream drape, gold vs silver, foundation history, compliment memory, and the
  paper check in good light.
- Look for undertone in the lightest areas (inner arm, palms excluded) and in the jawline vs neck.
  Deep skin often shows red, golden, blue-black or olive reflections in daylight; describe what you see.
- Value is usually *deep*, but chroma and contrast vary a lot. Bright eye whites and teeth against
  very deep skin create high contrast: many deep-skinned people look strongest in clear jewel tones
  (Deep Winter or Bright Winter) or in rich warm saturated colour (Deep Autumn, Warm Autumn), not
  only in "earth tones".
- Never suggest colours "to brighten" or "to lighten" the skin. Pastels and light colours are not
  forbidden either: icy tints and bright white often look striking on deep skin with high contrast.
- **Choosing a season for deep skin:** value is almost always deep, so it decides little. Choose
  by clarity and temperature, and treat contrast with eye whites and teeth as part of contrast:
  deep + clear + cool → Deep Winter or Bright Winter (the Bright Winter "medium value" in the table
  below describes lighter people; deep, very clear colouring belongs there too); deep + clear or rich
  + warm → Deep Autumn or Warm Autumn (or Bright Spring when very clear); deep + muted → Deep Autumn
  or Soft Autumn. When two fit, use `palette_tools.py overlap` and the person's compliment colours.
- Signature compliments are strong evidence: cobalt, fuchsia, emerald and optic white point to the
  clear cool seasons; rust, mustard, olive and warm brown to the warm ones.
- In photos, cameras often grey out or over-brighten deep skin. Ask for more light, and lower
  confidence if the face looks flat or ashy in the photo but the person says it isn't in person.

## 6. Olive protocol

- Olive is common in South Asian, Middle Eastern, Mediterranean, Latin American and some East and
  Southeast Asian skin, but it occurs in every population.
- Signs: skin looks greenish or grey-beige against white paper, pink blush looks "off", both gold and
  silver can look fine or both slightly wrong, foundations look too pink or too orange, many
  "neutral" shades look grey.
- Name the base: *olive on warm* (often Soft or Deep Autumn), *olive on neutral* (often Soft Summer
  or Soft Autumn), *olive on cool* (often Soft Summer or Deep Winter).
- Olive skin often handles muted and deep colours well and looks grey in pastel pinks and cool
  greys. Test teal, olive, aubergine, brick, warm navy and off-white.
- Confidence is usually Medium at best for olive from photos; rely on draping and compliment memory.
- **False olive:** a green cast (green walls, foliage outside the window, a green top, fluorescent
  tubes) makes any skin look olive in a photo. If the photo has any green cast, don't call olive from
  it; ask the words-only questions instead.
- **Olive vs neutral:** both can say "gold and silver both look fine". Olive says "both look a bit
  off", pink blush and baby pink look grey, and many beige foundations look too pink or too yellow.
  Neutral says both metals look fine and most mid-tone colours work.
- **Metals for olive:** when neither yellow gold nor bright silver glows, try brushed or antique gold,
  rose gold, bronze, pewter, mixed metals and pearls; matte finishes usually beat high polish.

## 7a. Words-only questions (no photos, no draping)

Skin depth, with neutral reference points (describe, never rank): "In daylight, is your skin closer
to very light, light, medium, medium-deep, deep or very deep? Many people find a foundation shade
name, or a comparison with family members, easier."

Clear vs soft (chroma), answerable from memory:
- "Do bright saturated colours (true red, cobalt, emerald) make you look more alive, or do they
  feel louder than you?" (alive → clear)
- "Do dusty colours (sage, dusty rose, greige) make you look calm and polished, or tired?" (polished → soft)
- "Are your eyes a crisp, solid colour with a clear edge against the white, or soft and blended?"
- "Does stark black-and-white together look sharp on you, or heavy?" (sharp → clear and high contrast)

Two or more answers pointing the same way give Medium confidence for chroma.

## 7b. "I look washed out / tired / sallow" — what it usually means

| Complaint | Likely cause | Try instead |
|---|---|---|
| Washed out, pale, faded | colours too light or too low-contrast for them, or warm beige on cool light skin | their palette's mid-depth colours near the face, soft navy, cool or deeper accents |
| Tired, shadows under eyes | colour too dark or too strong near the face (often black on light, soft colouring) | a lighter neutral near the face; black away from the face |
| Sallow, yellow-green | colour too cool and grey for warm skin, or too yellow for cool skin | the right temperature: ivory vs optic white, gold vs silver |
| Ashy, grey | colours too muted or too cool on deep warm skin; or a wrong foundation | richer, warmer or clearer colours; check foundation undertone |
| "Disappears" in photos | low contrast between outfit and skin, or matte dark on dark in dim light | a lighter or brighter colour near the face, contrast border, some sheen (silk, zari), and face the light (see occasions.md, being photographed) |

## 7. At-home draping tests (words-only path, two minutes each)

Sit or stand facing a window (a mirror on a table works for seated users; a helper can hold the
fabric), no makeup, hair off the face, neutral top. Hold each item under the chin and
look at the skin, not the fabric. Compare in pairs. Note which one makes the skin look smoother and
more even, the eyes clearer, and shadows under the eyes lighter.

1. **Temperature:** cream or ivory vs optic white; or a gold item vs a silver item.
2. **Value:** a light colour (pale blue) vs a deep one (navy or aubergine).
3. **Chroma:** a clear colour (true red, kelly green) vs a muted one (dusty rose, sage).
4. **Contrast:** black-and-white together vs two mid tones together.

Household substitutes work: tea towels, scarves, dupattas, T-shirts, coloured paper, phone
wallpapers held up to the chin (screens only for rough tests). Let the person report back. Use the
results as strong evidence at the check-in.

## 8. From dimensions to a season

| Season | Undertone | Value | Chroma | Contrast | Neighbours (always compare) |
|---|---|---|---|---|---|
| Light Spring | warm-neutral | light | clear, delicate | low | Light Summer, Warm Spring |
| Warm Spring (True Spring) | warm | medium-light | clear | medium | Light Spring, Bright Spring |
| Bright Spring (Clear Spring) | warm-neutral | medium | very clear | medium-high | Warm Spring, Bright Winter |
| Light Summer | cool-neutral | light | soft-medium | low | Light Spring, Cool Summer |
| Cool Summer (True Summer) | cool | light-medium | soft | low-medium | Light Summer, Soft Summer |
| Soft Summer | cool-neutral | medium | muted | low-medium | Cool Summer, Soft Autumn |
| Soft Autumn | warm-neutral | medium | muted | low-medium | Soft Summer, Warm Autumn |
| Warm Autumn (True Autumn) | warm | medium-deep | rich | medium | Soft Autumn, Deep Autumn |
| Deep Autumn (Dark Autumn) | warm-neutral | deep | rich | medium-high | Warm Autumn, Deep Winter |
| Deep Winter (Dark Winter) | cool-neutral | deep | clear, rich | high | Deep Autumn, Cool Winter |
| Cool Winter (True Winter) | cool | medium-deep | clear | high | Deep Winter, Bright Winter |
| Bright Winter (Clear Winter) | cool-neutral | medium | very clear | high | Cool Winter, Bright Spring |

Common colouring the table fits poorly, and what to do:
- **Medium-depth, neutral, medium-high contrast** (for example wheatish skin with black hair and
  dark eyes, very common in South Asia, the Middle East and Latin America): decide by chroma first.
  Clear → Bright Winter or Bright Spring (by temperature); rich and deep-leaning → Deep Winter or
  Deep Autumn. Give the overlap of the two (`palette_tools.py overlap`) when temperature is unclear.
- **Light skin with black or very dark hair and dark eyes** (very common in East Asia; the usual
  Korean 여름 쿨 vs 겨울 쿨 question): contrast is medium-high from the hair alone, so decide by
  temperature first, then chroma. Cool + clear → Cool Winter or Bright Winter; cool + soft → Cool
  Summer or Soft Summer; warm + clear → Bright Spring; warm + soft → Soft Autumn. Use the overlap of
  the two candidates until chroma is known.
- **Olive**: there is no olive season. Read the base under the olive and use the olive notes above.

Always write a short "why not" for the two neighbours. If two seasons fit about equally, say so and
give the shared colours (the overlap) instead of forcing one. Soft Summer and Soft Autumn are often
over-assigned when evidence is weak; require muted chroma evidence before choosing either.

Sub-season notes:
- **Light** seasons: lightness is the dominant trait; no heavy black near the face.
- **Warm / Cool (True)** seasons: temperature dominates; the "wrong" temperature shows first.
- **Bright / Clear** seasons: chroma dominates; dusty colours make them look tired.
- **Soft** seasons: muted chroma dominates; neon and stark black-and-white overpower them.
- **Deep / Dark** seasons: depth dominates; pastels on their own wash them out.

Hair change, greying, tanning, pregnancy and some medication can shift apparent colouring. Mention
re-checking after big changes.

## 9. Other systems people may mention

- **16-season systems** add a fourth sub-type per season (often "Light/Bright/Soft/Deep" variants or
  "flow" seasons). Map them to the nearest 12-season type and say so.
- **Sci\ART** (Kathryn Kalisz's system) and **Munsell**-based teaching use the same hue, value and
  chroma axes as this method; Munsell's names are hue, value and chroma.
- **Korean personal colour (퍼스널컬러)** usually reports *spring warm, summer cool, autumn warm,
  winter cool* with sub-types *light, bright, mute, deep* (e.g. 여름 쿨 라이트 = summer cool light ≈
  Light Summer; 가을 웜 뮤트 = autumn warm mute ≈ Soft Autumn; 겨울 쿨 딥 = winter cool deep ≈ Deep
  Winter). Japanese and Chinese services use the same four seasons (パーソナルカラー, 四季型人).
- **Monk Skin Tone scale** (10 tones, Google with Ellis Monk) and **Fitzpatrick** (6 types, built
  to predict sunburn risk in lighter skin) describe depth only. Use them only to set lighting
  expectations, never as a style category or a ranking.

## 10. Season palettes (hex)

These 14-colour starter palettes are original and live in `scripts/palettes.json` (the script and
this table are checked against each other by tests). Use them as a starting point: on deep skin,
the same season's colours are worn at full strength; don't lighten them. Roles: *face colour* =
best next to the face; *neutral* = trousers, coats, bags; *accent* = small amounts or prints.

### Light Spring
Light, warm-leaning and clear. Pastels with a little warmth; avoid heavy darks and dusty greys near the face. Metals: light yellow gold, rose gold, polished champagne.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Warm ivory | `#FFF3DC` | white substitute | very light, muted / soft cream / ivory |
| Light camel | `#D9B48C` | neutral | light, moderate tan / camel |
| Warm stone | `#C8B9A2` | neutral | light, muted / soft tan / camel |
| Soft navy | `#53698F` | dark neutral | deep, muted / soft blue / navy |
| Peach | `#F7B28A` | face colour | light, moderate orange / rust |
| Light coral | `#F79A86` | face colour | light, moderate coral / salmon |
| Warm pink | `#F4A6B4` | core | light, moderate pink / rose |
| Buttercup | `#F6D774` | accent | very light, clear / bright gold / mustard |
| Mint | `#A6E2B8` | core | very light, moderate green |
| Light aqua | `#7FD3CA` | core | light, moderate teal / turquoise |
| Periwinkle | `#9DB2EC` | core | light, moderate blue / navy |
| Light warm teal | `#4DB3A6` | accent | light, moderate teal / turquoise |
| Apricot | `#F9C79B` | core | very light, moderate tan / camel |
| Clear lilac | `#C3B0EA` | accent | light, moderate violet / indigo |

Keep away from the face: `#000000` (black is far darker than the face and drains it); `#5A4E5E` (dusty dark grey-plum muddies light warm skin); `#6B3E26` (heavy dark brown overpowers low contrast).

### Warm Spring
Golden, fresh and clear. Warm brights and light warm neutrals; avoid icy, blue-based and greyed colours. Metals: yellow gold, brass, warm bronze.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Cream | `#FDEFD2` | white substitute | very light, muted / soft cream / ivory |
| Golden camel | `#C99A5B` | neutral | light, moderate orange / rust |
| Warm taupe | `#A88B6D` | neutral | medium, muted / soft tan / camel |
| Chocolate | `#6A4325` | dark neutral | deep, moderate brown |
| Coral | `#F27A5E` | face colour | medium, clear / bright coral / salmon |
| Warm peach | `#F6A56E` | face colour | light, clear / bright orange / rust |
| Marigold | `#F2B233` | accent | light, clear / bright orange / rust |
| Golden yellow | `#F2CF45` | accent | very light, clear / bright gold / mustard |
| Leaf green | `#76B643` | core | light, clear / bright green |
| Warm turquoise | `#25B6A3` | core | light, moderate teal / turquoise |
| Tomato red | `#E2442F` | accent | medium, clear / bright red / brick |
| Warm aqua | `#5CC9B5` | core | light, moderate teal / turquoise |
| Clear warm navy | `#2F4E7E` | dark neutral | deep, moderate blue / navy |
| Salmon pink | `#F58C84` | core | light, moderate pink / rose |

Keep away from the face: `#000000` (black is too heavy and cool); `#B7B9C8` (cool grey-lavender greys out golden skin); `#C71585` (blue-based magenta clashes with golden undertone).

### Bright Spring
Vivid, clear and warm-leaning. Saturated brights with crisp contrast; avoid dusty, powdery and muddy colours. Metals: polished yellow gold, bright rose gold, shiny silver in small amounts.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Bright ivory | `#FFF8E7` | white substitute | very light, muted / soft cream / ivory |
| Warm charcoal | `#3E3A36` | dark neutral | very deep, neutral (almost no colour) neutral |
| Bright navy | `#1F3F8F` | dark neutral | deep, clear / bright blue / navy |
| Light warm grey | `#BDB4A6` | neutral | light, muted / soft tan / camel |
| Hot coral | `#FF5E4D` | face colour | medium, clear / bright red / brick |
| Watermelon | `#F2475E` | face colour | medium, clear / bright red |
| Sunflower | `#FFCC1A` | accent | very light, clear / bright gold / mustard |
| Kelly green | `#14A84A` | core | medium, clear / bright green |
| Turquoise | `#00B5B8` | core | light, moderate teal / turquoise |
| Bright aqua | `#2ED3C6` | accent | light, moderate teal / turquoise |
| Clear violet | `#7A4FD0` | accent | deep, clear / bright violet / indigo |
| Poppy red | `#F0301F` | accent | medium, clear / bright red |
| Bright periwinkle | `#6F8CF2` | core | medium, clear / bright blue / navy |
| Hot pink | `#FF4F9A` | core | medium, clear / bright magenta / berry |

Keep away from the face: `#A39A8C` (dusty greige flattens vivid colouring); `#B58C8C` (dusty rose looks faded next to clear features); `#6E5A3F` (muddy olive-brown dulls the face).

### Light Summer
Light, cool-leaning and gentle. Powdery cool pastels and soft greys; avoid black, orange and heavy earth tones. Metals: silver, white gold, platinum, soft rose gold.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Soft white | `#F5F3EE` | white substitute | very light, neutral (almost no colour) neutral |
| Light cool grey | `#BFC3C8` | neutral | light, neutral (almost no colour) neutral |
| Rose taupe | `#B9A3A0` | neutral | light, muted / soft coral / salmon |
| Slate navy | `#4E5E78` | dark neutral | deep, muted / soft blue / navy |
| Powder pink | `#EDB8C4` | face colour | light, muted / soft pink / rose |
| Soft rose | `#DE97A8` | face colour | light, moderate pink / rose |
| Powder blue | `#A9C6E6` | core | light, muted / soft blue / navy |
| Lavender | `#B9AEDD` | core | light, moderate violet / indigo |
| Light periwinkle | `#9AA9E0` | core | light, moderate blue / navy |
| Seafoam | `#A2D6CB` | core | very light, muted / soft teal / turquoise |
| Lemon ice | `#F1EDA6` | accent | very light, moderate yellow / olive |
| Cool watermelon | `#E57F92` | accent | medium, moderate pink / rose |
| Soft teal | `#6FAFB0` | accent | light, muted / soft teal / turquoise |
| Orchid haze | `#C99BC8` | core | light, moderate magenta / berry |

Keep away from the face: `#000000` (black overwhelms light, low-contrast colouring); `#E86A1C` (orange is too warm and strong); `#5C4127` (dark warm brown muddies cool light skin).

### Cool Summer
Cool, softened and mid-light. Blue-based colours with a little grey in them; avoid orange, gold-yellow and stark black-and-white. Metals: silver, pewter, platinum, white gold.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Soft white | `#F1F1EE` | white substitute | very light, neutral (almost no colour) neutral |
| Blue grey | `#8C99A8` | neutral | medium, muted / soft blue / navy |
| Cool taupe | `#9C918F` | neutral | medium, neutral (almost no colour) neutral |
| Greyed navy | `#3E4D68` | dark neutral | deep, muted / soft blue / navy |
| Raspberry soft | `#C25A7C` | face colour | medium, clear / bright red |
| Rose pink | `#D98AA2` | face colour | light, moderate pink / rose |
| Cornflower | `#7D97CF` | core | medium, moderate blue / navy |
| Cool sea blue | `#4F86A8` | core | medium, moderate blue / navy |
| Soft plum | `#8A5A84` | core | deep, moderate magenta / berry |
| Spruce | `#4F8C84` | core | medium, muted / soft teal / turquoise |
| Lavender grey | `#A7A1C4` | neutral | light, muted / soft violet / indigo |
| Watermelon cool | `#D8667F` | accent | medium, clear / bright red |
| Cool jade | `#6DAA9C` | accent | light, muted / soft teal / turquoise |
| Denim | `#5B7499` | core | medium, muted / soft blue / navy |

Keep away from the face: `#F28C28` (orange fights the blue-pink undertone); `#E0B000` (golden yellow makes cool skin look sallow); `#000000` (pure black is harsher than the colouring).

### Soft Summer
Muted, smoky and cool-leaning. Greyed blues, roses and sages; avoid neon, pure white, black and strong orange. Metals: brushed silver, pewter, matte rose gold.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Oyster | `#E7E2DA` | white substitute | very light, neutral (almost no colour) neutral |
| Mushroom | `#A59A92` | neutral | medium, neutral (almost no colour) neutral |
| Charcoal blue | `#4A5562` | dark neutral | deep, muted / soft blue / navy |
| Grey taupe | `#8A8079` | neutral | medium, neutral (almost no colour) neutral |
| Dusty rose | `#BC8A93` | face colour | medium, muted / soft pink / rose |
| Mauve | `#A57E95` | face colour | medium, muted / soft magenta / berry |
| Smoky blue | `#7A90A6` | core | medium, muted / soft blue / navy |
| Sage grey | `#93A394` | core | light, muted / soft green |
| Soft teal | `#5E8A88` | core | medium, muted / soft teal / turquoise |
| Heather plum | `#7E6478` | core | medium, muted / soft magenta / berry |
| Dusty lilac | `#A89DB5` | accent | light, muted / soft violet / indigo |
| Muted raspberry | `#A85C73` | accent | medium, moderate red |
| Slate | `#6C7A89` | neutral | medium, muted / soft blue / navy |
| Soft spruce | `#5C7A6E` | accent | medium, muted / soft green |

Keep away from the face: `#FFFFFF` (optic white is starker than the muted colouring); `#FF5E00` (bright orange overwhelms soft cool skin); `#00E676` (neon green is far too saturated).

### Soft Autumn
Muted, warm-leaning and gentle. Earthy softened colours; avoid icy pastels, neon and stark black. Metals: brushed gold, antique brass, bronze, matte rose gold.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Warm oatmeal | `#E6DAC3` | white substitute | very light, muted / soft cream / ivory |
| Camel | `#B08C62` | neutral | medium, moderate tan / camel |
| Mushroom taupe | `#998672` | neutral | medium, muted / soft tan / camel |
| Soft cocoa | `#5E4B3C` | dark neutral | deep, muted / soft brown |
| Salmon clay | `#C98B73` | face colour | medium, moderate tan / camel |
| Dusty peach | `#D8A88C` | face colour | light, moderate tan / camel |
| Sage | `#9AA587` | core | light, muted / soft green |
| Moss | `#7A8558` | core | medium, moderate green |
| Soft teal | `#5F8A82` | core | medium, muted / soft teal / turquoise |
| Muted jade | `#7FA397` | core | medium, muted / soft teal / turquoise |
| Warm rose | `#B97F7A` | accent | medium, muted / soft pink / rose |
| Mustard soft | `#C4A35A` | accent | light, moderate gold / mustard |
| Dusty denim | `#667C8F` | core | medium, muted / soft blue / navy |
| Olive drab | `#6A6A48` | dark neutral | deep, muted / soft yellow / olive |

Keep away from the face: `#000000` (black is harsh on low-contrast muted colouring); `#FF1493` (hot pink is too bright and cool); `#BFE6FF` (icy blue drains warmth).

### Warm Autumn
Rich, golden and earthy. Spice colours and warm greens; avoid icy pastels, fuchsia and blue-grey. Metals: yellow gold, copper, bronze, brass.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Warm cream | `#F1E0BD` | white substitute | very light, muted / soft cream / ivory |
| Caramel | `#A8743F` | neutral | medium, moderate orange / rust |
| Coffee | `#5C3D24` | dark neutral | deep, muted / soft brown |
| Khaki | `#A39568` | neutral | medium, moderate tan / camel |
| Rust | `#B2512A` | face colour | medium, clear / bright orange / rust |
| Terracotta | `#C06A45` | face colour | medium, clear / bright orange / rust |
| Mustard | `#C9A03A` | accent | light, clear / bright gold / mustard |
| Pumpkin | `#D2712E` | accent | medium, clear / bright orange / rust |
| Olive | `#6F7533` | core | medium, moderate yellow / olive |
| Forest moss | `#4E6B33` | core | deep, moderate green |
| Warm teal | `#2F7A70` | core | medium, moderate teal / turquoise |
| Tomato brick | `#B5402E` | accent | deep, clear / bright red / brick |
| Bronze | `#8C6A33` | neutral | medium, moderate orange / rust |
| Petrol blue | `#2F5C6B` | core | deep, muted / soft blue / navy |

Keep away from the face: `#E6E6FA` (icy lavender greys out golden skin); `#FF00A0` (fuchsia is too cool and bright); `#9AA5B5` (blue-grey looks cold and dull near the face).

### Deep Autumn
Deep, rich and warm-leaning. Dark spices, jewel-earth tones and espresso; avoid pastels and powdery greys. Metals: antique gold, bronze, copper, gunmetal in small amounts.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Warm ivory | `#F0E2C8` | white substitute | very light, muted / soft cream / ivory |
| Espresso | `#3B2618` | black substitute | very deep, muted / soft brown |
| Dark chocolate | `#4E3022` | dark neutral | very deep, muted / soft brown |
| Dark olive | `#4B4F26` | neutral | deep, moderate yellow / olive |
| Brick red | `#8E3423` | face colour | deep, clear / bright red / brick |
| Burnt orange | `#B5521F` | face colour | medium, clear / bright orange / rust |
| Deep teal | `#1D5C58` | core | deep, muted / soft teal / turquoise |
| Forest | `#2F4F2A` | core | deep, moderate green |
| Aubergine warm | `#4E2638` | core | very deep, muted / soft magenta / berry |
| Maroon | `#6A2029` | face colour | very deep, moderate red |
| Saffron | `#C88A1C` | accent | medium, clear / bright orange / rust |
| Paprika | `#A33A22` | accent | deep, clear / bright red / brick |
| Dark petrol | `#1F4552` | core | very deep, muted / soft blue / navy |
| Warm emerald | `#1C6B48` | core | deep, moderate green |

Keep away from the face: `#F8C8DC` (baby pink is too light and cool); `#C0C8D8` (powder blue-grey washes out depth); `#FFF44F` (lemon yellow is too light and acidic).

### Deep Winter
Deep, cool-leaning and saturated. Black, jewel tones and icy accents; avoid golden earth tones, peach and dusty pastels. Metals: silver, platinum, white gold, gunmetal.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Pure white | `#FAFAFA` | white | very light, neutral (almost no colour) neutral |
| Black | `#0B0B0D` | dark neutral | very deep, neutral (almost no colour) neutral |
| Charcoal | `#333438` | neutral | very deep, neutral (almost no colour) neutral |
| Midnight navy | `#141E3C` | dark neutral | very deep, muted / soft blue / navy |
| True red | `#B3122E` | face colour | deep, clear / bright red |
| Deep berry | `#7A1240` | face colour | very deep, clear / bright magenta / berry |
| Emerald | `#00704A` | core | deep, moderate green |
| Sapphire | `#1C3F94` | core | deep, clear / bright blue / navy |
| Plum | `#5B1F5E` | core | very deep, moderate purple / plum |
| Deep teal | `#00585E` | core | deep, muted / soft teal / turquoise |
| Burgundy | `#6A0F25` | core | very deep, moderate red |
| Royal purple | `#4B2A8C` | accent | very deep, clear / bright violet / indigo |
| Icy pink | `#F2DDE6` | accent | very light, muted / soft magenta / berry |
| Pine | `#0F4434` | accent | very deep, muted / soft teal / turquoise |

Keep away from the face: `#F4C29A` (peach is too light and warm); `#C2A67A` (golden camel turns the face sallow); `#B9A9A5` (dusty pastel lacks the depth and clarity).

### Cool Winter
Cool, clear and crisp. Blue-based brights, icy tints, black and white; avoid orange, gold-yellow and muted earth tones. Metals: silver, platinum, white gold.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Snow white | `#FBFCFE` | white | very light, neutral (almost no colour) neutral |
| Black | `#0A0A0F` | dark neutral | very deep, neutral (almost no colour) neutral |
| Cool charcoal | `#3A3D45` | neutral | very deep, neutral (almost no colour) neutral |
| Navy | `#152A5C` | dark neutral | very deep, moderate blue / navy |
| Blue red | `#C8102E` | face colour | deep, clear / bright red |
| Fuchsia | `#C2187A` | face colour | deep, clear / bright magenta / berry |
| Royal blue | `#2348B5` | core | deep, clear / bright blue / navy |
| Cool emerald | `#008060` | core | medium, moderate teal / turquoise |
| Icy blue | `#DCEBFA` | accent | very light, muted / soft blue / navy |
| Magenta | `#B0156E` | core | deep, clear / bright magenta / berry |
| Violet | `#5B2EA6` | core | deep, clear / bright violet / indigo |
| Pine teal | `#00606B` | core | deep, muted / soft teal / turquoise |
| Icy lavender | `#E4DDF5` | accent | very light, muted / soft violet / indigo |
| Cool grey | `#8E939C` | neutral | medium, neutral (almost no colour) neutral |

Keep away from the face: `#E8822A` (orange clashes with the cool undertone); `#C4A35A` (mustard looks muddy and warm); `#B08C62` (camel turns cool skin sallow).

### Bright Winter
Vivid, cool-leaning and high contrast. Electric jewel brights with black and white; avoid dusty, muted and beige colours. Metals: polished silver, platinum, chrome, bright white gold.

| Colour | Hex | Role | In words |
|---|---|---|---|
| Optic white | `#FFFFFF` | white | very light, neutral (almost no colour) neutral |
| Black | `#000000` | dark neutral | very deep, neutral (almost no colour) neutral |
| Ink navy | `#101E50` | dark neutral | very deep, moderate blue / navy |
| Steel grey | `#5A6070` | neutral | deep, muted / soft blue / navy |
| Hot magenta | `#E0157F` | face colour | medium, clear / bright magenta / berry |
| Crimson | `#D7193A` | face colour | medium, clear / bright red |
| Electric blue | `#1E5BFF` | core | medium, clear / bright blue / navy |
| Emerald bright | `#00A36C` | core | medium, clear / bright green |
| Cobalt | `#0047AB` | core | deep, clear / bright blue / navy |
| Bright violet | `#7B2FD6` | accent | deep, clear / bright violet / indigo |
| Turquoise cool | `#00A7C4` | core | medium, moderate teal / turquoise |
| Lemon cool | `#FFF04A` | accent | very light, clear / bright yellow / olive |
| Icy mint | `#D9F7EE` | accent | very light, muted / soft teal / turquoise |
| Shocking pink | `#FF3FA4` | accent | medium, clear / bright magenta / berry |

Keep away from the face: `#C8B8A0` (beige drains vivid contrast); `#9E8C76` (dusty taupe looks muddy); `#B58C8C` (dusty rose is too soft).

## 11. Colour-blind and low-vision format

About 1 in 12 men and 1 in 200 women of Northern European ancestry have red-green colour vision
deficiency (commonly cited figures; rates vary by population). When the person mentions it, or
always for palette cards:
- Give every colour as **lightness word + clarity word + common name + hex**, e.g. "deep, muted
  green (olive) #6F7533". `palette_tools.py describe` produces these words.
- Teach by **value pairing** ("pair a deep colour with a light one") and **families** ("anything
  from navy to teal"), which work regardless of hue perception.
- Suggest labelling hangers or using a colour-identifier app; avoid "match the red with the green".
- On cards, print the name and hex on each swatch (the card generator does this).

## 12. Cultural colour meanings (common customs, not universal rules)

Meanings differ by family, region, religion and generation. Present these as "often" and suggest
asking the host.

| Colour | South Asia | East Asia | Middle East / North Africa | Europe / Americas | Sub-Saharan Africa |
|---|---|---|---|---|---|
| Red | bridal, auspicious (Hindu and many Muslim and Sikh weddings); a guest in full red may compete with the bride | luck and celebration (China); bridal in China and Vietnam | celebration; varies | passion; fine for guests except some Western weddings consider it bold | celebration; in Ghana red with black is used for mourning |
| White | mourning and widowhood in many Hindu communities; but Kerala's off-white kasavu is festive, and white is common for Eid in some places | mourning (China, Korea traditionally); now also Western-style bridal | purity; common for men (thobe/dishdasha) and Hajj | bridal; guests avoid white at Western weddings | white is worn for celebration and for some mourning rites (varies by group) |
| Black | often avoided at Hindu weddings and pujas; fine for receptions in cities | mourning; formal | formal; abayas commonly black (fashion, not mourning) | mourning; also formal evening | mourning (with red in Ghana) |
| Yellow / saffron | haldi ceremony, Basant Panchami, spiritual; turmeric yellow | imperial in historic China | — | spring; cheerful | — |
| Green | Islamic association; Mehndi ceremony; fertility in Maharashtra (green glass bangles) | — | Islam, paradise | luck (Ireland) | growth; national colours in many flags |
| Purple | — | — | — | royalty; Lent and Advent colour in many churches | — |

Event notes: Indian weddings (avoid all-white and all-black unless the family says otherwise, avoid
outshining the bride's red), Chinese weddings (avoid all-white and all-black as a guest), Western
weddings (avoid white, ivory and anything bridal), funerals in most cultures (dark or white
depending on custom; ask).

## 13. Makeup and grooming colour (only if wanted)

- **Foundation**: match the undertone and depth at the jaw and neck in daylight; deep skin often
  needs a different shade for the centre and the edges of the face. Never recommend "a shade
  lighter". Grey or ashy results mean the base is wrong (too pink or too cool, or white-cast
  sunscreen); orange means too warm or oxidising.
- **Flash and stage light**: some powders and sunscreens with high SPF flash white in photos; test
  with a phone flash before the event.
- **Lips and cheeks**: take them from the palette's face colours (for example brick, berry or rose).
- **Brows and beard**: groom to the natural colour; dark brows are part of a person's contrast.
