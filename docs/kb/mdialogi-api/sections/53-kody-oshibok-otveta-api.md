---
id: mdialogi-api-53-kody-oshibok-otveta-api
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "4.2.1"
pdf_section: "4.2.1"
title: "Коды ошибок ответа API"
pdf_heading: "4.2.1 Коды ошибок ответа API"
pages: "60-62"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 60-62"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"60-62","global_pages":"60-62"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 729
status: extracted
ai-generated: true
---
# 4.2.1. Коды ошибок ответа API

> Трассировка: PDF §4.2.1 · сквозные стр. 60-62 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.60-62.

| Код | Текст | Описание |
| --- | --- | --- |
| 1000 | OK | Запрос<br>выполнен<br>успешно |
| 3100 | Authorization<br>failed | Ошибка<br>авторизации |
| 5000 | Channel not<br>found | Канал с<br>указанным<br>channel_id не<br>найден |
| 5000 | Operator not<br>found | Оператор с<br>указанным<br>abonent_id не<br>найден |
| 5000 | Group not found | Группа с<br>указанным<br>group_id не<br>найдена |
| 5000 | Message not<br>found | Сообщение с<br>указанным<br>message_id не<br>найдено |
| 5000 | Session already<br>taken | Сессия уже<br>взята в работу |
| 5000 | Session closed | Сессия<br>завершена |
| 5000 | Session not<br>found | Сессия не<br>существует |
| 5000 | Chat not found | Сессия с<br>указанным |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  |  | chat_id не<br>существует |
| --- | --- | --- |
| 5000 | Session not<br>taken | Сессия не была<br>взята в работу |
| 5000 | WhatsApp<br>session not<br>started | Нет ответа<br>клиента<br>WhatsApp |
| 5000 | Session already<br>exists | Для клиента уже<br>создано<br>обращение |
| 5000 | Channel does<br>not support<br>outgoing<br>messages | Канал не<br>поддерживает<br>исходящие<br>сообщения |
| 5000 | Widget disabled | Виджет<br>отключен |
| 5000 | Channel disabled | Канал отключен |
| 5000 | Email bot<br>unsupported | Чат‑бот не<br>может<br>обрабатывать<br>Email |
| 5000 | Operator not<br>assigned | Оператор не<br>обрабатывает<br>указанную<br>сессию |
| 5000 | Operator already<br>assigned | Оператор уже<br>обрабатывает<br>указанную<br>сессию |
| 5000 | local_message_id<br>must be unique | Значение<br>local_message_id<br>должно быть<br>уникальным |

Манго Диалоги. Справочник по API | Версия от 10.06.2026
