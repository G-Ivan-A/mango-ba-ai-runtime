---
id: vpbx-api-135-poluchit-kontakt-po-id
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.9.3.3"
pdf_section: "3.9.3.3"
title: "Получить контакт по id"
pdf_heading: "3.9.3.3 Получить контакт по id"
pages: "182-185"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 182-185"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"182-185","global_pages":"182-185"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 2582
status: extracted
ai-generated: true
---
# 3.9.3.3. Получить контакт по id

> Трассировка: PDF §3.9.3.3 · сквозные стр. 182-185 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.182-185.

POST /vpbx/ab/contact Метод возвращает информацию о контакте. Работа с контактами доступна в Контакт-центре и M.TALKER. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | contact_id |  |  | ID контакта |
| 2 | contact_ext_fields |  |  | Признак необходимости возвращать значения<br>пользовательских полей (custom_values) и поля<br>идентификатор персонального сотрудника (user_id ) |

Пример запроса: POST https://app.mango-office.ru/vpbx/ab/contact vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "contact_id":"12101250", "contact_ext_fields":true } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнем<br>вложенности | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- |

|  | 1 | 2 | 3 |  | ный |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | result |  |  |  | Да | Код результата |
| 2 | contact_id |  |  | string | Нет | id контакта |
| 3 | type |  |  | Число |  | Значение по умолчанию 0, число - тип контакта во<br>внешней CRM. Этот параметр носит<br>информационный характер, и в данный момент не<br>используется |
| 4 | n- ame |  |  | string | Нет | Название |
| 5 | office |  |  | string | Нет | Строка |
| 6 | site |  |  | string | Нет | Строка, сайт |
| 7 | org |  |  | Object | Нет | Организация, к которой относится контакт |
| 7.1 |  | org_id |  | string |  | Идентификатор организации в БД ВАТС |
| 7.2 |  | org_name |  | string |  | Название организации |
| 8 | importance |  |  | Число | Нет | Число [0-9] - флаг «важный контакт» |
| 9 | comment |  |  | string | Нет | Комментарий к контакту |
| 10 | birthday |  |  | string | Нет | Дата рождения в формате yyyy-mm-dd |
| 11 | sex |  |  | Число | Нет | Возможные значения 0, 1. Пол |
| 12 | avatar |  |  | string | Нет | Ссылка |
| 12 | url |  |  | string | Нет | Ссылка на карточку контакта (если источник<br>предоставляет такую возможность) |
| 14 | phones [] |  |  |  |  | Массив объектов «Телефон» |
|  |  | phone_id |  | string | Нет | Идентификатор телефонного номера |
|  |  | type |  | Число | Нет | Тип телефонного номера (0-Городской, 1-<br>Мобильный, 2-SIP, 3-Skype, 4-Другой, 5-Факс) |
|  |  | phone |  | string | Нет | Телефонный номер, в том виде, в котором<br>пользователь их ввел (макс 255 символов) |
|  |  | comment |  | string | Нет | Комментарий к номеру (макс 255 символов) |
|  |  | ext |  | string | Нет | Добавочный номер (макс 32 символ); |
|  |  | is_default |  | Boolean | Нет | Является ли номером по умолчанию, если не<br>указано, интерпретируется как false |
| 15 | emails [] |  |  |  |  | Массив объектов «Электронная почта» |
|  |  | email_id |  | string | Нет | Идентификатор емайла |
|  |  | email |  |  |  | Адрес электронной почты |
|  |  | comment |  | string | Нет | Комментарий к номеру |
|  |  | is_default |  | Boolean | Нет | Является ли адресом по умолчанию, если не<br>указано, интерпретируется как false |
| 16 | groups [] |  |  |  |  | Массив объектов «Группа» |
|  |  | group_id |  | string | Нет | Идентификатор группы в БД |
|  |  | group_nam<br>e |  | string | Нет | Название группы |
| 17 | nets[] |  |  |  |  | Массив объектов «Социальные сети» |
|  |  | net_id |  | string | Нет | Идентификатор записи |
|  |  | net |  |  |  | Идентификатор типа соц сети:<br>■ 0:facebook;<br>■ 1:вконтакте;<br>■ 2:google+;<br>■ 3:одноклассники;<br>■ 4:myspace;<br>■ 5:instagram;<br>■ 6:linkedin;<br>■ 7:twitter; |

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель- | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | ■ 8:vine;<br>■ 9:youtube;<br>■ 10:badoo |
|  |  | uname |  |  |  | Идентификатор в соц сети |
| 18 | messengers<br>[] |  |  |  |  | Массив объектов «Мессенджеры» |
|  |  | mgr_id |  | string | Нет | Идентификатор записи |
|  |  | mgr |  |  |  | Идентификатор типа мессенджера:<br>■ 0:Viber;<br>■ 1:Telegram;<br>■ 2:Skype;<br>■ 3:WhatsApp |
|  |  | uname |  |  |  | Идентификатор в соц мессенджере |
| 19 | in_favorites<br>[] |  |  |  |  | Массив идентификаторов сотрудников ВАТС, у<br>которых данный контакт в избранных (user_id) |
|  | custom_val<br>ues |  |  |  |  | Массив объектов «Значение пользовательского<br>поля» |
|  |  | custom_val<br>ue_id |  | Число |  | Идентификатор поля |
|  |  | custom_fiel<br>d_id |  | Число |  | Идентификатор пользовательского поля |
|  |  | type |  | Число |  | Тип поля:<br>■ 1 – текст;<br>■ 2 – список;<br>■ 3 - мультисписок |
|  |  | text |  |  |  | Значение текстового поля |
|  |  | list_items[] |  |  |  | Объект «Пункт списка», выбранные элементы<br>списка |
|  |  |  | enum_id | Число |  | Идентификатор пункта списка |
|  |  |  | order |  |  | Порядковый номер поля |
|  |  |  | name | string |  | Название пункта |
| 20 | user_id |  |  | Число | Нет | Идентификатор персонального сотрудника |
| 21 | when_created |  |  | Число | Нет | Время UTC. Время создания контакта |
| 22 | last_call |  |  | Число | Нет | Время UTC. Время последнего вызова (начало<br>дозвона) |

Пример ответа: { "result": 1000, "data": { "contact_id": "12761840", "type": 0, "name": "Ekovic", "office": "office!", "site": "site", "importance": 0, "comment": "http://some-url.org", "birthday": "", "sex": null, "avatar": "", "url": "", "org": { "org_id": "10433117", "org_name": "Edem Inc." }, "phones": [ { "phone_id": "13870362", "phone_num": "1111111", "phone": "1111111", "comment": "", "ext": null, "is_default": true, "type": 0 } ], "emails": [], "groups": [], "nets": [], "messengers": [], "in_favorites": [], "when_created": 1544090687, "custom_values": [ { "custom_value_id": 28276, "custom_field_id": 3236, "type": 1, "text": "" }, { "custom_value_id": 28248, "custom_field_id": 5443, "type": 1, "text": "" }, { "custom_value_id": 28263, "custom_field_id": 5452, "type": 1, "text": "фвВФЫ" } ], "user_id": null, "last_call": null } }
