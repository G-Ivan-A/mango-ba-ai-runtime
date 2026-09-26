---
id: vpbx-api-116-vyklyuchenie-zapreta-na-vse-ishodyaschie
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.8.3.8"
pdf_section: "3.8.3.8"
title: "Выключение запрета на все исходящие коммуникации"
pdf_heading: "3.8.3.8 Выключение запрета на все исходящие коммуникации"
pages: "157"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 157"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"157","global_pages":"157"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 364
status: extracted
ai-generated: true
---
# 3.8.3.8. Выключение запрета на все исходящие коммуникации

> Трассировка: PDF §3.8.3.8 · сквозные стр. 157 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.157.

POST /vpbx/outbound_blacklist/disable Выключение опции запрета на исходящие коммуникации. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/outbound_blacklist/disable vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие код результата:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>● 1000 - команда выполнена успешно;<br>● 5000 - внутренняя ошибка сервера. |

Пример ответа: { "result": 1000 }
