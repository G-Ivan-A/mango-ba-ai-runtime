---
id: mdialogi-api-48-soobschenie-operatora-prochitano-kliento
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.7"
pdf_section: "3.3.7"
title: "Сообщение оператора прочитано клиентом"
pdf_heading: "3.3.7 Сообщение оператора прочитано клиентом"
pages: "56-57"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 56-57"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"56-57","global_pages":"56-57"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 550
status: extracted
ai-generated: true
---
# 3.3.7. Сообщение оператора прочитано клиентом

> Трассировка: PDF §3.3.7 · сквозные стр. 56-57 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.56-57.

Данный вебхук отправляется во внешнюю систему в том случае, если сообщение оператора прочитано Клиентом. Примечание. Узнать больше о процессе приема и обработки обращений от Клиента вы можете из Примера использования API. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/chat/on_read_message Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры вебхука:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор вызова (например, UUID).<br>Формируется внешней системой. Манго Диалоги и<br>ВАТС никак не обрабатывают этот идентификатор, не<br>анализируют и не полагаются на его уникальность. |
| chat_id | String | Да | Идентификатор чата |
| abonent_id | Integer | Да | Идентификатор сотрудника ВАТС, получатель<br>сообщения |
| message_id | String | Да | Идентификатор сообщения в МД.<br>Примечание. Все сообщения c меньшими<br>идентификаторами также считаются прочитанными. |

Пример вебхука:

|  | { |  |
| --- | --- | --- |
|  | "id": "fc30", |  |
|  | "chat_id": "847b", |  |
|  | "client_id": "9e49", |  |
|  | "message_id": "1678" |  |
|  | } |  |
