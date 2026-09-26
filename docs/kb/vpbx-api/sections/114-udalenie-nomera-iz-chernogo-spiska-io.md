---
id: vpbx-api-114-udalenie-nomera-iz-chernogo-spiska-io
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.8.3.6"
pdf_section: "3.8.3.6"
title: "Удаление номера из \"черного\" списка ИО"
pdf_heading: "3.8.3.6 Удаление номера из \"черного\" списка ИО"
pages: "155-156"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 155-156"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"155-156","global_pages":"155-156"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 604
status: extracted
ai-generated: true
---
# 3.8.3.6. Удаление номера из "черного" списка ИО

> Трассировка: PDF §3.8.3.6 · сквозные стр. 155-156 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.155-156.

POST /vpbx/outbound_blacklist/delete Удаление номеров ч/б ИО. Примечание. Для вызова метода требуется в ВАТС наличие подключенной услуги "Черный и белый списки" и включенной опции запрета на исходящие коммуникации. Параметры запроса:

| Параметры | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| numbers | array | Да | Список номеров |

Пример запроса: POST https://app.mango-office.ru/vpbx/outbound_blacklist/delete vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "numbers": ["71234567890"] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие код ошибки:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>● 1000 - команда выполнена успешно;<br>● 3100 - ошибка валидации;<br>● 3103 - в запросе отсутствует обязательный параметр;<br>● 3104 - параметр передан в неправильном формате;<br>● 3136 - неправильный формат номера;<br>● 3300 - правило не найдено; |
|  |  |  |  | ● 5000 - внутренняя ошибка сервера;<br>● 5004 - таймаут запроса в БД;<br>● 5008 - не подлючена услуга "Черный и белый списки" в ВАТС<br>или услуга Контакт-центра "Исходящий обзвон PRO", или опция<br>блокировки исходящих номеров. |

Пример ответа: { "result": 1000 }
