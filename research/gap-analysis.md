# Gap analysis: personal-style-advisor

Research date: 2026-11-23. Method: web search (English, Japanese, Korean, Chinese, Spanish queries),
GitHub API licence checks, shallow clones of permissively licensed repos (read, never run), and
page fetches of key evidence. Every claim below links to where it was found. Vendor claims are
marked as vendor claims. Anything not verified is marked **UNVERIFIED**.

Sources I could not reach: Reddit (the fetch tool is blocked for reddit.com, tested 2026-11-23 on
r/coloranalysis), Quora (not attempted, blocked in earlier sessions), App Store review text beyond the
listing summaries, Google Play review text (only third-party aggregates), YouTube transcripts (no
transcript tool used), Product Hunt pages (search hits only). Outfevibe, Drapis, StyleSense.AI and
Stylia returned no usable results under those names, so I can't describe them.

## 1. Tools found

Licence column: what the GitHub API, the LICENSE file or the listing says. "None" means no licence
file, so all rights reserved (read for ideas only).

### Claude / agent skills

| Tool | Type | Licence | Inputs | Outputs | Strengths | Weaknesses | Link |
|---|---|---|---|---|---|---|---|
| TrueHue (true-hue) | Claude skill / plugin | MIT | 5 photos + white paper, 14-item questionnaire | 12-season result, ~36 hex palette, avoid list, metals, capsule, swatch PDF | Strict photo quality gate; mandatory check-in before naming a season; adjacent-season "why not" comparison; deep-skin test reliability table; honest limitations file | Colour only (no body, face, occasion, culture); 5-photo intake is heavy; Western grooming categories; no regional wear | https://github.com/bankielewicz/TrueHue |
| fashion (googlarz/fashion-skill) | Claude skill | CC BY 4.0 (LICENSE file; GitHub API shows NOASSERTION) | Profile blocks (height, weight, measurements), front/side/back photos "in minimal or fitted clothing", wardrobe photos | Body shape, colour system, outfits, pre-purchase check, flat-lay HTML, price alerts | Learns over time (profile, feedback, outfit "formulas"); strong onboarding; wardrobe sprint; visual wardrobe grid | Shopping wired to Zalando.de / Amazon.de / Vinted; works only in Claude Code / Cowork; asks weight and near-undressed photos; stores data in local JSON; no Indian or non-Western wear | https://github.com/googlarz/fashion-skill |
| fashion (ivangdavila, ClawHub) | OpenClaw skill | MIT-0 (listing) | Body, budget, lifestyle, constraints (incl. nursing/medical) | Styling advice (users.md, styling.md, fabrics.md, shopping.md, occasions.md) | Clean file split; audit passed | Audit summary notes it solicits sensitive details; scanner flagged hard-coded inches for petite users (not locale-aware) | https://clawhub.ai/ivangdavila/fashion |
| daily_fashion_stylist (HelloEveryboby/Butler) | Agent skill (Chinese) | MIT (repo) | Style keywords + live weather | Daily outfit card (weather, top, bottom, shoes, mnemonic) | Weather-aware; tidy output card; Chinese-language | No body, colour or culture input; generic templates | https://github.com/HelloEveryboby/Butler/tree/main/skills/daily_fashion_stylist |
| generate-outfits / import-clothes (tandpfun/wardrobe) | Codex skills + app | MIT | Garment photos, identity reference photo | Outfit combos and modeled images | Asks for count first; strict local-only handling of identity photos ("never add to Git") | Codex + gpt-image only; wardrobe-only; no suitability analysis | https://github.com/tandpfun/wardrobe |
| muapi-fashion-try-on | Skill (muapi.ai) | MIT (repo) | Person photo URL + garment photo URL | Try-on image, optional video | Visual try-on | Sends the person's photo to a third-party API; paid credits; no suitability logic | https://github.com/SamurAIGPT/Generative-Media-Skills |
| muapi-color-analysis-board | Skill (muapi.ai) | MIT (repo) | One portrait URL | Generated "editorial" colour board image | Attractive output | Single photo; no confidence or check-in; image model decides the palette; third-party upload | https://tessl.io/registry/skills/github/SamurAIGPT/Generative-Media-Skills/muapi-color-analysis-board |
| color-analysis (FerroxLabs, Skills Directory) | Skill | AGPL-3.0 (repo) | Text / photo | 4-season, undertone, coordination | Listed with security grade A | 4-season only; AGPL (read only) | https://www.skillsdirectory.com/skills/ferroxlabs-color-analysis |
| AKM Fashion (sirsws/akm) | OpenClaw skill | NOASSERTION (unclear) | Profile-first intake | Wardrobe and outfit decisions | Profile-first design | Licence unclear, not cloned | https://clawhub.ai/sirsws/akm-fashion-strategist |
| awesome-closet-stylist, wardrobe-curator, ootd, outfits | ClawHub skills | Not checked (listings only) | Wardrobe, preferences | Capsule, outfit planning | Capsule and planning flows | Listings only; **UNVERIFIED** contents | https://clawhub.ai/skills/wardrobe-curator |
| Wardrobe Capsule Builder | findskill.ai skill | Not stated | Preferences | Capsule, palette, rotation | Capsule focus | Listing only | https://findskill.ai/skills/home-lifestyle/wardrobe-capsule-builder |
| anthropics/skills (skill-creator etc.) | Official examples | Per-skill (skill-creator: Apache-2.0) | — | Format rules, eval tooling | Defines SKILL.md format, progressive disclosure | Not fashion | https://github.com/anthropics/skills |

