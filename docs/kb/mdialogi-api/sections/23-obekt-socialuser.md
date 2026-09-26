---
id: mdialogi-api-23-obekt-socialuser
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "2.4.3"
pdf_section: "2.4.3"
title: "Объект SocialUser"
pdf_heading: "2.4.3  Объект SocialUser"
pages: "21-23"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 21-23"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"21-23","global_pages":"21-23"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 912
status: extracted
ai-generated: true
---
# 2.4.3. Объект SocialUser

> Трассировка: PDF §2.4.3 · сквозные стр. 21-23 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.21-23.

Объект SocialUser содержит информацию о пользователе социальной сети или мессенджера.

| Параметр | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
|  |  |  |  |
| social_user_id | String | Да | Уникальный |
|  |  |  | идентификатор |
|  |  |  |  |
|  |  |  | пользователя в |
|  |  |  | социальной сети |
|  |  |  | или мессенджере |
| referer | String | Да | Источник |
|  |  |  | перехода |
|  |  |  |  |
|  |  |  |  |
| nickname | String | Нет | Никнейм |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| first_name | String | Нет | Имя пользователя |
| --- | --- | --- | --- |
|  |  |  |  |
| last_name | String | Нет | Фамилия |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| gender | String | Нет | Пол пользователя |
|  |  |  |  |
| ip | String | Нет | IP-адрес |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| user_agent | String | Нет | User-Agent |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| phone | String | Нет | Телефон |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| email | String | Нет | Email |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| photo | String | Нет | Ссылка на фото |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| custom_fields | Object | Нет | Пользовательские |
|  |  |  | поля из анкеты |
|  |  |  |  |
|  |  |  |  |
| additional_fields | Object | Нет | Дополнительные |
|  |  |  | поля, переданные |
|  |  |  |  |
|  |  |  | API виджета |
| city | String | Нет | Город |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| country | String | Нет | Страна |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| timezone | String | Нет | Часовой пояс |
|  |  |  | пользователя |
|  |  |  |  |
|  |  |  |  |
| profile_url | String | Нет | Ссылка на |
|  |  |  | профиль |
|  |  |  |  |
|  |  |  | пользователя |

Манго Диалоги. Справочник по API | Версия от 10.06.2026
