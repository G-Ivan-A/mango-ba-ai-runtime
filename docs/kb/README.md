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
| [`mango-cc-manual/`](mango-cc-manual/index.md) | руководство КЦ v1.26.42, 2 PDF-части, иллюстрации с текстовыми описаниями (issue #7) |
| [`mango-lk-manual/`](mango-lk-manual/index.md) | справочник абонента ЛК ВАТС v1.25, редакция v 26.42 от 07.10.2026; иллюстрации с текстовыми описаниями ([`IMAGES.md`](mango-lk-manual/IMAGES.md)); извлекается [`tools/extract_lk_manual.py`](tools/extract_lk_manual.py) (issue #8) |
| [`mtalker/`](mtalker/index.md) | комплект из 5 документов Mango Talker (issues #121, #317; описания иллюстраций Android и Windows/macOS — issue #11) |
| [`vpbx-api/`](vpbx-api/index.md) | API ВАТС MANGO OFFICE v1.9 (issue #310) |
| [`rolevaya-model-vats/`](rolevaya-model-vats/index.md) | роли и права доступа ВАТС v1.26.08 (issue #310) (issue #12: иллюстрации описаны текстом, декоративные удалены, PNG оптимизированы — [`IMAGES.md`](rolevaya-model-vats/IMAGES.md)) |
| [`lk-vats-sso/`](lk-vats-sso/index.md) | аутентификация и авторизация в рамках SSO (issue #310) |
| [`cov-robot-fil/`](cov-robot-fil/index.md) | голосовой робот и фильтр вызовов v1.26.28 (issue #317; описания иллюстраций — issue #11) |
| [`mdialogi-api/`](mdialogi-api/index.md) | API MDialogi от 10.06.2026 (issue #317) |
| [`integration-1c/`](integration-1c/index.md) | прямая интеграция ВАТС с «1С: Управление торговлей» от 22.12.2025 (issues #310, #320) (issue #12: иллюстрации описаны текстом, декоративные удалены, PNG оптимизированы — [`IMAGES.md`](integration-1c/IMAGES.md)) |
| [`integration-amocrm/`](integration-amocrm/index.md) | интеграция ВАТС и amoCRM от 25.08.2025 (issue #320) (issue #12: иллюстрации описаны текстом, декоративные удалены, PNG оптимизированы — [`IMAGES.md`](integration-amocrm/IMAGES.md)) |
| [`integration-bitrix24/`](integration-bitrix24/index.md) | интеграция ВАТС и Битрикс24 от 03.03.2026 (issue #320) (issue #12: иллюстрации описаны текстом, декоративные удалены, PNG оптимизированы — [`IMAGES.md`](integration-bitrix24/IMAGES.md)) |
| [`integration-bpmsoft/`](integration-bpmsoft/index.md) | интеграция ВАТС и BPMSoft от 22.06.2026 (issue #320) (issue #12: иллюстрации описаны текстом, декоративные удалены, PNG оптимизированы — [`IMAGES.md`](integration-bpmsoft/IMAGES.md)) |
| [`sip-trunk/`](sip-trunk/index.md) | SIP TRUNK, руководство пользователя v1.23.43 (issue #320) (issue #12: иллюстрации описаны текстом, декоративные удалены, PNG оптимизированы — [`IMAGES.md`](sip-trunk/IMAGES.md)) |
| [`quality-management/`](quality-management/index.md) | контроль качества v1.26.18 (issue #320; описания иллюстраций — issue #11) |
| [`speech-analytics/`](speech-analytics/index.md) | комплект из 4 руководств «Речевая аналитика» v1.26.15–1.26.42; «Руководство пользователя» обновлено до v1.26.42 с описаниями иллюстраций (issues #320, #11) |
| [`api-server-client/`](api-server-client/index.md) | описание API «Сервер-клиент», версия от 18.09.2024; извлекается [`tools/extract_kb_doc.py`](tools/extract_kb_doc.py), иллюстрации описаны ([`IMAGES.md`](api-server-client/IMAGES.md)) (issue #12) |
| [`integration-ident/`](integration-ident/index.md) | интеграция ВАТС и IDENT от 14.01.2025; [`tools/extract_kb_doc.py`](tools/extract_kb_doc.py), [`IMAGES.md`](integration-ident/IMAGES.md) (issue #12) |
| [`wallboard/`](wallboard/index.md) | программа для ЭВМ «Wallboard Mango Office» v7.22.25; [`tools/extract_kb_doc.py`](tools/extract_kb_doc.py), [`IMAGES.md`](wallboard/IMAGES.md) (issue #12) |

Синтетическая фикстура `contact-center-manual-sample/` удалена в issue #310:
БЗ содержит только извлечения реальных документов. Стенд конвейера
(`make kb-sample kb-extract`) пишет результат в некоммитируемый `.kb-sample/`.

## Источники

- Конвейер и оценка качества: [`docs/kb-experiment-report.md`](../../docs/kb-experiment-report.md)
- Пополнение БЗ: [`kb/sources/README.md`](../sources/README.md)
