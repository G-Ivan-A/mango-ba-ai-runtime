---
id: vpbx-api-15-api-kc
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "2.1.2"
pdf_section: "2.1.2"
title: "API КЦ"
pdf_heading: "2.1.2 API КЦ"
pages: "13"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 13"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"13","global_pages":"13"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 271
status: extracted
ai-generated: true
---
# 2.1.2. API КЦ

> Трассировка: PDF §2.1.2 · сквозные стр. 13 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.13.

Модель взаимодействия API КЦ с внешними системами практически полностью повторяет модель взаимодействия API ВАТС с внешними системами. Ниже приведено описание этих различий: 1) в качестве базового адреса API КЦ в сети Интернет используется https://app.mango- office.ru/cc/. Пример запроса к API КЦ: https://app.mango-office.ru/cc/set_abonent_status где /set_abonent_status - сервис. 2) основные коды результатов обработки запросов API КЦ находятся в диапазоне 12хх. (весь список кодов результатов см. в "Список кодов результатов").
