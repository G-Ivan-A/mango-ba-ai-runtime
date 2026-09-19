---
id: vpbx-api-175-zavershenie-sessii
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.4.2.2"
pdf_section: "4.4.2.2"
title: "Завершение сессии"
pdf_heading: "4.4.2.2 Завершение сессии"
pages: "231"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 231"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"231","global_pages":"231"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 384
status: extracted
ai-generated: true
---
# 4.4.2.2. Завершение сессии

> Трассировка: PDF §4.4.2.2 · сквозные стр. 231 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.231.

POST /events/user/session_end Событие завершения сессии пользователя. Событие отправляется только для инициатора сессии, пользователи будут получать события завершения только тех сессий, которые они инициировали. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | целое | Да | Код результата |
| 2 | abonent | целое | Да | Идентификатор абонента |
| 3 | session | string | Да | Идентификатор сессии |
| 4 | timestamp | целое | Да | Текущее время сервера в UTC на момент отправки пакета в<br>миллисекундах |

Пример события: POST https://app.mango-office.ru/events/user/session_end vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "result": 1000, "abonent_id": 6576434, "session": "dsftdr6w4e5q34regdf", "timestamp": 10937687345343 }
