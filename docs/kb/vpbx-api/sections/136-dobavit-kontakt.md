---
id: vpbx-api-136-dobavit-kontakt
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.3.4"
pdf_section: "3.9.3.4"
title: "Добавить контакт"
pdf_heading: "3.9.3.4 Добавить контакт"
pages: "185-191"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 185-191"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"185-191","global_pages":"185-191"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 3759
status: extracted
ai-generated: true
---
# 3.9.3.4. Добавить контакт

> Трассировка: PDF §3.9.3.4 · сквозные стр. 185-191 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.185-191.

POST /vpbx/ab/contacts/create/ Метод позволяет добавить контакт. Также можно добавить несколько контактов, до 500. Параметры:

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | data |  |  |  |  | Массив добавленных объектов типа Контакт |
| 1.1 |  | name |  | string | Да | Название |
| 1.2 |  | office |  | string | Нет | Должность |
| 1.3 |  | site |  | string | Нет | Сайт компании |

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 |  | org |  | Object | Нет | Объект типа Организация - организация, к которой<br>относится контакт. Включает в себя |
|  |  |  | org_id |  | Нет | ID организации, если уже существует, тогда второе<br>поле "org_name" отправлять не обязательно |
|  |  |  | org_name | string | Нет | Название организации, указывается для<br>существующей или создания новой организации, для<br>существующей поле "org_id" отправлять не<br>обязательно |
| 1.5 |  | importa<br>nce |  | Число | Нет | [0-9] - флаг «важный контакт» |
| 1.6 |  | commen<br>t |  | string | Нет | Комментарий к контакту |
| 1.7 |  | birthday |  | string | Нет | Дата рождения в формате yyyy-mm-dd |
| 1.8 |  | sex |  | Число | Нет | Возможные значения 0, 1. Пол |
| 1.9 |  | phones<br>[] |  |  |  | Массив объектов «Телефон» |
|  |  |  | phone_id | string | Нет | Идентификатор телефонного номера |
|  |  |  | type | Число | Нет | Тип телефонного номера (0-Городской, 1-Мобильный,<br>2-SIP, 3-Skype, 4-Другой, 5-Факс) |
|  |  |  | phone | string | Нет | Телефонный номер, в том виде, в котором<br>пользователь их ввел (макс 255 символов) |
|  |  |  | comment | string | Нет | Комментарий к номеру (255) |
|  |  |  | ext | string | Нет | Добавочный номер (макс 32 символ) |
|  |  |  | is_default | Boolean | Нет | Является ли номером по умолчанию, если не указано,<br>интерпретируется как false |
| 1.10 |  | emails<br>[] |  |  |  | Массив объектов «Электронная почта» |
|  |  |  | email_id | string | Нет | Идентификатор емайла |
|  |  |  | email |  |  | Адрес электронной почты |
|  |  |  | comment | string | Нет | Комментарий к номеру |
|  |  |  | is_default | Boolean | Нет | Является ли адресом по умолчанию, если не указано,<br>интерпретируется как false |
| 1.11 |  | groups<br>[] |  |  |  | Массив объектов «Группа» |
|  |  |  | group_id | string | Нет | Идентификатор группы в БД |
|  |  |  | group_name | string | Нет | Название группы |
| 1.12 |  | nets[] |  |  |  | Массив объектов «Социальные сети» |
|  |  |  | net_id | string | Нет | Идентификатор записи |
|  |  |  | net |  |  | Идентификатор типа соц сети - 0:Facebook,<br>1:Вконтакте, 2:Google+, 3:Одноклассники, 4:myspace,<br>5:Instagram, 6:linkedin, 7:Twitter, 8:Vine, 9:Youtube,<br>10:Badoo; |
|  |  |  | uname |  |  | Идентификатор в соц сети |
| 1.13 |  | messeng<br>ers |  |  |  | Массив объектов «Мессенджеры» |
|  |  |  | mgr_id | string | Нет | Идентификатор записи |
|  |  |  | mgr |  |  | Идентификатор типа мессенджера:<br>□ 0:viber;<br>□ 1:telegram; |

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | □ 2:skype;<br>□ 3:whatsapp |
|  |  |  | uname |  |  | Идентификатор в соц мессенджере |
| 1.14 |  | in_favor<br>es [] |  |  |  | Массив идентификаторов сотрудников ВАТС, у<br>которых данный контакт в избранных (user_id) |
| 1.15 |  | custom_<br>values<br>[] |  |  |  | Массив объектов «Значение пользовательского поля» |
|  |  |  | custom_field_<br>id | Число |  | Идентификатор пользовательского поля |
|  |  |  | text |  |  | Значение текстового поля |
|  |  |  | value |  |  | Значение для типа "Число", "Денежный", "Дата",<br>"Флаг", "Пользователь"; |
|  |  |  | list_items[] |  |  | Объект «Пункт списка», выбранные элементы списка:<br>□ enum_id - число, идентификатор пункта списка |
| 1.16 |  | user_id |  | Число |  | Идентификатор персонального сотрудника |
| 2 | on_error |  |  | string | Нет | Действие по умолчанию для записей, которые не<br>прошли проверку по критериям обеспечения<br>целостности (например, дубликаты существующих<br>записей), возможные значения |
|  |  | duplicate |  |  |  | Создавать дубликаты существующих записей. Если<br>выбран данный вариант разрешения коллизий, те<br>элементы, которые были продублированы,<br>помещаются в ответе в массив успешно обработанных<br>- в массив data |
|  |  | skip |  |  |  | (Значение по умолчанию) ничего не предпринимать,<br>пропускать проблемные записи. В случае, когда<br>выбрана эта опция, порядковые номера (индексы во<br>входном массиве data) не обработанных<br>(пропущенных) элементов попадают в массив skipped,<br>и отражаются в статистике операции |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/contacts/create vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "data":[ { "name":"Новый контакт 16 08 19", "office":"Office", "site":"my.site.test", "importance":"5", "comment":"Test contact create", "birthday":"2019-08-16", "sex":"1", "phones":[ { "type":"4", "phone":"296234567", "comment":"комментарий для телефона 291234567", "ext":"375", "is_default":"true"

| },<br>{<br>"type":"4","phone":"296234568","comment":"комментарий для телефона |
| --- |
| 291234568","ext":"375","is_default":"true"<br>} |
| ],<br>"emails":[ |
| {<br>"email":"new.email6@mail.ru",<br>"comment":"comment for new.email@mail.ru", |
| "is_default":"true"<br>},<br>{<br>"email":"new.emai62l@mail.ru", |
| "comment":"comment for new.email2@mail.ru",<br>"is_default":"true"<br>} |
| ],<br>"groups":[ |
| {<br>"group_name":"New6Group"<br>}, |
| {<br>"group_name":"New6Group Inc"<br>}, |
| {<br>"group_name":"New6Group Corp"<br>}<br>],<br>"nets":[<br>{<br>"net":"2",<br>"uname":"U6ser"<br>},<br>{<br>"net":"3",<br>"uname":"U6ser0"<br>}<br>], |
| "messengers":[<br>{<br>"mgr":"0", |
| "uname":"U6serV"<br>},<br>{<br>"mgr":"1",<br>"uname":"U6serT"<br>}<br>],<br>"in_favorites":"12761893",<br>"custom_values": [<br>{<br>"custom_field_id": 5140,<br>"text": "New Value"<br>},<br>{<br>"custom_field_id": 5444,<br>"text": "ЦОВ" |
| },<br>{ |
| "custom_field_id": 5445,<br>"list_items": [ |

{ "enum_id": 6979, }, { "enum_id": 6981, } ] }, { "custom_field_id": 5446, "list_items": [ { "enum_id": 6983, } ] } ], "on_error":"skip" } ] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  | Да | Код результата |
| 2 | data |  | Нет | Ассоциативный массив объектов успешно обработанных элементов (те,<br>которые были вставлены, и те, которые были перезаписаны или<br>продублированы в случае явного указания пользователем на режим<br>обработки коллизий) вида: { contact_id: contact, ... }. Где contact_id -<br>идентификатор созданного контакта, а contact - стандартный объект<br>контакта |
| 3 | skipped |  | Нет | Массив идентификаторов (начинающихся с 0) не обработанных элементов<br>(те, которые были выявлены, как дубликаты и были пропущены), где в<br>качестве идентификатора используется порядковый номер строки входного<br>массива data, вида [ XXX, YYY, ZZZ, ... ] |

Пример ответа: { "result": [ 1000 ], "data": { "12962817": { "contact_id": "12962817", "type": 0, "name": "Новый контакт 16 08 19", "office": "Office", "site": "my.site.test", "org": null, "importance": 5, "comment": "Test contact create", "birthday": "2019-08-16", "sex": 1,

| "avatar": "",<br>"url": null,<br>"phones": [ |
| --- |
| {<br>"phone_id": "13870398", |
| "type": 4,<br>"phone": "296234567", |
| "comment": "комментарий для телефона 291234567",<br>"ext": "375",<br>"is_default": true |
| },<br>{<br>"phone_id": "13870399",<br>"type": 4, |
| "phone": "296234568",<br>"comment": "комментарий для телефона 291234568",<br>"ext": "375" |
| }<br>], |
| "emails": [<br>{<br>"email_id": "11595948", |
| "email": "new.email6@mail.ru",<br>"comment": "comment for new.email@mail.ru",<br>"is_default": true |
| },<br>{<br>"email_id": "11595949",<br>"email": "new.emai62l@mail.ru",<br>"comment": "comment for new.email2@mail.ru"<br>}<br>],<br>"groups": [<br>{<br>"group_id": "10128775",<br>"group_name": "New6Group"<br>},<br>{<br>"group_id": "10128776", |
| "group_name": "New6Group Inc"<br>},<br>{ |
| "group_id": "10128777",<br>"group_name": "New6Group Corp"<br>}<br>],<br>"nets": [<br>{<br>"net_id": "12278",<br>"net": 2,<br>u"name": "U6ser"<br>},<br>{ "net_id": "12279",<br>"net": 3,<br>"uname": "U6ser0"<br>}<br>],<br>"messengers": [<br>{ mgr_id: "12277", |
| "mgr": 1,<br>"uname": "U6serT" |
| },<br>{ "mgr_id": "12276", |

"mgr": 0, "unamev: "U6serV" } ], "in_favorites": [], "when_created": 1565975061, "last_used": null, "last_call": null } }}
