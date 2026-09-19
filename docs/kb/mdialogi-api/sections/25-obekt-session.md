---
id: mdialogi-api-25-obekt-session
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "2.4.5"
pdf_section: "2.4.5"
title: "Объект Session"
pdf_heading: "2.4.5 Объект Session"
pages: "23-25"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 23-25"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"23-25","global_pages":"23-25"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1087
status: extracted
ai-generated: true
---
# 2.4.5. Объект Session

> Трассировка: PDF §2.4.5 · сквозные стр. 23-25 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.23-25.

Объект Session содержит информацию о сессии коммуникации между Клиентом и оператором.

| Параметр | Тип | Обязательн | Описание |
| --- | --- | --- | --- |
|  |  | ое |  |
| session_id | String | Да | Идентификато |
|  |  |  | р сессии |
|  |  |  |  |
| group_id | Integer | Нет | Идентификато |
|  |  |  | р группы, |
|  |  |  |  |
|  |  |  | обрабатываю |
|  |  |  | щей сессию |
| abonent_id | Integer | Нет | Идентификато |
|  |  |  | р сотрудника, |
|  |  |  |  |
|  |  |  | обрабатываю |
|  |  |  | щего сессию |
| chat | Object | Нет | Объект Chat |
|  |  |  | (см. раздел |
|  |  |  |  |
|  |  |  | «Объект |
|  |  |  | Chat»). |
|  |  |  | Передается |
|  |  |  | после взятия |
|  |  |  | сессии в |
|  |  |  | работу |
| parent_session_id | String | Нет | Идентификато |
|  |  |  | р |
|  |  |  |  |
|  |  |  | родительской |
|  |  |  | сессии |
| root_session_id | String | Нет | Идентификато |
|  |  |  | р корневой |
|  |  |  |  |
|  |  |  | сессии |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| widget | Object | Да | Объект Widget |
| --- | --- | --- | --- |
|  |  |  | (см. раздел |
|  |  |  |  |
|  |  |  | «Объект |
|  |  |  | Widget») |
|  |  |  | В массиве |
|  |  |  | channels |
|  |  |  | передается |
|  |  |  | только один |
|  |  |  | канал |
| update_time | Integer | Да | Время |
|  |  |  | обновления |
|  |  |  |  |
|  |  |  | сессии, Unix |
|  |  |  | Timestamp в |
|  |  |  | миллисекунда |
|  |  |  | х |
| state | String | Да | Состояние |
|  |  |  | сессии |
|  |  |  |  |
|  |  |  |  |
| variables | Object | Да | Набор |
|  |  |  | дополнительн |
|  |  |  |  |
|  |  |  | ых |
|  |  |  | переменных |
| social_user | Object | Да | Объект |
|  |  |  | SocialUser (см. |
|  |  |  |  |
|  |  |  | раздел |
|  |  |  | «Объект |
|  |  |  | SocialUser») |
| closed_by_abonent | Integer | Нет | Идентификато |
| _id |  |  | р сотрудника, |
|  |  |  |  |
|  |  |  | закрывшего |
|  |  |  |  |
|  |  |  | сессию |

Возможные значения state: • pending — сессия ожидает распределения; • dialog — сессия в состоянии диалога; • closed — сессия закрыта. Манго Диалоги. Справочник по API | Версия от 10.06.2026
