---
id: vpbx-api-156-osnovnoe
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.1"
pdf_section: "4.1"
title: "Основное"
pdf_heading: "4.1 Основное"
pages: "212"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 212"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"212","global_pages":"212"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 398
status: extracted
ai-generated: true
---
# 4.1. Основное

> Трассировка: PDF §4.1 · сквозные стр. 212 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.212.

1) Этот API позволяет обращаться к некоторым функциям и данными Контакт-центра MANGO OFFICE (далее по тексту - КЦ). Вы можете работать с обращениями, управлять статусами и сессиями пользователей, а также сделками и кампаниями исходящего обзвона (далее по тексту - ИО). Кроме того, можно работать с данными для звонка и управлять задачами на автоперезвон. 2) В случае недоступности API КЦ по тем или иным причинам, вызов любого метода возвращает ошибку 5008 - услуга не доступна. Пример ответа на любой запрос при недостуности API КЦ: { "result": 5008 } В этом случае свяжитесь со службой поддержки пользователей MANGO OFFICE. Поддержка доступна только клиентам, которые приобрели услуги Виртуальной АТС MANGO OFFICE и Контакт-центра MANGO OFFICE. 3) Частота передачи запросов к API КЦ указана в разделе Лимиты количества запросов к API.
