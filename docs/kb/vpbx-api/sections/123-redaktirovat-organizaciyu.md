---
id: vpbx-api-123-redaktirovat-organizaciyu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.1.5"
pdf_section: "3.9.1.5"
title: "Редактировать организацию"
pdf_heading: "3.9.1.5 Редактировать организацию"
pages: "164-165"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 164-165"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"164-165","global_pages":"164-165"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 695
status: extracted
ai-generated: true
---
# 3.9.1.5. Редактировать организацию

> Трассировка: PDF §3.9.1.5 · сквозные стр. 164-165 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.164-165.

POST /vpbx/ab/organizations/update Метод позволяет редактировать организацию. Также можно редактировать несколько организаций, до 500. Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив редактируемых организаций, разделитель «;» |
| 1.1 |  | org_id |  |  | id организации |
|  |  | org_name | string |  | Название организации |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/organizations/update vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data": [ { "org_id":"10433913", "org_name":"компания 11122" }, { "org_id":"10433914", "org_name":"компания 11123" } ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- |

|  | 1 | 2 |  | тель-<br>ный |  |
| --- | --- | --- | --- | --- | --- |
|  | Result |  |  | Да | Код результата |
| 1 | data |  |  |  | Массив измененных объектов типа Организация |
| 1.1 |  | org_id |  |  | id организации |
|  |  | org_name | string |  | Название организации |
| 2 | skipped |  |  | Нет | Массив идентификаторов (начинающихся с 0) строк в<br>исходном массиве data, содержит указатели на элементы<br>входящего массива, которые не были обработаны |

Пример ответа: { "result": [ 1000, 1000 ], "data": [ { "org_id": "10433913", "org_name": "компания 11122" }, { "org_id": "10433914", "org_name": "компания 11123" } ]}
