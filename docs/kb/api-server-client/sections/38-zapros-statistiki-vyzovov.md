---
id: api-server-client-38-zapros-statistiki-vyzovov
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.1.22"
pdf_section: "3.1.22"
title: "Запрос статистики вызовов"
pdf_heading: "3.1.22 Запрос статистики вызовов"
pages: "37-41"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 37-41"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"37-41","global_pages":"37-41"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 2346
images: 0
status: extracted
ai-generated: true
---
### 3.1.22. Запрос статистики вызовов

> Трассировка: PDF §3.1.22 · сквозные стр. 37-41 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.37-41.

Доступность запроса определяется наличием включенной услуги на продукте ВАТС API_VBPX_STAT

Для работы API v1 статистика в настройке ВАТС должен быть указан адрес внешней системы: PROD

https://api-client.mango-office.ru/api/v1

Получение статистики состоит из следующих этапов:

1. Запуск формирования статистики 2. Получение статистики

3.1.22.1 Запуск формирования статистики

POST /адрес/callstat/request?USER_ID={ext}&DATE={date} Header[X-Mango- API-Token, X-Mango-API-Salt]

Команда предназначена для запуска формирования статистики. Выходные данные генерируются системой API с учётом заданных параметров. Все параметры запроса обязательны.

В ответе приходит ключ, с помощью которого можно будет получить статистику по завершению ее построения.

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| USER_ID | string | Да | Внутренний номер сотрудника |  |
| DATE | date | Да | YYYY-MM-DD | Дата формирования статистики |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

Внутренний USER_ID string Да номер сотрудника

DATE date Да YYYY-MM-DD Дата формирования статистики

Пример запроса:

POST /адрес/callstat/request?USER_ID=8000&DATE=2017-08-28

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Result[data] | object |  |
| Result[data][key] | string | Ключ запроса на формирование статистики |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Result[data] object

Result[data][key] string Ключ запроса на формирование статистики

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 400 - Ключ подписи не задан. Result[code]=103, Result[message]="Salt not present"

● 400 - не верный ключ создания подписи. Result[code]=103, Result[message]="Salt is incorrect"

● 400 - дата некорректная. Result[code]=103, Result[message]="Incorrect date" ● 400 - Пользователь не найден в интеграции. Result[code]=103, Result[message]="User not found"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "key": " aIpiD52TBgRGvACkg0tlaKo/aVIq2eM/1W88SCvrhOOvCebb6AG9IcwtZ2DKjEWuTLvFw==" } }

3.1.22.2 Получение статистики

Подготовленные данные хранятся до первого обращения за ними не менее 1 минуты. API предусматривает две стратегии получения результата: ожидание получения специального события API о завершении построения и периодический опрос сервиса.

Обращаться к сервису за готовыми данными следует запросом вида:

POST /v1/callstat/result?USER_ID={ext}&PAGE_LIMIT={pageLimit}&PAGE={page}

Header[X-Mango-API-Token, X-Mango-API-Salt]

Параметры запроса:

| Параметр | Тип | Обяза- тель- ность | Формат |
| --- | --- | --- | --- |
| PAGE_LIMIT | string | Нет | Количество записей на страницу, в случае отсутствия параметра выводятся все записи |
| PAGE | string | Нет | Номер страницы с учетом PAGE_LIMIT, в случае отсутствия параметра выводятся все записи |

Обяза-

Параметр Тип

тель-

Формат

ность

Количество записей на страницу, в случае PAGE_LIMIT string Нет отсутствия параметра выводятся все записи

Номер страницы с учетом PAGE_LIMIT, в случае PAGE string Нет отсутствия параметра выводятся все записи

В теле запроса необходимо передавать следующие параметры:

| Параметр | Тип | Обяза- тель- ность | Формат | Описание |
| --- | --- | --- | --- | --- |
| Key | object | Да |  |  |
| Key[key] | string | Да | Ключ доступа к отчету |  |

Обяза-

Параметр Тип

тель-

Формат Описание

ность

Key object Да

Key[key] string Да Ключ доступа к отчету

Пример запроса:

POST /v1/callstat/result?USER_ID=8000&PAGE_LIMIT=3&PAGE=1

Параметры ответа:

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result | object |  |
| Result[code] | integer |  |
| Result[message] | string |  |
| Result[data] | object |  |

Параметр Тип Описание

Result object

Result[code] integer

Result[message] string

Result[data] object

| Параметр | Тип | Описание |
| --- | --- | --- |
| Result[data][count] | int | Количество записей всего |
| Result[data][page] | int | Номер страницы |
| Result[data][pageLimit] | int | Количество записей на страницу |
| Result[data][pageCount] | int | Количество страниц |
| Result[data][stat] | array | Массив статистических данных о звонках |
| Result[data][stat][index][callDate] | string | Дата поступления звонка |
| Result[data][stat][index][startDate] | string | Дата, время ответа на вызов |
| Result[data][stat][index][disconec tedReason] | string | Код завершения вызова |
| Result[data][stat][index][did] | string | Номер, на который поступил звонок (номер компании) |
| Result[data][stat][index][billSec] | string | Длительность разговора |
| Result[data][stat][index][fromExt] | string | Идентификатор сотрудника ВАТС для вызывающего абонента. Не передается в случае, если ВАТС не удалось идентифицировать вызывающего абонента как сотрудника ВАТС, либо у сотрудника ВАТС нет идентификатора (внутреннего номера). |
| Result[data][stat][index][fromNu mber] | string | Номер источник звонка |
| Result[data][stat][index][toNumber] | string | Номер назначения |
| Result[data][stat][index][toExt] | string | Идентификатор сотрудника ВАТС для вызываемого абонента. Опциональный параметр. Не передается в случае, если ВАТС не удалось идентифицировать вызываемого абонента как сотрудника ВАТС, либо у сотрудника ВАТС нет идентификатора (внутреннего номера). |
| Result[data][stat][index][type] | string | Тип звонка - входящий, исходящий, внутренний. Допустимые значения: INBOUND, OUTBOUND, INTERNAL, UNKNOWN |
| Result[data][stat][index][records] | string[] | Массив идентификаторов записей разговоров [rec1,rec2,rec3] |

Возможны следующие HTTP коды ответа:

● 200 - Result[code]=0 ● 400 - Ключ не найден в интеграции. Result[code]=103, Result[message]="Key not found"

● 400 - Ключ подписи не задан. Result[code]=103, Result[message]="Salt not present"

● 400 - не верный ключ создания подписи. Result[code]=103, Result[message]="Salt is incorrect"

● 401 - Ключ интеграции не прошел валидацию. Result[code]=103 ● 500 - ошибка сервера

Пример ответа:

{ "result": { "code": "0", "message": "OK" }, "data": { "count": 1, "page": 1, "pageLimit": 3, "pageCount": 1, "stat": [{ "callDate": "1504791513", "startDate": "0", "disconnectReason": "1100", "did": "74951204609", "billSec": "0", "fromExt": "8000", "fromNumber": "sip:dshi@vpbx400022984.mangosip.ru", "toNumber": "79269226127", "toExt": "", "type": "OUTBOUND", "records": [""] } ] } }
