---
id: vpbx-api-216-sozdanie-zakrytogo-obrascheniya
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.8.2"
pdf_section: "4.8.2"
title: "Создание закрытого обращения"
pdf_heading: "4.8.2 Создание закрытого обращения"
pages: "301-303"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 301-303"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"301-303","global_pages":"301-303"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1670
status: extracted
ai-generated: true
---
# 4.8.2. Создание закрытого обращения

> Трассировка: PDF §4.8.2 · сквозные стр. 301-303 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.301-303.

/cc/appeals/create-closed-appeals Этот обновленный метод позволяет создавать обращение в КЦ сразу в статусе "Закрыто". При этом, в поле "Ответственный" данного обращения будет указан системный пользователь, от имени которого отправляются запросы. Данный метод вы можете применять, к примеру, чтобы добавить в КЦ информацию о ранее состоявшейся коммуникации с Клиентом через Telegram. Параметры метода:

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ное | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | product_id |  |  | integer | Да | ID продукта, обязательное(для событий на<br>шине), числовое |
| 2 | channel_type |  |  | integer | Да | Канал обращения. Значения 0-10:<br>0 – неизвестно, 1 – звонок, 2 – Site,<br>3 – VK, 4 – Facebook, 5 – Viber,<br>6 – Telegram, 7 – SMS, 8 – Email,<br>9 – WhatsApp, 10 - yandex dialogs |
| 3 | direction |  |  | integer | Да | Направление обращения:<br>0 – входящее, 1 - исходящее |
| 4 | entry_point |  |  | String | Да | Точка входа обращения |
| 5 | create |  |  | String | Да | Дата/время создания обращения |
| 6 | end |  |  | String | Нет | Дата\время завершения обращения |
| 7 | tag_id |  |  | String | Нет | Тематики обращения |
| 8 | comment |  |  | String | Нет | Комментарий к обращению |
| 9 | rate |  |  | integer | Нет | Оценка обращений по шкале от 1 до 5.<br>Возможные значения: 1, 2, 3, 4, 5. |
| 10 | result |  |  | integer | Да | Результат обращения. Важно, при значении<br>меньше, либо равно 0, результат<br>обрабатывается как 1 (обработано).<br>Возможные значения:<br>1 - обработано<br>2 - переведено<br>3 - истекло время ожидания ответа<br>4 - не отвечено<br>5 - спам<br>6 - отправка запрещена |
| 11 | assign_user_id |  |  | integer | Нет | ID сотрудника (abonent_id), назначенного<br>на обработку обращения |
| 12 | close_user_id |  |  | integer | Нет | ID сотрудника (abonent_id), закрывшего<br>обращение |
| 13 | group_id |  |  | String | Нет | ID Группы, на которую было распределено<br>обращение |
| 14 | chat |  |  | Object | Нет | История переписки |
| 14.1 |  | text |  | String | Нет | Текст сообщения |
| 14.2 |  | time |  | String | Нет | Время отправки сообщения |

| 14.3 |  | sender |  | String | Нет | Имя отправителя |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | client_info |  |  | Object | Нет | Информация о клиенте |
| 15.1 |  | name |  | String | Нет | Имя клиента |
| 15.2 |  | phone |  | String | Нет | Номер телефона |
| 16 | contact |  |  | Object | Нет | Информация о контакте |
| 16.1 |  | source_id |  | Object | Нет | Информация о пользователе в соц. сети |
|  |  |  | type | String | Нет | Тип источника (vpbx, amo, exch, google...) |
|  |  |  | index | integer | Нет | Номер источника |
| 16.2 |  | contact_id |  | String | Нет | ID контакта в разрезе источника |

Пример запроса: POST https://app.mango-office.ru/vpbx/cc/appeals/create-closed-appeals vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "channel_type": 0, "direction": 0, "entry_point": "string", "create": "1642667259", "end": "1642667259", "tag_id": [ 0 ], "comment": "string", "rate": 1, "result": 1, "assign_user_id": 0, "close_user_id": 0, "group_id": "string", "chat": [ { "text": "string", "time": "1642667259", "sender": "string" } ], "client_info": { "name": "string", "phone": "string" }, "contact": { "source_id": { "type": "string", "index": 0 }, "contact_id": "string" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметр | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |

| 1 | result |  |  | Результат выполнения запроса;<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31хх - неверные параметры;<br>● 3300 - объект не существует;<br>● 5xxx – ошибка сервера |
| --- | --- | --- | --- | --- |
| 2 | appeal_id | integer |  | ИД обращения |

Пример ответа: { "result": 1000, "appeal_id": 14136224 }
