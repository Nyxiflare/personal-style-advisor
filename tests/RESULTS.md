# Test results

## Unit tests (offline)

`python -m unittest discover -s tests`: **29 tests, all passing** (2026-11-25). They cover:
- colour maths, checked against CIEDE2000 reference pairs;
- colour naming;
- palette sanity: light seasons are light, soft seasons are muted, warm seasons are yellower than
  their cool partners, and "avoid" colours fall outside the palette;
- white balance (yellow, blue, green and reflection casts);
- the overlap and contrast commands;
- the card generator, including HTML escaping;
- the skill package: frontmatter, line count, reference links, no placeholders, no prices in the
  shopping file, and step order.

## Persona tests (round 1, 2026-11-23)

Method: eight fresh subagents each loaded the skill and played a plain claude.ai chat with no
tools. Each one wrote turn 1 from the opening message alone, then played the user strictly from a
hidden persona sheet (see `personas.md`) until advice and a shopping answer were given. Each
agent graded its own transcript. **Limitation:** the same agent played both sides and could see
the hidden sheet after turn 1, so these are simulations, not real users.

Independent checks on all 8 transcripts (not self-graded):
- **C4** (a grep for hide, flaw, slimming, problem area, brighten or lighten the skin, "too dark",
  "unflattering"): no hits about the user. Two hits were neutral descriptions of a celebrity's
  build ("slimmer").
- **C6** (store names or prices before "Where can I buy this?"): none. The only currency amounts
  before that point were budgets the user had stated.

| Persona | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Transcript |
|---|---|---|---|---|---|---|---|---|---|
| P1 Tamil wedding, deep warm, petite | P | P | P | P | P | P | P | P | runs/P1.md |
| P2 Office + sangeet, wheatish, athletic | P | P | P | P | P | P | P | P | runs/P2.md |
| P3 Seoul interview, cool light, slim | P | P | P | P | P | P | P | P | runs/P3.md |
| P4 Lagos gala, deep cool, plus | P | P | P | P | P | P | P | P | runs/P4.md |
| P5 Dubai graduation, olive, modest | P | P | P | P | P | P | P | P | runs/P5.md |
| P6 Tuscany wedding, fair cool, tall | P | P | P | P (borderline wording) | P | P | P | P | runs/P6.md |
| P7 Creative studio, non-binary, mixed heritage | P | P (borderline) | P | P | P | P | P | P | runs/P7.md |
| P8 Naming ceremony, 72, wheelchair user | P | P | P | P | P | P | P | P | runs/P8.md |

No rubric check failed. The runs did log about 100 quality defects, many repeated across personas.
Each one is listed in its transcript's "Skill defects" section.

## What failed and what was fixed

