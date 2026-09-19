#!/usr/bin/env python3
"""Машинный гейт G-mach пакета исполнения MVP BCREQ.

Гейт fail-closed: непройденная проверка останавливает маршрут. Скрипт проверяет
сам пакет (компиляция), а не отдельный прогон: словари закрыты, граф маршрута
разрешим, каждый узел-агент имеет скомпилированный навык, эталоны ссылаются на
существующие слоты и узлы, а в runtime-артефактах нет ссылок в Хаб.

Запуск (из корня пакета либо из корня репозитория Хаба):

    python3 tools/validate-package.py [путь-к-пакету]

Зависимость: PyYAML. Пакет разворачивается копированием в спутник, поэтому
зависимость объявлена здесь, а не подразумевается: `pip install pyyaml`.
"""

from __future__ import annotations

import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - диагностика вместо трассировки
    sys.stderr.write("ERROR: требуется PyYAML: pip install pyyaml\n")
    raise SystemExit(2)

ERRORS: list[str] = []

# Служебные узлы графа: не навыки, скомпилированного SKILL.md не имеют.
PSEUDO_NODES = {"entry", "exit", "refuse", "halt"}

SKILL_SECTIONS = [
    "## Когда применять",
    "## Предусловия",
    "## Шаги",
    "## Обязательные слоты выхода",
    "## Самопроверка (G-self)",
    "## Отказ",
]

# Провенанс компиляции указывает на документы Хаба намеренно: это происхождение,
# а не ссылка времени выполнения. Всё остальное на Хаб ссылаться не вправе.
PROVENANCE_KEYS = ("derived_from:", "compiled_from:", "source:", "hub_ssot:")
HUB_PATH = re.compile(r"\b(ba-meta-model|ba-process-taxonomy|ba-operation-taxonomy|research/|standards/|ops/|docs/rfc/)")


def fail(message: str) -> None:
    ERRORS.append(message)


def load_yaml(root: str, rel: str):
    path = os.path.join(root, rel)
    if not os.path.isfile(path):
        fail(f"отсутствует обязательный файл пакета: {rel}")
        return None
    with open(path, encoding="utf-8") as handle:
        try:
            return yaml.safe_load(handle)
        except yaml.YAMLError as error:
            fail(f"{rel}: YAML не разбирается: {error}")
            return None


def load_json(root: str, rel: str):
    path = os.path.join(root, rel)
    if not os.path.isfile(path):
        fail(f"отсутствует обязательный файл пакета: {rel}")
        return None
    with open(path, encoding="utf-8") as handle:
        try:
            return json.load(handle)
        except json.JSONDecodeError as error:
            fail(f"{rel}: JSON не разбирается: {error}")
            return None


def frontmatter(path: str) -> dict[str, str]:
    """Читает frontmatter построчно, как это делает валидатор Хаба."""
    fields: dict[str, str] = {}
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if not lines or lines[0].strip() != "---":
        return fields
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def check_taxonomies(root: str) -> dict:
    loaded = {}
    for name in ("artifacts", "operations", "processes", "products", "source-tiers", "projections", "domain-glossary"):
        data = load_yaml(root, f"taxonomy/{name}.yaml")
        loaded[name] = data
        if data is None:
            continue
        if name != "domain-glossary" and data.get("closed") is not True:
            fail(f"taxonomy/{name}.yaml: словарь среза обязан быть закрытым (closed: true)")

    operations = loaded.get("operations") or {}
    items = operations.get("items") or []
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    pattern = re.compile(r"^OP-(EXT|TRN|GEN|CHK|ASM)-\d{2}$")
    for item in items:
        op_id = item.get("id", "")
        if not pattern.match(op_id):
            fail(f"taxonomy/operations.yaml: идентификатор вне формата OP-(EXT|TRN|GEN|CHK|ASM)-NN: {op_id!r}")
        if op_id in seen_ids:
            fail(f"taxonomy/operations.yaml: повторяющийся идентификатор операции: {op_id}")
        seen_ids.add(op_id)
        slug = item.get("slug")
        if slug in seen_slugs:
            fail(f"taxonomy/operations.yaml: повторяющийся slug операции: {slug}")
        seen_slugs.add(slug)
        if not item.get("refusal"):
            fail(f"{op_id}: условие отказа обязательно и пустым не бывает")

    processes = loaded.get("processes") or {}
    for skill in processes.get("l3") or []:
        if not skill.get("in_slice"):
            continue
        for slug in skill.get("operations") or []:
            if slug not in seen_slugs:
                fail(f"taxonomy/processes.yaml: навык {skill.get('id')} ссылается на операцию вне словаря: {slug}")

    artifacts = loaded.get("artifacts") or {}
    for item in artifacts.get("items") or []:
        schema = item.get("schema")
        if schema and not os.path.isfile(os.path.join(root, schema)):
            fail(f"taxonomy/artifacts.yaml: {item.get('id')} ссылается на несуществующую схему {schema}")
    return loaded


