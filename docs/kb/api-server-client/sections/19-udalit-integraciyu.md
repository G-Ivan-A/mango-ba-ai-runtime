---
id: api-server-client-19-udalit-integraciyu
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.3"
pdf_section: "3.1.3"
title: "Удалить интеграцию"
pdf_heading: "3.1.3 Удалить интеграцию"
pages: "13"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 13"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"13","global_pages":"13"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 307
images: 0
status: extracted
ai-generated: true
---
### 3.1.3. Удалить интеграцию

> Трассировка: PDF §3.1.3 · сквозные стр. 13 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.13.

POST /v1/integration/delete/{token}

После этого все сообщения, накопленные для пользователей данной интеграции станут недоступными.

Параметры запроса:

| Параметр | Тип | Описание |
| --- | --- | --- |
| token | string(UUID) | Ключ интеграции |

Параметр Тип Описание

token string(UUID) Ключ интеграции

Пример запроса:

curl -X POST .../v1/integration/delete/1a71c2bc-47dc-4668-8714-e0158653xxxx

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

● 200 - удаление успешно. Result[code]=0 ● 403 - token не указан. Result[code]=103, Result[message]="Auth token is not set"

● 500 - критическая ошибка. Result[code]=500

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
