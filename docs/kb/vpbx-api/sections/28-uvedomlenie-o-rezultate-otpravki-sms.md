---
id: vpbx-api-28-uvedomlenie-o-rezultate-otpravki-sms
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.1.3"
pdf_section: "3.1.3"
title: "Уведомление о результате отправки SMS"
pdf_heading: "3.1.3 Уведомление о результате отправки SMS"
pages: "22"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 22"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"22","global_pages":"22"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 388
status: extracted
ai-generated: true
---
# 3.1.3. Уведомление о результате отправки SMS

> Трассировка: PDF §3.1.3 · сквозные стр. 22 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.22.

POST https://external-system.com/events/sms Уведомление содержит информацию о статусе доставки SMS конечному адресату. Параметры уведомления:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string |  | Идентификатор команды внешней системы, в результате<br>которой появился вызов (строка не более 128 байт).<br>Уникальность строки для внешней системы гарантируется<br>внешней системой |
| 2 | timestamp | integer |  | Время события UTC+3 |
| 3 | reason | integer |  | Результат отправки SMS (см. "Список кодов результатов",<br>коды 43хх) |

Пример уведомления: POST https://external-system.com/events/sms HEADERS: content-type: application/x-www-form-urlencoded BODY: vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":1sjdhjh1231, "timestamp":"1399906980", "reason":"1000" }
