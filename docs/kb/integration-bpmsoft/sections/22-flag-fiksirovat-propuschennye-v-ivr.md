---
id: integration-bpmsoft-22-flag-fiksirovat-propuschennye-v-ivr
doc_code: INTBPM
doc_title: "Интеграция Виртуальной АТС и BPMSoft. Руководство по интеграции"
doc_version: "22.06.2026"
section: "0"
pdf_section: "2.1"
title: "Флаг “Фиксировать пропущенные в IVR”"
pdf_heading: "Флаг “Фиксировать пропущенные в IVR”"
pages: "25-26"
source: kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf
source_part: "1"
source_pages: "ч.1: 25-26"
source_refs: '[{"source_pdf":"kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf","part":1,"pages":"25-26","global_pages":"25-26"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 455
status: extracted
ai-generated: true
---
# Флаг “Фиксировать пропущенные в IVR”

> Трассировка: PDF §2.1 · сквозные стр. 25-26 · источники: ч.1 `kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf` с.25-26.

Если включен флаг “Фиксировать пропущенные в IVR”, то каждый звонок, пришедший в IVR и НЕ распределенный на сотрудника ВАТС и пропущенный, будет зафиксирован в BPMSoft, при этом ответственным за него будет указан выбранный в данной настройке сотрудник. Если флаг выключен, то звонок, пришедший в IVR, не распределенный на группу и пропущенный не фиксируется в BPMSoft. Чтобы назначить ответственного при пропущенных в IVR, в окне “Основные настройки интеграции” следует: 1) включить флаг “Фиксировать пропущенные в IVR”; 2) выбрать ответственного сотрудника; Важно! Вы можете указать ответственным только тех сотрудников, у которых есть внутренний номер Виртуальной АТС, связанный с вашим аккаунтом BPMSoft. 3) нажать на кнопку “Сохранить”:

![Изображение, стр. 25](../images/22-flag-fiksirovat-propuschennye-v-ivr-1.png)

Руководство по интеграции АТС MANGO OFFICE и BPMSoft | Версия от 22.06.2026
