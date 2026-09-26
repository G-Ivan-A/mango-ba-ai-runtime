---
id: vpbx-api-182-poluchenie-spiska-dokumentov-sdelki
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.5.6"
pdf_section: "4.5.6"
title: "Получение списка документов сделки"
pdf_heading: "4.5.6 Получение списка документов сделки"
pages: "242-243"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 242-243"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"242-243","global_pages":"242-243"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 685
status: extracted
ai-generated: true
---
# 4.5.6. Получение списка документов сделки

> Трассировка: PDF §4.5.6 · сквозные стр. 242-243 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.242-243.

POST /cc/deal/documents.list Назначение: получение списка документов сделки. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | deal_id | Число | Да | Уникальный номер сделки |

Пример запроса: POST https://app.mango-office.ru/cc/deal/documents.list vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "deal_id":160578 } В результате обработки запроса, формируются и передаются JSON-данные, содержащие код результата result (см. Список кодов результата) и следующие параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
| 1 | deal_id |  | Число | Да | Уникальный номер сделки |
| 2 | documents |  | Массив | Да | Массив документов сделки |
| 2.1 |  | create | Дата | Да | Дата создания документа |
| 2.2 |  | abonent_id | Число | Да | Сотрудник, создавший документ |
| 2.3 |  | file_id | Число | Да | Уникальный номер документа |
| 2.4 |  | blob_type | Строка | Да | Тип документа |
| 2.5 |  | blob_size_kb | Строка | Да | Размер документа |
| 2.6 |  | blob_name | Строка | Да | Наименование документа |

Пример ответа: { "result": 1000, "deal_id": 160578, "documents": [ { "create": "2021-07-19 15:50:06", "abonent_id": 160578, "file_id": 2653, "blob_name": "image.png", "blob_type": "image/png", "blob_size_kb": 109 }, { "create": "2020-10-16 10:24:28", "abonent_id": 10094537, "file_id": 2528, "blob_name": "gkdyltpqsk552.jpg", "blob_type": "image/jpeg", "blob_size_kb": 1212 }, ] }
