---
id: vpbx-api-130-redaktirovat-gruppu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.2.5"
pdf_section: "3.9.2.5"
title: "Редактировать группу"
pdf_heading: "3.9.2.5 Редактировать группу"
pages: "171-172"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 171-172"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"171-172","global_pages":"171-172"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 668
status: extracted
ai-generated: true
---
# 3.9.2.5. Редактировать группу

> Трассировка: PDF §3.9.2.5 · сквозные стр. 171-172 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.171-172.

POST /vpbx/ab/groups/update Метод позволяет редактировать группу. Также можно редактировать несколько групп, до 500. Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив добавленных объектов типа Группа |
| 1.1 |  | group_id |  |  | id группы |
| 1.2 |  | group_name | строка |  | Название группы |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/groups/update vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data": [ { "group_id":"10433913", "group_name":"компания 11122" }, { "group_id":"10433914", "group_name":"компания 11123" } ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  | Да | Код результата |
| 2 | data |  |  |  | Массив измененных объектов типа Группа |
| 2.1 |  | group_id |  |  | id группы |
| 2.2 |  | group_name | строка |  | Название группы |
| 3 | skipped |  |  | Нет | Массив идентификаторов (начинающихся с 0) строк в<br>исходном массиве data, содержит указатели на элементы<br>входящего массива, которые не были обработаны |

Пример ответа: { "result": [ 1000, 1000 ], "data": [ { "group_id": "10433913", "group_name": "компания 11122" }, { "group_id": "10433914", "group_name": "компания 11123" } ]}
