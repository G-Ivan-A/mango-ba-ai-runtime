---
id: mdialogi-api-42-sessiya-v-sostoyanii-ozhidaniya
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.1"
pdf_section: "3.3.1"
title: "Сессия в состоянии ожидания"
pdf_heading: "3.3.1 Сессия в состоянии ожидания"
pages: "47-49"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 47-49"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"47-49","global_pages":"47-49"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 740
status: extracted
ai-generated: true
---
# 3.3.1. Сессия в состоянии ожидания

> Трассировка: PDF §3.3.1 · сквозные стр. 47-49 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.47-49.

Данный вебхук отправляется во внешнюю систему после того, как в МД будет создана новая сессия. Сессии автоматически присваивается статус "pending". Примечание. В МД новая сессия создается либо по запросу "Создать новую сессию", либо автоматически при получении первого Манго Диалоги. Справочник по API | Версия от 10.06.2026 сообщения от Клиента по тому или иному текстовому каналу коммуникации. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/on_pending Параметры вебхука:

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

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  | "group_id": 7384 |  |
| --- | --- | --- |
|  | } |  |
|  | ] |  |
|  | }, |  |
|  | "update_time": 1677577204267, |  |
|  | "variables": { |  |
|  | "social_user": { |  |
|  | "social_user_id": "7016", |  |
|  | "nickname": "Irina", |  |
|  | "photo": null, |  |
|  | "phone": "7016", |  |
|  | "first_name": "Irina", |  |
|  | "referer": "7009" |  |
|  | } |  |
|  | } |  |
|  | } |  |
|  | } |  |
