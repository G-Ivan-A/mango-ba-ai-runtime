---
id: api-server-client-20-ustanovit-nastroyki
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.4"
pdf_section: "3.1.4"
title: "Установить настройки"
pdf_heading: "3.1.4 Установить настройки"
pages: "14"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 14"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"14","global_pages":"14"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 496
images: 0
status: extracted
ai-generated: true
---
### 3.1.4. Установить настройки

> Трассировка: PDF §3.1.4 · сквозные стр. 14 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.14.

POST /v1/settings/set/ Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| Settings | object | Да |  |  |
| Settings[enable_presence] | boolean | Нет | true/false | Уведомление о статусах клиентов |
| Settings[enable_internal_calls] | boolean | Нет | true/false | Включить/выключить события внутренних звонков |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

Settings object Да

true/false Уведомление о Settings[enable_presence] boolean Нет статусах клиентов

Включить/выключить

Settings[enable_internal_calls] boolean Нет true/false

события внутренних звонков

Пример запроса:

curl -X POST -d '{"enable_presence": true}' .../v1/settings/set/1a71c2bc-47dc- 4668-8714-e0158653xxxx

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

● 200 - настройки успешно установлены. Result[code]=0 ● 400 - Settings[data] пустой. Result[code]=103 не задан. Result[message]="Data is empty"

● 400 - Settings[data] ошибка парсинга JSON запроса. Result[code]=103 не задан. Result[message]="Data format corrupted"

● 403 - token не указан. Result[code]=103, Result[message]="Auth token is not set" ● 500 - критическая ошибка. Result[code]=500 Пример ответа:

{ "result": { "code": "0", "message": "OK" }}
