---
id: vpbx-api-62-poluchenie-statistiki-vyzovov
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.4.2.3"
pdf_section: "3.4.2.3"
title: "Получение статистики вызовов"
pdf_heading: "3.4.2.3 Получение статистики вызовов"
pages: "72-86"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 72-86"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"72-86","global_pages":"72-86"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 8589
status: extracted
ai-generated: true
---
# 3.4.2.3. Получение статистики вызовов

> Трассировка: PDF §3.4.2.3 · сквозные стр. 72-86 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.72-86.

Подготовленные данные хранятся до обращения за ними не менее 1 минуты. API предусматривает для получения результата совершать периодический опрос сервиса. API генерирует событие (запрос к внешней системе) о готовности данных вида: POST /vpbx/stats/calls/result/ Параметры события (запроса к внешней системе):

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | key | Да |  | Ключ, созданный при обработке запроса от внешней системы на<br>получение статистики. |

Пример запроса POST https://app.mango-office.ru/vpbx/stats/calls/result/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "key":"fHJ2mmMBZ1Cnu/YvTRJg==" } Результат (расширенная статистика). В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры, см. таблицу ниже. Важно. В отчете на запрос некоторые элементы могут быть служебными и не содержать время ответа, завершения и продолжительность звонка — например, при создании конференции.

| № | Параметры с уровнями вложенности |  |  |  | Тип | Обя<br>а-<br>тель<br>ный | з Описание<br>- |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |  |  |  |
| 1 | result |  |  |  | integer |  | Код результата. |
| 2 | status |  |  |  | string |  | Статус запроса, тип. Может<br>принимать следующие<br>значения:<br>● 'request': выполняется<br>команда на запрос данных;<br>● 'work': запрос в работе;<br>● 'complete': запрос<br>выполнен, данные<br>получены;<br>● 'cancel': получена команда<br>отмены выполнения запроса.<br>Устанавливается только в<br>случае status == 'request';<br>● 'error': ошибка выполнения<br>запроса;<br>● 'not-found': по указанному<br>ключу запрос не найден. |
| 3 | data |  |  |  |  |  |  |
| 3.1 |  | list |  |  | array |  | Массив вызовов, объектов<br>со следующим возможным<br>(некоторые есть не всегда)<br>набором полей, тип array. |
| 3.1.1 |  |  | entry_id |  | string |  | Идентификатор вызова. |
| 3.1.2 |  |  | context_type |  | integer |  | Cтатус звонка: 1 –<br>входящий,<br>2 – исходящий, 3 –<br>внутренний. |
| 3.1.3 |  |  | context_status |  | integer |  | Признак успешности звонка:<br>0 – неуспешный, 1 –<br>успешный. |
| 3.1.4 |  |  | caller_id |  | integer |  | id абонента, который звонил,<br>null, если звонил не сотрудник,<br>значение идентично значению<br>general.user_id, получаемым из |

| № | Параметры с уровнями вложенности |  |  |  | Тип | Обяз | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | запроса Запрос списка<br>сотрудников ВАТС. |
| 3.1.5 |  |  | caller_name |  | string |  | Имя абонента, который<br>звонил. |
| 3.1.6 |  |  | caller_number |  | string |  | Номер, с которого звонят. |
| 3.1.7 |  |  | called_number |  | string |  | Номер, на который звонят. |
| 3.1.8 |  |  | context_start_time |  | integer |  | Дата/время начала звонка,<br>время в формате UTC. |
| 3.1.9 |  |  | duration |  | integer |  | Продолжительность звонка<br>в секундах. |
| 3.1.10 |  |  | talk_duration |  | integer |  | Продолжительность<br>разговора в секундах. |
| 3.1.11 |  |  | operator_call_duratio<br>n |  | integer |  | Время дозвона до оператора<br>в секундах. Заполняется<br>только для звонков в<br>кампаниях исходящего<br>обзвона для типов<br>dial_mode: «Одновременно<br>оператору и абоненту»,<br>«Сначала оператору, потом<br>абоненту», «Сначала<br>абоненту, потом оператору»,<br>«Предиктивный режим<br>обзвона». Если массив<br>context_calls отсутствует,<br>значение возвращается в<br>объекте звонка. Для<br>остальных случаев значение<br>поля равно null. |
| 3.1.12 |  |  | context_cost_full |  | numeri<br>c |  | Стоимость звонка. |
| 3.1.13 |  |  | context_cost_tariff |  | numeri<br>c |  | Стоимость звонка без<br>услуг. |
| 3.1.14 |  |  | context_init_type |  | string |  | Тип инициатора звонка:<br>● 0 - звонок пользователя с<br>любого устройства;<br>● 1 - звонок пользователя с<br>SIP на номер;<br>● 2 - звонок пользователя на<br>SIP; ● 3 - звонок<br>пользователя с КЦ; ● 4 -<br>заказ звонка;<br>● 5 - заказ звонка через<br>виджет; ● 6 - обратный<br>звонок и автоперезвоны на<br>группу. |

