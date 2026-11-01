---
id: api-server-client-26-poluchit-spisok-polzovateley-v-integraci
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.10"
pdf_section: "3.1.10"
title: "Получить список пользователей (в интеграции)"
pdf_heading: "3.1.10 Получить список пользователей (в интеграции)"
pages: "22-23"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 22-23"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"22-23","global_pages":"22-23"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 508
images: 0
status: extracted
ai-generated: true
---
### 3.1.10. Получить список пользователей (в интеграции)

> Трассировка: PDF §3.1.10 · сквозные стр. 22-23 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.22-23.

GET /v1/users Header[X-Mango-API-Token]

Запрос возвращает информацию о пользователях ВАТС, зарегистрированных в сервисе интеграций, внешнему приложению. Уникальным идентификатором пользователя служит внутренний номер пользователя ВАТС.

Примечание. Запрос можно использовать, к примеру, для отображения настроек сервиса интеграций внешним приложением.

Запрос без параметров.

Пример запроса:

GET /v1/users

Параметры ответа

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | array of User |  |
| [Data[User]] | User |  |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data array of User

[Data[User]] User

Для каждого пользователя возвращается набор данных, идентичный методу "Создать пользователя (в интеграции)". Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 200 - Result[code]=109, Result[message]="Users not found" ● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": [{ "ext": "101", "name": "Test1", "second_name": "Secondname", "last_name": "Lastname",

"email": "aaa@aaa.com" }, { "ext": "102", "name": "Test2", "second_name": "Secondname", "last_name": "Lastname", "email": "ccc@ccc.com" }, { "ext": "103", "name": "Test3", "second_name": "Secondname", "last_name": "Lastname", "email": "aaa@aaa.com" } ] }
