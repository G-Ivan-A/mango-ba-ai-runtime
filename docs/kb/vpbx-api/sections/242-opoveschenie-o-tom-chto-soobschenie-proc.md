---
id: vpbx-api-242-opoveschenie-o-tom-chto-soobschenie-proc
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.10.3.4"
pdf_section: "4.10.3.4"
title: "Оповещение о том, что сообщение прочитано"
pdf_heading: "4.10.3.4 Оповещение о том, что сообщение прочитано"
pages: "324"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 324"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"324","global_pages":"324"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 257
status: extracted
ai-generated: true
---
# 4.10.3.4. Оповещение о том, что сообщение прочитано

> Трассировка: PDF §4.10.3.4 · сквозные стр. 324 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.324.

В данном разделе описано событие "Оповещение о том, что сообщение прочитано", отправляемое Контакт-центром MANGO OFFICE в ваше внешнее приложение. Параметры:

| № | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | messageId | Строка | Id сообщения |

Пример события: { "point_id": 10006434, "path": "/events/md", "data": { "userId": "KdpikRr7aLbBheMGnFAk", "messageId": "435594321659769152", "type": "notifyMessageRead" } }
