---
product_taxonomy_ref: taxonomy/products.yaml#classes
product_ids: [voice-ucaas]
type: kb-source-index
doc_code: INTIDENT
doc_title: "Интеграция Виртуальной АТС и системы IDENT. Инструкция по настройке"
doc_version: "14.01.2025"
status: extracted
ai-generated: true
source_document: "Mango_office_integration_IDENT.pdf"
extraction_date: "2026-11-01"
model_used: "PyMuPDF 1.28.2 + pdfplumber 0.11.10 + tesseract OCR (rus+eng)"
confidence_level: "high"
pages_covered: "1-9"
---

# Интеграция Виртуальной АТС и системы IDENT. Инструкция по настройке — индекс БЗ (карта разделов)

> Источник: `kb/sources/integration-ident/Mango_office_integration_IDENT.pdf` (версия документа 14.01.2025, 9 с.). Исходный PDF в репозитории
> не хранится. Токены: tiktoken:cl100k_base. Это **карта поиска** для агента (ADR-007 R2): найди
> раздел по колонке «Когда обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия
> **high**. Отбор и описание иллюстраций: [`IMAGES.md`](IMAGES.md).

## Как цитировать

`[INTIDENT, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `docs/kb/integration-ident/sections/<file>#<якорь>` (ADR-007 R3).

## Иллюстрации

Каждая содержательная иллюстрация в разделе сопровождается блоком
`> **Описание иллюстрации INTIDENT-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста
руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.
OCR-текст — вспомогательный: факты цитируются по тексту руководства.

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-2 | ч.1 с.1-2 | 230 | Интеграция Виртуальной АТС и системы IDENT |
| 1 | Обзор | [sections/01-obzor.md](sections/01-obzor.md) | 3-4 | ч.1 с.3-4 | 1174 | Данная инструкция предназначена для ознакомления пользователей с порядком самостоятельной  |
| 2 | Как настроить интеграцию | [sections/02-kak-nastroit-integraciyu.md](sections/02-kak-nastroit-integraciyu.md) | 5 | ч.1 с.5 | 0 | — |
| 2 | Порядок действий | [sections/03-poryadok-deystviy.md](sections/03-poryadok-deystviy.md) | 5 | ч.1 с.5 | 443 | Чтобы настроить интеграцию, вам потребуется: |
| — | Шаг 1. Подключение Виртуальной АТС MANGO OFFICE | [sections/04-shag-1-podklyuchenie-virtualnoy-ats-mang.md](sections/04-shag-1-podklyuchenie-virtualnoy-ats-mang.md) | 5 | ч.1 с.5 | 91 | Сначала подключите ту или иную версию Виртуальной АТС MANGO OFFICE, если у вас ее еще нет. |
| — | Шаг 2. Установка софтфона Mango Talker | [sections/05-shag-2-ustanovka-softfona-mango-talker.md](sections/05-shag-2-ustanovka-softfona-mango-talker.md) | 5-6 | ч.1 с.5-6 | 323 | Виртуальная АТС позволяет установить телефонную связь между абонентами. Ваш IDENT позволяе |
| — | Шаг 3. Подключение виджета в Личном кабинете Виртуальной АТС | [sections/06-shag-3-podklyuchenie-vidzheta-v-lichnom.md](sections/06-shag-3-podklyuchenie-vidzheta-v-lichnom.md) | 6-7 | ч.1 с.6-7 | 1706 | Для подключения интеграции с IDENT вам необходимо: |
| — | Шаг 4. Как обратиться в службу поддержки IDENT | [sections/07-shag-4-kak-obratitsya-v-sluzhbu-podderzh.md](sections/07-shag-4-kak-obratitsya-v-sluzhbu-podderzh.md) | 8 | ч.1 с.8 | 160 | После того, как вы подключили виджет интеграции, свяжитесь со службой поддержки пользовате |
| 3 | Как отключить виджет интеграции | [sections/08-kak-otklyuchit-vidzhet-integracii.md](sections/08-kak-otklyuchit-vidzhet-integracii.md) | 8-9 | ч.1 с.8-9 | 1187 | Для отключения интеграции с IDENT вам необходимо: |
