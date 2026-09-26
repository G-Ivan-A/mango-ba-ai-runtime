---
id: vpbx-api-188-poluchenie-spiska-kampaniy-io
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.3"
pdf_section: "4.6.3"
title: "Получение списка кампаний ИО"
pdf_heading: "4.6.3 Получение списка кампаний ИО"
pages: "250-259"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 250-259"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"250-259","global_pages":"250-259"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 6323
status: extracted
ai-generated: true
---
# 4.6.3. Получение списка кампаний ИО

> Трассировка: PDF §4.6.3 · сквозные стр. 250-259 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.250-259.

POST /vpbx/campaign/list Метод позволяет получить список кампаний ИО, созданных вручную оператором КЦ или при помощи соответствующего запроса к API. В ответе отправляются все поля, включая поля в которых нет данных (null). Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/campaign/list vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируется и передается массив данных в формате JSON, содержащий список кампаний ИО и код результата:

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | result |  |  | Число | Да | Код результата |

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | campaigns [] |  |  | Массив<br>объектов | Да | Список кампаний |
| 2.1 |  | campaign_id |  | Число | Да | ID кампании |
| 2.2 |  | line_id |  | Число | Да | ID исходящей линии |
| 2.3 |  | name |  | string | Да | Название кампании, максимум 70<br>символов |
| 2.4 |  | created_by |  | Объект | Да | Кем добавлена кампания |
| 2.4.1 |  |  | user_id | Число | Да | Значение user_id для сотрудника |
| 2.4.2 |  |  | name | Строка | Да | ФИО сотрудника |
| 2.4.3 |  |  | extension | Строка | Да | Внутренний номер сотрудника |
| 2.5 |  | priority |  | Число | Да | Приоритет кампании: 1 - важный,<br>2 - нормальный, 3 - низкий (по<br>умолчанию: 2 - нормальный) |
| 2.6 |  | order |  | Число | Нет | Порядок выполнения кампании.<br>Допустимые значения: от 1 до 999. |
| 2.7 |  | start |  | Число | Да | Дата начала кампании в формате unix<br>timestamp (UTC) |
| 2.8 |  | end |  | Число | Да | Дата окончания кампании в формате<br>unix timestamp (UTC) |
| 2.9 |  | status |  | Число | Да | Статус кампании: 0 - остановлена, 1 -<br>запланирована, 2 - в работе, 3 -<br>останавливается, 4 - завершена,<br>5 - обрабатывается, 6 – удаляется |
| 2.10 |  | members [] |  | Массив<br>строк из<br>чисел | Да | Список внутренних номеров<br>(extension) сотрудников, добавленных<br>в кампанию, без учета статусов в КЦ<br>и настроек в ЛК |
| 2.11 |  | operators [] |  | Массив<br>чисел \| [] | Да | Список abonent_id сотрудников, а также<br>сотрудников-роботов, участвующих в<br>обработке кампании, без учета статусов в<br>КЦ и настроек в ЛК. |
| 2.12 |  | dial_mode |  | Число | Да | Режим обзвона:<br>2 (по умолчанию) - одновременно<br>оператору и абоненту; 3 - сначала<br>оператору, потом абоненту; 4 - сначала<br>абоненту, потом оператору; 7 -<br>предиктивный режим обзвона: система<br>на основе данных о ходе кампании<br>определяет возможность дозвона до<br>следующего клиента до того момента,<br>как оператор освободится. |
| 2.13 |  | redial_busy |  | Число | Да | Максимальное количество попыток<br>дозвона, если номер занят.<br>Допустимые значения: 1,3,5,10 |
| 2.14 |  | redial_no_answer |  | Число | Да | Максимальное количество попыток<br>дозвона, если не берёт трубку.<br>Допустимые значения: 1,3,5,10 |
| 2.15 |  | redial_not_avail |  | Число | Да | Максимальное количество попыток<br>дозвона, если номер недоступен. |

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Допустимые значения: 1,3,5,10 |
| 2.16 |  | redial_antirobot<br>_voice_mail |  | Число | Да | Максимальное количество попыток<br>дозвона в случае, если антиробот<br>распознал голосовую почту, 3 по<br>умолчанию. Допустимые значения:<br>1,3,5,10 |
| 2.17 |  | redial_antirobot<br>_busy |  | Число | Да | Максимальное количество попыток<br>дозвона в случае, если антиробот<br>распознал, что клиент разговаривает<br>или занят, 3 по умолчанию.<br>Допустимые значения: 1,3,5,10 |
| 2.18 |  | redial_antirobot<br>_client_hungup |  | Число | Да | Максимальное количество попыток,<br>если клиент повесил трубку во время<br>анализа антироботом. По умолчанию 1.<br>Допустимые значения: 1,3,5,10 |
| 2.19 |  | redial_antirobot<br>_not_avail |  | Число | Да | Максимальное количество попыток<br>дозвона [1-10] - если антиробот вернул:<br>номер недоступен. По умолчанию 3. |
| 2.20 |  | answer_wait |  | Число | Да | Ожидание ответа клиента (в<br>секундах). Допустимые значения: 10,<br>20, 30, 60 |
| 2.21 |  | add_calls_coef |  | Число | Да | Коэффициент дополнительных<br>вызовов - отношение количества<br>одновременно генерируемых<br>системой попыток дозвона до<br>клиентов к количеству свободных<br>операторов. Допустимые значения:<br>0.1, 0.5, 0.7, 1, 1.5, 2, 3, 5 |
| 2.22 |  | timer_busy |  | Число | Да | Ожидание перед повторной<br>попыткой, если номер занят (в<br>секундах). Допустимые значения: 60,<br>300, 900, 3600 |
| 2.23 |  | timer_no_answer |  | Число | Да | Ожидание перед повторной<br>попыткой, если не берёт трубку (в<br>секундах). Допустимые значения:<br>3600, 10800, 43200, 86400 |
| 2.24 |  | timer_not_avail |  | Число | Да | Ожидание перед повторной<br>попыткой, если номер недоступен (в<br>секундах). Допустимые значения:<br>3600, 10800, 43200, 86400, null/0 - (не<br>перезванивать) |
| 2.25 |  | timer_antirobot_<br>voice_mail |  | Число | Нет | Ожидание перед повторной попыткой<br>в случае, если антиробот распознал<br>голосовую почту (в секундах) |
| 2.26 |  | timer_antirobot_<br>busy |  | Число | Нет | Ожидание перед повторной<br>попыткой в случае, если антиробот<br>распознал, что клиент разговаривает<br>или занят (в секундах) |
| 2.27 |  | timer_antirobot_ |  | Число | Нет | Ожидание перед повторной |

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | client_hungup |  |  |  | попыткой, если Клиент повесил<br>трубку во время анализа антироботом<br>(в секундах). По умолчанию 0. |
| 2.28 |  | timer_antirobot_<br>not_avail |  | Число | Нет | Ожидание перед повторной<br>попыткой, если антиробот вернул:<br>номер недоступен (в секундах). [900,<br>1800, 3600, 7200, 10800, 43200,<br>86400]. По умолчанию 3600. |
| 2.29 |  | sip_trunk_id_op<br>erator |  | Число | Да | ID транка, через который<br>выполняется соединение с<br>оператором |
| 2.30 |  | sip_trunk_id_cli<br>ent |  | Число | Да | ID транка, через который<br>выполняется соединение с клиентом |
| 2.31 |  | use_auto_substit<br>ution_num |  | Булево | Нет | Признак использования услуги<br>"Автоподстановка номеров".<br>Значение по умолчанию – false |
| 2.32 |  | timezone_mode |  | Число | Нет | Режим учета часового пояса и<br>расписания: 0 - не учитываются часовая<br>зона и расписание; 1 - учитываются<br>часовая зона оператора и клиента, и<br>расписание; 2 - учитываются часовая<br>зона клиента и расписание. По<br>умолчанию 0. |
| 2.33 |  | antirobot |  | Булево | Нет | Признак использования услуги<br>"АнтиРобот". Значение по<br>умолчанию – false |
| 2.34 |  | call_processing |  | Число | Да | Поствызовная обработка, сек. |
| 2.35 |  | status_reason |  | Число | Да | Причина перехода в статус (поле<br>status): 1 - команда из вне, 2 -<br>выполнена, 3 - expired (faend <=<br>now()), 4 - не попадает в расписание, 5<br>- пропал "Пинг", 6 - no service, 7 - no<br>balance, 8 - maintanance, 9 - остановлен<br>администратором. |
| 2.36 |  | schema_id |  | Число | Да | ID схемы распределения |
| 2.37 |  | created |  | Число | Да | Дата создания кампании в формате<br>unix timestamp (UTC) |
| 2.38 |  | service_type |  | Число | Да | Тип кампаний. Список чисел от 0 до<br>2147483647 |
| 2.39 |  | tasks_count |  | Число | Да | Общее количество заданий<br>(контактов) |
| 2.40 |  | finished_tasks_c<br>ount |  | Число | Да | Количество выполненных заданий<br>(контактов) обзвона |
| 2.41 |  | completed |  | Число | Да | Время завершения кампании в<br>формате unix timestamp (UTC) |

