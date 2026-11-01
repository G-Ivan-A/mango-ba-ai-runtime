---
id: api-server-client-17-sozdanie-integracii
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.1"
pdf_section: "3.1.1"
title: "Создание интеграции"
pdf_heading: "3.1.1 Создание интеграции"
pages: "9-11"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 9-11"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"9-11","global_pages":"9-11"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 1251
images: 0
status: extracted
ai-generated: true
---
### 3.1.1. Создание интеграции

> Трассировка: PDF §3.1.1 · сквозные стр. 9-11 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.9-11.

POST /v1/integration/create

С помощью этого запроса создается уникальный ключ интеграции (token). Порядок использования запроса:

1) Клиент из внешней системы вызывает метод /integration/create; 2) при успешной валидации запроса внешней системе возвращается уникальный ключ интеграции (token). В дальнейшем, все вызовы методов API выполняются с данным ключом, кроме метода /session/ping;

3) на стороне сервера интеграций сохраняется соответствие token и vpbx_key;

4) система позволяет создавать несколько одновременных интеграций для одной ВАТС, в том числе с одинаковым типом внешней системы (system). Примечание. Если сменился "Уникальный код вашей АТС" в настройках услуги API ВАТС, то необходимо выполнить обновление регистрации интеграции для продолжения работы интеграции.

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| Registration | object | Да |  |  |
| Registration[vpbx_key] | string | Да | [\\w_=]{32} | API key ВАТС. Значение равно "Уникальный код вашей АТС" из настроек услуги API ВАТС. Идентифицирует ВАТС. |
| Registration[system] | integer | Нет | [\\d]+ | Тип внешней системы, предназначен для возможности реализации различия поведения системы, в зависимости от типа. Сохраняется, но пока не используется. |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

Registration object Да

API key ВАТС. Значение равно "Уникальный код вашей АТС" из настроек

Registration[vpbx_key] string Да [\\w_=]{32}

услуги API ВАТС.

Идентифицирует ВАТС.

Тип внешней системы, предназначен для возможности реализации различия

Registration[system] integer Нет [\\d]+

поведения системы, в зависимости от типа. Сохраняется, но пока не используется.

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| Registration[description] | string | Нет | [\\.]{0, 4096} | Описание. Сохраняется, но пока не используется. |

Пример запроса:

curl -X POST -d '{"vpbx_key": "80vs768xbekg9lq2wmii6i45elz2xxxx", "system": 1}' .../v1/integration/create

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | object |  |
| Data[token] | string(UUID) | Ключ интеграции |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data object

Data[token] string(UUID) Ключ интеграции

Возможны следующие HTTP коды ответа:

● 200 - успешно. Result[code]=0, Data[token] - код интеграции для дальнейшей авторизации;

● 400 - Registration[data] ошибка парсинга JSON запроса. Result[code]=103 не задан. Result[message]="Data format corrupted";

● 403 - Registration[api_key] не задан. Result[code]=103 не задан. Result[message]="VPBX key is not set";

● 403 - Registration[api_key] не верная длинна. Result[code]=103 не задан. Result[message]="VPBX key length is not 32";

● 403 - Registration[api_key] не найден в ВАТС. Result[code]=103 не задан. Result[message]="VPBX key is not valid";

● 403 - Registration[api_key] не уникален. Result[code]=103 не задан. Result[message]="VPBX key is not unique";

● 403 - Registration[description] не верная длинна. Result[code]=103 не задан. Result[message]="Description is too large, length more than 4096";

● 403 - Registration[system] не верный формат. Result[code]=103 не задан. Result[message]="System is not integer";

● 500 - ошибка сервера.

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "token": "1a71c2bc-47dc-4668-8714-e0158653f2be" } }
