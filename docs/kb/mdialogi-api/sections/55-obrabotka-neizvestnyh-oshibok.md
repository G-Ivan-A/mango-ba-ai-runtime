---
id: mdialogi-api-55-obrabotka-neizvestnyh-oshibok
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "4.2.3"
pdf_section: "4.2.3"
title: "Обработка неизвестных ошибок"
pdf_heading: "4.2.3 Обработка неизвестных ошибок"
pages: "65"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 65"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"65","global_pages":"65"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 144
status: extracted
ai-generated: true
---
# 4.2.3. Обработка неизвестных ошибок

> Трассировка: PDF §4.2.3 · сквозные стр. 65 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.65.

Если система получает код ошибки, который отсутствует в реестре, он обрабатывается как:

|  | system-error |  |
| --- | --- | --- |

В этом случае рекомендуется повторить отправку сообщения позже.
