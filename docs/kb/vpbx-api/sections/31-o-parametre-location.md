---
id: vpbx-api-31-o-parametre-location
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "3.1.5"
title: "О параметре location"
pdf_heading: "О параметре location"
pages: "26-27"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 26-27"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"26-27","global_pages":"26-27"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 526
status: extracted
ai-generated: true
---
# О параметре location

> Трассировка: PDF §3.1.5 · сквозные стр. 26-27 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.26-27.

Параметр location состоит из двух определителей и имеет следующий формат: [system].[subsystem]{1,} Каждый определитель [system] имеет свои уровни [subsystem]. [subsystem]. Может быть несколько, разделяются через точку. Возможные варианты:

| system | subsystem | Описание |
| --- | --- | --- |
| ivr | "{Пункт меню N}" | N - любое натуральное число. Обозначает пункт меню, на которое<br>произошел переход после набора числа N с помощью DTMF. |

Параметр location отображает фактическое положение звонка в системе на момент сбора DTMF-клавиш, а не будущий переход, который совершит система. Такое решение позволяет избежать неоднозначности, если будущего перехода не существует (например, звонок завершится), либо требуется снять показания с конкретного блока ввода. Пример события DTMF, которые набраны в уровне 2-го блока меню: POST https://external-system.com/events/dtmf vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "seq":1, "dtmf":"124", "timestamp":"1399906980", "call_id":"100:500:256", "entry_id":"232wc3e3w3s222", "location":"ivr.2", "initiator":"79000000000", "from_number":"79000000000", "to_number":"7800123456789", "line_number":"7800123456789" }
