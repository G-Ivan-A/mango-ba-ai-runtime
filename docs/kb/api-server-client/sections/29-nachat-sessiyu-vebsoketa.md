---
id: api-server-client-29-nachat-sessiyu-vebsoketa
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.13"
pdf_section: "3.1.13"
title: "Начать сессию вебсокета"
pdf_heading: "3.1.13 Начать сессию вебсокета"
pages: "26-27"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 26-27"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"26-27","global_pages":"26-27"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 314
images: 0
status: extracted
ai-generated: true
---
### 3.1.13. Начать сессию вебсокета

> Трассировка: PDF §3.1.13 · сквозные стр. 26-27 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.26-27.

POST /v1/session/register/{userId} Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обязательность | Формат |
| --- | --- | --- | --- |
| userId | integer | Да | Внутренний номер пользователя |

Параметр Тип Обязательность Формат

Внутренний номер userId integer Да пользователя

Пример запроса:

POST /v1/session/register/101

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

● 400 - Пользователь зарегистрирован. Result[code]=103, Result[message]="User registered"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
