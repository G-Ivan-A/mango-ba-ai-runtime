---
id: integration-bitrix24-50-vo-vremya-zvonka
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "2.3"
title: "Во время звонка"
pdf_heading: "Во время звонка"
pages: "43-45"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 43-45"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"43-45","global_pages":"43-45"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 504
status: extracted
ai-generated: true
---
# Во время звонка

> Трассировка: PDF §2.3 · сквозные стр. 43-45 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.43-45.

Если вы подключили интеграцию с динамическим коллтрекингом, а также настроили динамический коллтрекинг, то: - при входящем звонке от Клиента, в карточке звонка будут показаны данные коллтрекинга. Отображаемые в карточке звонка данные коллтрекинга изменить невозможно. Пример отображения данных коллтрекинга показан на рисунке:

![Изображение, стр. 43](../images/50-vo-vremya-zvonka-1.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026 • при исходящем звонке данные коллтрекинга не отображаются:

![Изображение, стр. 44](../images/50-vo-vremya-zvonka-2.png)

Если во время звонка в интеграцию еще не поступили данные коллтрекинга, в карточке звонка в Битрикс24 будет показано сообщение "Ожидание данных Коллтрекинга MANGO OFFICE". Пример отображения данных коллтрекинга показан на рисунке:

![Изображение, стр. 44](../images/50-vo-vremya-zvonka-3.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
