---
id: vpbx-api-237-poluchenie-istorii-soobscheniy
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.10.2.5"
pdf_section: "4.10.2.5"
title: "Получение истории сообщений"
pdf_heading: "4.10.2.5 Получение истории сообщений"
pages: "321-323"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 321-323"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"321-323","global_pages":"321-323"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1121
status: extracted
ai-generated: true
---
# 4.10.2.5. Получение истории сообщений

> Трассировка: PDF §4.10.2.5 · сквозные стр. 321-323 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.321-323.

POST /cc/get_chat_history Позволяет получить историю сообщений чата. Вы можете в методе указать id сообщения, начиная от которого можно получить до 50 сообщений, предшевствовавших указанному сообщению. Примечания: 1) если обращение еще не взято в работу, то при запросе /cc/get_chat_history Клиенту вернется пустой массив (то есть, никакой истории Клиент не получит); 2) если обращение закрыто, то при запросе /cc/get_chat_history Клиенту вернется пустой массив (то есть, никакой истории Клиент не получит). Параметры метода:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | channelId | Число | Да | Id текстового канала Манго Диалогов, через<br>который отправлялись соообщения |
| 2 | userId | Строка | Да | Id клиента на стороне внешней системы |
| 3 | toId | Строка | Нет | messageId до которого нужно получить историю |

Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Подробнее об этих обязательных полях… Примеры запроса. 1) Получения последних 50-ти сообщений POST https://app.mango-office.ru/cc/get_chat_history vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "channelId": 40771, "userId": "KdpikRr7aLbBheMGnFAk" } 2) Получения 50-ти сообщений старее, чем messageId POST https://app.mango-office.ru/cc/get_chat_history vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "channelId": 40771, "userId": "KdpikRr7aLbBheMGnFAk", "toId": "40821" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнем<br>вложенности |  |  | Тип | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |
| 1 | data[] |  |  | Массив | Массив истории сообщений |
| 1.1 |  | messageId |  | Строка | Id сообщения |
| 1.2 |  | isClientMessage |  | Bool | Признак того является ли сообщение клиентским |
| 1.3 |  | type |  | Строка | Тип сообщения |
| 1.4 |  | time |  | Число | Временная метка |
| 1.5 |  | payload |  | Объект | Объект сообщения |
|  |  |  | body | Строка | Содержимое сообщения |

Пример ответа: { "result": 1000, "data": [ { "messageId": "435434578998201120", "isClientMessage": true, "type": "text", "time": 1684916324211, "payload": { "body": "Hi" } }, { "messageId": "435434580821686688", "isClientMessage": false, "type": "text", "time": 1684916331334, "payload": { "body": "Hello" } }, { "messageId": "435434582343220768", "isClientMessage": true, "type": "text", "time": 1684916337278, "payload": { "body": "How are you" } }, { "messageId": "435434588064726304", "isClientMessage": false, "type": "text", "time": 1684916359627, "payload": { "body": "I'm fine thanks" } } ]}
