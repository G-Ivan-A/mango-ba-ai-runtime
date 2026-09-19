---
id: vpbx-api-195-zapusk-kampanii
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.9"
pdf_section: "4.6.9"
title: "Запуск кампании"
pdf_heading: "4.6.9 Запуск кампании"
pages: "276"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 276"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"276","global_pages":"276"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 406
status: extracted
ai-generated: true
---
# 4.6.9. Запуск кампании

> Трассировка: PDF §4.6.9 · сквозные стр. 276 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.276.

POST /vpbx/campaign/start Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | campaign_id |  |  | id кампании, обязательное |

Пример запроса: POST https://app.mango-office.ru/vpbx/campaign/start vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "campaign_id":"16340" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Число | Да | Код результата |
| 2 | status | Число | Да | Текущий статус кампании. Статус кампании: 0 – остановлена;<br>1 – запланирована; 2 - в работе; 3 – останавливается;<br>4 – завершена; 5 – обрабатывается; 6 – удаляется. |

Пример ответа: { "result": 1000, "status": 1 }
