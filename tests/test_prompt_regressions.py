"""Product profiles and prompt regressions moved out of prompt texts (issue #495 of the spoke).

taxonomy/product-profiles.yaml (И-11, РТ-8) keeps the product facts that the
steps Ш-0 and Ш-2 used to carry inline; golden/prompt-regressions.yaml (И-12,
РТ-9) keeps the cases that illustrated the principles. The spoke links both by
pinned SHA, so the form checked here is the contract of that link: closed ids,
required fields, dictionaries that exist, and principles that stay free of the
case they replaced. Line-based parsing keeps the test free of a YAML dependency.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "taxonomy" / "product-profiles.yaml"
REGRESSIONS = ROOT / "golden" / "prompt-regressions.yaml"

# Case-specific tokens that a principle must not carry: the case lives in the
# `case` field, the principle stays universal.
CASE_TOKENS = re.compile(r"amoCRM|HDE|коннектор|\bЛК\b|ВАТС|Битрикс|\bамо\b", re.I)


def parse_list(text, key, item_re):
    """Items of a top-level list ``key:`` as dicts of ``field: value`` lines."""
    block = re.search(rf"^{key}:\n((?:[ #].*\n|\n)*)", text, re.M)
    items, item = [], None
    for line in block[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if match := re.match(item_re, line):
            item = {"id": match[1]}
            items.append(item)
            rest = match[2] if match.lastindex and match.lastindex >= 2 else ""
            for field, value in re.findall(r"(\w+): (\[[^]]*\]|\"[^\"]*\"|[^,}]+)", rest or ""):
                item[field] = value.strip().strip('"')
        elif match := re.match(r"^ {4}(\w+): *(.*)$", line):
            item[match[1]] = match[2].strip().strip('"')
            last = match[1]
        elif item is not None and line.startswith("      "):
            item[last] = (item[last].removeprefix(">-") + " " + line.strip()).strip()
    return items


def ids(value):
    return [v.strip() for v in value.strip("[]").split(",") if v.strip()]


class ProductProfiles(unittest.TestCase):
    def setUp(self):
        self.text = PROFILES.read_text(encoding="utf-8")
        self.dictionaries = parse_list(self.text, "dictionaries", r"^  - \{id: (\S+?), (.*)\}$")
        self.profiles = parse_list(self.text, "profiles", r"^  - id: (\S+)()$")

    def test_closed_vocabulary(self):
        self.assertRegex(self.text, r"(?m)^vocabulary: product-profiles$")
        self.assertRegex(self.text, r"(?m)^closed: true$")

    def test_dictionaries_d1_to_d11(self):
        self.assertEqual([d["id"] for d in self.dictionaries], [f"D{n}" for n in range(1, 12)])
        for d in self.dictionaries:
            self.assertTrue(d.get("name") and d.get("scope"), d["id"])

    def test_minimal_set_is_declared(self):
        minimal = ids(re.search(r"(?m)^minimal_set: (\[.*\])$", self.text)[1])
        self.assertEqual(minimal, ["D1", "D2", "D11"])

    def test_profiles_reference_declared_dictionaries(self):
        known = {d["id"] for d in self.dictionaries}
        self.assertEqual([p["id"] for p in self.profiles],
                         ["PP-LK", "PP-VATS", "PP-KC", "PP-RA", "PP-API", "PP-OPERATOR"])
        for p in self.profiles:
            for field in ("name", "scope", "dictionaries"):
                self.assertTrue(p.get(field), f"{p['id']}: {field}")
            used = ids(p["dictionaries"])
            self.assertTrue(used, p["id"])
            self.assertLessEqual(set(used), known, p["id"])

    def test_ids_do_not_collide_with_slot_profiles(self):
        slot_profiles = set(re.findall(r"\{id: (P-[A-Z-]+),", (ROOT / "taxonomy/products.yaml").read_text(encoding="utf-8")))
        self.assertTrue(slot_profiles)
        self.assertFalse(slot_profiles & {p["id"] for p in self.profiles})


class PromptRegressions(unittest.TestCase):
    def setUp(self):
        self.text = REGRESSIONS.read_text(encoding="utf-8")
        self.cases = parse_list(self.text, "cases", r"^  - id: (\S+)()$")

    def test_case_ids_and_register(self):
        self.assertEqual([c["id"] for c in self.cases], ["PR-01", "PR-02", "PR-03"])
        self.assertEqual(sorted(c["register"] for c in self.cases), ["CR-01", "CR-02", "CR-03"])

    def test_required_fields(self):
        for c in self.cases:
            for field in ("register", "steps", "principle", "case", "expect", "reject"):
                self.assertTrue(c.get(field), f"{c['id']}: {field}")

    def test_principle_is_universal(self):
        for c in self.cases:
            self.assertIsNone(CASE_TOKENS.search(c["principle"]), c["id"])
            self.assertIsNotNone(CASE_TOKENS.search(c["case"]), f"{c['id']}: case keeps its specifics")

    def test_mutation_case_token_in_principle_fails(self):
        mutated = self.text.replace("Новизна решения не отменяет", "Новизна коннектора не отменяет", 1)
        self.assertNotEqual(mutated, self.text)
        self.cases_mutated = parse_list(mutated, "cases", r"^  - id: (\S+)()$")
        self.assertTrue(any(CASE_TOKENS.search(c["principle"]) for c in self.cases_mutated))

    def test_not_in_g_mach_index(self):
        # G-mach and the smoke test read golden/cases*.yaml only.
        self.assertFalse(REGRESSIONS.name.startswith("cases"))
        self.assertRegex(self.text, r"(?m)^origin: synthetic$")


if __name__ == "__main__":
    unittest.main()
