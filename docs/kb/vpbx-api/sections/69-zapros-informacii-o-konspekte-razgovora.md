---
id: vpbx-api-69-zapros-informacii-o-konspekte-razgovora
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.5.6"
pdf_section: "3.5.6"
title: "Запрос информации о конспекте разговора"
pdf_heading: "3.5.6 Запрос информации о конспекте разговора"
pages: "94"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 94"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"94","global_pages":"94"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 627
status: extracted
ai-generated: true
---
# 3.5.6. Запрос информации о конспекте разговора

> Трассировка: PDF §3.5.6 · сквозные стр. 94 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.94.

POST /s2t/queries/recording_summary Описание Метод предназначен для получения информации о резюме разговора. Параметры запроса:

| № | Параметры | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | communicati<br>on_id | array<br>[string] | Да | Массив id коммуникации |

Тело запроса должно быть в формате json, например: { "communication_id": [ "MzAwMTMwMzIyMg==", "MzAwMTMwMzIyMw==" ] }

| № | Параметры с уровнями<br>вложенности |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  | integer | Да | Код статуса результата ответа |
| 2 | data |  | объект | Да | Данные коммуникации |
| 2.1 |  | communicati<br>on_id | array<br>[string] | Да | Массив id коммуникации |
| 2.2 |  | summary | string | Да | Расшифровка коммуникации |

Пример ответа: { "result": 1000, "data": [ { "communication_id": "MzAwMTMwMzIyMg==", "summary": "1. Цель звонка: клиент обратился с проблемой настройки связи для приёма звонков во время прямого эфира.\\n2. Запрос клиента: клиент пожаловался на отсутствие поступающих звонков, несмотря на предварительную настройку связи.\\n3. Итоги встречи: сотрудник компании начал диагностику проблемы, но пока не может её решить." } ] } Методы данного раздела работают, только если используется Речевая аналитика
