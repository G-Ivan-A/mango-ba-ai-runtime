---
id: vpbx-api-100-zapros-nomerov-sip-trunk-ov
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.22"
pdf_section: "3.7.22"
title: "Запрос номеров sip-trunk'ов"
pdf_heading: "3.7.22 Запрос номеров sip-trunk'ов"
pages: "143-144"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 143-144"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"143-144","global_pages":"143-144"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 583
status: extracted
ai-generated: true
---
# 3.7.22. Запрос номеров sip-trunk'ов

> Трассировка: PDF §3.7.22 · сквозные стр. 143-144 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.143-144.

POST /vpbx/trunks/numbers Метод позволяет получить информацию о sip-trunk'ах. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/trunks/numbers vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
| 1 | result |  |  |  | Код результата:<br>● 1000 - удачное выполнение;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера |

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
| 2 | data |  |  | Да | Данные |
|  |  | trunk_number_id | integer |  | ID номера sip-trunk'а |
|  |  | trunk_id | integer |  | SIP trunk id |
|  |  | number | string |  | Номер |
|  |  | options | integer |  | Опции: 2 - принять, 4 - звонить, 6 - и принять и<br>звонить |
|  |  | desc | string |  | Описание |

Пример ответа: { "result": 1000, "data": [ { "trunk_number_id": 787, "trunk_id": 460, "number": "74955358853", "options": 2, "desc": "Номер для TrunkYou 3" }, ] }
