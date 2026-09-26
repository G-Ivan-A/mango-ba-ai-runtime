---
id: mdialogi-api-39-otpravit-soobschenie-operatora-k-klientu
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.2.5"
pdf_section: "3.2.5"
title: "Отправить сообщение оператора к Клиенту"
pdf_heading: "3.2.5 Отправить сообщение оператора к Клиенту"
pages: "42-45"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 42-45"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"42-45","global_pages":"42-45"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1071
status: extracted
ai-generated: true
---
# 3.2.5. Отправить сообщение оператора к Клиенту

> Трассировка: PDF §3.2.5 · сквозные стр. 42-45 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.42-45.

Метод позволяет отправить Клиенту сообщение от имени оператора. С помощью метода можно отправить: - текстовое сообщение (до 10 000 символов); - файл или изображение (размер до 50 МБ). Если передается файл, используется формат multipart/form-data. HTTP-запрос: POST https://app.mango-office.ru/cc/md/session/chat/send_message Параметры запроса

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный<br>идентификатор<br>вызова |
| chat_id | String | Да | Идентификатор<br>чата |
| abonent_id | Integer | Да | Идентификатор<br>сотрудника<br>ВАТС |
| local_message_id | String | Да | Локальный<br>идентификатор<br>сообщения |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| payload | Object | Да | Объект<br>сообщения (см.<br>раздел 2.4) |
| --- | --- | --- | --- |

Примеры запроса. 1) Текстовое сообщение

| { |
| --- |
| "id": "fc30", |
| "chat_id": "847b", |
| "abonent_id": 3645, |
| "local_message_id": "1678", |
| "payload": { |
| "type": "text", |
| "text": "Hello world!" |
| } |
| } |

2) Отправка файла (multipart/form-data)

| Content-Type: multipart/form-data; boundary="1234567890-boundary" |
| --- |
|  |
| --1234567890-boundary |
| Content-Disposition: form-data; name="request" |
| Content-Type: application/json |
|  |
| { |
| "id": "fc30", |
| "chat_id": "847b", |
| "abonent_id": 3645, |
| "local_message_id": "1678", |
| "payload": { |
| "type": "file", |
| "name": "data.zip" |
| } |
| } |
|  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| --1234567890-boundary |
| --- |
| Content-Disposition: form-data; name="file"; filename="data.zip" |
| Content-Type: application/octet-stream |
|  |
| <...........................binary data...........................> |
|  |
| --1234567890-boundary-- |

Параметры ответа:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| name | String | Да | Наименование<br>статуса HTTP |
| status | Integer | Да | Код ответа HTTP |
| code | Integer | Да | Код результата |
| error | String | Нет | Текст ошибки, если<br>она произошла |
| message | Object | Нет | Информация об<br>отправленном<br>сообщении |

Структура объекта message

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| local_message_id | String | Да | Локальный<br>идентификат<br>ор<br>сообщения |
| message_id | String | Да | Идентифика<br>тор<br>сообщения в<br>МД |
| time | Integer | Да | Время<br>отправки<br>сообщения<br>(Unix<br>Timestamp) |

Манго Диалоги. Справочник по API | Версия от 10.06.2026 Пример ответа:

| { |
| --- |
| "name": "OK", |
| "status": 200, |
| "code": 1000, |
| "message": { |
| "local_message_id": "1678", |
| "message_id": "1678", |
| "time": 1678 |
| } |
| } |
