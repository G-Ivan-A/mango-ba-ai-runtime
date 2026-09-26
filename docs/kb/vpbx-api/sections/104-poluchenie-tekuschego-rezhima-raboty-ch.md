---
id: vpbx-api-104-poluchenie-tekuschego-rezhima-raboty-ch
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.8.2.1"
pdf_section: "3.8.2.1"
title: "Получение текущего режима работы ч/б списка"
pdf_heading: "3.8.2.1 Получение текущего режима работы ч/б списка"
pages: "144-145"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 144-145"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"144-145","global_pages":"144-145"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 506
status: extracted
ai-generated: true
---
# 3.8.2.1. Получение текущего режима работы ч/б списка

> Трассировка: PDF §3.8.2.1 · сквозные стр. 144-145 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.144-145.

POST /vpbx/bwlists/state/ В Виртуальной АТС можно включить или выключить работу ч/б списка. Этот метод позволяет получить статус (включен/выключен) нужного вам ч/б списка Виртуальной АТС. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/bwlists/state/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки, формируются и передаются JSON-данные, содержащие код ошибки:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | Result |  | Да | Код результата:<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31XX - неверные параметры;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера. |
|  | active |  |  | Текущий режим ч/б списка Виртуальной АТС.<br>Возможные значения:<br>- black – "черный" список;<br>- white - «белый» список. |

Пример ответа: { "result": 1000, "active": "black" }
