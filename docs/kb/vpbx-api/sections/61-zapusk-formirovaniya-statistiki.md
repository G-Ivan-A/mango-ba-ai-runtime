---
id: vpbx-api-61-zapusk-formirovaniya-statistiki
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.4.2.2"
pdf_section: "3.4.2.2"
title: "Запуск формирования статистики"
pdf_heading: "3.4.2.2 Запуск формирования статистики"
pages: "71-72"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 71-72"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"71-72","global_pages":"71-72"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1365
status: extracted
ai-generated: true
---
# 3.4.2.2. Запуск формирования статистики

> Трассировка: PDF §3.4.2.2 · сквозные стр. 71-72 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.71-72.

POST /vpbx/stats/calls/request Команда предназначена для запуска формирования статистики. Выходные данные генерируются системой API ВАТС с учётом фильтра. Фильтр задаётся во входных параметрах запроса. Все параметры запроса опциональны, за исключением start_date, end_date, limit & offset. Присутствие этих 4-х параметров обязательно в запросе, причём должно выполняться условие - разница дат не может превышать месяц, т.е. есть ограничение на период выборки, равный одному месяцу. Поля context_type, context_status и recall_status заполняются по следующему правилу: поле recall_status проставляется только если context_type = 1 context_status = 0, в остальном любые комбинации. Входные параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | start_date | string | Да | Дата/время начала выборки, строка совместимая с форматом<br>класса datetime [[http://php.net/manual/en/class.datetime.php]] (если<br>время не передается, по умолчанию берется 00:00:00). |
| 2 | end_date | string | Да | Дата/время окончания выборки, строка совместимая с форматом<br>класса datetime [[http://php.net/manual/en/class.datetime.php]] (если<br>время не передается, по умолчанию берется 00:00:00). |
| 3 | user_ids | array [integer,<br>...] | Нет | Идентификаторы сотрудников, участвовавших в звонке. Массив<br>целочисленных значений, значения идентичны general.user_id из<br>запроса Запрос списка сотрудников ВАТС. |
| 4 | group_ids | array [integer,<br>...] | Нет | Идентификаторы групп, участвовавших в звонке. Массив<br>целочисленных значений, значения идентичны group_id из<br>/vpbx/groups. |
| 5 | context_type | integer/array<br>[integer, ...] | Нет | Тип cтатус звонка: 1 – входящий, 2 – исходящий, 3 – внутренний. |

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 6 | context_status | integer | Нет | Признак успешности звонка: 1 – успешный, 0 – неуспешный. |
| 7 | recall_status | integer | Нет | Признак успешности перезвона для входящих:<br>0 - неуспешный перезвон, 1 - успешный перезвон,<br>2 - нет перезвона. |
| 8 | search_string | string | Нет | Поисковая строка (минимум 3 символа, фильтрует по вхождениям<br>в номерах внешних/внутренних). |
| 9 | limit | integer | Да | Лимит выборки, целочисленное (допустимые значения - 1, 5, 10,<br>20, 50, 100, 500, 1000, 2000, 5000). |
| 10 | offset | integer | Да | Смещение начала выборки, целочисленное, обязательное. |
| 11 | ext_params | integer | Нет | Получить данные КЦ: 0 - нет, 1 - да, получить. |
| 12 | ext_fields | array [string, ...] | Нет | Список дополнительных полей в ответе;<br>● 'context_cost_full': тип «string», стоимость по всему звонку;<br>● 'context_cost_tariff': тип «string», стоимость без услуг по звонку. |

Пример запроса: POST https://app.mango-office.ru/vpbx/stats/calls/request/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "start_date":"31.10.2019 00:00:00", "end_date":"29.11.2019 23:59:59", "limit":"100", "offset":"0" } Результат: В ответе на запрос приходит ключ, с помощью которого можно будет получить статистику по завершению ее построения. Пример ответа: { "key": "BK7TWiy3+Lku1yV0lfHJ2mmMBZ1Cnu" }