Fashion-designer-pro, fashion-campaign-director, editorial-fashion-six and vistoya-fashion-shop were
named in the seed list. They are designer, campaign and shop skills, not personal styling. I did not
find their repos within the time spent, so their licences are **UNVERIFIED**.

### Open-source code, models and datasets

| Tool | Type | Licence | Inputs | Outputs | Strengths | Weaknesses | Link |
|---|---|---|---|---|---|---|---|
| Aura (Deeraj25/aura) | Web app | None | Undertone, contrast, face shape, hair | Scored look feed | Joins colouring + face shape; explains each score | Deterministic stand-in engine; no licence | https://github.com/Deeraj25/aura |
| PerfectFit | Web app | None | Garment photos | Outfit suggestions, background removal | Wardrobe digitising | Wardrobe only | https://github.com/howielongs/PerfectFit |
| WardrobeWizard | Django + TF app | None | Garment photos | Category labels, outfits | Auto-classification | Wardrobe only | https://github.com/NowarkCodes/WardrobeWizard |
| Fashion Flair | GenAI app | MIT | Chat prompt + Flipkart product data | Outfit recs with Indian products | India retail grounding (Flipkart dataset) | One retailer; no body or colour analysis | https://github.com/debanjan-2002/fashion-flair |
| VogueGenie | App | None | Prompts | Outfit ideas | — | No licence; little documentation | https://github.com/GopalVerma1303/VogueGenie |
| Vastra AI | ML app | None | Wardrobe photos | Style suggestions (ResNet50 Siamese) | Indian-wardrobe framing | No licence; wardrobe similarity only | https://github.com/lazy-wav/Vastra-AI |
| face_shape_classification (goalhunter) | Notebook | None | Face photo | 5 face shapes | Shows MTCNN cropping helps | Accuracy depends on crop; no licence | https://github.com/goalhunter/face_shape_classification |
| faceshape (dsmlr) | Dataset + paper | None | Face photo | 5 shapes, hairstyle recommender | Peer-reviewed (Expert Systems with Applications 2018) | No licence | https://github.com/dsmlr/faceshape |
| inception-face-shape-classifier | Code + paper | None | Face photo | 5 shapes | Inception v3 ~84-85% vs other classifiers 36-65% (arXiv 1911.07916 abstract) | 500 celebrity images from web search; copyright-constrained | https://github.com/adonistio/inception-face-shape-classifier |
| metadome/face_shape_classification | HF model (ViT) | Not stated | Face photo | 5 shapes | Reported accuracy 0.853 (unverified, self-reported) | No licence in card | https://huggingface.co/metadome/face_shape_classification |
| fahd9999/face_shape_classification | HF model | Not stated | Face photo | Shapes incl. Diamond | 85% val accuracy, macro F1 0.83 (self-reported) | Model card only | https://huggingface.co/fahd9999/face_shape_classification |
| IdentiFace (arXiv 2401.01227) | Paper | arXiv | Face photo | Face shape among other traits | Per-class F1: round ~93%, oval ~85%, heart ~83%; 5-class 88% vs 3-class 94% | Authors attribute errors to overlapping classes | https://arxiv.org/pdf/2401.01227 |
| Kaggle face-shape-dataset (niten19) | Dataset | Kaggle listing (not checked) | — | 5 labelled shapes | Widely used | Celebrity-scraped labels | https://www.kaggle.com/datasets/niten19/face-shape-dataset |
| CatchTone (YBIGTA) | Code | GPL-3.0 | Frontal photo | Warm/cool + 4 seasons | Photo calibration step; Korean personal-colour framing | GPL (ideas only); 4 seasons | https://github.com/YBIGTA/CatchTone |
| SkinToneClassifier (ChenglongMa) | Python library | GPL-3.0 | Image | Dominant skin colour + category | Popular (188 stars) | GPL (ideas only); measures colour, not undertone | https://github.com/ChenglongMa/SkinToneClassifier |
| Monk Skin Tone Scale | Open scale (Google + Ellis Monk) | Open (CC BY 4.0 per Google) | — | 10 tones | Designed to fix Fitzpatrick's darker-skin gap | Depth only, not undertone; annotation is subjective | https://blog.google/technology/research/ai-monk-scale-skin-tone-story/ |
| STW / SkinToneNet (arXiv 2603.02475) | Dataset + model | CC BY 4.0 (paper) | In-the-wild photos | 10-tone MST | 42,313 images, 3,564 people | Research; tone depth only | https://arxiv.org/html/2603.02475v1 |
| IndoFashion | Dataset (CVPRW 2021) | On request | Product images | 15 Indian ethnic classes | ~106K images; sarees, lehengas, sherwanis, Nehru jackets | Classification only; e-commerce product shots | https://indofashion.github.io |
| BodyM | Dataset | AWS open data | Silhouettes + height/weight | 14 measurements | 2,505 real people | Measurement research; not styling | https://registry.opendata.aws/bodym/ |
| Single-image body shape classification (arXiv 2305.18480) | Paper | arXiv | One photo | Body shape | — | 71.4% accuracy; errors linked to camera angle | https://arxiv.org/pdf/2305.18480 |

