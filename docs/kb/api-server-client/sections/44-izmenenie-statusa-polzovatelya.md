---
id: api-server-client-44-izmenenie-statusa-polzovatelya
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.2.3"
pdf_section: "3.2.3"
title: "Изменение статуса пользователя"
pdf_heading: "3.2.3 Изменение статуса пользователя"
pages: "47"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 47"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"47","global_pages":"47"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 477
images: 0
status: extracted
ai-generated: true
---
### 3.2.3. Изменение статуса пользователя

> Трассировка: PDF §3.2.3 · сквозные стр. 47 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.47.

routeKey="/user_state"

Параметры события:

| Параметр | Тип | Описание |
| --- | --- | --- |
| routeKey | string | Тип события |
| data | object | Данные события звонка |
| data[ext] | string | Идентификатор пользователя |
| data[call_id] | string | ID звонка |
| data[caller] | string | Номер звонящего |
| data[phone] | string | Номер на который идет звонок |
| data[state] | string | Состояние пользователя: APPEARED, CONNECTED, ON_HOLD, FREE |
| data[callType] | string | Тип звонка, возможные значения: INBOUND, OUTBOUND, INTERNAL, UNKNOWN |
| data[entryId] | string |  |

Параметр Тип Описание

routeKey string Тип события

data object Данные события звонка

data[ext] string Идентификатор пользователя

data[call_id] string ID звонка

data[caller] string Номер звонящего

data[phone] string Номер на который идет звонок

Состояние пользователя: APPEARED, CONNECTED, data[state] string ON_HOLD, FREE

Тип звонка, возможные значения: INBOUND, data[callType] string OUTBOUND, INTERNAL, UNKNOWN

data[entryId] string

Пример события:

{ "routeKey": "user_state", "data": { "ext": "8000", "callId": "MToxMDAxMzAxOTozNjI6NDE2MDU1NDk3", "caller": "8000", "phone": "79269226127", "state": "CONNECTED", "callType": "OUTBOUND", "entryId": "MzE2OTgzMDA3NDozNjI=" } }{ "routeKey": "user_state", "data": { "ext": "8000", "state": "FREE" } }
