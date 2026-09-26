---
id: vpbx-api-240-otpravka-soobscheniya
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "4.10.3.2"
pdf_section: "4.10.3.2"
title: "Отправка сообщения"
pdf_heading: "4.10.3.2 Отправка сообщения"
pages: "323-324"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 323-324"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"323-324","global_pages":"323-324"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 483
status: extracted
ai-generated: true
---
# 4.10.3.2. Отправка сообщения

> Трассировка: PDF §4.10.3.2 · сквозные стр. 323-324 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.323-324.

В данном разделе описано событие "Отправка сообщения", отправляемое Контакт-центром MANGO OFFICE в ваше внешнее приложение. Примечание. Этот метод так же используется автоответами и ответами от чат-бота. Параметры события:

| № | Параметры с уровнями вложенности |  |  |  | Тип | Описание |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |  |  |
| 1 | data[] |  |  |  | Массив | Массив истории сообщений |
|  |  | message |  |  | Массив | Массив данных сообщения |
|  |  |  | serverMessageId |  | Строка | Id сообщения |
|  |  |  | type |  | Строка | Тип сообщения |
|  |  |  | time |  | Число | Временная метка |
|  |  |  | payload |  | Объект | Объект сообщения |

|  |  |  |  | body | Строка | Содержимое сообщения |
| --- | --- | --- | --- | --- | --- | --- |

Пример события: { "point_id": 10006434, "path": "/events/md", "data": { "message": { "serverMessageId": "435594321659769152", "type": "text", "time": 1685540319002, "payload": { "body": "message was sent via API Sender" } }, "type": "sendMessage" }}
