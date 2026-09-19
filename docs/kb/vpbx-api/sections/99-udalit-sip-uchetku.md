---
id: vpbx-api-99-udalit-sip-uchetku
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.21"
pdf_section: "3.7.21"
title: "Удалить sip-учетку"
pdf_heading: "3.7.21 Удалить sip-учетку"
pages: "142-143"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 142-143"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"142-143","global_pages":"142-143"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 404
status: extracted
ai-generated: true
---
# 3.7.21. Удалить sip-учетку

> Трассировка: PDF §3.7.21 · сквозные стр. 142-143 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.142-143.

POST /vpbx/sip/delete Метод позволяет удалить редактировать sip учетку. Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | sip_id | integer |  | ID SIP-учётки, обязательное |

Пример запроса: POST https://app.mango-office.ru/vpbx/sip/delete vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "sip_id":"100111111" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31XX - неверные параметры;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера. |

Пример ответа: { "result": 1000 }
