---
id: vpbx-api-33-sobytie-o-zavershenii-processa-raspoznav
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.1.7"
pdf_section: "3.1.7"
title: "Событие о завершении процесса распознавания тематик в разговорах"
pdf_heading: "3.1.7 Событие о завершении процесса распознавания тематик в разговорах"
pages: "31-32"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 31-32"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"31-32","global_pages":"31-32"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 602
status: extracted
ai-generated: true
---
# 3.1.7. Событие о завершении процесса распознавания тематик в разговорах

> Трассировка: PDF §3.1.7 · сквозные стр. 31-32 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.31-32.

POST https://external-system.com/events/record/tagged Событие отправляется после того, как для записи телефонного разговора были распознаны тематики, и их можно получить через API. Примечание. В зависимости от нагрузки, запись разговора иногда не сразу доступна по API. Параметры уведомления:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | entry_id | string |  | Идентификатор группы вызовов. |
| 2 | product_id | integer |  | Идентификатор продукта. |
| 3 | user_id | integer | Да | Идентификатор связанного с записью сотрудника ВАТС.<br>Может принимать следующие значения:<br>● user_id системного пользователя (Admin), если запись<br>нельзя ассоциировать с конкретным сотрудником, но по<br>логике ВАТС вызов относится к сотруднику;<br>● значение «-1», если по логике ВАТС не удалось связать с<br>конкретным сотрудником или с системным пользователем. |
| 4 | timestamp |  |  | Время. |
| 5 | recording_id | string |  | Идентификатор записи разговора. |

Пример запроса: POST https://external-system.com/events/record/tagged vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "entry_id":"NTAwOTQxMTAyMg==", "product_id":300022532, "user_id":300049012, "timestamp":1578664187, "recording_id":"MToxMDAwNjAMDA5NDExMDIyOjE=" }
