---
id: vpbx-api-84-poluchenie-spiska-melodiy-i-zvukovyh-soo
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.8"
pdf_section: "3.7.8"
title: "Получение списка мелодий и звуковых сообщений"
pdf_heading: "3.7.8 Получение списка мелодий и звуковых сообщений"
pages: "123-124"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 123-124"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"123-124","global_pages":"123-124"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 590
status: extracted
ai-generated: true
---
# 3.7.8. Получение списка мелодий и звуковых сообщений

> Трассировка: PDF §3.7.8 · сквозные стр. 123-124 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.123-124.

POST /vpbx/audiofiles Данная функция возвращает список мелодий общих и продукта. Общими являются мелодии, не принадлежащие конкретному продукту, для кампаний ИО могут использоваться всеми. Мелодиями продукта являются аудиофайлы, установленные от лица продукта, используются только самим продуктом. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/audiofiles vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  |  | Да | Код результата |
| 2 | audiofiles |  |  |  |  |
|  |  | id |  |  | id аудиофайла |

| № | Параметры |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  |  | name |  |  | Название аудиофайла |

Пример ответа: { "result": 1000, "audiofiles": [ { "id": 17, "name": "Abandoned" }, { "id": 20, "name": "Aisle 9 Please" }, { "id": 56, "name": "Aventura Love Story" }, { "id": 57, "name": "Bad boys blue Only one breath away" }, ... ] }
