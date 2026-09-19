---
id: vpbx-api-16-rabota-s-uslugami-virtualnoy-ats
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "2.3"
pdf_section: "2.3"
title: "Работа с услугами Виртуальной АТС"
pdf_heading: "2.3 Работа с услугами Виртуальной АТС"
pages: "13"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 13"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"13","global_pages":"13"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 252
status: extracted
ai-generated: true
---
# 2.3. Работа с услугами Виртуальной АТС

> Трассировка: PDF §2.3 · сквозные стр. 13 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.13.

API предоставляет внешней системе доступ к подключению услуг. Для этого в личном кабинете выберите «Интеграции → API коннектор», в открывшемся разделе нажмите кнопку «Подключить API коннектор», чтобы активировать опцию:

![Изображение, стр. 13](../images/16-rabota-s-uslugami-virtualnoy-ats-1.jpeg)

Рисунок 1 В случае если этого не сделать, а в методе выполняются манипуляции с услугами, то возвращается код ответа: { "result":5201 }
