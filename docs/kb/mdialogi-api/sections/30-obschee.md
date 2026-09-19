---
id: mdialogi-api-30-obschee
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
section: "3.1.1"
pdf_section: "3.1.1"
title: "Общее"
pdf_heading: "3.1.1 Общее"
pages: "27"
source: kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf
source_part: "1"
source_pages: "ч.1: 27"
source_refs: '[{"source_pdf":"kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf","part":1,"pages":"27","global_pages":"27"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 352
status: extracted
ai-generated: true
---
# 3.1.1. Общее

> Трассировка: PDF §3.1.1 · сквозные стр. 27 · источники: ч.1 `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` с.27.

Если к Вашей Виртуальной АТС подключена услуга "WhatsApp Business API (провайдер Edna)", в API Манго Диалоги становится доступна возможность отправлять Клиентам HSM-сообщения через WhatsApp. Примечание. Подробнее о подключении услуги "WhatsApp (провайдер Edna)" вы можете узнать в Справочнике абонента ВАТС. В данном разделе используются следующие термины: HSM - (highly-structured message) шаблонизированное сервисное сообщение, используемое WhatsApp Business API; WA - WhatsApp канал. При помощи данного API, вы можете: - получить список уже созданных HSM-шаблонов; - выдать команду на отправку Клиенту HSM-сообщения; - получить статус отправленного HSM-сообщения. Примечание. Создавать, редактировать и удалять HSM-шаблоны сообщений при помощи данных методов API нельзя.
