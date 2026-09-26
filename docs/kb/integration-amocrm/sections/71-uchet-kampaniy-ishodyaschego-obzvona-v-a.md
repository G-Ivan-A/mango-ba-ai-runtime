---
id: integration-amocrm-71-uchet-kampaniy-ishodyaschego-obzvona-v-a
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "14.1"
pdf_section: "14.1"
title: "Учет кампаний исходящего обзвона в amoCRM"
pdf_heading: "14.1 Учет кампаний исходящего обзвона в amoCRM"
pages: "124-125"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 124-125"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"124-125","global_pages":"124-125"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 631
status: extracted
ai-generated: true
---
# 14.1. Учет кампаний исходящего обзвона в amoCRM

> Трассировка: PDF §14.1 · сквозные стр. 124-125 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.124-125.

Если Вы подключили Контакт Центр MANGO OFFICE (далее по тексту – КЦ) к Виртуальной АТС, то в рамках интеграции с amoCRM будет доступна дополнительная возможность: учет кампаний исходящего обзвона в amoCRM. То есть, звонки, выполненные в рамках кампаний исходящего обзвона КЦ, обрабатываются (с показом карточки) и фиксируются в amoCRM только при включенной опции “Интеграция с Контакт-центром”.

![Изображение, стр. 124](../images/71-uchet-kampaniy-ishodyaschego-obzvona-v-a-1.png)

Кроме того, если запущена кампания исходящего обзвона из КЦ, то при входящем звонке будет показана информация о контакте из настроек кампании:

![Изображение, стр. 124](../images/71-uchet-kampaniy-ishodyaschego-obzvona-v-a-2.png)

Если контакт создается в amoCRM автоматически (согласно настройкам виджета) или создается из карточки звонка, то в контакте автоматически сохранятся данные:

| Поле в amoCRM | Описание |
| --- | --- |

Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

| ЦОВ: Привлечен кампанией исходящего<br>обзвона | Имя кампании |
| --- | --- |
| ЦОВ: Идентификатор кампании<br>исходящего обзвона | Уникальный идентификатор кампании |
| ЦОВ: Идентификатор Клиента | Уникальный идентификатор кампании из кампании |
