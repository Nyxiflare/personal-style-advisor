# Learned from existing tools

Compiled 2026-11-23 from the research in the package's `research/gap-analysis.md`. Ideas were
studied and rewritten in original words; no text or code was copied. Attributions are in the
package's NOTICE.md.

## Borrowed ideas (with credit)

| Idea | From | Licence | How it is used here |
|---|---|---|---|
| Work dimensions (undertone, value, chroma, contrast) before naming a season | TrueHue by Bryan Ankielewicz | MIT | colour-analysis.md section 4 |
| Mandatory check-in before the verdict; evidence vs preference pushback | TrueHue | MIT | SKILL.md Step 4, applied to every factor, not only colour |
| Explain "why not" the two neighbouring seasons; between-seasons result | TrueHue | MIT | colour-analysis.md section 8 |
| Test reliability by skin depth (skip the vein test on deep skin) | TrueHue | MIT | colour-analysis.md sections 4-5 |
| White paper as a camera reference; photo quality gate with partial acceptance | TrueHue | MIT | colour-analysis.md sections 2-3, extended with a correction table and `palette_tools.py wb` |
| Honest limitations and "what high confidence means" | TrueHue | MIT | SKILL.md rule 4, colour-analysis.md section 1 |
| Tool-or-plain-text fallback for questions | TrueHue | MIT | SKILL.md "Works everywhere" |
| Onboarding by blocks (body, life, style, budget); learning over time with a feedback loop | fashion-skill by Dawid Piaskowski (googlarz) | CC BY 4.0 | SKILL.md Step 2 and the 7-day trial week (feedback without stored files) |
| Visual wardrobe grid / flat lay rendered as HTML | fashion-skill (googlarz) | CC BY 4.0 | visual-outputs.md sections 1 and 4 |
| Weather-aware daily outfit card with a short summary line | daily_fashion_stylist (HelloEveryboby/Butler) | MIT | occasions.md section 10 (climate) and the output shape |
| Keep identity photos local and out of version control | tandpfun/wardrobe | MIT | SKILL.md rule 2, visual-outputs.md section 6 |
| Ground Indian shopping in Indian retail | Fashion Flair (debanjan-2002) | MIT | shopping-by-country.md, India first |
| Scoring a look against several traits at once (colouring + face shape) | Aura (Deeraj25) | no licence: idea only | the joined style profile in SKILL.md Step 3 |
| Indian ethnic garment categories | IndoFashion dataset (Rajput and Aneja, CVPRW 2021) | dataset on request: categories as facts only | regional-wear.md part A |

## Fixed gaps (what others got wrong, and the fix)

| Gap (evidence in gap-analysis.md) | Fix here |
|---|---|
| One factor per tool | one profile joining colour, face, proportions, height, personality, culture, country, budget, occasion |
| Colour from one selfie; about a 50% broad-season hit rate in a published test | directions first, season as a hypothesis with neighbours, lighting table, confidence, home draping test |
| Bias against deep skin; colourist language | deep-skin protocol, banned-language table, no "brightening" advice, Monk/Fitzpatrick for lighting only |
| No confidence, no correction | High/Medium/Low per factor, mandatory check-in, evidence-based corrections |
| Near-undressed photos, weight, medical details, third-party uploads | words-only path, never ask for weight or undressed photos, no uploads, nothing stored by default |
| Indian and non-Western wear ignored | deep India section plus 12 regions; cultural colour customs; respectful wearing rules |
| Face-shape labels treated as facts (classifiers ~85-88% at best on clean data) | blends with Medium confidence max; advice from features |
| Kibbe or body type from one photo | proportions from words or tape; Kibbe and 骨格 as optional lenses |
| Celebrity apps match faces, paywalled | trait matching with style recipes; free |
| Single-region shopping (Zalando.de, Amazon.de, Flipkart) | 36 countries; tiers by store type; rent, tailor and second-hand first; shopping last |
| Inches hard-coded (scanner finding on a ClawHub skill) | cm first, both units accepted |
| Claude Code only | no tools required; scripts optional |

## New additions (not found in any tool reviewed)

- Lighting and camera correction table with a maximum confidence per light source, plus a
  white-balance helper script.
- Celebrity trait library with confidence marks and adaptation steps for culture, modesty and budget.
- Adaptive, seated, pregnancy, older-adult and gender-neutral fit guidance in the same flow.
- Korean 퍼스널컬러 and Japanese 骨格 mapping to the skill's own method.
- Colour-blind format: every colour given as lightness and clarity words plus name and hex.
- 7-day trial week that refines readings from real wear.
- Sustainability built into every recommendation (re-wear, rent, tailor, second-hand, cost per wear).
