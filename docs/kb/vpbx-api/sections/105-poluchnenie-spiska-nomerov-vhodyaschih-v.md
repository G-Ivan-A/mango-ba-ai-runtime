---
id: vpbx-api-105-poluchnenie-spiska-nomerov-vhodyaschih-v
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.8.2.2"
pdf_section: "3.8.2.2"
title: "Получнение списка номеров, входящих в ч/б списки ВАТС"
pdf_heading: "3.8.2.2 Получнение списка номеров, входящих в ч/б списки ВАТС"
pages: "145-147"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 145-147"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"145-147","global_pages":"145-147"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 993
status: extracted
ai-generated: true
---
# 3.8.2.2. Получнение списка номеров, входящих в ч/б списки ВАТС

> Трассировка: PDF §3.8.2.2 · сквозные стр. 145-147 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.145-147.

POST /vpbx/bwlists/numbers/ Метод позволяет получить текущий список номеров, уже включенных в "черный" либо "белый" список Виртуальной АТС. Параметры запроса: пустой json. Примечание. Согласно модели взаимодействия, в POST-запросах отправляются обязательные поля vpbx_api_key и sign. Пример запроса: POST https://app.mango-office.ru/vpbx/bwlists/numbers/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры с уровнями<br>вложенности |  |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |  |  |  |
| 1 | result |  |  |  |  |  | Код ошибки:<br>● 1000 - удачное выполнение;<br>● 3300 - объект не существует;<br>● 5XXX – ошибка сервера; |
| 2 | data |  |  |  |  |  |  |
|  |  | active |  |  |  |  | Активный список, см. Получить<br>текущий режим ч/б списка; |
|  |  | black |  |  |  |  | Блок с настройками «черного» списка |
|  |  | white |  |  |  |  | Блок с настройками «белого» списка |
| Параметры, входящие в блок black и\или в блок white |  |  |  |  |  |  |  |
|  |  |  | allow_unknown<br>_number |  | Булевое |  | true/false, вызовы с неопределившихся<br>номеров разрешать/нет |
|  |  |  | numbers |  |  |  | Список номеров |
|  |  |  |  | number_id |  |  | ID номера |
|  |  |  |  | number |  |  | Номер. Может быть указана маска.<br>"*" - означает произвольную<br>последовательность цифр/символов,<br>"#" - означает одну произвольную<br>цифру/символ.<br>Кроме того, могут быть заданы<br>диапазоны номеров, используя<br>тире ("-") в качестве разделителя |
|  |  |  |  | comment |  |  | Комментарий, до 255 символов |
|  |  |  |  | number_t<br>ype |  |  | Тип номера, "tel", "sip" |

Пример ответа: { "result": 1000, "data": { "active": "black", "black": { "allow_unknown_number": true, "numbers": [ { "number_id": 10088581, "number": "1111", "comment": "", "number_type": "tel" }, { "number_id": 10088582, "number: "sdsds@sdsd.ru", "comment": "", "number_type": "sip" } ] }, "white": { "allow_unknown_number ": false, "numbers": [] } } }