### Apps and services

| Tool | Type | Licence | Inputs | Outputs | Strengths | Weaknesses | Link |
|---|---|---|---|---|---|---|---|
| Style DNA | App | Proprietary | Selfie | Season, palette, outfits | Large user base (4.2/5, 11K+ ratings per Spark listing) | Review themes: unauthorised charges (25), inaccurate personalisation (18), subscription issues (13); Trustpilot 2/5 (8 reviews); in Kettlewell test said True Summer for a warm subject | https://spark.mwm.ai/kr/apps/style-dna-ai-color-analysis/1358319821 |
| Stylz | App (India) | Proprietary | Photos, preferences | AI + human stylist | India-first dataset (claims 10M+ images incl. regional styles); human stylist in loop | Paid tiers (Pro/Glo/VIP); launch figures inconsistent across press | https://www.deccanchronicle.com/business/in-other-news/stylz-set-to-redefine-personal-styling-in-india-with-ai-powered-platform-1917664 |
| Sty AI | App | Proprietary | — | AI stylist | — | Listing only | https://apps.apple.com/us/app/sty-ai/id6744839778 |
| Whering | Wardrobe app | Proprietary | Garment photos | Digital closet, outfits | Background removal, planning | Crashes, cumbersome UI, tedious photo setup (third-party review summary + App Store) | https://kimola.com/reports/unveil-the-future-of-wardrobe-management-with-our-in-depth-whering-report-google-play-en-us-140612 |
| Alta | Wardrobe app | Proprietary | Closet, avatar | Daily outfits, packing | Avatars, packing | AI styling "hit-or-miss" (Substack review) | https://technocouture.substack.com/p/reflections-from-my-clueless-closet |
| Acloset | Wardrobe app | Proprietary | Garment photos | Closet, outfits | — | Only comparison pages found | https://myindyx.com/versus/acloset-vs-whering |
| Stitch Fix | Styling service | Proprietary | Quiz + feedback | Shipped boxes | Human stylists | US/UK only; review text not reached (**UNVERIFIED**) | https://www.stitchfix.com |
| Kibbe body-type apps (several) | Apps | Proprietary | Photos / quiz | Kibbe type | Quick | Developer admits early photo-analysis issues; Grand Screen aggregate 1.4/5 (49 Play reviews); reviewer found manual selection more reliable | https://grand-screen.com/apps/kibbe-body/ |
| Japanese 骨格診断 apps (Luft Skeletal Camera etc.) | Apps | Proprietary | Full-body photo / quiz | Straight / Wave / Natural | Three-frame system popular in Japan and Korea | Luft states results are for reference and change a lot with camera height, angle, pose and clothing | https://www.luft.co.jp/cgi/skeletal-camera.php |
| Star by Face, Y-Star, Celebs, CeleTwin, Twin | Celebrity lookalike apps | Proprietary | Face photo | Celebrity face match | Fun | Match faces, not style; weekly paywall complaints; accuracy claims are the developers' own | https://apps.apple.com/us/app/id1633698910 |
| Fytted | App | Proprietary | Body measurements | Celebrity "style twin" by measurements | Closest to trait matching | Measurements only; no colour, culture or personality | https://apps.apple.com/us/app/-/id6475787674 |
| Mys Tyler | App | Proprietary | Body type, aesthetic | Outfits from "style twins" | Body + aesthetic | Matching method not disclosed | https://apps.apple.com/US/app/id1523259518 |
| Mosso | App | Proprietary | Photos | Colour + outfits | — | Trustpilot reviewers report accuracy problems and refund/cancellation trouble | https://www.trustpilot.com/review/mosso.ai?page=9 |
| ColorMine AI, PersonalColorAI, Tone & Fit, color-analysis.pro, Dressika, YouCam | Colour apps / sites | Proprietary | Selfie | Season | Fast | Accuracy claims (82-97%) are vendor claims with no named independent test | https://www.truhue.app/compare/ |
| ChatGPT (as a colour analyst) | General chatbot | Proprietary | Selfie | Season | Free | Washington Post reporter got autumn (ChatGPT) vs winter (TikTok) vs true spring vs light summer (two human analysts); a style coach said it labelled darker skin warm indiscriminately | https://newsindiatimes.com/?p=74921 |

