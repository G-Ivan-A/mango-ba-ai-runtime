---
id: vpbx-api-93-poluchit-spisok-individualnyh-pravil-avt
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.15"
pdf_section: "3.7.15"
title: "Получить список индивидуальных правил автосекретаря для сотрудников"
pdf_heading: "3.7.15 Получить список индивидуальных правил автосекретаря для сотрудников"
pages: "135-138"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 135-138"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"135-138","global_pages":"135-138"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1903
status: extracted
ai-generated: true
---
# 3.7.15. Получить список индивидуальных правил автосекретаря для сотрудников

> Трассировка: PDF §3.7.15 · сквозные стр. 135-138 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.135-138.

POST /vpbx/autosecretary/rules Метод позволяет получить список индивидуальных правил автосекретаря сотрудников в ЛК. Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | user_id | integer | Да | ID сотрудника (можно получить при помощи запроса<br>списка групп сотрудников) |
| 2 | rules | array | Нет | Массив идентификаторов индивидуальных правил<br>автосекретаря |

Пример запроса: POST https://app.mango-office.ru/vpbx/autosecretary/rules vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "user_id":"300100588", "rules": [ "1309" ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | rules |  |  |  |  |  |
| 1.1 |  | rule_id |  | integer |  | Идентификатор индивидуального правила<br>автосекретаря |
| 1.2 |  | name |  | string |  | Название правила |
| 1.3 |  | active |  | bool |  | Статус правила (0 - включено, 1 - выключено) |
| 1.4 |  | direction |  | array |  | Направления звонка для правила (incoming -<br>входящие, internal - внутренние) |
| 1.5 |  | schedule |  | array |  | Расписание для правила |
|  |  |  | items | array |  | Массив правил самого расписания |
|  |  |  | type | integer |  | Тип дня, для которого заведено расписание;<br>1 : все дни;<br>2 : рабочие дни;<br>3 : нерабочие дни;<br>4 : воскресенье;<br>5 : понедельник;<br>6 : вторник;<br>7 : среда;<br>8 : четверг;<br>9 : пятница;<br>10 : суббота;<br>11 : конкретная дата |
|  |  |  | date | string |  | Конкретная дата, для которой задается расписание,<br>применяется с type = 11(конкретная дата) |
|  |  |  | from | string |  | Начало временного диапазона, формат: "HH:MM" |
|  |  |  | until | string |  | Конец временного диапазона, формат: "HH:MM" |
|  |  |  | schedule_id | integer |  | Идентификатор расписания |
|  |  |  | from | string |  | Начало периода действия расписания, формат:<br>"YYYY-MM-DD HH:MM" ('Europe/Moscow') |
|  |  |  | until | string |  | Конец периода действия расписания, формат:<br>"YYYY-MM-DD HH:MM" ('Europe/Moscow') |
| 1.6 |  | wait_time |  | integer |  | Длительность ожидания звонка для правила (0-100) |
| 1.7 |  | melody_id |  | integer |  | Идентификатор мелодии для правила |
| 1.8 |  | actions |  | array |  | Набор действий со звонком для правила |
|  |  |  | action | string |  | Тип действия над звонком (end_call - завершить<br>вызов, voice_mail - принять голосовую почту, |

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
|  |  |  |  |  |  | redirect_group - переадресовать на группу,<br>redirect_member - переадресовать на сотрудника,<br>redirect_ext_number - переадресовать на номер<br>телефона) |
|  |  |  | param | string |  | Дополнительный параметр, обязательность<br>значения определяется типом действия над звонком<br>(end_call - оставить пустым, voice_mail - указать<br>адрес электронной почты для принятия голосового<br>сообщения, redirect_group - указать ID группы для<br>переадресации вызова, redirect_member - указать ID<br>сотрудника для переадресации вызова,<br>redirect_ext_number - указать внешний номер<br>телефона для переадресации) |
|  |  |  | wait_time | integer |  | Время ожидания ответа для action =<br>redirect_ext_number |
| 1.9 |  | notifications |  | array |  | Массив настроек для рассылки уведомлений о<br>пропущенном звонке |
|  |  |  | action | string |  | Способ отправки уведомления<br>(send_sms_ext_number - отправить уведомление<br>через SMS, send_email - отправить уведомление на e-<br>mail); |
|  |  |  | param | string |  | Адрес отправки уведомления (send_sms_ext_number<br>- ввести номер телефона, send_email - ввести e-mail). |

Пример ответа: { "result": 1000, "rules": [ { "rule_id": 1309, "name": "das asd a", "active": true, "direction": [ "incoming", "internal" ], "schedule": { "items": [], "schedule_id": 10006617, "from": "2021-05-01 00:00", "until": "2021-05-07 00:00" }, "wait_time": 1, "melody_id" 1000007836, "actions": [ { "action": "redirect_member", "param": 300100588 } ], "notifications: [ { "action": "send_sms_ext_number", "param": "+7972113322235912" }, { "action": "send_email", "param": "99991234567890@123456gmailm12345678.com" } ] } ]}
