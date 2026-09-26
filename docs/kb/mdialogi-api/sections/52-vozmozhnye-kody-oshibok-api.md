---
id: mdialogi-api-52-vozmozhnye-kody-oshibok-api
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "4.2"
pdf_section: "4.2"
title: "Возможные коды ошибок API"
pdf_heading: "4.2 Возможные коды ошибок API"
pages: "59-60"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 59-60"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"59-60","global_pages":"59-60"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 335
status: extracted
ai-generated: true
---
# 4.2. Возможные коды ошибок API

> Трассировка: PDF §4.2 · сквозные стр. 59-60 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.59-60.

В системе Манго Диалоги используются два типа ошибок: 1. Ошибки API — возникают при обработке запроса API (неверные параметры, ошибки авторизации, состояние сессии и другие ошибки обработки запроса). 2. Ошибки доставки сообщений — возникают при отправке сообщений через текстовые каналы коммуникации (WhatsApp, Telegram, VK, Email, Avito, MAX и другие каналы). Ошибки API возвращаются в ответе на HTTP-запрос. Ошибки доставки сообщений передаются во внешнюю систему через вебхук: Манго Диалоги. Справочник по API | Версия от 10.06.2026 Код ошибки передается в параметре:

|  | /events/cc/md/session/chat/on_error_message |  |
| --- | --- | --- |

Поле ошибки передается в параметре:

|  | error |  |
| --- | --- | --- |
