---
id: vpbx-api-171-statusy-polzovateley-produkta
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.4.1.3"
pdf_section: "4.4.1.3"
title: "Статусы пользователей продукта"
pdf_heading: "4.4.1.3 Статусы пользователей продукта"
pages: "227-229"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 227-229"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"227-229","global_pages":"227-229"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 878
status: extracted
ai-generated: true
---
# 4.4.1.3. Статусы пользователей продукта

> Трассировка: PDF §4.4.1.3 · сквозные стр. 227-229 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.227-229.

POST /cc/get_presence Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | abonent_id | Целое | Нет | Идентификатор пользователя, передается если нужны данные<br>конкретного пользователя |
| 2 | session_types | Object | Нет | Массив строк. Фильтр типов сессий presence. Значения типов:<br>● sip - sip сессии;<br>● сс - сессии операторов в кц/цов;<br>● mtm - сессии операторов в m.talker (мобильные версии);<br>● mtd - сессии операторов в m.talker (настольные версии) |

Примечание. Если привязки к пользователю не обнаружилось, то в ответ вернётся пустой объект. Пример запроса: POST https://app.mango-office.ru/cc/get_presence vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "session_types": ["cc"] } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | result |  |  | Код результата |
| 2 | abonents |  |  | Объекты в формате "данные абонента" (описание этого формата см.<br>Ниже по тексту) |

Пример ответа: { "result":1000, "abonents": [ { abonent1 doc }, { abonent2 doc }, // ... { abonentN doc } ] } Описание формата «Данные абонента»: - общие для всех типов: ● uac - cтрока, идентификатор ПО пользователя (User Agent); ● ip - строка, ip адрес пользователя; ● timestamp - целое, время обновления в UTC; ● poss - массив целых, возможности пользователя; - дополнительные поля для типа "sip": ● uname - строка, учетная запись sip; - дополнительные поля для типа "cc": ● status - целое, статус пользователя в КЦ; ● device - строка, идентификатор устройства пользователя; - дополнительные поля для типов "mtd" и "mtm": ● uname - строка, учетная запись sip зарегистрированная в M.Talker; ● status - целое, статус пользователя в M.Talker; ● device - строка, идентификатор устройства пользователя. Общий формат документа для отдельного абонента: { "abonent_id": id, "used_uac_type": [ "uac1", "uac2", ... ], "sip": [ { sess1 }, ... ], "mtm": [ { sess1 }, ... ], "mtd": [ { sess1 }, ... ], "сс": [ { sess1 }, ... ], "calls": [ { call1 }, ... ]}
