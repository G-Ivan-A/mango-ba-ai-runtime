---
id: vpbx-api-96-poluchit-nastroennye-domeny
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.18"
pdf_section: "3.7.18"
title: "Получить настроенные домены"
pdf_heading: "3.7.18 Получить настроенные домены"
pages: "140"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 140"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"140","global_pages":"140"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 351
status: extracted
ai-generated: true
---
# 3.7.18. Получить настроенные домены

> Трассировка: PDF §3.7.18 · сквозные стр. 140 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.140.

POST /vpbx/domains Метод позволяет получить настроенные в Личном кабинете домены для Виртуальной АТС. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/domains vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | domains | string |  | Наименование домена |

Пример ответа: { "result": 1000, "domains": [ "test1.mangosip.ru", "test2.mangosip.ru" ] }
