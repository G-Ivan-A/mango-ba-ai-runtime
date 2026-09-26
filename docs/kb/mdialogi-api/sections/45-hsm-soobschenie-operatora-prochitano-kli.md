---
id: mdialogi-api-45-hsm-soobschenie-operatora-prochitano-kli
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.3.4"
pdf_section: "3.3.4"
title: "HSM-сообщение оператора прочитано клиентом"
pdf_heading: "3.3.4 HSM-сообщение оператора прочитано клиентом"
pages: "53-54"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 53-54"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"53-54","global_pages":"53-54"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 605
status: extracted
ai-generated: true
---
# 3.3.4. HSM-сообщение оператора прочитано клиентом

> Трассировка: PDF §3.3.4 · сквозные стр. 53-54 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.53-54.

В МД существует возможность отправлять Клиентам HSM-сообщения через WhatsApp, при подключении к Виртуальной АТС услуги "WhatsApp Business API (провайдер Edna)". HSM - (highly-structured message) шаблонизированное сервисное сообщение, отправляемое Клиентам через WhatsApp Business. Данный вебхук отправляется во внешнюю систему после того, как из МД было отправлено Клиенту HSM-сообщение и данное сообщение было прочитано Клиентом. HTTP-запрос:

| POST https://external- |
| --- |
| system.ru/events/cc/md/session/on_read_message |

Параметры вебхука:

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| id | String | Да | Уникальный идентификатор вызова (например,<br>UUID). Формируется внешней системой. Манго<br>Диалоги и ВАТС никак не обрабатывают этот<br>идентификатор, не анализируют и не<br>полагаются на его уникальность |
| session_id | String | Да | Идентификатор сессии |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| social_user_id | String | Да | Уникальный идентификатор пользователя в<br>соц. сети (Клиента) |
| --- | --- | --- | --- |
| message_id | String | Да | Идентификатор сообщения в МД |

Пример вебхука:

|  | { |  |
| --- | --- | --- |
|  | "id": "fc30", |  |
|  | "session_id": "DA0h", |  |
|  | "social_user_id":"3645", |  |
|  | "message_id": "199a" |  |
|  | } |  |
