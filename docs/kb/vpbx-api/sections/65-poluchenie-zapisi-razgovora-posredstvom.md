---
id: vpbx-api-65-poluchenie-zapisi-razgovora-posredstvom
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.5.2"
pdf_section: "3.5.2"
title: "Получение записи разговора посредством GET запроса без авторизации"
pdf_heading: "3.5.2 Получение записи разговора посредством GET запроса без авторизации"
pages: "88-89"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 88-89"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"88-89","global_pages":"88-89"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 729
status: extracted
ai-generated: true
---
# 3.5.2. Получение записи разговора посредством GET запроса без авторизации

> Трассировка: PDF §3.5.2 · сквозные стр. 88-89 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.88-89.

GET /vpbx/queries/recording/link/[recording_id]/[action]/[vpbx_api_key]/[timestamp]/[si gn] Внешней системе предоставляется возможность генерации и использования ссылок для скачивания/воспроизведения записей разговоров. Данная возможность по умолчанию выключена, требуется явное включение в Личном кабинете. Внешняя система может сама управлять временем жизни генерируемой ею ссылки. Возвращаемые в перенаправлении ссылки являются временными, срок их жизни ограничен, после первого доступа к файлу ссылки будут недействительными, поэтому они не должны сохраняться внешней системой. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | recording_id |  |  | Идентификатор записи разговора |
| 2 | action |  |  | Разрешенные значения download, play |
| 3 | timestamp | timestamp |  | Часовой пояс UTC+3, время до которого действует ссылка |
| 4 | vpbx_api_key |  |  | Ключ доступа пользователя к API (выдан при регистрации<br>внешней системы) |
| 5 | sign |  |  | Подпись |

Важно! В данном запросе для рассчета параметра sign следует использовать следующую формулу: sign=sha256(vpbx_api_key + timestamp + recording_id + vpbx_api_salt) Примеры. Запрос: GET https://app.mango- office.ru/vpbx/queries/recording/link/0d0a984b45c0/play/5f4dcaa765d61d8327deb882cf9 9/:/188c920769765c1b226aa1a40a9ce1bf9f46b48d81fc386aafeb Ответ API: 302 Found ... Location: https://files.mango-office.ru/sdwee3en38fh328923943534ff3d2jh2d .... Запрос: GET https://files.mango-office.ru/sdwee3en38fh328923943534ff3d2jh2d ...... Ответ сервиса доступа к файлам: 200 OK ... Content-Type: audio/mpeg Content-Length: 16099 ...
