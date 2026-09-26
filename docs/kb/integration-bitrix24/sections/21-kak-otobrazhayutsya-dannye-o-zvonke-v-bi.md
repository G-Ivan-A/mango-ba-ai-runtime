---
id: integration-bitrix24-21-kak-otobrazhayutsya-dannye-o-zvonke-v-bi
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "1.4"
pdf_section: "1.4"
title: "Как отображаются данные о звонке в Битрикс24. Обобщенно"
pdf_heading: "1.4 Как отображаются данные о звонке в Битрикс24. Обобщенно"
pages: "23"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 23"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"23","global_pages":"23"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 286
status: extracted
ai-generated: true
---
# 1.4. Как отображаются данные о звонке в Битрикс24. Обобщенно

> Трассировка: PDF §1.4 · сквозные стр. 23 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.23.

В зависимости от включен или выключен флаг "Автоматически создавать лид и дело при входящих звонках" в дополнительных настройках интеграции, данные о звонке отображаются следующим образом: - если флаг включен, при входящем звонке от нового номера в Битрикс24 будет автоматически создан новый лид; - если флаг выключен, то при входящем звонке от нового номера (не заведенного в Битрикс24), НЕ будет автоматически создан новый лид и в карточке звонка в Битрикс24 будет предложено создать лид.
