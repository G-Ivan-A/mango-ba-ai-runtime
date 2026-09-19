---
id: sip-trunk-35-ishodyaschaya-marshrutizaciya
doc_code: SIPT
doc_title: "SIP TRUNK. Руководство пользователя"
doc_version: "1.23.43"
section: "7.1.2"
pdf_section: "7.1.2"
title: "Исходящая маршрутизация"
pdf_heading: "7.1.2. Исходящая маршрутизация"
pages: "35-38"
source: kb/sources/sip-trunk/MO_SIP_Trunk.pdf
source_part: "1"
source_pages: "ч.1: 35-38"
source_refs: '[{"source_pdf":"kb/sources/sip-trunk/MO_SIP_Trunk.pdf","part":1,"pages":"35-38","global_pages":"35-38"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 995
status: extracted
ai-generated: true
---
# 7.1.2. Исходящая маршрутизация

> Трассировка: PDF §7.1.2 · сквозные стр. 35-38 · источники: ч.1 `kb/sources/sip-trunk/MO_SIP_Trunk.pdf` с.35-38.

Outbound Routes - исходящая маршрутизация FreePBX. На основании набранного номера выбирается направление (транк) для исходящего вызова. Набираемый номер делится на префикс и паттерн и может модифицироваться после набора. Connectivity > Outbound Routes (Подключения > Исходящая Маршрутизация)

![Изображение, стр. 36](../images/35-ishodyaschaya-marshrutizaciya-1.png)

![Изображение, стр. 36](../images/35-ishodyaschaya-marshrutizaciya-2.png)

![Изображение, стр. 36](../images/35-ishodyaschaya-marshrutizaciya-3.png)

![Изображение, стр. 36](../images/35-ishodyaschaya-marshrutizaciya-4.png)

![Изображение, стр. 37](../images/35-ishodyaschaya-marshrutizaciya-5.png)

![Изображение, стр. 37](../images/35-ishodyaschaya-marshrutizaciya-6.png)

Route name – имя маршрута Trunk Sequence for Matched Routes – выбор транка для данного маршрута Вкладка Dial Pattern Шаблон набора номера (Dial Pattern) – это уникальный набор цифр, который позволяет отправить вызов в нужный SIP–транк. Если шаблон совпадает, то вызов отправляется через SIP–транк в сторону провайдера. Шаблон набора номера имеет 4 поля настройки: Prepend, Prefix, Match Pattern и CallerID. Формат шаблона: (prepend) prefix | [ match pattern / caller ID ], где ● X - любое целое число от 0 до 9 ● Z - любое целое число от 1 до 9 ● N - любое целое число от 2 до 9 ● [#####] - любое целое число в скобках. Например, перечисление – [1.2.7], или диапазон чисел –[1.2.6-9], в который попадают числа 1,2,6,7,8,9 ● .(точка) -любой набор символов

![Изображение, стр. 38](../images/35-ishodyaschaya-marshrutizaciya-7.png)

<!-- изображение на стр. 38: байты не извлечены (PyMuPDF недоступен) -->

Поля, доступные для заполнения: Prepend - данная часть будет добавлена к номеру, перед отправкой в SIP – транк в случае совпадения шаблона. Prefix - префикс – это часть шаблона, которая будет удалена Match Pattern - Набранный номер. ВАЖНО: Asterisk ищет совпадения сопоставляя поле Prefix и Match Pattern. CallerID - данный звонок будет выполнен только в случае, если звонок инициирован с указанного CallerID. В данном поле можно использовать шаблоны. Полезно, если компания имеет несколько офисов с нумерацией виду 1XXX, 2XXX и так далее. Указанный на скриншоте шаблон 795ХХХХХХХ соответствует номерам из 10 цифр начинающимся на 795.
