---
id: vpbx-api-20-o-parametre-sign
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "2.4.3"
pdf_section: "2.4.3"
title: "О параметре \"sign\""
pdf_heading: "2.4.3 О параметре \"sign\""
pages: "14"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 14"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"14","global_pages":"14"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 235
status: extracted
ai-generated: true
---
# 2.4.3. О параметре "sign"

> Трассировка: PDF §2.4.3 · сквозные стр. 14 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.14.

Данные, которыми обмениваются системы, как правило, будут передаваться в теле POST- запроса. В этом случае, в тело запроса включаются обязательные параметры json, vpbx_api_key и sign. Параметр vpbx_api_key заполняется уникальным кодом продукта ВАТС. Значение sign рассчитывается следующим образом: sign = sha256(vpbx_api_key + json + vpbx_api_salt) Важно! Подписываются все запросы — как от внешней системы, так и от API ВАТС.
