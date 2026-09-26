---
id: mdialogi-api-40-zagruzka-istorii-chata
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.2.6"
pdf_section: "3.2.6"
title: "Загрузка истории чата"
pdf_heading: "3.2.6 Загрузка истории чата"
pages: "45-47"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 45-47"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"45-47","global_pages":"45-47"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 886
status: extracted
ai-generated: true
---
# 3.2.6. Загрузка истории чата

> Трассировка: PDF §3.2.6 · сквозные стр. 45-47 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.45-47.

Метод возвращает массив сообщений, которыми обменивались Клиент и оператор, в рамках определенной сессии. HTTP-запрос: POST https://app.mango-office.ru/cc/md/session/chat/history Параметры запроса:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный<br>идентификато<br>р вызова |
| chat_id | String | Да | Идентификато<br>р чата |
| since_message_id | String | Нет | Сообщения<br>старше<br>указанного |
| to_message_id | String | Нет | Сообщения<br>новее<br>указанного |
| since_time | Integer | Нет | Сообщения<br>после времени<br>(мс) |
| to_time | Integer | Нет | Сообщения до<br>времени (мс) |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| latest | Integer | Нет | Количество<br>последних<br>сообщений |
| --- | --- | --- | --- |

Пример запроса:

| { |
| --- |
| "id": "fc30", |
| "chat_id": "847b", |
| "latest": 100 |
| } |

Структура объекта Message:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| message_id | String | Да | Идентификатор<br>сообщения |
| local_message_id | String | Да | Локальный<br>идентификатор |
| time | Integer | Да | Время<br>сообщения (мс) |
| direction | String | Да | incoming/<br>outgoing |
| client_id | String | Условно | Если incoming |
| abonent_id | Integer | Условно | Если outgoing |
| payload | Object | Да | Содержимое<br>сообщения |

Возможные значения параметра direction - incoming — сообщение от Клиента к оператору; - outgoing — сообщение от оператора к Клиенту. Манго Диалоги. Справочник по API | Версия от 10.06.2026 Пример ответа:

| { |
| --- |
| "name": "OK", |
| "status": 200, |
| "code": 1000, |
| "messages": [ |
| { |
| "message_id": "4336", |
| "local_message_id": "NoRn", |
| "time": 1678107546702, |
| "direction": "incoming", |
| "client_id": "9e49", |
| "payload": { |
| "type": "text", |
| "text": "Вам видны товары в моей корзине?" |
| } |
| }, |
| { |
| "message_id": "4336", |
| "time": 1678107579452, |
| "local_message_id": "75cd", |
| "abonent_id": 4035, |
| "direction": "outgoing", |
| "payload": { |
| "type": "text", |
| "text": "К сожалению нет, не видим" |
| } |
| } |
| ] |
| } |
