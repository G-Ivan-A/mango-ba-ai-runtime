---
id: api-server-client-31-proverka-statusa-servera
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.15"
pdf_section: "3.1.15"
title: "Проверка статуса сервера"
pdf_heading: "3.1.15 Проверка статуса сервера"
pages: "28"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 28"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"28","global_pages":"28"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 160
images: 0
status: extracted
ai-generated: true
---
### 3.1.15. Проверка статуса сервера

> Трассировка: PDF §3.1.15 · сквозные стр. 28 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.28.

GET /v1/session/ping

Запрос без параметров.

Пример запроса:

curl -X GET ../v1/session/ping

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● Иной ответ - проблема сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
