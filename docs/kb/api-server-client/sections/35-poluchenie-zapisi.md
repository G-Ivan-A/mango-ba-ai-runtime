---
id: api-server-client-35-poluchenie-zapisi
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.19"
pdf_section: "3.1.19"
title: "Получение записи"
pdf_heading: "3.1.19 Получение записи"
pages: "32-33"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 32-33"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"32-33","global_pages":"32-33"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 535
images: 0
status: extracted
ai-generated: true
---
### 3.1.19. Получение записи

> Трассировка: PDF §3.1.19 · сквозные стр. 32-33 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.32-33.

GET /v1/record/{userId}/{recordingId}

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат |
| --- | --- | --- | --- |
| userId | integer | Да | Внутренний номер пользователя |
| recordingId | string | Да | ID записи |

Обяза-

Параметр Тип

тель-

Формат

ность

userId integer Да Внутренний номер пользователя

recordingId string Да ID записи

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" \\ -H "X-Mango-API-Salt:1111-1111-1111-0000" \\ -X GET .../v1/record/101/MToxMDA1OTY5NTozMTAzNDY4XXX3OjA%3D

Запрос

Header[X-Mango-API-Token]

Header[X-Mango-API-Salt] Ключ для создания подписи {userId} - внутренний номер пользователя {recordingId} - ID записи

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

● 200 - Content-type=audio/mpeg, файл записи ● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 404 - не заданы параметры {userId}, {recordingId} ● 400 - не задан ключ создания подписи. Result[code]=103, Result[message]="Salt not present"

● 400 - не верный ключ создания подписи. Result[code]=103, Result[message]="Salt is incorrect"

● 404 - запись не найдена. Result[code]=103, Result[message]="Record not found"

● 500 - прочие ошибки получения записи. Result[code]=500, Result[message]="Cannot get record"

Пример ответа:

HTTP 200 Content-Type audio/mpeg Content-Length 10000