def check_skills(root: str) -> dict[str, dict]:
    skills_dir = os.path.join(root, ".agents", "skills")
    compiled: dict[str, dict] = {}
    if not os.path.isdir(skills_dir):
        fail("отсутствует каталог .agents/skills: пакет не разворачивается в спутник копированием")
        return compiled
    for entry in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, entry, "SKILL.md")
        rel = f".agents/skills/{entry}/SKILL.md"
        if not os.path.isfile(path):
            fail(f"каталог навыка без SKILL.md: .agents/skills/{entry}")
            continue
        fields = frontmatter(path)
        for required in ("name", "description", "packs", "inputs", "outputs", "contracts", "gates", "compiled_from", "derived_from"):
            if not fields.get(required):
                fail(f"{rel}: обязательное поле frontmatter отсутствует или пусто: {required}")
        if fields.get("name") != entry:
            fail(f"{rel}: поле name ({fields.get('name')!r}) не совпадает с именем каталога ({entry!r})")
        if fields.get("name") in compiled:
            fail(f"{rel}: имя навыка не уникально: {fields.get('name')}")
        body = open(path, encoding="utf-8").read()
        for section in SKILL_SECTIONS:
            if f"\n{section}\n" not in body:
                fail(f"{rel}: отсутствует обязательный раздел {section}")
        for dropped in ("prompts/", "runs/"):
            if dropped in fields.get("derived_from", ""):
                fail(f"{rel}: слой {dropped} отброшен компиляцией и в derived_from попадать не должен")
        compiled[entry] = fields
    return compiled


