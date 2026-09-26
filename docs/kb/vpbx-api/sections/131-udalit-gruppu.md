---
id: vpbx-api-131-udalit-gruppu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.2.6"
pdf_section: "3.9.2.6"
title: "Удалить группу"
pdf_heading: "3.9.2.6 Удалить группу"
pages: "172-173"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 172-173"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"172-173","global_pages":"172-173"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 397
status: extracted
ai-generated: true
---
# 3.9.2.6. Удалить группу

> Трассировка: PDF §3.9.2.6 · сквозные стр. 172-173 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.172-173.

POST /vpbx/ab/groups/delete Метод позволяет удалить группу. Также можно удалить несколько групп, до 500. Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив удаляемых групп, разделитель «;» |
| 1.1 |  | group_id |  |  | id группы |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/groups/delete vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data": [ "10433913", "10433914", "10000" ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  | Да | Код результата |

Пример ответа: { "result": 1000 }
