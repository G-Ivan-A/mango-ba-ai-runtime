---
id: vpbx-api-251-perevod-vyzova-bez-konsultacii
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "—"
title: "Перевод вызова без консультации"
pdf_heading: "Перевод вызова без консультации"
pages: "342-345"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 342-345"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"342-345","global_pages":"342-345"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1303
status: extracted
ai-generated: true
---
# Перевод вызова без консультации

> Трассировка: PDF §— · сквозные стр. 342-345 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.342-345.

Входящий вызов с номера "74955404444" на номер сотрудника ВАТС "44332211" с внутренним номером "333" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "300:200", "timestamp": 1399956976, "seq": "1", "call_state": "Appeared", "from": { "number": "74955404444" }, "to": { "extension": "333", "number": "44332211" } } Абонент "74955404444" соединен с "44332211" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "300:200", "timestamp": 1399956986, "seq": "2", "call_state": "Connected", "from": { "number": "74955404444" }, "to": { "extension": "333", "number": "44332211" } } Разговор абонентов "74955404444" и "44332211" на удержании POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "300:200", "timestamp": 1399956986, "seq": "3", "call_state": "OnHold", "from": { "number": "74955404444" }, "to": { "extension": "333", "number": "44332211" } } Исходящий вызов с номера "44332211" сотрудника ВАТС с внутренним номером "333" на номер "87654321" сотрудника ВАТС с внутренним номером "321" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "400-200", "timestamp": 1399956996, "seq": "1", "call_state": "Appeared", "from": { "extension": "333", "number": "44332211" }, "to": { "extension": "321", "number": "87654321" } } Вызов завершен, сотрудник ВАТС "44332211" с внутренним номером "333" повесил трубку. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "300:200", "timestamp": 1399957006, "seq": "4", "call_state": "Disconnected", "from": { "number": "74955404444" }, "to": { "extension": "333", "number": "44332211" }, "disconnect_reason": "1120" } Вызов с номера "44332211" сотрудника ВАТС с внутренним номером "333" замещен на вызов с номера "74955404444" на номер "87654321" сотрудника ВАТС с внутренним номером "321" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "400-200", "timestamp": 1399957006, "seq": "2", "call_state": "Appeared", "from": { "number": "74955404444", "taken_from_call_id": "300:200" }, "to": { "extension": "321", "number": "87654321" } } Произошло соединение абонентов "74955404444" и "87654321" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "400-200", "timestamp": "1399957016", "seq": "3", "call_state": "Connected", "from": { "number": "74955404444", "taken_from_call_id": "300:200" }, "to": { "extension": "321", "number": "87654321" } } Вызов завершен абонентом "74955404444". POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "400-200", "timestamp": 1399957036, "seq": "4", "call_state": "Disconnected", "from": { "number": "74955404444", "taken_from_call_id": "300:200" }, "to": { "extension": "321", "number": "87654321" }, "disconnect_reason": "1110" }