| 3.1.15 |  |  | recall_status |  | integer |  | Признак успешности<br>перезвона для входящих: 0 -<br>неуспешный перезвон, 1 -<br>успешный перезвон; 2 - нет<br>перезвона. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1.16 |  |  | cost |  | numeri<br>c |  | Стоимость разговора. |
| 3.1.17 |  |  | conversion |  |  |  |  |
|  |  |  |  | conversio<br>n_id | integer |  | ИД обращения. |
|  |  |  |  | channel_t<br>ype | integer |  | Тип канала:<br>0 – неизвестно;<br>1 – звонок;<br>2 – Site;<br>3 – VK;<br>4 – Facebook;<br>5 – Viber;<br>6 – Telegram;<br>7 – SMS;<br>8 – Email;<br>9 - WhatsApp (wa);<br>10 – dialogs; |
|  |  |  |  | create | timesta<br>mp |  | Время поступления<br>обращения. |
|  |  |  |  | end | timesta<br>mp |  | Время закрытия<br>обращения. |
|  |  |  |  | result | integer |  | ИД результата обращения:<br>1- Обработано;<br>2 - Переведено;<br>3 - Истекло время ожидания<br>ответа;<br>4 - Не отвечено;<br>5 - Спам;<br>6 - Запрещена отправка. |
|  |  |  |  | assign_us<br>er_id | integer |  | Назначенный сотрудник. |
|  |  |  |  | close_use<br>r_id | integer |  | Закрывший сотрудник. |
|  |  |  |  | contact_i<br>d | integer |  | ИД контакта. |
|  |  |  |  | first_ans<br>wer | timesta<br>mp |  | Время первого ответа<br>пользователя в обращении. |
|  |  |  |  | start | timesta<br>mp |  | Время взятия обращения в<br>работу. |
|  |  |  |  | entry_poi<br>nt | string |  | Точка входа, используется<br>для идентификации<br>источника обращения, тип.<br>Для звонка - это номер на<br>который поступил входящий<br>вызов. |
|  |  |  |  | group_id | integer |  | Группа, на которую было<br>распределено обращение. |
|  |  |  |  | deal_id | integer |  | ИД сделки. |

| № | Параметры с уровнями вложенности |  |  |  | Тип | Обяз | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | params | integer |  | Битовая маска параметров<br>обращения<br>● 0 и 1 бит - направление<br>обращения:<br>■ 0 - внутреннее, 1 -<br>входящее, 2 -исходящее;<br>● 2 бит - признак<br>автоматического обращения:<br>■ 1 - автоматическое;<br>● 3 бит - признак триггерной<br>коммуникации:<br>■ 1 - триггерная<br>коммуникация. |
| 3.2 |  | tag_id |  |  | array<br>[intege<br>r, ..] |  | Массив ИД тематик. |
| 3.3 |  | call_com<br>ment |  |  | string |  | Комментарий. |
| 3.4 |  | script_id |  |  | Array<br>[integer,<br>...] |  | Массив ID скрипта КЦ,<br>связанный со звонком. |
| 3.5 |  | mark_clie<br>nt |  |  | integer |  | Постзвонковая оценка<br>клиента<br>● "1".."10": постзвонковая<br>оценка клиента;<br>● "-1": значит, что человека<br>перекинуло на оценку, но он<br>ничего не ответил;<br>● null: то клиента не<br>перекидывало на оценку, он<br>раньше положил трубку. |
| 3.6 |  | mark_cont<br>roller |  |  | json |  | Оценка контролера. |
| 3.6.1 |  |  | question_id |  | integer |  | ИД вопроса из анкеты. |
| 3.6.2 |  |  | mark |  | integer |  | Оценка. |
| 3.6.3 |  |  | comment |  | string |  | Комментарий. |
| 3.7 |  | context_ca<br>lls |  |  | array |  | Данные о звонке с<br>информацией по плечам<br>вызова, массив элементов<br>(тип array) с информацией по<br>плечам вызова. |
| 3.7.1 |  |  | call_type |  | string |  | Тип плеча<br>(number\|user\|group\|conferen<br>ce). |

