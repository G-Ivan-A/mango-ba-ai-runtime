---
id: api-server-client-52-sostoyanie-zvonka
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "4.3"
pdf_section: "4.3"
title: "Состояние звонка"
pdf_heading: "4.3 Состояние звонка"
pages: "51-52"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 51-52"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"51-52","global_pages":"51-52"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 391
images: 1
status: extracted
ai-generated: true
---
## 4.3. Состояние звонка

> Трассировка: PDF §4.3 · сквозные стр. 51-52 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.51-52.

Список состояний:

| Код | Описание |
| --- | --- |
| APPEARED | Звонок в состоянии ожидания |
| CONNECTED | Звонок в состоянии разговора |
| ON_HOLD | Звонок на удержании |
| DISCONNECTED | Звонок завершен |

Код Описание

APPEARED Звонок в состоянии ожидания

CONNECTED Звонок в состоянии разговора

ON_HOLD Звонок на удержании

DISCONNECTED Звонок завершен

Диаграмма состояний вызова:

![Снимок экрана / схема, стр. 52](../images/52-sostoyanie-zvonka-1.png)

> **Описание иллюстрации APISC-§4.3-1** (к §4.3 «Состояние звонка», стр. 52; 583×257 px). Снимок экрана / схема.
> Относится к тексту руководства: «…DISCONNECTED Звонок завершен Диаграмма состояний вызова:».
> Текст на изображении (OCR, требует сверки): Connected

Начальное состояние вызова - APPEARED.

Уведомления о вызовах для каждого пользователя можно упорядочить по времени поступления (timestamp).

Конечным состоянием любого вызова является DISCONNECTED.
