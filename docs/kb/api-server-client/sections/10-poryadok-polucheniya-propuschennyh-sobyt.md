---
id: api-server-client-10-poryadok-polucheniya-propuschennyh-sobyt
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "2.3"
pdf_section: "2.3"
title: "Порядок получения пропущенных событий"
pdf_heading: "2.3 Порядок получения пропущенных событий"
pages: "7"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 7"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"7","global_pages":"7"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 267
images: 0
status: extracted
ai-generated: true
---
## 2.3. Порядок получения пропущенных событий

> Трассировка: PDF §2.3 · сквозные стр. 7 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.7.

1) пользователь не залогинен в websocket-сессии; 2) все события, проходящие через систему, записываются для пользователя как пропущенные; Важно! Речь идет именно о событиях, необработанных ("пропущенных") внешним приложением, а не о статусе "пропущен" того или иного вызова.

3) после успешного создания вебсокет-соединения и выполнения запроса «Начать сессию вебсокета» (/v1/session/register) пользователем:

а) выполнить запрос /v1/session/register циклически, пока Result[code]=0. Если больше пропущенных событий нет, то Result[code]=109;

б) параметр LIMIT можно варьировать. Таймаут на запрос к Сервиса равен 1 минуте; 4) пропущенные события хранятся 2 недели до удаления из истории.
