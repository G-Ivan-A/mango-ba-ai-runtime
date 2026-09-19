---
id: vpbx-api-98-redaktirovat-sip-uchetku
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.20"
pdf_section: "3.7.20"
title: "Редактировать sip-учетку"
pdf_heading: "3.7.20 Редактировать sip-учетку"
pages: "141-142"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 141-142"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"141-142","global_pages":"141-142"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 733
status: extracted
ai-generated: true
---
# 3.7.20. Редактировать sip-учетку

> Трассировка: PDF §3.7.20 · сквозные стр. 141-142 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.141-142.

POST /vpbx/sip/update Метод позволяет редактировать sip учетку для сотрудника. При выборе имени SIP в домене второго уровня, если до редактирования домен был не второго уровня и в ЛК указано «Разрешаю подключать услуги ВАТС средствами API конструктора», происходит подключение услуги «Красивый sip адрес». Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | sip_id | integer | Да | ID SIP-учётки [обязательное] |
| 2 | user_id | integer |  | ID пользователя, чья SIP-учётка |
| 3 | login | string |  | Логин [обязательное, если указан domain. Передаются<br>login и domain вместе либо ни одно из этих полей] |
| 4 | domain | string |  | Домен [обязательное, если указан login. Передаются<br>login и domain вместе либо ни одно из этих полей] |
| 5 | password | string |  | Пароль |

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 6 | description | string |  | Описание |

Пример запроса: POST https://app.mango-office.ru/vpbx/sip/update vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "login":"3000222222LoginB2", "domain":"tst1.mangosip.ru", "description":"Description 2 Updated", "sip_id":"100111111" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31XX - неверные параметры;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера. |

Пример ответа: { "result": 1000, }
