---
id: api-server-client-40-kc-poluchenie-informacii-o-zadanii
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.24"
pdf_section: "3.1.24"
title: "КЦ. Получение информации о задании"
pdf_heading: "3.1.24 КЦ. Получение информации о задании"
pages: "43-44"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 43-44"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"43-44","global_pages":"43-44"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 241
images: 0
status: extracted
ai-generated: true
---
### 3.1.24. КЦ. Получение информации о задании

> Трассировка: PDF §3.1.24 · сквозные стр. 43-44 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.43-44.

POST /v1/cov/get_campaign_task_info?campaign_task_id={id} Header[X-Mango- API-Token]

Параметры запроса:

| Параметр | Тип | Описание |
| --- | --- | --- |
| campaign_task_id | integer | id задания, обязательное |

Параметр Тип Описание

campaign_task_id integer id задания, обязательное

Пример запроса:

GET /v1/cov/get_campaign_task_info?campaign_task_id=123

Пример ответа:

{ "result": { "code": "0", "message": "OK", "appInfoId": null }, "data": { "result": 1000, "campaign_task": { "name": "FIO 0016", "position": "DOLJN 0016", "organization": "ORG 0016", "number": "9015", "talk_duration": null, "status": 1, "status_reason": null, "comment": "", "end": null, "created": "2017-12-20 09:48:35.501139" } } }