def check_route(root: str, processes: dict, skills: dict[str, dict]) -> dict:
    graph = load_yaml(root, "routes/rg-bcreq-v1.yaml") or {}
    nodes = graph.get("nodes") or []
    l2_ids = {item.get("id") for item in (processes or {}).get("l2") or []}
    declared = {item.get("id") for item in (processes or {}).get("l2") or [] if item.get("in_slice")}

    for process in graph.get("processes") or []:
        if process not in l2_ids:
            fail(f"routes/rg-bcreq-v1.yaml: процесс вне закрытого словаря: {process}")
        elif process not in declared:
            fail(f"routes/rg-bcreq-v1.yaml: процесс {process} не объявлен входящим в срез (in_slice)")

    # Навык узла записан идентификатором таксономии (SK-*), навык на диске —
    # именем каталога. Связь задаётся полем packs скомпилированного навыка.
    by_pack = {}
    for name, fields in skills.items():
        pack = fields.get("packs", "")
        if "/" in pack:
            by_pack[pack.split("/", 1)[1]] = name

    node_ids: set[str] = set()
    for node in nodes:
        node_id = node.get("node")
        if node_id in node_ids:
            fail(f"routes/rg-bcreq-v1.yaml: повторяющийся узел {node_id}")
        node_ids.add(node_id)
        if node.get("process") not in l2_ids:
            fail(f"{node_id}: процесс узла вне закрытого словаря: {node.get('process')}")
        if not node.get("gates"):
            fail(f"{node_id}: узел без гейта запрещён")
        actor = node.get("actor")
        if actor == "agent":
            if node.get("skill") not in by_pack:
                fail(f"{node_id}: узел-агент ссылается на навык без скомпилированного SKILL.md: {node.get('skill')}")
        elif actor == "human":
            if not node.get("note"):
                fail(f"{node_id}: человеческий узел обязан нести основание, почему навык не скомпилирован")
        else:
            fail(f"{node_id}: actor обязан быть agent или human, получено {actor!r}")

    known = node_ids | PSEUDO_NODES
    outgoing: set[str] = set()
    reachable = {"entry"}
    edges = graph.get("edges") or []
    for edge in edges:
        source, target = edge.get("from"), edge.get("to")
        for endpoint in (source, target):
            if endpoint not in known:
                fail(f"routes/rg-bcreq-v1.yaml: ребро ссылается на неизвестный узел: {endpoint}")
        if not edge.get("condition"):
            fail(f"ребро {source} → {target}: условие перехода обязательно (ребро «по усмотрению» запрещено)")
        outgoing.add(source)

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if edge.get("from") in reachable and edge.get("to") not in reachable:
                reachable.add(edge.get("to"))
                changed = True
    for node_id in sorted(node_ids):
        if node_id not in reachable:
            fail(f"{node_id}: узел недостижим из entry")
        if node_id not in outgoing:
            fail(f"{node_id}: у узла нет исходящего ребра, траектория обрывается")

    policy = graph.get("gate_policy") or {}
    if policy.get("fail_closed") is not True:
        fail("routes/rg-bcreq-v1.yaml: gate_policy.fail_closed обязан быть true")
    if policy.get("corrective_attempts") != 1:
        fail("routes/rg-bcreq-v1.yaml: допускается ровно одна корректирующая попытка узла")
    if not (graph.get("trace") or {}).get("required"):
        fail("routes/rg-bcreq-v1.yaml: состав обязательного следа не объявлен")
    return graph


def check_golden(root: str, graph: dict, skills: dict, glossary: dict) -> None:
    schema = load_json(root, "contracts/c-out-bcreq.schema.json") or {}
    slots = set(((schema.get("properties") or {}).get("slots") or {}).get("required") or [])
    cases = load_yaml(root, "golden/cases.yaml") or {}
    node_ids = {node.get("node") for node in graph.get("nodes") or []}
    terms = {term.get("id") for term in (glossary or {}).get("terms") or []}

    case_list = cases.get("cases") or []
    kinds = {case.get("kind") for case in case_list}
    if "positive" not in kinds or "negative" not in kinds:
        fail("golden/cases.yaml: минимальный Golden Set обязан содержать и положительный, и отрицательный случай")

    for case in case_list:
        case_id = case.get("id")
        rel = case.get("file", "")
        if not os.path.isfile(os.path.join(root, rel)):
            fail(f"{case_id}: файл эталона отсутствует: {rel}")
        expect = case.get("expect") or {}
        if case.get("kind") == "positive":
            filled = set(expect.get("filled") or [])
            empty = set((expect.get("empty_with_reason") or {}).keys())
            unknown = (filled | empty) - slots
            if unknown:
                fail(f"{case_id}: слоты вне закрытого перечня контракта: {sorted(unknown)}")
            missing = slots - filled - empty
            if missing:
                fail(f"{case_id}: слот не объявлен ни заполненным, ни пустым с причиной: {sorted(missing)}")
            overlap = filled & empty
            if overlap:
                fail(f"{case_id}: слот объявлен одновременно заполненным и пустым: {sorted(overlap)}")
            if not expect.get("trace_nonempty"):
                fail(f"{case_id}: положительный эталон без требования непустого следа")
        else:
            if expect.get("outcome") != "refused":
                fail(f"{case_id}: отрицательный эталон обязан ожидать отказ")
            if expect.get("refusing_node") not in node_ids:
                fail(f"{case_id}: отказывающий узел вне графа маршрута: {expect.get('refusing_node')}")
            if expect.get("refusing_skill") not in skills:
                fail(f"{case_id}: отказывающий навык не скомпилирован: {expect.get('refusing_skill')}")
            for term in case.get("glossary_pair") or []:
                if term not in terms:
                    fail(f"{case_id}: термин вне словаря домена: {term}")


