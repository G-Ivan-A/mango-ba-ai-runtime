---
status: draft
version: 0.3
updated: 2026-08-25
ai-generated: true
type: kb-processed-guide
scope: kb/processed
related_artifacts:
  - "scripts/kb/extract.py"
  - "kb/USAGE.md"
related_issues:
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/111"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/117"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/119"
  - "https://github.com/G-Ivan-A/mango_ba_prompts/issues/320"
---

# `kb/processed/` — результаты извлечения (для агентов)

Сгенерированный, **machine-readable** слой БЗ: вывод
[`scripts/kb/extract.py`](../../scripts/kb/extract.py). Эти файлы **не правят
руками** — правят источник в `kb/sources/` и перезапускают извлечение.

> Как промпт читает этот слой (индекс → выбор раздела → загрузка одного раздела →
> цитата → сравнение токенов) — c реальными сниппетами в
> [`kb/USAGE.md`](../USAGE.md).

## Структура одного документа

```
kb/processed/<doc-slug>/
├── index.md            ← карта разделов: раздел → файл → стр. → источник → токены
├── meta.json           ← метаданные: источники/части, sha256, счётчики, токены
├── sections/
│   ├── 00-...md        ← титульная часть
│   ├── 01-...md        ← раздел = чанк (frontmatter: id, pages, source_refs)
│   └── NN-...md
└── images/
    └── NN-...-1.png    ← извлечённые растровые изображения, ссылки — внутри разделов
```

## Контракт раздела-чанка

Каждый `sections/NN-slug.md` — самодостаточный фрагмент со стабильным адресом
(путь + якорь Markdown-заголовка) и frontmatter:

```yaml
id: <doc-slug>-NN-<section-slug>   # стабильный идентификатор (будущий chunk-id для RAG)
doc_code: CC                       # короткий код документа для цитат
section: "4"                       # номер раздела в документе
pdf_section: "4"                   # номер из PDF/outline или ближайший родитель
pdf_heading: "4 Обращения"         # исходный заголовок PDF/bookmark
pages: "5"                         # сквозные страницы документа
source_part: "1"                   # часть split-документа
source_pages: "ч.1: 5"             # локальные страницы внутри PDF-части
source_refs: '[{"source_pdf":"kb/sources/.../*.pdf","part":1,"pages":"5","global_pages":"5"}]'
tokens: 378                        # реальные токены (метод — token_method)
source: kb/sources/.../*.pdf       # первичный PDF-источник раздела
status: extracted
ai-generated: true
```

Сразу под H1 раздела выводится человекочитаемая строка `Трассировка` с номером
PDF-раздела, сквозными страницами, PDF-частями и локальными страницами. Для
multi-part документов `pages` остаётся сквозной пагинацией всего руководства, а
`source_refs` хранит точный путь к части и локальный диапазон страниц.

Это соответствует pre-RAG-механике стандарта БЗ (ADR-007, правила R1–R4):
каждый раздел = файл = чанк; `index.md` = retrieval-шаг; адреса `path#anchor`
станут chunk-id без переписывания, когда появится векторный RAG.

## Каталоги

| Документ | Статус |
| --- | --- |
| [`mango-cc-manual/`](mango-cc-manual/index.md) | руководство КЦ v1.26.28.1 (issue #317) |
| [`mango-lk-manual/`](mango-lk-manual/index.md) | справочник абонента ЛК ВАТС v1.23 (issue #317) |
| [`mtalker/`](mtalker/index.md) | комплект из 5 документов Mango Talker (issues #121, #317) |
| [`vpbx-api/`](vpbx-api/index.md) | API ВАТС MANGO OFFICE v1.9 (issue #310) |
| [`rolevaya-model-vats/`](rolevaya-model-vats/index.md) | роли и права доступа ВАТС v1.26.08 (issue #310) |
| [`lk-vats-sso/`](lk-vats-sso/index.md) | аутентификация и авторизация в рамках SSO (issue #310) |
| [`cov-robot-fil/`](cov-robot-fil/index.md) | голосовой робот и фильтр вызовов v1.26.28 (issue #317) |
| [`mdialogi-api/`](mdialogi-api/index.md) | API MDialogi от 10.06.2026 (issue #317) |
| [`integration-1c/`](integration-1c/index.md) | прямая интеграция ВАТС с «1С: Управление торговлей» от 22.12.2025 (issues #310, #320) |
| [`integration-amocrm/`](integration-amocrm/index.md) | интеграция ВАТС и amoCRM от 25.08.2025 (issue #320) |
| [`integration-bitrix24/`](integration-bitrix24/index.md) | интеграция ВАТС и Битрикс24 от 03.03.2026 (issue #320) |
| [`integration-bpmsoft/`](integration-bpmsoft/index.md) | интеграция ВАТС и BPMSoft от 22.06.2026 (issue #320) |
| [`sip-trunk/`](sip-trunk/index.md) | SIP TRUNK, руководство пользователя v1.23.43 (issue #320) |
| [`quality-management/`](quality-management/index.md) | контроль качества v1.26.18 (issue #320) |
| [`speech-analytics/`](speech-analytics/index.md) | комплект из 4 руководств «Речевая аналитика» v1.26.15–1.26.18 (issue #320) |

Синтетическая фикстура `contact-center-manual-sample/` удалена в issue #310:
БЗ содержит только извлечения реальных документов. Стенд конвейера
(`make kb-sample kb-extract`) пишет результат в некоммитируемый `.kb-sample/`.

## Источники

- Конвейер и оценка качества: [`docs/kb-experiment-report.md`](../../docs/kb-experiment-report.md)
- Пополнение БЗ: [`kb/sources/README.md`](../sources/README.md)
