---
id: integration-amocrm-20-otvetstvennyy-pri-propuschennyh-zvonkah
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "2.8"
pdf_section: "2.8"
title: "Ответственный при пропущенных звонках в группу"
pdf_heading: "2.8 Ответственный при пропущенных звонках в группу"
pages: "47-48"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 47-48"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"47-48","global_pages":"47-48"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 431
status: extracted
ai-generated: true
---
# 2.8. Ответственный при пропущенных звонках в группу

> Трассировка: PDF §2.8 · сквозные стр. 47-48 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.47-48.

Если этот флаг включен, а также в поле “Действие для нового” выбрано одно из значений “Создать контакт” / “Создать контакт и сделку” / “Фиксировать в”неразобранное”, то при каждом звонке от нового Клиента, распределенном в любую группу ВАТС и пропущенном: - автоматически создается контакт; - автоматически создается сделка (если включен флаг “Создать контакт и сделку”); - в контакте (и сделке) указывается выбранный ответственный сотрудник. Если флаг выключен, то для такого звонка при создании контакта (сделки) - в качестве ответственного указывается первый сотрудник, на которого распределялся вызов. Нажмите кнопку “Сохранить” внизу закладки “Обработка звонков”, чтобы сохранить настройку. Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

![Изображение, стр. 48](../images/20-otvetstvennyy-pri-propuschennyh-zvonkah-1.png)
