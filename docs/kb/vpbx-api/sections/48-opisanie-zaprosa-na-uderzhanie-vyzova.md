---
id: vpbx-api-48-opisanie-zaprosa-na-uderzhanie-vyzova
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.2.11.1"
pdf_section: "3.2.11.1"
title: "Описание запроса на удержание вызова"
pdf_heading: "3.2.11.1 Описание запроса на удержание вызова"
pages: "58"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 58"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"58","global_pages":"58"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 568
status: extracted
ai-generated: true
---
# 3.2.11.1. Описание запроса на удержание вызова

> Трассировка: PDF §3.2.11.1 · сквозные стр. 58 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.58.

POST /commands/call/hold/on Команда применяется для постановки вызова на удержание. Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Да | Идентификатор команды (строка не более 128 байт).<br>Формируется внешней системой. ВАТС никак не обрабатывает<br>этот идентификатор, не анализирует и не полагается на<br>уникальность его значения. Идентификатор можно<br>использовать для связи команды с результатом ее выполнения<br>и возможными последующими событиями, которые появляются<br>в результате выполнения команды. |
| 2 | call_id | string |  | Идентификатор вызова, который ставится на удержание. |
| 3 | initiator |  | Да | Участник разговора от имени которого выполняется постановка<br>вызова на удержание. Должно быть заполнено значением<br>одного из полей блока "from" или "to" переводимого вызова<br>(например, "from.extension", "from.number", "to.extension" или<br>"to.number"). В ВАТС разрешены переводы только от имени<br>сотрудника ВАТС. |

Пример запроса: POST https://app.mango-office.ru/vpbx/commands/call/hold/on vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"cmd.1.vpbx.12345.external.system.com.net", "call_id":"100500", "initiator":"100500" }
