---
id: integration-bpmsoft-67-obzor
doc_code: INTBPM
doc_title: "Интеграция Виртуальной АТС и BPMSoft. Руководство по интеграции"
doc_version: "22.06.2026"
section: "0"
pdf_section: "2.4"
title: "Обзор"
pdf_heading: "Обзор"
pages: "52"
source: kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf
source_part: "1"
source_pages: "ч.1: 52"
source_refs: '[{"source_pdf":"kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf","part":1,"pages":"52","global_pages":"52"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 308
status: extracted
ai-generated: true
---
# Обзор

> Трассировка: PDF §2.4 · сквозные стр. 52 · источники: ч.1 `kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf` с.52.

Если Клиент ранее несколько раз обращался к вам, то в вашем BPMSoft одному и тому же Клиенту может соответствовать несколько сущностей (например, несколько контактов). По умолчанию, при поступлении повторного звонка от Клиента, этот звонок автоматически привязывается к сущности, которая первой была найдена в BPMSoft. В приложении интеграции существует настройка, которая позволяет вручную привязывать звонок к определенной сущности. Если звонку соответствует несколько сущностей (например, несколько контактов), то при обработке звонка все они будут выведены на экран и пользователь сможет вручную привязать звонок к любой из сущностей.
