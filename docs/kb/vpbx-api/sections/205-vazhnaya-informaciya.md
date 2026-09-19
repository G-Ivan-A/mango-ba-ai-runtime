---
id: vpbx-api-205-vazhnaya-informaciya
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "4.6.18"
title: "Важная информация"
pdf_heading: "Важная информация"
pages: "287"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 287"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"287","global_pages":"287"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 298
status: extracted
ai-generated: true
---
# Важная информация

> Трассировка: PDF §4.6.18 · сквозные стр. 287 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.287.

Этот метод позволяет получить информацию о завершенных заданиях кампании исходящего обзвона. Он возвращает звонковые задания, которые были завершены и не имеют признака соединения с оператором. Для применения данного метода понадобится следующее: - значение поля "status" у кампании ИО должно быть 4, то есть кампания должна быть завершена; - значение поля "task_status_reason" у кампании ИО должно быть больше 1, то есть разговор состоялся; - кампания ИО должна быть завершена в промежуток времени, указанный в запросе. При этом, в запросе разница между началом и концом диапазона не должна быть больше 4 часов.
