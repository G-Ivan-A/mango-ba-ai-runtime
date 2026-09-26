---
id: vpbx-api-77-zapros-spiska-sotrudnikov-vats
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.1"
pdf_section: "3.7.1"
title: "Запрос списка сотрудников ВАТС"
pdf_heading: "3.7.1 Запрос списка сотрудников ВАТС"
pages: "105-113"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 105-113"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"105-113","global_pages":"105-113"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 3849
status: extracted
ai-generated: true
---
# 3.7.1. Запрос списка сотрудников ВАТС

> Трассировка: PDF §3.7.1 · сквозные стр. 105-113 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.105-113.

POST /vpbx/config/users/request Параметры запроса:

| № | Параметры с уровнями<br>вложенности |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | extension |  |  | Нет | Идентификатор сотрудника<br>ВАТС, настройки которого<br>запрашиваются. Для<br>получения полного списка<br>сотрудников параметр не<br>передается |
| 2 | ext_fields |  | array<br>[string,string,<br>...] | Нет | Тип данных array [string,string,<br>...], можно указать список<br>дополнительных полей в<br>ответе |
| 2.1 |  | general.user_id |  |  | id сотрудника |
| 2.2 |  | general.sips |  |  | Массив SIP-учеток сотрудника |
| 2.3 |  | groups |  |  | Группы в которых состоит<br>сотрудник (id- номер группы) |
| 2.4 |  | general.access_role_id |  |  | Id-номер роли сотрудника |
| 2.5 |  | telephony.dial_alg |  |  | Алгоритм дозвона |
| 2.6 |  | telephony.numbers.sc<br>hedule |  |  | Расписание в формате<br>аналогичного запроса в общей<br>шине |
| 2.7 |  | telephony.line_id |  |  | Исходящий номер (значение, id<br>линии) |
| 2.8 |  | telephony.trunk_num<br>ber_id |  |  | id номера sip-trunk'a<br>исходящего номера;<br>возвращается<br>trunk_number_id: integer - id<br>номера sip-trunk'a исходящего<br>номера |
| 2.9 |  | general.mobile | string |  | Мобильный телефон |
| 2.10 |  | general.login | string |  | Логин |
| 2.11 |  | general.use_status | string |  | Учитывать статус сотрудника<br>в Контакт- центре при<br>распределении вызовов на него |
| 2.12 |  | general.use_cc_numb<br>ers | string |  | Принимать вызовы на номер(а)<br>выбранные в Контакт-центре |

В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры: - если запрос был передан без указания параметров ext_fields: ● extension – внутренний номер сотрудника; ● name – ФИО сотрудника; ● email – адрес электронной почты; ● department – отдел; ● position – должность; ● number – номер телефона (зависит от protocol); ● protocol – протокол номера телефона, возможные значения: tel – PSTN номер, sip – sip-номер, fmc – FMC номер; ● wait_sec – время ожидания ответа, специальное значение 0 – действуют общие ограничение платформы или оператора связи; ● order – порядок использования номера; ● status – статус номера, возможные значения: on – активен, off – выключен; ● use_status - учитывать статус сотрудника в Контакт-центре при распределении вызовов на него, integer; ● use_cc_numbers - принимать вызовы на номер(а) выбранные в Контакт-центре, integer; ● mobile - мобильный телефон, string; ● login – логин, string; - если в запросе указаны дополнительные поля для ответа (ext_fields), то в ответе также будет: ● telephony.outgoingline - номер исходящей линии сотрудника; ● telephony.line_id – id исходящей линии сотрудника; ● trunk_number_id: - id номера sip-trunk'a исходящего номера; ● telephony.numbers.schedule – расписание; ● telephony.dial_alg - алгоритм дозвона; ● general.user_id - id сотрудника; ● general.access_role_id - id роли сотрудника; ● general.sips - массив SIP-учеток сотрудника; ● groups – группы, в которые добавлен сотрудник. Примеры. Пример 1. Данные по сотруднику с внутренним номером 1234, без запроса дополнительных полей. Запрос: POST https://app.mango-office.ru/vpbx/config/users/request vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "extension": "1234" } Ответ: json = { "users": [ { "general": { "name":"Ivan", "email":"john@mango-office.com", "department":"IT", "position":"lead developer" }, "telephony": { "extension":"1234", "outgoingline": "749512345678", "numbers": [ { "number": "sip:ivan@apidomain.mangosip.ru", "protocol":"sip", "order":"0", "wait_sec": "12", "status":"on" }, { "number": "74952223311", "order":"1", "protocol":"tel", "wait_sec": "5", "status":"on" } ] } }, { "general": { "name":"Pavel", "email":"pavel@mango-office.com", "department":"IT", "position":"developer" }, "telephony": { "extension":"1234", "outgoingline": "749512345678", "numbers": [ { "number": "sip:pavel@aomain.mangosip.ru", "protocol":"sip", "order":"0", "wait_sec": "12", "status":"on" }, { "number": "78121000000", "protocol":"tel", "order":"1", "wait_sec": "12", "status":"off" } ] } } ] } Пример 2. Данные по сотруднику с внутренним номером 13, с запросом дополнительных полей. Запрос: POST https://app.mango-office.ru/vpbx/config/users/request vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "ext_fields": [ "general.user_id", "general.sips", "groups", "general.access_role_id", "telephony.dial_alg", "telephony.numbers.schedule", "telephony.line_id", "telephony.trunk_number_id", "general.mobile", "general.login", "general.use_status", "general.use_cc_numbers" ] } Ответ:

