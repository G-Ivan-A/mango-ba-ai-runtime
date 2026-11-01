---
id: api-server-client-37-poluchit-propuschennye-sobytiya
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.21"
pdf_section: "3.1.21"
title: "Получить пропущенные события"
pdf_heading: "3.1.21 Получить пропущенные события"
pages: "35-37"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 35-37"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"35-37","global_pages":"35-37"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 731
images: 0
status: extracted
ai-generated: true
---
### 3.1.21. Получить пропущенные события

> Трассировка: PDF §3.1.21 · сквозные стр. 35-37 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.35-37.

POST /v1/notifications/missed/pull?USER_ID={ext}&LIMIT={limit} Header[X- Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Описание |
| --- | --- | --- |
| USER_ID | string | Внутренний номер сотрудника |
| LIMIT | integer | Ограничение на кол-во возвращаемых записей |

Параметр Тип Описание

USER_ID string Внутренний номер сотрудника

LIMIT integer Ограничение на кол-во возвращаемых записей

Пример запроса:

POST /v1/notifications/missed/pull?USER_ID=101&LIMIT=3

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Result[data] | Array |  |
| Result[data][index][key] | string | Тип события |
| Result[data][index][data] | object | Событие в формате события Websocket |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Result[data] Array

Result[data][index][key] string Тип события

Result[data][index][data] object Событие в формате события Websocket

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 200 - Пропущенных событий нет. Result[code]=109, Result[message]="Missed notifications not found"

● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа #1:

{ "result": { "code": "0", "message": "OK" }, "data": [{ "key": "/call", "data": { "id": "MToxMDAxMzAxOToyMjo5NTAxMjXXX=", "entryId": "MzAxNjAzNTY5MjoXXX", "callType": "INBOUND", "timestamp": 1499872854171, "phone": "101", "caller": "7926000000", "timeStart": null, "timeEnd": null, "recordingStatus": "NONE", "state": "APPEARED", "userId": { "accountId": { "token": "e064f18c-2d04-4801-8cd5-xxx" }, "ext": { "value": "101" } }, "disconnectReason": null, "isInternalCall": false, "isConnected": false, "isFinished": false, "takenFromCallId": "MToxMDAxMzAxOToyMjo5NTAxMjIXXXX", "acdGroup": null, "transactionId": null, "isGroupDisconnect": false } } ] }

Пример ответа #2:

{ "result": { "code": "109", "message": "Missed notifications not found" } }
