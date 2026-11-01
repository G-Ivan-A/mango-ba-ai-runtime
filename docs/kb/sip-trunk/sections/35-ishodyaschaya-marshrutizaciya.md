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
tokens: 1841
images: 4
status: extracted
ai-generated: true
---
# 7.1.2. Исходящая маршрутизация

> Трассировка: PDF §7.1.2 · сквозные стр. 35-38 · источники: ч.1 `kb/sources/sip-trunk/MO_SIP_Trunk.pdf` с.35-38.

Outbound Routes - исходящая маршрутизация FreePBX. На основании набранного номера выбирается направление (транк) для исходящего вызова. Набираемый номер делится на префикс и паттерн и может модифицироваться после набора. Connectivity > Outbound Routes (Подключения > Исходящая Маршрутизация)

![Снимок экрана / схема, стр. 36](../images/35-ishodyaschaya-marshrutizaciya-2.png)

> **Описание иллюстрации SIPT-§7.1.2-1** (к §7.1.2 «Исходящая маршрутизация», стр. 36; 686×303 px). Снимок экрана / схема.
> Относится к тексту руководства: «…ова. Набираемый номер делится на префикс и паттерн и может модифицироваться после набора. Connectivity > Outbound Routes (Подключения > Исходящая Маршрутизация)».
> Текст на изображении (OCR, требует сверки): Dashboard; Хх Admin; Applications; Reports; Settings; conn; Outbound Route:; API; Add Route; DAHDI Channel DIDs; DAHDi Config; Inbound Routes; Route Settings; Dig; sport Patterns; Additional Settings; Outbound Routes; Route Name @; SIPSTATION; Route CID ©; Trunks; Override Extension @; Route Password @

![Снимок экрана / схема, стр. 36](../images/35-ishodyaschaya-marshrutizaciya-3.png)

> **Описание иллюстрации SIPT-§7.1.2-2** (к §7.1.2 «Исходящая маршрутизация», стр. 36; 946×277 px). Снимок экрана / схема.
> Относится к тексту руководства: «…ова. Набираемый номер делится на префикс и паттерн и может модифицироваться после набора. Connectivity > Outbound Routes (Подключения > Исходящая Маршрутизация)».
> Текст на изображении (OCR, требует сверки): Outbound Routes; This page is used to manage your outbound routing.; | + Add outbound Route; Outbound ср; Attributes; | Name; aoe&oO; | + from mango

![Снимок экрана / схема, стр. 37](../images/35-ishodyaschaya-marshrutizaciya-5.png)

> **Описание иллюстрации SIPT-§7.1.2-3** (к §7.1.2 «Исходящая маршрутизация», стр. 37; 883×719 px). Снимок экрана / схема.
> Относится к тексту руководства: начало раздела.
> Текст на изображении (OCR, требует сверки): Outbound Routes; Add Route; Route Settings; Dial Patterns; Import/Export Patterns; Additional Settings; Route Name @; mango; Route CID @; Override Extension @; Route Password @; Route Туре ©; Emergency; Intra-Company; Music On Hold? @; default; Time Match Time Zone: @; Use System Timezone; Time Match Time Group @; ---Permanent Route---; Trunk Sequence for Matched Routes @; Optional Destination оп Congestion @; Normal Congestion

Route name – имя маршрута Trunk Sequence for Matched Routes – выбор транка для данного маршрута Вкладка Dial Pattern Шаблон набора номера (Dial Pattern) – это уникальный набор цифр, который позволяет отправить вызов в нужный SIP–транк. Если шаблон совпадает, то вызов отправляется через SIP–транк в сторону провайдера. Шаблон набора номера имеет 4 поля настройки: Prepend, Prefix, Match Pattern и CallerID. Формат шаблона: (prepend) prefix | [ match pattern / caller ID ], где ● X - любое целое число от 0 до 9 ● Z - любое целое число от 1 до 9 ● N - любое целое число от 2 до 9 ● [#####] - любое целое число в скобках. Например, перечисление – [1.2.7], или диапазон чисел –[1.2.6-9], в который попадают числа 1,2,6,7,8,9 ● .(точка) -любой набор символов

![Снимок экрана / схема, стр. 38](../images/35-ishodyaschaya-marshrutizaciya-7.png)

> **Описание иллюстрации SIPT-§7.1.2-4** (к §7.1.2 «Исходящая маршрутизация», стр. 38; 1557×414 px). Снимок экрана / схема.
> Относится к тексту руководства: «…ое целое число в скобках. Например, перечисление – [1.2.7], или диапазон чисел –[1.2.6-9], в который попадают числа 1,2,6,7,8,9 ● .(точка) -любой набор символов».
> Текст на изображении (OCR, требует сверки): Outbound Routes; Edit Route: from mango: from mango; Route Settings; | ial patterns | Import/Export Patterns | Additional settings; Dial Patterns that will use this Route; Pattern Help; | prepena

<!-- изображение на стр. 38: байты не извлечены (PyMuPDF недоступен) -->

Поля, доступные для заполнения: Prepend - данная часть будет добавлена к номеру, перед отправкой в SIP – транк в случае совпадения шаблона. Prefix - префикс – это часть шаблона, которая будет удалена Match Pattern - Набранный номер. ВАЖНО: Asterisk ищет совпадения сопоставляя поле Prefix и Match Pattern. CallerID - данный звонок будет выполнен только в случае, если звонок инициирован с указанного CallerID. В данном поле можно использовать шаблоны. Полезно, если компания имеет несколько офисов с нумерацией виду 1XXX, 2XXX и так далее. Указанный на скриншоте шаблон 795ХХХХХХХ соответствует номерам из 10 цифр начинающимся на 795.
