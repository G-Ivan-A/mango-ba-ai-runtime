---
id: api-server-client-22-sozdat-polzovatelya-v-integracii
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.6"
pdf_section: "3.1.6"
title: "Создать пользователя (в интеграции)"
pdf_heading: "3.1.6 Создать пользователя (в интеграции)"
pages: "16-17"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 16-17"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"16-17","global_pages":"16-17"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 789
images: 0
status: extracted
ai-generated: true
---
### 3.1.6. Создать пользователя (в интеграции)

> Трассировка: PDF §3.1.6 · сквозные стр. 16-17 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.16-17.

POST /v1/users/create Header[X-Mango-API-Token]

С помощью этого запроса вы можете регистрировать пользователя ВАТС в сервисе интеграций. После регистрации пользователя, сервис интеграций начинает обрабатывать звонки на данного пользователя ВАТС и от данного пользователя ВАТС. Если пользователь ВАТС не зарегистрирован в сервисе интеграций, то вызовы на него или с него не обрабатываются сервисом интеграций. Уникальным идентификатором пользователя для сервиса интеграций служит внутренний номер пользователя в ВАТС.

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

e-mail пользователя, формат User[email] string Нет не проверяется

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" -X POST -d '{\\ "ext": "101",\\ "name": "Test", \\ "email": "example@example.com",\\ "last_name": "Lastname",\\ "second_name": "Secondname"\\ }' .../v1/users/create

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

● 400 - User[ext] существует. Result[code]=103, Result[message]="User exist" ● 400 - ошибка парсинга JSON запроса ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" } }
