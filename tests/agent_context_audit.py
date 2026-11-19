#!/usr/bin/env python3
"""As-Is audit of the agent context of this repository (RFC-RT-002, issue #25).

The script is read-only: it inventories tracked files, client-specific
context packages, agent entry points and skills, and prints an evidence log
for hypotheses H1-H3 of the RFC. It needs only the standard library and git.

Usage (from the repository root):

    python tests/agent_context_audit.py > tests/agent_context_audit.log
    python tests/agent_context_audit.py --base 90f0823 \
        --deps runtime-deps.json --handoff ssot-stage1-handoff-manifest.json

``--deps`` and ``--handoff`` take local copies of the stage-1 audit files from
G-Ivan-A/mango_ba_prompts; their sha256 is checked against the pinned values
below, so the embedded summary can be re-derived. Without them the script
uses the embedded summary. ``--base`` compares the protected paths with a git
revision byte for byte.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT_VERSION = "0.1"

# Stage-1 inputs (task 1: G-Ivan-A/mango_ba_prompts#492, PR #493, merged as
# 7611c041). Pinned by commit and sha256 of the file bytes.
STAGE1_REPO = "G-Ivan-A/mango_ba_prompts"
STAGE1_COMMIT = "7af2dc57bb4481d8bed7134ea8f396d3f1f51eda"
DEPS_PATH = "experiments/issue_492/runtime-deps.json"
DEPS_SHA256 = "a7db1c665f844413c5a844768b82649387510f8f4beb751a18c1035b52e8c9cb"
HANDOFF_PATH = "docs/contracts/ssot-stage1-handoff-manifest.json"
HANDOFF_SHA256 = "00d71f4a71211bf57547b27cfd2882a76c54d394b51293ea8075ad842e7d0937"
REGISTRY_SHA = "68ad8fcffd47439fc3051852d9a2fbbe23815855"

# Runtime paths that stage-1 consumers read (runtime-deps.json, `paths`),
# except the 422 single-file rows under docs/kb, which are summarised by
# DEPS_KB. Value: (status, consumers, reference types).
DEPS_PATHS = {
    "/": ("защищённый", "валидатор, сайт, сборка", "SHA (иной срез), SHA (реестр), main, корень, шаблон"),
    "AGENTS.md": ("защищённый", "валидатор", "SHA (иной срез)"),
    "README.md": ("защищённый", "валидатор", "SHA (иной срез)"),
    "contracts/c-in.md": ("защищённый", "валидатор", "SHA (иной срез)"),
    "docs/kb": ("защищённый", "валидатор", "SHA (иной срез), шаблон"),
    "docs/kb/MAP.json": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр), main"),
    "docs/kb/README.md": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр), main"),
    "docs/kb/USAGE.md": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр), main"),
    "evaluation/g-human-checklist.md": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр)"),
    "evaluation/validate-package.md": ("защищённый", "валидатор", "SHA (иной срез)"),
    "golden/cases-analytics-reporting.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (реестр)"),
    "golden/cases-voice-ucaas.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (реестр)"),
    "golden/cases.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр), клон"),
    "golden/gs-cc-01-queue-overflow.md": ("защищённый", "валидатор", "SHA (иной срез)"),
    "golden/gs-cc-neg-03-sla-vs-aht.md": ("защищённый", "валидатор", "SHA (иной срез)"),
    "routes/rg-bcreq-v1.yaml": ("защищённый", "валидатор", "SHA (иной срез)"),
    "skills/": ("защищённый", "валидатор", "SHA (иной срез)"),
    "taxonomy/domain-glossary-analytics-reporting.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (реестр)"),
    "taxonomy/domain-glossary-voice-ucaas.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр)"),
    "taxonomy/domain-glossary.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (реестр)"),
    "taxonomy/mango-products.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр), клон"),
    "taxonomy/processes.yaml": ("защищённый", "валидатор", "SHA (иной срез)"),
    "taxonomy/products.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр), main, клон"),
    "taxonomy/projections.yaml": ("защищённый", "валидатор", "SHA (иной срез)"),
    "taxonomy/source-tiers.yaml": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр)"),
    "templates/bcreq-skeleton.md": ("защищённый (двойной)", "валидатор, модель, сайт", "SHA (иной срез), SHA (реестр)"),
}
DEPS_KB = {"rows": 424, "защищённый": 419, "защищённый (двойной)": 3, "свободный": 2}
DEPS_SUMMARY = {"runtime_paths": 447, "защищённый": 431, "защищённый (двойной)": 14, "свободный": 2}
HANDOFF_SUMMARY = {
    "source_commit": "7dea8f716d69e55c183865630d10f40cdb6e46b1",
    "artifacts": 133,
    "contracts": 24,
    "in_runtime": 0,
    "transfer_cards": {"BL-185": 38, "BL-186": 31, "BL-187": 62, "BL-188": 2},
}

# Directories the ФТ-4 constraint keeps byte for byte (issue #25, section 3).
PROTECTED_DIRS = ["docs/kb", "taxonomy", "templates", "golden", "evaluation"]

# Purpose of each top-level element, taken from README.md («Состав»),
# AGENTS.md («Что здесь есть») and compilation-manifest.yaml (deployment.result).
PURPOSE = {
    ".github": "CI: smoke и unittest при push/pull_request",
    ".gitignore": "исключение байткода Python",
    "AGENTS.md": "загрузочный системный промпт маршрута RG-BCREQ-v1",
    "README.md": "вход человека: первый запуск, состав, навигация БЗ",
    "compilation-manifest.yaml": "происхождение пакета: copied / transformed / discarded",
    "contracts": "системные промпты-контракты C-IN, C-CORE, C-QUEST, C-OUT-BCREQ, C-RK",
    "docs": "docs/kb — БЗ ST-5-LOCAL; docs/guides — инструкции пользователя",
    "evaluation": "метрики, чек-листы гейтов, промпт G-mach",
    "golden": "Golden Set по продуктовым классам",
    "routes": "граф маршрута и шаблон листа прогона",
    "skills": "11 навыков узлов маршрута",
    "taxonomy": "закрытые словари, каталог продуктов, уровни источников",
    "templates": "скелеты A-BCREQ, A-QUEST, A-CORE",
    "tests": "проверки репозитория (smoke, unittest), этот аудит",
}

# Consumers of elements that stage-1 files do not reference.
OTHER_CONSUMER = {
    ".github": "CI (GitHub Actions)",
    ".gitignore": "git",
    "compilation-manifest.yaml": "человек; tests/test_source_pin.py",
    "tests": "CI (GitHub Actions)",
}

# Context files of agent clients. Each path is the convention documented by
# the client (see RFC-RT-002, section «Матрица совместимости клиентов»).
CLIENT_MARKERS = [
    ("AGENTS.md", "открытый стандарт AGENTS.md (OpenCode, Codex и др.)"),
    ("CLAUDE.md", "Claude Code"),
    (".claude", "Claude Code"),
    ("GEMINI.md", "Gemini CLI"),
    (".gemini", "Gemini CLI"),
    (".opencode", "OpenCode"),
    ("opencode.json", "OpenCode"),
    ("opencode.jsonc", "OpenCode"),
    (".agents", "каталог навыков .agents/skills"),
    (".hub-profile.json", "профиль среды исполнения Хаба"),
    (".clinerules", "Cline"),
    (".cursor", "Cursor"),
    (".cursorrules", "Cursor (устаревший формат)"),
    (".windsurf", "Windsurf"),
    (".windsurfrules", "Windsurf"),
    (".github/copilot-instructions.md", "GitHub Copilot"),
    (".github/instructions", "GitHub Copilot"),
    (".qwen", "Qwen Code"),
    (".gigacode", "GigaCode"),
    ("QWEN.md", "Qwen Code"),
]

CLIENT_NAMES = re.compile(
    r"\b(gigacode|cline|cursor|opencode|copilot|windsurf|claude|qwen|codex|gemini|gitverse)\b",
    re.IGNORECASE,
)

# Elements of the navigation contract the issue asks for (ФТ-2).
AGENTS_CHECKS = [
    ("маркер ACCESS_GAP", r"ACCESS_GAP"),
    ("запрет имитации чтения (unverified)", r"unverified"),
    ("правило цитирования: локатор + дословная цитата", r"локатор\s+плюс\s+дословная\s+цитата"),
    ("навигация БЗ: README.md базы знаний", r"docs/kb/README\.md"),
    ("навигация БЗ: MAP.json", r"MAP\.json"),
    ("навигация БЗ: sections_toc / *.toc.tsv", r"sections_toc|toc\.tsv"),
    ("навигация БЗ: USAGE.md", r"USAGE\.md"),
    ("навигация БЗ: index.md → sections/", r"index\.md` → `sections/"),
]


def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout if result.returncode == 0 else ""


def tracked_files() -> list[str]:
    return [line for line in git("ls-files", "-z").split("\0") if line]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def tree_digest(files: list[str]) -> str:
    """sha256 over sorted «path NUL sha256(bytes) LF» lines."""
    digest = hashlib.sha256()
    for path in sorted(files):
        digest.update(path.encode() + b"\0")
        digest.update(sha256_bytes((ROOT / path).read_bytes()).encode() + b"\n")
    return digest.hexdigest()


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    fields = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"')
    return fields


def top_level(path: str) -> str:
    return path.split("/", 1)[0]


def section(title: str) -> None:
    print()
    print(f"## {title}")
    print()


def report_inventory(files: list[str]) -> None:
    section("1. Инвентаризация (ФТ-1): элементы верхнего уровня")
    groups: dict[str, list[str]] = collections.defaultdict(list)
    for path in files:
        groups[top_level(path)].append(path)
    print("| Элемент | Файлов | Байт | sha256 дерева (12) | Назначение | Потребитель этапа 1 (#492) |")
    print("| --- | ---: | ---: | --- | --- | --- |")
    for name in sorted(groups):
        items = groups[name]
        size = sum((ROOT / p).stat().st_size for p in items)
        consumers = sorted(
            {DEPS_PATHS[p][1] for p in DEPS_PATHS if p != "/" and top_level(p.strip("/")) == name}
        )
        consumer = "; ".join(consumers) if consumers else OTHER_CONSUMER.get(name, "не найден")
        print(
            f"| `{name}` | {len(items)} | {size} | {tree_digest(items)[:12]} | "
            f"{PURPOSE.get(name, 'не описан')} | {consumer} |"
        )


def report_protected(files: list[str], base: str | None) -> None:
    section("2. Защищённые пути этапа 1 (ФТ-4)")
    print(f"Источник: {STAGE1_REPO}@{STAGE1_COMMIT[:8]}:{DEPS_PATH} (sha256 {DEPS_SHA256[:12]}).")
    print(f"Сводка #492: {DEPS_SUMMARY}; строк docs/kb/*: {DEPS_KB}.")
    print()
    print("| Путь | Статус | Потребитель | Тип ссылки | Есть в рабочем дереве |")
    print("| --- | --- | --- | --- | --- |")
    tracked = set(files)
    for path, (status, consumer, refs) in DEPS_PATHS.items():
        clean = path.strip("/")
        exists = clean == "" or clean in tracked or any(f.startswith(clean + "/") for f in tracked)
        print(f"| `{path}` | {status} | {consumer} | {refs} | {'да' if exists else 'НЕТ'} |")
    print()
    print("Дайджест защищённых каталогов (sha256 по «путь NUL sha256 LF»):")
    for directory in PROTECTED_DIRS:
        items = [f for f in files if f.startswith(directory + "/")]
        print(f"- `{directory}`: {len(items)} файлов, {tree_digest(items)}")
    if base:
        for ref in (base, REGISTRY_SHA):
            if not git("rev-parse", "--verify", "--quiet", ref + "^{commit}", check=False):
                print(f"- сравнение с `{ref[:12]}`: ревизия недоступна (неполный клон)")
                continue
            changed = git("diff", "--name-only", ref, "--", *PROTECTED_DIRS).split()
            print(f"- изменено в защищённых каталогах относительно `{ref[:12]}`: {len(changed)}")
            for path in changed:
                print(f"  - {path}")


def report_clients(files: list[str]) -> None:
    section("3. Г1: пакеты и файлы контекста агентных клиентов")
    tracked = set(files)
    print("| Путь | Клиент | В рабочем дереве | Последнее удаление в истории |")
    print("| --- | --- | --- | --- |")
    shallow = git("rev-parse", "--is-shallow-repository", check=False).strip() == "true"
    for path, client in CLIENT_MARKERS:
        present = path in tracked or any(f.startswith(path + "/") for f in tracked)
        removed = ""
        if shallow:
            removed = "история недоступна (неполный клон)"
        else:
            log = git("log", "--diff-filter=D", "--format=%h %ad", "--date=short", "-1", "--", path, check=False)
            removed = log.strip() or "—"
        print(f"| `{path}` | {client} | {'да' if present else 'нет'} | {removed} |")
    print()
    print("Упоминания имён клиентов в отслеживаемых файлах вне docs/kb:")
    hits = collections.Counter()
    kb_hits = 0
    for path in files:
        try:
            text = (ROOT / path).read_text(encoding="utf-8")
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        found = len(CLIENT_NAMES.findall(text))
        if not found:
            continue
        if path.startswith("docs/kb/"):
            kb_hits += found
        else:
            hits[path] += found
    for path, count in sorted(hits.items()):
        print(f"- `{path}`: {count}")
    if not hits:
        print("- нет")
    print(f"- docs/kb (продуктовая БЗ, не конфигурация клиента): {kb_hits}")
    if not shallow:
        print()
        print("Коммиты, удалившие срез под среду исполнения:")
        for marker in (".hub-profile.json", ".agents"):
            entry = git("log", "--diff-filter=D", "--format=%h %ad %s", "--date=short", "-1", "--", marker, check=False).strip()
            if entry:
                print(f"- `{marker}`: {entry}")
                body = git("show", "-s", "--format=%b", entry.split()[0], check=False)
                for line in body.splitlines():
                    if line.strip():
                        print(f"  > {line.strip()}")
                break


def report_entry_and_skills(files: list[str]) -> None:
    section("4. Г2: единый вход AGENTS.md и каталог навыков")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    meta = frontmatter(agents)
    print(f"AGENTS.md: version {meta.get('version')}, updated {meta.get('updated')}, {len(agents.encode())} байт.")
    print()
    print("| Элемент контракта ФТ-2 | В AGENTS.md |")
    print("| --- | --- |")
    for label, pattern in AGENTS_CHECKS:
        print(f"| {label} | {'да' if re.search(pattern, agents) else 'нет'} |")
    print()
    skills = sorted(f for f in files if f.startswith("skills/"))
    layouts = collections.Counter(
        "skills/<имя>/SKILL.md" if f.endswith("/SKILL.md") else "skills/<имя>.md" for f in skills
    )
    print(f"Навыков: {len(skills)}; раскладка: {dict(layouts)}.")
    keys = collections.Counter()
    for path in skills:
        keys.update(frontmatter((ROOT / path).read_text(encoding="utf-8")).keys())
    print(f"Поля frontmatter навыков (поле: число навыков): {dict(sorted(keys.items()))}.")
    for field in ("version", "compiled_from", "derived_from", "compiled_at"):
        print(f"- поле `{field}` есть у {keys.get(field, 0)} из {len(skills)} навыков")
    print()
    print("| Навык | version | compiled_at | compiled_from.source_commit | слой meta_model |")
    print("| --- | --- | --- | --- | --- |")
    for path in skills:
        meta = frontmatter((ROOT / path).read_text(encoding="utf-8"))
        origin = meta.get("compiled_from", "")
        commit = re.search(r"source_commit:\s*([0-9a-f]+)", origin)
        layer = re.search(r"meta_model:\s*([0-9.]+)", origin)
        print(
            f"| `{meta.get('name')}` | {meta.get('version')} | {meta.get('compiled_at')} | "
            f"{commit.group(1)[:12] if commit else '—'} | {layer.group(1) if layer else '—'} |"
        )
    print(f"- каталог `agents/`: {'есть' if any(f.startswith('agents/') for f in files) else 'нет'}")


def report_staleness(files: list[str]) -> None:
    section("5. Г3: иная устаревшая информация")
    manifest = (ROOT / "compilation-manifest.yaml").read_text(encoding="utf-8")
    m_version = re.search(r'^version:\s*"?([^"\n]+)', manifest, re.M).group(1)
    m_meta = re.search(r'^meta_model_version:\s*"?([^"\n]+)', manifest, re.M).group(1)
    m_compiled = re.search(r"^compiled_at:\s*(\S+)", manifest, re.M).group(1)
    print(f"compilation-manifest.yaml: version {m_version}, meta_model_version {m_meta}, compiled_at {m_compiled}.")
    print()
    print("| Файл | version | meta_model_version | updated | Расхождение с манифестом |")
    print("| --- | --- | --- | --- | --- |")
    candidates = ["AGENTS.md", "README.md"] + sorted(
        f for f in files if f.startswith(("contracts/", "evaluation/", "templates/", "docs/guides/")) and f.endswith(".md")
    )
    for path in candidates:
        meta = frontmatter((ROOT / path).read_text(encoding="utf-8"))
        notes = []
        if meta.get("meta_model_version") and meta["meta_model_version"] != m_meta:
            notes.append(f"meta_model_version {meta['meta_model_version']} ≠ {m_meta}")
        if path == "README.md" and meta.get("version") != m_version:
            notes.append(f"версия пакета {meta.get('version')} ≠ {m_version}")
        if meta.get("updated") and meta["updated"] < m_compiled:
            notes.append(f"updated раньше compiled_at {m_compiled}")
        print(
            f"| `{path}` | {meta.get('version', '—')} | {meta.get('meta_model_version', '—')} | "
            f"{meta.get('updated', '—')} | {'; '.join(notes) or '—'} |"
        )
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    heading = re.search(r"^# .*$", readme, re.M).group(0)
    print()
    print(f"- заголовок README.md: «{heading[2:]}»")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    print(
        "- навигация БЗ: README.md — "
        f"{'MAP.json → toc.tsv' if 'MAP.json' in readme else 'нет MAP.json'}; AGENTS.md — "
        f"{'MAP.json' if 'MAP.json' in agents else 'index.md → sections/ (без MAP.json и sections_toc)'}"
    )
    print("- упоминания прежнего источника модели (Хаб) вне compilation-manifest.yaml и tests/:")
    for path in files:
        if path.startswith(("docs/kb/", "tests/")) or path == "compilation-manifest.yaml":
            continue
        try:
            lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, 1):
            if re.search(r"Хаб|hybrid-Intelligence-lab", line):
                print(f"  - `{path}:{number}`: {line.strip()[:110]}")


# Smoke-test rules (tests/runtime-smoke.sh) that an as-is copy would meet.
SMOKE_ENV = re.compile(r"GigaCode|GitVerse|Qwen|\.schema\.json|\.agents/|tools/validate|hub-profile")
SMOKE_BAN = re.compile(r"не подключать|out_of_slice", re.I)
SMOKE_REF = re.compile(r"(?:^|[\]\[ `(,])((?:contracts|skills|taxonomy|routes|templates|golden|evaluation)/[A-Za-z0-9._-]+\.(?:md|yaml))")
# Result of --stage1-repo at HANDOFF_SUMMARY["source_commit"], kept for offline runs.
INTAKE_SUMMARY = {
    "sha256_match": 133,
    "extensions": {"md": 126, "json": 7},
    "env_word_hits": ["standards/bcreq-lessons/golden-set-bcreq-stage1.md"],
    "ban_hits": [],
    "missing_refs": [],
}


def intake_check(handoff: dict, repo: str) -> dict:
    """Read every handoff artifact at source_commit and apply the smoke rules."""
    commit = handoff["source_commit"]
    result = {"sha256_match": 0, "extensions": collections.Counter(), "env_word_hits": [],
              "ban_hits": [], "missing_refs": set()}
    for artifact in handoff["artifacts"]:
        path = artifact["path"]
        data = subprocess.run(["git", "-C", repo, "show", f"{commit}:{path}"],
                              capture_output=True, check=True).stdout
        result["sha256_match"] += sha256_bytes(data) == artifact["sha256"]
        result["extensions"][path.rsplit(".", 1)[-1]] += 1
        text = data.decode("utf-8", "replace")
        if SMOKE_ENV.search(text):
            result["env_word_hits"].append(path)
        if SMOKE_BAN.search(text):
            result["ban_hits"].append(path)
        for line in text.splitlines():
            for ref in SMOKE_REF.findall(line):
                if not (ROOT / ref).exists():
                    result["missing_refs"].add(ref)
    result["extensions"] = dict(result["extensions"])
    result["missing_refs"] = sorted(result["missing_refs"])
    return result


def report_handoff(handoff: dict | None, intake: dict | None) -> None:
    section("6. Приём SSOT этапа 1 (ФТ-3): манифест задачи 1")
    print(f"Источник: {STAGE1_REPO}@{STAGE1_COMMIT[:8]}:{HANDOFF_PATH} (sha256 {HANDOFF_SHA256[:12]}).")
    print(f"Сводка: {HANDOFF_SUMMARY}.")
    if handoff:
        print()
        print("| Карточка | Каталог источника | Артефактов |")
        print("| --- | --- | --- |")
        groups = collections.Counter(
            (a["transfer_card"], "/".join(a["path"].split("/")[:2])) for a in handoff["artifacts"])
        for (card, folder), count in sorted(groups.items()):
            print(f"| {card} | `{folder}` | {count} |")
    print()
    if intake is not None:
        assert intake == INTAKE_SUMMARY, intake
        print("Проверка копии как есть по правилам tests/runtime-smoke.sh: пересчитано по клону, совпадает со встроенной.")
    else:
        print("Проверка копии как есть по правилам tests/runtime-smoke.sh (встроенный результат; пересчёт — --stage1-repo):")
    print(f"- sha256 совпадает у {INTAKE_SUMMARY['sha256_match']} из {HANDOFF_SUMMARY['artifacts']} артефактов;")
    print(f"- расширения: {INTAKE_SUMMARY['extensions']} — файлы .json вне docs/kb, tests, .github нарушают проверку 'no .py or .json runtime files';")
    print(f"- слова привязки к среде: {INTAKE_SUMMARY['env_word_hits']};")
    print(f"- явные запреты внешних баз: {INTAKE_SUMMARY['ban_hits'] or 'нет'};")
    print(f"- относительные ссылки (contracts|skills|…)/x.(md|yaml) без файла в runtime: {INTAKE_SUMMARY['missing_refs'] or 'нет'}.")


def load_pinned(path: str | None, expected: str, label: str) -> dict | None:
    if not path:
        return None
    raw = Path(path).read_bytes()
    actual = sha256_bytes(raw)
    if actual != expected:
        raise SystemExit(f"{label}: sha256 {actual} ≠ закреплённого {expected}")
    return json.loads(raw)


def verify_embedded(deps: dict | None, handoff: dict | None) -> None:
    if deps:
        rows = {r["runtime_path"]: r for r in deps["paths"]}
        for path, (status, _, _) in DEPS_PATHS.items():
            assert rows[path]["status"] == status, path
        kb = [r for r in deps["paths"] if r["runtime_path"].startswith("docs/kb/") and r["runtime_path"] not in DEPS_PATHS]
        counted = collections.Counter(r["status"] for r in kb)
        assert len(kb) + 3 == DEPS_KB["rows"], len(kb)
        assert counted["свободный"] == DEPS_KB["свободный"], counted
        print("Встроенная сводка #492 сверена с runtime-deps.json: совпадает.")
    if handoff:
        assert handoff["source_commit"] == HANDOFF_SUMMARY["source_commit"]
        assert len(handoff["artifacts"]) == HANDOFF_SUMMARY["artifacts"]
        assert len(handoff["contracts"]) == HANDOFF_SUMMARY["contracts"]
        present = [a["path"] for a in handoff["artifacts"] if (ROOT / a["path"]).exists()]
        print(f"Сверено с манифестом передачи: артефактов уже в runtime — {len(present)}.")
        cards = collections.Counter(a["transfer_card"] for a in handoff["artifacts"])
        assert dict(cards) == HANDOFF_SUMMARY["transfer_cards"], cards


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", help="git-ревизия для побайтного сравнения защищённых каталогов")
    parser.add_argument("--deps", help=f"локальная копия {DEPS_PATH}")
    parser.add_argument("--handoff", help=f"локальная копия {HANDOFF_PATH}")
    parser.add_argument("--stage1-repo", help=f"локальный клон {STAGE1_REPO} с коммитом source_commit (нужен --handoff)")
    args = parser.parse_args(argv)
    deps = load_pinned(args.deps, DEPS_SHA256, DEPS_PATH)
    handoff = load_pinned(args.handoff, HANDOFF_SHA256, HANDOFF_PATH)

    files = tracked_files()
    print(f"# Аудит As-Is агентного контекста (RFC-RT-002), версия скрипта {AUDIT_VERSION}")
    print()
    print(f"HEAD: {git('rev-parse', 'HEAD').strip()}; отслеживаемых файлов: {len(files)}.")
    verify_embedded(deps, handoff)
    report_inventory(files)
    report_protected(files, args.base)
    report_clients(files)
    report_entry_and_skills(files)
    report_staleness(files)
    intake = intake_check(handoff, args.stage1_repo) if handoff and args.stage1_repo else None
    report_handoff(handoff, intake)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
