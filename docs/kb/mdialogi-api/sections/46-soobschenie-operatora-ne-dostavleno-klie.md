---
id: mdialogi-api-46-soobschenie-operatora-ne-dostavleno-klie
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.5"
pdf_section: "3.3.5"
title: "Сообщение оператора не доставлено клиенту"
pdf_heading: "3.3.5 Сообщение оператора не доставлено клиенту"
pages: "54-55"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 54-55"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"54-55","global_pages":"54-55"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 444
status: extracted
ai-generated: true
---
# 3.3.5. Сообщение оператора не доставлено клиенту

> Трассировка: PDF §3.3.5 · сквозные стр. 54-55 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.54-55.

Данный вебхук отправляется во внешнюю систему в том случае, если сообщение оператора не удалось доставить Клиенту. Примечание В текущей версии API используется вебхук /events/cc/md/session/chat/on_error_message Если ранее в интеграции использовался вебхук /events/cc/md/session/on_error_message то необходимо заменить его на новый URL. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/chat/on_error_message Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры вебхука

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор события |
| chat_id | String | Да | Идентификатор чата |
| message_id | String | Да | Идентификатор сообщения в МД |
| error | String | Да | Код ошибки доставки сообщения |

Примечание Расшифровка кодов ошибок приведена в разделе 4.2 Возможные коды ошибок. Пример вебхука

| { |
| --- |
| "id": "fc30", |
| "chat_id": "DA0h", |
| "message_id": "199a", |
| "error": "address-error" |
| } |
