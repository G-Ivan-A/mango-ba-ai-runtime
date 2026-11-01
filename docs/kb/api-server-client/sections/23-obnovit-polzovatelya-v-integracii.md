---
id: api-server-client-23-obnovit-polzovatelya-v-integracii
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.7"
pdf_section: "3.1.7"
title: "Обновить пользователя (в интеграции)"
pdf_heading: "3.1.7 Обновить пользователя (в интеграции)"
pages: "17-18"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 17-18"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"17-18","global_pages":"17-18"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 629
images: 0
status: extracted
ai-generated: true
---
### 3.1.7. Обновить пользователя (в интеграции)

> Трассировка: PDF §3.1.7 · сквозные стр. 17-18 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.17-18.

POST /v1/users/update Header[X-Mango-API-Token]

С помощью данного запроса вы можете обновить зарегистрированного пользователя ВАТС в сервисе интеграций.

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| User | object | Да |  |  |
| User[ext] | string | Да | [\\d]{1,7} | Внутренний номер сотрудника в ВАТС |
| User[name] | string | Нет |  | Фамилия пользователя |
| User[second_name] | string | Нет |  | Имя пользователя |
| User[last_name] | string | Нет |  | Отчество пользователя |
| User[email] | string | Нет |  | e-mail пользователя, формат не проверяется |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

User object Да

Внутренний номер User[ext] string Да [\\d]{1,7} сотрудника в ВАТС

User[name] string Нет Фамилия пользователя

User[second_name] string Нет Имя пользователя

User[last_name] string Нет Отчество пользователя

e-mail пользователя, User[email] string Нет формат не проверяется

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" -X POST -d '{\\ "ext": "101",\\ "name": "Test", \\ "email": "example@example.com"\\ }' .../v1/users/update

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

● 400 - User[ext] не существует. Result[code]=103, Result[message]="User not exist"

● 400 - ошибка парсинга JSON запроса ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
