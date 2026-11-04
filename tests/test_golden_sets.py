"""Golden Set indexes golden/cases*.yaml, one per product class (RT-3, issue #20).

RFC-RT-001 asks for a set per class bound to the closed product catalog: every
case names the set class and a catalog function of that class, every
confusable_with pair of the class glossary is covered by a negative case, and
each set has at least two positives and a catalog-check negative (function
outside the catalog or of a foreign class). The invalid input value of such a
case is `declared_function`, so `atomic_function` always stays a catalog id.
Line-based parsing keeps the test free of a YAML dependency.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOLDEN = ROOT / "golden"
SETS = {
    "cases.yaml": ("contact-center", "domain-glossary.yaml"),
    "cases-voice-ucaas.yaml": ("voice-ucaas", "domain-glossary-voice-ucaas.yaml"),
    "cases-analytics-reporting.yaml": ("analytics-reporting", "domain-glossary-analytics-reporting.yaml"),
}
NODES = {f"n{i}" for i in range(1, 13)}


def parse_cases(path):
    header, cases, case = {}, [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if match := re.match(r"^([a-z_]+): *(.*?)(?: +#.*)?$", line):
            header[match[1]] = match[2].strip('"')
        elif match := re.match(r"^  - id: (\S+)$", line):
            case = {"id": match[1]}
            cases.append(case)
        elif match := re.match(r"^ {4,6}([a-z_]+): *(.*?)(?: +#.*)?$", line):
            case.setdefault(match[1], match[2].strip('"'))
    return header, cases


def catalog_functions():
    text = (ROOT / "taxonomy" / "mango-products.yaml").read_text(encoding="utf-8")
    return {
        m[1]: set(re.findall(r'"([^"]+)"', m[2]))
        for m in re.finditer(r'^  - \{id: "([^"]+)", level: function, .*?classes: \[([^]]*)\]', text, re.M)
    }


def glossary_pairs(name):
    text = (ROOT / "taxonomy" / name).read_text(encoding="utf-8")
    ids = dict(re.findall(r"^  - id: (\S+)\n    term: (.+)$", text, re.M))
    by_term = {term: tid for tid, term in ids.items()}
    pairs = set()
    for block in re.split(r"^  - id: ", text, flags=re.M)[1:]:
        tid = block.split("\n", 1)[0].strip()
        for other in re.findall(r"^      - term: (.+)$", block, re.M):
            pairs.add(frozenset((tid, by_term[other])))
    return pairs


class GoldenSetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = catalog_functions()
        cls.version = re.search(r'^catalog_version: "([^"]+)"', (ROOT / "taxonomy" / "mango-products.yaml").read_text(encoding="utf-8"), re.M)[1]
        cls.sets = {name: parse_cases(GOLDEN / name) for name in SETS}

    def test_one_set_per_class(self):
        self.assertEqual(sorted(p.name for p in GOLDEN.glob("cases*.yaml")), sorted(SETS))

    def test_header(self):
        for name, (header, cases) in self.sets.items():
            with self.subTest(name):
                self.assertEqual(header["product_class"], SETS[name][0])
                self.assertEqual(header["catalog_version"], self.version)
                self.assertEqual(header["structural_only"], "true")
                self.assertTrue(header["golden_set"].startswith("mvp-bcreq"))
                ids = [c["id"] for c in cases]
                self.assertEqual(len(ids), len(set(ids)))

    def test_cases_bound_to_catalog_function_of_set_class(self):
        for name, (header, cases) in self.sets.items():
            for case in cases:
                with self.subTest(case["id"]):
                    self.assertEqual(case["product_class"], header["product_class"])
                    self.assertIn(case["atomic_function"], self.catalog)
                    self.assertIn(header["product_class"], self.catalog[case["atomic_function"]])
                    self.assertIn(case["origin"], ("synthetic", "run-observed"))
                    self.assertEqual(case["confirmed_by"], "none")
                    self.assertTrue((ROOT / case["file"]).is_file(), case["file"])
                    text = (ROOT / case["file"]).read_text(encoding="utf-8")
                    self.assertIn(f"golden_id: {case['id']}\n", text)
                    self.assertIn(f"product_class: {header['product_class']}\n", text)

    def test_counts_and_glossary_pair_coverage(self):
        for name, (header, cases) in self.sets.items():
            with self.subTest(name):
                kinds = [c["kind"] for c in cases]
                self.assertGreaterEqual(kinds.count("positive"), 2)
                covered = {
                    frozenset(re.findall(r"TRM-[A-Z0-9-]+", c["glossary_pair"]))
                    for c in cases if "glossary_pair" in c
                }
                self.assertEqual(covered, glossary_pairs(SETS[name][1]))
                self.assertTrue(any("catalog_check" in c for c in cases), name)

    def test_negatives_refuse_without_artifact(self):
        for name, (header, cases) in self.sets.items():
            for case in (c for c in cases if c["kind"] == "negative"):
                with self.subTest(case["id"]):
                    self.assertEqual(case["outcome"], "refused")
                    self.assertEqual(case["artifact_produced"], "false")
                    self.assertIn(case["refusing_node"], NODES)
                    self.assertTrue(case.get("refusing_skill") or case.get("refusing_pack"))
                    self.assertTrue(case["reason"])

    def test_catalog_check_cases(self):
        for name, (header, cases) in self.sets.items():
            for case in (c for c in cases if "catalog_check" in c):
                with self.subTest(case["id"]):
                    declared = case["declared_function"]
                    self.assertEqual(case["refusing_node"], "n1")
                    if case["catalog_check"] == "outside-catalog":
                        self.assertNotIn(declared, self.catalog)
                        self.assertNotIn(declared, (ROOT / "taxonomy" / "mango-products.yaml").read_text(encoding="utf-8"))
                    else:
                        self.assertEqual(case["catalog_check"], "foreign-class")
                        self.assertIn(declared, self.catalog)
                        self.assertNotIn(header["product_class"], self.catalog[declared])


if __name__ == "__main__":
    unittest.main()
