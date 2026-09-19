---
id: vpbx-api-97-sozdat-sip-uchetku
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.19"
pdf_section: "3.7.19"
title: "Создать sip-учетку"
pdf_heading: "3.7.19 Создать sip-учетку"
pages: "140-141"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 140-141"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"140-141","global_pages":"140-141"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 608
status: extracted
ai-generated: true
---
# 3.7.19. Создать sip-учетку

> Трассировка: PDF §3.7.19 · сквозные стр. 140-141 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.140-141.

POST /vpbx/sip/create Метод позволяет создать sip учетку для сотрудника. При выборе имени SIP в домене второго уровня, если в Личном кабинете включена функция «API коннектор», происходит подключение услуги «Красивый sip адрес». Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | user_id | integer | Да | ID пользователя, чья SIP-учётка [обязательное] |
| 2 | login | string |  | Логин [обязательное] |
| 3 | domain | string |  | Домен [обязательное] |
| 4 | password | string | Да | Пароль [обязательное] |
| 5 | description | string |  | Описание |

Пример запроса: POST https://app.mango-office.ru/vpbx/sip/create vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "user_id":"300022222", "login":"sipLogin", "domain":"vpbx300011111.mangosip.ru", "password":"sipPassword", "description":"sip Description" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  | Да | Код результата |
| 2 | sip_id |  |  | ID созданной SIP-учётки |

Пример ответа: { "result": 1000, "sip_id": 100333333 } result

| 1000 | удачное выполнение |
| --- | --- |
| 3100 | переданы неверные параметры команды |
| 31XX | неверные параметры |
| 3300 | объект не существует |
| 5XXX | исключение |
