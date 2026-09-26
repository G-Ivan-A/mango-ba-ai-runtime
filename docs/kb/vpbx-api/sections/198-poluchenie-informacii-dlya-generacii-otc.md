---
id: vpbx-api-198-poluchenie-informacii-dlya-generacii-otc
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.6.12"
pdf_section: "4.6.12"
title: "Получение информации для генерации отчёта исходящего обзвона"
pdf_heading: "4.6.12 Получение информации для генерации отчёта исходящего обзвона"
pages: "278-281"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 278-281"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"278-281","global_pages":"278-281"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 2631
status: extracted
ai-generated: true
---
# 4.6.12. Получение информации для генерации отчёта исходящего обзвона

> Трассировка: PDF §4.6.12 · сквозные стр. 278-281 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.278-281.

POST /vpbx/campaign-report/create Метод позволяет получить данные для отчета исходящего обзвона. Параметры:

| № | Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | campaign_id | Число | Да | ID кампании |

POST https://app.mango-office.ru/vpbx/campaign-report/create vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "campaign_id": 56919 } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие компоненты:

| № | Параметры с уровнями вложенности |  |  |  | Тип<br>данных | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |  |  |  |
| 1 | result |  |  |  | Число | Да | Код результата |
| 2 | data |  |  |  | Объект | Да | Данные по кампании |
| 2.1 |  | campaign_id |  |  | Число | Да | ID кампании |
| 2.2 |  | tasks [] |  |  | Массив | Да | Задачи кампании |
| 3.1 |  |  | task_id |  | Число | Да | ID задачи |
| 3.2 |  |  | attempts [] |  | Массив | Да | Попытки обзвона кампании |
| 4.1 |  |  |  | attempt_id | Число | Да | ID попытки |
| 4.2 |  |  |  | name | string | Да | Имя клиента, которому<br>адресован звонок |
| 4.3 |  |  |  | position | string | Да | Должность контактного лица |
| 4.4 |  |  |  | organization | string | Да | Название организации |
| 4.5 |  |  |  | record_id | Число | Да | Идентификатор записи<br>разговора |
| 4.6 |  |  |  | phone | string | Да | Номер телефона адресата, от<br>которого получена обратная<br>связь |
| 4.7 |  |  |  | sms | string | Да | Код подтверждения<br>полученный по SMS |
| 4.8 |  |  |  | text | string | Да | Транскрибация ответа на<br>исходящий обзвон |
| 4.9 |  |  |  | number | string | Да | Код подтверждения<br>полученный по телефону –<br>цифра, набранная при<br>голосовом исходящем обзвоне |
| 4.10 |  |  |  | result | Число | Да | Код результата попытки:<br>1 - разговор состоялся;<br>2 - абонент занят;<br>3 - абонент не взял трубку;<br>4 - абонент недоступен;<br>5 - оператор занят; |

| № | Параметры с уровнями вложенности |  |  |  | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | 6 - оператор не взял трубку;<br>7 - оператор недоступен;<br>8 - номер внешнего абонента<br>не существует;<br>10 - оператор не дождался<br>ответа клиента;<br>11 - остановлен администратором;<br>20 - остановлен оператором;<br>21 - антиробот: абонент<br>недоступен;<br>22 - антиробот: абонент занят;<br>23 - антиробот: голосовая почта;<br>24 - клиент повесил трубку во<br>время анализа антироботом;<br>26 - номер находится в списке<br>запрещённых номеров. |

Пример ответа: { "result": 1000, "data": { "campaign_id": 56919, "tasks": [ { "task_id": 870224817, "attempts": [ { "attempt_id": 1103498743, "name": "Евгеньев Евгений Евгеньевич", "position": null, "organization": null, "record_id": "MToxMDE4OTAxMToxNjAzNTMwMjk0NTow", "phone": null, "sms": null, "text": null, "number": null, "result": 1 }, { "attempt_id": 1103507574, "name": "Евгеньев Евгений Евгеньевич", "position": null, "organization": null, "record_id": "MToxMDE4OTAxMToxNjAzNTMwMjk0NTow", "phone": null, "sms": null, "text": null, "number": null, "result": 1 }, { "attempt_id": 1103520744, "name": "Евгеньев Евгений Евгеньевич", "position": null, "organization": null, "record_id": "MToxMDE4OTAxMToxNjAzNTMwMjk0NTow", "phone": null, "sms": null,

| "text": null,<br>"number": null,<br>"result": 1 |
| --- |
| }<br>] |
| },<br>{ |
| "task_id": 870218547,<br>"attempts": [<br>{ |
| "attempt_id": 1103475052,<br>"name": "Евгеньев Евгений Евгеньевич",<br>"position": null,<br>"organization": null, |
| "record_id": "MToxMDE4OTAxMToxNjAzNDczMTMyMzow",<br>"phone": null,<br>"sms": null, |
| "text": null,<br>"number": null, |
| "result": 1<br>},<br>{ |
| "attempt_id": 1103498712,<br>"name": "Евгеньев Евгений Евгеньевич",<br>"position": null, |
| "organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzNDczMTMyMzow",<br>"phone": null,<br>"sms": null,<br>"text": null,<br>"number": null,<br>"result": 1<br>},<br>{<br>"attempt_id": 1103504238,<br>"name": "Евгеньев Евгений Евгеньевич",<br>"position": null,<br>"organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzNDczMTMyMzow", |
| "phone": null,<br>"sms": null,<br>"text": null, |
| "number": null,<br>"result": 1<br>}<br>]<br>},<br>{<br>"task_id": 870144471,<br>"attempts": [<br>{<br>"attempt_id": 1103381398,<br>"name": "Евгеньев Евгений Евгеньевич",<br>"position": null,<br>"organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzMjA2ODc3NTow",<br>"phone": null,<br>"sms": null,<br>"text": null, |
| "number": null,<br>"result": 1 |
| }<br>] |

| },<br>{<br>"task_id": 870093894, |
| --- |
| "attempts": [<br>{ |
| "attempt_id": 1103329125,<br>"name": "Евгеньев Евгений Евгеньевич", |
| "position": null,<br>"organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzMTY1NjE5NTow", |
| "phone": null,<br>"sms": null,<br>"text": null,<br>"number": null, |
| "result": 1<br>},<br>{ |
| "attempt_id": 1103366389,<br>"name": "Евгеньев Евгений Евгеньевич", |
| "position": null,<br>"organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzMTY1NjE5NTow", |
| "phone": null,<br>"sms": null,<br>"text": null, |
| "number": null,<br>"result": 1<br>}<br>]<br>},<br>{<br>"task_id": 870000538,<br>"attempts": [<br>{<br>"attempt_id": 1103336127,<br>"name": "Евгеньев Евгений Евгеньевич",<br>"position": null,<br>"organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzMTc2NjA5Mzow", |
| "phone": null,<br>"sms": null,<br>"text": null, |
| "number": null,<br>"result": 1<br>},<br>{<br>"attempt_id": 1103364624,<br>"name": "Евгеньев Евгений Евгеньевич",<br>"position": null,<br>"organization": null,<br>"record_id": "MToxMDE4OTAxMToxNjAzMTc2NjA5Mzow",<br>"phone": null,<br>"sms": null,<br>"text": null,<br>"number": null,<br>"result": 1<br>}<br>]<br>} |
| ]<br>} |
| } |
