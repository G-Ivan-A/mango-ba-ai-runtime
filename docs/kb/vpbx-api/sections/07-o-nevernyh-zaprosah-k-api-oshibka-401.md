---
id: vpbx-api-07-o-nevernyh-zaprosah-k-api-oshibka-401
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "1.4.1"
pdf_section: "1.4.1"
title: "О неверных запросах к API. Ошибка 401"
pdf_heading: "1.4.1 О неверных запросах к API. Ошибка 401"
pages: "9"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 9"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"9","global_pages":"9"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 235
status: extracted
ai-generated: true
---
# 1.4.1. О неверных запросах к API. Ошибка 401

> Трассировка: PDF §1.4.1 · сквозные стр. 9 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.9.

Если ваш запрос к API MANGO OFFICE неверный, вы получаете код ошибки 3ХХХ. API MANGO OFFICE позволяет: - 1 неверный запрос в 2 минуты Если количество неверных запросов превышает эту квоту, то вы получаете ошибку 401. Если вы отправили к API MANGO OFFICE больше 1 неверного запроса, ваш доступ к API MANGO OFFICE блокируется до тех пор, пока не пройдет 2 минуты после получения первой ошибки 3ХХХ.
