---
id: mdialogi-api-62-otpravlenie-kaskada-soobscheniy-cherez-w
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "6.1"
pdf_section: "6.1"
title: "Отправление каскада сообщений через WhatsApp и SMS"
pdf_heading: "6.1 Отправление каскада сообщений через WhatsApp и SMS"
pages: "80"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 80"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"80","global_pages":"80"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 162
status: extracted
ai-generated: true
---
# 6.1. Отправление каскада сообщений через WhatsApp и SMS

> Трассировка: PDF §6.1 · сквозные стр. 80 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.80.

POST /cc/send_text_message Основные сведения Метод позволяет выполнять массовую рассылку текстовых сообщений Клиентам, в зависимости от правил, которые определяете вы. Рассылка выполняется по каналам WhatsApp (далее по тексту – WA) и SMS.
