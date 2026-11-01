---
id: api-server-client-36-perevesti-na-sotrudnika
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.20"
pdf_section: "3.1.20"
title: "Перевести на сотрудника"
pdf_heading: "3.1.20 Перевести на сотрудника"
pages: "34-35"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 34-35"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"34-35","global_pages":"34-35"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 462
images: 0
status: extracted
ai-generated: true
---
### 3.1.20. Перевести на сотрудника

> Трассировка: PDF §3.1.20 · сквозные стр. 34-35 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.34-35.

POST /v1/route/async/{userId}?TO={ext}&CALL_ID={callId}&TRANSACTION_ID={txId} Header[X-Mango-API-Token]

Может совершаться при получении события routeKey=/ivr

Параметры запроса:

| Параметр | Тип | Описание |
| --- | --- | --- |
| TO | integer | Внутренний номер сотрудника, на которого перевести |
| CALL_ID | string | ID текущего звонка |
| TRANSACTION_ID | string | ID транзакции |

Параметр Тип Описание

Внутренний номер сотрудника, на которого TO integer перевести

CALL_ID string ID текущего звонка

TRANSACTION_ID string ID транзакции

Пример запроса:

POST /v1/route/async/101?TO=102&CALL_ID=MToxMDA1ODc2Njg4NXXX&TRANSACTION_ID=1000000

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

● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="Target user not found"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Асинхронно приходит событие результата перевода.

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
