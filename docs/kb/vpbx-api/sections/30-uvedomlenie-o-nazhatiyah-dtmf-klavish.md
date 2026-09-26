---
id: vpbx-api-30-uvedomlenie-o-nazhatiyah-dtmf-klavish
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.1.5"
pdf_section: "3.1.5"
title: "Уведомление о нажатиях DTMF клавиш"
pdf_heading: "3.1.5 Уведомление о нажатиях DTMF клавиш"
pages: "26"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 26"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"26","global_pages":"26"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 734
status: extracted
ai-generated: true
---
# 3.1.5. Уведомление о нажатиях DTMF клавиш

> Трассировка: PDF §3.1.5 · сквозные стр. 26 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.26.

POST https://external-system.com/events/dtmf Уведомление содержит информацию о нажатиях DTMF-клавиш. Такое событие генерируется в сценарии, когда абонент находится в IVR-меню и нажимает DTMF-клавиши на устройстве. Фиксируются и отправляются не единичные нажатия, а факт сбора полной значимой последовательности (пакета) нажатий одной или нескольких DTMF-клавиш. Факт сбора последовательности определяется логикой ВАТС и текущим положением в IVR-меню. Параметры уведомления:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | seq |  |  | Счетчик последовательности уведомлений по фактам сбора<br>пакетов DTMF-клавиш. |
| 2 | dtmf | string |  | Строка, представляющая собранную последовательность. |
| 3 | timestamp |  |  | Время события UTC+3. |
| 4 | call_id |  |  | Внутренний идентификатор вызова, строка не более 128 байт.<br>Не имеет отношения к CALL-ID из SIP-протокола. |
| 5 | entry_id |  |  | Внутренний идентификатор группы вызовов. Не имеет<br>отношения к CALL-ID из SIP-протокола. |
| 6 | location |  |  | Текущее расположение вызова в системе ВАТС. Подробнее… |
| 7 | initiator | string | Да | Тип данных строковый, номер абонента, который ввел DTMF. |
| 8 | from_number | string | Нет | Тип данных строковый, номер вызывающего абонента, в<br>случае, если ВАТС удалось определить номер. |
| 9 | to_number | string | Нет | Тип данных строковый, номер вызываемого абонента. |
| 10 | line_number | string | Нет | Тип данных строковый, линия ВАТС, на которую поступил<br>вызов. |