| № | Параметры с уровнями вложенности |  |  |  | Тип | Обяз | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.7.2 |  |  | call_abonent_id |  | integer |  | Этот параметр:<br>● id группы (если call_type =<br>group) идентичный group_id<br>из POST /vpbx/groups;<br>● user_id (если call_type =<br>user) идентичный<br>general.user_id, получаемым<br>POST /config/users/request;<br>● user_id (если call_type =<br>number) идентичный<br>general.user_id, получаемым<br>POST /config/users/request (ид<br>звонящего или<br>принимающего абонента, в<br>зависимости от направления<br>вызова);<br>● user_id (если call_type =<br>conference) идентичный<br>general.user_id, получаемым<br>POST /config/users/request (ид<br>инициатора конференц-<br>колла) |
| 3.7.3 |  |  | call_abonent_info |  | string |  | Текстовое описание<br>абонента. |
| 3.7.4 |  |  | call_abonent_number |  | string |  | Номер/SIP-учетка, на котором<br>сотрудник принимал звонок. |
| 3.7.5 |  |  | call_start_time |  | integer |  | Дата/время начала звонка,<br>время события в формате<br>UTC. |
| 3.7.6 |  |  | call_answer_time |  | integer |  | Время ответа, время события<br>в формате UTC. |
| 3.7.7 |  |  | call_end_time |  | integer |  | Время завершения, время<br>события в формате UTC. |
| 3.7.8 |  |  | call_duration |  | integer |  | Продолжительность звонка в<br>секундах. |
| 3.7.9 |  |  | talk_duration |  | integer |  | Продолжительность<br>разговора в секундах. |
| 3.7.10 |  |  | dial_duration |  | integer |  | Продолжительность вызова в<br>секундах. |
| 3.7.11 |  |  | operator_call_duratio<br>n |  | integer |  | Время дозвона до оператора в<br>секундах. Заполняется только<br>для звонков в кампаниях<br>исходящего обзвона для типов<br>dial_mode: «Одновременно<br>оператору и абоненту»,<br>«Сначала оператору, потом<br>абоненту», «Сначала<br>абоненту, потом оператору»,<br>«Предиктивный режим<br>обзвона». Для переводов и<br>консультаций значение |

|  |  |  |  |  |  |  | возвращается в первом<br>элементе массива<br>context_calls, у которого<br>продолжительность вызова<br>больше 0. Для остальных<br>случаев значение поля равно<br>null. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.7.12 |  |  | hold_duration |  | integer |  | Продолжительность<br>удержания в секундах. |
| 3.7.13 |  |  | call_end_reason |  | integer |  | Код завершения звонка. |
| 3.7.14 |  |  | recording_id |  | array<br>[string,<br>...] |  | Массив идентификаторов<br>записи разговора (при<br>наличии). |
| 3.7.15 |  |  | external_call_id |  | string |  | Внутренний идентификатор<br>вызова (плеча вызова), строка<br>не более 128 байт. Не имеет<br>отношения к CALL-ID из SIP-<br>протокола. Уникальность<br>идентификатора вызова<br>гарантируется ВАТС на<br>протяжении всего периода<br>оказания услуг по данному<br>API. Внутренний формат<br>идентификатора не должен<br>как-либо использоваться<br>внешней системой.<br>Реализация ВАТС может<br>изменять принцип генерации<br>идентификатора вызова, не<br>нарушая при этом<br>соглашение об уникальности |
| 3.7.16 |  |  | DirectionInbound |  | bool |  | Признак звонка в режиме<br>"входящий". |
| 3.7.17 |  |  | DirectionOutbound |  | bool |  | Признак звонка в режиме<br>"исходящий". |
| 3.7.18 |  |  | ModeConversation |  | bool |  | Признак звонка в режиме<br>"разговор". |
| 3.7.19 |  |  | ModeListen |  | bool |  | Признак звонка в режиме<br>"прослушивание". |
| 3.7.20 |  |  | ModePrompt |  | bool |  | Признак звонка в режиме<br>"суфлирование". |
| 3.7.21 |  |  | ModeConference |  | bool |  | Признак звонка в режиме<br>"конференция". |
| 3.7.22 |  |  | ModeGroup |  | bool |  | Признак звонка в режиме<br>"для группы". |
| 3.7.23 |  |  | RecordInbound |  | bool |  | Признак звонка "запись<br>входящего плеча". |
| 3.7.24 |  |  | RecordOutbound |  | bool |  | Признак звонка "запись<br>исходящего плеча". |
| 3.7.25 |  |  | BlindTransfer |  | bool |  | Признак "слепого" перевода<br>звонка. |

