---
id: api-server-client-39-perevod-transfer-zvonka
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.23"
pdf_section: "3.1.23"
title: "Перевод (transfer) звонка"
pdf_heading: "3.1.23 Перевод (transfer) звонка"
pages: "42-43"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 42-43"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"42-43","global_pages":"42-43"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 582
images: 0
status: extracted
ai-generated: true
---
### 3.1.23. Перевод (transfer) звонка

> Трассировка: PDF §3.1.23 · сквозные стр. 42-43 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.42-43.

3.1.23.1 "Слепой" перевод

POST /v1/transfer/blind?USER_ID={ext}&CALL_ID={callId}&DESTINATION_NUMBER={to}& TRANSACTION_ID={txId}

Header[X-Mango-API-Token]

3.1.23.2 Консультативный перевод

POST /v1/transfer/hold?USER_ID={ext}&CALL_ID={callId}&DESTINATION_NUMBER={to}&T RANSACTION_ID={txId}

Header[X-Mango-API-Token]

3.1.23.3 Описание запросов

Совершается в состоянии CONNECTED

Параметры запроса:

| Параметр | Тип | Описание |
| --- | --- | --- |
| DESTINATION_NUMBER | string | Номер, на который перевести |
| CALL_ID | string | ID текущего звонка |
| USER_ID | string | Внутренний номер сотрудника, принимающего вызов |
| TRANSACTION_ID | string | ID транзакции |

Параметр Тип Описание

DESTINATION_NUMBER string Номер, на который перевести

CALL_ID string ID текущего звонка

Внутренний номер сотрудника, USER_ID string принимающего вызов

TRANSACTION_ID string ID транзакции

Пример запроса:

POST /v1/transfer/blind?USER_ID=1234&DESTINATION_NUMBER=84955404444&CALL_ID=MToxMDAX XX&transaction_id=1000000

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Result[data] | object |  |
| Result[data][code] | string | Результат запроса |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Result[data] object

Result[data][code] string Результат запроса

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "code": 1000 } }
