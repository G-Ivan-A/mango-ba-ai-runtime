---
id: mdialogi-api-68-poluchenie-statusov-otpravlennyh-hsm-soo
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "6.2"
pdf_section: "6.2"
title: "Получение статусов отправленных HSM-сообщений"
pdf_heading: "6.2 Получение статусов отправленных HSM-сообщений"
pages: "91-93"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 91-93"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"91-93","global_pages":"91-93"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 749
status: extracted
ai-generated: true
---
# 6.2. Получение статусов отправленных HSM-сообщений

> Трассировка: PDF §6.2 · сквозные стр. 91-93 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.91-93.

Метод позволяет получить статус ранее отправленного HSM- сообщения. HTTP-запрос: POST /cc/get_mcw_message_status Параметры запроса:

| № | Параметры | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | messageIds | Массив |  | Список сообщений, для которых<br>нужно получить статус |

Примечание. Согласно модели взаимодействия, в POST- запросах отправляются обязательные поля vpbx_api_key и sign. Подробнее об этих обязательных полях… Пример запроса:

| POST https://app.mango-office.ru/cc/get_mcw_message_status |
| --- |
|  |
| vpbx_api_key=1234567890qwerty |
| sign=1234567890qwerty |
|  |
| json={ |
| "messageIds": [ |
| "2135567.007" |
| ] |
| } |

Манго Диалоги. Справочник по API | Версия от 10.06.2026 Параметры ответа. Данные возвращаются в теле ответа в формате JSON:

| № | Параметр |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  | Число | Да | Код результата |
| 2 | statuses |  | Массив |  | Статус |
| 3 | result |  | Массив |  | Список объектов |
| 3.1 |  | messageId | Строка |  | id сообщения |
|  |  | status | Строка |  | Статус сообщения. Может иметь<br>значения:<br>• sended - сообщение принято<br>на доставку;<br>• delivered - сообщение<br>доставлено;<br>• read - сообщение<br>прочитано;<br>• error - возникла<br>ошибка. |
|  |  | time | Временная<br>метка |  | Дата / время события |

Пример ответа:

| { |
| --- |
| "result": 1000, |
| "statuses": { |
| "result": [ |
| { |
| "messageId": "1655452135567.007", |
| "status": "read", |
| "time": "2022-06-17T07:49:38.000Z" |
| } |
| ] |
| } |
| } |

Манго Диалоги. Справочник по API | Версия от 10.06.2026
