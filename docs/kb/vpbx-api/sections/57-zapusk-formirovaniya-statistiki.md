---
id: vpbx-api-57-zapusk-formirovaniya-statistiki
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.4.1.1"
pdf_section: "3.4.1.1"
title: "Запуск формирования статистики"
pdf_heading: "3.4.1.1 Запуск формирования статистики"
pages: "66-69"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 66-69"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"66-69","global_pages":"66-69"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1805
status: extracted
ai-generated: true
---
# 3.4.1.1. Запуск формирования статистики

> Трассировка: PDF §3.4.1.1 · сквозные стр. 66-69 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.66-69.

POST /vpbx/stats/request Команда предназначена для запуска формирования базовой статистики. Выходные данные генерируются ВАТС с учётом фильтра. Фильтр задаётся во входных параметрах запроса. Все параметры запроса опциональны, за исключением date_from и date_to. Присутствие этих двух параметров обязательно в запросе, причём должно выполняться условие — разница дат не может превышать месяц, т.е. есть ограничение на период выборки, равный одному месяцу. Входные параметры:

| № | Параметры с<br>уровнями<br>вложенности |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | date_from |  | timestamp | Да | Предоставить статистику с указанного времени. Формат<br>данных — timestamp (unix время, часовой пояс utc+3), даёт<br>возможность указать время с точностью до одной секунды. |
| 2 | date_to |  | timestamp | Да | Предоставить статистику по указанное время. |
| 3 | fields |  | string | Нет | Позволяет указать какие поля (см. список возможных<br>полей ниже) и в каком порядке необходимо включить в<br>выгрузку. Значение по умолчанию:<br>- records,<br>- start,<br>- finish,<br>- answer,<br>- from_extension,<br>- from_number,<br>- to_extension,<br>- to_number,<br>- disconnect_reason,<br>- line_number,<br>- location.<br>Примечание. Чтобы связывать звонки из истории с<br>событиями, вы можете в параметре fields указать поле<br>entry_id (внутренний идентификатор группы вызовов. Не<br>имеет отношения к CALL-ID из<br>SIP-протокола). |
| 4 | from |  |  |  | Данные, относящиеся строго к вызывающему абоненту. |
| 4.1 |  | extension |  |  | Идентификатор сотрудника ВАТС для вызывающего<br>абонента. |
| 4.2 |  | number | string |  | Номер вызывающего абонента (строка) (для PSTN номеров<br>в формате E164). |
| 5 | to |  |  |  | Данные, относящиеся строго к вызываемому абоненту. |
| 5.1 |  | extension |  |  | Идентификатор сотрудника ВАТС для вызываемого<br>абонента. |
| 5.2 |  | number | string |  | Номер вызываемого абонента (строка) (для PSTN номеров<br>в формате E164). |
| 6 | call_party |  |  |  | Данные, относящиеся к вызываемому или вызывающему<br>абоненту. Использование поля допустимо только без<br>заполнения полей to и from. |
| 6.1 |  | extension |  |  | Идентификатор сотрудника ВАТС. |
| 6.2 |  | number | string |  | Номер абонента (для PSTN номеров в формате E164) |
| 7 | request_id |  | string |  | Идентификатор запроса (строка не более 128 байт),<br>опциональное поле. Формируется внешней системой.<br>ВАТС никак не обрабатывает этот идентификатор, не<br>анализирует и не полагается на уникальность его значения.<br>Идентификатор можно использовать для связи запроса с<br>результатом его выполнения и возможными<br>последующими событиями, которые появляются в<br>результате обработки запроса. |

Примеры запроса. Пример 1. Все вызовы с участием сотрудника: POST https://app.mango-office.ru/vpbx/stats/request vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "date_from": "1072915200", "date_to": "1072997812", "fields": "records, start, finish, from_extension, from_number, to_extension, to_number, disconnect_reason", "call_party": { "extension": "789" }, "request_id": "request222320" } Пример 2. Все вызовы с участием клиента: POST https://app.mango-office.ru /vpbx/stats/request vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "date_from": "1072915200", "date_to": "1072997812", "fields": "records, start, finish, from_extension, from_number, to_extension, to_number, disconnect_reason", "call_party": { "number": "79123456789" }, "request_id": "request222320" } Пример 3. Вызовы от сотрудника: POST https://app.mango-office.ru/vpbx/stats/request vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "date_from": "1072915200", "date_to": "1072997812", "fields": "records, start, finish, from_extension, from_number, to_extension, to_number, disconnect_reason", "from": { "extension": "123" }, "request_id": "request2322320" } Пример 4. Вызовы сотруднику: POST https://app.mango-office.ru/vpbx/stats/request vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = {"date_from": "1072915200", "date_to": "1072997812", "fields": "records, start, finish, from_extension, from_number, to_extension, to_number, disconnect_reason", "to": { "extension": "123" }, "request_id": "request2322320" } Результат: В ответе на запрос приходит ключ, с помощью которого можно будет получить статистику по завершению ее построения. Пример ответа: { "key":"B+DvIt8hPJReV8v4MYspQQA==" }
