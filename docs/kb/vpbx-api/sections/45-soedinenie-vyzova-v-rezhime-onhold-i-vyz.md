---
id: vpbx-api-45-soedinenie-vyzova-v-rezhime-onhold-i-vyz
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.2.9"
pdf_section: "3.2.9"
title: "Соединение вызова в режиме OnHold и вызова в режиме Connected"
pdf_heading: "3.2.9 Соединение вызова в режиме OnHold и вызова в режиме Connected"
pages: "55-56"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 55-56"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"55-56","global_pages":"55-56"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1213
status: extracted
ai-generated: true
---
# 3.2.9. Соединение вызова в режиме OnHold и вызова в режиме Connected

> Трассировка: PDF §3.2.9 · сквозные стр. 55-56 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.55-56.

POST /commands/calls_connect Команда предназначена для объединения двух плечей консультативного перевода. Команда соединяет вызов, находящийся в режиме OnHold, и вызов в режиме Connected. Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Да | Идентификатор команды (строка не более 128 байт).<br>Формируется внешней системой. ВАТС никак не обрабатывает<br>этот идентификатор, не анализирует и не полагается на<br>уникальность его значения. Идентификатор можно<br>использовать для связи команды с результатом ее выполнения<br>и возможными последующими событиями, которые<br>появляются в результате выполнения команды. |
| 2 | holded_call_id | string | Да | Идентификатор вызова, который можно взять в событии<br>call_state: "OnHold". |

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 3 | transfer_initiato<br>r_number | string | Да | Номер плеча, которое нужно оставить (from-number в<br>событии call_state: "Appeared", идущего после OnHold). |
| 4 | transferred_cal<br>l_id | string | Да | Идентификатор вызова, который можно взять в событии<br>call_state: "Appeared", идущего после OnHold. |

Важно! В параметрах "transferred_call_id" и "holded_call_id" могут быть только Call_ID с одинаковым "entry_id". Пример запроса: POST https://app.mango-office.ru/vpbx/commands/calls_connect/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"888.3.MToxMDAwNjA4NTox", "holded_call_id":"MToxMDAwNjA4NToxMzQxOjI5NzU3Ng==", "transfer_initiator_number":"sip:userc@t3.mangosip.ru", "transferred_call_id":"MToxMDAwNjA4NToxMzQxOjI5NzU3OA==" } Результат: POST /result/calls_connect/ В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Нет | Идентификатор команды (строка не более 128 байт). |
| 2 | result |  | Да | Результат выполнения команды маршрутизации, полученной от<br>внешней системы. Ниже приведены некоторые возможные<br>значения результата (полный список см. п. "Список кодов<br>результатов"):<br>● 1000 - команда перевода выполнена успешно;<br>● 22хх - команда перевода ограничена биллинговой системой ВАТС;<br>● 32хх - передан неверный номер либо команда перевода не<br>может быть выполнена с этим номером;<br>● 4001 - команда не поддерживается;<br>● 4100 - перевод не предусмотрен для такого типа вызовов ВАТС;<br>● 4101 - вызов завершен либо не существует;<br>● 5ххх - ошибка сервера. |

Пример запроса: POST https://app.mango-office.ru/vpbx/api/v1/result/calls_connect/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"888.3.MToxMDAwNjA4NTox", "result":"1000" }
