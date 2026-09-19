---
id: vpbx-api-115-vklyuchenie-zapreta-na-vse-ishodyaschie
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.8.3.7"
pdf_section: "3.8.3.7"
title: "Включение запрета на все исходящие коммуникации"
pdf_heading: "3.8.3.7 Включение запрета на все исходящие коммуникации"
pages: "156"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 156"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"156","global_pages":"156"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 354
status: extracted
ai-generated: true
---
# 3.8.3.7. Включение запрета на все исходящие коммуникации

> Трассировка: PDF §3.8.3.7 · сквозные стр. 156 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.156.

POST /vpbx/outbound_blacklist/enable Включение опции запрета на исходящие коммуникации. Примечание. Для вызова метода требуется в ВАТС наличие подключенной услуги "Черный и белый списки". Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/outbound_blacklist/enable vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие код ошибки:

| Параметры | Тип | Обяза-<br>тель-<br>ный |
| --- | --- | --- |
| Result |  | Да |

Пример ответа: { "result": 1000 }
