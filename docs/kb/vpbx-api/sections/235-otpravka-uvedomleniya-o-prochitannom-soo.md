---
id: vpbx-api-235-otpravka-uvedomleniya-o-prochitannom-soo
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.10.2.3"
pdf_section: "4.10.2.3"
title: "Отправка уведомления о прочитанном сообщении"
pdf_heading: "4.10.2.3 Отправка уведомления о прочитанном сообщении"
pages: "319-320"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 319-320"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"319-320","global_pages":"319-320"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 513
status: extracted
ai-generated: true
---
# 4.10.2.3. Отправка уведомления о прочитанном сообщении

> Трассировка: PDF §4.10.2.3 · сквозные стр. 319-320 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.319-320.

POST /cc/event_message_read Позволяет отправлять уведомления о прочитанном сообщении из внешнего приложения в Контакт-центр MANGO OFFICE. Параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | channelId | Число | Да | Id текстового канала Манго Диалогов, через<br>который отправится уведомление |
| 2 | userId | Строка | Да | Id клиента на стороне внешней системы |
| 3 | time | Число | Да | Время, когда сообщение было прочитано |
| 4 | serverMessageId | Строка | Да | Id сообщения |

Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Подробнее об этих обязательных полях… Пример запроса: POST https://app.mango-office.ru/cc/event_message_read vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "channelId": 40771, "userId": "123qwert", "time": 1690290852274, "serverMessageId": "436829657578282400" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие код ошибки. Примеры ответа. Пример успешного ответа: { "result": 1000 } Пример ответа с ошибкой: { "result": 5000 }
