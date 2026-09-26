---
id: vpbx-api-213-vopros-dlya-ocenki-kachestva-raboty-oper
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.7.4"
pdf_section: "4.7.4"
title: "Вопрос для оценки качества работы операторов по обработке вызовов"
pdf_heading: "4.7.4 Вопрос для оценки качества работы операторов по обработке вызовов"
pages: "299-300"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 299-300"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"299-300","global_pages":"299-300"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 789
status: extracted
ai-generated: true
---
# 4.7.4. Вопрос для оценки качества работы операторов по обработке вызовов

> Трассировка: PDF §4.7.4 · сквозные стр. 299-300 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.299-300.

POST /vpbx/quality/control/question/ Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | question_id | json |  | ID вопроса |

Пример запроса: POST https://app.mango-office.ru/vpbx/quality/control/question/ vpbx_api_key = 1234567890qwerty, sign = 1234567890qwerty, json = { "question_id":"3092" } В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | 2 |  |  |  |
| result |  |  |  | Результат выполнения запроса;<br>● 1000 - удачное выполнение;<br>● 3100 - переданы неверные параметры команды;<br>● 31хх - неверные параметры;<br>● 3300 - объект не существует;<br>● 5xxx – ошибка сервера |
| Question |  |  |  |  |
|  | id | integer |  | ID вопроса |
|  | qual_ctrl_fo<br>rm_id | integer |  | Ссылка на анкету |
|  | qual_ctrl_fo | string |  | Название анкеты. Уникально в рамках продукта |

| № | Параметры |  | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- | --- |
|  |  | rm_name |  |  |  |
|  |  | block_name | string |  | Название блока вопросов |
|  |  | block_order | integer |  | Порядковый номер блока вопросов |
|  |  | name | string |  | Наименование вопроса, по которому контролёр<br>выставляет оценку |
|  |  | order | integer |  | Порядковый номер вопроса в блоке |
|  |  | required | integer |  | Вопрос обязателен к оценке? |
|  |  | hint | string |  | Подсказка к вопросу |

Пример ответа: { "result": 1000, "question": { "id": 3092, "qual_ctrl_form_id": 357, "qual_ctrl_form_name": "Базовая оценка сотрудника", "block_name": "Установление контакта", "block_order": 0, "name": "Приветствие", "order": 0, "required": 1, "hint": null }}
