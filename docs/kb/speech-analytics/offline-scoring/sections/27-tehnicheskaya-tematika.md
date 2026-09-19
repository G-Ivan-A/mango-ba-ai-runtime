---
id: offline-scoring-27-tehnicheskaya-tematika
doc_code: SA-SCORE
doc_title: "Руководство пользователя. Речевая аналитика. Офлайн скоринг"
doc_version: "1.26.15"
section: "3.6"
pdf_section: "3.6"
title: "Техническая тематика"
pdf_heading: "3.6. Техническая тематика"
pages: "53"
source: kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_Skoring_Rukovodstvo-polzovatelya_v.1.26.15.pdf
source_part: "1"
source_pages: "ч.1: 53"
source_refs: '[{"source_pdf":"kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_Skoring_Rukovodstvo-polzovatelya_v.1.26.15.pdf","part":1,"pages":"53","global_pages":"53"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 346
status: extracted
ai-generated: true
---
# 3.6. Техническая тематика

> Трассировка: PDF §3.6 · сквозные стр. 53 · источники: ч.1 `kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_Skoring_Rukovodstvo-polzovatelya_v.1.26.15.pdf` с.53.

Техническая тематика необходима для корректной диаризации – автоматического разделения системой одноканальных записей, загруженных по api, ftp и вручную, на два канала. Техническая тематика содержится в списке предустановленных тематик. В ней заданы слова- признаки, которые произносит Сотрудник, и по которым система впоследствии разделит каналы. Пользователь может внести изменения в настройки тематики в соответствии со своими индивидуальными словами-признаками. Если в настройках тематик включен переключатель «перезаписывание тематик», то при изменении списка слов-признаков перетегирование одноканальных записей не происходит.
