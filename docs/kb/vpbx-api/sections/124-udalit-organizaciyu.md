---
id: vpbx-api-124-udalit-organizaciyu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.1.6"
pdf_section: "3.9.1.6"
title: "Удалить организацию"
pdf_heading: "3.9.1.6 Удалить организацию"
pages: "165-166"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 165-166"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"165-166","global_pages":"165-166"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 493
status: extracted
ai-generated: true
---
# 3.9.1.6. Удалить организацию

> Трассировка: PDF §3.9.1.6 · сквозные стр. 165-166 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.165-166.

POST /vpbx/ab/organizations/delete Метод позволяет удалить организацию. Также можно удалить несколько организаций, до 500. Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  |  | Массив удаляемых организаций, разделитель – запятая «,» |
| 1.1 |  | org_id |  |  | id организации |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/organizations/delete vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data": [ "10433913", "10433914", "10000" ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31XX - неверные параметры;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера. |

Пример ответа: { "result": 1000 }
