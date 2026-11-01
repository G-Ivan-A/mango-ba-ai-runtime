---
id: api-server-client-09-korrektnoe-zavershenie-raboty-prilozheni
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "2.2"
pdf_section: "2.2"
title: "Корректное завершение работы приложения пользователя"
pdf_heading: "2.2 Корректное завершение работы приложения пользователя"
pages: "6"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 6"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"6","global_pages":"6"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 178
images: 0
status: extracted
ai-generated: true
---
## 2.2. Корректное завершение работы приложения пользователя

> Трассировка: PDF §2.2 · сквозные стр. 6 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.6.

1) клиентское приложение завершает вебсокет сессию (вкладка браузера закрывается, выход из приложения);

2) клиентское приложение отправляет запрос завершения сессии вебсокета (/v1/session/unregister/) для конкретного пользователя ВАТС

3) Сервис накапливает события о вызовах для конкретного пользователя ВАТС;

4) внешнее приложение сможет в дальнейшем обработать накапливаемые события согласно разделу "Порядок получения пропущенных событий".
