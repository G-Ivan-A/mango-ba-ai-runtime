---
id: vpbx-api-200-zapusk-zadaniya-kampanii-io
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.14"
pdf_section: "4.6.14"
title: "Запуск задания кампании ИО"
pdf_heading: "4.6.14 Запуск задания кампании ИО"
pages: "284-285"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 284-285"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"284-285","global_pages":"284-285"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 330
status: extracted
ai-generated: true
---
# 4.6.14. Запуск задания кампании ИО

> Трассировка: PDF §4.6.14 · сквозные стр. 284-285 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.284-285.

POST /vpbx/task/start Метод позволяет запустить задание ИО. Параметры запроса:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | campaign_id | Число | Да | ID кампании |
| 2 | task_id | Число | Да | ID задания кампании |

Пример запроса: POST https://app.mango-office.ru/vpbx/task/start vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "campaign_id": 56919, "task_id": 11227830 } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Число | Да | Код результата |
