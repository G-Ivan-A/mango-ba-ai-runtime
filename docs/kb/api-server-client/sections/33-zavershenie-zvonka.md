---
id: api-server-client-33-zavershenie-zvonka
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.17"
pdf_section: "3.1.17"
title: "Завершение звонка"
pdf_heading: "3.1.17 Завершение звонка"
pages: "30-31"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 30-31"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"30-31","global_pages":"30-31"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 490
images: 0
status: extracted
ai-generated: true
---
### 3.1.17. Завершение звонка

> Трассировка: PDF §3.1.17 · сквозные стр. 30-31 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.30-31.

POST /v1/callmanager/hangup Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Описание |
| --- | --- | --- | --- |
| USER_ID | string | Да | Внутренний номер пользователя |
| CALL_ID | string | Да | Идентификатор звонка |

Обяза-

Параметр Тип

тель-

Описание

ность

USER_ID string Да Внутренний номер пользователя

CALL_ID string Да Идентификатор звонка

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" -X POST .../v1/callmanager/hangup?USER_ID=8000&CALL_ID=MToxMDAxMzAxOToyNjE6NzA2OTM1NzY0

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | object |  |
| Data[code] | integer | результат запроса |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data object

Data[code] integer результат запроса

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 и Result[data][code]=1000 ● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 400 - Ошибка при операции в ВАТС. Result[code]=500, Result[message]="Hangup failed", Data[code]="код ошибки"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "code": 1000 } }
