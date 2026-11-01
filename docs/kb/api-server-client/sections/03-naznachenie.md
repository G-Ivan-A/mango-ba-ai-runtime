---
id: api-server-client-03-naznachenie
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "1.1"
pdf_section: "1.1"
title: "Назначение"
pdf_heading: "1.1 Назначение"
pages: "4"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 4"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"4","global_pages":"4"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 277
images: 0
status: extracted
ai-generated: true
---
## 1.1. Назначение

> Трассировка: PDF §1.1 · сквозные стр. 4 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.4.

API «Сервер-клиент» (далее по тексту – Сервис) позволяет внешним приложениям:

 взаимодействовать с Виртуальной АТС MANGO OFFICE (далее по тексту – ВАТС) отдельным пользователям, независимо от других пользователей, т.е. каждое клиентское приложение получает информацию только о звонках данного пользователя;

 сохраняет информацию о звонках и событиях пользователя, если пользователь недоступен (к примеру, клиентское приложение недоступно);

 и предоставляет сохраненную информацию для обработки клиентскому приложению. Сервис позволяет реализовывать решения, построенные по принципу «сервер-клиент» (в отличие от API ВАТС для внешних приложений, которое построено по принципу «сервер-сервер»).
