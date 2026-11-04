"""Binding of c-in.atomic_function to the closed product catalog (rule PT-5).

Executable proxy of the G-mach checks in evaluation/validate-package.md:
check_taxonomies items 6-11 (catalog shape) and check_golden items 2-5 and 7
(class and catalog function of every Golden Set case), plus the c-in product
condition of contracts/c-in.md. Every checker is run on the repository files
(no errors expected) and on broken fixtures (the error must be reported), so
a checker that accepts everything fails the suite. No YAML dependency.
"""

import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_product_catalog import LEVELS, NODE  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "taxonomy" / "products.yaml"
CATALOG = ROOT / "taxonomy" / "mango-products.yaml"
GOLDEN = ROOT / "golden"
REASONS = ("функция вне каталога", "уровень каталога не функция", "функция чужого класса")
OUTSIDE = "queue-callback-offer"


def block(text, key):
    """Two-space `name: value` pairs of a top-level mapping `key:`."""
    match = re.search(rf"^{key}:\n((?:  [a-z-]+: [a-z-]+\n)+)", text, re.M)
    return dict(re.findall(r"^  ([a-z-]+): ([a-z-]+)$", match[1], re.M)) if match else {}


def products():
    text = PRODUCTS.read_text(encoding="utf-8")
    catalog = re.search(r"^catalog: (\S+)", text, re.M)
    classes = re.findall(r"^  - \{id: ([a-z-]+), name:", text.split("\nclasses:\n", 1)[1], re.M)
    return (catalog[1] if catalog else None), classes, block(text, "class_domains")


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
    header = dict(re.findall(r"^([a-z_]+): (.+?)(?:\s+#.*)?$", text.split("\ncases:\n", 1)[0], re.M))
    cases = []
    for chunk in re.split(r"^  - id: ", text.split("\ncases:\n", 1)[1], flags=re.M)[1:]:
        case = {"id": chunk.split("\n", 1)[0].strip()}
        case.update(re.findall(r"^    ([a-z_]+): ([^\s#].*?)(?:\s+#.*)?$", chunk, re.M))
        case["expect"] = dict(re.findall(r"^      ([a-z_]+): (.+?)(?:\s+#.*)?$", chunk, re.M))
        cases.append(case)
    return {k: v.strip('"') for k, v in header.items()}, cases


def set_class(path, classes):
    """golden/cases.yaml is the contact-center set; cases-<class>.yaml is that class."""
    if path.name == "cases.yaml":
        return "contact-center"
    name = re.fullmatch(r"cases-([a-z-]+)\.yaml", path.name)
    return name[1] if name and name[1] in classes else None


def golden_errors(name, text, cls, by_id, root=ROOT):
    """check_golden items 2-5 and 7 for one Golden Set file."""
    if cls is None:
        return [f"{name}: набор неизвестного класса"]
    header, cases = parse_cases(text)
    errors = []
    if header.get("product_class") != cls:
        errors.append(f"{name}: product_class набора не {cls}")
    kinds = {c.get("kind") for c in cases}
    if not {"positive", "negative"} <= kinds:
        errors.append(f"{name}: нет положительного или отрицательного случая")
    for case in cases:
        where = f"{name} {case['id']}"
        if "file" not in case or not (root / case["file"]).is_file():
            errors.append(f"{where}: нет файла случая")
        if case.get("product_class") != cls:
            errors.append(f"{where}: product_class не {cls}")
        if "atomic_function" not in case:
            errors.append(f"{where}: нет atomic_function")
            continue
        expect = case["expect"]
        refusal = product_refusal(cls, case["atomic_function"], by_id)
        catalog_case = (case.get("kind") == "negative" and expect.get("refusing_node") == "n1"
                        and expect.get("reason", "").strip('"').startswith(REASONS))
        if catalog_case and refusal is None:
            errors.append(f"{where}: случай отказа по каталогу объявляет функцию каталога")
        if not catalog_case and refusal is not None:
            errors.append(f"{where}: {refusal}")
        if case.get("kind") == "negative":
            if expect.get("outcome") != "refused":
                errors.append(f"{where}: отрицательный случай не refused")
            if "glossary_pair" not in case and not catalog_case:
                errors.append(f"{where}: нет glossary_pair")
    return errors


class CatalogBindingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog_path, cls.classes, cls.class_domains = products()
        cls.text = CATALOG.read_text(encoding="utf-8")
        cls.errors, cls.by_id = catalog_errors(cls.text, cls.classes, cls.class_domains)

    # check_taxonomies item 6
    def test_products_declare_catalog_and_class_domains(self):
        self.assertEqual(self.catalog_path, "taxonomy/mango-products.yaml")
        self.assertTrue((ROOT / self.catalog_path).is_file())
        self.assertEqual(sorted(self.class_domains), sorted(self.classes))

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

    # check_golden items 2-5 and 7, every golden/cases*.yaml
    def test_golden_sets(self):
        sets = sorted(GOLDEN.glob("cases*.yaml"))
        self.assertIn(GOLDEN / "cases.yaml", sets)
        for path in sets:
            with self.subTest(path.name):
                errors = golden_errors(path.name, path.read_text(encoding="utf-8"),
                                       set_class(path, self.classes), self.by_id)
                self.assertEqual(errors, [])

    def test_golden_has_catalog_refusal_case(self):
        _, cases = parse_cases((GOLDEN / "cases.yaml").read_text(encoding="utf-8"))
        refusals = [c for c in cases if c["expect"].get("refusing_node") == "n1"]
        self.assertEqual([c["atomic_function"] for c in refusals], [OUTSIDE])
        self.assertEqual(refusals[0]["expect"]["outcome"], "refused")
        self.assertEqual(refusals[0]["expect"]["refusing_skill"], "transcript-normalization-contact-center")

    def test_golden_checker_reports_broken_sets(self):
        text = (GOLDEN / "cases.yaml").read_text(encoding="utf-8")
        good = "    atomic_function: call-routing/function/overflow-routing\n"
        broken = {
            "product_class не contact-center": text.replace(
                "    product_class: contact-center\n", "", 1),
            "нет atomic_function": text.replace(good, "", 1),
            REASONS[0]: text.replace(good, "    atomic_function: overflow-routing\n", 1),
            REASONS[1]: text.replace(good, "    atomic_function: call-routing/feature/overflow-rules\n", 1),
            REASONS[2]: text.replace(
                good, "    atomic_function: ivr-voice-menu/function/ivr-menu-navigation\n", 1),
            "объявляет функцию каталога": text.replace(
                f"atomic_function: {OUTSIDE}", "atomic_function: call-routing/function/queue-management"),
        }
        for expected, fixture in broken.items():
            with self.subTest(expected):
                errors = golden_errors("cases.yaml", fixture, "contact-center", self.by_id)
                self.assertTrue(any(expected in e for e in errors), errors)
        self.assertEqual(golden_errors("cases-unknown.yaml", text, set_class(
            Path("cases-unknown.yaml"), self.classes), self.by_id), ["cases-unknown.yaml: набор неизвестного класса"])
        self.assertEqual(set_class(Path("cases-voice-ucaas.yaml"), self.classes), "voice-ucaas")


if __name__ == "__main__":
    unittest.main()
