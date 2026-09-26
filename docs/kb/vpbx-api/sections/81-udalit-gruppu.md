---
id: vpbx-api-81-udalit-gruppu
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.5"
pdf_section: "3.7.5"
title: "Удалить группу"
pdf_heading: "3.7.5 Удалить группу"
pages: "121"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 121"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"121","global_pages":"121"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 526
status: extracted
ai-generated: true
---
# 3.7.5. Удалить группу

> Трассировка: PDF §3.7.5 · сквозные стр. 121 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.121.

POST /vpbx/group/delete Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | group_id |  |  | Id группы, которую нужно удалить. Получить значение<br>можно запросом получить список групп |

Пример запроса: POST https://app.mango-office.ru/vpbx/group/delete vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "group_id":"10049774" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>■ 1000 – действие выполнено успешно;<br>■ 3100 - переданы неверные параметры команды;<br>■ 3300 - объект не существует;<br>■ 5XXX – ошибка сервера:<br>* 5201 - Опция "Разрешаю подключать услуги ВАТС средствами API<br>конструктора" не активирована;<br>* 5202 - Группа/сотрудник задействованы в схеме переадресации;<br>* 5203 - Группа/сотрудник задействованы в переадресации по номеру<br>клиента;<br>* 5204 - Группа/сотрудник задействованы в виджете обратных звонков. |

Пример ответа: { "result": 1000 }
