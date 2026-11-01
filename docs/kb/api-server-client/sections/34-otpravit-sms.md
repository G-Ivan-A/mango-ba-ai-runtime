---
id: api-server-client-34-otpravit-sms
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.18"
pdf_section: "3.1.18"
title: "Отправить SMS"
pdf_heading: "3.1.18 Отправить SMS"
pages: "31-32"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 31-32"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"31-32","global_pages":"31-32"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 577
images: 0
status: extracted
ai-generated: true
---
### 3.1.18. Отправить SMS

> Трассировка: PDF §3.1.18 · сквозные стр. 31-32 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.31-32.

POST /v1/sms Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Описание |
| --- | --- | --- | --- |
| USER_ID | string | Да | Внутренний номер пользователя |
| DESTINATION_NUMBER | string | Да | Номер для отправки sms |
| TEXT | string | Да | Текст сообщения |
| SENDER_ID | string | Нет | Идентификатор запроса |

Обяза-

Параметр Тип

тель-

Описание

ность

USER_ID string Да Внутренний номер пользователя

DESTINATION_NUMBER string Да Номер для отправки sms

TEXT string Да Текст сообщения

SENDER_ID string Нет Идентификатор запроса

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" -X POST .../v1/sms?USER_ID=8000&

DESTINATION_NUMBER=79216019999&TEXT=test&SENDER_ID=taxi

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | object |  |
| Data[code] | integer | результат запроса |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data object

Data[code] integer результат запроса

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 и Result[data][code]=1000 ● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 400 - Номер для отправки sms пустой. Result[code]=103, Result[message]="Destination number is empty"

● 400 - Текст сообщения пустой. Result[code]=103, Result[message]="Text is empty"

● 400 - Текст сообщения превышает 612 символов. Result[code]=103, Result[message]="Text is too long"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "code": 1000 } }
