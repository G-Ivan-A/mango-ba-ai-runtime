---
id: mdialogi-api-26-obekt-message
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "2.4.6"
pdf_section: "2.4.6"
title: "Объект Message"
pdf_heading: "2.4.6 Объект Message"
pages: "25-26"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 25-26"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"25-26","global_pages":"25-26"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 828
status: extracted
ai-generated: true
---
# 2.4.6. Объект Message

> Трассировка: PDF §2.4.6 · сквозные стр. 25-26 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.25-26.

Объект Message описывает сообщение между Клиентом и оператором.

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
|  |  |  |  |
| message_id | String | Да | Идентификатор |
|  |  |  | сообщения в МД |
|  |  |  |  |
| local_message_id | String | Да | Уникальный |
|  |  |  | локальный |
|  |  |  |  |
|  |  |  | идентификатор |
| time | Integer | Да | Unix Timestamp в |
|  |  |  | мс |
|  |  |  |  |
|  |  |  |  |
| direction | String | Да | incoming/ |
|  |  |  | outgoing |
|  |  |  |  |
|  |  |  |  |
| client_id | String | Да, с | Если incoming |
|  |  | условием |  |
|  |  |  |  |
|  |  |  |  |
| abonent_id | Integer | Да, с | Если outgoing |
|  |  | условием |  |
|  |  |  |  |
|  |  |  |  |
| payload | Object | Да | Содержимое |
|  |  |  | сообщения |
|  |  |  |  |
|  |  |  |  |

Возможные значения direction: • incoming — от клиента • outgoing — от оператора Параметры объекта payload

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
|  |  |  |  |
| type | String | Да | Тип сообщения |
|  |  |  |  |
| text | String | Да, с условием | Текст сообщения |
|  |  |  |  |
| name | String | Да, с условием | Имя файла |
|  |  |  |  |
| link | String | Да, с условием | Ссылка на файл |
|  |  |  |  |
| file_size | Integer | Да, с условием | Размер файла |
|  |  |  |  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| width | Integer | Да, с условием | Ширина изображения |
| --- | --- | --- | --- |
|  |  |  |  |
| height | Integer | Да, с условием | Высота изображения |
|  |  |  |  |
| buttons | Array | Да, с условием | Список кнопок |
|  |  |  |  |

Возможные значения type: • text — текстовое сообщение; • file — сообщение с файлом; • image — сообщение с изображением; • buttons — сообщение с кнопками; • info — информационное сообщение; • video — сообщение с видео; • audio — сообщение с аудио.
