---
id: api-server-client-13-poryadok-perevoda-na-otvetstvennogo-sotr
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "2.6"
pdf_section: "2.6"
title: "Порядок перевода на ответственного сотрудника"
pdf_heading: "2.6 Порядок перевода на ответственного сотрудника"
pages: "8"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 8"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"8","global_pages":"8"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 207
images: 0
status: extracted
ai-generated: true
---
## 2.6. Порядок перевода на ответственного сотрудника

> Трассировка: PDF §2.6 · сквозные стр. 8 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.8.

1) при получении входящего звонка на ВАТС Сервис отправляет событие телефонии (/ivr) в статусе APPEARED случайному пользователю, находящемуся в сессии вебсокет;

2) получено событие с routeKey="/ivr"; 3) внешнее приложение осуществляет поиск ответственного по номеру телефона в своей системе хранения данных;

4) если ответственный найден, то отправляется запрос «Перевести на сотрудника» (/v1/route) на внутренний номер ответственного;

5) асинхронно по вебсокету приходит событие результата выполнения ВАТС перевода вызова (/route_result).
