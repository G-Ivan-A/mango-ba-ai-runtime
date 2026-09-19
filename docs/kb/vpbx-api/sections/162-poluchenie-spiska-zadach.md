---
id: vpbx-api-162-poluchenie-spiska-zadach
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.3.4"
pdf_section: "4.3.4"
title: "Получение списка задач"
pdf_heading: "4.3.4 Получение списка задач"
pages: "220-222"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 220-222"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"220-222","global_pages":"220-222"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1830
status: extracted
ai-generated: true
---
# 4.3.4. Получение списка задач

> Трассировка: PDF §4.3.4 · сквозные стр. 220-222 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.220-222.

POST /cc/task/list Метод позволяет получить список задач. В результате обработки запроса, формируется массив текстовых данных, содержащий все поля задачи, даже те, в которых нет данных (null). Параметры запроса:

| № | Параметр | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | limit | Число | Нет | Количество возвращаемых сущностей за один запрос<br>Максимум – 500. Если параметр не указан, отправляем<br>максимум |
| 2 | offset | Число | Нет | Смещение от начала выборки |
| 3 | task_id | Массив | Нет | Массив из нескольких ID |
| 4 | start_time | timestamp | Нет | Дата/время начала события |
| 5 | status | Массив | Нет | Статус задачи. Доступные значения: 0 - Открыта (создана); 1 -<br>Выполнена (завершена); 2 - Отменена; 3 - Подтверждена |
| 6 | event_type | Массив | Нет | Тип задачи. Доступные значения: 1 – Позвонить,<br>2 – Написать, 3 – Встретиться, 4 - Сделать |
| 7 | contact_id | Массив | Нет | Массив контактов |
| 8 | priority | Массив | Нет | Важность. Доступные значения: null - не важная,<br>1 - обычная, 2 - важная |
| 9 | from_user_id | Массив | Нет | ID сотрудника, от чьего имени поставлена задача |
| 10 | to_user_id | Массив | Нет | ID сотрудника, которому назначена задача |

Пример запроса: POST https://app.mango-office.ru/cc/task/list vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "product_id":300023344, "task_id":[45594,45584,45374], "contact_id":[19451232] } В ответе содержатся следующие данные:

| № | Параметр |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  | Число | Да | Код результата |
| 2 | tasks [] |  | Объект | Да |  |
| 2.1 |  | task_id | Число | Да | ID задачи |
| 2.2 |  | status | Число | Да | Статус задачи. Доступные значения:<br>0 - Открыта (создана); 1 - Выполнена<br>(завершена); 2 - Отменена; 3 - Подтверждена |
| 2.3 |  | event_type | Число | Да | Тип задачи. Доступные значения: 1 – Позвонить,<br>2 – Написать, 3 – Встретиться, 4 - Сделать |
| 2.4 |  | start_time | timestamp | Да | Дата/время начала события. Формат timestamp<br>как в API ВАТС |
| 2.5 |  | duration | Число | Да | Длительность события. В минутах. |
| 2.6 |  | priority | Число | Да | Важность. Доступные значения:<br>null - не важная, 1 - обычная, 2 - важная |

| № | Параметр |  | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- | --- |
| 2.7 |  | contact_id | Число | Да | ID контакта адресной книги |
| 2.8 |  | source_id | Число | Да | Источника контакта |
| 2.9 |  | source_type | string | Да | Тип источника контакта |
| 2.10 |  | from_user_id | Число | Да | ID сотрудника, от чьего имени поставлена задача |
| 2.11 |  | to_user_id | Число | Да | ID сотрудника, которому назначена задача |
| 2.12 |  | description | string | Да | Описание задачи |
| 2.13 |  | is_auto_call | bool | Да | Доступно два состояния: true или false |
| 2.14 |  | phone | string | Да | Номер телефона. Внешняя система<br>контролирует самостоятельно корректность<br>указания номера и контакта |
| 2.15 |  | theme | string | Да | Тема задачи |
| 2.16 |  | deal_id | Число | Да | ID сделки Контакт-центра |

Пример ответа: { "result": 1000, "tasks": [ { "task_id": 45594, "status": 1, "event_type": 1, "start_time": "2021-10-01 07:30:00+03", "duration": 23, "priority": 1, "contact_id": 19451232, "source_id": 0, "source_type": "vpbx", "from_user_id": 10068242, "to_user_id": 10068242, "deal_id": 233226, "description": "END MISSION", "phone": "+79219407346", "is_auto_call": true, "theme": "321" }, { "task_id": 45584, "status": 1, "event_type": 1, "start_time": "2021-09-17 15:00:00+03", "duration": 30, "priority": 1, "contact_id": 19449103, "source_id": 0, "source_type": "vpbx", "from_user_id": 10143111, "to_user_id": 10143111, "deal_id": 41373, "description": "6", "phone": "12341234", "is_auto_call": false, "theme": null }, { "task_id": 45374, "status": 0, "event_type": 1, "start_time": "2021-09-07 12:46:30+03", "duration": 15, "priority": 1, "contact_id": null, "source_id": null, "source_type": "", "from_user_id": 10081428, "to_user_id": 10081428, "deal_id": 244334, "description": "saasdfadf", "phone": "", "is_auto_call": false, "theme": "Назначенные и возвращенные" } ] }
