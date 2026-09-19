---
id: vpbx-api-09-api-kc
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "1.4.3"
pdf_section: "1.4.3"
title: "API КЦ"
pdf_heading: "1.4.3 API КЦ"
pages: "10"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 10"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"10","global_pages":"10"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 243
status: extracted
ai-generated: true
---
# 1.4.3. API КЦ

> Трассировка: PDF §1.4.3 · сквозные стр. 10 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.10.

Устанавливаются следующие лимиты запросов в секунду:

| Запрос | Максимальное число запросов / в секунду |
| --- | --- |
| Для всех запросов | 10/1 |
| Создание задачи на автоперезвон (/task/add) | 5/1 |

Если установленный лимит превышен, то обработка запросов, поступающих к API КЦ, будет временно остановлена и вы увидите следующее сообщение: { "result": 5008 } Если ошибка 5008 не возникала, значит лимит количества запросов не превышен.
