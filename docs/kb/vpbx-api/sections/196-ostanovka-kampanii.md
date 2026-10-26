---
id: vpbx-api-196-ostanovka-kampanii
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.10"
pdf_section: "4.6.10"
title: "Остановка кампании"
pdf_heading: "4.6.10 Остановка кампании"
pages: "276-277"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 276-277"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"276-277","global_pages":"276-277"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 506
status: extracted
ai-generated: true
---
# 4.6.10. Остановка кампании

> Трассировка: PDF §4.6.10 · сквозные стр. 276-277 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.276-277.

POST /vpbx/campaign/stop Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | campaign_id |  |  | id кампании, обязательное |

Пример запроса: POST https://app.mango-office.ru/vpbx/campaign/stop vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "campaign_id":"16340" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result | Число | Да | Код результата |
| 2 | status | Число | Да | Текущий статус кампании.<br>Статус кампании: 0 – остановлена; 1 – запланирована;<br>2 - в работе; 3 – останавливается; 4 – завершена;<br>5 – обрабатывается; 6 – удаляется. |

Пример ответа:

| { "result": 1000,<br>"status": 0 |
| --- |
| } |

![Изображение, стр. 277](../images/196-ostanovka-kampanii-1.png)

![Изображение, стр. 277](../images/196-ostanovka-kampanii-2.png)

<!-- изображение на стр. 277: байты не извлечены (PyMuPDF недоступен) -->
