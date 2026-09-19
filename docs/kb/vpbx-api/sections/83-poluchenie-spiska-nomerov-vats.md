---
id: vpbx-api-83-poluchenie-spiska-nomerov-vats
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.7"
pdf_section: "3.7.7"
title: "Получение списка номеров ВАТС"
pdf_heading: "3.7.7 Получение списка номеров ВАТС"
pages: "122-123"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 122-123"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"122-123","global_pages":"122-123"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 854
status: extracted
ai-generated: true
---
# 3.7.7. Получение списка номеров ВАТС

> Трассировка: PDF §3.7.7 · сквозные стр. 122-123 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.122-123.

POST /vpbx/incominglines Метод позволяет получить список номеров, привязанных к ВАТС, без информации о sip-trunk`ах, для этого есть отдельный метод (см. Получение номеров транков) Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/incominglines vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнем<br>вложенности |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  | Да | Код результата:<br>● 1000 - удачное выполнение;<br>● 3300 - объект не существует |
| 2 | lines |  |  |  |  |
| 2.1 |  | line_id |  |  | Уникальный ID линии |
| 2.2 |  | number |  |  | Номер |
| 2.3 |  | name |  |  | Пользовательское описание номера (для SIP линий) |
| 2.4 |  | comment |  |  | Комментарий к номеру, задается в Личном кабинете ВАТС |
| 2.5 |  | region |  |  | Тип региона номера. Для активных sip-линий передается<br>"sip-uac", пассивных - "sip", для номеров 7800 - "toll-free" |
| 2.6 |  | schema_id |  |  | Уникальный ID схемы распределения, заданной для<br>номера |

| № | Параметры с уровнем<br>вложенности |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- |
| 2.7 |  | schema_name |  |  | Название схемы распределения, заданной для номера |

Пример ответа: { "result": 1000, "lines": [ { "line_id": 300015801, "number": "sip:main_uri_my@mangosip.ru", "name": "майн", "comment": "сип линия", "region": "sip", "schema_id": 11000849, "schema_name": "Мое название схемы" }, { "line_id": 300024487, "number": "78124072916", "name": null, "comment": null, "region": "2", "schema_id": 10000008, "schema_name": "По умолчанию" } ] }
