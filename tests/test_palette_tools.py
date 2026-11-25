"""Offline tests for personal-style-advisor. Run: python -m unittest discover -s tests"""
import json
import os
import re
import statistics
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "personal-style-advisor")
sys.path.insert(0, os.path.join(SKILL, "scripts"))

import palette_tools as pt  # noqa: E402

PALETTES = pt.load_palettes()


def lab_stats(season):
    labs = [pt.hex_to_lab(c["hex"]) for c in PALETTES[season]["colours"]]
    lch = [pt.lab_to_lch(x) for x in labs]
    chromatic = [x for x in labs if (x[1] ** 2 + x[2] ** 2) ** 0.5 > 15]
    return {
        "medL": statistics.median(x[0] for x in lch),
        "medC": statistics.median(x[1] for x in lch),
        "meanB": statistics.mean(x[2] for x in chromatic),
    }


class TestConversions(unittest.TestCase):
    def test_parse_hex(self):
        self.assertEqual(pt.parse_hex("a0522d"), "#A0522D")
        self.assertEqual(pt.parse_hex(" #ffffff "), "#FFFFFF")
        for bad in ("#FFF", "red", "#GGGGGG", ""):
            with self.assertRaises(ValueError):
                pt.parse_hex(bad)

    def test_lab_endpoints(self):
        L, a, b = pt.hex_to_lab("#FFFFFF")
        self.assertAlmostEqual(L, 100, delta=0.05)
        self.assertAlmostEqual(a, 0, delta=0.05)
        self.assertAlmostEqual(b, 0, delta=0.05)
        self.assertAlmostEqual(pt.hex_to_lab("#000000")[0], 0, delta=0.01)

    def test_ciede2000_reference_pairs(self):
        # Pairs from Sharma, Wu & Dalal (2005) test data.
        cases = [
            ((50.0, 2.6772, -79.7751), (50.0, 0.0, -82.7485), 2.0425),
            ((50.0, 0.0, 0.0), (50.0, -1.0, 2.0), 2.3669),
            ((50.0, 2.5, 0.0), (73.0, 25.0, -18.0), 27.1492),
            ((60.2574, -34.0099, 36.2677), (60.4626, -34.1751, 39.4387), 1.2644),
            ((22.7233, 20.0904, -46.6940), (23.0331, 14.9730, -42.5619), 2.0373),
        ]
        for lab1, lab2, expected in cases:
            self.assertAlmostEqual(pt.delta_e_2000(lab1, lab2), expected, places=3)

    def test_describe_words(self):
        d = pt.describe("#6F7533")
        self.assertEqual(d["hex"], "#6F7533")
        self.assertIn("olive", d["hue_family"])
        self.assertIn("green", pt.describe("#14A84A")["hue_family"])
        # Regression: blues were once named "purple" (CIELAB hue puts blue next to violet).
        for blue in ("#2348B5", "#0047AB", "#101E50", "#0000FF", "#1F3F8F"):
            self.assertEqual(pt.describe(blue)["hue_family"], "blue / navy", blue)
        expected = {"#7A4FD0": "violet / indigo", "#5B1F5E": "purple / plum",
                    "#C8102E": "red", "#BC8A93": "pink / rose", "#3B2618": "brown",
                    "#F0E2C8": "cream / ivory", "#B08C62": "tan / camel",
                    "#C9A03A": "gold / mustard", "#14A84A": "green", "#00B5B8": "teal / turquoise"}
        for hx, name in expected.items():
            self.assertEqual(pt.describe(hx)["hue_family"], name, hx)
        self.assertEqual(pt.describe("#808080")["chroma"], "neutral (almost no colour)")
        self.assertEqual(pt.describe("#FFFFFF")["lightness"], "very light")
        self.assertEqual(pt.describe("#0B0B0D")["lightness"], "very deep")


