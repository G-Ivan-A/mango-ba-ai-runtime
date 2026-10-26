---
id: vpbx-api-250-perevod-vyzova-s-konsultaciey
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "—"
title: "Перевод вызова с консультацией"
pdf_heading: "Перевод вызова с консультацией"
pages: "339-342"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 339-342"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"339-342","global_pages":"339-342"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1513
status: extracted
ai-generated: true
---
# Перевод вызова с консультацией

> Трассировка: PDF §— · сквозные стр. 339-342 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.339-342.

Входящий вызов с номера "74955404444" на номер сотрудника ВАТС "12345678" с внутренним номером "123" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "200:514", "timestamp": "1398956978", "seq": "1", "locaton": "abonent"; "call_state": "Appeared", "from": { "number": "74955404444" }, "to": { "extension": "123", "number": "12345678" } } Абонент "74955404444" соединен с "12345678" . POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "200:514", "timestamp": 1398956985, "seq": "2", "locaton": "abonent"; "call_state": "Connected", "from": { "number": "74955404444" }, "to": { "extension": "123", "number": "12345678" } } Вызов абонентов "74955404444" и "12345678" на удержании. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "200:514", "timestamp": "1398956995", "seq": "3", "call_state": "OnHold", "locaton": "abonent"; "from": { "number": "74955404444" }, "to": { "extension": "123", "number": "12345678" } } Исходящий вызов с номера "12345678" сотрудника ВАТС с внутренним номером "123" на номер "87654321" сотрудника ВАТС с внутренним номером "321" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "202:515", "timestamp": "1398957005", "seq": "1", "locaton": "abonent"; "call_state": "Appeared", "from": { "extension": "123", "number": "12345678", "taken_from_call_id":"200:514" }, "to": { "extension": "321", "number": "87654321" } } Произошло соединение абонентов "12345678" и "87654321" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "202:515", "timestamp": 1398957005, "seq": "2", "locaton": "abonent"; "call_state": "Connected", "from": { "extension": "123", "number": "12345678", "taken_from_call_id":"200:514" }, "to": { "extension": "321", "number": "87654321" } } Вызов завершен, сотрудник ВАТС с внутренним номером "123" повесил трубку.

| POST https://external-system.com/events/call<br>vpbx_api_key = qwerty123<br>sign = qwerty123<br>json = { |
| --- |
| "entry_id": "232wc3e3w3s222",<br>"call_id": "200:514",<br>"timestamp": 1398956995,<br>"seq": "4",<br>"locaton": "abonent"; |
| "call_state": "Disconnected",<br>"from": {<br>"number": "74955404444" },<br>"to": {<br>"extension": "123",<br>"number": "12345678" }<br>"disconnect_reason": "1120"<br>} |

![Изображение, стр. 341](../images/250-perevod-vyzova-s-konsultaciey-1.png)

![Изображение, стр. 341](../images/250-perevod-vyzova-s-konsultaciey-2.png)

![Изображение, стр. 341](../images/250-perevod-vyzova-s-konsultaciey-3.png)

![Изображение, стр. 341](../images/250-perevod-vyzova-s-konsultaciey-4.png)

Произошло соединение абонентов "74955404444" и "87654321", абонент "12345678" замещен абонентом "74955404444" POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "202:515", "timestamp": 1398957005, "seq": "3", "locaton": "abonent"; "call_state": "Connected", "from": { "number": "74955404444", "taken_from_call_id": "200:514" }, "to": { "extension": "321", "number": "87654321" } } Вызов завершен, вызывающий абонент повесил трубку. POST https://external-system.com/events/call vpbx_api_key = qwerty123 sign = qwerty123 json = { "entry_id": "232wc3e3w3s222", "call_id": "202:515", "timestamp": "1398957015", "seq": "4", "locaton": "abonent"; "call_state": "Disconnected", "from": { "number": "74955404444", "taken_from_call_id": "200:514" }, "to": { "extension": "321", "number": "87654321" }, "disconnect_reason": "1110" }
