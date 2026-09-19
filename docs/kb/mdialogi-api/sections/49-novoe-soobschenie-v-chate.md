---
id: mdialogi-api-49-novoe-soobschenie-v-chate
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.8"
pdf_section: "3.3.8"
title: "Новое сообщение в чате"
pdf_heading: "3.3.8 Новое сообщение в чате"
pages: "57-59"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 57-59"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"57-59","global_pages":"57-59"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 580
status: extracted
ai-generated: true
---
# 3.3.8. Новое сообщение в чате

> Трассировка: PDF §3.3.8 · сквозные стр. 57-59 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.57-59.

Данный вебхук отправляется во внешнюю систему, когда Клиент либо оператор отправил сообщение. Примечание. Узнать больше о процессе приема и обработки обращений от Клиента вы можете из Примера использования API. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/chat/on_message Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры вебхука:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор вызова |
| session_id | String | Да | Идентификатор сессии |
| chat_id | String | Да | Идентификатор чата |
| message_id | Object | Да | Объект Message (см. раздел «Объект Message») |

Пример вебхука:

|  | { |  |
| --- | --- | --- |
|  | "id": "fc30", |  |
|  | "session_id": "DA0h" |  |
|  | "chat_id": "847b", |  |
|  | "client_id": "9e49", |  |
|  | "message": { |  |
|  | "message_id": "4336", |  |
|  | "local_message_id": "NoRn", |  |
|  | "time": 1678107546702, |  |
|  | "direction": "incoming", |  |
|  | "client_id": "9e49", |  |
|  | "payload": { |  |
|  | "type": "text", |  |
|  | "text": "Вам видны товары в моей корзине?" |  |
|  | } |  |
|  | } |  |
|  | } |  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026
