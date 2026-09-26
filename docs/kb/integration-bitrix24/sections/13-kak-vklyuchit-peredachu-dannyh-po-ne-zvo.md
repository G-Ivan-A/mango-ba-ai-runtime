---
id: integration-bitrix24-13-kak-vklyuchit-peredachu-dannyh-po-ne-zvo
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "1.1"
title: "Как включить передачу данных по “не звонковым” обращениям"
pdf_heading: "Как включить передачу данных по “не звонковым” обращениям"
pages: "14"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 14"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"14","global_pages":"14"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 364
status: extracted
ai-generated: true
---
# Как включить передачу данных по “не звонковым” обращениям

> Трассировка: PDF §1.1 · сквозные стр. 14 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.14.

Под “не звонковым” обращением понимается текстовая коммуникация Клиента с оператором, например, заявка с сайта, чата на сайте и т.д. Статистику таких обращений собирает Коллтрекинг MANGO OFFICE, при его уставке на вашем сайте. Чтобы иметь возможность загружать в Битрикс24 данные коллтрекинга по различным типам не звонковых обращений, очень важно в таблице сопоставления сотруднику, под которым было установлено приложение интеграции (см. раздел "Установка приложения интеграции в Битрикс24"), поставить в соответствие сотрудника Виртуальной АТС. Это необходимо, чтобы CRM Битрикс24 начал принимать вебхуки с данными по различным видам обращений, зафиксированным коллтрекингом.
