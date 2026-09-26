---
id: integration-amocrm-14-dopolnitelnye-nastroyki-integracii-obzor
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "2.2"
pdf_section: "2.2"
title: "Дополнительные настройки интеграции. Обзор"
pdf_heading: "2.2 Дополнительные настройки интеграции. Обзор"
pages: "23-25"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 23-25"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"23-25","global_pages":"23-25"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 793
status: extracted
ai-generated: true
---
# 2.2. Дополнительные настройки интеграции. Обзор

> Трассировка: PDF §2.2 · сквозные стр. 23-25 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.23-25.

В зависимости от ваших задач можно указать дополнительные настройки интеграции. На вкладке “Обработка звонков” настраивается логика обработки звонков – нужно ли автоматически создавать контакт или создавать в “неразобранном”, нужно ли ставить задачи по пропущенным звонкам и т.д.: ![](ITG_amoCRM25112024.assets/image28.png”/> Важно! Если включить настройку “Фиксировать в”НЕРАЗОБРАННОЕ”, то будут сохраняться данные о звонках от новых Клиентов в amoCRM. Кроме того, второй и последующие звонки также будут фиксироваться в категории “НЕРАЗОБРАННОЕ”. Например, если новый Клиент, практически сразу после первого звонка, перезвонил вам для уточнения деталей, то в категории “НЕРАЗОБРАННОЕ” будут зафиксированы два отдельных звонка:

![Изображение, стр. 23](../images/14-dopolnitelnye-nastroyki-integracii-obzor-1.png)

На вкладке “SMS” настраивается работа с SMS – нужно ли использовать SMS-визитку, дать сотрудникам возможность отправлять SMS из карточки контакта и т.д.: Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

![Изображение, стр. 24](../images/14-dopolnitelnye-nastroyki-integracii-obzor-2.png)

На вкладке “Дополнительно” настраивается интеграция с Коллтрекингом MANGO OFFICE (сквозная аналитика), Контакт-центром, Digital-воронкой amoCRM, Речевой аналитикой:

![Изображение, стр. 24](../images/14-dopolnitelnye-nastroyki-integracii-obzor-3.png)

На вкладке “Ограничения” указывается, для каких линий Виртуальной АТС работает интеграция с amoCRM Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

![Изображение, стр. 25](../images/14-dopolnitelnye-nastroyki-integracii-obzor-4.png)
