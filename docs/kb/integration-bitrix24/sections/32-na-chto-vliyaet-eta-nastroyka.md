---
id: integration-bitrix24-32-na-chto-vliyaet-eta-nastroyka
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "2.3"
title: "На что влияет эта настройка"
pdf_heading: "На что влияет эта настройка"
pages: "32-33"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 32-33"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"32-33","global_pages":"32-33"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 475
status: extracted
ai-generated: true
---
# На что влияет эта настройка

> Трассировка: PDF §2.3 · сквозные стр. 32-33 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.32-33.

Если у вас несколько номеров подключено к Виртуальной АТС, и вы хотите разделять Клиентов, обращающихся по разным номерам, то приложение интеграции поддерживает эту возможность. При поступлении звонка от Клиента, приложение интеграции будет передавать в Битрикс24 номер, на который звонил Клиент. Этот номер будет показан: 1) в карточке звонка:

![Изображение, стр. 32](../images/32-na-chto-vliyaet-eta-nastroyka-1.png)

2) в карточке Клиента:

![Изображение, стр. 32](../images/32-na-chto-vliyaet-eta-nastroyka-2.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026 3) в детализации звонков; Примечание. Как открыть отчет "Детализация звонков" описано в приложении А.

![Изображение, стр. 33](../images/32-na-chto-vliyaet-eta-nastroyka-3.png)

4) в лиде (в пользовательских полях) сохранится информация о номере, на который поступил звонок (об источнике):

![Изображение, стр. 33](../images/32-na-chto-vliyaet-eta-nastroyka-4.png)
