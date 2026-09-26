---
id: vpbx-api-03-naznachenie
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "1.1"
pdf_section: "1.1"
title: "Назначение"
pdf_heading: "1.1 Назначение"
pages: "8"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 8"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"8","global_pages":"8"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 463
status: extracted
ai-generated: true
---
# 1.1. Назначение

> Трассировка: PDF §1.1 · сквозные стр. 8 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.8.

API MANGO OFFICE (далее по тексту – API) позволяет внешним клиентским системам, подключенным через API коннектор, работать с Виртуальной АТС и Контакт-центром MANGO OFFICE. В этом документе описаны два API: - API Виртуальной АТС MANGO OFFICE (далее по тексту – API ВАТС) предоставляет возможность управлять существующей функциональностью Виртуальной АТС; - API Контакт-центра MANGO OFFICE (далее по тексту – API КЦ) предоставляет возможность управлять статусами пользователей Контакт-центра MANGO OFFICE, получать уведомления о смене статусов пользователей, работать со сделками, кампаниями ИО, обращениями и задачами. Не допускаются различия в поведении в зависимости от того каким образом было инициировано выполнение той или иной операции. В частности, внешняя система не может претендовать на расширение или уменьшение прав на действия в ВАТС и/или в КЦ, так как это определяется исключительно правами сотрудника ВАТС и/или в КЦ, с которым ВАТС и/или в КЦ ассоциирует выполняемые действия.