| { |
| --- |
| "users":<br>[<br>{ |
| "general": |
| { |
| "name": "2409Name",<br>"email": "test25a25@mail.ru", |
| "department": "", |
| "position": "",<br>"user_id": 300052407, |
| "access_role_id": 10454,<br>"mobile": "mobile",<br>"login": null, |
| "use_status": 0,<br>"use_cc_numbers": 0,<br>"sips":<br>[<br>{ |
| "number": "AAA25@mangosip.ru"<br>},<br>{ |
| "number": "AAA25AA@mangosip.ru"<br>},<br>{<br>"number": "AAA25B@mangosip.ru"<br>}<br>]<br>},<br>"telephony":<br>{<br>"extension": "23",<br>"outgoingline": "sip:user1@wer.mangosip.ru",<br>"numbers":<br>[<br>{<br>"number": "skype:25A25", |
| "protocol": "skype",<br>"order": 0,<br>"wait_sec": 120, |
| "status": "on",<br>"schedule":<br>[ |
| ]<br>},<br>{ |
| "number: " "123654123",<br>"number_normalized": "123654123",<br>"protocol": "tel",<br>"order": 1,<br>"wait_sec": 120,<br>"status": "on", |

| "schedule":<br>[<br>] |
| --- |
| },<br>{ |
| "number": "78965",<br>"number_normalized": "78965", |
| "protocol": "tel",<br>"order": 2,<br>"wait_sec": 120, |
| "status": "on",<br>"schedule":<br>[<br>] |
| },<br>{<br>"number": "sip:AAA25@mangosip.ru", |
| "protocol": "sip",<br>"order": 3, |
| "wait_sec": 0,<br>"status": "on",<br>"schedule": |
| [<br>]<br>}, |
| {<br>"number": "sip:AAA25AA@mangosip.ru",<br>"protocol": "sip",<br>"order": 4,<br>"wait_sec": 0,<br>"status": "on",<br>"schedule":<br>[<br>]<br>},<br>{<br>"number": "sip:AAA25B@mangosip.ru",<br>"protocol": "sip",<br>"order": 5, |
| "wait_sec": 0,<br>"status": "on",<br>"schedule": |
| [<br>]<br>},<br>{<br>"number": "mobile",<br>"number_normalized": "",<br>"protocol": "tel",<br>"order": 6,<br>"wait_sec": 120,<br>"status": "on",<br>"schedule":<br>[<br>]<br>}<br>],<br>"dial_alg": 1,<br>"line_id": 300049195, |
| "trunk_number_id": null<br>}, |
| "groups":<br>[ |

| ]<br>},<br>{ |
| --- |
| "general": {<br>"name": "Cekovic", |
| "email": "",<br>"department": "", |
| "position": "Добавлено описание",<br>"user_id: 300049012,<br>"access_role_id": 10451, |
| "mobile": null,<br>"login": "300022532/Cekovic",<br>"use_status": 1,<br>"use_cc_numbers": 0, |
| "sips": [<br>{<br>"number": "Agent_1309_2@mangosip.ru" |
| },<br>{ |
| "number": "userc@tst-devpg3-minsk01.mangosip.ru"<br>}<br>] |
| },<br>"telephony": {<br>"extension": "12", |
| "outgoingline": "74994567918",<br>"numbers": [<br>{<br>"number": "sip:userc@tst-devpg3-minsk01.mangosip.ru",<br>"protocol": "sip",<br>"order": 0,<br>"wait_sec": 120,<br>"status": "on",<br>"schedule": []<br>},<br>{<br>"number": "1212121",<br>"number_normalized": "74951212121",<br>"protocol": "tel", |
| "order": 1,<br>"wait_sec": 120,<br>"status": "on", |
| "schedule": []<br>},<br>{<br>"number": "sip:Agent_1309_2@mangosip.ru",<br>"protocol": "sip",<br>"order": 3,<br>"wait_sec": 120,<br>"status": "on",<br>"schedule": []<br>}<br>],<br>"dial_alg": 1,<br>"line_id": 300049196,<br>"trunk_number_id": null<br>},<br>"groups": [<br>10048964 |
| ]<br>}, |
| {<br>"general": { |

| "name": "JulyNineteen",<br>"email": "",<br>"department": "", |
| --- |
| "position": "",<br>"user_id": 300052242, |
| "access_role_id": 10451,<br>"mobile": null, |
| "login": null,<br>"use_status": 0,<br>"use_cc_numbers": 0, |
| "sips": [<br>{<br>"number": "julynineteen@tst-devpg3-minsk01.mangosip.ru"<br>}, |
| {<br>"number": "qwerty123@tst-devpg3-minsk01.mangosip.ru"<br>} |
| ]<br>}, |
| "telephony": {<br>"extension": "1907",<br>"outgoingline": null, |
| "numbers": [<br>{<br>"number": "555", |
| "number_normalized": "555",<br>"protocol": "tel",<br>"order": 1,<br>"wait_sec": 120,<br>"status": "on",<br>"schedule": []<br>},<br>{<br>"number": "sip:qwerty123@tst-devpg3-minsk01.mangosip.ru",<br>"protocol": "sip",<br>"order": 2,<br>"wait_sec": 120,<br>"status": "on",<br>"schedule": [] |
| },<br>{<br>"number": "sip:julynineteen@tst-devpg3-minsk01.mangosip.ru", |
| "protocol": "sip",<br>"order": 3,<br>"wait_sec": 120,<br>"status": "on",<br>"schedule": []<br>}<br>],<br>"dial_alg": 1,<br>"line_id": null,<br>"trunk_number_id": null<br>},<br>"groups": []<br>},<br>{<br>"general": {<br>"name": "Zaqav",<br>"email": "", |
| "department": "",<br>"position": "", |
| "user_id": 300056842,<br>"access_role_id": 10451, |

| "mobile": null,<br>"login": null,<br>"use_status": 0, |
| --- |
| "use_cc_numbers": 0,<br>"sips": [] |
| },<br>"telephony": { |
| "extension": "324",<br>"outgoingline": null,<br>"numbers": [ |
| {<br>"number": "784w487",<br>"number_normalized": "784487",<br>"protocol": "tel", |
| "order": 0,<br>"wait_sec": 120,<br>"status": "on", |
| "schedule": []<br>} |
| ],<br>"dial_alg": 1,<br>"line_id": null, |
| "trunk_number_id": 825<br>},<br>"groups": [] |
| },<br>{<br>"general": {<br>"name": "Фыв",<br>"email": null,<br>"department": null,<br>"position": null,<br>"user_id": 300058832,<br>"access_role_id": 3,<br>"mobile": null,<br>"login": null,<br>"use_status": 0,<br>"use_cc_numbers": 0,<br>"sips": [] |
| },<br>"telephony": {<br>"extension": "0511", |
| "outgoingline": null,<br>"numbers": [],<br>"dial_alg": 1,<br>"line_id": null,<br>"trunk_number_id": 828<br>},<br>"groups": []<br>} ]<br>} |
