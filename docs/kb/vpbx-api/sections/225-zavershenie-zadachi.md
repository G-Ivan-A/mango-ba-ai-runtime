---
id: vpbx-api-225-zavershenie-zadachi
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.9.1.5"
pdf_section: "4.9.1.5"
title: "Завершение задачи"
pdf_heading: "4.9.1.5 Завершение задачи"
pages: "313-314"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 313-314"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"313-314","global_pages":"313-314"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 402
status: extracted
ai-generated: true
---
# 4.9.1.5. Завершение задачи

> Трассировка: PDF §4.9.1.5 · сквозные стр. 313-314 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.313-314.

POST /cc/task/done Позволяет завершать задачи. Параметры метода:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | task_id | Массив | Да | Массив из нескольких ID |

Пример запроса: POST https://app.mango-office.ru/cc/task/done vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "product_id":300023344, "task_id":[45594,45584,45374] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Целое | Да | Код результата |
| 2 | data [] | Объект | Нет | Массив задач с результатом по каждой из задач |

Пример ответа: { "result": 1000, "data": [ { "task_id": 45594, "result": 5000 }, { "task_id": 45584, "result": 5000 }, { "task_id": 45374, "result": 1000 } ]}
