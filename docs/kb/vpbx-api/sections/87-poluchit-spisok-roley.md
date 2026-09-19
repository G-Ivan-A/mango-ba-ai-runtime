---
id: vpbx-api-87-poluchit-spisok-roley
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.7.11"
pdf_section: "3.7.11"
title: "Получить список ролей"
pdf_heading: "3.7.11 Получить список ролей"
pages: "128-129"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 128-129"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"128-129","global_pages":"128-129"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 593
status: extracted
ai-generated: true
---
# 3.7.11. Получить список ролей

> Трассировка: PDF §3.7.11 · сквозные стр. 128-129 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.128-129.

POST /vpbx/roles Настройка ролей выполняется в Личном кабинете. Метод используется для управления сотрудниками по API. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/roles vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | role_id |  |  | id роли |
| 2 | name |  |  | Название роли |
| 3 | permissions |  |  | Установленные привилегии роли |

Пример ответа: { "result": 1000, "roles": [ { "role_id": 10453, "name": "Администратор", "permissions: [ { "code": "cc_recording_softphone" }, { "code": "adv_banners_ldap" }, ..., { "code": "sip_trunk_can_manage" }, { "code": "perm_personal_manager_view" }, { "code": "cc_change_status_to_offline", "param": "3" }, { "code": "addressbook_manage" } ] }, { "role_id": 10452, "name": "Бухгалтер", "permissions": [ { "code": "cc_recording_softphone" }, { "code": "recording_records_access", "param": "3" }, ..., { "code": "perm_personal_manager_view" }, { "code": "cc_change_status_to_offline", "param": "1" }, { "code": "addressbook_manage" } ] }, { "role_id": 3, "name": "Нет доступа", "permissions": [] } ]}
