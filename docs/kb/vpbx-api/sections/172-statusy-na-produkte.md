---
id: vpbx-api-172-statusy-na-produkte
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.4.1.4"
pdf_section: "4.4.1.4"
title: "Статусы на продукте"
pdf_heading: "4.4.1.4 Статусы на продукте"
pages: "229-230"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 229-230"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"229-230","global_pages":"229-230"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 616
status: extracted
ai-generated: true
---
# 4.4.1.4. Статусы на продукте

> Трассировка: PDF §4.4.1.4 · сквозные стр. 229-230 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.229-230.

POST /cc/get_statuses Команда предназначена для получения всех статусов на продукте и их характеристик. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример события: POST https://app.mango-office.ru/cc/get_statuses vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  | Да | Код результата |
| 2 | id | целое | Да | Идентификатор статуса |
| 3 | name | string | Нет | Имя статуса |
| 4 | color | string | Нет | Цвет в hex (пример: #999999) |
| 5 | parent | целое | Нет | id родительского статуса |
| 6 | deleted | boolean | Да | Флаг удален уже статус; |
| 7 | order | целое | Да | Значения для сортировки |
| 8 | description | string | Нет | Описание статуса |
| 9 | status_alias | string | Нет | Псевдоним/синоним статуса. |

Пример ответа: { "result":1000, "statuses": [ { "id": 1, "name": "На линии", "color": "#999999", "deleted": false, "order": 1, "description": "desc" }, { "id": 107, "name": "custom status 1", "color": "#222222", "parent": 1, "point_id": 10000006, "deleted": false, "order": 600, "description": "" "status_alias": qwe123, } ]}
