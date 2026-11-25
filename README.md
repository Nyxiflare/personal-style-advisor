# personal-style-advisor

A free, open-source Claude skill that works out what actually **suits** a person: colours,
silhouettes, fabrics and styles. It works for anyone in any country, from photos or from words.

Most style apps look at one thing (colour, *or* body type, *or* your wardrobe). They give one
confident verdict from one selfie and then try to sell you something. This skill joins the whole
person: colouring, face, proportions, height, personality, culture, country, budget and occasion.
It shows how sure it is about each part, checks with you before advising, and leaves shopping until
last.

## What it does

- **Asks first** for your country, budget, what you want to wear and where, and anything that must
  be respected (modesty, religion, workplace, mobility).
- **Reads your colouring** (undertone, value, chroma, contrast) from words or daylight photos. It
  corrects for lighting, says High / Medium / Low confidence for each part, and checks with you before
  naming a season.
- **Face framing**: necklines, blouse necks, collars, earrings, glasses, hair, beard, hijab,
  turban, dupatta and scarf framing.
- **Fit by proportion** for every gender and body: petite, tall, plus, pregnancy, older adults,
  adaptive and seated dressing, gender-neutral.
- **Traditional wear worldwide**, with deep Indian wear: saree drapes by region, weaves, blouses,
  kurtas, lehengas, sherwani, bandhgala, achkan, veshti, and wedding and festival colour customs.
- **Style twins by trait, not by face**: public figures who share your build, height range,
  colouring, face family or style personality, each with a style recipe adapted to you.
- **Extras**: wardrobe audit, capsule wardrobe, palette cards and mood boards, a 7-day trial week,
  and sustainability (re-wear, rent, tailor, second-hand, cost per wear).
- **Shopping last, only if asked**: store types for 36 countries (India first), marked
  "verify before buying". It never makes up prices.

It works in claude.ai (web and mobile), the Claude apps and Claude Code. No tools are required.
The optional Python helper (`scripts/palette_tools.py`, standard library only) does colour maths:
describe a hex in words, white-balance correction from a white-paper reference, contrast level,
palette matching, and a self-contained HTML palette card.

## Install

- **Claude Code**: copy the `personal-style-advisor/` folder into `~/.claude/skills/`.
- **claude.ai / Claude apps**: zip the `personal-style-advisor/` folder and upload it under
  Settings → Capabilities → Skills.

Then just ask, for example: "My cousin's wedding is in Madurai next month. I'm petite with deep
skin. What should I wear?"

## Privacy and respect

- Photos are optional. The words-only path gives complete advice.
- It never asks for weight, undressed photos or medical history, and never identifies anyone from a face.
- Nothing is stored between conversations unless you ask.
- No body-shaming or colourist language: no "hide", "flaws", "slimming" or "brightening" skin.
  Deep skin gets full palettes, not lightened copies.

## Known limitations

- **Photo colour reading is uncertain.** In one published test, AI tools named the right broad
  season about half the time even in studio light. Phone cameras, white balance and screens all shift
  colour. The skill gives directions with confidence levels and a two-minute home draping test, but
  in-person draping in daylight is still more reliable.
- **Face-shape labels are fuzzy.** Published classifiers lose accuracy as overlapping classes
  (oval, round, heart) are added, so the skill caps face-shape confidence at Medium and advises
  from features.
- **The model reads photos, not pixels.** Without a colour-picker reading, hex values from a photo
  are estimates.
- **Reference files are dated seeds (2026-11).** Store names, celebrity looks and customs change.
  Customs vary by family and community, so the skill asks rather than assumes.
- **The palettes are original starting points.** They are checked numerically for lightness,
  chroma and warmth, not tested on a panel of people.
- **The persona tests are simulated.** The eight test conversations in `tests/runs/` were run by
  fresh Claude sessions playing both sides from a hidden persona sheet. They are not real users.

## Package layout

```
personal-style-advisor/       the skill (copy this folder)
  SKILL.md
  references/                 10 researched reference files
  scripts/palette_tools.py    optional colour helper (stdlib)
  scripts/palettes.json       12 season palettes
research/gap-analysis.md      tools found, ranked gaps, borrow/fix/new table
tests/                        unit tests, personas, persona test transcripts
evals/trigger-eval.json       trigger test queries for the description
NOTICE.md                     attributions
```

Run the unit tests (offline):

```
python -m unittest discover -s tests
```

## Licence

MIT. Copyright (c) 2026 Nyxiflare. See NOTICE.md for the ideas credited to other open-source projects.