## 2. Ranked gap list (with evidence)

Ranked by how much harm the gap does to a user, times how common it is across tools.

1. **Single-factor tools; nothing joins the whole person.** Colour-only (TrueHue, Style DNA, ColorMine),
   body-only (Kibbe and 骨格 apps, Fytted), wardrobe-only (Whering, PerfectFit, tandpfun/wardrobe),
   weather-only (Butler). TrueHue's own limitations file says it does not cover body type, face shape
   or aesthetic identity. Aura joins colouring and face shape, but nothing adds height, personality,
   occasion, country and budget. Evidence: table above;
   https://github.com/bankielewicz/TrueHue/blob/main/skills/true-hue/references/known_limitations.md
2. **Colour accuracy from photos is poor, and lighting / white balance drive it.** In Kettlewell's test
   under studio daylight lighting, the AI tools had about a 50% chance of the right broad season (one
   warm subject, so a small sample from a brand with a commercial interest). A Washington Post reporter
   got four different seasons from four sources. Korean guidance names indoor yellow light, filters,
   lip colour and coloured lenses as the misreading causes. Vendors' 82-97% figures are uncited.
   Evidence: https://kettlewellcolours.com/blogs/the-colour-blog/does-ai-colour-analysis-work ,
   https://newsindiatimes.com/?p=74921 ,
   https://miso.kr/blog/thread/%ED%8D%BC%EC%8A%A4%EB%84%90%EC%BB%AC%EB%9F%AC-%EC%A7%84%EB%8B%A8-%EC%82%AC%EC%A7%84-%EC%B4%AC%EC%98%81-%EC%88%9C%EC%84%9C ,
   https://www.colorpaletteanalysis.com/learn/ai-color-analysis-comparison/
3. **Bias against darker skin and diverse bodies; colourist language.** Distribution-parity test found
   statistically significant skin-tone bias in a fashion visual search system. Fashion datasets skew
   thin and tall. Fitzpatrick was built for sunburn risk in lighter skin. The vein test fails on deep
   skin. Professionals told the Washington Post that AI repeats colour analysis's history of excluding
   darker skin. Evidence: https://arxiv.org/pdf/1909.06429 , https://arxiv.org/pdf/1912.06697 ,
   https://blog.google/technology/research/ai-monk-scale-skin-tone-story/ , https://newsindiatimes.com/?p=74921
4. **No confidence levels, no mid-analysis check-in, no way to correct.** Only TrueHue has a
   mandatory check-in and confidence statements. Single-photo tools (muapi board, Style DNA, lookalike
   apps) give one verdict. Kettlewell found the most useful tools let people compare options against
   their own face rather than giving a definitive answer. Evidence: TrueHue SKILL.md;
   https://us.kettlewellcolours.com/blogs/the-color-blog/does-ai-color-analysis-work