| Defect (personas that hit it) | Fix |
|---|---|
| Blue colours named "purple" by `palette_tools.py describe`, which breaks colour-blind output (P3, P4, P7) | Colour names now use HSV hue; added brown, tan, cream, red vs pink rules; regression test; tables regenerated |
| Too many question rounds before any help; the advice came on turn 4 for a time-sensitive interview (P3, P8, P5) | New "Pace" section in SKILL.md: a safe default outfit in the first reply when the event is soon, merged rounds, about 4 short questions per round, plain words, "just tell me" offered |
| Check-in questions people can't answer; no path forward when they're unsure (P3, P5, P6, P7) | Check-in questions are now answerable from memory; when someone is unsure, readings are marked unconfirmed and the advice uses their compliment colours plus the new `overlap` command |
| The "not sure" style menu came after the advice step (P4, P5, P6) | Steps reordered: check-in → style menu → advice; a test enforces the order |
| Step 2 asked about sun reaction and left out foundation history, contradicting the deep-skin protocol (P1, P4) | Colouring row rewritten: foundation history added; sun question only for light to medium skin |
| The photo request had no plain-wall or neutral-top rule; green walls and clothes made skin read as olive (P7) | Photo request updated; "false olive" rule added; `wb` now reports green-yellow casts as foliage, never High; new `--reflection` flag |
| No lighting row for warm bulbs without white paper; a background wall used as the reference (P2) | New lighting rows; a "what a flawed photo can still tell you" table; walls ruled out as a reference |
| No season fit for medium-depth, neutral, high-contrast colouring, or for deep clear cool colouring (P2, P4) | Deep-skin season rule (choose by clarity and temperature); medium-neutral guidance; `overlap` command |
| A compliment colour (emerald) rated "borderline" by the tool (P1) | Rule: the person's compliment colours outrank the script; maroon and a warm emerald added to Deep Autumn |
| No clear vs soft questions for words-only users; olive metals missing; olive vs neutral confusion (P5, P2) | New §7a words-only questions; olive metals and olive vs neutral notes |
| "Washed out" and "disappear in photos" complaints not answered (P1, P6) | Step 6 now answers the stated worry first; new §7b complaint map; "Being photographed" section in occasions.md |
| Home country and event country mixed up (P6) | Step 1 asks both; shopping notes cover where to buy and alter, plus EU cross-border rules |
| No menswear suiting or alterations guidance; athletic V shape treated as something to balance (P2, P3, P6) | body-proportions §15 tailoring and alterations; athletic and long-torso rows; heat note for tall men |
| Plus-size gown fit was thin (P4) | body-proportions §16 |
| Limited grip, carer-assisted dressing, seated saree and scratchy zari missing (P8) | body-proportions §17; kasavu note in regional-wear |
| Graduation (cap over hijab, gown colour), naming ceremony, Lagos native black tie, winter sangeet, Korean black suit, Italian garden wedding missing (P5, P8, P4, P2, P3, P6) | occasions.md §13 |
| Mixed heritage and diaspora dressing ignored; Igbo detail thin (P7, P4) | Heritage question in Step 1; "heritage doesn't predict colouring"; diaspora note in regional-wear; heritage-fusion style family; Igbo row expanded |
| Shopping rows thin (UAE, Germany, Italy, Korea, Nigeria, UK, Kerala) (P5, P6, P3, P4, P7, P8) | Rows expanded with "verify" marks; Kerala and weaving towns; silk authenticity; budget split by share (no prices) |
| Celebrity library gaps (older South Indian women, Indian disabled figures, Igbo, plus deep cool, German, hair-covering notes, Harry Styles under a non-binary heading) (P1, P4, P5, P6, P7, P8) | Entries added with confidence marks; headings and notes corrected |
| Borderline wording "that's fixable" (P6) | Added to the language table |
| Words-only readings marked High too easily (P5 rated olive High from words) | Rule: High from words needs three agreeing signals or a draping test |

## Round 2 (re-runs after fixes)

P3 and P8 were re-run on 2026-11-25 against the fixed skill to check the pace changes (self-graded,
same method as round 1).

| Re-run | C1-C8 | First usable outfit | Notes and follow-up fixes |
|---|---|---|---|
| P3 Seoul interview | all PASS (C1 gap: home city never asked) | **assistant turn 1** (was turn 4) | Fixed: a priority order for quick-path questions, with "do you live there too?" folded into the budget question; time-critical fit points allowed before the check-in; a mapping for light skin with black hair and dark eyes; a winter coat and "when unsure, wear a tie" note for Korea |
| P8 naming ceremony, wheelchair user | all PASS (C8 borderline: reassurance about ready-stitched sarees came before the check-in) | assistant turn 4 (same count, shorter rounds) | Fixed: a "light path" that folds the check-in into the traits round, aiming for advice by the third reply; confidence in plain words; a depth-dependent greying rule (it had said "softer or cooler" for everyone); jewellery for limited grip; keeping tradition's fixed main colour and applying the palette to the details |

Not re-run after the round-2 fixes: P8's light path was added after its re-run, so it is untested.

## Trigger evaluation (not completed)

`evals/trigger-eval.json` holds 20 trigger queries: 10 that should trigger the skill and 10
near-misses. They couldn't be scored here, for two reasons:
- skill-creator's `run_eval.py` uses `select()` on pipes, which Windows doesn't support, so every
  query errored;
- a Windows-safe wrapper still got no output from a nested `claude -p` in this environment.

The 0/10 recall that both attempts printed is a harness failure, not a measurement. Run the set on
macOS or Linux with skill-creator's `run_loop.py` before relying on the description's triggering.
