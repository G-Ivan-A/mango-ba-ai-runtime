---
id: vpbx-api-248-iniciirovanie-ishodyaschego-vyzova
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "—"
title: "Инициирование исходящего вызова"
pdf_heading: "Инициирование исходящего вызова"
pages: "334-336"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 334-336"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"334-336","global_pages":"334-336"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1194
status: extracted
ai-generated: true
---
# Инициирование исходящего вызова

> Трассировка: PDF §— · сквозные стр. 334-336 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.334-336.

Вешняя система отправляет команду инициирования вызова сотрудником ВАТС с внутренним номером "1234" на номер "74955404444". Номер вызываемого абонента был идентифицирован как номер сотрудника ВАТС с внутренним номером "5555". POST https://app.mango-office.ru/vpbx/commands/callback vpbx_api_key = qwerty123 sign = qwerty123 json = { "command_id": "cmd.2.vpbx.12345.external.system.com.net", "from": { "extension": "1234" }, "to_number": "74955404444" } Команда инициирования вызова обработана успешно. POST https://app.mango-office.ru/vpbx/result/callback vpbx_api_key = qwerty123 sign = qwerty123 json = { "command_id": "cmd.2.vpbx.12345.external.system.com.net", "result": "1000" } Система звонит инициатору вызова — сотруднику ВАТС с внутренним номером "1234", для связи используется номер "12345678". POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:251", "entry_id": "232wc3e3w3s222", "timestamp": 1399906971, "seq": "1", "location": "abonent", "call_state": "Appeared", "from": { "extension": "5555", "number": "74955404444" }, "to": { "extension": "1234", "number": "12345678" }, "command_id": "cmd.2.vpbx.12345.external.system.com.net" } Инициатор взял трубку: POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:251", "entry_id": "232wc3e3w3s222", "timestamp": 1399906973, "seq": "2", "location": "abonent", "call_state": "Connected", "from": { "extension": "5555", "number": "74955404444" }, "to": { "extension": "1234", "number": "12345678" }, "command_id": "cmd.2.vpbx.12345.external.system.com.net" } Система сообщает о завершении первого вызова POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:251", "entry_id": "232wc3e3w3s222", "timestamp": 1399906975, "seq": "3", "location": "abonent", "call_state": "Disconnected", "from": { "extension": "5555", "number": "74955404444" }, "to": { "extension": "1234", "number": "12345678" }, "disconnect_reason": "1000", "command_id": "cmd.2.vpbx.12345.external.system.com.net" } Появляется новый вызов: POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:258", "entry_id": "232wc3e3w3s222", "timestamp": 1399906976, "seq": "1", "location": "abonent", "call_state": "Appeared", "from": { "extension": "1234", "number": "12345678" "taken_from_call_id": "100:500:251" }, "to": { "extension": "5555", "number": "74955404444" }, "command_id": "cmd.2.vpbx.12345.external.system.com.net" } Сотрудника ВАТС с внутренним номером "5555" отклонил вызов на номер "74955404444" до соединения. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:258", "entry_id": "232wc3e3w3s222", "timestamp": 1399906979, "seq": "2", "location": "abonent", "call_state": "Disconnected", "from": { "extension": "1234", "number": "12345678" }, "to": { "extension": "5555", "number": "74955404444" }, "disconnect_reason": "1124", "command_id": "cmd.2.vpbx.12345.external.system.com.net" }
