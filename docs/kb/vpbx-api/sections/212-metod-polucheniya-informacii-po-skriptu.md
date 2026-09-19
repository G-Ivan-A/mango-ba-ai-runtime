---
id: vpbx-api-212-metod-polucheniya-informacii-po-skriptu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.7.3"
pdf_section: "4.7.3"
title: "Метод получения информации по скрипту(сценарию) КЦ"
pdf_heading: "4.7.3 Метод получения информации по скрипту(сценарию) КЦ"
pages: "298-299"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 298-299"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"298-299","global_pages":"298-299"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 689
status: extracted
ai-generated: true
---
# 4.7.3. Метод получения информации по скрипту(сценарию) КЦ

> Трассировка: PDF §4.7.3 · сквозные стр. 298-299 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.298-299.

POST /vpbx/script/ Метод позводяет получить ИД и имя скрипта (сценарию) КЦ. Важно! Данные о скрипте хранятся в БД ВАТС, откуда не удаляются. Однако ID скрипта может быть удален из БД. Это означает, что если вы получили ID скрипта из устаревшей истории звонка, то запрос /vpbx/script/ может не выполниться (выполниться с ошибкой), потому что указанного вами ID скрипта может уже и не быть в БД ВАТС. Параметры:

| № | Параметр | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | entry_id |  |  | ID звонка, тип данных integer, формат json |

Пример запроса: POST https://app.mango-office.ru/vpbx/script/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "entry_id":"1121" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  | Да | Результат выполнения запроса;<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31хх - неверные параметры; |

| № | Параметры |  | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | ● 3300 - объект не существует;<br>● 5xxx – ошибка сервера |
| 2 | Script |  |  |  |  |
|  |  | id | integer |  | ID скрипта |
|  |  | name | string |  |  |

Пример ответа: { "result": 1000, "script": { "id: " 1121, "name": "1" } }
