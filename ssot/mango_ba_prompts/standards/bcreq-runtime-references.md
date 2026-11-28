---
status: draft
version: 0.5
updated: 2026-11-05
temperature: 0.1
ai-generated: true
type: standard
scope: bcreq-flow
runtime_repo: "https://github.com/G-Ivan-A/mango-ba-ai-runtime"
runtime_sha: "68ad8fcffd47439fc3051852d9a2fbbe23815855"
related_artifacts:
  - "docs/rfc/2026-11-bcreq-flow-processes-prompts.md"
  - "standards/bcreq-flow-glossary.md"
  - "docs/ba-processes/bcreq-manual-process.md"
  - "docs/contracts/kb-citations.md"
  - "pr-ops/backlog-ba-model.md"
  - "docs/rfc/2026-11-runtime-product-catalog-golden-set.md"
related_issues:
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/427"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/430"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/434"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/442"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/444"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/450"
---

# Справочники runtime для промптов потока BCREQ

> Носитель — [RFC #427](../docs/rfc/2026-11-bcreq-flow-processes-prompts.md#8-исключения-ссылки-промптов-на-mango-ba-ai-runtime)
> (`accepted`), решения DEC-427-09 и DEC-427-10, задачи
> [BL-154](../pr-ops/backlog-ba-model.md#bl-154-справочники-runtime-перечень-требования-закреплённый-срез)
> и [BL-155](../pr-ops/backlog-ba-model.md#bl-155-заглушки-недостающих-справочников-runtime).
> Отдельный файл — по
> [поправке 0.4 RFC](../docs/rfc/2026-11-bcreq-flow-processes-prompts.md#поправка-04-гейт-и-его-типы-issue-430)
> (issue [#430](https://github.com/G-Ivan-A/mango_ba_prompts/issues/430)):
> [базовый стандарт](bcreq-prompt-base-standard.md#34-источники-цитаты-и-справочники-runtime)
> BL-151 (решение Р-14, issue #432, PR #435) подключает этот реестр
> ссылкой, а не копией (правила БС-18…БС-22). Режим — «по тесту» до прогонов на новых задачах.
> Термины — [словарь потока](bcreq-flow-glossary.md).

Промпт ручного потока самодостаточен. Исключение — справочники
`mango-ba-ai-runtime` из раздела 2: они больше бюджета вставки или
меняются чаще промпта, нужны модели как факт или образец, а не как
правило, и имеют стабильный путь и версию (критерии раздела 8.1 RFC).
Правила исполнения в справочник не выносятся.

## 1. Закреплённый срез

| Поле | Значение |
| --- | --- |
| Репозиторий | [`G-Ivan-A/mango-ba-ai-runtime`](https://github.com/G-Ivan-A/mango-ba-ai-runtime) |
| SHA | `68ad8fcffd47439fc3051852d9a2fbbe23815855` |
| Дата коммита | 2026-11-05 (слияние [runtime PR #23](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/23): РТ-7, оглавления `sections_toc`; прежний срез `f31dcde3` — слияние [runtime PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21): РТ-6, РТ-4, РТ-3 и норма PT-5) |
| Проверено | 2026-11-05, клон на SHA: все пути раздела 2 существуют, `sections_toc` есть у документов `MAP.json`; сверка — `experiments/issue_450/runtime-pin-check.py`. С прежнего среза `f31dcde3` изменены только индекс `docs/kb/` (`MAP.json`, 25 новых `maps/*.toc.tsv`, `USAGE.md`, `build_map.py`), `README.md` и тест навигации; каталог, golden set и глоссарии не менялись — лог `experiments/issue_450/runtime-pin-check.log` |

Это **единственная точка обновления SHA** (ТС-5). Промпты набора берут
SHA отсюда при сборке; другой SHA в ссылке на runtime — ошибка
валидатора `scripts/validate_issue_430_runtime_refs.py`.

Как обновить срез:

1. Выбрать коммит runtime, проверить пути раздела 2 и требования ТС-2,
   ТС-3 на нём.
2. Заменить SHA в таблице выше, во frontmatter (`runtime_sha`) и во всех
   ссылках раздела 2 одной правкой.
3. Пересобрать промпты набора; запись в `CHANGELOG.md`.

## 2. Перечень

Ссылка дана на закреплённый SHA. «Шаги» — шаги потока Ш- по
[процессу BCREQ, часть 0](../docs/ba-processes/bcreq-manual-process.md#0-поток-bcreq-процессы-шаги-гейты)
и разделу 9.2 RFC.

| № | Справочник | Ссылка на срезе | Есть в runtime | Решение | Шаги |
| --- | --- | --- | --- | --- | --- |
| И-1 | База знаний продуктов | [`docs/kb/MAP.json`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/docs/kb/MAP.json) → `docs/kb/maps/<id>.toc.tsv` (поле `sections_toc`, читается за одно обращение) → `docs/kb/<slug>/sections/NN-*.md`; `docs/kb/maps/<id>.json` — только когда нужны `hint`, страницы или токены; путь поиска — [`docs/kb/USAGE.md`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/docs/kb/USAGE.md) | Да: 25 документов в `MAP.json`, 18 каталогов документов | **Ссылка обязательна** | Ш-1, Ш-2, Ш-3, Ш-6, Ш-7 |
| И-2 | Таксономия продуктов | Значения: [`taxonomy/mango-products.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/taxonomy/mango-products.yaml); форма уровней и классы: [`taxonomy/products.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/taxonomy/products.yaml) | Да: закрытый каталог (`closed: true`), 353 узла — Domain 7, Capability 43, Feature 151, Atomic Function 152; у каждого узла классы runtime; копия каталога спицы (раздел 2.1) | **Ссылка**; `atomic_function` — только id из каталога (BL-163, [issue #442](https://github.com/G-Ivan-A/mango_ba_prompts/issues/442)); как читать — раздел 2.2 (М-4) | Ш-2 |
| И-3 | Шаблон документа BCREQ | [`templates/bcreq-skeleton.md`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/templates/bcreq-skeleton.md) | Да: 14 слотов, формы F-SHORT, F-APPROVAL, F-CLASSIC, F-NARRATIVE | Ссылка | Ш-0, Ш-В, Ш-Р |
| И-4 | Примеры разделов (ФТ, UC, US, НФТ, ОРР) | — | Нет (`A-FR`, `A-UC`, `A-US` вне среза) | Заглушка З-2 | Ш-3, Ш-4, Ш-5, Ш-8, Ш-С |
| И-5 | Golden set по классу продуктовой таксономии | `contact-center`: [`golden/cases.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/golden/cases.yaml); `voice-ucaas`: [`golden/cases-voice-ucaas.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/golden/cases-voice-ucaas.yaml); `analytics-reporting`: [`golden/cases-analytics-reporting.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/golden/cases-analytics-reporting.yaml) | Да: три класса, синтетические кейсы — `contact-center` 2 положительных и 5 отрицательных, `voice-ucaas` 2 и 4, `analytics-reporting` 2 и 3; `atomic_function` каждого — функция каталога И-2 класса набора; все `structural_only: true`, `confirmed_by: none` — содержательную проверку человеком ведёт BL-165 | Ссылка; кейс — образец формы, а не подтверждённый эталон | Ш-В |
| И-6 | Доменный глоссарий | `contact-center`: [`taxonomy/domain-glossary.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/taxonomy/domain-glossary.yaml); `voice-ucaas`: [`taxonomy/domain-glossary-voice-ucaas.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/taxonomy/domain-glossary-voice-ucaas.yaml); `analytics-reporting`: [`taxonomy/domain-glossary-analytics-reporting.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/taxonomy/domain-glossary-analytics-reporting.yaml) | Да: три класса — 8, 6 и 4 термина, у каждого пары `confusable_with`; термины `voice-ucaas` и `analytics-reporting` ссылаются на узлы каталога И-2 | Ссылка по классу задачи | Ш-1 |
| И-7 | Порядок источников и уровни доверия | [`taxonomy/source-tiers.yaml`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/taxonomy/source-tiers.yaml) | Да | Ссылка в базовом стандарте (BL-151) | все шаги |
| И-8 | Чек-лист гейта G-human | [`evaluation/g-human-checklist.md`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/68ad8fcffd47439fc3051852d9a2fbbe23815855/evaluation/g-human-checklist.md) | Да | Ссылка | Ш-В |
| И-9 | Уроки прогонов | — (здесь: `standards/bcreq-lessons/lessons.json`) | — | **Не исключение**: уроки — правила, входят в промпт (ADR-017, DEC-411-01) | — |
| И-10 | Мета-стандарты разделов | — (здесь: `standards/bcreq-sections/`) | — | **Не исключение**: правила входят в промпт через профиль GENERATE | — |
| И-11 | Профили продуктов (словари и параметры профиля продукта для набора словарей Ш-2 и таблицы Ш-0) | — (`taxonomy/product-profiles.yaml`) | Влит в runtime, вне закреплённого среза | Заглушка З-5 | Ш-0, Ш-2 |
| И-12 | Регрессионные кейсы чистоты промптов (кейсы, вынесенные из текста промптов как принцип) | — (`golden/prompt-regressions.yaml`) | Влит в runtime, вне закреплённого среза | Не читается промптом: кейсы проверяют исполнение принципа при прогоне (реестр кейсов CR-01…CR-04, `standards/bcreq-prompt-purity.json`) | Ш-0…Ш-2, A-IN |

И-8 — чек-лист **ключевого** гейта: runtime сам разводит человеческий и
машинный гейт («Всё, что попало в чек-лист `G-mach`, здесь не
перепроверяется», `evaluation/g-human-checklist.md`). Типы гейтов —
[словарь потока, раздел 3](bcreq-flow-glossary.md#3-гейт-определение-типы-ключевые-гейты).

### 2.1. Каталог продуктов: копия и сверка со спицей

ССОТ значений каталога — спица, [`docs/taxonomy/products.json`](../docs/taxonomy/products.json)
([RFC-RT-001, раздел 3](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md#3-ссот-и-разделение-ответственности)).
В runtime — копия: `taxonomy/mango-products.yaml` с полями `source_commit` и
`source_sha256` (манифест runtime, раздел `copied`). Промпт читает копию по
SHA раздела 1, не спицу и не ветку (ТС-5, БС-19).

Сверка на срезе раздела 1 (2026-11-04, после РТ-6):

| Что сверяется | Копия runtime | Спица | Итог |
| --- | --- | --- | --- |
| Источник копии | `source_commit: e3597fd7`, `source_sha256: 2ca6fafa…` | sha256 `docs/taxonomy/products.json` на `e3597fd7` (и на `main`) — `2ca6fafa…` | Совпадает: копия без потерь |
| id, уровень, родители 353 узлов | 353 узла | 353 узла (`main`) | Совпадают все |
| `lifecycle` 74 узлов с портала, статус каталога | `accepted`, `catalog_status: accepted` | `accepted`, `status: accepted` (Р-17, [PR #440](https://github.com/G-Ivan-A/mango_ba_prompts/pull/440)) | Совпадают: расхождение среза `2db0ef5` снято РТ-6 ([runtime PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21)) |

Правило чтения `added-for-review` как `accepted` (реестр 0.3) снято вместе
с расхождением: в копии таких узлов нет.

Правило сверки (обязательно перед каждым обновлением SHA): id, уровни и
родители копии совпадают с текущим каталогом спицы; `source_sha256` равен
sha256 каталога спицы на `source_commit`; любое расхождение — повод не
обновлять срез. Проверка —
`scripts/validate_issue_430_runtime_refs.py` при `RUNTIME_CLONE`.

### 2.2. Как промпт шага читает каталог (М-4)

Звено М-4 механизма снятия заглушки таксономии
([RFC-RT-001, раздел 4](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md#4-механизм-снятия-заглушки-таксономии-критично)).
Текст ниже сборщик `scripts/build_bcreq_step_prompts.py` переносит дословно
в промпт каждого шага, у которого в разделе 2 есть И-2 (сейчас Ш-2).
`<SHA реестра>` подставляется из раздела 1. Отличие от образца RFC — шаг 5:
оговорка про `added-for-review` снята, потому что РТ-6 обновила копию
(раздел 2.1).

```text
Таксономия продуктов: https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/<SHA реестра>/taxonomy/mango-products.yaml
1. Возьми продуктовый класс задачи из входа БА (contact-center,
   voice-ucaas или analytics-reporting). Класс не выводится из текста.
2. Отбери узлы, у которых в `classes` есть этот класс.
3. Пройди цепочку: domain → capability → feature → function по полю
   `parents`. Для каждого затронутого продукта выбери id узла
   `level: function` и приведи цепочку целиком.
4. Если подходящей функции нет или подходят две, не выбирай сам: выведи
   «Продуктовая принадлежность: [ТРЕБУЕТСЯ УТОЧНЕНИЕ]», подтверждённые
   уровни и вопрос БА.
5. Узлы с `lifecycle: retained` и `lifecycle: accepted` равноправны:
   оба утверждены владельцем (Р-17).
6. Каталог не утверждает доступность функции клиенту
   (`availability: not-established-by-taxonomy`): доступность — только
   из источника задачи или БЗ.
```

## 3. Требования к справочникам

| № | Требование | Проверка | Как проверено сейчас |
| --- | --- | --- | --- |
| ТС-1 | Ссылка закреплена по коммиту: `https://github.com/G-Ivan-A/mango-ba-ai-runtime/blob/<SHA>/…`, `tree/<SHA>/…` или raw-URL с `<SHA>`; не `main` | Валидатор: в ссылке на runtime 40-символьный SHA | `validate_issue_430_runtime_refs.py`: все ссылки на runtime в области ТС-5, ссылок на `main` нет (долг раздела 7 закрыт) |
| ТС-2 | Путь стабилен и описан в `USAGE.md` или `README.md` runtime | Ссылка открывается на закреплённом SHA | Клон на SHA, 2026-11-04 (раздел 1) |
| ТС-3 | У справочника есть версия (`version` в YAML или frontmatter) и источник происхождения | Поле есть | `products.yaml` — `"1.1"`, `mango-products.yaml`, `domain-glossary.yaml` — `"1.0"`, `cases.yaml` — `"1.1"`, `cases-voice-ucaas.yaml`, `cases-analytics-reporting.yaml` — `"0.2"`, `domain-glossary-voice-ucaas.yaml`, `domain-glossary-analytics-reporting.yaml` — `"0.1"`; источник каталога — `source_commit`, `source_sha256`; `source-tiers.yaml` — `"0.5"`; `g-human-checklist.md` — `version: 1.0`; `MAP.json` — `schema_version` |
| ТС-4 | Справочник содержит факты и образцы, не правила исполнения | Ревью при включении в перечень | И-9, И-10 исключены по этому требованию |
| ТС-5 | Одна точка обновления SHA — раздел 1 этого файла | Один SHA во всех промптах набора | Валидатор: любой SHA runtime в репозитории вне истории совпадает с разделом 1 |
| ТС-6 | Если модель не открывает ссылки — БА прикладывает файл; промпт говорит это явно | Строка в промпте | Текст строки — раздел 5; вставка — сборщик BL-156 в черновики `prompts/drafts/` |
| ТС-7 | Цитата из справочника — с локатором (документ, раздел) по [контракту цитат KB](../docs/contracts/kb-citations.md) | Проверка Ш-В | Правило входит в базовый стандарт BL-151 |

## 4. Заглушки

Где справочника нет или он неполон, промпт шага содержит блок (раздел
8.4 RFC; номер задачи BL-155 из блока RFC в промпт не переносится — стандарт
чистоты промптов, issue #495):

```text
[СПРАВОЧНИК ОТСУТСТВУЕТ: <имя>]
Действуй без образца: не придумывай значения, которых нет во входе;
пометь место [ТРЕБУЕТСЯ УТОЧНЕНИЕ] и добавь вопрос в 8.4.
```

Заглушка — известный пробел в реестре прогона. При закреплении среза
с новым справочником строка ниже снимается, справочник получает ссылку
в разделе 2, SHA обновляется по разделу 1.

| № | Справочник | Условие заглушки | Шаги | Строка `<имя>` | Задача для runtime |
| --- | --- | --- | --- | --- | --- |
| З-2 | И-4 Примеры разделов | всегда | Ш-3, Ш-4, Ш-5, Ш-8, Ш-С | `И-4 примеры разделов ФТ, НФТ, UC, US, ОРР` | РТ-2 |
| З-5 | И-11 Профили продуктов | пока профиль недоступен в закреплённом срезе runtime | Ш-0, Ш-2 | `И-11 профили продуктов` | РТ-8 |

Шаг выпуска Ш-Р сам по себе — заглушка промпта (пилот, раздел 9.2 RFC),
а не заглушка справочника: ему нужен только И-3. Промпт Ш-Р — в BL-156.

Снятые заглушки. Id не переиспользуется: на него ссылаются карточки
бэклога и история прогонов.

| № | Справочник | Строка `<имя>` | Снята | Почему |
| --- | --- | --- | --- | --- |
| З-1 | И-2 Таксономия продуктов | `И-2 таксономия продуктов: уровни ниже класса не заполнены` | 2026-11-04, BL-163 ([issue #442](https://github.com/G-Ivan-A/mango_ba_prompts/issues/442)) | РТ-1 слита: каталог `taxonomy/mango-products.yaml` на срезе раздела 1, И-2 — «Да» |
| З-3 | И-5 Golden set | `И-5 golden set класса <класс>` | 2026-11-04, BL-156а ([issue #444](https://github.com/G-Ivan-A/mango_ba_prompts/issues/444)) | РТ-3 слита ([runtime PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21)): наборы `voice-ucaas` и `analytics-reporting` на срезе раздела 1, И-5 — «Да» |
| З-4 | И-6 Доменный глоссарий | `И-6 доменный глоссарий класса <класс>` | 2026-11-04, BL-156а ([issue #444](https://github.com/G-Ivan-A/mango_ba_prompts/issues/444)) | РТ-4 слита ([runtime PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21)): глоссарии `voice-ucaas` и `analytics-reporting` на срезе раздела 1, И-6 — «Да» |

## 5. Строка для промпта (ТС-6)

```text
Справочники runtime закреплены на коммите <SHA из раздела 1>. Если ты не
можешь открыть ссылку, скажи об этом и попроси БА приложить файл; не
восстанавливай содержимое справочника по памяти.
```

Основание: `docs/guides/00-quick-start.md` runtime — «Если модель не
может открыть ссылку, вставьте или приложите `AGENTS.md`, …».

## 6. Задачи для репозитория runtime

Создаёт владелец в
[`mango-ba-ai-runtime`](https://github.com/G-Ivan-A/mango-ba-ai-runtime/issues):
у исполнителя этой спицы нет решения о бэклоге runtime (A-08 RFC #427).
Ссылка на задачу runtime вписывается в столбец «Задача runtime» после
создания.

Готовые к копированию тела задач РТ-1 и РТ-3, задача Хаба ХАБ-1 и
механизм снятия заглушки З-1 (снята, BL-163) — в
[RFC-RT-001](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md)
(issue [#434](https://github.com/G-Ivan-A/mango_ba_prompts/issues/434)).
Строки РТ-1 и РТ-3 ниже расширены по нему: каталог нужен всем трём
классам, а не только `contact-center`, и живёт в отдельном файле
`taxonomy/mango-products.yaml`, а не в словаре формы `taxonomy/products.yaml`.

| № | Что нужно в runtime | Снимает заглушку | Приоритет | Почему | Задача runtime |
| --- | --- | --- | --- | --- | --- |
| РТ-1 | Закрытый каталог продуктов `taxonomy/mango-products.yaml`: все уровни Domain → Capability → Feature → Atomic Function по всей линейке (каталог спицы 2026-10-28.1, 353 узла) с классами runtime у каждого узла; проверка smoke без каталога падает. Норма привязки `c-in` — задача Хаба ХАБ-1 ([RFC-RT-001, разделы 5–6](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md#5-рт-1--тело-задачи-для-mango-ba-ai-runtime-копировать-целиком)) | З-1 | P1 | `c-in` требует `atomic_function`, а каталога функций нет — модель придумывает функцию или оставляет пусто | [runtime #15](https://github.com/G-Ivan-A/mango-ba-ai-runtime/issues/15), [PR #16](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/16) — слита 2026-11-04, `2db0ef51`; норма `c-in` — Хаб [#719](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/719), [PR #720](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/720) — слита; компиляция в runtime: [PR #17](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/17) закрыт без слияния, недостающая логика (норма PT-5, `check_taxonomies` 6–11, `check_golden` 2–8) перенесена в [PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21) — слита 2026-11-04, `f31dcde3` |
| РТ-2 | Примеры разделов ФТ, НФТ, UC, US, ОРР (по одному эталону на раздел, с источником происхождения) | З-2 | P1 | Образцы улучшают форму вывода шагов Ш-3…Ш-8; сейчас `A-FR`, `A-UC`, `A-US` вне среза | — (создаёт владелец) |
| РТ-3 | Golden set для `voice-ucaas` и `analytics-reporting` (`golden/cases-<класс>.yaml`); у каждого случая `product_class` и `atomic_function` из каталога РТ-1; подтверждение человеком кейсов `contact-center` (`structural_only: false`) ([RFC-RT-001, раздел 7](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md#7-рт-3--тело-задачи-для-mango-ba-ai-runtime-копировать-целиком)) | З-3 | P1 | Issue #427: «голден сет по каждому классу проуктовой таксономии» | [runtime #20](https://github.com/G-Ivan-A/mango-ba-ai-runtime/issues/20), [PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21) — слита 2026-11-04, `f31dcde3`; подтверждение человеком кейсов (`confirmed_by: none` у всех трёх классов) — BL-165 спицы |
| РТ-4 | Доменный глоссарий для `voice-ucaas` и `analytics-reporting` | З-4 | P2 | Термины продукта нужны глоссарию раздела 1 BCREQ (К-14) | [runtime #20](https://github.com/G-Ivan-A/mango-ba-ai-runtime/issues/20), [PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21) — слита 2026-11-04, `f31dcde3` |
| РТ-6 | Обновить копию каталога `taxonomy/mango-products.yaml` до текущего коммита каталога спицы (после Р-17 — `e3597fd74da9c4f631ca46697c643462e2cf0b85`): `lifecycle: accepted` у 74 узлов, `catalog_status: accepted`, новые `source_commit` и `source_sha256`, запись `copied` в манифесте. Тело задачи — [RFC-RT-001, поправка 0.3](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md#123-рт-6--тело-задачи-для-mango-ba-ai-runtime-копировать-целиком) | расхождение раздела 2.1 | P2 | Копия старше решения Р-17: промпт читает `added-for-review` у принятых узлов; id и связи совпадают, поэтому не блокирует И-2 | [runtime #20](https://github.com/G-Ivan-A/mango-ba-ai-runtime/issues/20), [PR #21](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/21) — слита 2026-11-04, `f31dcde3`; расхождение раздела 2.1 снято |
| РТ-7 | Лёгкие оглавления `maps/<id>.toc.tsv` и поле `sections_toc` в `MAP.json`, порядок чтения в `USAGE.md` | дефект Р-1 RUN-0083: большая карта не читается за одно обращение | P1 | Шаги с И-1 не видели большую часть разделов крупных документов | [PR #23](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/23) — слита 2026-11-05, `68ad8fcf`; маршрут промптов переведён, issue [#450](https://github.com/G-Ivan-A/mango_ba_prompts/issues/450) |
| РТ-8 | Справочник профилей продуктов `taxonomy/product-profiles.yaml`: профили D1…D11 с продуктами и словарями — факты, вынесенные из промптов Ш-0 и Ш-2 (issue #495, проблема B) | З-5 | P1 | Промпт держит принцип «возьми словари профилей задействованных продуктов», значения профилей — справочник runtime | [runtime PR #28](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/28) слит в `fe623c6b`; закрепление SHA — BL-242 |
| РТ-9 | Регрессионные кейсы `golden/prompt-regressions.yaml` (PR-01 внешняя CRM, PR-02 новый интеграционный компонент, PR-03 аналогия с внешней системой, PR-04 функция продукта и доступность в интеграции или тарифе) и тест формы | — (И-12) | P2 | Кейсы ушли из текста промптов; без набора регрессия принципа не проверяется | [runtime PR #28](https://github.com/G-Ivan-A/mango-ba-ai-runtime/pull/28) слит в `fe623c6b`; закрепление SHA — BL-242 |

## 7. Долг закрыт: ссылки на `main` в промптах v0.1

До 2026-11-04 все 14 файлов `prompts/bcreq-*.md` ссылались на runtime
через `blob/main` — нарушение ТС-1. Ссылок было три:

- `mango-ba-ai-runtime/blob/main/docs/kb/README.md`;
- `mango-ba-ai-runtime/blob/main/docs/kb/MAP.json`;
- `mango-ba-ai-runtime/blob/main/taxonomy/products.yaml`.

Правка `prompts/` допускается только «не хуже базовой линии golden set»
(DEC-427-11), поэтому долг держался до замера. BL-156а
([issue #444](https://github.com/G-Ivan-A/mango_ba_prompts/issues/444))
закрепила ссылки на срез раздела 1 вместе с подстановками типизации
`experiments/issue_438/prompt-typing.json` и измерила результат прогоном
RUN-0081 против RUN-0079. Валидатор больше не держит список долга:
ссылка на runtime через `main` в области ТС-5 — ошибка.

## Related Artifacts

- [RFC #427, раздел 8](../docs/rfc/2026-11-bcreq-flow-processes-prompts.md#8-исключения-ссылки-промптов-на-mango-ba-ai-runtime) — исключения, требования, заглушка
- [BL-114](../pr-ops/backlog-ba-model.md#bl-114-самодостаточность-промптов-и-справочники-в-runtime) — правило самодостаточности; перечень и требования — здесь
- [Словарь потока BCREQ](bcreq-flow-glossary.md) — термины «справочник runtime», «заглушка», типы гейтов
- [Процесс BCREQ, часть 0](../docs/ba-processes/bcreq-manual-process.md#0-поток-bcreq-процессы-шаги-гейты) — шаги потока
- [Контракт цитат KB](../docs/contracts/kb-citations.md) — ТС-7
- [RFC-RT-001](../docs/rfc/2026-11-runtime-product-catalog-golden-set.md) — тела задач РТ-1, РТ-3, ХАБ-1, РТ-6, механизм снятия З-1 (исполнен BL-163, issue #442) и снятие З-3, З-4 (BL-156а, поправка 0.4, issue #444)
