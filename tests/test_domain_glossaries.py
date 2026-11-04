"""Domain glossaries taxonomy/domain-glossary*.yaml, one per product class.

contact-center has taxonomy/domain-glossary.yaml; RT-4 (issue #20) adds
voice-ucaas and analytics-reporting. The checks pin the record form, the
symmetry of confusable_with pairs (the source of EP-G7 negative golden cases)
and the grounding of the new terms: every source exists in docs/kb and every
catalog node exists in taxonomy/mango-products.yaml with the glossary class.
Line-based parsing keeps the test free of a YAML dependency.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "taxonomy"
REQUIRED = ("id", "term", "definition", "confusable_with")


def parse_glossary(path):
    header, terms = {}, []
    term, key = None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if match := re.match(r"^([a-z_]+): *(.*?)(?: +#.*)?$", line):
            header[match[1]] = match[2].strip('"')
            continue
        if match := re.match(r"^  - id: (.+)$", line):
            term = {"id": match[1], "confusable_with": [], "sources": [], "catalog": []}
            terms.append(term)
            continue
        if match := re.match(r"^    ([a-z_]+):(?: (.*))?$", line):
            key, value = match[1], (match[2] or "")
            if key == "catalog":
                term[key] = [v.strip() for v in value.strip("[]").split(",") if v.strip()]
            elif key not in ("confusable_with", "sources"):
                term[key] = value
            continue
        if match := re.match(r"^      - term: (.+)$", line):
            term["confusable_with"].append(match[1])
            continue
        if key == "sources" and (match := re.match(r"^      - (\S+)$", line)):
            term["sources"].append(match[1])
    return header, terms


def catalog_classes():
    text = (TAXONOMY / "mango-products.yaml").read_text(encoding="utf-8")
    return {
        m[1]: set(re.findall(r'"([^"]+)"', m[2]))
        for m in re.finditer(r'^  - \{id: "([^"]+)", .*?classes: \[([^]]*)\]', text, re.M)
    }


class DomainGlossaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(TAXONOMY.glob("domain-glossary*.yaml"))
        cls.glossaries = {p.name: parse_glossary(p) for p in cls.files}
        products = (TAXONOMY / "products.yaml").read_text(encoding="utf-8")
        cls.classes = re.findall(r"^  - \{id: ([a-z-]+), name: .*in_slice", products, re.M)
        cls.catalog = catalog_classes()

    def test_one_glossary_per_product_class(self):
        by_class = {h["product_class"]: name for name, (h, _) in self.glossaries.items()}
        self.assertEqual(
            by_class,
            {
                "contact-center": "domain-glossary.yaml",
                "voice-ucaas": "domain-glossary-voice-ucaas.yaml",
                "analytics-reporting": "domain-glossary-analytics-reporting.yaml",
            },
        )
        self.assertEqual(sorted(by_class), sorted(self.classes))

    def test_header_form(self):
        for name, (header, _) in self.glossaries.items():
            with self.subTest(name):
                self.assertEqual(header["vocabulary"], "domain-glossary")
                self.assertEqual(header["closed"], "false")
                self.assertEqual(header["required_fields"], "[" + ", ".join(REQUIRED) + "]")
                self.assertRegex(header["version"], r"^\d+\.\d+$")

    def test_terms_have_required_fields_and_unique_ids(self):
        for name, (_, terms) in self.glossaries.items():
            with self.subTest(name):
                self.assertTrue(terms)
                for term in terms:
                    for field in REQUIRED:
                        self.assertTrue(term.get(field), f"{term['id']}: {field}")
                ids = [t["id"] for t in terms]
                self.assertEqual(len(ids), len(set(ids)))
                self.assertTrue(all(re.match(r"^TRM-[A-Z0-9-]+$", i) for i in ids), ids)

    def test_confusable_pairs_are_symmetric_and_local(self):
        for name, (_, terms) in self.glossaries.items():
            with self.subTest(name):
                by_term = {t["term"]: t for t in terms}
                self.assertEqual(len(by_term), len(terms), "terms are unique")
                for term in terms:
                    for other in term["confusable_with"]:
                        self.assertIn(other, by_term, f"{term['id']} -> {other}")
                        self.assertIn(term["term"], by_term[other]["confusable_with"])

    def test_new_terms_are_grounded_in_kb_and_catalog(self):
        for name, (header, terms) in self.glossaries.items():
            if name == "domain-glossary.yaml":
                continue  # contact-center: compiled from the hub, no sources field
            with self.subTest(name):
                for term in terms:
                    self.assertTrue(term["sources"], term["id"])
                    for source in term["sources"]:
                        self.assertTrue(source.startswith("docs/kb/"), source)
                        self.assertTrue((ROOT / source).is_file(), source)
                    self.assertTrue(term["catalog"], term["id"])
                    for node in term["catalog"]:
                        self.assertIn(node, self.catalog, node)
                        self.assertIn(header["product_class"], self.catalog[node], node)


if __name__ == "__main__":
    unittest.main()