class TestPalettes(unittest.TestCase):
    def test_twelve_seasons_fourteen_colours(self):
        self.assertEqual(len(PALETTES), 12)
        for name, info in PALETTES.items():
            hexes = [c["hex"] for c in info["colours"]]
            self.assertEqual(len(hexes), 14, name)
            self.assertEqual(len(set(hexes)), 14, f"duplicate hex in {name}")
            for h in hexes + [a["hex"] for a in info["avoid"]]:
                pt.parse_hex(h)
            for key in ("undertone", "value", "chroma", "contrast", "neighbours", "metals", "summary"):
                self.assertIn(key, info, name)
            for n in info["neighbours"]:
                self.assertIn(n, PALETTES, f"{name} neighbour {n}")

    def test_light_and_deep_seasons(self):
        for s in ("Light Spring", "Light Summer"):
            self.assertGreaterEqual(lab_stats(s)["medL"], 65, s)
        for s in ("Deep Autumn", "Deep Winter"):
            self.assertLessEqual(lab_stats(s)["medL"], 40, s)

    def test_soft_vs_bright_chroma(self):
        for s in ("Soft Summer", "Soft Autumn"):
            self.assertLessEqual(lab_stats(s)["medC"], 25, s)
        for s in ("Bright Spring", "Bright Winter"):
            self.assertGreaterEqual(lab_stats(s)["medC"], 50, s)

    def test_warm_partner_is_yellower_than_cool_partner(self):
        pairs = [("Light Spring", "Light Summer"), ("Warm Spring", "Cool Summer"),
                 ("Bright Spring", "Bright Winter"), ("Soft Autumn", "Soft Summer"),
                 ("Warm Autumn", "Cool Winter"), ("Deep Autumn", "Deep Winter")]
        for warm, cool in pairs:
            self.assertGreater(lab_stats(warm)["meanB"], lab_stats(cool)["meanB"] + 8,
                               f"{warm} vs {cool}")

    def test_avoid_colours_are_not_in_palette(self):
        for name, info in PALETTES.items():
            for a in info["avoid"]:
                res = pt.match(a["hex"], name, PALETTES)
                self.assertGreater(res["nearest"][0]["delta_e"], 6,
                                   f"{name}: avoid colour {a['hex']} is inside the palette")

    def test_overlap_between_neighbours(self):
        res = pt.overlap("deep winter", "bright winter", PALETTES)
        self.assertEqual(res["seasons"], ["Deep Winter", "Bright Winter"])
        self.assertGreater(len(res["shared"]), 3)
        for s in res["shared"]:
            self.assertLessEqual(s["delta_e_to_other"], res["limit"])
        far = pt.overlap("light spring", "deep winter", PALETTES, limit=6)
        self.assertLess(len(far["shared"]), len(res["shared"]))

    def test_season_aliases(self):
        self.assertEqual(pt.find_season("dark winter", PALETTES), "Deep Winter")
        self.assertEqual(pt.find_season("True-Autumn", PALETTES), "Warm Autumn")
        self.assertEqual(pt.find_season("clear spring", PALETTES), "Bright Spring")
        with self.assertRaises(KeyError):
            pt.find_season("Purple Season", PALETTES)

    def test_match_exact_colour_is_in_palette(self):
        res = pt.match("#B5521F", "Deep Autumn", PALETTES)
        self.assertEqual(res["nearest"][0]["delta_e"], 0)
        self.assertTrue(res["verdict"].startswith("in palette"))
        far = pt.match("#F8C8DC", "Deep Autumn", PALETTES)
        self.assertTrue(far["verdict"].startswith(("borderline", "off palette")))

    def test_reference_tables_match_json(self):
        with open(os.path.join(SKILL, "references", "colour-analysis.md"), encoding="utf-8") as fh:
            md = fh.read()
        for name, info in PALETTES.items():
            section = md.split(f"### {name}\n", 1)
            self.assertEqual(len(section), 2, f"{name} missing from colour-analysis.md")
            body = section[1].split("\n### ", 1)[0]
            for c in info["colours"]:
                self.assertIn(c["hex"], body, f"{name}: {c['hex']} not in the markdown table")


class TestWhiteBalance(unittest.TestCase):
    def test_neutral_white_is_high_confidence(self):
        r = pt.white_balance("#F4F4F4", "#A0705A")
        self.assertEqual(r["confidence"], "high")
        self.assertEqual(r["cast"], ["none detected"])

    def test_yellow_cast_detected_and_corrected(self):
        r = pt.white_balance("#F2E0BE", "#B07A55")
        self.assertTrue(any("yellow" in c for c in r["cast"]))
        before = pt.hex_to_lab("#B07A55")[2]
        after = pt.hex_to_lab(r["corrected_sample"])[2]
        self.assertLess(after, before, "correction should remove some yellow")
        self.assertIn(r["confidence"], ("medium", "low"))

    def test_blue_cast_detected(self):
        r = pt.white_balance("#D8E4F5", "#8A6A5A")
        self.assertTrue(any("blue" in c for c in r["cast"]))

    def test_green_paper_is_foliage_not_warm_bulb(self):
        r = pt.white_balance("#E8F0E2", "#B0876A")
        self.assertTrue(any("green" in c for c in r["cast"]))
        self.assertFalse(any("warm bulb" in c for c in r["cast"]))
        self.assertNotEqual(r["confidence"], "high")

    def test_reflection_forces_low_and_limits_use(self):
        r = pt.white_balance("#F4F4F4", "#A0705A", reflection=True)
        self.assertEqual(r["confidence"], "low")
        self.assertEqual(r["usable_for"], ["lightness", "contrast"])

    def test_too_dark_white_refuses(self):
        with self.assertRaises(ValueError):
            pt.white_balance("#202020", "#8A6A5A")