| 3.7.26 |  |  | ConsultTransfer |  | bool |  | Признак "консультативного"<br>перевода звонка. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.7.27 |  |  | OutboundDialing |  | bool |  | Признак звонка в рамках<br>исходящего обзвона. |
| 3.7.28 |  |  | Intercepted |  | bool |  | Признак "перехвата" звонка, у<br>того, кто перехватил – true. |
| 3.7.29 |  |  | IvrNotUsed |  | bool |  | Признак использования<br>голосового меню. |
| 3.8 |  |  | task |  | object |  | Информация о задаче<br>кампании исходящего<br>обзвона. |
| 3.9 |  |  | members |  |  |  | Массив данных (array) по<br>сотрудникам, участвовавшим<br>в звонке (только для call_type<br>- group), структура<br>аналогична context_calls. |
| 3.10 | period |  |  |  | string |  | Дата выборки данных. |
| 3.11 | total_ta<br>l<br>ks_dura<br>t ion |  |  |  | integer |  | Общая продолжительность<br>разговоров за дату выборки, в<br>зависимости от указанных<br>фильтров. |
| 3.12 | total_cal<br>l<br>s_durati<br>o n |  |  |  | integer |  | Общая продолжительность<br>звонков за дату выборки, в<br>зависимости от указанных<br>фильтров. |
| 3.13 | total_cal<br>l<br>s_count |  |  |  | integer |  | Общее количество звонков за<br>дату выборки, в зависимости<br>от указанных фильтров. |

