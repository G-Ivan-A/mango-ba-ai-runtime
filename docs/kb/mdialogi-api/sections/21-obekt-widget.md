---
id: mdialogi-api-21-obekt-widget
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "2.4.1"
pdf_section: "2.4.1"
title: "Объект Widget"
pdf_heading: "2.4.1 Объект Widget"
pages: "18-19"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 18-19"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"18-19","global_pages":"18-19"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 379
status: extracted
ai-generated: true
---
# 2.4.1. Объект Widget

> Трассировка: PDF §2.4.1 · сквозные стр. 18-19 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.18-19.

Объект Widget описывает виджет, настроенный в системе Манго Диалоги.

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
|  |  |  |  |
| widget_id | Integer | Да | Идентификатор |
|  |  |  | виджета |
|  |  |  |  |
| name | String | Да | Наименование виджета |
|  |  |  |  |
| enabled | Boolean | Да | Статус активности |
|  |  |  | виджета: true – включен; |
|  |  |  |  |
|  |  |  | false – выключен |
| channels | Array | Да | Список каналов, |
|  |  |  | подключенных к |
|  |  |  |  |
|  |  |  | виджету (массив |
|  |  |  | объектов Channel, см. |
|  |  |  | раздел «Объект |
|  |  |  | Channel») |

Манго Диалоги. Справочник по API | Версия от 10.06.2026