def check_source_tiers(root: str, tiers: dict) -> None:
    """Контракт маршрутизации источников: объявлен уровень, форма доказательства и порядок."""
    tiers = tiers or {}
    forms = {form.get("id") for form in tiers.get("evidence_forms") or []}
    declared = [tier.get("id") for tier in tiers.get("tiers") or []]
    if not declared:
        fail("taxonomy/source-tiers.yaml: словарь уровней источников пуст — маршрутизация знания не объявлена")
    for tier in tiers.get("tiers") or []:
        if tier.get("evidence_form") not in forms:
            fail(f"{tier.get('id')}: форма доказательства вне перечня evidence_forms")
        if not tier.get("rationale"):
            fail(f"{tier.get('id')}: уровень источника без обоснования применимости")
    order = tiers.get("order") or []
    if sorted(order) != sorted(declared):
        fail("taxonomy/source-tiers.yaml: порядок применения не покрывает ровно объявленные уровни")
    for rule in ("conflict_rule", "escalation_rule", "investment_rule"):
        if not tiers.get(rule):
            fail(f"taxonomy/source-tiers.yaml: отсутствует {rule} — расхождение источников разрешалось бы усмотрением")
    for item in tiers.get("out_of_slice") or []:
        if not item.get("why"):
            fail(f"{item.get('id')}: уровень вне среза без объявленной причины — необъявленная ветка")

    schema = load_json(root, "contracts/c-in.schema.json") or {}
    source_item = (((schema.get("properties") or {}).get("sources") or {}).get("items") or {})
    if "tier" not in (source_item.get("required") or []):
        fail("contracts/c-in.schema.json: уровень источника обязан быть обязательным полем (fail-closed)")
    enum = ((source_item.get("properties") or {}).get("tier") or {}).get("enum") or []
    in_slice = [tier.get("id") for tier in tiers.get("tiers") or [] if tier.get("in_slice")]
    if sorted(enum) != sorted(in_slice):
        fail("contracts/c-in.schema.json: перечень уровней источника расходится с закрытым словарём source-tiers")


def check_projections(root: str, projections: dict) -> None:
    """Проекция перестаёт быть пустой веткой: обязательна в контракте и разрешима в словарь."""
    projections = projections or {}
    schema = load_json(root, "contracts/c-out-bcreq.schema.json") or {}
    slots = set(((schema.get("properties") or {}).get("slots") or {}).get("required") or [])
    if "projection" not in (schema.get("required") or []):
        fail("contracts/c-out-bcreq.schema.json: проекция обязана быть обязательным полем — иначе ветка не исполняется")
    enum = ((schema.get("properties") or {}).get("projection") or {}).get("enum") or []
    declared = [item.get("id") for item in projections.get("items") or []]
    if sorted(enum) != sorted(declared):
        fail("contracts/c-out-bcreq.schema.json: перечень проекций расходится с закрытым словарём projections")
    for item in projections.get("items") or []:
        unknown = set(item.get("required_slots") or []) - slots
        if unknown:
            fail(f"{item.get('id')}: обязательные слоты проекции вне закрытого перечня: {sorted(unknown)}")
        if not item.get("required_slots"):
            fail(f"{item.get('id')}: проекция без обязательных слотов не отличается от отсутствия проекции")
        for field in ("addressee", "wording_rule"):
            if not item.get(field):
                fail(f"{item.get('id')}: проекция без поля {field} не задаёт предмет проверки гейта")


