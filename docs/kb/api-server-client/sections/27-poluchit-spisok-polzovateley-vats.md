---
id: api-server-client-27-poluchit-spisok-polzovateley-vats
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.11"
pdf_section: "3.1.11"
title: "Получить список пользователей (ВАТС)"
pdf_heading: "3.1.11 Получить список пользователей (ВАТС)"
pages: "23-25"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 23-25"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"23-25","global_pages":"23-25"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 664
images: 0
status: extracted
ai-generated: true
---
### 3.1.11. Получить список пользователей (ВАТС)

> Трассировка: PDF §3.1.11 · сквозные стр. 23-25 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.23-25.

POST /v1/vpbxusers/get/

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| USER_ID | integer | Нет | Внутренний номер пользователя |  |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

USER_ID integer Нет Внутренний номер пользователя

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" \\ -H "X-Mango-API-Salt:1111-1111-1111-0000" \\ -X POST .../v1/vpbxusers/get

Запрос

Header[X-Mango-API-Token]

Header[X-Mango-API-Salt] Ключ для создания подписи

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Result[data][users] | array | Список пользователей |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Result[data][users] array Список пользователей

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 400 - Result[code]=109, Result[message]="Salt not present" ● 400 - Result[code]=109, Result[message]="ApiKey not found" ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "users": [{ "general": { "name": "admin", "email": null, "department": null, "position": null }, "telephony": { "extension": null, "outgoingline": "74951204609", "numbers": [] } }, { "general": { "name": "AMO_MOD", "email": null, "department": null, "position": null }, "telephony": { "extension": "20000", "outgoingline": "74951204609", "numbers": [{ "number": "sip:amo_mod@vpbx400022984.mangosip.ru", "protocol": "sip", "order": 0, "wait_sec": null, "status": "on" } ] } }, { "general": { "name": "Bit Test", "email": "", "department": "", "position": "" }, "telephony": { "extension": "10000", "outgoingline": "74951204609", "numbers": [{ "number": "sip:bittest@vpbx400022984.mangosip.ru",

"protocol": "sip", "order": 0, "wait_sec": 120, "status": "on" } ] } } ] } }
