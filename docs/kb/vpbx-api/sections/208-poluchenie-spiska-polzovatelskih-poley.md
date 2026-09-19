---
id: vpbx-api-208-poluchenie-spiska-polzovatelskih-poley
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.20"
pdf_section: "4.6.20"
title: "Получение списка пользовательских полей"
pdf_heading: "4.6.20 Получение списка пользовательских полей"
pages: "291-292"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 291-292"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"291-292","global_pages":"291-292"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 763
status: extracted
ai-generated: true
---
# 4.6.20. Получение списка пользовательских полей

> Трассировка: PDF §4.6.20 · сквозные стр. 291-292 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.291-292.

POST /vpbx/custom-type/list Метод позволяет получить список пользовательских полей кампании ИО на продукте. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/custom-type/list vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | status |  |  | Число | Да | Код результата |
| 2 | result [] |  |  | Массив<br>объектов | Да |  |
| 2.1 |  | id |  | Число | Да | ID пользовательского поля |

| 2.2 |  | order |  | Число | Да | Порядковый номер пользовательского<br>поля |
| --- | --- | --- | --- | --- | --- | --- |
| 2.3 |  | name |  | Строка | Да | Наименование пользовательского поля |
| 2.4 |  | field_type |  | Строка | Да | Тип пользовательского поля (input_field,<br>enum, multi_enum, address, int, money,<br>,date, check_box, url, text, point_member) |
| 2.5 |  | props |  | Строка | Нет | Дополнительные параметры<br>пользовательских полей |
|  |  |  | show_master_io | Булево | Нет | Показывать в карточке обращения |
|  |  |  | show_member | Булево | Нет | Показывать в мастере создания<br>компании |

Пример ответа: { "result": [ { "id": 5908, "order": 1, "name": "Город", "field_type":"text", "props": { "show_master_io": true, "show_member": true } }, { "id": 5915, "order": 3, "name": "Должность", "field_type":"text", "props": { "show_master_io": false, "show_member": false } } ], "status": 200 }
