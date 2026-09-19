---
id: vpbx-api-38-zavershenie-vyzova
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.2.3"
pdf_section: "3.2.3"
title: "Завершение вызова"
pdf_heading: "3.2.3 Завершение вызова"
pages: "38-39"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 38-39"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"38-39","global_pages":"38-39"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 898
status: extracted
ai-generated: true
---
# 3.2.3. Завершение вызова

> Трассировка: PDF §3.2.3 · сквозные стр. 38-39 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.38-39.

POST /vpbx/commands/call/hangup Команда завершает указанный вызов. Выполняется, если вызов находится в location=IVR или location=abonent. Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string |  | Идентификатор команды (строка не более 128 байт).<br>Формируется внешней системой. ВАТС никак не обрабатывает<br>этот идентификатор, на анализирует и не полагается на<br>уникальность его значения. Идентификатор можно<br>использовать для связи команды с результатом ее выполнения и<br>возможными последующими событиями, которые появляются в<br>результате выполнения команды. |
| 2 | call_id |  |  | Внутренний идентификатор вызова, который необходимо<br>завершить. Не имеет отношения к CALL-ID из SIP-протокола. |

Пример запроса: POST https://app.mango-office.ru/vpbx/commands/call/hangup vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"cmd.888.vpbx.12345.external.system.com.net", "call_id":"100500" } POST /vpbx/result/call/hangup В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Нет | Идентификатор команды (строка не более 128 байт). |
| 2 | result |  | Да | Результат выполнения команды завершения вызова от<br>внешней системы. Ниже приведены возможные значения<br>результата (см. "Список кодов результатов"):<br>● 1000 - команда завершения вызова выполнена успешно;<br>● 4001 - команда не поддерживается;<br>● 4100 - вызов не может быть завершен по логике работы<br>ВАТС;<br>● 4101 - на момент поступления команды в ВАТС, вызов, к<br>которому относится команда завершения, уже завершился<br>либо указанный идентификатор вызова не найден (указан<br>неверно);<br>● 5ххх - ошибка сервера. |

Пример запроса: POST https://app.mango-office.ru/vpbx/result/call/hangup vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"cmd.654.vpbx.12345.external.system.com.net", "result":"4101" }
