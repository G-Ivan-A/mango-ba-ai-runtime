---
id: vpbx-api-82-poluchenie-balansa
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.6"
pdf_section: "3.7.6"
title: "Получение баланса"
pdf_heading: "3.7.6 Получение баланса"
pages: "121-122"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 121-122"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"121-122","global_pages":"121-122"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 372
status: extracted
ai-generated: true
---
# 3.7.6. Получение баланса

> Трассировка: PDF §3.7.6 · сквозные стр. 121-122 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.121-122.

POST /vpbx/account/balance Параметры запроса: пустой json Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/account/balance vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | balance |  |  | Сумма |
| 2 | currency |  |  | Валюта |
| 3 | response_at |  |  | Дата и время, на которые актуальна информации по<br>балансу. |

Пример ответа: { "result": 1000, "balance": 963592.45, "currency": "RUB", "response_at": "2019-01-24 17:55:24" }
