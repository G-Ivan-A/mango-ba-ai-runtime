---
id: api-server-client-21-poluchit-nastroyki
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.5"
pdf_section: "3.1.5"
title: "Получить настройки"
pdf_heading: "3.1.5 Получить настройки"
pages: "15"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 15"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"15","global_pages":"15"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 288
images: 0
status: extracted
ai-generated: true
---
### 3.1.5. Получить настройки

> Трассировка: PDF §3.1.5 · сквозные стр. 15 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.15.

POST /v1/settings/get/ Header[X-Mango-API-Token]

Запрос без параметров.

Пример запроса:

curl -X POST .../v1/settings/get/1a71c2bc-47dc-4668-8714-e0158653xxxx

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | object |  |
| Data[enable_presence] | boolean | Уведомление о статусах клиентов |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data object

Data[enable_presence] boolean Уведомление о статусах клиентов

Возможны следующие HTTP коды ответа:

● 200 - настройки успешно получены. Result[code]=0 ● 403 - token не указан. Result[code]=103, Result[message]="Auth token is not set"

● 500 - критическая ошибка. Result[code]=500

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "enable_presence": true } }
