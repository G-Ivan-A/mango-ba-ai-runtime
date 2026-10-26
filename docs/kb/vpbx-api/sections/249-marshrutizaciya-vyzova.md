---
id: vpbx-api-249-marshrutizaciya-vyzova
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "—"
title: "Маршрутизация вызова"
pdf_heading: "Маршрутизация вызова"
pages: "336-338"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 336-338"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"336-338","global_pages":"336-338"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1144
status: extracted
ai-generated: true
---
# Маршрутизация вызова

> Трассировка: PDF §— · сквозные стр. 336-338 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.336-338.

Вызов поступает на номер DID 7800123456789, попадает в IVR. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:256", "entry_id": "232wc3e3w3s222", "timestamp": "1399906976", "seq": "1", "call_state": "Appeared", "location": "ivr", "from": { "number": "79000000000" }, "to": { "number": "7800123456789", "line_number": "7800123456789" } } От внешней системы поступает команда маршрутизации на внутренний номер 123 POST https://app.mango-office.ru/vpbx/commands/route vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:256", "command_id": "c111", "to_number": "123" } IVR завершается POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:256", "entry_id": "232wc3e3w3s222", "timestamp": "1399906976", "seq": "2", "call_state": "Disconnected", "location": "ivr", "from": { "number": "79000000000" }, "to": { "number": "7800123456789", "line_number": "7800123456789" } "disconnect_reason": "1100" } Новый вызов на сотрудника, уведомление о результате выполнения команды POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:257", "entry_id": "232wc3e3w3s222", "timestamp": "1399906977", "seq": "1", "command_id": "c111", "call_state": "Appeared", "location": "abonent", "from": { "number": "79000000000", "taken_from_call_id": "100:500:256" }, "to": { "extension": "123" "number": "sip:aaa@mangosip.ru", "line_number": "7800123456789" } } POST https://app.mango-office.ru/vpbx/result/route vpbx_api_key = qwerty123 sign = qwerty123 json = { "command_id": "c111", "result": "1000" } Сотрудник снимает трубку.

| POST https://external-system.com/events/call<br>vpbx_api_key = qwerty123<br>sign = qwerty123<br>json = {<br>"call_id": "100:500:257",<br>"entry_id": "232wc3e3w3s222", |
| --- |
| "timestamp": "1399906988",<br>"seq": "2",<br>"command_id": "c111",<br>"call_state": "Connected",<br>"location": "abonent", |
| "from": {<br>"number": "79000000000",<br>"taken_from_call_id": "100:500:256" |
| },<br>"to": {<br>"extension": "123"<br>"number": "sip:aaa@mangosip.ru",<br>"line_number": "7800123456789" } } |

![Изображение, стр. 338](../images/249-marshrutizaciya-vyzova-1.png)

![Изображение, стр. 338](../images/249-marshrutizaciya-vyzova-2.png)

<!-- изображение на стр. 338: байты не извлечены (PyMuPDF недоступен) -->

Вызов завершен, внешний абонент повесил трубку. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:257", "entry_id": "232wc3e3w3s222", "timestamp": "1399907008", "seq": "3", "command_id": "c111", "call_state": "Disconnected", "location": "abonent", "from": { "number": "79000000000", "taken_from_call_id": "100:500:256" }, "to": { "extension": "123" "number": "sip:aaa@mangosip.ru", "line_number": "7800123456789" } "disconnect_reason": "1120" }