def check_confusable_coverage(root: str, glossary: dict, cases: dict) -> None:
    """Правило EP-G7 в исполняемом виде: пара близких терминов обязана иметь отрицательный случай.

    До этой проверки EP-G7 существовало как текст правила и один эталон: три из
    четырёх объявленных пар словаря не имели ни одного теста, то есть правило
    было выполнено формально.
    """
    terms = (glossary or {}).get("terms") or []
    id_by_name: dict[str, str] = {}
    for term in terms:
        id_by_name[term.get("term")] = term.get("id")
        for alias in term.get("aliases") or []:
            id_by_name.setdefault(alias, term.get("id"))

    covered: set[frozenset[str]] = set()
    for case in (cases or {}).get("cases") or []:
        pair = case.get("glossary_pair") or []
        if len(pair) == 2:
            covered.add(frozenset(pair))

    expected: set[frozenset[str]] = set()
    for term in terms:
        for other in term.get("confusable_with") or []:
            name = other.get("term") if isinstance(other, dict) else other
            target = id_by_name.get(name)
            if target is None:
                fail(f"{term.get('id')}: confusable_with ссылается на термин вне словаря: {name!r}")
                continue
            if not (other.get("why") if isinstance(other, dict) else True):
                fail(f"{term.get('id')}: пара близких терминов без объяснения подмены не проверяема")
            expected.add(frozenset({term.get("id"), target}))

    missing = expected - covered
    if missing:
        listed = sorted(" + ".join(sorted(pair)) for pair in missing)
        fail(
            "EP-G7: пара близких терминов словаря домена не покрыта отрицательным случаем Golden Set: "
            + "; ".join(listed)
        )


def check_metrics(root: str) -> None:
    data = load_yaml(root, "evaluation/metrics.yaml") or {}
    declared = {item.get("id") for item in data.get("metrics") or []}
    expected = {f"M-{i}" for i in range(1, 6)} | {f"MP-{i}" for i in range(1, 7)}
    missing = expected - declared
    if missing:
        fail(f"evaluation/metrics.yaml: базовая линия неполна, отсутствуют метрики: {sorted(missing)}")
    for item in data.get("metrics") or []:
        if not item.get("formula") or not item.get("target"):
            fail(f"{item.get('id')}: метрика без формулы или цели не измеряется")


def check_runtime_independence(root: str) -> None:
    """Контракт 2: ни один артефакт времени выполнения не ссылается в Хаб."""
    runtime_dirs = (".agents", "routes", "templates", "golden", "evaluation", "taxonomy", "contracts")
    for directory in runtime_dirs:
        base = os.path.join(root, directory)
        for current, _dirs, files in os.walk(base):
            for filename in sorted(files):
                path = os.path.join(current, filename)
                rel = os.path.relpath(path, root)
                with open(path, encoding="utf-8") as handle:
                    for number, line in enumerate(handle, start=1):
                        if line.lstrip().startswith("#") or line.lstrip().startswith("//"):
                            continue
                        if any(key in line for key in PROVENANCE_KEYS):
                            continue
                        if HUB_PATH.search(line):
                            fail(
                                f"{rel}:{number}: ссылка в документ Хаба во время выполнения "
                                "(дефект компиляции, контракт 2): " + line.strip()[:80]
                            )


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.abspath(root)
    if not os.path.isdir(os.path.join(root, "taxonomy")):
        sys.stderr.write(f"ERROR: каталог не похож на пакет исполнения: {root}\n")
        return 2

    taxonomies = check_taxonomies(root)
    skills = check_skills(root)
    graph = check_route(root, taxonomies.get("processes") or {}, skills)
    check_golden(root, graph, skills, taxonomies.get("domain-glossary") or {})
    check_source_tiers(root, taxonomies.get("source-tiers") or {})
    check_projections(root, taxonomies.get("projections") or {})
    check_confusable_coverage(
        root,
        taxonomies.get("domain-glossary") or {},
        load_yaml(root, "golden/cases.yaml") or {},
    )
    check_metrics(root)
    check_runtime_independence(root)

    for schema in ("c-in", "c-core", "c-quest", "c-out-bcreq", "c-rk"):
        load_json(root, f"contracts/{schema}.schema.json")

    if ERRORS:
        for message in ERRORS:
            sys.stderr.write(f"ERROR: {message}\n")
        sys.stderr.write(f"G-mach: пакет отвергнут, ошибок: {len(ERRORS)}.\n")
        return 1

    print(f"G-mach: пакет принят (навыков: {len(skills)}, узлов маршрута: {len(graph.get('nodes') or [])}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
