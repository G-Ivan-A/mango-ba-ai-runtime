---
id: vpbx-api-119-poluchit-organizaciyu-po-id
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.1.1"
pdf_section: "3.9.1.1"
title: "Получить организацию по id"
pdf_heading: "3.9.1.1 Получить организацию по id"
pages: "157-159"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 157-159"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"157-159","global_pages":"157-159"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 463
status: extracted
ai-generated: true
---
# 3.9.1.1. Получить организацию по id

> Трассировка: PDF §3.9.1.1 · сквозные стр. 157-159 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.157-159.

POST /vpbx/ab/organization Метод возвращает информацию об организации. Работа с организациями доступна в Контакт- центре. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | org_id |  |  | id организации |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/organization vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "org_id":"10182085" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнями<br>вложенности |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  | Да | Код результата |
| 2 | data |  |  |  |  |
|  |  | org_id |  |  | id организации |
|  |  | org_name | string |  | Название организации |

Пример ответа: { "result: 1000, "data: { "org_id: "10182085", "org_name: "компания 2" } }
