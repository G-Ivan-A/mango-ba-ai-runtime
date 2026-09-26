---
id: integration-bpmsoft-94-kak-proverit-vklyuchena-li-nastroyka-nas
doc_code: INTBPM
doc_title: "Интеграция Виртуальной АТС и BPMSoft. Руководство по интеграции"
doc_version: "22.06.2026"
section: "0"
pdf_section: "2.6"
title: "Как проверить, включена ли настройка ”Настройки действий в зависимости от роли”"
pdf_heading: "Как проверить, включена ли настройка ”Настройки действий в зависимости от роли”"
pages: "70-71"
source: kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf
source_part: "1"
source_pages: "ч.1: 70-71"
source_refs: '[{"source_pdf":"kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf","part":1,"pages":"70-71","global_pages":"70-71"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 575
status: extracted
ai-generated: true
---
# Как проверить, включена ли настройка ”Настройки действий в зависимости от роли”

> Трассировка: PDF §2.6 · сквозные стр. 70-71 · источники: ч.1 `kb/sources/integration-bpmsoft/Mango_office_integration_BPMSoft.pdf` с.70-71.

от роли” Для этого, в вашей BPMSoft следует:

![Изображение, стр. 70](../images/94-kak-proverit-vklyuchena-li-nastroyka-nas-1.png)

1) нажмите на кнопку и выберите пункт “Открыть дизайнер системы”:

![Изображение, стр. 70](../images/94-kak-proverit-vklyuchena-li-nastroyka-nas-2.png)

2) нажмите на ссылку “Справочники” в блоке “Настройка системы”:

![Изображение, стр. 70](../images/94-kak-proverit-vklyuchena-li-nastroyka-nas-3.png)

3) нажмите на строку ” Настройки действий в зависимости от роли (MANGO OFFICE)“. Будут открыты дополнительные поля:

![Изображение, стр. 70](../images/94-kak-proverit-vklyuchena-li-nastroyka-nas-4.png)

Руководство по интеграции АТС MANGO OFFICE и BPMSoft | Версия от 22.06.2026 4. посмотрите, указано ли значение “Нет” в первой строке таблицы (столбец “Конечное действие при срабатывании”). Настройка “Настройки действий в зависимости от роли (MANGO OFFICE)” включена, если в первой строке таблицы, в столбце “Конечное действие при срабатывании” указано значение “Нет”. Примечание. Если настройка отключена, то правила обработки звонков будут применяться не полностью.

![Изображение, стр. 71](../images/94-kak-proverit-vklyuchena-li-nastroyka-nas-5.png)
