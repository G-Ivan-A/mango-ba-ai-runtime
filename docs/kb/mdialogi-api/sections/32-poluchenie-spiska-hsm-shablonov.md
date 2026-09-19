---
id: mdialogi-api-32-poluchenie-spiska-hsm-shablonov
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.1.3"
pdf_section: "3.1.3"
title: "Получение списка HSM-шаблонов"
pdf_heading: "3.1.3 Получение списка HSM-шаблонов"
pages: "28-31"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 28-31"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"28-31","global_pages":"28-31"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1849
status: extracted
ai-generated: true
---
# 3.1.3. Получение списка HSM-шаблонов

> Трассировка: PDF §3.1.3 · сквозные стр. 28-31 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.28-31.

Метод позволяет получить список HSM-шаблонов, имеющих статус "APPROVED" и не отправленных в архив. HTTP-запрос: POST /cc/md/hsm/templates Параметры метода:

| № | Параметры | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | id | Строка | Да | Уникальный идентификатор вызова,<br>например UUID, используется для<br>логирования и отладки |
| 2 | channel_id | Целое | Да | Идентификатор канала |

Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Подробнее о формировании электронной подписи см. раздел Подробнее об этих обязательных полях… Пример запроса:

| POST https://app.mango-office.ru/cc/md/hsm/templates |
| --- |
|  |
| vpbx_api_key=1234567890qwerty |
| sign=1234567890qwerty |
|  |
| json= |
| { |
| "id": "qwerty123", |
| "channel_id": 32680 |
| } |

Параметры ответа:

| № | Параметры |  |  |  | Тип | Обязат<br>ельный | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |  |  |  |
| 1 | name |  |  |  | Строка | Да | ID HSM-шаблона |
| 2 | status |  |  |  | Число | Да | id канала с<br>подключенным WA |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

| 3 | code |  |  |  | Число | Да | Текст шаблона |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | error |  |  |  | Строка | Нет | Текст ошибки, если<br>она произошла |
| 5 | templates |  |  |  | Массив<br>объектов | Да |  |
| 5.1 |  | id |  |  | Целое | Да | Идентификатор<br>шаблона |
| 5.2 |  | name |  |  | Строка | Да | Название шаблона |
| 5.3 |  | content |  |  | Объект | Да |  |
|  |  |  | text |  | Строка | Да | Основной текст<br>шаблона |
|  |  |  | buttons |  | Массив<br>объектов | Нет |  |
|  |  |  |  | buttonType | Строка | Нет | Тип кнопки.<br>Возможные значения:<br>- URL: открывает<br>указанную ссылку<br>- PHONE:<br>набирает указанный<br>номер<br>телефона -<br>QUICK_REPL<br>Y:<br>отправляет готовый<br>ответ |
|  |  |  |  | text | Строка | Нет | Текст кнопки (для всех<br>типов) |
|  |  |  |  | url | Строка | Нет | Ссылка (для кнопки<br>типа URL) |
|  |  |  |  | phone | Строка | Нет | Номер телефона (для<br>кнопки типа PHONE) |
|  |  |  |  | payload | Строка | Нет | Код кнопки (для<br>кнопки типа<br>QUICK_REPLY) |
|  |  |  | header |  | Объект | Нет |  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  |  |  |  | headerType | Строка | Нет | Тип заголовка<br>шаблона. Возможные<br>значения:<br>- TEXT: заголовок-<br>текст<br>- IMAGE:<br>заголовок<br>изображение<br>- VIDEO:<br>заголовок-видео<br>- DOCUMENT:<br>заголовок файл |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | text | Строка | Да | Обязательное, если<br>headerType == TEXT |
|  |  |  | footer |  | Объект | Нет |  |
|  |  |  |  | text | Строка | Да | Текст подписи<br>шаблона |
| 5.<br>4 |  | categor<br>y |  |  | Строка | Да | Категория шаблона |

Пример ответа:

|  | { |  |
| --- | --- | --- |
|  | "name": "OK", |  |
|  | "status": 200, |  |
|  | "code": 1000, |  |
|  | "templates": [ |  |
|  | { |  |
|  | "id": "qwerty123", |  |
|  | "name": "example_template", |  |
|  | "content": { |  |
|  | "text": "Добрый день, {{1}}! Переходи по ссылке для просмотра всех позиций.", |  |
|  | "buttons": [ |  |
|  | { |  |
|  | "text": "Чудо-ссылка", |  |
|  | "buttonType": "URL", |  |
|  | "url": "https://www.mango-office.ru" |  |
|  | } |  |
|  | ], |  |
|  | "header": null, |  |
|  | "footer": null |  |
|  | }, |  |
|  | "category": "MARKETING" |  |
|  | }, |  |
|  | { |  |
|  | "id": "qwerty456", |  |
|  | "name": "yet_another_template", |  |
|  | "content": { |  |
|  | "text": "{{1}}, for more information, please call the phone 108.", |  |
|  | "buttons": [], |  |

Манго Диалоги. Справочник по API | Версия от 10.06.2026

|  | "header": { |  |
| --- | --- | --- |
|  | "headerType": "TEXT", |  |
|  | "text": "Very Important Title" |  |
|  | }, |  |
|  | "footer": "Best regards, A5" |  |
|  | }, |  |
|  | "category": "UTILITY" |  |
|  | } |  |
|  | ] |  |
|  | } |  |
