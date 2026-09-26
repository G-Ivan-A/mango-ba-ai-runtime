---
id: integration-bitrix24-84-kak-nastroit-uvedomlenie-v-robotah-i-biz
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "2.7"
title: "Как настроить уведомление в роботах и бизнес-процессах"
pdf_heading: "Как настроить уведомление в роботах и бизнес-процессах"
pages: "75-78"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 75-78"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"75-78","global_pages":"75-78"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 762
status: extracted
ai-generated: true
---
# Как настроить уведомление в роботах и бизнес-процессах

> Трассировка: PDF §2.7 · сквозные стр. 75-78 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.75-78.

Чтобы сделать рассылку, в Битрикс24 следует: 1) выберите "CRM"; 2) нажмите кнопку "Настройка", затем выберите "Настройка CRM":

![Изображение, стр. 75](../images/84-kak-nastroit-uvedomlenie-v-robotah-i-biz-1.jpeg)

3) выберите пункт "Роботы и бизнес-процессы"; 4) выберите, для какой сущности будет использован робот: лид, сделка:

![Изображение, стр. 75](../images/84-kak-nastroit-uvedomlenie-v-robotah-i-biz-2.png)

5) Начните редактировать робота. Для добавления SMS уведомления выберите "+" на нужном этапе воронки продаж:

![Изображение, стр. 75](../images/84-kak-nastroit-uvedomlenie-v-robotah-i-biz-3.jpeg)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026 Нажмите на пункт "Коммуникация с клиентом", затем в блоке "Роботы и Триггеры" выберите пункт "Отправить СМС клиенту":

![Изображение, стр. 76](../images/84-kak-nastroit-uvedomlenie-v-robotah-i-biz-4.png)

В настройках уведомления: 1) выберите провайдера: MANGO OFFICE Виртуальная АТС; 2) настройте другие параметры уведомления; 3) нажмите кнопку "Сохранить":

![Изображение, стр. 76](../images/84-kak-nastroit-uvedomlenie-v-robotah-i-biz-5.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026 При наступлении соответствующего события, автоматически отправится SMS и зафиксируется в карточке. На примере ниже, SMS была автоматически отправлена при смене статуса сделки:

![Изображение, стр. 77](../images/84-kak-nastroit-uvedomlenie-v-robotah-i-biz-6.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
