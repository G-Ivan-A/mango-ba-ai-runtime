---
id: vats-offline-scoring-37-tehnicheskaya-tematika
doc_code: SA-VATS-SCORE
doc_title: "Руководство пользователя. Речевая аналитика. ВАТС & Офлайн скоринг"
doc_version: "1.26.18"
section: "6.7"
pdf_section: "6.7"
title: "Техническая тематика"
pdf_heading: "6.7 Техническая тематика"
pages: "59"
source: kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_VATS-_-Skoring-1.26.18.pdf
source_part: "1"
source_pages: "ч.1: 59"
source_refs: '[{"source_pdf":"kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_VATS-_-Skoring-1.26.18.pdf","part":1,"pages":"59","global_pages":"59"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 342
status: extracted
ai-generated: true
---
# 6.7. Техническая тематика

> Трассировка: PDF §6.7 · сквозные стр. 59 · источники: ч.1 `kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_VATS-_-Skoring-1.26.18.pdf` с.59.

Техническая тематика необходима для корректной диаризации – автоматического разделения системой одноканальных аудиозаписей, загруженных по api, ftp и вручную, на два канала. Техническая тематика содержится в списке предустановленных тематик. В ней заданы слова- признаки, которые произносит Сотрудник, и по которым система впоследствии разделит каналы. Пользователь может внести изменения в настройки тематики в соответствии со своими индивидуальными словами-признаками. Если в настройках тематик включен переключатель «перезаписывание тематик», то при изменении списка слов-признаков перетегирование одноканальных записей не происходит.
