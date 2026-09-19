---
id: vpbx-api-34-sobytie-o-pomeschenii-zapisi-razgovora-v
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.1.8"
pdf_section: "3.1.8"
title: "Событие о помещении записи разговора в облачное хранилище"
pdf_heading: "3.1.8 Событие о помещении записи разговора в облачное хранилище"
pages: "32"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 32"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"32","global_pages":"32"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 609
status: extracted
ai-generated: true
---
# 3.1.8. Событие о помещении записи разговора в облачное хранилище

> Трассировка: PDF §3.1.8 · сквозные стр. 32 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.32.

POST https://external-system.com/events/record/added Событие отправляется после того, как запись разговора помещается в Облачное хранилище и готово к скачиванию по API. Примечание. В зависимости от нагрузки, запись разговора иногда не сразу доступна по API. Параметры уведомления:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | entry_id |  |  | Идентификатор группы вызовов |
| 2 | product_id |  |  | Идентификатор продукта |
| 3 | user_id | integer | Да | Идентификатор связанного с записью сотрудника ВАТС.<br>Возможные значения:<br>● user_id системного пользователя (Admin) - в случае, когда<br>нельзя ассоциировать с конкретным сотрудником, но по<br>логике ВАТС вызов относится к сотруднику;<br>● специальное значение -1 - в случае, когда по логике ВАТС<br>не удалось связать с конкретным сотрудником или с<br>системным пользователем. |
| 4 | timestamp | timestamp |  | Время |
| 5 | recording_id |  |  | Идентификатор записи разговора. |

Пример сообщения: POST https://external-system.com/events/record/added vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "entry_id":"NTAwOTQxMTAyMg==", "product_id":300022532, "user_id":300049012, "timestamp":1578664187, "recording_id":"MToxMDAwNjA4NTo1MDA5NDExMDIyOjE=" } }
