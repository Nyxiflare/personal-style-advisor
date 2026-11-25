# P3 re-run: Ji-ho, Seoul interview (photo described)

Re-run after fixes. Simulated claude.ai chat: no AskUserQuestion, no artifacts, no web search, no
code execution shown to the user. Turn 1 was written from the opening message only, before the
persona sheet was opened. Files the assistant drew on: SKILL.md, references/occasions.md (sections 3
and 13), references/body-proportions.md (sections 4-6, 8, 15), references/colour-analysis.md
(sections 2-4, 8, 10: Cool Summer, Cool Winter, neighbours), references/face-framing.md (sections
5, 7, 8, 10), references/celebrity-trait-library.md (rules, East Asia, Europe). The Cool Summer /
Cool Winter overlap below was checked against `palette_tools.py overlap "Cool Summer" "Cool Winter"`
by the tester (the chat itself had no tools, so the assistant read the shared colours off both
palettes, as SKILL.md Step 4 allows).

---

**User (turn 1)**

I have a final-round interview at a big company in Seoul next week. What should I wear? I'm Korean,
175 cm, quite slim.

**Assistant (turn 1)**

Good luck with the final round. A week is enough time to get this right, so here is a safe outfit
now, and a few quick questions so I can tune it to you.

**Safe starting point for a big-company interview in Seoul** (a default, not yet tailored to your
colouring)
- **Suit:** navy or charcoal, single-breasted, plain or a very faint pattern. Matching jacket and
  trousers (or a matching skirt, if you wear skirts). This is the conservative norm at large Korean
  firms.
- **Shirt or blouse:** white or light blue, freshly pressed. This is the colour nearest your face,
  so it is the one piece I will fine-tune once I know your colouring.
- **Tie (if you wear one):** plain or subtle pattern in navy or a muted tone. Some firms are fine
  with no tie; a black tie is best avoided because it reads as funeral dress in Korea.
- **Shoes:** dark leather (black or dark brown), polished, comfortable enough to walk and wait in.
- **Grooming:** tidy and natural. Minimal accessories: a simple watch is plenty.

**The one fit tip for you:** at 175 cm and slim, the most common problem is a jacket that is too
big, especially in the shoulders. The shoulder seam should end right at your shoulder bone, and
sleeves should show about 1 cm of shirt cuff. Shoulders are hard to alter, so if a jacket is big
there, swap it or rent one; waist, sleeves and trouser length are quick fixes (allow a few days, so
book any tailoring early this week).

