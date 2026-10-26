---
id: mango-lk-manual-232-postanovka-celey-po-sobytiyam-tekstovye
doc_code: LK
doc_title: "Виртуальная АТС MANGO OFFICE - Справочник абонента"
doc_version: "1.23"
section: "4.5.11.5.2"
pdf_section: "4.5.11.5.2"
title: "Постановка целей по событиям «Текстовые коммуникации» в Яндекс.Метрике"
pdf_heading: "4.5.11.5.2 Постановка целей по событиям «Текстовые коммуникации» в Яндекс.Метрике"
pages: "367-368"
source: kb/sources/mango-lk-manual/LK_manual_v-123.pdf
source_part: "1"
source_pages: "ч.1: 367-368"
source_refs: '[{"source_pdf":"kb/sources/mango-lk-manual/LK_manual_v-123.pdf","part":1,"pages":"367-368","global_pages":"367-368"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1149
status: extracted
ai-generated: true
---
# 4.5.11.5.2. Постановка целей по событиям «Текстовые коммуникации» в Яндекс.Метрике

> Трассировка: PDF §4.5.11.5.2 · сквозные стр. 367-368 · источники: ч.1 `kb/sources/mango-lk-manual/LK_manual_v-123.pdf` с.367-368.

в Яндекс.Метрике 1. Зарегистрируйтесь в Яндекс.Метрике и установите счетчик на сайт, на котором размещен виджет «Текстовые коммуникации» , по инструкции 2. Для анализа событий Мультиканального виджета создайте Цель «JavaScript- событие» по инструкции 3. В идентификаторе цели укажите события, которые нужно отслеживать, из следующего списка:

| Наименование | Правило передачи<br>события | Категория | Действие |
| --- | --- | --- | --- |
| Чат начат | Клиент открыл форму<br>чата и написал туда<br>сообщение, при этом<br>нет активного диалога с<br>оператором | mch_chat | mch_chat_created |
| Чат установлен | Чат взят в работу<br>оператором | mch_chat | mch_chat_established |
| Запрос чата в<br>нерабочее<br>время | Клиент ввел и отправил<br>данные в форме чата в<br>нерабочее время | mch_chat | mch_chat_propose |

![Изображение, стр. 368](../images/232-postanovka-celey-po-sobytiyam-tekstovye-1.jpeg)

| Заказ<br>обратного<br>звонка | Клиент ввел номер<br>телефон, нажал<br>заказать звонок | mch_callback | mch_callback_created |
| --- | --- | --- | --- |
| Лидогенератор<br>показан | Посетителю сайта<br>отобразилась форма<br>лидогенератора | mch_leadgen | mch_leadgen_shown |
| Лидогенератор<br>показан | Посетитель сайта<br>заказал обратный<br>звонок в форме<br>лидогенератора | mch_leadgen | mch_leadgen_created |
| Проактивный<br>чат начат | Посетитель сайта<br>написал в проактивный<br>чат | mch_proactivechat | mch_proactivechat_crea<br>ted |
| Проактивный<br>чат начат | Посетителю сайта<br>отобразилось форма<br>проактивного чата | mch_proactivechat | mch_proactivechat_sho<br>wn |
| Проактивный<br>чат начат | Проактивный чат взят в<br>работу оператором | mch_proactivechat | mch_proactivechat_esta<br>blished |
| Нажатие на<br>кнопку канала<br>(Callback) | Пользователь нажал на<br>кнопку канала<br>«Обратный звонок» | mch_channel | mch_channel_press_call<br>back |
| Нажатие на<br>кнопку канала<br>(Chat) | Пользователь нажал на<br>кнопку канала «Чат» | mch_channel | mch_channel_press_cha<br>t |
| Нажатие на<br>кнопку канала<br>(VK) | Пользователь нажал на<br>кнопку канала<br>«ВКонтакте» | mch_channel | mch_channel_press_vk |
| Нажатие на<br>кнопку канала<br>(WhatsApp) | Пользователь нажал на<br>кнопку канала<br>«WhatsApp» | mch_channel | mch_channel_press_wh<br>atsapp |
| Нажатие на<br>кнопку канала<br>(Telegram) | Пользователь нажал на<br>кнопку канала<br>«Telegram» | mch_channel | mch_channel_press_tg |
| Нажатие на<br>кнопку канала<br>(Email) | Пользователь нажал на<br>кнопку канала «Email» | mch_channel | mch_channel_press_em<br>ail |
