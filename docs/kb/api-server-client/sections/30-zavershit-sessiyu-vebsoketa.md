---
id: api-server-client-30-zavershit-sessiyu-vebsoketa
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.14"
pdf_section: "3.1.14"
title: "Завершить сессию вебсокета"
pdf_heading: "3.1.14 Завершить сессию вебсокета"
pages: "27-28"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 27-28"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"27-28","global_pages":"27-28"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 301
images: 0
status: extracted
ai-generated: true
---
### 3.1.14. Завершить сессию вебсокета

> Трассировка: PDF §3.1.14 · сквозные стр. 27-28 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.27-28.

POST /v1/session/unregister/{userId} Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат |
| --- | --- | --- | --- |
| userId | integer | Да | Внутренний номер пользователя |

Обяза-

Параметр Тип

тель-

Формат

ность

userId integer Да Внутренний номер пользователя

Пример запроса:

POST /v1/session/unregister/101

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

● 200 - Result[code]=0 ● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