A few short questions (or just tell me what you have and I'll work from that):
1. Which clothes should I cover: menswear, womenswear, or gender-neutral?
2. What do you already own that might work (a suit, shirts, shoes), and does it fit?
3. Your budget in won, roughly (zero is fine if you'd rather use what you have).
4. What kind of company is it (bank, conglomerate, tech, creative), and do you know if they expect
   a tie?

Optional, if you'd like me to fine-tune the shirt colour: which colours do people compliment you
in? You can also share a daylight selfie, but words are enough.

---

**User (turn 2)**

Menswear. I have a black suit but it's a bit big in the shoulders. Not sure about shirts and shoes.
Budget is up to ₩400,000. It's a big conglomerate, strategy team. Not sure about the tie. People
compliment me in navy and grey-blue. Here's a selfie.

*[Photo stand-in: selfie by a window on an overcast day, holding white paper under the jaw; the
paper looks neutral white; no filter. Light skin with a pink look, black hair, dark brown eyes.]*

**Assistant (turn 2)**

Thanks, that's a really useful photo. Quick note: photos can carry location data, so you may want
to strip it or crop before sharing photos anywhere.

**Photo check:** soft window daylight, white paper looks neutral, no filter. That passes, so I can
read your skin tone with good confidence. I can't tell how far the camera was, so I'm cautious
about face shape.

**Your reading so far**
| Factor | Reading | Confidence | Why |
|---|---|---|---|
| Undertone | cool (pink-leaning) | Medium | skin reads pink against neutral paper in good light, and your compliment colours (navy, grey-blue) are cool; one more non-photo signal would make it High |
| Value | light skin, deep hair and eyes | High | clear in the photo |
| Contrast | medium-high (light skin against black hair) | Medium-High | clear in the photo; eyebrows and eyes add to it |
| Chroma (clear vs soft) | not read yet | Low | one overcast photo can't separate crisp from soft colouring; grey-blue hints soft, the contrast hints clear |
| Face framing | oval, possibly on the longer side | Low | selfie distance unknown; I'll advise from features so it holds either way |
| Proportions | slim; jackets big in the shoulders | Medium | from your words; one suit isn't enough to say it's your shoulders and not just that suit |

Working idea: **Cool Summer or Cool Winter** (Korean personal colour: 여름 쿨 or 겨울 쿨). They
share navy, charcoal, white, icy blue and blue-grey, which is great news for an interview: the safe
interview colours are already your colours.

**About your black suit (time-sensitive):** black suits are fine for interviews in Korea, as long as
the tie isn't black. The shoulders are the catch: a jacket that's big in the shoulders usually can't
be fixed well in a week, so we may be looking at renting or buying. I'll confirm once I know a bit
more.

Four quick checks (answer from memory; "not sure" is fine):
1. Silver or gold next to your bare skin: which makes you look more alive?
2. Do bright, saturated colours (cobalt, true red) make you look more alive, or louder than you?
3. Do most jackets feel big in the shoulders, or just this black suit?
4. Will you wear glasses on the day?

Optional: three words for how you want to come across in the room.

Anything I've got wrong above, tell me and I'll fix it.

---

**User (turn 3)**

Silver, definitely. Not sure about bright colours. Most jackets are big in the shoulders, I have
narrow shoulders. Yes, I wear glasses. Trustworthy and sharp.

**Assistant (turn 3)**

**In three lines**
- **The look:** navy wool suit with a natural shoulder, white or icy-blue spread-collar shirt,
  greyed-navy tie, black oxfords.
- **Your colours:** navy, charcoal, crisp white, icy blue and blue-grey near your face; silver for
  your watch and glasses.
- **The one fit tip:** buy or rent for your shoulders first; fix sleeves and hems after.

**Your reading (updated)**
| Factor | Reading | Confidence | What changed |
|---|---|---|---|
| Undertone | cool | **High** | silver confirmed: photo + compliments + metal all agree |
| Value | light skin, deep hair and eyes | High | — |
| Contrast | medium-high | Medium-High | — |
| Chroma | **unconfirmed** | Low | you weren't sure, so I'm using only the colours Cool Summer and Cool Winter share near your face |
| Season | Cool Summer or Cool Winter (unconfirmed) | Medium | cool is settled; soft vs crisp isn't. Why not warmer neighbours: silver and cool compliments rule them out |
| Face framing | oval, possibly long | Low | not confirmed; collar and glasses advice below works for both |
| Proportions | narrow shoulders, slim, fine-to-medium frame, 175 cm | High (shoulders), Medium (frame) | most jackets are big in the shoulders, so it's your build, not the suit |

None of this affects what you wear next week: the shared colours are exactly the interview
colours. If you want to settle Summer vs Winter later, there's a two-minute draping test in the
options at the end.

### For your interview

Strategy team at a conglomerate is about as conservative as Seoul gets, and early December is
cold, so wool and a coat are part of the plan. When you're not sure about the tie, wear one: it's
easy to take off and impossible to add.

**Look 1 (recommended): navy suit, new or rented**
- **Suit:** navy (deep navy, `#152A5C`, or a slightly greyed navy, `#3E4D68`), plain or a very faint
  texture, mid-weight wool. Single-breasted, two buttons. **Natural shoulder with light padding**:
  no wide, built-up or extended shoulders. Slim-to-medium lapels. Jacket long enough to cover your
  seat; sleeves showing about 1 cm of shirt cuff.
- **Trousers:** flat front, straight or gently tapered leg, hemmed with a slight break (the
  traditional business length).
- **Shirt:** crisp white (`#FBFCFE`) or icy blue (`#DCEBFA`), with a **spread collar**. Fitted
  through the body without pulling at the buttons.
- **Tie:** greyed navy or blue-grey (`#3E4D68` / `#8C99A8`), plain or a small dot or fine stripe.
  Tie width to match your lapels.
- **Shoes, belt, socks:** black leather oxfords (cap-toe is the classic choice), black belt, socks
  in navy or charcoal so the line runs unbroken from trousers to shoes.
- **Accessories:** a simple silver watch; nothing else needed.
- **Coat:** charcoal or navy wool overcoat for the commute. Take it off before you go in and carry
  it folded over your arm. Skip camel: it's a warm colour that fights your cool colouring near the
  face.

**Look 2: charcoal suit**
Same cut and fit as Look 1 in charcoal (`#3A3D45`), with a light blue or icy-blue shirt and a navy
tie. Charcoal reads a touch more serious; navy reads a touch more approachable. Both are fully safe.

**Look 3 (zero spend): your black suit, only if it passes the mirror test**
Put it on in front of a mirror. If the shoulder seam sits clearly past your shoulder bone, or you
see a dent in the sleeve just below the shoulder, it will look borrowed in the room: go with Look 1
(renting is a good fit for a one-off). If it only looks slightly roomy, it's acceptable: white
shirt, **navy or blue-grey tie (never black)**, black shoes and belt. Black is a little harsh next
to your face if you turn out to be a Summer; the white shirt between your face and the jacket keeps
it fine.

**Budget (₩400,000), roughly:**
- Suit: the largest share, around 60-70% if buying; far less if you rent.
- Tailoring: about 10% for sleeves and trouser hem. **Ask how long it takes before you pay**, and
  make sure you get it back at least two days before the interview.
- Shirt and tie: about 15-20% (two shirts if you can, so one is always pressed).
- Shoes: whatever is left, or polish a pair you already own if they're black and in good shape.

Do the shopping or rental in the next day or two so tailoring has time.

**Glasses:** wear the pair you have if it fits well; don't switch frames a week before. Clean the
lenses, check they sit level, and if there's glare in photos ask the optician about anti-reflective
coating later. For next time: black, grey, navy, silver or clear-grey frames suit your colouring,
and if your face is on the longer side, frames with a bit of lens depth balance it.

**Hair and grooming:** a trim three to five days before, so it looks settled, not freshly cut.
Neat sides and natural styling; if your face is longer, avoid lots of height on top. Clean-shaven or
very tidy.

### Why it suits you
- **Navy, charcoal, white, icy blue, blue-grey:** your cool undertone (High) and your compliment
  colours. They sit in both of your possible seasons, so they're right whichever way the last
  reading goes.
- **Silver watch:** you said silver looks more alive on you.
- **Natural shoulder, light padding:** your shoulders are narrow, so an extended shoulder would
  hang past them; a natural shoulder fits the frame you have and reads sharp.
- **Slim-to-medium lapels and a matching tie width:** in scale with a slim, fine-to-medium frame.
- **Spread collar:** frames an oval or longer face well; a narrow point collar would lengthen it
  further.
- **Slight trouser break, jacket covering the seat:** clean, traditional lines for a conservative
  room, at your height.
- **"Trustworthy and sharp":** navy and white read trustworthy; precise fit is what reads sharp.
  Fit will do more for you than any colour choice.

### Style twins (shared traits, not lookalikes)
From a reference list dated 2026-11 (I can't check their latest looks here). Heights are reported
figures.
- **Gong Yoo (Korea):** shares a lean build, light cool-neutral colouring and a classic, quiet
  style. Difference: reported as tall. *Recipe:* navy and charcoal suits; white shirts; grey or
  navy overcoat; minimal accessories; let the fit do the work.
- **Lee Min-ho (Korea):** shares a slim build, light cool-neutral colouring and a polished classic
  style. Difference: reported as tall. *Recipe:* slim (not tight) tailoring in dark neutrals; clean
  grooming; after you're hired, a fine-knit turtleneck under a coat for off-duty days.
- **Tom Hiddleston (UK):** shares a slim build, cool colouring and a "sharp classic" style.
  Difference: lighter overall colouring and taller. *Recipe:* slim navy suits; crisp shirts;
  polished black shoes; nothing extra.

### Next options (pick any)
1. **Two-minute draping test** to settle Cool Summer vs Cool Winter (useful for work clothes after
   you get the job).
2. **Palette list** of your best colours with names and hex codes.
3. **Work wardrobe starter** for after the offer: a small capsule around navy, charcoal and grey.
4. **Shopping help:** where to buy or rent in Seoul, with size and tailoring notes.

---

**User (turn 4)**

Where can I buy this?

*(Transcript ends here, as specified.)*

---

## Self-grade

| # | Check | Result | Evidence |
|---|---|---|---|
| C1 | Asked country and budget first | **PASS** (with a gap) | Turn 1 asks budget in won ("Your budget in won, roughly"). Event country/city was given ("Seoul"). Gap: turn 1 never asked where he **lives** (SKILL.md Step 1 item 1); it turned out not to matter here, but it went unasked across the whole run. |
| C2 | Asked what they want to wear and where | **PASS** | Turn 1 Q4 asks the kind of company and whether they expect a tie (the dress-code detail); Q2 asks what he owns; the occasion and date were given. Setting (indoor, conglomerate, winter) was covered in turn 3. |
| C3 | Confidence levels | **PASS** | Turn 2 and turn 3 tables give undertone, value, contrast, chroma, face framing and proportions each a High/Medium/Low with a reason. Chroma is marked "unconfirmed / Low", not guessed. The undertone moved Medium → High only after a third, non-photo signal (silver), as colour-analysis.md §4 requires. |
| C4 | No body-shaming or colourist language | **PASS** | No hide/flaws/slimming/problem areas/brighten. Narrow shoulders were framed as "fits the frame you have"; "it's your build, not the suit" is neutral. |
| C5 | Celebrities by trait with a recipe | **PASS** | Turn 3: Gong Yoo, Lee Min-ho (own region), Tom Hiddleston (elsewhere); shared traits and differences named; 3-5-move recipes adapted to a conservative Seoul interview; "shared traits, not lookalikes"; heights "reported"; list dated 2026-11. Weakness: all three are reported as tall while he is 175 cm (see defects). |
| C6 | Shopping last | **PASS** | No store, brand, programme or price in turns 1-3. Budget given as shares only. "Rent" mentioned generically. Shopping offered as the last item of the turn-3 menu; the user asks in turn 4. |
| C7 | Modesty and culture respected | **PASS** | Conservative Korean big-company norms followed in every look (navy/charcoal, white/light-blue shirt, a tie by default); black tie explicitly ruled out (funeral association); the black-suit option is kept but tied to fit. No modesty constraints were stated. |
| C8 | Check-in before advising | **PASS** | Turn 2 shows readings with confidence and asks four memory-answerable checks plus "tell me what I've got wrong"; full looks come only in turn 3 after the answers; chroma marked unconfirmed and the overlap used, as Step 4 directs. The turn-1 safe default is the labelled quick-path starting point SKILL.md allows; turn 2's black-suit note was a time-sensitive fit fact, not a look. |

**Summary:** C1 PASS (gap: home city never asked), C2 PASS, C3 PASS, C4 PASS, C5 PASS, C6 PASS, C7 PASS, C8 PASS.

## Pace

- **First usable outfit:** assistant **turn 1** (labelled safe default: navy or charcoal suit,
  white or light-blue shirt, plain tie that isn't black, polished dark shoes, plus the shoulder fit
  tip). Wearable as is.
- **First outfit tailored to him:** assistant turn 3.
- **Question rounds:** 2 (turn 1: 4 questions plus an optional one; turn 2: 4 checks plus an optional
  one). Then full advice. 3 assistant turns in all before "Where can I buy this?"
- Feel: brisk. The one moment that felt slow was turn 2: he had just said "black suit, big in the
  shoulders" and the assistant could only hint at "rent or buy" because the check-in comes first.

## Remaining defects

1. **Turn-1 question budget squeezes out "where they live"** (SKILL.md, "Pace" and Step 1).
   Step 1 asks for home and event location, budget, occasion details, constraints, gender scope
   (ground rule 7), what they own, and words/photos, but the Pace rule caps a round at about four
   single-part questions. With gender unclear, the home city fell off and was never asked.
   **Change:** in SKILL.md "Pace: help early, ask little", add a priority order for the first round
   on the quick path: "(1) which clothes to cover, if unclear; (2) what they own; (3) budget;
   (4) dress-code detail. When the event city is given, ask whether they live there in the same
   line as the budget ('budget in won, and do you live in Seoul too?') or defer home city to
   Step 8 (shopping)." Also say whether a two-part question that only adds a yes/no counts as one.

2. **No mapping for light skin with black hair and dark eyes** (references/colour-analysis.md §8,
   "Common colouring the table fits poorly"). That section covers medium-depth wheatish skin and
   olive only. Light skin with black hair (very common in East Asia, and the base case for Korean
   퍼스널컬러) sits between Cool Summer (light-medium value, low-medium contrast) and Cool Winter
   (medium-deep value, high contrast), so the table pulls two ways and the assistant has to improvise.
   **Change:** add a bullet: "**Light skin with black or very dark brown hair and dark eyes**: value
   is split (light skin, deep hair), so contrast is medium-high from the hair alone. Decide by
   temperature, then by chroma: cool + clear → Cool Winter or Bright Winter; cool + soft → Cool
   Summer or Soft Summer; warm + clear → Bright Spring; warm + soft → Soft Autumn. Until chroma is
   known, use the overlap of the two cool (or warm) candidates. In Korean terms this is the common
   여름 쿨 vs 겨울 쿨 question."

3. **Style twins are all tall for an average-height man** (references/celebrity-trait-library.md,
   East and Southeast Asia table). The section warns "search for figures of their own height range",
   but in a no-web-search chat every Korean man in the seed list (Gong Yoo, Lee Min-ho, Park Seo-joon,
   RM) is listed as tall or average-tall, so a 175 cm user gets only tall twins. **Change:** add two
   or three East Asian men with **average** reported heights and a classic or polished-tailoring style
   (verify heights and current looks before adding; don't fill from memory), and add one line to the
   Rules: "When no seed figure matches the person's height range and search is unavailable, say so
   and name height as a difference."

4. **The check-in delays time-sensitive fit and rental decisions** (SKILL.md Step 4). "Mandatory,
   before any recommendation" left turn 2 unable to say clearly "your black suit's shoulders can't be
   fixed in a week, plan to rent or buy", even though that decision doesn't depend on any colour
   reading and the lead time matters. **Change:** add to Step 4: "Exception: fit and lead-time facts
   that don't depend on the readings (a jacket too big in the shoulders, a rental that needs booking)
   may be stated before the check-in, so the person can act on them."

5. **Korean interview guidance has no cold-weather or tie-uncertainty line** (references/occasions.md
   §3 Korea row and §13 "Korean job interviews"). Seoul's main hiring seasons include winter, and
   users often don't know whether to wear a tie. **Change:** add to §13: "In winter, a charcoal or navy
   wool overcoat (not camel for cool colouring; choose from the palette), taken off before entering.
   If unsure about a tie at a large firm, wear one: it can be removed."
