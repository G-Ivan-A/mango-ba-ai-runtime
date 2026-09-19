---
id: integration-bitrix24-181-zapis-razgovorov
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "3.7"
pdf_section: "3.7"
title: "Запись разговоров"
pdf_heading: "3.7 Запись разговоров"
pages: "159-160"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 159-160"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"159-160","global_pages":"159-160"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 421
status: extracted
ai-generated: true
---
# 3.7. Запись разговоров

> Трассировка: PDF §3.7 · сквозные стр. 159-160 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.159-160.

Если в Виртуальной АТС подключена услуга записи разговоров и в настройках API включен флаг "Предоставлять возможность генерации и использования ссылок" (см. Настройка Виртуальной АТС MANGO OFFICE, п.4), то при наличии записи разговора ее можно прослушать в Битрикс24:

![Изображение, стр. 159](../images/181-zapis-razgovorov-1.png)

Примечания: 1. Запись разговора может отобразиться в карточке контакта с небольшой задержкой. 2. Если длительность разговора менее 6 сек, то запись разговора не сохранится в Виртуальной АТС и соответственно не отобразится в Битрикс24. Если в ходе обработки вызова, сотрудники переводили его на других сотрудников, то в Битрикс24 будет сохранены все записи разговоров Клиентам с каждым из сотрудников. Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
