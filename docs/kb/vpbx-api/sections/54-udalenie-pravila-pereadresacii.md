---
id: vpbx-api-54-udalenie-pravila-pereadresacii
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.3.4"
pdf_section: "3.3.4"
title: "Удаление правила переадресации"
pdf_heading: "3.3.4 Удаление правила переадресации"
pages: "65-66"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 65-66"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"65-66","global_pages":"65-66"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 461
status: extracted
ai-generated: true
---
# 3.3.4. Удаление правила переадресации

> Трассировка: PDF §3.3.4 · сквозные стр. 65-66 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.65-66.

POST /vpbx/forwarding/number/remove Метод позволяет удалить действующее правило безусловной переадресации на внутренний или внешний номер при звонке клиента. Входные параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | forward_id | integer | Да | ID правила переадресации. |

Пример запроса: POST https://app.mango-office.ru/vpbx/forwarding/number/remove/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "forward_id":"10023155" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  | Да | Результат выполнения команды завершения вызова от<br>внешней системы. Ниже приведены возможные значения<br>результата (см. "Список кодов результатов"):<br>● 1000 - команда завершения вызова выполнена успешно;<br>● 3100 - удачное выполнение;<br>● 3300 - объект не существует;<br>● 5XXX – исключение. |
