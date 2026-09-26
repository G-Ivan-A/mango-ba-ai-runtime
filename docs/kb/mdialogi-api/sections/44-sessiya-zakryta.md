---
id: mdialogi-api-44-sessiya-zakryta
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.3"
pdf_section: "3.3.3"
title: "Сессия закрыта"
pdf_heading: "3.3.3 Сессия закрыта"
pages: "51-53"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 51-53"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"51-53","global_pages":"51-53"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 769
status: extracted
ai-generated: true
---
# 3.3.3. Сессия закрыта

> Трассировка: PDF §3.3.3 · сквозные стр. 51-53 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.51-53.

Данный вебхук отправляется во внешнюю систему после того, как сессия будет переведена из статуса "dialog" в статус "closed". Примечание. Узнать больше о процессе приема и обработки обращений от Клиента вы можете из Примера использования API. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/on_closed Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры вебхука:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор<br>события |
| session | Object | Да | Объект Session (см. раздел<br>«Объект Session») |

Пример вебхука:

|  | { |  |
| --- | --- | --- |
|  | "name": "OK", |  |
|  | "status": 200, |  |
|  | "code": 1000, |  |
|  | "session": { |  |
|  | "session_id": "aPH6", |  |
|  | "widget": { |  |
|  | "widget_id": 123, |  |
|  | "name": "Сайт", |  |
|  | "enabled": true, |  |
|  | "channels": [ |  |
|  | { |  |
|  | "channel_id": 456, |  |
|  | "type": 3, |  |
|  | "mode": "group", |  |
|  | "group_id": 7384 |  |
|  | } |  |
|  | ] |  |
|  | }, |  |
|  | "update_time": 1677, |  |
|  | "variables": { |  |
|  | "social_user": { |  |
|  | "social_user_id": "7016", |  |
|  | "nickname": "Irina", |  |
|  | "photo": null, |  |
|  | "phone": "7016", |  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  | "first_name": "Irina", |  |
| --- | --- | --- |
|  | "referer": "7009" |  |
|  | } |  |
|  | }, |  |
|  | "chat": { |  |
|  | "chat_id": "847bc", |  |
|  | "client_id": "5273" |  |
|  | }, |  |
|  | "abonent_id": 3456, |  |
|  | "closed_by_abonent_id": 3456 |  |
|  | } |  |
|  | } |  |
