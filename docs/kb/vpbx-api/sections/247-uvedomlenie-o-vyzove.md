---
id: vpbx-api-247-uvedomlenie-o-vyzove
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "—"
title: "Уведомление о вызове"
pdf_heading: "Уведомление о вызове"
pages: "333-334"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 333-334"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"333-334","global_pages":"333-334"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 508
status: extracted
ai-generated: true
---
# Уведомление о вызове

> Трассировка: PDF §— · сквозные стр. 333-334 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.333-334.

Сотрудник ВАТС с внутренним номером "1234" вызывает с номера "74955404444" внешнего абонента с номером "12345678". POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:256", "entry_id": "232wc3e3w3s222", "timestamp": "1399906976", "seq": "1", "location": "abonent", "call_state": "Appeared", "from": { "extension": "1234" }, "to": { "number": "12345678" } } Произошло соединение абонентов. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:256", "entry_id": "232wc3e3w3s222", "timestamp": "1399906988", "seq": "2", "location": "abonent", "call_state": "Connected", "from": { "extension": "1234", "number": "74955404444" }, "to": { "number": "12345678" } } Вызов завершен, внешний абонент повесил трубку. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "call_id": "100:500:256", "entry_id": "232wc3e3w3s222", "timestamp": "1399907008", "seq": "3", "location": "abonent", "call_state": "Disconnected", "from": { "extension": "1234", "number": "74955404444" }, "to": { "number": "12345678" }, "disconnect_reason": "1120" }
