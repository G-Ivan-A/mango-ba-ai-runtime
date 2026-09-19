---
id: vpbx-api-202-udalenie-zadaniya
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.16"
pdf_section: "4.6.16"
title: "Удаление задания"
pdf_heading: "4.6.16 Удаление задания"
pages: "285-286"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 285-286"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"285-286","global_pages":"285-286"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 327
status: extracted
ai-generated: true
---
# 4.6.16. Удаление задания

> Трассировка: PDF §4.6.16 · сквозные стр. 285-286 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.285-286.

POST /vpbx/task/delete Метод предназначен для удаления задания кампании ИО. Параметры запроса:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | campaign_id | Число | Да | ID кампании |
| 2 | task_id | Число | Да | ID задания кампании |

Пример запроса: POST https://app.mango-office.ru/vpbx/task/delete vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = {"campaign_id": 56919, "task_id": 11227830 } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Число | Да | Код результата |
