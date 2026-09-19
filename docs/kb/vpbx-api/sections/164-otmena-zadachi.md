---
id: vpbx-api-164-otmena-zadachi
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.3.6"
pdf_section: "4.3.6"
title: "Отмена задачи"
pdf_heading: "4.3.6 Отмена задачи"
pages: "223"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 223"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"223","global_pages":"223"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 377
status: extracted
ai-generated: true
---
# 4.3.6. Отмена задачи

> Трассировка: PDF §4.3.6 · сквозные стр. 223 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.223.

POST /cc/task/cancel Метод предназначен для отмены ранее поставленной задачи. Параметры запроса:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | task_id | Массив | Да | Массив из нескольких ID |

Пример запроса: POST https://app.mango-office.ru/cc/task/cancel vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "product_id":300023344, "task_id":[45594,45584,45374] } В ответе содержатся следующие данные:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Целое | Да | Код результата |
| 2 | data | Массив | Нет | Массив задач с результатом по каждой из задач |

Пример ответа: { "result": 1000, "data": [ { "task_id": 45594, "result": 5000 }, { "task_id": 45584, "result": 5000 }, { "task_id": 45374, "result": 1000 } ]}
