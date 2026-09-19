---
id: vpbx-api-203-obnovlenie-zadaniya-kampanii-io
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.17"
pdf_section: "4.6.17"
title: "Обновление задания кампании ИО"
pdf_heading: "4.6.17 Обновление задания кампании ИО"
pages: "286-287"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 286-287"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"286-287","global_pages":"286-287"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 691
status: extracted
ai-generated: true
---
# 4.6.17. Обновление задания кампании ИО

> Трассировка: PDF §4.6.17 · сквозные стр. 286-287 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.286-287.

POST /vpbx/task/update Метод позволяет обновить статус задания кампании ИО. Параметры запроса:

| № | Параметры | Тип<br>данных | Обяза-<br>тель-<br>ность | Описание |
| --- | --- | --- | --- | --- |
| 1 | campaign_id | Число | Да | ID кампании |
| 2 | task_id | Число | Да | ID задания кампании |
| 3 | name | string | Да | Имя клиента, которому адресован звонок.<br>Ограничение - 255 символов |
| 4 | priority | integer |  | Приоритет выполнения звонка. Может иметь значение от<br>1 до 1000 |
| 5 | organization | string | Нет | Название организации, которой адресован звонок.<br>Ограничение - 255 символов |
| 6 | position | string | Нет | Должность человека, которому адресован звонок.<br>Ограничение - 255 символов |
| 7 | custom_fields | Объект<br>ключ-<br>значение | Нет | Значение пользовательских полей. Для получения списка<br>пользовательских полей, используется метод "Получение<br>списка пользовательских полей". Обязательность<br>заполнения пользовательского поля зависит от<br>настройки. |

Пример запроса: POST https://app.mango-office.ru/vpbx/task/update vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = {"campaign_id": 56919, "task_id": 11227830, "name": "Михайлов Михаил Михайлович", "priority":"1", "organization": "Копыта и Рога", "position": "Директор", "custom_fields": [ { "5781": "Фейерверк" } ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Число | Да | Код результата |

Пример ответа: { "result": 1000 }
