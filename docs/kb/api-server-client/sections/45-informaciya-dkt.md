---
id: api-server-client-45-informaciya-dkt
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "3.2.4"
pdf_section: "3.2.4"
title: "Информация ДКТ"
pdf_heading: "3.2.4 Информация ДКТ"
pages: "48-49"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 48-49"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"48-49","global_pages":"48-49"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 1075
images: 0
status: extracted
ai-generated: true
---
### 3.2.4. Информация ДКТ

> Трассировка: PDF §3.2.4 · сквозные стр. 48-49 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.48-49.

routeKey="/dct"

Параметры события:

| Параметр | Тип | Описание |
| --- | --- | --- |
| routeKey | string | Тип события |
| data | object | Данные события ДКТ |
| data[entryId] | string | ID Entry звонка |
| data[uid] | string | ДКТ: uid |
| data[widgetId] | string | ДКТ: ID виджета |
| data[cid] | string | ДКТ: client_cid |
| data[yaCid] | string | ДКТ: ya_client_id |
| data[ip] | string | ДКТ: IP |
| data[regionId] | string | ДКТ: ID региона |
| data[countryCode] | string | ДКТ: код страны |
| data[regionCode] | string | ДКТ: код региона |
| data[region] | string | ДКТ: регион |
| data[city] | string | ДКТ: город |
| data[source] | string | ДКТ: Источник |
| data[medium] | string | ДКТ: Канал |
| data[campaign] | string | ДКТ: Кампания |
| data[content] | string | ДКТ: Содержимое |
| data[term] | string | ДКТ: term |
| data[duration] | string | ДКТ: Время на сайте |
| data[currentPageTitle] | string | ДКТ: Заголовок |
| data[currentPageUrl] | string | ДКТ: URL |
| data[roistat] | string | ДКТ: roistat |
| data[device] | string | ДКТ: device |
| data[newUserFlag] | boolean | ДКТ: новый пользователь |
| data[custom] | string | ДКТ: Custom |
| data[widgetName] | string | ДКТ: Имя виджета |

Параметр Тип Описание

routeKey string Тип события

data object Данные события ДКТ

data[entryId] string ID Entry звонка

data[uid] string ДКТ: uid

data[widgetId] string ДКТ: ID виджета

data[cid] string ДКТ: client_cid

data[yaCid] string ДКТ: ya_client_id

data[ip] string ДКТ: IP

data[regionId] string ДКТ: ID региона

data[countryCode] string ДКТ: код страны

data[regionCode] string ДКТ: код региона

data[region] string ДКТ: регион

data[city] string ДКТ: город

data[source] string ДКТ: Источник

data[medium] string ДКТ: Канал

data[campaign] string ДКТ: Кампания

data[content] string ДКТ: Содержимое

data[term] string ДКТ: term

data[duration] string ДКТ: Время на сайте

data[currentPageTitle] string ДКТ: Заголовок

data[currentPageUrl] string ДКТ: URL

data[roistat] string ДКТ: roistat

data[device] string ДКТ: device

data[newUserFlag] boolean ДКТ: новый пользователь

data[custom] string ДКТ: Custom

data[widgetName] string ДКТ: Имя виджета

Пример события:

{ "routeKey": "/dct", "data": { "entryId": "OTE2OTk5MDg4MA==", "uid": "XV4u5IcwpKSfGx3kvaXw", "widgetId": "20448", "productId": "400199601", "cid": "1448419958.1592496259", "yaCid": "1592496259143169716", "ip": "81.88.83.28", "regionId": "", "countryCode": "RU", "regionCode": "MOW", "region": "", "city": "Москва", "source": "(direct)", "medium": "(none)", "campaign": "(none)", "content": "(none)", "term": "(none)", "duration": 0, "currentPageTitle": "Ки***ин (40010) | drupal.dev", "currentPageUrl": "http://mango-office.ru/node/1716", "roistat": "42405", "type": "call", "device": "desktop", "newUserFlag": false, "custom": "", "widgetName": "802730 ITG" } }
