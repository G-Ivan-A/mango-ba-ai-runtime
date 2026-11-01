---
id: api-server-client-43-sobytiya-zapisi
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.2.2"
pdf_section: "3.2.2"
title: "События записи"
pdf_heading: "3.2.2 События записи"
pages: "46"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 46"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"46","global_pages":"46"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 307
images: 0
status: extracted
ai-generated: true
---
### 3.2.2. События записи

> Трассировка: PDF §3.2.2 · сквозные стр. 46 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.46.

routeKey="/record"

Важно! Для внутренних разговоров события записи не передаются

Параметры события:

| Параметр | Тип | Описание |
| --- | --- | --- |
| routeKey | string | Тип события |
| data | object | Данные события звонка |
| data[record_id] | string | ID записи |
| data[call_id] | string | ID звонка |
| data[url] | string | URL для получения записи |
| data[record_status] | string | Статус записи |

Параметр Тип Описание

routeKey string Тип события

data object Данные события звонка

data[record_id] string ID записи

data[call_id] string ID звонка

data[url] string URL для получения записи

data[record_status] string Статус записи

Пример события:

{ "routeKey": "/call", "data": { "record_id": "MToxMDAxMzAxOToyOTU3MzYzNzU5OjA=", "record_status": "AVAILABLE", "call_id": "MToxMDAxMzAxOTo0NDE6NDI5MzcwMDUw" } }
