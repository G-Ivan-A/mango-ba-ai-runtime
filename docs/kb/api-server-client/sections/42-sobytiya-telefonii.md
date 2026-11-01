---
id: api-server-client-42-sobytiya-telefonii
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.2.1"
pdf_section: "3.2.1"
title: "События телефонии"
pdf_heading: "3.2.1 События телефонии"
pages: "44-46"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 44-46"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"44-46","global_pages":"44-46"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 1004
images: 0
status: extracted
ai-generated: true
---
### 3.2.1. События телефонии

> Трассировка: PDF §3.2.1 · сквозные стр. 44-46 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.44-46.

routeKey="/call"

или

routeKey="/ivr"

Параметры события:

| Параметр | Тип | Описание |
| --- | --- | --- |
| routeKey | string | Тип события |
| data | object | Данные события звонка |
| data[transaction_id] | string | ID транзакции, заданной пользователем |
| data[from] | string | Номер откуда |
| data[to] | string | Номер куда |

Параметр Тип Описание

routeKey string Тип события

data object Данные события звонка

data[transaction_id] string ID транзакции, заданной пользователем

data[from] string Номер откуда

data[to] string Номер куда

| Параметр | Тип | Описание |
| --- | --- | --- |
| data[call_state] | string | Состояние звонка |
| data[disconnect_re ason] | integer | Код завершения |
| data[type] | string | Тип звонка |
| data[call_id] | string | ID звонка в ВАТС |
| data[is_group_disco nnect] | boolean | True=Звонок ушел на обработку другим сотрудникам группы ВАТС |
| data["timestamp] | long | Таймстамп создания |
| data["task_id"] | string | Идентификатор задачи исходящего обзвона, в результате которой появился вызов |
| data["callback_initia tor"] | string | Инициатор обратного звонка, в результате которого появился вызов |

Значения callback_initiator, передается, если звонок типа callback, а при обычном звонке отсутствует:

| callback_initiator | Описание |
| --- | --- |
| СС | ЦОВ-callback (Callback-вызов, инициатором которого является Центр обработки вызовов) |
| API | API-callback (Callback-вызов, инициатором которого является API) |
| WEB | WEB-callback, (Callback-вызов, инициатором которого является ЛК (Заказ звонка)) |
| ObDial | Callback-вызов, инициированный кампанией исходящего обзвона Центра обработки вызовов |
| CallbackWidget | Callback-вызов, инициированный виджетом обратного звонка |
| MissGroupСallCall back | Callback-вызов, инициированный перезвоном по пропущенному в группе |

callback_initiator Описание

ЦОВ-callback (Callback-вызов, инициатором которого СС является Центр обработки вызовов)

API-callback (Callback-вызов, инициатором которого API является API)

WEB-callback, (Callback-вызов, инициатором которого WEB является ЛК (Заказ звонка))

Callback-вызов, инициированный кампанией исходящего ObDial обзвона Центра обработки вызовов

Callback-вызов, инициированный виджетом обратного CallbackWidget звонка

MissGroupСallCall

Callback-вызов, инициированный перезвоном по

back

пропущенному в группе

Пример события:

{ "routeKey": "/call", "data": { "transaction_id": "3456345ydfgh", "is_internal": false, "from": "31020", "call_state": "CONNECTED", "to": "7926012xxxx", "disconnect_reason": "null", "type": "OUTBOUND", "call_id": "MToxMDAxMzAxOToyODE6NDUwNjU2NTM1", "timestamp": 1497620928925 } }
