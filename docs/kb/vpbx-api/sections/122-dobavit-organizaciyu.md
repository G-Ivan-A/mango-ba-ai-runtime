---
id: vpbx-api-122-dobavit-organizaciyu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.1.4"
pdf_section: "3.9.1.4"
title: "Добавить организацию"
pdf_heading: "3.9.1.4 Добавить организацию"
pages: "163-164"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 163-164"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"163-164","global_pages":"163-164"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 688
status: extracted
ai-generated: true
---
# 3.9.1.4. Добавить организацию

> Трассировка: PDF §3.9.1.4 · сквозные стр. 163-164 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.163-164.

POST /vpbx/ab/organizations/create Метод позволяет добавить организацию. Также можно добавить несколько организаций, до 500. Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив добавляемых организаций, разделитель «;»: |
| 1.1 |  | org_name | string |  | Название организации |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/organizations/create vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data": [ { "org_name":"компания 11112" }, { "org_name":"компания 11113" } ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  | Да | Код результата |
| 2 | data |  |  |  | Массив добавленных объектов типа Организация |
| 2.1 |  | org_id |  |  | id организации |

| № | Параметры |  | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- | --- |
| 2.2 |  | org_name | string |  | Название организации |
| 3 | skipped |  |  | Нет | Массив идентификаторов (начинающихся с 0) строк в исходном<br>массиве data, содержит указатели на элементы входящего массива,<br>которые не были обработаны |

Пример ответа: { "result": [ 1000, 1000 ], "data": [ { "org_id": "10433913", "org_name": "компания 11112" }, { "org_id": "10433914", "org_name": "компания 11113" } ]}
