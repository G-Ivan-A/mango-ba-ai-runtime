---
id: integration-amocrm-42-propuschennye-zvonki
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "5"
pdf_section: "5"
title: "Пропущенные звонки"
pdf_heading: "5 Пропущенные звонки"
pages: "91-92"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 91-92"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"91-92","global_pages":"91-92"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 545
status: extracted
ai-generated: true
---
# 5. Пропущенные звонки

> Трассировка: PDF §5 · сквозные стр. 91-92 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.91-92.

Если сотрудник отсутствовал на рабочем месте и были пропущенные звонки, то вне зависимости, был открыт amoCRM у него или не был открыт, в amoCRM попадет информация о пропущенных звонках. Чтобы увидеть все пропущенные звонки, необходимо открыть область уведомлений amoCRM:

![Изображение, стр. 91](../images/42-propuschennye-zvonki-1.png)

Пропущенные звонки от новых Клиентов (не сохраненных в amoCRM) также отображаются в неразобранном.

![Изображение, стр. 91](../images/42-propuschennye-zvonki-2.png)

Примечания: 1. Это зависит от настроек виджета – звонок также может сохраниться в качестве контакта (если включен флаг “Создавать контакт при звонках с новых номеров”), а также сделки (если пир этом еще включен флаг “Создавать сделку”). 2. Если пропущенный звонок сохранился в неразобранном, то если вы сконвертируете его в сделку, то дата и время звонка будут равны дате и времени конвертации из неразобранного. 3. Звонки, сохраненные в неразобранном не попадут в инструменты аналитики, до тех пор пока не будут сконвертированы в сделки. Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025
