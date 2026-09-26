---
id: vpbx-api-49-poluchenie-rezultata-vypolneniya-zaprosa
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.2.11.2"
pdf_section: "3.2.11.2"
title: "Получение результата выполнения запроса"
pdf_heading: "3.2.11.2 Получение результата выполнения запроса"
pages: "58-59"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 58-59"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"58-59","global_pages":"58-59"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 531
status: extracted
ai-generated: true
---
# 3.2.11.2. Получение результата выполнения запроса

> Трассировка: PDF §3.2.11.2 · сквозные стр. 58-59 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.58-59.

POST /result/call/hold/on Метод предназначен для получения код результата выполнения запроса "Постановка вызова на удержание". В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Нет | Идентификатор команды (строка не более 128 байт). |
| 2 | result |  | Да | Результат выполнения команды маршрутизации, полученной от<br>внешней системы. В ответе содержит код результата:<br>● 1000 - команда перевода выполнена успешно;<br>● 22хх - команда перевода ограничена биллинговой системой ВАТС;<br>● 32хх - передан неверный номер либо команда перевода не<br>может быть выполнена с этим номером;<br>● 4001 - команда не поддерживается;<br>● 4100 - перевод не предусмотрен для такого типа вызовов ВАТС;<br>● 4101 - вызов завершен либо не существует;<br>● 5ххх - ошибка сервера. |

Пример запроса: POST https://app.mango-office.ru/vpbx/api/v1/result/call/hold/on vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"cmd.2.vpbx.12345.external.system.com.net", "result":"1000" }
