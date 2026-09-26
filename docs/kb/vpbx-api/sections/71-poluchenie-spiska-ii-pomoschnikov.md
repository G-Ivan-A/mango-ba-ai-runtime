---
id: vpbx-api-71-poluchenie-spiska-ii-pomoschnikov
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.5.8"
pdf_section: "3.5.8"
title: "Получение списка ИИ помощников"
pdf_heading: "3.5.8 Получение списка ИИ помощников"
pages: "96-99"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 96-99"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"96-99","global_pages":"96-99"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1803
status: extracted
ai-generated: true
---
# 3.5.8. Получение списка ИИ помощников

> Трассировка: PDF §3.5.8 · сквозные стр. 96-99 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.96-99.

POST /s2t/queries/ai_agents Метод предназначен для получения списка ИИ помощников, настроенных в сервисе Речевой аналитики. Параметры запроса отсутствуют. Заголовки запроса:

| № | Параметры | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- |
| 1 | X-Product-Id | string | Да | Идентификатор продукта |

Пример запроса: POST /s2t/queries/ai_agents В результате обработки запроса формируются и передаются JSON-данные, содержащие список ИИ помощников. Эти JSON-данные содержат следующие параметры:

| № | Параметры с уровнями<br>вложенности |  | Тип | Обязательный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | result |  | integer | Да | Код результата. |
| 2 | data |  | array | Да | Массив ИИ<br>помощников. |
| 2.1 |  | id | integer | Да | Идентификатор<br>помощника. |
| 2.2 |  | name | string | Да | Наименование<br>помощника. |
| 2.3 |  | status | string | Да | Статус<br>помощника<br>(active,<br>disabled). |
| 2.4 |  | created_at | string | Да | Дата и время<br>создания<br>помощника в<br>формате ISO<br>8601. |
| 2.5 |  | updated_at | string | Да | Дата и время<br>последнего<br>изменения<br>помощника в<br>формате ISO<br>8601. |
| 2.6 |  | output_fields | array | Да | Массив полей, в<br>которые будут<br>записаны<br>результаты<br>работы ИИ<br>помощника. |
| 2.6.1 |  | id | integer | Да | Идентификатор<br>поля. |
| 2.6.2 |  | label | string | Да | Наименование<br>поля. |
| 2.6.3 |  | description | string | Нет | Описание поля. |
| 2.6.4 |  | created_at | string | Да | Дата и время<br>создания поля<br>в формате ISO<br>8601. |
| 2.6.5 |  | updated_at | string | Да | Дата и время<br>последнего<br>изменения<br>поля в формате<br>ISO 8601. |

Пример ответа:

|  | { |  |
| --- | --- | --- |
|  | "result": 1000, |  |
|  | "data": [ |  |
|  | { |  |
|  | "id": 1, |  |
|  | "name": "Анализ продаж", |  |
|  | "status": "active", |  |
|  | "model": "yandex-gpt-5.1-pro", |  |
|  | "created_at": "2026-03-10T14:22:11Z", |  |
|  | "updated_at": "2026-03-15T09:12:00Z", |  |
|  | "output_fields": [ |  |
|  | { |  |
|  | "id": 1, |  |
|  | "key": "operator_recommendation", |  |
|  | "label": "Рекомендация оператору", |  |
|  | "type": "string", |  |
|  | "description": "Сформированные рекомендации не более 300 слов" |  |
|  | }, |  |
|  | { |  |
|  | "id": 2, |  |
|  | "key": "competitors_mentioned", |  |
|  | "label": "Упомянуты конкуренты", |  |
|  | "type": "boolean", |  |
|  | "description": "Правда, если клиент сам назвал конкурентов" |  |
|  | } |  |
|  | ] |  |
|  | }, |  |
|  | { |  |
|  | "id": 2, |  |
|  | "name": "Цель разговора", |  |
|  | "status": "active", |  |
|  | "model": "yandex-gpt-5.1-pro", |  |
|  | "created_at": "2026-03-10T14:22:11Z", |  |
|  | "updated_at": "2026-03-15T09:12:00Z", |  |
|  | "output_fields": [ |  |
|  | { |  |
|  | "id": 3, |  |
|  | "key": "conversation_goal", |  |
|  | "label": "Цель разговора", |  |
|  | "type": "string", |  |
|  | "description": "" |  |

|  | } |  |
| --- | --- | --- |
|  | ] |  |
|  | }, |  |
|  | { |  |
|  | "id": 3, |  |
|  | "name": "Резюме разговора", |  |
|  | "status": "active", |  |
|  | "model": "yandex-gpt-5.1-pro", |  |
|  | "created_at": "2026-03-10T14:22:11Z", |  |
|  | "updated_at": "2026-03-15T09:12:00Z", |  |
|  | "output_fields": [ |  |
|  | { |  |
|  | "id": 4, |  |
|  | "key": "call_goal", |  |
|  | "label": "Цель разговора", |  |
|  | "type": "string", |  |
|  | "description": "" |  |
|  | }, |  |
|  | { |  |
|  | "id": 5, |  |
|  | "key": "client_request", |  |
|  | "label": "Запрос клиента", |  |
|  | "type": "string", |  |
|  | "description": "" |  |
|  | }, |  |
|  | { |  |
|  | "id": 6, |  |
|  | "key": "call_result", |  |
|  | "label": "Итоги встречи", |  |
|  | "type": "string", |  |
|  | "description": "" |  |
|  | } |  |
|  | ] |  |
|  | } |  |
|  | ] |  |
|  | } |  |
