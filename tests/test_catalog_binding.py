"""Binding of c-in.atomic_function to the closed product catalog (rule PT-5).

Executable proxy of the G-mach checks in evaluation/validate-package.md that
the Hub rule PT-5 (meta-model 0.5) adds: check_taxonomies items 6-11 (catalog
shape), check_golden items 2-8 for every golden/cases*.yaml (class, catalog
function, catalog-refusal case, refusing skill or pack) and the
confusable-pair coverage per class glossary, plus the c-in product condition
of contracts/c-in.md. The logic is ported from PR #17 (HUB-1) and adapted to
the form of the Golden Set of issue #20: the invalid input value of a
catalog-refusal case is `declared_function` with `catalog_check`, so
`atomic_function` is a catalog function of the set class without exceptions,
and classes with `in_slice: false` refuse through `refusing_pack` (the skill
pack of the route node), not a class skill. Every checker runs on the
repository files (no errors expected) and on broken fixtures (the error must
be reported), so a checker that accepts everything fails the suite. No YAML
dependency.
"""

import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_golden_sets import glossary_pairs  # noqa: E402
from test_product_catalog import LEVELS, NODE  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "taxonomy" / "products.yaml"
CATALOG = ROOT / "taxonomy" / "mango-products.yaml"
GOLDEN = ROOT / "golden"
CATALOG_CHECKS = {
    "outside-catalog": "функция вне каталога",
    "not-function": "уровень каталога не функция",
    "foreign-class": "функция чужого класса",
}
REASONS = tuple(CATALOG_CHECKS.values())
OUTSIDE = "queue-callback-offer"


def block(text, key):
    """Two-space `name: value` pairs of a top-level mapping `key:`."""
    match = re.search(rf"^{key}:\n((?:  [a-z-]+: [a-z-]+\n)+)", text, re.M)
    return dict(re.findall(r"^  ([a-z-]+): ([a-z-]+)$", match[1], re.M)) if match else {}


def products(text=None):
    """catalog path, {class: in_slice} and class_domains of taxonomy/products.yaml."""
    text = PRODUCTS.read_text(encoding="utf-8") if text is None else text
    catalog = re.search(r"^catalog: (\S+)", text, re.M)
    classes = dict(re.findall(
        r"^  - \{id: ([a-z-]+), name: .*?in_slice: (true|false)\}$",
        text.split("\nclasses:\n", 1)[1], re.M))
    return (catalog[1] if catalog else None), classes, block(text, "class_domains")


def products_errors(text):
    """check_taxonomies item 6."""
    catalog, classes, class_domains = products(text)
    errors = []
    if catalog != "taxonomy/mango-products.yaml":
        errors.append("products.yaml не объявляет catalog: taxonomy/mango-products.yaml")
    if sorted(class_domains) != sorted(classes):
        errors.append("ключи class_domains не равны классам products.yaml")
    return errors


def parse_catalog(text):
    """Header, class_domains and nodes; malformed node lines are kept as errors."""
    header = dict(re.findall(r"^([a-z0-9_]+): (.+)$", text, re.M))
    nodes, errors = [], []
    for line in text.splitlines():
        if not line.startswith("  - "):
            continue
        match = NODE.match(line)
        if not match:
            errors.append(f"узел без id, level, parents или classes: {line[:80]}")
            continue
        nodes.append({"id": json.loads(match["id"]), "level": match["level"],
                      "parents": json.loads(match["parents"]),
                      "classes": json.loads(match["classes"])})
    return header, block(text, "class_domains"), nodes, errors


