---
id: mdialogi-api-47-soobschenie-operatora-dostavleno-klientu
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.6"
pdf_section: "3.3.6"
title: "Сообщение оператора доставлено клиенту"
pdf_heading: "3.3.6 Сообщение оператора доставлено клиенту"
pages: "55-56"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 55-56"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"55-56","global_pages":"55-56"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 553
status: extracted
ai-generated: true
---
# 3.3.6. Сообщение оператора доставлено клиенту

> Трассировка: PDF §3.3.6 · сквозные стр. 55-56 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.55-56.

Данный вебхук отправляется во внешнюю систему в том случае, если сообщение оператора доставлено Клиенту. Примечание. Узнать больше о процессе приема и обработки обращений от Клиента вы можете из Примера использования API. HTTP-запрос: POST https://external-system.ru/events/cc/md/session/chat/on_recv_message Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры вебхука:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор вызова (например, UUID).<br>Формируется внешней системой. Манго Диалоги и<br>ВАТС никак не обрабатывают этот идентификатор, не<br>анализируют и не полагаются на его уникальность. |
| chat_id | String | Да | Идентификатор чата |
| abonent_id | Integer | Да | Идентификатор сотрудника ВАТС, получатель<br>сообщения |
| message_id | String | Да | Идентификатор сообщения в МД.<br>Примечание. Все сообщения c меньшими<br>идентификаторами также считаются полученными |

Пример вебхука:

|  | { |  |
| --- | --- | --- |
|  | "id": "fc30", |  |
|  | "chat_id": "847b", |  |
|  | "abonent_id": 3645, |  |
|  | "message_id": "1678" |  |
|  | } |  |
|  |  |  |
