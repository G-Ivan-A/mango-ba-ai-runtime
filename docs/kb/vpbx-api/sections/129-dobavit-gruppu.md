---
id: vpbx-api-129-dobavit-gruppu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.2.4"
pdf_section: "3.9.2.4"
title: "Добавить группу"
pdf_heading: "3.9.2.4 Добавить группу"
pages: "170-171"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 170-171"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"170-171","global_pages":"170-171"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 613
status: extracted
ai-generated: true
---
# 3.9.2.4. Добавить группу

> Трассировка: PDF §3.9.2.4 · сквозные стр. 170-171 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.170-171.

POST /vpbx/ab/groups/create/ Метод позволяет добавить группу. Также можно добавить несколько групп, до 500. Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив добавляемых групп, разделитель - запятая «,» |
| 1.1 |  | group_name | string |  | Название группы |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/groups/create/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data": [ { "group_name":"группа 11111" }, { "group_name":"группа 1111112" } ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив добавленных объектов типа Группа |
| 1.1 |  | group_id |  |  | id группы |
| 1.2 |  | group_name | строка |  | Название группы |
| 2 | skipped |  |  | Нет | Массив идентификаторов (начинающихся с 0) строк в<br>исходном массиве data, содержит указатели на элементы<br>входящего массива, которые не были обработаны |

Пример ответа: { "result": [ 1000, 1000 ], "data": [ { "group_id": "10129660", "group_name": "группа 11111" }, { "group_id": "10129661", "group_name": "группа 1111112" } ]}
