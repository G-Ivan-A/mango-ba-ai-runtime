---
id: api-server-client-25-poluchit-status-polzovateley-v-integraci
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.9"
pdf_section: "3.1.9"
title: "Получить статус пользователей (в интеграции)"
pdf_heading: "3.1.9 Получить статус пользователей (в интеграции)"
pages: "20-21"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 20-21"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"20-21","global_pages":"20-21"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 805
images: 0
status: extracted
ai-generated: true
---
### 3.1.9. Получить статус пользователей (в интеграции)

> Трассировка: PDF §3.1.9 · сквозные стр. 20-21 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.20-21.

POST /v1/users/state Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| User | object | Нет |  |  |
| User[ext] | string | Нет | [\\d]{1,7} | Внутренний номер сотрудника в ВАТС, в случае отсутствия параметра будет выводить полный список пользователей |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

User object Нет

Внутренний номер сотрудника в ВАТС, в

User[ext] string Нет [\\d]{1,7}

случае отсутствия параметра будет выводить полный список пользователей

Пример запроса:

{ "ext": "8000" }

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | object |  |
| Data[registred] | boolean | зарегистрирован / не зарегистрирован вебсокет |
| Data[State] | object | состояние пользователя |
| Data[State[ext]] | string | Идентификатор пользователя |
| Data[State[callid]] | string | ID звонка |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data object

boolean зарегистрирован / не зарегистрирован Data[registred] вебсокет

Data[State] object состояние пользователя

Data[State[ext]] string Идентификатор пользователя

Data[State[callid]] string ID звонка

| Параметр | Тип | Описание |
| --- | --- | --- |
| Data[State[entryid]] | string |  |
| Data[State[callType]] | string | Входящий / Исходящий / Внутренний |
| Data[State[phone]] | string | Звонок на номер |
| Data[State[caller]] | string | Звонящий |
| Data[State[state]] | string | Состояние пользователя: APPEARED, CONNECTED, ON_HOLD, FREE |

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 200 - статусов нет ● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 400 - User[ext] не задан. Result[code]=103, Result[message]="User not found" ● 400 - ошибка парсинга JSON запроса ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": [{ "state": { "ext": "8000", "callId": "MToxMDAxMzAxOTozODE6NTY1NjQxNzEy", "entryId": "MzE4MDc3NjgyMzozODE=", "callType": "OUTBOUND", "phone": "79269226127", "caller": "8000", "state": "CONNECTED" }, "registred": true } ] }