def catalog_errors(text, classes, class_domains):
    """check_taxonomies items 7-11 for the catalog text."""
    header, catalog_domains, nodes, errors = parse_catalog(text)
    if header.get("vocabulary") != "mango-products":
        errors.append("vocabulary не mango-products")
    if header.get("closed") != "true":
        errors.append("каталог не закрыт")
    if not header.get("catalog_version"):
        errors.append("нет catalog_version")
    by_id = {}
    for node in nodes:
        if node["id"] in by_id:
            errors.append(f"повтор id {node['id']}")
        by_id[node["id"]] = node
    if catalog_domains != class_domains:
        errors.append("class_domains каталога и products.yaml различаются")
    for node in nodes:
        depth = LEVELS.index(node["level"]) if node["level"] in LEVELS else None
        if depth is None:
            errors.append(f"{node['id']}: неизвестный уровень {node['level']}")
            continue
        if depth == 0 and node["parents"]:
            errors.append(f"{node['id']}: у домена есть родитель")
        if depth > 0 and not node["parents"]:
            errors.append(f"{node['id']}: нет родителя")
        for parent in node["parents"]:
            if parent not in by_id or by_id[parent]["level"] != LEVELS[depth - 1]:
                errors.append(f"{node['id']}: родитель {parent} не на уровень выше")
    domain_class = {domain: cls for cls, domain in class_domains.items()}

    def domains(node_id, seen=()):
        node = by_id.get(node_id)
        if node is None or node_id in seen:
            return set()
        if node["level"] == "domain":
            return {node_id}
        return set().union(*(domains(p, seen + (node_id,)) for p in node["parents"]))

    for node in nodes:
        expected = sorted(domain_class[d] for d in domains(node["id"]) if d in domain_class)
        if sorted(node["classes"]) != expected:
            errors.append(f"{node['id']}: classes {node['classes']} вместо {expected}")
        unknown = set(node["classes"]) - set(classes)
        if unknown:
            errors.append(f"{node['id']}: неизвестные классы {sorted(unknown)}")
    return errors, by_id


def product_refusal(product_class, atomic_function, by_id):
    """Reason of contracts/c-in.md for one c-in.products[] item, or None."""
    node = by_id.get(atomic_function)
    if node is None:
        return f"{REASONS[0]}: {atomic_function}"
    if node["level"] != "function":
        return f"{REASONS[1]}: {atomic_function} ({node['level']})"
    if product_class not in node["classes"]:
        return f"{REASONS[2]}: {atomic_function} не входит в {product_class}"
    return None


def parse_cases(text):
    """Header and cases of a golden/cases*.yaml text; `expect` fields nested."""
    head, _, body = text.partition("\ncases:\n")
    header = dict(re.findall(r"^([a-z_]+): (.+?)(?:\s+#.*)?$", head, re.M))
    cases = []
    for chunk in re.split(r"^  - id: ", body, flags=re.M)[1:]:
        case = {"id": chunk.split("\n", 1)[0].strip()}
        case.update(re.findall(r"^    ([a-z_]+): ([^\s#].*?)(?:\s+#.*)?$", chunk, re.M))
        case["expect"] = {k: v.strip('"') for k, v in
                          re.findall(r"^      ([a-z_]+): (.+?)(?:\s+#.*)?$", chunk, re.M)}
        cases.append(case)
    return {k: v.strip('"') for k, v in header.items()}, cases


def set_class(path, classes):
    """golden/cases.yaml is the contact-center set; cases-<class>.yaml is that class."""
    if path.name == "cases.yaml":
        return "contact-center"
    name = re.fullmatch(r"cases-([a-z-]+)\.yaml", path.name)
    return name[1] if name and name[1] in classes else None


def glossary_name(cls):
    return "domain-glossary.yaml" if cls == "contact-center" else f"domain-glossary-{cls}.yaml"


def glossary_terms(cls):
    text = (ROOT / "taxonomy" / glossary_name(cls)).read_text(encoding="utf-8")
    return set(re.findall(r"^  - id: (\S+)$", text, re.M))


def route_skills():
    text = (ROOT / "routes" / "rg-bcreq-v1.yaml").read_text(encoding="utf-8")
    return dict(re.findall(r"^  - \{node: (n\d+), process: \S+, skill: ([^,]+),", text, re.M))


def skill_names():
    return {p.stem for p in (ROOT / "skills").glob("*.md")}


