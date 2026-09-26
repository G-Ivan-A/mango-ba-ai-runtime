---
id: vpbx-api-75-zapros-istorii-navigacii-posetitelya-say
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.6.2"
pdf_section: "3.6.2"
title: "Запрос истории навигации посетителя сайта по динамическому номеру"
pdf_heading: "3.6.2 Запрос истории навигации посетителя сайта по динамическому номеру"
pages: "104"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 104"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"104","global_pages":"104"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 490
status: extracted
ai-generated: true
---
# 3.6.2. Запрос истории навигации посетителя сайта по динамическому номеру

> Трассировка: PDF §3.6.2 · сквозные стр. 104 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.104.

POST /vpbx/queries/user_history_by_dct_number По номеру динамического коллтрекинга выдаёт историю навигации пользователя в текущей сессии. Параметры:

| № | Параметры | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | number | string | Да | Динамический номер |

Пример запроса: POST https://app.mango-office.ru/vpbx/queries/user_history_by_dct_number vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "number": "74951112233" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с<br>уровнем<br>вложенности |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | data |  |  | Да | Массив объектов с полями |
|  |  | url | string | Да | Абсолютный адрес страницы,<br>например, http://example.ru/orders/123?param=1 |
|  |  | date | string | Да | Дата и время открытия страницы в формате UTC+3<br>(по ISO) |
|  |  | title | string | Нет | Заголовок страницы |

Примечание. Если запрос не результативен, возвращается пустой массив.
