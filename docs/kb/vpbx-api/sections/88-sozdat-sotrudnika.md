---
id: vpbx-api-88-sozdat-sotrudnika
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.12"
pdf_section: "3.7.12"
title: "Создать сотрудника"
pdf_heading: "3.7.12 Создать сотрудника"
pages: "130-131"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 130-131"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"130-131","global_pages":"130-131"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1621
status: extracted
ai-generated: true
---
# 3.7.12. Создать сотрудника

> Трассировка: PDF §3.7.12 · сквозные стр. 130-131 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.130-131.

POST /vpbx/member/create Метод позволяет добавлять сотрудников в Виртуальную АТС. Обратите внимание, чтобы добавить дополнительных сотрудников, необходимо разрешить работать с услугами для API коннектора. Набор настроек идентичен настрокам в Личном кабинете. Параметры запроса:

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | name |  |  |  | Да | ФИО сотрудника |
| 2 | email |  |  |  |  | Адрес электронной почты |
| 3 | mobile |  |  |  |  | Мобильный телефон |
| 4 | department |  |  |  |  | Отдел |
| 5 | position |  |  |  |  | Должность |
| 6 | login |  |  |  |  | Логин [обязательное, если указан password.<br>Передаются login и password вместе либо ни одно<br>из этих полей]; |
| 7 | password |  |  |  |  | Пароль [обязательное, если указан login .<br>Передаются login и password вместе либо ни одно<br>из этих полей] |
| 8 | use_status |  |  |  |  | Учитывать статус сотрудника в Контакт-центре<br>при распределении вызовов на него |
| 9 | use_cc_numbers |  |  |  |  | Принимать вызовы на номер(а) выбранные в<br>Контакт-центре |
| 10 | access_role_id |  |  |  | Да | id роли сотрудника |
| 11 | extension |  |  |  | Да | Внутренний номер сотрудника |
| 12 | line_id |  |  |  |  | Исходящий номер (значение, id линии, можно<br>использовать все линии, кроме линий с region =<br>"sip") |
| 13 | trunk_number_<br>id |  |  | integer |  | id номера sip-trunk'a исходящего (у номера поле<br>options должно быть 4 или 6) номера SIP-TRUNK |
| 14 | dial_alg |  |  |  |  | Алгоритм дозвона, 0..2 |
| 15 | numbers |  |  |  |  | Настройки средств дозвона, порядок определяет<br>порядок использования |
| 15.1 |  | number |  | string |  | Зависит от protocol: PSTN-номер, sip-номер, FMC-<br>номер |
| 15.2 |  | protocol |  |  |  | Протокол номера телефона, возможные значения:<br>tel – PSTN номер, sip – sip-номер, fmc – FMC номер |
| 15.3 |  | wait_sec |  |  |  | Время ожидания ответа, специальное значение 0 –<br>действуют общие ограничение платформы или<br>оператора связи |
| 15.4 |  | status |  |  |  | Статус номера, возможные значения: on – активен,<br>off – выключен |
| 15.5 |  | schedule |  |  |  | Расписание, опциональное |
|  |  |  | from | string |  | Дата начала, "2019-05-23 12:50:25" (UTC) |
|  |  |  | until | string |  | Дата окончания, "2019-05-23 17:25:45" (UTC) |
|  |  |  | items |  |  | Расписание по критериям |

|  |  |  | type | string |  | Варианты дней ['alldays', 'workingdays', 'Holidays',<br>'specificdate', 'Monday', 'Tuesday', 'Wednesday',<br>'Thursday', 'Friday', 'Saturday', 'Sunday'] |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | from | string |  | Время начала (по московскому времени), формат:<br>"12:25" |
|  |  |  | until | string |  | Время окончания (по московскому времени),<br>формат: "18:25" |
|  |  |  | specific<br>_date | string |  | Дата, "2019-05-23 14:25:45" (UTC), если type =<br>SpecificDate. |

Пример запроса: POST https://app.mango-office.ru/vpbx/member/create vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "name":"Name", "email":"name@mail.ru", "department":"Department", "position":"Position", "access_role_id":"10451", "use_status":"1", "use_cc_numbers":"1", "extension":"30052", "dial_alg":"2", "line_id":"300049196", "login":"Login", "password":"Password" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  | Да | Код результата |
| 2 | user_id |  | Нет | id созданного сотрудника |

Пример ответа: { "result": 1000, "user_id": 1234567 }
