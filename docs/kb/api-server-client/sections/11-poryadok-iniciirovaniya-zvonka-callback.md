---
id: api-server-client-11-poryadok-iniciirovaniya-zvonka-callback
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "2.4"
pdf_section: "2.4"
title: "Порядок инициирования звонка callback"
pdf_heading: "2.4 Порядок инициирования звонка callback"
pages: "7"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 7"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"7","global_pages":"7"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 146
images: 0
status: extracted
ai-generated: true
---
## 2.4. Порядок инициирования звонка callback

> Трассировка: PDF §2.4 · сквозные стр. 7 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.7.

1) у пользователя открыт софтфон или иное настроенное средство приема; 2) выполняется запрос инициации звонка (/v1/callback); 3) на средстве приема (открытого на шаге 1) появляется входящий звонок (с номера, указанного в DESTINATION_NUMBER);

4) пользователь принимает звонок; 5) система инициирует дозвон на указанный номер, начинают приходить события по звонку.
