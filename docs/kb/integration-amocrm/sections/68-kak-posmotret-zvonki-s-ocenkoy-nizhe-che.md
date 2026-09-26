---
id: integration-amocrm-68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che
doc_code: INTAMO
doc_title: "Интеграция Виртуальной АТС и amoCRM. Инструкция по настройке"
doc_version: "25.08.2025"
section: "0"
pdf_section: "12"
title: "Как посмотреть звонки с оценкой ниже, чем максимальный порог"
pdf_heading: "Как посмотреть звонки с оценкой ниже, чем максимальный порог"
pages: "119-122"
source: kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf
source_part: "1"
source_pages: "ч.1: 119-122"
source_refs: '[{"source_pdf":"kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf","part":1,"pages":"119-122","global_pages":"119-122"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 888
status: extracted
ai-generated: true
---
# Как посмотреть звонки с оценкой ниже, чем максимальный порог

> Трассировка: PDF §12 · сквозные стр. 119-122 · источники: ч.1 `kb/sources/integration_amocrm/Mango_office_integration_amoCRM.pdf` с.119-122.

Вы можете отфильтровать данные о звонках с оценкой качества, ниже чем установленный вами порог качества, при помощи стандартных инструментов amoCRM. Для этого, в amoCRM необходимо: 1. перейдите в раздел “Аналитика”, затем выберите пункт “Список событий” 2. нажмите на поле “Фильтр”;

![Изображение, стр. 119](../images/68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che-1.png)

3. в поле “Типы событий”. Будет открыто дополнительное поле; 4. введите слово “Тег” в поле “Поиск”; Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

![Изображение, стр. 120](../images/68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che-2.png)

5. установите галочку в полях “Теги добавлены” и “Теги убраны” и нажмите кнопку “Ок”;

![Изображение, стр. 120](../images/68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che-3.png)

6. в поле “Значение до” укажите значение “Оценка минимальная оценка звонка, выше которой звонки вас не интересуют”. Например, укажите значение “Оценка 1”; 7. нажмите кнопку “Применить”;

![Изображение, стр. 120](../images/68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che-4.png)

8. будут отфильтрованы данные о всех звонках, оценка которых меньше либо равна указанного вами порогу оценки качества. Применительно к примеру, будут отфильтрованы все звонки с оценкой качества 1 или ниже. Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025

![Изображение, стр. 121](../images/68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che-5.jpeg)

Чтобы прослушать запись разговора, которому поставлена та или оценка, нажмите на поле “Контакт” в нужной вам строке с данными звонка. Будет открыта карточка контакта, в которой вы можете прослушать запись разговора.

![Изображение, стр. 121](../images/68-kak-posmotret-zvonki-s-ocenkoy-nizhe-che-6.jpeg)

Интеграция Виртуальной АТС MANGO OFFICE и amoCRM | Версия от 25.08.2025
