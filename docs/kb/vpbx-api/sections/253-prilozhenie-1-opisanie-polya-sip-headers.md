---
id: vpbx-api-253-prilozhenie-1-opisanie-polya-sip-headers
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "0"
pdf_section: "—"
title: "Приложение 1 – Описание поля sip-headers"
pdf_heading: "Приложение 1 – Описание поля sip-headers"
pages: "349"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 349"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"349","global_pages":"349"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 620
status: extracted
ai-generated: true
---
# Приложение 1 – Описание поля sip-headers

> Трассировка: PDF §— · сквозные стр. 349 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.349.

Опциональный параметр, содержащий вложенные SIP заголовки и их значения. Принимается как входной параметр некоторыми методами API (при поддержке данного поля указывается в описании метода). При заполнении этих заголовков со стороны внешней системы, ВАТС после прохождения валидации переданных полей заполнит соответствующие заголовки в SIP INVITE переданными значениями. Для каждого метода в API имеется свой набор разрешенных заголовков. При передаче заголовка, который не поддерживается в данном методе либо не прошел валидацию - он будет проигнорирован ВАТС. Для гарантированного прохождения валидации при заполнении каждого параметра значениями нужно руководствоваться рекомендациями соответствующего стандарта RFC. Формальное описание грамматики поля sip_headers:

| sip_headers = { fields }<br>fields = "param":"value"<br>param = "sip_header/sip_header_part" |
| --- |
| sip_header = string token ## Сип заголовок из стандартных<br>заголовков сип<br>sip_header_part = string token ## Изменяемый раздел заголовка<br>из стандартных<br>разделов заголовков сип<br>value = string ## Подставляемое значение |
| string = ALPHA\|DIGIT exclude ";" / "/" / "?" / ":" / "@" / "&" / "=" / "+"<br>/ "$" / "," |

![Изображение, стр. 349](../images/253-prilozhenie-1-opisanie-polya-sip-headers-1.png)

![Изображение, стр. 349](../images/253-prilozhenie-1-opisanie-polya-sip-headers-2.png)

![Изображение, стр. 349](../images/253-prilozhenie-1-opisanie-polya-sip-headers-3.png)

Примеры: "sip_headers": { "From/display-name": "Santa Claus", "Call-Info/answer-after": "0", }
