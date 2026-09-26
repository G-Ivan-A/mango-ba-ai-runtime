---
id: vpbx-api-184-poluchenie-spiska-voronok
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.5.8"
pdf_section: "4.5.8"
title: "Получение списка воронок"
pdf_heading: "4.5.8 Получение списка воронок"
pages: "244-245"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 244-245"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"244-245","global_pages":"244-245"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 974
status: extracted
ai-generated: true
---
# 4.5.8. Получение списка воронок

> Трассировка: PDF §4.5.8 · сквозные стр. 244-245 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.244-245.

POST /cc/deal/funnels.list Назначение: Получение списка воронок и этапов. Параметры: Нет Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | result |  |  | Целое | Да | Код результата |
| 2 | sales_funnels |  |  |  |  |  |
| 2.1 |  | sales_fun<br>nel_id |  | Число | Да | Уникальный номер этапа воронки |
| 2.2 |  | name |  | Строка | Да | Наименование воронки |
| 2.3 |  | deleted |  | Булево | Да | Признак удаленной воронки |
| 2.4 |  | steps |  | Массив | Да | Данные об этапах в воронке |
| 2.4.1 |  |  | step_id | Число | Да | Уникальный номер этапа воронки |
| 2.4.2 |  |  | name | Строка | Да | Наименование этапа |

Пример ответа: { "result": 1000, "sales_funnels": [ { "sales_funnel_id": 778, "name": "Новая воронка2222", "deleted": true, "steps": null }, {

| "sales_funnel_id": 779,<br>"name": "Новая воронка123",<br>"deleted": false, |
| --- |
| "steps": [<br>{ |
| "step_id": 3662,<br>"name": "Проявлен интерес" |
| },<br>{<br>"step_id": 3663, |
| "name": "Принятие решения"<br>},<br>{<br>"step_id": 3664, |
| "name": "Оплата"<br>}<br>] |
| },<br>{ |
| "sales_funnel_id": 148,<br>"name": "НеСтандартная воронка",<br>"deleted": false, |
| "steps": [<br>{<br>"step_id": 1402, |
| "name": "Переговоры и КП"<br>},<br>{<br>"step_id": 1403,<br>"name": "Принятие решения"<br>},<br>{<br>"step_id": 1404,<br>"name": "Подписание договора"<br>},<br>{<br>"step_id": 1405,<br>"name": "Оплата"<br>}, |
| {<br>"step_id": 1406,<br>"name": "23 воронка" |
| },<br>{<br>"step_id": 1407,<br>"name": "24 воронка"<br>}<br>]<br>},<br>{<br>"sales_funnel_id": 771,<br>"name": "Новая воронка Нов",<br>"deleted": true,<br>"steps": null<br>},<br>{<br>"sales_funnel_id": 777,<br>"name": "На удаление",<br>"deleted": true, |
| "steps": null<br>} |
| ]} |
