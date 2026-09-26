---
id: mdialogi-api-38-zakryt-sessiyu
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.2.4"
pdf_section: "3.2.4"
title: "Закрыть сессию"
pdf_heading: "3.2.4 Закрыть сессию"
pages: "41-42"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 41-42"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"41-42","global_pages":"41-42"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 645
status: extracted
ai-generated: true
---
# 3.2.4. Закрыть сессию

> Трассировка: PDF §3.2.4 · сквозные стр. 41-42 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.41-42.

Метод позволяет принудительно закрыть сессию в статусе "dialog". Закрыть сессию в статусе "pending" невозможно. HTTP-запрос: POST https://app.mango-office.ru/cc/md/session/close Параметры запроса:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор вызова (например, UUID).<br>Формируется внешней системой. Манго Диалоги и<br>ВАТС никак не обрабатывают этот идентификатор, не<br>анализируют и не полагаются на его уникальность. |
| session_id | String | Да | Идентификатор сессии (этот идентификатор можно<br>получить при помощи запроса "Получить список<br>активных сессий). |
| abonent_id | Integer | Да | Идентификатор сотрудника ВАТС, закрывающего<br>сессию.<br>Узнать список сотрудников ВАТС и их<br>идентификаторы вы можете при помощи API MANGO<br>OFFICE или API Realtime. |

Пример запроса:

| { |
| --- |
| "id": "fc30", |
| "session_id": "3xJn", |
| "abonent_id": 3645 |
| } |

Параметры ответа:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| name | String | Да | Наименование статуса HTTP |
| status | Integer | Да | Код ответа HTTP |
| code | Integer | Да | Код результата (список) |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| error | String | Нет | Текст ошибки, если она произошла |
| --- | --- | --- | --- |

Пример ответа:

| { |
| --- |
| "name": "OK", |
| "status": 200, |
| "code": 1000 |
| } |