Пример ответа: { "result": 1000, "campaigns": [ {

| "campaign_id": 1254253,<br>"line_id": 403429597,<br>"created_by": { |
| --- |
| "user_id": 403425571,<br>"name": "Евгеньев Евгений", |
| "extension": "10004"<br>}, |
| "name": "Рога и Копыта Обзвон",<br>"start": 1666814400,<br>"end": 1672516799, |
| "status": 0,<br>"priority": 2,<br>"members": [<br>"10004", |
| "10200",<br>"10201",<br>"10202", |
| "10203",<br>"10204", |
| "10205",<br>"10206",<br>"10207", |
| "10208",<br>"10209",<br>"10210", |
| "10211"<br>],<br>"operators": [],<br>"redial_busy": 3,<br>"redial_no_answer": 3,<br>"redial_not_avail": 3,<br>"timer_busy": 900,<br>"timer_no_answer": 1800,<br>"timer_not_avail": 1800,<br>"answer_wait": 60,<br>"add_calls_coef": 1,<br>"dial_mode": 3,<br>"call_processing": 30,<br>"status_reason": 1, |
| "schema_id": null,<br>"created": 1666870142,<br>"sip_trunk_id_operator": null, |
| "sip_trunk_id_client": null,<br>"service_type": 8,<br>"tasks_count": 265,<br>"finished_tasks_count": 265,<br>"completed": null<br>},<br>{<br>"campaign_id": 1264308,<br>"line_id": 403427465,<br>"created_by": {<br>"user_id": 403425571,<br>"name": "Евгеньев Евгений",<br>"extension": "10004"<br>},<br>"name": "ММ Обзвон(ноябрь) ",<br>"start": 1668369600,<br>"end": 1672516799, |
| "status": 0,<br>"priority": 2, |
| "members": [<br>"10200", |

| "10201",<br>"10202",<br>"10203", |
| --- |
| "10204",<br>"10205", |
| "10206",<br>"10207", |
| "10208",<br>"10209",<br>"10210", |
| "10211"<br>],<br>"redial_busy": 3,<br>"redial_no_answer": 3, |
| "redial_not_avail": 3,<br>"timer_busy": 3600,<br>"timer_no_answer": 1800, |
| "timer_not_avail": 1800,<br>"answer_wait": 30, |
| "add_calls_coef": 1,<br>"dial_mode": 3,<br>"call_processing": 0, |
| "status_reason": 5,<br>"schema_id": null,<br>"created": 1668402895, |
| "sip_trunk_id_operator": null,<br>"sip_trunk_id_client": null,<br>"service_type": 8,<br>"tasks_count": 406,<br>"finished_tasks_count": 406,<br>"completed": null<br>},<br>{<br>"campaign_id": 1264327,<br>"line_id": 403429597,<br>"created_by": {<br>"user_id": 403425571,<br>"name": "Евгеньев Евгений",<br>"extension": "10004" |
| },<br>"name": "Рога и Копыта Обзвон(ноябрь) ",<br>"start": 1668369600, |
| "end": 1672516799,<br>"status": 0,<br>"priority": 2,<br>"members": [<br>"10200",<br>"10201",<br>"10202",<br>"10203",<br>"10204",<br>"10205",<br>"10206",<br>"10207",<br>"10208",<br>"10209",<br>"10210",<br>"10211"<br>], |
| "redial_busy": 3,<br>"redial_no_answer": 3, |
| "redial_not_avail": 3,<br>"timer_busy": 3600, |

| "timer_no_answer": 1800,<br>"timer_not_avail": 1800,<br>"answer_wait": 30, |
| --- |
| "add_calls_coef": 1,<br>"dial_mode": 3, |
| "call_processing": 0,<br>"status_reason": 1, |
| "schema_id": null,<br>"created": 1668404890,<br>"sip_trunk_id_operator": null, |
| "sip_trunk_id_client": null,<br>"service_type": 8,<br>"tasks_count": 47,<br>"finished_tasks_count": 47, |
| "completed": null<br>},<br>{ |
| "campaign_id": 1266248,<br>"line_id": 403427465, |
| "created_by": {<br>"user_id": 403425571,<br>"name": "Евгеньев Евгений", |
| "extension": "10004"<br>},<br>"name": "Рога и Копыта Обзвон(Ноябрь новый)", |
| "start": 1668542400,<br>"end": 1672516799,<br>"status": 0,<br>"priority": 2,<br>"members": [<br>"10200",<br>"10201",<br>"10202",<br>"10203",<br>"10204",<br>"10205",<br>"10206",<br>"10207",<br>"10208", |
| "10209",<br>"10210",<br>"10211" |
| ],<br>"redial_busy": 3,<br>"redial_no_answer": 3,<br>"redial_not_avail": 3,<br>"timer_busy": 3600,<br>"timer_no_answer": 1800,<br>"timer_not_avail": 1800,<br>"answer_wait": 30,<br>"add_calls_coef": 1,<br>"dial_mode": 3,<br>"call_processing": 30,<br>"status_reason": 1,<br>"schema_id": null,<br>"created": 1668628350,<br>"sip_trunk_id_operator": null,<br>"sip_trunk_id_client": null,<br>"service_type": 8, |
| "tasks_count": 211,<br>"finished_tasks_count": 206, |
| "completed": null<br>}, |

| {<br>"campaign_id": 1266247,<br>"line_id": 403427465, |
| --- |
| "created_by": {<br>"user_id": 403425571, |
| "name": "Евгеньев Евгений",<br>"extension": "10004" |
| },<br>"name": "ММ Обзвон(Ноябрь новый)",<br>"start": 1668542400, |
| "end": 1672516799,<br>"status": 0,<br>"priority": 2,<br>"members": [ |
| "10200",<br>"10201",<br>"10202", |
| "10203",<br>"10204", |
| "10205",<br>"10206",<br>"10207", |
| "10208",<br>"10209",<br>"10210", |
| "10211"<br>],<br>"redial_busy": 3,<br>"redial_no_answer": 3,<br>"redial_not_avail": 3,<br>"timer_busy": 3600,<br>"timer_no_answer": 1800,<br>"timer_not_avail": 1800,<br>"answer_wait": 30,<br>"add_calls_coef": 1,<br>"dial_mode": 3,<br>"call_processing": 30,<br>"status_reason": 1,<br>"schema_id": null, |
| "created": 1668628267,<br>"sip_trunk_id_operator": null,<br>"sip_trunk_id_client": null, |
| "service_type": 8,<br>"tasks_count": 2031,<br>"finished_tasks_count": 2005,<br>"completed": null<br>},<br>{<br>"campaign_id": 1254251,<br>"line_id": 403427465,<br>"created_by": {<br>"user_id": 403425571,<br>"name": "Евгеньев Евгений",<br>"extension": "10004"<br>},<br>"name": "ММ Обзвон",<br>"start": 1667246400,<br>"end": 1670702399,<br>"status": 4, |
| "priority": 2,<br>"members": [ |
| "10200",<br>"10201", |

| "10202",<br>"10203",<br>"10204", |
| --- |
| "10205",<br>"10206", |
| "10207",<br>"10208", |
| "10209",<br>"10210",<br>"10211" |
| ],<br>"redial_busy": 3,<br>"redial_no_answer": 3,<br>"redial_not_avail": 3, |
| "timer_busy": 900,<br>"timer_no_answer": 1800,<br>"timer_not_avail": 1800, |
| "answer_wait": 60,<br>"add_calls_coef": 1, |
| "dial_mode": 3,<br>"call_processing": 30,<br>"status_reason": 3, |
| "schema_id": null,<br>"created": 1666870097,<br>"sip_trunk_id_operator": null, |
| "sip_trunk_id_client": null,<br>"service_type": 8,<br>"tasks_count": 2504,<br>"finished_tasks_count": 2504,<br>"completed": 1670702406<br>},<br>{<br>"campaign_id": 1264947,<br>"line_id": 403429597,<br>"created_by": {<br>"user_id": 403425571,<br>"name": "Евгеньев Евгений",<br>"extension": "10004"<br>}, |
| "name": "тест",<br>"start": 1668456000,<br>"end": 1668628799, |
| "status": 4,<br>"priority": 2,<br>"members": [<br>"10004"<br>],<br>"redial_busy": 3,<br>"redial_no_answer": 3,<br>"redial_not_avail": 3,<br>"timer_busy": 3600,<br>"timer_no_answer": 1800,<br>"timer_not_avail": 1800,<br>"answer_wait": 30,<br>"add_calls_coef": 1,<br>"dial_mode": 3,<br>"call_processing": 0,<br>"status_reason": 3,<br>"schema_id": null, |
| "created": 1668485990,<br>"sip_trunk_id_operator": null, |
| "sip_trunk_id_client": null,<br>"service_type": 8, |

"tasks_count": 7, "finished_tasks_count": 0, "completed": 1668628799 } ]}
