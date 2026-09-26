---
id: cov-robot-fil-52-integraciya-s-yclients
doc_code: ROBOTFIL
doc_title: "Модуль ЦОВ «Робот Фил 2,0». Руководство пользователя"
doc_version: "1.26.28"
section: "6.6"
pdf_section: "6.6"
title: "Интеграция с YCLIENTS"
pdf_heading: "6.6. Интеграция с YCLIENTS"
pages: "153-155"
source: kb/sources/cov-robot-fil/Модуль ЦОВ Робот Фил 2,0_manual_v7.26.28.pdf
source_part: "1"
source_pages: "ч.1: 153-155"
source_refs: '[{"source_pdf":"kb/sources/cov-robot-fil/Модуль ЦОВ Робот Фил 2,0_manual_v7.26.28.pdf","part":1,"pages":"153-155","global_pages":"153-155"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 701
status: extracted
ai-generated: true
---
# 6.6. Интеграция с YCLIENTS

> Трассировка: PDF §6.6 · сквозные стр. 153-155 · источники: ч.1 `kb/sources/cov-robot-fil/Модуль ЦОВ Робот Фил 2,0_manual_v7.26.28.pdf` с.153-155.

Администратор, отвечающий за настройку роботов, может подключить и настроить взаимодействие робота с YCLIENTS. После подключения в момент звонка робот может выполнять в системе YCLIENTS следующие функции:  Записать клиента в расписание в удобное для него время;  Принять звонок и произвести корректировку записи клиента;  Перевести звонок в чат-бот WhatsApp или Telegram. Для настройки интеграции следует зайти в раздел Настройки интеграций левого бокового меню модуля, выбрать «YCLIENTS» и нажать кнопку Подключить.

![Изображение, стр. 153](../images/52-integraciya-s-yclients-1.png)

![Изображение, стр. 153](../images/52-integraciya-s-yclients-2.png)

После подключения интеграцию необходимо настроить.

![Изображение, стр. 154](../images/52-integraciya-s-yclients-3.png)

![Изображение, стр. 154](../images/52-integraciya-s-yclients-4.png)

![Изображение, стр. 154](../images/52-integraciya-s-yclients-5.png)

После успешного подключения в блоке «HTTP-запрос» конструктора скриптов для роботов, а также в блоке «Интеграция» конструктора скриптов для робота-администратора будет доступен способ интеграции «YCLIENTS». ПРИМЕР. Администратор, отвечающий за настройку голосового робота, может использовать ключи авторизации в http-запросе, чтобы не терять время на повторный ввод этих данных в каждом http-запросе:

![Изображение, стр. 155](../images/52-integraciya-s-yclients-6.png)

![Изображение, стр. 155](../images/52-integraciya-s-yclients-7.png)

![Изображение, стр. 155](../images/52-integraciya-s-yclients-8.png)
