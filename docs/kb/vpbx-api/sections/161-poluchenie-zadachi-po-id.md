---
id: vpbx-api-161-poluchenie-zadachi-po-id
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.3.3"
pdf_section: "4.3.3"
title: "Получение задачи по ID"
pdf_heading: "4.3.3 Получение задачи по ID"
pages: "218-219"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 218-219"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"218-219","global_pages":"218-219"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1150
status: extracted
ai-generated: true
---
# 4.3.3. Получение задачи по ID

> Трассировка: PDF §4.3.3 · сквозные стр. 218-219 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.218-219.

POST /cc/task/get Метод позволяет получить данные определенной задачи по ее id-номеру. В результате обработки запроса, формируется массив текстовых данных, содержащий все поля задачи, даже те, в которых нет данных (null). Параметры запроса:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | task_id | Число | Да | ID задачи |

Пример запроса: POST https://app.mango-office.ru/cc/task/get vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "product_id":300023344, "task_id":45594 } В ответе содержатся следующие данные:

| № | Параметр |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 уровень | 2 уровень |  |  |  |
| 1 | result |  | Число | Да | Код результата |
| 2 | task |  | Массив | Да |  |
| 2.1 |  | task_id | Число | Да | ID задачи |
| 2.2 |  | status | Число | Да | Статус задачи. Доступные значения:<br>0 - Открыта (создана); 1 - Выполнена<br>(завершена); 2 - Отменена; 3 - Подтверждена |
| 2.3 |  | event_type | Число | Да | Тип задачи. Доступные значения: 1 – Позвонить,<br>2 – Написать, 3 – Встретиться, 4 - Сделать |
| 2.4 |  | start_time | timestamp | Да | Дата/время начала события. |
| 2.5 |  | duration | Число | Да | Длительность события. В минутах |
| 2.6 |  | priority | Число | Да | Важность задачи. Доступные значения: null - не<br>важная, 1 - обычная, 2 - важная |
| 2.7 |  | contact_id | Число | Да | ID контакта адресной книги |
| 2.8 |  | source_id | Число | Нет | Источника контакта |
| 2.9 |  | source_type | string | Нет | Тип источника контакта |
| 2.10 |  | from_user_id | Число | Да | ID сотрудника, от чьего имени поставлена задача |
| 2.11 |  | to_user_id | Число | Да | ID сотрудника, которому назначена задача |
| 2.12 |  | description | string | Да | Описание задачи |
| 2.13 |  | is_auto_call | bool | Да | Доступно два состояния: true или false |
| 2.14 |  | phone | string | Да | Номер телефона. Внешняя система<br>контролирует самостоятельно корректность<br>указания номера и контакта |
| 2.15 |  | theme | string | Да | Тема задачи |
| 2.16 |  | deal_id | Число | Да | ID сделки Контакт-центра |

Пример ответа: { "result": 1000, "task": { "task_id": 45594, "status": 1, "event_type": 1, "start_time": "2021-10-01 07:30:00", "duration": 1400, "priority": 1, "contact_id": 19451232, "source_id": 0, "source_type": "vpbx", "from_user_id": 10068242, "to_user_id": 10068242, "deal_id": 233226, "description": "Новое описание миссии на Марс", "phone": "+79219407346", "is_auto_call": true, "theme": "123" } }
