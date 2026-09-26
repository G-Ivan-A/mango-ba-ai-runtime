---
id: vpbx-api-70-zapros-zapisey-s-rasshifrovkami-zvonkov
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.5.7"
pdf_section: "3.5.7"
title: "Запрос записей с расшифровками звонков"
pdf_heading: "3.5.7 Запрос записей с расшифровками звонков"
pages: "95-96"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 95-96"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"95-96","global_pages":"95-96"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 964
status: extracted
ai-generated: true
---
# 3.5.7. Запрос записей с расшифровками звонков

> Трассировка: PDF §3.5.7 · сквозные стр. 95-96 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.95-96.

POST /s2t/queries/records Описание: Метод предназначен для получения записей звонков с расшифровками Параметры запроса:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | date_from | string | Да | Дата начала |
| 2 | date_to |  | Да | Дата завершения |
| 3 | offset |  | Нет | оффсет |
| 4 | limit |  | Нет | Лимит записи |

Тело запроса должно быть в формате json, например: { "number": "74951112233" }

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |  |
| 1 | result |  |  | integer | Да | Код статуса результата |
| 2 | data |  |  | object | Да | Данные ответа |
| 2.1 |  | communica<br>tion_id |  | string | Да | id Коммуникации |
| 2.2 |  | communica<br>tion_type |  | string | Да | Тип Коммуникации |
| 2.3. |  | info |  | object | Да | Информация о коммуникации |
| 2.3 |  |  | direction | integer | Да | Направление коммуникации |
| 2.3 |  |  | duration | integer | Да | Длительность коммуникации в<br>секундах |
| 2.3 |  |  | time_created | Integer<br>(timestam<br>p) | Да | Время создания коммуникации |
| 2.3 |  |  | from_number |  | Да | Исходящий номер |
| 2.3 |  |  | to_number | string | Да | Входящий номер |
| 3 |  | sentiments |  | object | Да | Данные взаимодействий |
| 3.1 |  |  | client | string | Да | Клиент |
| 3.2 |  |  | operator | string | Да | Оператор |
| 4 |  | has_s2t |  | boolean | Да | Признак наличия расшифровки |
| 5 |  | has_transcr<br>ipt |  | boolean | Да | Имеет суммаризацию |
| 6 |  | has_summa<br>ry |  | boolean | Да | Имеет расшифровку |

Пример ответа: { "result": 1000, "data": [ { "communication_id": "MzAwMTI5NjM3OA==", "communication_type": 1, "info": { "direction": "out", "duration": 25, "time_created": 1756724256, "from_number": "sip:user6@tst-devpg3-minsk94.mangosip.ru", "to_number": "7007374951200532" }, "sentiments": { "client": null, "operator": null }, "has_s2t": false, "has_transcript": false, "has_summary": false } ] } Методы данного раздела работают только если используется Динамический коллтрекинг.
