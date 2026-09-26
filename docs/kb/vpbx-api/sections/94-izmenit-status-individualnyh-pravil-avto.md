---
id: vpbx-api-94-izmenit-status-individualnyh-pravil-avto
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.16"
pdf_section: "3.7.16"
title: "Изменить статус индивидуальных правил автосекретаря сотрудника"
pdf_heading: "3.7.16 Изменить статус индивидуальных правил автосекретаря сотрудника"
pages: "138"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 138"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"138","global_pages":"138"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 547
status: extracted
ai-generated: true
---
# 3.7.16. Изменить статус индивидуальных правил автосекретаря сотрудника

> Трассировка: PDF §3.7.16 · сквозные стр. 138 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.138.

POST /vpbx/autosecretary/status/change Метод служит для включения или отключения индивидуальных правил автосекретаря для сотрудника. Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | user_id | integer | Да | ID сотрудника |
| 2 | rule_id | string | Да | ID правила автосекретаря сотрудника |
| 3 | active | bool | Да | Статус правила автосекретаря (0 - выключен, 1 - включен) |

Пример запроса: POST https://app.mango-office.ru/vpbx/autosecretary/status/change vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "user_id":"300056738", "rule_id":"2147", "active":"0" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие код ошибки:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>- 1000 - удачное выполнение;<br>- 2230 - услуга недоступна;<br>- 3000 - неверный запрос;<br>- 3100 - переданы неверные параметры команды;<br>- 31XX - неверные параметры;<br>- 3300 - объект не существует;<br>- 5XXX – ошибка сервера. |

Пример ответа: { "result": 1000 }
