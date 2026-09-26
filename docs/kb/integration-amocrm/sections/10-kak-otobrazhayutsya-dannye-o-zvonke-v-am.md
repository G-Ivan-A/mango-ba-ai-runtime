---
id: integration-amocrm-10-kak-otobrazhayutsya-dannye-o-zvonke-v-am
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "0"
pdf_section: "1"
title: "Как отображаются данные о звонке в amoCRM. Обобщенно"
pdf_heading: "Как отображаются данные о звонке в amoCRM. Обобщенно"
pages: "20"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 20"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"20","global_pages":"20"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 287
status: extracted
ai-generated: true
---
# Как отображаются данные о звонке в amoCRM. Обобщенно

> Трассировка: PDF §1 · сквозные стр. 20 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.20.

В зависимости от настройки “Действие для нового Клиента” дополнительных настроек интеграции, после каждого принятого входящего звонка с нового номера телефона в amoCRM в разделе “Списки”: - будет создан контакт, в которой сохранится номер телефона позвонившего, ЛИБО • будет создан контакт и сделка, связанная с контактом. Название сделки по умолчанию будет в формате “Сделка номер телефона” (к примеру, “Сделка 74955404444”), ЛИБО • информация о звонке сохранится в категории “НЕРАЗОБРАННОЕ”, при этом контакт и сделка не будут созданы.
