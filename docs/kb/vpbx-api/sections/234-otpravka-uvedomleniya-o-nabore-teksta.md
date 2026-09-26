---
id: vpbx-api-234-otpravka-uvedomleniya-o-nabore-teksta
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.10.2.2"
pdf_section: "4.10.2.2"
title: "Отправка уведомления о наборе текста"
pdf_heading: "4.10.2.2 Отправка уведомления о наборе текста"
pages: "319"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 319"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"319","global_pages":"319"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 477
status: extracted
ai-generated: true
---
# 4.10.2.2. Отправка уведомления о наборе текста

> Трассировка: PDF §4.10.2.2 · сквозные стр. 319 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.319.

POST /cc/user_typing Позволяет отправлять уведомления о наборе текста из внешнего приложения в Контакт- центр MANGO OFFICE. Параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | channelId | Число | Да | Id текстового канала Манго Диалогов, через<br>который отправится уведомление |
| 2 | userId | Строка | Да | Id клиента на стороне внешней системы |
| 3 | typing | Логический | Да | Состояние печати |

Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Подробнее об этих обязательных полях… Пример запроса: POST https://app.mango-office.ru/cc/user_typing vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "channelId": 40771, "userId": "123qwerty", "typing": false } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обязательный |
| --- | --- | --- | --- |
| 1 | result |  | Да |

Пример успешного ответа: { "result": 1000 }
