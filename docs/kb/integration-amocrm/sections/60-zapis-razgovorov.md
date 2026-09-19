---
id: integration-amocrm-60-zapis-razgovorov
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "10"
pdf_section: "10"
title: "Запись разговоров"
pdf_heading: "10 Запись разговоров"
pages: "112-113"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 112-113"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"112-113","global_pages":"112-113"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 469
status: extracted
ai-generated: true
---
# 10. Запись разговоров

> Трассировка: PDF §10 · сквозные стр. 112-113 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.112-113.

Если в Виртуальной АТС подключена услуга записи разговоров, то при наличии записи разговора ее можно прослушать или скачать в amoCRM:

![Изображение, стр. 112](../images/60-zapis-razgovorov-1.png)

1. запись разговора может отобразиться в карточке контакта с небольшой задержкой. 2. если длительность разговора менее 6 сек, то запись разговора не сохранится в Виртуальной АТС и соответственно не отобразится в amoCRM. Если в ходе обработки вызова, сотрудники переводили его на других сотрудников, то в amoCRM будет сохранены все записи разговоров Клиентам с каждым из сотрудников; 3. при прослушивании записи разговора осуществляется проверка прав доступа сотрудника к записи согласно модели прав доступа Виртуальной АТС. Права доступа настраиваются в разделе “Безопасность и ограничения” на вкладке “Настройка доступа”. Если прав доступа недостаточно, то пользователь не сможет прослушать запись разговора. Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025
