---
id: integration-amocrm-69-integraciya-s-adresnoy-knigoy-virtualnoy
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "13"
pdf_section: "13"
title: "Интеграция с адресной книгой Виртуальной АТС"
pdf_heading: "13 Интеграция с адресной книгой Виртуальной АТС"
pages: "122-124"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 122-124"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"122-124","global_pages":"122-124"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 769
status: extracted
ai-generated: true
---
# 13. Интеграция с адресной книгой Виртуальной АТС

> Трассировка: PDF §13 · сквозные стр. 122-124 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.122-124.

Если в Виртуальной АТС подключена услуга “Расширенные возможности интеграции”, то в Личном кабинете можно подключить amoCRM как внешний источник контактов в адресную книгу MANGO OFFICE. Вам нужно установить флаг “Подключить к адресной книге Виртуальной АТС” и нажать “Сохранить”. Начнется отображение контактов и компаний из amoCRM в адресной книге Виртуальной АТС:

![Изображение, стр. 122](../images/69-integraciya-s-adresnoy-knigoy-virtualnoy-1.png)

Контакты и компании из amoCRM будут видны: - в Личном кабинете Виртуальной АТС в разделе “Адресная книга”; - в Mango Talker; - в Контакт Центр MANGO OFFICE. В MANGO TALKER:

![Изображение, стр. 122](../images/69-integraciya-s-adresnoy-knigoy-virtualnoy-2.png)

В Личном кабинете Виртуальной АТС: Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

![Изображение, стр. 123](../images/69-integraciya-s-adresnoy-knigoy-virtualnoy-3.png)

При обновлении контактов/компаний в amoCRM, информация о них будет автоматически обновлена в адресной книге Виртуальной АТС. Это обеспечивается с помощью автоматически устанавливаемых WebHook в amoCRM:

![Изображение, стр. 123](../images/69-integraciya-s-adresnoy-knigoy-virtualnoy-4.png)

Адреса для web-hook: - контакт - https://amocrm.mango-office.ru/webhook/contact/ххх - компания - https://amocrm.mango-office.ru/webhook/company/ххх Если удалить web-hook, то информация о контактах и компаниях не будет автоматически обновляться в адресной книге Виртуальной АТС. Внимание! Можно просматривать карточку контакта/компании, но нельзя ее редактировать. Редактировать ее можно только из amoCRM Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025
