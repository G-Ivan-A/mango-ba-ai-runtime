---
id: api-server-client-06-obrabotka-oshibok
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "1.4"
pdf_section: "1.4"
title: "Обработка ошибок"
pdf_heading: "1.4 Обработка ошибок"
pages: "5"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 5"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"5","global_pages":"5"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 123
images: 0
status: extracted
ai-generated: true
---
## 1.4. Обработка ошибок

> Трассировка: PDF §1.4 · сквозные стр. 5 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.5.

В случае некорректных данных или при возникновении ошибок обработки данных любой из методов Сервиса возвращает один из следующих ответов:

● 200 - успешное выполнение ● 4хх - неверный запрос или отсутствие в ответе данных ● 500 - ошибка сервера Возможные коды ошибок Сервиса являются подмножеством кодов результатов (см. "Список кодов результатов").