Пример ответа (расширенная статистика): { "result": 1000, "status": "complete", "data": [ { "list": [ { "entry_id":"NTAwODcxNjI1Ng==", "context_type":2, "context_status":1, "caller_id":300043164, "caller_name":"Ctulhu_cov", "caller_number":"sip:ctulhu_cov@tinsk01.mango sip.ru", "called_number":"7007374952233501", "context_start_time":1555601310 , "duration":8, "talk_duration":1, "context_init_type":3, "recall_status":2, "cost":20, "context_calls":[ { "call_type":"number", "call_abonent_id":300043164, "call_abonent_info":"Ctulhu_cov", "call_abonent_number":null, "call_start_time":1555601311, "call_answer_time":1555601317, "call_end_time":1555601318, "call_duration":7, "talk_duration":1, "dial_duration":6, "hold_duration":null, "call_end_reason":1110, "recording_id": [ ], [ "MToxMDAwND1MDA4NzE2MjU2OjA=" ],

| "DirectionInbound":false,<br>"DirectionOutbound":true, |
| --- |
| "ModeConversation":true,<br>"ModeListen":false, |
| "ModePrompt":false,<br>"ModeConference":false, |
| "ModeGroup":false,<br>"RecordInbound":false,<br>"RecordOutbound":false, |
| "BlindTransfer":false,<br>"ConsultTransfer":false,<br>"OutboundDialing":true,<br>"Intercepted":false,<br>"IvrNotUsed":true, |
| "members":[<br>]<br>} |
| ], |
| "task":{<br>"campaign_id":2047594,<br>"name":"Перенос", |
| "task_id":1549362305,<br>"status":5,<br>"status_reason":28, |
| "subtasks":[<br>],<br>"attempts":[<br>{<br>"attempt_id":1947613410,<br>"result":1<br>}<br>],<br>"custom_fields":{<br>}<br>}<br>},<br>{<br>"entry_id":"NTAwODcxNjIyNQ==", |
| "context_type":1,<br>"context_status":1,<br>"caller_id":null, |
| "caller_name":"74956496674",<br>"caller_number":"74956496674",<br>"called_number":"74952233567",<br>"context_start_time":1555660155,<br>"duration":14,<br>"talk_duration":9,<br>"context_init_type":0,<br>"recall_status":2,<br>"cost":155.25,<br>[<br>{<br>"call_type":"group",<br>"call_abonent_id":10051192,<br>"call_abonent_info":"Два сотрудника",<br>"call_abonent_number":null,<br>"call_start_time":1555660155,<br>"call_answer_time":1555660160, |
| "call_end_time":1555660169,<br>"call_duration":14, |
| "talk_duration":9, |

| "dial_duration":5,<br>"hold_duration":null,<br>"call_end_reason":1110, |
| --- |
| recording_id":<br>[ |
| "MToxMDAw1MDA4NzE2MjI1OjA="<br>], |
| "DirectionInbound":true,<br>"DirectionOutbound":false,<br>"ModeConversation":false, |
| "ModeListen":false,<br>"ModePrompt":false,<br>"ModeConference":false,<br>"ModeGroup":true, |
| "RecordInbound":false,<br>"RecordOutbound":true,<br>"BlindTransfer":false, |
| "ConsultTransfer":false, |
| "OutboundDialing":false,<br>"Intercepted":false,<br>"IvrNotUsed":false, |
| "members":<br>[<br>{ |
| "call_type":"user",<br>"call_abonent_id":300043135,<br>"call_abonent_info":"Сергей",<br>"call_abonent_number":<br>"sip:cu@t1.mangosip.ru",<br>"call_start_time":1555660155,<br>"call_answer_time":1555660160,<br>"call_end_time":1555660169,<br>"call_duration":14,<br>"talk_duration":9,<br>"dial_duration":5,<br>"hold_duration":null,<br>"call_end_reason":1110,<br>"recording_id": |
| [<br>"MToxMDAwNDYyOTo1MDA4NzE2MjI1OjA="<br>], |
| "DirectionInbound":true,<br>"DirectionOutbound":false,<br>"ModeConversation":true,<br>"ModeListen":false,<br>"ModePrompt":false,<br>"ModeConference":false,<br>"ModeGroup":false,<br>"RecordInbound":false,<br>"RecordOutbound":true,<br>"BlindTransfer":false,<br>"ConsultTransfer":false,<br>"OutboundDialing":false,<br>"Intercepted":false,<br>"IvrNotUsed":true,<br>"members":null<br>}<br>] |
| }<br>] |
| },<br>{ |

| "entry_id": "NTAwODcxNjIyMw==",<br>"context_type":1,<br>"context_status":0, |
| --- |
| "caller_id": null,<br>"caller_name": "74956496674", |
| "caller_number":"74956496674",<br>"called_number":"74952233567", |
| "context_start_time":1555660068,<br>"duration":7,<br>"talk_duration":0, |
| "context_init_type":0,<br>"recall_status":1,<br>"cost":10.3,<br>"context_calls": |
| [<br>{<br>"call_type":"group", |
| "call_abonent_id":10051192, |
| "call_abonent_info":"Два сотрудника",<br>"call_abonent_number":null, |
| "call_start_time":1555660068,<br>"call_answer_time":null,<br>"call_end_time":1555660075,<br>"call_duration":7, |
| "talk_duration":0,<br>"dial_duration":7,<br>"hold_duration":null,<br>"call_end_reason":110,<br>"recording_id":<br>[<br>],<br>"DirectionInbound":true,<br>"DirectionOutbound":false,<br>"ModeConversation":false,<br>"ModeListen":false,<br>"ModePrompt":false,<br>"ModeConference":false,<br>"ModeGroup":true, |
| "RecordInbound":false,<br>"RecordOutbound":false,<br>"BlindTransfer":false, |
| "ConsultTransfer":false,<br>"OutboundDialing": alse,<br>"Intercepted":false,<br>"IvrNotUsed":false,<br>"members":<br>[<br>{<br>"call_type":"user",<br>"call_abonent_id":300043135,<br>"call_abonent_info":"Сергей",<br>"call_abonent_number:<br>"sip:ctulhu@t1.mangosip.ru",<br>"call_start_time":1555660069,<br>"call_answer_time":null,<br>"call_end_time":1555660075,<br>"call_duration":6,<br>"talk_duration":0, |
| "dial_duration":6,<br>"hold_duration":null, |
| "call_end_reason":1110, |

"recording_id":[], "DirectionInbound":tr ue, "DirectionOutbound":f alse, "ModeConversation":tr ue, "ModeListen":false, "ModePrompt":false, "ModeConference":fals e, "ModeGroup":false, "RecordInbound":false , "RecordOutbound":fals e, "BlindTransfer":false , "ConsultTransfer":fal se, "OutboundDialing":fal se, "Intercepted":false, "IvrNotUsed":true, "members":null } ] } ] } ], "period":"20 19-04-19", "total_talks_dura tion":123, "total_calls_dura tion":141, "total_calls_coun t":5 }, { "list": [ { "entry_id":"NTAwODcxNj AxOQ==", "context_type":2, "context_status":1, "caller_id":300043164, "caller_name":"Ctulhu_ cov", "caller_number":"sip:ctulhu_cov@tinsk01.mangosip. ru", "called_number":"7007374952233501", "context_start_time":1555601310, "duration":8, "talk_duration" :1, "context_init_t ype":3, "recall_status" :2, "cost":20, "context_calls" :

| [<br>:2, "cost":20, |
| --- |
| "context_calls":<br>[ |
| ], |
| "period":"2019-04-19",<br>"total_talks_duration":123,<br>"total_calls_duration":141, |
| "total_calls_count":5<br>},<br>{<br>"list": |
| [<br>{<br>"entry_id":"NTAwODcxNjAxOQ==", |
| "context_type":2,<br>"context_status":1, |
| "caller_id":300043164,<br>"caller_name":"Ctulhu_cov",<br>"caller_number":"sip:ctulhu_cov@tinsk01.mangosip.ru", |
| "called_number":"7007374952233501",<br>"context_start_time":1555601310,<br>"duration":8, |
| "talk_duration":1,<br>"context_init_type":3,<br>"recall_status":2,<br>"cost":20,<br>"context_calls":<br>[<br>{<br>"call_type":"number",<br>"call_abonent_id":300043164,<br>"call_abonent_info":"Ctulhu_cov",<br>"call_abonent_number":null,<br>"call_start_time":1555601311,<br>"call_answer_time":1555601317,<br>"call_end_time":1555601318, |
| "call_duration":7,<br>"talk_duration":1,<br>"dial_duration":6,<br>"hold_duration":null, |
| "call_end_reason":1110,<br>"recording_id":<br>[<br>],<br>"DirectionInbound":false,<br>"DirectionOutbound":true,<br>"ModeConversation":true,<br>"ModeListen":false,<br>"ModePrompt":false,<br>"ModeConference":false,<br>"ModeGroup":false,<br>"RecordInbound":false,<br>"RecordOutbound":false,<br>"BlindTransfer":false,<br>"ConsultTransfer":false,<br>"OutboundDialing":true,<br>"Intercepted":false, |
| "IvrNotUsed":true,<br>"members": |
|  |

| ]<br>} |
| --- |
|  |
| ]<br>},<br>{ |
| "entry_id":"NTAwODcxNjAxNQ==",<br>"context_type":2,<br>"context_status":1, |
| "caller_id":300043164,<br>"caller_name":"Ctulhu_cov",<br>"caller_number":"sip:ctulhu_cov@tst-devpg4-<br>minsk01.mangosip.ru",<br>"called_number":"7007374952233503", |
| "context_start_time":1555601304,<br>"duration":6,<br>"talk_duration":2,<br>"context_init_type":3, |
| "recall_status":2,<br>"cost":12.05,<br>"context_calls": |
| [<br>{<br>"call_type":"number", |
| "call_abonent_id":300043164,<br>"call_abonent_info":"Ctulhu_cov",<br>"call_abonent_number":null,<br>"call_start_time":1555601305, |
| "call_answer_time":1555601308,<br>"call_end_time":1555601310,<br>"call_duration":5,<br>"talk_duration":2,<br>"dial_duration":3,<br>"hold_duration": null,<br>"call_end_reason": 110,<br>""recording_id":<br>[<br>],<br>"DirectionInbound":false,<br>"DirectionOutbound":true,<br>"ModeConversation":true,<br>"ModeListen":false,<br>"ModePrompt":false,<br>"ModeConference":false,<br>"ModeGroup":false,<br>"RecordInbound":false, |
| "RecordOutbound":false,<br>"BlindTransfer":false,<br>"ConsultTransfer":false,<br>"OutboundDialing":true, |
| "Intercepted":false,<br>"IvrNotUsed":true,<br>"members":<br>[<br>]<br>}<br>] }, ...} |
