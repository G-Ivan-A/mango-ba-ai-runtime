---
id: api-server-client-46-rezultat-komandy-route-async
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.2.5"
pdf_section: "3.2.5"
title: "Результат команды route/async/"
pdf_heading: "3.2.5 Результат команды route/async/"
pages: "49"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 49"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"49","global_pages":"49"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 147
images: 0
status: extracted
ai-generated: true
---
### 3.2.5. Результат команды route/async/

> Трассировка: PDF §3.2.5 · сквозные стр. 49 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.49.

routeKey="/route_result"

| Параметр | Тип | Описание |
| --- | --- | --- |
| routeKey | string | Тип события |
| data | object |  |
| data[transaction_id] | string | ID транзакции |
| data[result] | integer | Код результата |

Параметр Тип Описание

routeKey string Тип события

data object

data[transaction_id] string ID транзакции

data[result] integer Код результата

Пример события:

{"routeKey":"/route_result","data":{"transaction_id":"gsfgsdfgsdfg","result":310 3}}
