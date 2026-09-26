---
id: mdialogi-api-33-otpravlenie-hsm
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.1.4"
pdf_section: "3.1.4"
title: "Отправление HSM"
pdf_heading: "3.1.4 Отправление HSM"
pages: "31-34"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 31-34"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"31-34","global_pages":"31-34"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1536
status: extracted
ai-generated: true
---
# 3.1.4. Отправление HSM

> Трассировка: PDF §3.1.4 · сквозные стр. 31-34 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.31-34.

Метод позволяет отправить Клиенту сообщение в соответствии с тем или иным уже созданным HSM-шаблоном (HSM-сообщение). HTTP-запрос: POST /cc/md/hsm/send_message Параметры запроса:

| № | Параметр |  |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | id |  |  | Строка | Да | Уникальный<br>идентификатор вызова,<br>например UUID,<br>используется для<br>логирования и отладки |
| 2 | social_user_id |  |  | Строка | Да | Номер телефона в<br>WhatsApp |
| 3 | channel_id |  |  | Целое | Да | Идентификатор канала |
| 4 | template_id |  |  | Целое | Да | Идентификатор шаблона,<br>используемого при<br>формировании HSM |
| 5 | creator_abo<br>nent_id |  |  | Целое | Да | Идентификатор<br>сотрудника MANGO<br>OFFICE, отправитель<br>сообщения |
| 6 | parameters |  |  | Объект | Да | Динамические данные<br>шаблона HSM |
| 6.1 |  | bindings |  | Массив<br>строк | Да | Переменные основного<br>текста шаблона |
| 6.2 |  | header |  | Объект | Нет | Данные заголовка |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  |  |  | сontent | Строка | Нет | Ссылка на файл для<br>заголовка |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | bindings | Массив<br>строк | Нет | Переменные текста<br>заголовка шаблона |

Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Подробнее об этих обязательных полях… Пример запроса:

|  | POST https://app.mango-office.ru/cc/md/hsm/send_message |  |
| --- | --- | --- |
|  |  |  |
|  | vpbx_api_key = qwerty123 |  |
|  | sign = qwerty123 |  |
|  |  |  |
|  | json = { |  |
|  | "id": "qwerty123", |  |
|  | "social_user_id": "74955404444", |  |
|  | "channel_id": 11111, |  |
|  | "template_id": 22222, |  |
|  | "creator_abonent_id": 33333, |  |
|  | "parameters": { |  |
|  | "bindings": ["Иванов Иван"], |  |
|  | "header": { |  |
|  | "content": "https://image.png", |  |
|  | "bindings": ["Иванов Иван"] |  |
|  | } |  |
|  | } |  |
|  | } |  |

Параметры ответа:

| № | Параметры |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | name |  | Строка | Да | Наименование статуса<br>HTTP |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| 2 | status |  | Целое | Да | Статус HTTP |
| --- | --- | --- | --- | --- | --- |
| 3 | code |  | Целое | Да | Код результата |
| 4 | error |  | Строка | Нет | Текст ошибки, если она<br>произошла |
| 5 | message |  | Объект | Да | Объект Message (см.<br>раздел «Объект<br>Message») |
| 5.1 |  | local_messa ge_id | Строка | Да | Локальный<br>идентификатор<br>отправляемого<br>сообщения. |
| 5.2 |  | message_id | Строка | Да | Идентификатор<br>сообщения на<br>сервере |
| 5.3 |  | time | Целое | Да | Время отправки<br>сообщения в Unix Time<br>в миллисекундах |
| 5.4 |  | session_id | Строка |  | Идентификатор<br>сессии |

Пример успешного ответа:

| { |
| --- |
| "name": "OK", |
| "status": 200, |
| "code": 1000, |
| "message": { |
| "local_message_id": "92f7cc123000ecadfe6f0f680972098e", |
| "message_id": "449026466343509280", |
| "time": 1738009633316, |
| "session_id": "mFv5u7SUXl6N+FE/pOsAIMd+" |
| } |
| } |

Пример неуспешного ответа:

| { |
| --- |
| "result": 3000, |
| "error": "error-address-format" |
| } |

Манго Диалоги. Справочник по API | Версия от 10.06.2026
