---
id: mdialogi-api-18-obschee
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "0"
pdf_section: "2.3.7"
title: "Общее"
pdf_heading: "Общее"
pages: "16-17"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 16-17"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"16-17","global_pages":"16-17"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 459
status: extracted
ai-generated: true
---
# Общее

> Трассировка: PDF §2.3.7 · сквозные стр. 16-17 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.16-17.

Данные, которыми обмениваются системы, как правило, передаются в теле POST-запроса в формате JSON. Каждый запрос должен содержать обязательные параметры: - vpbx_api_key — уникальный код вашей ВАТС; - sign — электронная подпись запроса; - json — JSON-строка с данными запроса. Важно! Подписываются все запросы — как от внешней системы, так и от API. Параметр json Параметр json представляет собой JSON-строку с данными запроса. Рекомендуется формировать JSON программно, без лишних пробелов и переносов строк. Пример:

| { |
| --- |
| "id": "123qwerty", |
| "channel_id": 123, |
| "social_user_id": "123ytrewqAns", |
| "message": "Здравствуйте!", |
| "abonent_id": 5555555 |
| } |

Важно! Примеры в данном документе будут форматироваться с добавлением пробелов и переводов строк для лучшей читаемости. vpbx_api_key Уникальный код вашей ВАТС. Используется для идентификации внешней системы. Манго Диалоги. Справочник по API | Версия от 10.06.2026 Пример значения: 123qwerty123qwerty Передается в каждом запросе в параметре vpbx_api_key