5. **Privacy: photos uploaded, stored or sent to third parties; sensitive data collected.**
   googlarz asks for photos "in minimal or fitted clothing" plus weight, and stores a profile; muapi
   skills send the person's photo to an external API; the ClawHub fashion audit summary notes
   solicitation of medical/nursing details. Face images can count as biometric data; deleting an app
   often doesn't delete stored photos. Evidence: https://github.com/googlarz/fashion-skill/blob/main/SKILL.md ,
   https://github.com/SamurAIGPT/Generative-Media-Skills ,
   https://www.tomsguide.com/ai/ai-image-video/viral-ai-photo-filters-are-everywhere-right-now-but-heres-why-you-might-want-to-delete-them
6. **Indian and other non-Western wear is ignored or shallow; almost nothing is global.** IndoFashion's
   authors say standard fashion datasets don't transfer to ethnic wear. India-only apps (Stylz) exist
   but are paid and India-only. Western skills (googlarz, TrueHue, ivangdavila) have no saree,
   lehenga, kurta, hanbok, kimono, abaya, kente or similar guidance. Saree drape guides disagree on
   details (e.g. the Seedha Pallu's path). Evidence: https://arxiv.org/abs/2104.02830 ,
   https://www.deccanchronicle.com/business/in-other-news/stylz-set-to-redefine-personal-styling-in-india-with-ai-powered-platform-1917664 ,
   https://theculturetrip.com/asia/india/articles/11-traditional-saree-draping-styles-from-india
7. **Face-shape accuracy is limited and the categories themselves are fuzzy.** Classical classifiers
   36-65%; Inception v3 ~84-85% on 500 web images; IdentiFace drops from 94% (3 classes) to 88%
   (5 classes) because of overlap, with heart and oval weakest. The seed's "about 70%" figure for
   dsmlr was **not** confirmed in what I could read. The "websites disagree on celebrity face
   shapes" claim is cited in a search summary of arXiv 1911.07916 but I could not read it in the PDF,
   so it is **UNVERIFIED**. Evidence: https://arxiv.org/abs/1911.07916 , https://arxiv.org/pdf/2401.01227
8. **Body-type tools rely on dropdowns or one photo; Kibbe/骨格 photo typing is unreliable.**
   Single-image body-shape classification 71.4% with errors tied to camera angle; Luft says pose,
   angle and clothing change results a lot; Kibbe app developer admits photo-analysis problems and a
   reviewer preferred manual selection. Evidence: https://arxiv.org/pdf/2305.18480 ,
   https://www.luft.co.jp/cgi/skeletal-camera.php , https://grand-screen.com/apps/kibbe-body/
9. **Celebrity-twin apps match faces for fun and teach nothing.** Y-Star, Star by Face, Celebs all
   match facial features; Star by Face reviewers complain of a weekly paywall. Fytted matches by
   measurements only. Evidence: https://apps.apple.com/app/id1508738428 ,
   https://apps.apple.com/us/app/-/id1633698910 , https://apps.apple.com/us/app/-/id6475787674
10. **Paywalls and inaccurate paid results.** Style DNA review themes (unauthorised charges,
    inaccurate personalisation); Mosso refund complaints; color-analysis.pro "$1 offer" complaint;
    lookalike-app weekly fees. Evidence: https://spark.mwm.ai/kr/apps/style-dna-ai-color-analysis/1358319821 ,
    https://www.trustpilot.com/review/mosso.ai?page=9 , https://nl-be.trustpilot.com/review/color-analysis.pro
11. **Shopping tied to one region or retailer; budgets not localised.** googlarz: Zalando.de,
    Amazon.de, Vinted; Fashion Flair: Flipkart only; ivangdavila: inches hard-coded (scanner finding).
    Evidence: https://github.com/googlarz/fashion-skill , https://github.com/debanjan-2002/fashion-flair ,
    https://clawhub.ai/ivangdavila/fashion
12. **Skills that only work in Claude Code.** googlarz states it works in Claude Code and Cowork;
    it uses curl for weather and local JSON files. TrueHue relies on AskUserQuestion with a text
    fallback (good). Evidence: https://github.com/googlarz/fashion-skill/blob/main/SKILL.md
13. **Adaptive, older, pregnant and gender-neutral dressing is missing.** None of the skills covers
    seated fit, one-handed closures, sensory needs or pregnancy. Adaptive guidance exists in
    rehabilitation sources (seated measuring, shorter front length, side openings, pressure points).
    Evidence: https://sci.washington.edu/info/forums/reports/fashion_solutions.asp ,
    https://cdn.vanderbilt.edu/vu-URL/wp-content/uploads/sites/255/2023/09/01121849/The-Adaptive-Clothing-Resource-Guide.pdf ,
    https://newmobility.com/a-wheelchair-users-guide-to-dressing-well/
14. **"What suits you" is confused with "what you like".** Most apps output preferences or trends;
    TrueHue holds the line against preference-only pushback but only for colour. (Inference from the
    tools above, not a cited statistic.)
15. **Non-Western body and colour systems are ignored by Western tools.** Japan/Korea use the
    3-frame 骨格 system (Straight / Wave / Natural) and Korean 퍼스널컬러 (spring warm, summer cool,
    etc.); Western skills only know Kibbe and 12-season. Evidence:
    https://apps.apple.com/us/app/id6503636675 , https://www.luft.co.jp/cgi/skeletal-camera.php

## 3. Borrow / fix / new

| Gap | Borrow (with credit) | Fix | New in personal-style-advisor |
|---|---|---|---|
| 1 Single factor | Aura's idea of scoring a look against several traits (idea only, no code; no licence) | — | One "style profile" joining colouring, face framing, proportions, height, personality, country, budget, occasion and modesty, with each factor's confidence shown separately |
| 2 Colour accuracy | TrueHue: quality gate, white-paper reference, adjacent-season comparison (MIT, ideas adapted) | Never name one sub-season from one photo; give the broad direction (value, chroma, contrast) first | Lighting/camera correction table with confidence levels; "what we can't know from this photo"; a 3-day mirror draping test the user runs at home; `palette_tools.py` to compare garment colours by measured distance |
| 3 Bias | TrueHue deep-skin test reliability table (idea) | Banned-word list (no "fair = good", no "flattering = slimming") | Deep-skin palettes built for deep skin, not lightened copies; Monk scale for depth only, never as a beauty scale; body-neutral fit language |
| 4 No confidence / check-in | TrueHue mandatory check-in (idea) | — | Check-in after the reading and before recommendations; confidence (high/medium/low) on every factor; "correct me" step that changes the result on evidence, holds on preference |
| 5 Privacy | tandpfun "keep identity images local" rule (MIT, idea) | No near-undressed photos, no weight, no medical detail unless the user offers it; nothing stored unless asked | Words-only path is first-class; photo use is opt-in; reminder to remove EXIF/location; never identify the user or bystanders from a face |
| 6 Indian / global wear | IndoFashion category list (idea) | — | Deep regional-wear reference: saree drapes by region, blouse necklines, kurta lengths, lehenga silhouettes, sherwani/bandhgala/achkan, festive and bridal colour rules; plus 12 other regions |
| 7 Face-shape accuracy | — | Treat face shape as a blend with low-medium confidence; use measurable features (width at brow/cheek/jaw, length) instead of labels | "Face framing" by features, so advice still works if the label is wrong |
| 8 Body typing | fashion-skill's proportion checklist idea (CC BY 4.0) | No Kibbe/骨格 verdict from one photo; offer them as optional lenses | Proportion-first fit logic (shoulder-hip line, torso-leg ratio, frame, height) from tape-measure or words |
| 9 Celebrity twins | — | No face matching | Trait-matched public figures (build, height range, colouring, face family, personality) with a style recipe each, adapted to the user's culture and budget; live search to extend |
| 10 Paywalls | — | Free and open (MIT) | — |
| 11 Single-region shopping | fashion-flair's India retail grounding (MIT, idea) | Shopping last, only if asked | 25+ country store guide (India first), tiers by store type, "verify before quoting" |
| 12 Claude Code only | TrueHue's tool-or-text fallback (idea) | No scripts required; no file storage required | Works in claude.ai web/mobile with plain text; artifacts/HTML only when available |
| 13 Adaptive and life stages | — | — | Adaptive (seated, one-handed, sensory, prosthetics), pregnancy, older adults, gender-neutral fit |
| 14 Suits vs likes | TrueHue "hold the line on preference" (idea) | — | Every recommendation labelled "suits you because…" with the trait; preferences respected but kept separate |
| 15 Non-Western systems | — | — | Korean personal-colour names and Japanese 骨格 frames mapped to the skill's own method |

Extras the user asked for, all new: wardrobe audit, capsule wardrobe, hair/glasses/jewellery,
mood boards and palette cards, a 7-day trial week, sustainability (cost per wear, rental, tailoring,
second-hand).
