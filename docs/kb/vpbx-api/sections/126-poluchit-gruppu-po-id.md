---
id: vpbx-api-126-poluchit-gruppu-po-id
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.2.1"
pdf_section: "3.9.2.1"
title: "Получить группу по id"
pdf_heading: "3.9.2.1 Получить группу по id"
pages: "166-167"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 166-167"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"166-167","global_pages":"166-167"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 451
status: extracted
ai-generated: true
---
# 3.9.2.1. Получить группу по id

> Трассировка: PDF §3.9.2.1 · сквозные стр. 166-167 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.166-167.

POST /vpbx/ab/group Метод возвращает информацию о группе. Работа с группами доступна в Контакт-центре. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | group_id |  |  | id группы |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/group vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "group_id":"10129645" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с<br>уровнями<br>вложенности |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  |  | Код результата |
| 2 | data |  |  |  |  |
|  |  | group_id | string |  | Идентификатор группы |
| 4 |  | group_name | string |  | Название группы |

Пример ответа: { "result": 1000, "data": { "group_id": "10129645", "group_name": "NAMER" } }
