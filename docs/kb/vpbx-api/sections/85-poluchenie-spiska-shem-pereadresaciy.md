---
id: vpbx-api-85-poluchenie-spiska-shem-pereadresaciy
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.9"
pdf_section: "3.7.9"
title: "Получение списка схем переадресаций"
pdf_heading: "3.7.9 Получение списка схем переадресаций"
pages: "124-126"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 124-126"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"124-126","global_pages":"124-126"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1118
status: extracted
ai-generated: true
---
# 3.7.9. Получение списка схем переадресаций

> Трассировка: PDF §3.7.9 · сквозные стр. 124-126 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.124-126.

POST /vpbx/schemas Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | trunks_numbers | строка |  | Номер sip-trunk'а |

В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнем<br>вложенности |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  |  | Код результата:<br>● 1000 - удачное выполнение;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера; |
| 2 | data |  |  | Да |  |
| 2.1 |  | schema_id: | integer | Да | ID-номер схемы |
| 2.2 |  | Name | string |  | Название схемы (указывается в ЛК) |
| 2.3 |  | description | string |  | Описание схемы (указывается в ЛК) |
| 2.4 |  | incominglines | array<br>[line_id,line_id,..] |  | Массив связанных со схемой<br>входящих линий, с указанием line_id; |
| 2.5 |  | sip_trunks_numbers | array<br>[trunk_number_id,tr |  | Массив связанных со схемой sip-<br>trunk'ов, с указанием |

| № | Параметры с уровнем<br>вложенности |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- |
|  |  |  | unk_number_id,..] |  | trunk_number_id_id: ID схемы<br>переадресации |

Примеры. Пример 1. Запрос без указания номера sip_trunks: Запрос: POST https://app.mango-office.ru/vpbx/schemas vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } Ответ: { "result": 1000, "data": [ { "schema_id": 11004852, "name": "dd", "description": null, "incominglines": [] }, { "schema_id": 11004848, "name": "H2407кирили", "description": "", "incominglines": [ 300049195, 300049196 ] }, { "schema_id": 11004849, "name": "Новая схема line73895", "description": null, "incominglines": [ 300052347 ] }, { "schema_id": 11003886, "name": "По умолчанию", "description": null, "incominglines": [] } ] } Пример 2. Запрос с указаним номера sip_trunks: Запрос: POST https://app.mango-office.ru/vpbx/schemas vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "ext_fields": [ "trunks_numbers" ] } Ответ: { "result": 1000, "data": [ { "schema_id": 11004852, "name": "dd", "description": null, "incominglines": [ 300052347, 300049196 ], "sip_trunks_numbers": [ 786 ] }, { "schema_id": 11004848, "name": "H2407кирили", "description": "", "incominglines": [], "sip_trunks_numbers": [ 829 ] }, { "schema_id": 11004849, "name": "Новая схема line73895", "description": null, "incominglines": [ 300049195 ], "sip_trunks_numbers": [] }, { "schema_id": 11003886, "name": "По умолчанию", "description": null, "incominglines": [], "sip_trunks_numbers": [ 796, 833, 832, 831, 830 ] } ]}
