---
status: runtime
version: 0.8
meta_model_version: 0.5
updated: 2026-11-26
---

# Mango BA AI Runtime — MVP BCREQ 0.8

Репозиторий, на который БА ссылается при работе в чате модели. Маршрут
`A-IN → A-CORE → A-BCREQ` исполняет модель по системным промптам из этого
репозитория; итог — бизнес-требование `A-BCREQ` в Markdown. Репозиторий не
привязан к среде и варианту развёртывания.

## Первый запуск

1. Откройте [быстрый старт](docs/guides/00-quick-start.md).
2. Откройте новый чат модели для новой задачи, дайте ссылку на этот
   репозиторий и вставьте пример из быстрого старта. Один чат — одна задача.
3. Получите `A-BCREQ` в диалоге.

Все инструкции: [docs/guides/README.md](docs/guides/README.md).

## Состав

| Путь | Назначение |
| --- | --- |
| `AGENTS.md` | загрузочный системный промпт; единый вход для любого клиента |
| `skills/` | 11 навыков узлов MVP — единственный источник навыков |
| `.agents/skills/<имя>/SKILL.md` | генерируемая побайтная копия `skills/<имя>.md` в открытой раскладке навыков; вручную не правится |
| `contracts/` | системные промпты-контракты `C-IN`, `C-CORE`, `C-QUEST`, `C-OUT-BCREQ`, `C-RK` |
| `taxonomy/`, `routes/` | закрытые словари и граф маршрута |
| `taxonomy/mango-products.yaml` | закрытый каталог продуктов Mango (Domain → Capability → Feature → Atomic Function); значение `atomic_function` берётся из него по id |
| `taxonomy/domain-glossary*.yaml` | словарь домена на продуктовый класс: `domain-glossary.yaml` — `contact-center`, `domain-glossary-voice-ucaas.yaml`, `domain-glossary-analytics-reporting.yaml`; пары `confusable_with` — источник отрицательных эталонов (EP-G7) |
| `taxonomy/product-profiles.yaml` | профили продуктов для сверки терминов: словари D1…D11, минимальный набор и словари профиля (И-11 спицы промптов); не путать с профилями заполненности слотов `P-*` в `taxonomy/products.yaml` |
| `templates/`, `golden/`, `evaluation/` | шаблоны, эталоны, гейты и промпт `G-mach` |
| `golden/cases*.yaml` | Golden Set на продуктовый класс: `cases.yaml` — `contact-center`, `cases-voice-ucaas.yaml`, `cases-analytics-reporting.yaml`; `G-mach` (`check_golden`) проверяет все наборы; `atomic_function` случая — функция каталога класса набора (правило PT-5) |
| `golden/prompt-regressions.yaml` | регрессионные кейсы чистоты промптов спицы PR-01…PR-04 (И-12): кейс — вход прогона, принцип — в промпте; в `G-mach` не входит |
| `docs/kb/` | база знаний (уровень `ST-5-LOCAL`) |
| `docs/guides/` | пошаговые инструкции для пользователя |

## Клиенты-агенты

Клиент, который читает `AGENTS.md` сам, получает весь контекст без настройки:
`AGENTS.md` ведёт по маршруту и открывает навык на его узле. Навыки клиент
находит в `.agents/skills/` — это копия `skills/`, а не второй источник:

- правка навыка — только в `skills/<имя>.md`, затем
  `python3 tests/build_skills_mirror.py`;
- `tests/test_skills_mirror.py` и `tests/runtime-smoke.sh` сверяют копию с
  `skills/` по sha256 и падают при расхождении;
- `tests/opencode_smoke.py` проверяет на заданной версии OpenCode, что
  `AGENTS.md` доходит до модели целиком и что модели предложены все 11
  навыков; модель не вызывается, ответ даёт локальная заглушка.

Адаптер под отдельного клиента (файл, который только указывает клиенту на
`AGENTS.md` и `.agents/skills/`, без копии содержания) добавляется решением
владельца по конкретному клиенту.

## Маршрутизация знаний

Порядок: материал задачи → корпоративная БЗ → Confluence → публичные ресурсы
Манго → внешние системы → `docs/kb` → вопрос человеку. Работу с внешними
базами знаний регламентирует сама модель: недоступный уровень пропускается с
записью причины `ACCESS_GAP: <что> — <почему>` и работу не блокирует;
содержание недоступного источника не выводится.

`docs/kb/` — копия `kb/processed` из
[`mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/kb/processed).
Навигация: [`docs/kb/MAP.json`](docs/kb/MAP.json) →
`docs/kb/maps/<документ>.toc.tsv` → `sections/NN-*.md`; карта
`docs/kb/maps/<документ>.json` — когда нужны подсказка, страницы или токены.
Порядок выбора и повторного поиска: [`docs/kb/USAGE.md`](docs/kb/USAGE.md).

## Версии и происхождение

- пакет: `0.8`; зависимость от мета-модели: `0.5`;
- исходные снимки и SHA записаны в `compilation-manifest.yaml`.
