---
id: vpbx-api-181-poluchenie-spiska-polzovatelskih-poley
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.5.5"
pdf_section: "4.5.5"
title: "Получение списка пользовательских полей"
pdf_heading: "4.5.5 Получение списка пользовательских полей"
pages: "239-242"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 239-242"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"239-242","global_pages":"239-242"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1355
status: extracted
ai-generated: true
---
# 4.5.5. Получение списка пользовательских полей

> Трассировка: PDF §4.5.5 · сквозные стр. 239-242 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.239-242.

POST /cc/deal/custom_fields.list Назначение: получение списка созданных на продукте пользовательских полей для сделок. Параметры: нет Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. В результате обработки запроса, формируются и передаются JSON-данные, содержащие код результата result (см. Список кодов результата) и объект deal (обязательный):

| № | Параметр | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | custom_type_id | Число | Да | Идентификатор пользовательского поля |
| 2 | type | Список | Нет | Тип пользовательского поля. Значения списка:<br>● text;<br>● enum;<br>● multi_enum; |

| № | Параметр | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
|  |  |  |  | ● address;<br>● int;<br>● money;<br>● date;<br>● check_box;<br>● url;<br>● input_field;<br>● point_member |
| 3 | name | Строка | Да | Наименование пользовательского поля |
| 4 | required | Булево | Да | Флаг обязательности заполнения |
| 5 | api_only | Булево | Да | Флаг доступности пользовательского поля только в<br>режиме чтения |
| 6 | check_mode | Перечисление | Да | Способ сравнения, указанный в настройках<br>пользовательского поля. Значения списка:<br>● more;<br>● equal;<br>● less;<br>● between |
| 7 | check_length | Строка | Да | Значения для проверки на длину поля или на значение<br>– слева |
| 8 | check_length_b | Строка | Да | На значение – справа |
| 9 | currency | Перечисление | Да | Тип валюты. Значения списка:<br>● rub;<br>● usd;<br>● eu |
| 10 | list_items |  | Да | Для пользовательского поля типа - список, значения<br>списка |

Пример ответа: { "result": 1000, "custom_fields": [ { "custom_type_id": 702, "type": "enum", "name": "Выпадающий список ", "required": false, "api_only": false, "check_mode": null, "check_length": null, "check_length_b": null, "currency": null, "list_items": [ { "custom_type_enum_id": 895, "order": 0, "value": "1" }, { "custom_type_enum_id": 896, "order": 1, "value": "2" }

| ]<br>},<br>{ |
| --- |
| "custom_type_id": 703,<br>"type": "multi_enum", |
| "name": "Выпад. список (мульти)",<br>"required": false, |
| "api_only": false,<br>"check_mode": null,<br>"check_length": null, |
| "check_length_b": null,<br>"currency": null,<br>"list_items": [<br>{ |
| "custom_type_enum_id": 897,<br>"order": 0,<br>"value": "1" |
| },<br>{ |
| "custom_type_enum_id": 898,<br>"order": 1,<br>"value": "2" |
| },<br>{<br>"custom_type_enum_id": 899, |
| "order": 2,<br>"value": "3"<br>}<br>]<br>},<br>{<br>"custom_type_id": 705,<br>"type": "int",<br>"name": "Число",<br>"required": false,<br>"api_only": false,<br>"check_mode": "less",<br>"check_length": "10",<br>"check_length_b": null, |
| "currency": null,<br>"list_items": null<br>}, |
| {<br>"custom_type_id": 714,<br>"type": "date",<br>"name": "дата",<br>"required": false,<br>"api_only": false,<br>"check_mode": null,<br>"check_length": null,<br>"check_length_b": null,<br>"currency": null,<br>"list_items": null<br>},<br>{<br>"custom_type_id": 715,<br>"type": "check_box",<br>"name": "флаг(да, нет)",<br>"required": false, |
| "api_only": false,<br>"check_mode": null, |
| "check_length": null,<br>"check_length_b": null, |

"currency": null, "list_items": null }, { "custom_type_id": 716, "type": "url", "name": "ссыль", "required": false, "api_only": false, "check_mode": "more", "check_length": "5", "check_length_b": null, "currency": null, "list_items": null }, ] }
