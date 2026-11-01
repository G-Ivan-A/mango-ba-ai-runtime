---
id: api-server-client-32-iniciirovat-zvonok
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.16"
pdf_section: "3.1.16"
title: "Инициировать звонок"
pdf_heading: "3.1.16 Инициировать звонок"
pages: "29-30"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 29-30"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"29-30","global_pages":"29-30"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 453
images: 0
status: extracted
ai-generated: true
---
### 3.1.16. Инициировать звонок

> Трассировка: PDF §3.1.16 · сквозные стр. 29-30 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.29-30.

POST /v1/callback Header[X-Mango-API-Token]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Описание |
| --- | --- | --- | --- |
| USER_ID | string | Да | Внутренний номер пользователя |
| DESTINATION_NUM BER | string | Да | Номер для дозвона |
| TRANSACTION_ID | string | Нет | Идентификатор запроса |

Обяза-

Параметр Тип

тель-

Описание

ность

USER_ID string Да Внутренний номер пользователя

DESTINATION_NUM string Да Номер для дозвона BER

TRANSACTION_ID string Нет Идентификатор запроса

Пример запроса:

curl -H "X-Mango-API-Token:1a71c2bc-47dc-4668-8714-e0158653xxxx" -X POST .../v1/callback?USER_ID=10&DESTINATION_NUMBER=74995404444

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

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": {

"code": 1000 } }
