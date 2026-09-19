---
id: vpbx-api-243-opoveschenie-o-tom-chto-obraschenie-zakr
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.10.3.5"
pdf_section: "4.10.3.5"
title: "Оповещение о том, что обращение закрыто и нужно оценить работу оператора"
pdf_heading: "4.10.3.5 Оповещение о том, что обращение закрыто и нужно оценить работу оператора"
pages: "324-325"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 324-325"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"324-325","global_pages":"324-325"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 598
status: extracted
ai-generated: true
---
# 4.10.3.5. Оповещение о том, что обращение закрыто и нужно оценить работу оператора

> Трассировка: PDF §4.10.3.5 · сквозные стр. 324-325 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.324-325.

В данном разделе описано событие, отправляемое Контакт-центром MANGO OFFICE в ваше внешнее приложение. Параметры:

| № | Параметры с уровнями<br>вложенности |  |  | Тип | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 |  |  |
| 1 | userId |  |  | Объект | Id пользователя |
| 2 | rule |  |  | Объект | Объект правила для оценки работы оператора |
| 2.1 |  | id |  | Число | Id правила |
| 2.2 |  | name |  | Строка | Строковое наименование правила |
| 2.3 |  | byeMessage |  | Строка | Прощальное сообщение, которое показывается после<br>ответов на все вопросы (если не указано, то значение<br>будет пустой строкой) |
| 2.4 |  | questions |  | Массив | Список вопросов для оценки работы оператора |
|  |  |  | id | Число | Id вопроса |
|  |  |  | text | Строка | Текст вопроса |
| 3 | Type |  |  |  | Тип сообщения:<br>- rateQuality: оценка качества;<br>- sendMessage: отправка сообщения либо файла. |

Пример события: { "point_id": 10006434, "path": "/events/md", "data": { "userId":"9216hhm6Q27Oz1bHZDOD9", "rule": { "id": 885, "name": "правило сотрудника 1", "byeMessage": "", "questions": [ { "id": 100500, "text": "Вопрос?" } ] }, "type":"rateQuality" } }
