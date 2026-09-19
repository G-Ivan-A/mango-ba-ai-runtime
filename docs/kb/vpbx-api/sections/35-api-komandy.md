---
id: vpbx-api-35-api-komandy
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.2"
pdf_section: "3.2"
title: "API Команды"
pdf_heading: "3.2 API Команды"
pages: "33"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 33"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"33","global_pages":"33"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 234
status: extracted
ai-generated: true
---
# 3.2. API Команды

> Трассировка: PDF §3.2 · сквозные стр. 33 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.33.

API Команды представляет собой набор запросов, которые инициирует внешняя система и направляет их к API ВАТС. Часть команд требует передачи идентификаторов, которые можно получить только при использовании API Realtime. После приема команды к исполнению, API генерирует для внешней системы уведомление о результате старта команды. Последовательность доставки результата старта команды и событий, которые команда породила, не гарантируется.