def golden_errors(name, text, cls, classes, by_id, catalog_version, root=ROOT):
    """check_golden items 2-8 for one Golden Set file."""
    if cls is None:
        return [f"{name}: набор неизвестного класса"]
    header, cases = parse_cases(text)
    errors = []
    if header.get("product_class") != cls:
        errors.append(f"{name}: product_class набора не {cls}")
    if header.get("catalog_version") != catalog_version:
        errors.append(f"{name}: catalog_version набора не {catalog_version}")
    kinds = {c.get("kind") for c in cases}
    if not {"positive", "negative"} <= kinds:
        errors.append(f"{name}: нет положительного или отрицательного случая")
    in_slice = classes.get(cls) == "true"
    nodes, skills, terms = route_skills(), skill_names(), glossary_terms(cls)
    catalog_cases = 0
    for case in cases:
        where = f"{name} {case['id']}"
        path = root / case["file"] if "file" in case else None
        if path is None or not path.is_file():
            errors.append(f"{where}: нет файла случая")
        else:
            front = path.read_text(encoding="utf-8").split("\n---\n", 1)[0]
            if (f"\ngolden_id: {case['id']}\n" not in front
                    or f"\nproduct_class: {cls}\n" not in front + "\n"):
                errors.append(f"{where}: frontmatter файла не объявляет golden_id и product_class")
        if case.get("product_class") != cls:
            errors.append(f"{where}: product_class не {cls}")
        if "atomic_function" not in case:
            errors.append(f"{where}: нет atomic_function")
        else:
            refusal = product_refusal(cls, case["atomic_function"], by_id)
            if refusal is not None:
                errors.append(f"{where}: atomic_function: {refusal}")
        expect = case["expect"]
        if ("declared_function" in case) != ("catalog_check" in case):
            errors.append(f"{where}: declared_function без catalog_check или наоборот")
        elif "catalog_check" in case:
            catalog_cases += 1
            reason = CATALOG_CHECKS.get(case["catalog_check"])
            refusal = product_refusal(cls, case["declared_function"], by_id)
            if reason is None:
                errors.append(f"{where}: неизвестный catalog_check {case['catalog_check']}")
            elif refusal is None or not refusal.startswith(reason):
                errors.append(f"{where}: declared_function не отвергается по причине «{reason}»")
            if case.get("kind") != "negative" or expect.get("refusing_node") != "n1":
                errors.append(f"{where}: отказ по каталогу не на узле n1")
            if reason and not expect.get("reason", "").startswith(reason):
                errors.append(f"{where}: reason не начинается с «{reason}»")
        if case.get("kind") == "positive":
            continue
        if expect.get("outcome") != "refused":
            errors.append(f"{where}: отрицательный случай не refused")
        node = expect.get("refusing_node")
        if node not in nodes:
            errors.append(f"{where}: refusing_node {node} не узел графа")
        if in_slice and expect.get("refusing_skill") not in skills:
            errors.append(f"{where}: refusing_skill не существующий навык")
        if not in_slice:
            if "refusing_skill" in expect:
                errors.append(f"{where}: refusing_skill у класса вне среза")
            if expect.get("refusing_pack") != nodes.get(node):
                errors.append(f"{where}: refusing_pack не skill узла {node}")
        pair = set(re.findall(r"TRM-[A-Z0-9-]+", case.get("glossary_pair", "")))
        if "glossary_pair" in case and (len(pair) != 2 or not pair <= terms):
            errors.append(f"{where}: glossary_pair не из словаря домена класса")
        if "glossary_pair" not in case and "catalog_check" not in case:
            errors.append(f"{where}: нет glossary_pair")
    if not catalog_cases:
        errors.append(f"{name}: нет случая отказа по каталогу")
    return errors


def coverage_errors(cls, text):
    """check_confusable_coverage for one class: every pair has a negative case."""
    _, cases = parse_cases(text)
    covered = {frozenset(re.findall(r"TRM-[A-Z0-9-]+", c["glossary_pair"]))
               for c in cases if c.get("kind") == "negative" and "glossary_pair" in c}
    return [f"{cls}: пара {sorted(p)} не покрыта отрицательным случаем"
            for p in sorted(glossary_pairs(glossary_name(cls)) - covered, key=sorted)]


class CatalogBindingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog_path, cls.classes, cls.class_domains = products()
        cls.text = CATALOG.read_text(encoding="utf-8")
        cls.version = re.search(r'^catalog_version: "([^"]+)"', cls.text, re.M)[1]
        cls.errors, cls.by_id = catalog_errors(cls.text, cls.classes, cls.class_domains)
        cls.sets = {p: set_class(p, cls.classes) for p in sorted(GOLDEN.glob("cases*.yaml"))}

    def golden(self, name, text, cls):
        return golden_errors(name, text, cls, self.classes, self.by_id, self.version)

    # check_taxonomies item 6
    def test_products_declare_catalog_and_class_domains(self):
        text = PRODUCTS.read_text(encoding="utf-8")
        self.assertEqual(products_errors(text), [])
        self.assertTrue((ROOT / self.catalog_path).is_file())
        self.assertEqual(self.classes, {"contact-center": "true", "voice-ucaas": "false",
                                        "analytics-reporting": "false"})
        broken = {
            "catalog": text.replace("\ncatalog: taxonomy/mango-products.yaml", "\n"),
            "class_domains": text.replace("  analytics-reporting: analytics\n", ""),
        }
        for expected, fixture in broken.items():
            with self.subTest(expected):
                self.assertTrue(any(expected in e for e in products_errors(fixture)))

    # check_taxonomies items 7-11
    def test_catalog_shape(self):
        self.assertEqual(self.errors, [])

    def test_catalog_checker_reports_broken_catalogs(self):
        line = next(l for l in self.text.splitlines() if "level: function" in l)
        feature = next(l for l in self.text.splitlines() if "level: feature" in l)
        domain = re.search(r'\{id: "([^"]+)", level: domain', self.text)[1]
        broken = {
            "каталог не закрыт": self.text.replace("\nclosed: true\n", "\nclosed: false\n"),
            "повтор id": self.text.replace(feature, feature + "\n" + feature),
            "не на уровень выше": self.text.replace(
                line, re.sub(r"parents: \[[^]]*\]", f'parents: ["{domain}"]', line)),
            "узел без id, level, parents или classes": self.text.replace(
                line, re.sub(r", classes: \[[^]]*\]", "", line)),
            "classes": self.text.replace(
                line, re.sub(r"classes: \[[^]]*\]", 'classes: ["voice-ucaas"]', line)
                if '"voice-ucaas"' not in line else re.sub(r"classes: \[[^]]*\]", "classes: []", line)),
            "class_domains каталога": self.text.replace(
                "  analytics-reporting: analytics\n", "  analytics-reporting: call-tracking\n"),
        }
        for expected, text in broken.items():
            with self.subTest(expected):
                errors, _ = catalog_errors(text, self.classes, self.class_domains)
                self.assertTrue(any(expected in e for e in errors), errors)

    def test_function_without_runtime_class_is_explicit(self):
        bare = [n for n in self.by_id.values() if n["level"] == "function" and not n["classes"]]
        self.assertTrue(bare)
        for node in bare:
            for cls in self.classes:
                self.assertTrue(product_refusal(cls, node["id"], self.by_id).startswith(REASONS[2]))

    # contracts/c-in.md, AGENTS.md rule 1
    def test_c_in_product_condition(self):
        self.assertIsNone(product_refusal(
            "contact-center", "call-routing/function/overflow-routing", self.by_id))
        self.assertTrue(product_refusal("contact-center", OUTSIDE, self.by_id).startswith(REASONS[0]))
        self.assertTrue(product_refusal(
            "contact-center", "call-routing/feature/overflow-rules", self.by_id).startswith(REASONS[1]))
        self.assertTrue(product_refusal(
            "contact-center", "ivr-voice-menu/function/ivr-menu-navigation", self.by_id
        ).startswith(REASONS[2]))

    def test_runtime_norm_states_the_condition(self):
        for path in ("contracts/c-in.md", "skills/transcript-normalization-contact-center.md"):
            text = " ".join((ROOT / path).read_text(encoding="utf-8").split())
            with self.subTest(path):
                self.assertIn("taxonomy/mango-products.yaml", text)
                for reason in REASONS:
                    self.assertIn(reason, text)
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("taxonomy/mango-products.yaml", agents)
        validate = " ".join((ROOT / "evaluation" / "validate-package.md").read_text(encoding="utf-8").split())
        for check, reason in CATALOG_CHECKS.items():
            self.assertIn(f"«{reason}» — `{check}`", validate)

    # check_golden items 2-8, every golden/cases*.yaml
    def test_golden_sets(self):
        self.assertEqual(sorted(self.sets.values()), sorted(self.classes))
        for path, cls in self.sets.items():
            with self.subTest(path.name):
                self.assertEqual(self.golden(path.name, path.read_text(encoding="utf-8"), cls), [])

    def test_catalog_refusal_cases(self):
        found = {}
        for path, cls in self.sets.items():
            _, cases = parse_cases(path.read_text(encoding="utf-8"))
            for case in (c for c in cases if "catalog_check" in c):
                found[case["id"]] = (case["declared_function"], case["catalog_check"],
                                     case["expect"].get("refusing_skill") or case["expect"]["refusing_pack"])
        self.assertEqual(found, {
            "GS-CC-NEG-05": (OUTSIDE, "outside-catalog", "transcript-normalization-contact-center"),
            "GS-VU-NEG-04": ("call-tracking/function/dynamic-number-substitution", "foreign-class",
                             "SK-transcript-normalization"),
            "GS-AR-NEG-03": ("romi-dashboard-export", "outside-catalog", "SK-transcript-normalization"),
        })

    def test_golden_checker_reports_broken_sets(self):
        text = (GOLDEN / "cases.yaml").read_text(encoding="utf-8")
        good = "    atomic_function: call-routing/function/overflow-routing\n"
        broken = {
            "product_class не contact-center": text.replace(
                "    product_class: contact-center\n", "", 1),
            "catalog_version набора": text.replace(f'catalog_version: "{self.version}"',
                                                    'catalog_version: "2026-01-01.1"'),
            "нет atomic_function": text.replace(good, "", 1),
            REASONS[0]: text.replace(good, "    atomic_function: overflow-routing\n", 1),
            REASONS[1]: text.replace(good, "    atomic_function: call-routing/feature/overflow-rules\n", 1),
            REASONS[2]: text.replace(
                good, "    atomic_function: ivr-voice-menu/function/ivr-menu-navigation\n", 1),
            "не отвергается по причине": text.replace(
                f"declared_function: {OUTSIDE}", "declared_function: call-routing/function/queue-management"),
            "без catalog_check": text.replace("    catalog_check: outside-catalog\n", ""),
            "неизвестный catalog_check": text.replace(
                "catalog_check: outside-catalog", "catalog_check: near-catalog"),
            "reason не начинается": text.replace('reason: "функция вне каталога: ', 'reason: "'),
            "не на узле n1": re.sub(r"(declared_function: [\s\S]*?refusing_node: )n1", r"\1n2", text),
            "нет случая отказа по каталогу": text.replace(
                f"    declared_function: {OUTSIDE}\n    catalog_check: outside-catalog\n", ""),
            "нет glossary_pair": text.replace("    glossary_pair: [TRM-INBOUND, TRM-OUTBOUND]\n", ""),
            "glossary_pair не из словаря": text.replace("[TRM-INBOUND, TRM-OUTBOUND]", "[TRM-INBOUND, TRM-SIP-TRUNK]"),
            "refusing_skill не существующий": text.replace(
                "refusing_skill: context-extraction-contact-center", "refusing_skill: no-such-skill", 1),
            "refusing_node n99": text.replace("refusing_node: n2", "refusing_node: n99", 1),
            "нет файла случая": text.replace("golden/gs-cc-01-queue-overflow.md", "golden/missing.md"),
            "frontmatter": text.replace("file: golden/gs-cc-01-queue-overflow.md",
                                        "file: golden/gs-vu-01-after-hours-forwarding.md"),
        }
        for expected, fixture in broken.items():
            with self.subTest(expected):
                self.assertFalse(fixture == text, "fixture unchanged")
                errors = self.golden("cases.yaml", fixture, "contact-center")
                self.assertTrue(any(expected in e for e in errors), errors)
        self.assertEqual(self.golden("cases-unknown.yaml", text, set_class(
            Path("cases-unknown.yaml"), self.classes)), ["cases-unknown.yaml: набор неизвестного класса"])
        self.assertEqual(set_class(Path("cases-voice-ucaas.yaml"), self.classes), "voice-ucaas")

    def test_golden_checker_reports_broken_out_of_slice_sets(self):
        text = (GOLDEN / "cases-voice-ucaas.yaml").read_text(encoding="utf-8")
        broken = {
            "refusing_pack не skill узла n1": text.replace(
                "refusing_pack: SK-transcript-normalization", "refusing_pack: SK-context-extraction", 1),
            "refusing_skill у класса вне среза": text.replace(
                "refusing_pack: SK-transcript-normalization",
                "refusing_pack: SK-transcript-normalization\n      refusing_skill: transcript-normalization-contact-center", 1),
            "не отвергается по причине «функция вне каталога»": text.replace(
                "catalog_check: foreign-class", "catalog_check: outside-catalog"),
        }
        for expected, fixture in broken.items():
            with self.subTest(expected):
                self.assertFalse(fixture == text, "fixture unchanged")
                errors = self.golden("cases-voice-ucaas.yaml", fixture, "voice-ucaas")
                self.assertTrue(any(expected in e for e in errors), errors)

    # check_confusable_coverage, per class glossary
    def test_glossary_pairs_covered_per_class(self):
        for path, cls in self.sets.items():
            with self.subTest(cls):
                text = path.read_text(encoding="utf-8")
                self.assertEqual(coverage_errors(cls, text), [])
                self.assertTrue((ROOT / "taxonomy" / glossary_name(cls)).is_file())
        text = (GOLDEN / "cases-analytics-reporting.yaml").read_text(encoding="utf-8")
        pair = re.search(r"^    glossary_pair: .+\n", text, re.M)[0]
        self.assertTrue(coverage_errors("analytics-reporting", text.replace(pair, "", 1)))


if __name__ == "__main__":
    unittest.main()
