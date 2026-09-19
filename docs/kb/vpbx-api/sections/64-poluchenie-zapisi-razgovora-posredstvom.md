---
id: vpbx-api-64-poluchenie-zapisi-razgovora-posredstvom
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.5.1"
pdf_section: "3.5.1"
title: "Получение записи разговора посредством POST запроса"
pdf_heading: "3.5.1 Получение записи разговора посредством POST запроса"
pages: "87-88"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 87-88"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"87-88","global_pages":"87-88"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 466
status: extracted
ai-generated: true
---
# 3.5.1. Получение записи разговора посредством POST запроса

> Трассировка: PDF §3.5.1 · сквозные стр. 87-88 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.87-88.

POST /vpbx/queries/recording/post Наиболее защищенный способ получения записи разговора. Возвращаемые в перенаправлениях ссылки являются временными, срок их жизни ограничен, после первого доступа к файлу ссылки будут недействительными, поэтому они не должны сохраняться внешней системой. Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | recording_id |  |  | Идентификатор записи разговора |
| 2 | action |  |  | Разрешенные значения download, play |

Примеры. Запрос: POST https://app.mango-office.ru/vpbx/queries/recording/post vpbx_api_key = 1234567890qwerty, sign = 1234567890qwert, json = { "recording_id": "d12a45f67b90c12345", "action": "play" } Ответ API: 302 Found ... Location: https://files.mango-office.ru/sdwee3en38fh328923943534ff3d2jh2d .... Запрос: GET https://files.mango-office.ru/sdwee3en38fh328923943534ff3d2jh2d ...... Ответ сервиса доступа к файлам: 200 OK ... Content-Type: audio/mp3 Content-Length: 16099.
