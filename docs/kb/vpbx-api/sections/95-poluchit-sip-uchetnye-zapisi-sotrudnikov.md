---
id: vpbx-api-95-poluchit-sip-uchetnye-zapisi-sotrudnikov
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.17"
pdf_section: "3.7.17"
title: "Получить sip учетные записи сотрудников"
pdf_heading: "3.7.17 Получить sip учетные записи сотрудников"
pages: "139"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 139"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"139","global_pages":"139"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 506
status: extracted
ai-generated: true
---
# 3.7.17. Получить sip учетные записи сотрудников

> Трассировка: PDF §3.7.17 · сквозные стр. 139 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.139.

POST /vpbx/sips Метод позволяет получить sip учетные записи, настроенные в Виртуальной АТС. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/sips vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  |  | Тип | Обяза-<br>тельный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | data |  |  |  |  |  |
|  |  | user_id |  | integer |  | ID сотрудника |
|  |  | sips |  |  |  |  |
|  |  |  | id | integer |  | ID SIP |
|  |  |  | login | string |  | Логин |
|  |  |  | domain | string |  | Наименование домена |

Пример ответа: { "result": 1000, "data": [ { "user_id": 300031111, "sips": [ { "id": 10031302, "login": "Login", "domain": "vpbx3000000.mangosip.ru" } ] }, { "user_id": 30002222, "sips": [] }, ]}
