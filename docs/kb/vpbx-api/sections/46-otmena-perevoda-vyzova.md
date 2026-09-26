---
id: vpbx-api-46-otmena-perevoda-vyzova
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.2.10"
pdf_section: "3.2.10"
title: "Отмена перевода вызова"
pdf_heading: "3.2.10 Отмена перевода вызова"
pages: "57-58"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 57-58"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"57-58","global_pages":"57-58"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 888
status: extracted
ai-generated: true
---
# 3.2.10. Отмена перевода вызова

> Трассировка: PDF §3.2.10 · сквозные стр. 57-58 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.57-58.

POST /commands/transfer_cancel Команда применяется для отмены вызовов, находящихся в состоянии OnHold Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Да | Идентификатор команды (строка не более 128 байт).<br>Формируется внешней системой. ВАТС никак не<br>обрабатывает этот идентификатор, не анализирует и не<br>полагается на уникальность его значения. Идентификатор<br>можно использовать для связи команды с результатом ее<br>выполнения и возможными последующими событиями,<br>которые появляются в результате выполнения команды. |
| 2 | call_id | string | Да | Идентификатор вызова, который можно взять в событии<br>call_state: "OnHold". |

Пример запроса: POST https://app.mango-office.ru/vpbx/commands/transfer_cancel/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"123400", "call_id":"MToxMDAwNjA4NToxMzQxOj3Ng==" } Результат: POST /result/transfer_cancel/ В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | command_id | string | Нет | Идентификатор команды (строка не более 128 байт). |
| 2 | result |  | Да | Результат выполнения команды маршрутизации, полученной от<br>внешней системы. Ниже приведены некоторые возможные<br>значения результата (полный список см. п. "Список кодов<br>результатов"):<br>● 1000 - команда перевода выполнена успешно;<br>● 22хх - команда перевода ограничена биллинговой системой ВАТС;<br>● 32хх - передан неверный номер либо команда перевода не<br>может быть выполнена с этим номером;<br>● 4001 - команда не поддерживается;<br>● 4100 - перевод не предусмотрен для такого типа вызовов ВАТС;<br>● 4101 - вызов завершен либо не существует;<br>● 5ххх - ошибка сервера. |

Пример запроса: POST https://app.mango-office.ru/vpbx/api/v1/result/transfer_cancel/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "command_id":"123400", "result": 4101 }
