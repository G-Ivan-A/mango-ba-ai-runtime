---
id: vpbx-api-21-pole-json
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "2.4.4"
pdf_section: "2.4.4"
title: "Поле json"
pdf_heading: "2.4.4 Поле json"
pages: "15"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 15"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"15","global_pages":"15"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 256
status: extracted
ai-generated: true
---
# 2.4.4. Поле json

> Трассировка: PDF §2.4.4 · сквозные стр. 15 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.15.

Поле json можно рассматривать как ассоциативный массив любой вложенности и размера (действуют только системные ограничения на размер всего POST-запроса). JSON-строка должна быть корректной, лучше программно формируемой из ассоциативного массива, без искусственных пробелов и переносов строк, например: POST https://app.mango-office.ru/vpbx/commands/callback vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"cmd.2.vpbx.system.com.net", "from": { "extension":"123" }, "to_number":"744" }
