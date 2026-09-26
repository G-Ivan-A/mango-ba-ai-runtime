---
id: vpbx-api-51-poluchit-spisok-pravil-pereadresacii
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.3.1"
pdf_section: "3.3.1"
title: "Получить список правил переадресации"
pdf_heading: "3.3.1 Получить список правил переадресации"
pages: "59-61"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 59-61"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"59-61","global_pages":"59-61"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1829
status: extracted
ai-generated: true
---
# 3.3.1. Получить список правил переадресации

> Трассировка: PDF §3.3.1 · сквозные стр. 59-61 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.59-61.

POST /vpbx/forwarding/numbers Метод позволяет получить список номеров переадресации с их настройками в ЛК. Содержит информацию о внешнем номере клиента, номере переадресации, типах этих номеров (Телефон или SIP), идентификаторе правила переадресации. При переадресации на внешние номера возвращается значение времени ожидания ответа абонента (в секундах). Опционально также могут быть указаны маски номеров и комментарии. Маски настраиваются внутри ЛК. Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | limit | integer | Нет | Количество переадресаций в ответе (максимальное значение<br>- 1000), значение по умолчанию – 1000. |
| 2 | offset | integer | Нет | Смещение начала выборки, значение по умолчанию – 0. |

Пример запроса: POST https://app.mango-office.ru/vpbx/forwarding/numbers/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = {} В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | numbers |  |  |  | Да | Список правил переадресации, массив. |
| 1.1 |  | forward_id |  | integer |  | ID правила переадресации. |
| 1.2 |  | client_phone_<br>number |  | string |  | Номер, с которого поступает входящий<br>звонок. |
| 1.3 |  | client_phone_<br>type |  | bool |  | Тип номера, с которого поступает входящий<br>звонок (0 - телефон, 1 - SIP-Номер). |
| 1.4 |  | status |  | bool |  | Статус активности правила переадресации (0<br>- правило неактивно, 1 - правило активно). |
| 1.5 |  | comment |  | string |  | Комментарий. |
| 1.6 |  | forward_type |  |  |  | Тип переадресации (group - группа, user -<br>сотрудник, ext_forward - внешний номер). |
| 1.7 |  | forward_to_gr<br>oup |  |  |  | Массив данных при переадресации на группу;<br>возвращается, если у параметра forward_type<br>указано значение group, массив. |
| 1.7.1 |  |  | forward_g<br>roup_id | integer |  | ID сотрудника, на которого осуществляется<br>переадресация. |
| 1.8 |  | forward_to_<br>user |  |  |  | Массив данных при переадресации на<br>сотрудника; возвращается, если у параметра<br>forward_type указано значение user, массив. |
| 1.8.1 |  |  | forward<br>_user_id | integer |  | ID сотрудника, на которого осуществляется<br>переадресация. |
| 1.8.2 |  |  | forward<br>_contact<br>_id | integer |  | ID контакта сотрудника, на который<br>осуществляется переадресация. |
| 1.8.3 |  |  | is_defau<br>lt_conta<br>ct_id | bool |  | Тип номера сотрудника (0 - стандатный<br>номер сотрудника, 1 - номер по-умолчанию). |
| 1.9 |  | forward_to_<br>ext |  |  |  | Массив данных при переадресации на<br>внешний номер; возвращается, если у<br>параметра forward_type указано значение<br>ext_forward, массив. |
| 1.9.1 |  |  | forward<br>_number<br>_type | bool |  | Тип внешнего номера, на который<br>осуществляется переадресация вызова (0 -<br>телефон, 1 - SIP-Номер). |
| 1.9.2 |  |  | forward<br>_number | string |  | Внешний номер, на который осуществляется<br>переадресация вызова. |
| 1.9.3 |  |  | forward_<br>wait_sec | integer |  | Время ожидания ответа абонента (в секундах)<br>при переадресации на внешний номер. |
| 2 | total |  |  | integer |  | Общее количество правил переадресаций. |

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | result |  |  |  |  | Результат выполнения команды завершения<br>вызова от внешней системы.Ниже приведены<br>возможные значения результата (см. "Список<br>кодов результатов"):<br>● 1000 - команда завершения вызова<br>выполнена успешно;<br>● 3300 - объект не существует;<br>● 5XXX – исключение. |

Пример ответа: { "result":1000, "numbers":[ { "forward_id":10160018, "client_phone_number":"121-130", "client_phone_type":0, "status":"1", "comment":"", "forward_type":"group", "forward_to_group":{ "forward_group_id":10322281 } }, { "forward_id":78056, "client_phone_number":"3736354", "client_phone_type":0, "status":"1", "comment":"Jdbdvdv", "forward_type":"group", "forward_to_group":{ "forward_group_id":10322281 } }, { "forward_id":10130880, "client_phone_number":"a@mangosip.ru", "client_phone_type":1, "status":"1", "comment":"", "forward_type":"group", "forward_to_group":{ "forward_group_id":10322281 } } ], "total":28 }
