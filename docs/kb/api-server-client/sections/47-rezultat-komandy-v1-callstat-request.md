---
id: api-server-client-47-rezultat-komandy-v1-callstat-request
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.2.6"
pdf_section: "3.2.6"
title: "Результат команды v1/callstat/request"
pdf_heading: "3.2.6 Результат команды v1/callstat/request"
pages: "50"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 50"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"50","global_pages":"50"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 170
images: 0
status: extracted
ai-generated: true
---
### 3.2.6. Результат команды v1/callstat/request

> Трассировка: PDF §3.2.6 · сквозные стр. 50 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.50.

routeKey="/stat"

Сообщает о готовности результатов запроса статистики.

Параметры события:

| Параметр | Тип | Описание |
| --- | --- | --- |
| routeKey | string | Тип события |
| data | object |  |
| data[key] | string | Ключ запроса статистики |

Параметр Тип Описание

routeKey string Тип события

data object

data[key] string Ключ запроса статистики

Пример события:

{"routeKey":"/stat","data":{"key":"aIpiDTBCkg0tlaKo/aVIq2eM/1W8SCvxmg+tG2uTLvFw= ="}}