class TestContrastAndCard(unittest.TestCase):
    def test_contrast_levels(self):
        self.assertEqual(pt.value_contrast("#F3D9C6", "#1A1410")["contrast"], "high")
        self.assertEqual(pt.value_contrast("#C99A7B", "#8A6A4A")["contrast"], "low")
        self.assertEqual(pt.value_contrast("#6B4A35", "#151010", "#2A1A10")["contrast"], "medium")

    def test_card_has_all_swatches_and_escapes_label(self):
        page = pt.card_html("Deep Autumn", PALETTES, '<script>alert(1)</script>')
        for c in PALETTES["Deep Autumn"]["colours"]:
            self.assertIn(c["hex"], page)
            self.assertIn(c["name"], page)
        self.assertNotIn("<script>", page)
        self.assertIn("prefers-color-scheme", page)

    def test_cli_runs(self):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(pt.main(["describe", "#123456"]), 0)
            self.assertEqual(pt.main(["match", "#123456", "--season", "cool winter"]), 0)
            self.assertEqual(pt.main(["describe", "nothex"]), 2)
        self.assertIn("Cool Winter", out.getvalue())


class TestSkillPackage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8") as fh:
            cls.skill = fh.read()

    def test_frontmatter(self):
        m = re.match(r"^---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", self.skill)
        self.assertIsNotNone(m, "frontmatter must be name then description")
        name, desc = m.group(1), m.group(2)
        self.assertEqual(name, "personal-style-advisor")
        self.assertRegex(name, r"^[a-z0-9-]+$")
        self.assertNotIn("claude", name)
        self.assertNotIn("anthropic", name)
        self.assertLessEqual(len(desc), 1024)
        self.assertNotIn("<", desc)

    def test_length_and_no_readme_in_skill(self):
        self.assertLess(len(self.skill.splitlines()), 500)
        self.assertFalse(os.path.exists(os.path.join(SKILL, "README.md")))

    def test_every_reference_exists_and_is_linked(self):
        refs = sorted(os.listdir(os.path.join(SKILL, "references")))
        expected = ["body-proportions.md", "celebrity-trait-library.md", "colour-analysis.md",
                    "face-framing.md", "learned-from-existing-tools.md", "occasions.md",
                    "regional-wear.md", "shopping-by-country.md", "style-families.md",
                    "visual-outputs.md"]
        self.assertEqual(refs, expected)
        for r in refs:
            self.assertIn(f"references/{r}", self.skill, f"{r} not linked from SKILL.md")
        for linked in re.findall(r"references/([a-z-]+\.md)", self.skill):
            self.assertIn(linked, refs)

    def test_no_placeholders(self):
        pattern = re.compile(r"\b(TODO|TBD|lorem ipsum|PALETTE_TABLES|FIXME|XXX)\b", re.I)
        for r in os.listdir(os.path.join(SKILL, "references")):
            with open(os.path.join(SKILL, "references", r), encoding="utf-8") as fh:
                text = fh.read()
            self.assertIsNone(pattern.search(text), f"placeholder in {r}")
            self.assertGreater(len(text), 3000, f"{r} looks too thin")

    def test_core_rules_present(self):
        for phrase in ("Where they live and where the event is", "Budget",
                       "What they want to wear and where", "Check-in (mandatory",
                       "Shopping comes last", "Never invent", "never by facial resemblance",
                       "High / Medium / Low", "Quick path", "Answer their stated worry first",
                       "plain light wall behind", "foundation history"):
            self.assertIn(phrase, self.skill)

    def test_unsure_menu_comes_before_advice(self):
        menu = self.skill.index("## Step 5. If they're unsure")
        advise = self.skill.index("## Step 6. Advise")
        checkin = self.skill.index("## Step 4. Check-in")
        self.assertLess(checkin, menu)
        self.assertLess(menu, advise)

    def test_shopping_has_no_prices(self):
        with open(os.path.join(SKILL, "references", "shopping-by-country.md"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn("Verify before quoting", text)
        self.assertIsNone(re.search(r"(₹|Rs\.?\s?\d|\$\s?\d|£\s?\d|€\s?\d|\bINR\s?\d)", text),
                          "shopping reference must not contain prices")
        countries = re.findall(r"^\| ([A-Z][A-Za-z ,]+) \([A-Z]{3}", text, re.M)
        self.assertGreaterEqual(len(countries) + 1, 25)


if __name__ == "__main__":
    unittest.main()
