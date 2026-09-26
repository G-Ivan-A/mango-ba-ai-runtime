---
id: integration-bitrix24-122-pereklyuchenie-mezhdu-rezhimami-raboty-b
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "2.19"
pdf_section: "2.19"
title: "Переключение между режимами работы Битрикс24"
pdf_heading: "2.19 Переключение между режимами работы Битрикс24"
pages: "102-104"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 102-104"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"102-104","global_pages":"102-104"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 643
status: extracted
ai-generated: true
---
# 2.19. Переключение между режимами работы Битрикс24

> Трассировка: PDF §2.19 · сквозные стр. 102-104 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.102-104.

Приложение интеграции поддерживает разные режимы работы: - классическая CRM Сделка + клиент (без лидов); - простая CRM Лид -> сделка + клиент. Важным различием режима работы является использование лидов в классическом режиме (в режиме простой CRM лиды не используются). Вы можете переключаться между режимами работы: 1) выберите "CRM"; 2) перейдите в раздел "Лиды";

![Изображение, стр. 102](../images/122-pereklyuchenie-mezhdu-rezhimami-raboty-b-1.png)

3) нажмите пиктограмму "Настройки" 4) выберите "Режим работы CRM":

![Изображение, стр. 102](../images/122-pereklyuchenie-mezhdu-rezhimami-raboty-b-2.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026 5) выберите режим работы и нажмите кнопку "Сохранить":

![Изображение, стр. 103](../images/122-pereklyuchenie-mezhdu-rezhimami-raboty-b-3.png)

В упрощенном режиме работы вместо лидов - автоматически создаются контакты и связанные с ними сделки. Звонки фиксируются в контактах, для звонка указывается номер, на который звонил Клиент:

![Изображение, стр. 103](../images/122-pereklyuchenie-mezhdu-rezhimami-raboty-b-4.png)

Обратите внимание, замечено, что Битрикс24 в этом режиме автоматически создает лиды, но не отображает их в приложении. Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
