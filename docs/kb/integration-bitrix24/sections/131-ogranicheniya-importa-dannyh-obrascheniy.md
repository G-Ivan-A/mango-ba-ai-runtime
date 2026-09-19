---
id: integration-bitrix24-131-ogranicheniya-importa-dannyh-obrascheniy
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "2.22"
title: "Ограничения импорта данных обращений"
pdf_heading: "Ограничения импорта данных обращений"
pages: "108-109"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 108-109"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"108-109","global_pages":"108-109"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 400
status: extracted
ai-generated: true
---
# Ограничения импорта данных обращений

> Трассировка: PDF §2.22 · сквозные стр. 108-109 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.108-109.

После настройки интеграции вы сможете отправлять данные обращений Контакт-центра MANGO OFFICE в свой Битрикс24. Импортированные данные будут использоваться для создания новых сделок и новых контактов в Битрикс24. Однако, необходимо учитывать определенные ограничения: • новая сделка всегда создается в Битрикс24; • новый контакт создается в Битрикс24, только если этот контакт ранее НЕ был создан. Проверка выполняется по номеру телефона Клиента. В новом контакте могут сохраняться пользовательские поля из Контакт- центра MANGO OFFICE, если вы включите соответствующую настройку; • существующий в Битрикс24 контакт не обновляется, но может быть дополнен "пользовательскими" полями из Контакт-центра MANGO OFFICE, если вы включите соответствующую настройку. Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
