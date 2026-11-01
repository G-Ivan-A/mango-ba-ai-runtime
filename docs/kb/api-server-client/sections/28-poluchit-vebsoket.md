---
id: api-server-client-28-poluchit-vebsoket
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.12"
pdf_section: "3.1.12"
title: "Получить вебсокет"
pdf_heading: "3.1.12 Получить вебсокет"
pages: "25-26"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 25-26"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"25-26","global_pages":"25-26"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 501
images: 0
status: extracted
ai-generated: true
---
### 3.1.12. Получить вебсокет

> Трассировка: PDF §3.1.12 · сквозные стр. 25-26 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.25-26.

GET /v1/channel/{userId} Header[X-Mango-API-Token]

Запрос служит для предоставления отдельного вебсокета клиентскому приложению. Возвращается идентификатор канала и URL вебсокета. Эти данные необходимо использовать клиентскому приложению для получения информации о звонках пользователя.

Параметры запроса:

| Параметр | Тип | Обязательность | Формат |
| --- | --- | --- | --- |
| userId | integer | Да | Внутренний номер пользователя |

Параметр Тип Обязательность Формат

Внутренний номер userId integer Да пользователя

Пример запроса:

GET /v1/channel/101

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Data | object |  |
| Data[id] | string | id канала |
| Data[ws_url] | URL | URL вебсокета |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Data object

Data[id] string id канала

Data[ws_url] URL URL вебсокета

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "id": "api_prod9e8a2db8-4827-4d90-b9a4-bd1dca89xxxx", "ws_url": " ws://api.mango-office.ru:9080/ws/channel/api_prob8-4827-4d90-b9a4- b89xxxx"

} }
