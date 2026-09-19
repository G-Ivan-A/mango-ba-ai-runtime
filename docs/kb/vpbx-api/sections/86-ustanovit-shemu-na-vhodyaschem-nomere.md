---
id: vpbx-api-86-ustanovit-shemu-na-vhodyaschem-nomere
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.10"
pdf_section: "3.7.10"
title: "Установить схему на входящем номере"
pdf_heading: "3.7.10 Установить схему на входящем номере"
pages: "127-128"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 127-128"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"127-128","global_pages":"127-128"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 721
status: extracted
ai-generated: true
---
# 3.7.10. Установить схему на входящем номере

> Трассировка: PDF §3.7.10 · сквозные стр. 127-128 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.127-128.

POST /vpbx/schema/set Настройка схем переадресации выполняется в Личном кабинете. Можно, к примеру, заранее настроить несколько схем и средствами API, при помощи описанного ниже метода, оперативно переключать их на номерах со стороны внешней системы. Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | schema _id |  | Да | id схемы, можно получить запросом списка схем |
| 2 | line_id |  | Да | id линии, можно получить запросом списка номеров |
| 3 | trunk_number_id | integer | Нет | Тип данных, опционально, id номера sip-trunk'a исходящего<br>номера (у номера поле options должно быть 2 или 6) |

В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  |  | Код результата:<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31XX - неверные параметры;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера; |
| 2 | data |  | Да | В виде сплошной строки текста |

Примеры запросов. Пример 1. Запрос без номера sip-trunk'a: Запрос: POST https://app.mango-office.ru/vpbx/schema/set vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "schema_id":"11004848", "line_id":"300049196" } Ответ: { "result": 1000 } Пример 2. Запрос с указанием номера sip-trunk'a: Запрос: POST https://app.mango-office.ru/vpbx/schema/set vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "schema_id":"11004848", "trunk_number_id":"829" } Ответ: { "result": 1000 }
