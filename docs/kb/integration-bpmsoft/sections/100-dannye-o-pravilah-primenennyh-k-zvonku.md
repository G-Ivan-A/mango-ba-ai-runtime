---
id: integration-bpmsoft-100-dannye-o-pravilah-primenennyh-k-zvonku
doc_code: INTBPM
doc_title: "Интеграция Виртуальной АТС и BPMSoft. Руководство по интеграции"
doc_version: "22.06.2026"
section: "0"
pdf_section: "2.7"
title: "Данные о правилах, применённых к звонку"
pdf_heading: "Данные о правилах, применённых к звонку"
pages: "73"
source: kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf
source_part: "1"
source_pages: "ч.1: 73"
source_refs: '[{"source_pdf":"kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf","part":1,"pages":"73","global_pages":"73"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 400
status: extracted
ai-generated: true
---
# Данные о правилах, применённых к звонку

> Трассировка: PDF §2.7 · сквозные стр. 73 · источники: ч.1 `kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf` с.73.

Отчет “Действия звонка” содержит список правил, примененных к звонку (одна строка=одно правило), название сущностей, созданных в BPMSoft и переходов между правилами. Столбцы отчета:

| Название<br>столбца | Пояснение |
| --- | --- |
| Порядок | Порядковый номер правила в таблице настройки |
| Направление<br>звонка | Направление звонка, к которому применено правило |
| Функциональная<br>роль | Роль (группа) сотрудников, обработавших звонок |
| Условие | Условие, указанное в правиле, примененном к звонку |
| Сущность | Сущность, над которой выполнено действие |
| Сущность 2 | Сущность, связанная с предыдущей сущностью |
| Действие | Действие, выполненное приложением интеграции в<br>BPMSoft |
| Значение | Номер правила, к которому совершен переход, либо<br>логическое выражение |
