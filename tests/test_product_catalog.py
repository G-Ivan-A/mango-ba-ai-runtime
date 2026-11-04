"""Structure of the closed Mango product catalog taxonomy/mango-products.yaml.

The catalog is a copy of the spoke catalog 2026-10-28.1: one line per node.
The checks pin the numbers of issue #15 (RT-1) and the chain
Domain -> Capability -> Feature -> Atomic Function without a YAML dependency.
"""

import json
import re
import unittest
from collections import Counter
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "taxonomy" / "mango-products.yaml"
LEVELS = ("domain", "capability", "feature", "function")
NODE = re.compile(
    r'^  - \{id: (?P<id>"[^"]+"), level: (?P<level>[a-z]+), name: (?P<name>"(?:[^"\\]|\\.)*"), '
    r"parents: (?P<parents>\[[^]]*\]), classes: (?P<classes>\[[^]]*\]), "
    r"lifecycle: (?P<lifecycle>[a-z-]+)(?P<rest>.*)\}$"
)


def load():
    text = CATALOG.read_text(encoding="utf-8")
    header = dict(re.findall(r"^([a-z0-9_]+): (.+)$", text, re.M))
    class_domains = dict(re.findall(r"^  ([a-z-]+): ([a-z-]+)$", text, re.M))
    nodes, bad = [], []
    for line in text.splitlines():
        if line.startswith("  - "):
            match = NODE.match(line)
            if not match:
                bad.append(line)
                continue
            node = {k: match[k] for k in ("level", "lifecycle")}
            for key in ("id", "name", "parents", "classes"):
                node[key] = json.loads(match[key])
            nodes.append(node)
    return header, class_domains, nodes, bad


class ProductCatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header, cls.class_domains, cls.nodes, cls.bad = load()
        cls.by_id = {n["id"]: n for n in cls.nodes}

    def test_header(self):
        self.assertEqual(self.header["vocabulary"], "mango-products")
        self.assertEqual(self.header["closed"], "true")
        self.assertEqual(self.header["catalog_version"], '"2026-10-28.1"')
        commit = json.loads(self.header["source_commit"])
        self.assertRegex(commit, r"^[0-9a-f]{40}$")
        self.assertIn(f"/blob/{commit}/", self.header["source"])
        self.assertRegex(self.header["source_sha256"], r"^[0-9a-f]{64}$")
        self.assertEqual(
            self.class_domains,
            {"contact-center": "contact-center", "voice-ucaas": "voice-ucaas",
             "analytics-reporting": "analytics"},
        )

    def test_one_line_per_node(self):
        self.assertEqual(self.bad, [])

    def test_counts(self):
        self.assertEqual(len(self.nodes), 353)
        self.assertEqual(len(self.by_id), 353, "ids are unique")
        self.assertEqual(
            Counter(n["level"] for n in self.nodes),
            {"domain": 7, "capability": 43, "feature": 151, "function": 152},
        )
        functions = [n for n in self.nodes if n["level"] == "function"]
        per_class = Counter(c for n in functions for c in n["classes"])
        self.assertEqual(
            per_class, {"contact-center": 66, "voice-ucaas": 51, "analytics-reporting": 28}
        )
        self.assertEqual(sum(1 for n in functions if not n["classes"]), 39)

    def test_parents_are_one_level_up(self):
        for node in self.nodes:
            depth = LEVELS.index(node["level"])
            if depth == 0:
                self.assertEqual(node["parents"], [], node["id"])
                continue
            self.assertTrue(node["parents"], node["id"])
            for parent in node["parents"]:
                self.assertEqual(self.by_id[parent]["level"], LEVELS[depth - 1], node["id"])

    def test_classes_follow_domain_ancestors(self):
        domain_class = {d: c for c, d in self.class_domains.items()}

        def domains(node_id):
            node = self.by_id[node_id]
            if node["level"] == "domain":
                return {node_id}
            return set().union(*(domains(p) for p in node["parents"]))

        for node in self.nodes:
            expected = sorted(domain_class[d] for d in domains(node["id"]) if d in domain_class)
            self.assertEqual(node["classes"], expected, node["id"])
        no_class = {d for d in self.by_id if self.by_id[d]["level"] == "domain"} - set(domain_class)
        self.assertEqual(no_class, {"digital-channels", "ai-automation", "hardware", "security"})


if __name__ == "__main__":
    unittest.main()
