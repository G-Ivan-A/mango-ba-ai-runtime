---
id: mdialogi-api-15-limity-kolichestva-zaprosov-k-api
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "2.3.5"
pdf_section: "2.3.5"
title: "Лимиты количества запросов к API"
pdf_heading: "2.3.5 Лимиты количества запросов к API"
pages: "14-15"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 14-15"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"14-15","global_pages":"14-15"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 549
status: extracted
ai-generated: true
---
# 2.3.5. Лимиты количества запросов к API

> Трассировка: PDF §2.3.5 · сквозные стр. 14-15 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.14-15.

В API существуют ограничения на максимальное число запросов в секунду. Не гарантируется обработка запросов сверх обозначенных лимитов. Если установленный лимит превышен, то обработка запросов, поступающих к API, будет временно остановлена и вы увидите следующее сообщение:

| { |
| --- |
| "name": "Service Unavailable", |
| "message": "Rate limit exceeded.", |
| "code": 0, |
| "status": 429 |
| } |

Если ошибка 429 НЕ возникала, значит лимит количества запросов НЕ превышен. Устанавливаются следующие лимиты запросов в секунду:

| Запрос Максимальное число запросов / в секунду |  |
| --- | --- |
|  |  |
| По вашей ВАТС (по продукту) | 10/1 |
|  |  |
| Всего запросов к API | 100/1 |
| Дополнительные ограничения на вызов определенных методов |  |
|  |  |
| Загрузка истории чата (/cc/md/session/chat/history) |  |
|  |  |
| По вашей ВАТС (по продукту) | 4/1 |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| Всего запросов к API | 10/1 |
| --- | --- |
|  |  |
| Отправить сообщение оператора к клиенту (/cc/md/session/chat/send_message) |  |
| По вашей ВАТС (по продукту) | 4/1 |
|  |  |
| Всего запросов к API | 10/1 |
