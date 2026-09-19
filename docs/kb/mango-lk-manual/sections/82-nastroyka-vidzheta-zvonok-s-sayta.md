---
id: mango-lk-manual-82-nastroyka-vidzheta-zvonok-s-sayta
doc_code: LK
doc_title: "Виртуальная АТС MANGO OFFICE - Справочник абонента"
doc_version: "1.23"
section: "4.2.3.2"
pdf_section: "4.2.3.2"
title: "Настройка виджета «Звонок с сайта»"
pdf_heading: "4.2.3.2 Настройка виджета «Звонок с сайта»"
pages: "80-81"
source: kb/sources/mango-lk-manual/LK_manual_v-123.pdf
source_part: "1"
source_pages: "ч.1: 80-81"
source_refs: '[{"source_pdf":"kb/sources/mango-lk-manual/LK_manual_v-123.pdf","part":1,"pages":"80-81","global_pages":"80-81"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 471
status: extracted
ai-generated: true
---
# 4.2.3.2. Настройка виджета «Звонок с сайта»

> Трассировка: PDF §4.2.3.2 · сквозные стр. 80-81 · источники: ч.1 `kb/sources/mango-lk-manual/LK_manual_v-123.pdf` с.80-81.

Если для этого продукта ранее не создавались учетные записи SIP, то открытии формы будут автоматически созданы: • входящая IP-линия (учетная запись SIP) в этом поддомене; • схема переадресации для этой входящей линии. При этом используется формат учетной записи вида lineNNNNN@vpbxXXXXXXX.mangosip.ru, где: • NNNNN — случайный пятизначный номер; • vpbxXXXXXXX.mangosip.ru — поддомен SIP, который автоматически генерируется системой при создании продукта; • XXXXXXX — уникальный системный идентификатор текущего продукта.

![Изображение, стр. 81](../images/82-nastroyka-vidzheta-zvonok-s-sayta-1.jpeg)

Созданная внешняя линия автоматически используется для вызова при помощи виджета, а сгенерированная для нее схема переадресации подставляется в поле «Схема» в настройках распределения звонков. Настройка виджета осуществляется при помощи дополнительной формы с четырьмя вкладками: • Основные; • Расписание; • Внешний вид; • Код для вставки.
