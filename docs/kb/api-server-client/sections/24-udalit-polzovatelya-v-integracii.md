---
id: api-server-client-24-udalit-polzovatelya-v-integracii
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.8"
pdf_section: "3.1.8"
title: "Удалить пользователя (в интеграции)"
pdf_heading: "3.1.8 Удалить пользователя (в интеграции)"
pages: "19-20"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 19-20"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"19-20","global_pages":"19-20"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 504
images: 0
status: extracted
ai-generated: true
---
### 3.1.8. Удалить пользователя (в интеграции)

> Трассировка: PDF §3.1.8 · сквозные стр. 19-20 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.19-20.

POST /v1/users/delete Header[X-Mango-API-Token]

С помощью этого запроса вы можете удалить регистрацию пользователя ВАТС в сервисе интеграций. После удаления пользователя из сервиса интеграций, сервис прекращает обрабатывать звонки на данного пользователя ВАТС и от данного пользователя ВАТС.

Примечание. Накопленная информация по сотруднику останется в системе и будет доступна после повторного создания пользователя с этим extension.

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| User | object | Да |  |  |
| User[ext] | string | Да | [\\d]{1,7} | Внутренний номер сотрудника в ВАТС |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

User object Да

Внутренний номер сотрудника в User[ext] string Да [\\d]{1,7} ВАТС

Пример запроса:

{ "ext": "1100" }

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

● 200 - Result[code]=0 ● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 400 - User[ext] не задан. Result[code]=103, Result[message]="User extension number not set"

● 400 - ошибка парсинга JSON запроса ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "500", "message": "Auth failed" } }
