---
id: integration-bitrix24-30-avtomaticheski-sozdavat-lid-i-delo-pri-v
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "2.3"
title: "Автоматически создавать лид и дело при входящих звонках"
pdf_heading: "Автоматически создавать лид и дело при входящих звонках"
pages: "30-32"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 30-32"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"30-32","global_pages":"30-32"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 648
status: extracted
ai-generated: true
---
# Автоматически создавать лид и дело при входящих звонках

> Трассировка: PDF §2.3 · сквозные стр. 30-32 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.30-32.

Откройте форму настройки приложения интеграции. В блоке "Входящие звонки" вы увидите флаг "Автоматически создавать лид и дело при входящих звонках". По умолчанию настройка включена.

![Изображение, стр. 30](../images/30-avtomaticheski-sozdavat-lid-i-delo-pri-v-1.png)

Если флаг включен, при входящем звонке c номера, ранее не сохраненного в Битрикс24, будет автоматически создан новый лид:

![Изображение, стр. 30](../images/30-avtomaticheski-sozdavat-lid-i-delo-pri-v-2.png)

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026 При этом, в карточке звонка в Битрикс24 НЕ будет предложено создать лид (только добавить комментарий):

![Изображение, стр. 31](../images/30-avtomaticheski-sozdavat-lid-i-delo-pri-v-3.png)

Если флаг выключен, то при входящем звонке с номера, ранее не сохраненного в Битрикс24, НЕ будет автоматически создан новый лид и в карточке звонка в Битрикс24 будет предложено создать лид:

![Изображение, стр. 31](../images/30-avtomaticheski-sozdavat-lid-i-delo-pri-v-4.png)

Обратите внимание, что если номер звонящего внесен в Битрикс24 в список исключений (CRM - Настройки - Другое - Список исключений), то лид при звонке с этого номера не будет создан. Подробнее… Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
