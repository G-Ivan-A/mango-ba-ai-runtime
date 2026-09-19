---
id: integration-amocrm-56-ogranicheniya-po-peredachi-zvonka-v-novy
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "7.12"
pdf_section: "7.12"
title: "Ограничения по передачи звонка в новый контакт"
pdf_heading: "7.12 Ограничения по передачи звонка в новый контакт"
pages: "106-107"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 106-107"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"106-107","global_pages":"106-107"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 391
status: extracted
ai-generated: true
---
# 7.12. Ограничения по передачи звонка в новый контакт

> Трассировка: PDF §7.12 · сквозные стр. 106-107 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.106-107.

Если вы завершили разговор с новым абонентом и, спустя некоторое время, вручную добавили этого абонента в контакты amoCRM, то данные нового контакта корректно отобразятся в Истории звонков. При этом, мы не гарантируем, что в новый контакт amoCRM добавятся данные о звонках, совершенных ранее (чем контакт был создан). Например, если сегодня вы вручную добавили контакт Иван Иванов в amoCRM, но с этим абонентом вы созванивались ранее (вчера или позавчера), данные о ранее совершенных звонках могут не отобразится в контакте amoCRM. Если же вы позвонили новому абоненту после того, как добавили его в контакт amoCRM, данные о звонке добавятся в контакт. Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025
