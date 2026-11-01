---
id: api-server-client-12-poryadok-proigryvaniya-zapisi
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "2.5"
pdf_section: "2.5"
title: "Порядок проигрывания записи"
pdf_heading: "2.5 Порядок проигрывания записи"
pages: "7"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 7"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"7","global_pages":"7"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 165
images: 0
status: extracted
ai-generated: true
---
## 2.5. Порядок проигрывания записи

> Трассировка: PDF §2.5 · сквозные стр. 7 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.7.

1) осуществляется запись звонка более 6 секунд; 2) после получения события записи (/record) со статусом AVAILABLE можно сохранить значение url для скачивания данной записи разговора;

3) ВАТС формирует запись разговора, доступность записи может занимать время - более 5 минут в часы нагрузки;

4) рекомендуется хранить ссылку на запись, а не саму запись; 5) пользователь пытается прослушать запись - надо выполнить запрос по сохраненной ссылке.
