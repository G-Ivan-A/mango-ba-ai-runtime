---
id: vpbx-api-141-dlya-organizaciy
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.4.2"
pdf_section: "3.9.4.2"
title: "Для организаций"
pdf_heading: "3.9.4.2 Для организаций"
pages: "196-197"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 196-197"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"196-197","global_pages":"196-197"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 659
status: extracted
ai-generated: true
---
# 3.9.4.2. Для организаций

> Трассировка: PDF §3.9.4.2 · сквозные стр. 196-197 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.196-197.

Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | action |  | Да | Название события зависит от действия:<br>● при создании – new;<br>● при редактировании – updated; |

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
|  |  |  |  | ● при удалении – deleted |
| 2 | data |  |  | Данные зависят от объекта. Набор данных идентичен получаемым<br>данным в методах «получить <объект> по id». Для контакта<br>указывается дополнительный параметр last_used |

Событие о добавлении организации Параметры события:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | action |  | Да | Название события = new |
| 2 | data |  | Да | Массив организации. В массиве объектов может быть один либо<br>несколько организаций, принадлежащих одному источнику |

Пример события: POST https://external-system.com/events/ab/organizations vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "action": "new", "data": [ { "org_id": "14642887", "org_name": "dfgdfgdfg" } ] } Событие об удалении организации Параметры события:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | action |  | Да | Название события = deleted |
| 2 | data |  | Да | Массив id организации. В массиве объектов может быть одна либо<br>несколько id организаций, принадлежащих одному источнику. |
