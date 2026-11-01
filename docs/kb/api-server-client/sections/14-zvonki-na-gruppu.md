---
id: api-server-client-14-zvonki-na-gruppu
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
section: "2.7"
pdf_section: "2.7"
title: "Звонки на группу"
pdf_heading: "2.7 Звонки на группу"
pages: "8"
source: kb/sources/api-server-client/Api_server_client.pdf
source_part: "1"
source_pages: "ч.1: 8"
source_refs: '[{"source_pdf":"kb/sources/api-server-client/Api_server_client.pdf","part":1,"pages":"8","global_pages":"8"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 182
images: 0
status: extracted
ai-generated: true
---
## 2.7. Звонки на группу

> Трассировка: PDF §2.7 · сквозные стр. 8 · источники: ч.1 `kb/sources/api-server-client/Api_server_client.pdf` с.8.

1) происходит звонок на группу в ВАТС; 2) один из сотрудников группы поднял трубку; 3) остальные сотрудники получат событие телефонии (/call) с состоянием DISONNECTED и признаком is_group_disconnect=true Получение события DISONNECTED c признаком is_group_disconnect=true означает, что звонок сотрудника был завершен по причине ответа на звонок другим сотрудником группы и не обрабатывать такой DISCONNECT, например, как статистику или пропущенный вызов.
