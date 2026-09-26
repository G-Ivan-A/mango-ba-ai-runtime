---
id: mdialogi-api-43-sessiya-vzyata-v-rabotu
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.2"
pdf_section: "3.3.2"
title: "Сессия взята в работу"
pdf_heading: "3.3.2  Сессия взята в работу"
pages: "49-51"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 49-51"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"49-51","global_pages":"49-51"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 756
status: extracted
ai-generated: true
---
# 3.3.2. Сессия взята в работу

> Трассировка: PDF §3.3.2 · сквозные стр. 49-51 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.49-51.

Данный вебхук отправляется во внешнюю систему после того, как сессия будет переведена из статуса "pending" в статус "dialog". Примечание. Узнать больше о процессе приема и обработки обращений от Клиента вы можете из Примера использования API. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/on_dialog Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры вебхука:

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

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  | "variables": { |  |
| --- | --- | --- |
|  | "social_user": { |  |
|  | "social_user_id": "7016", |  |
|  | "nickname": "Irina", |  |
|  | "photo": null, |  |
|  | "phone": "7016", |  |
|  | "first_name": "Irina", |  |
|  | "referer": "7009" |  |
|  | } |  |
|  | }, |  |
|  | "chat": { |  |
|  | "chat_id": "847b", |  |
|  | "client_id": "5273" |  |
|  | }, |  |
|  | "abonent_id": 3456 |  |
|  | } |  |
|  | } |  |
