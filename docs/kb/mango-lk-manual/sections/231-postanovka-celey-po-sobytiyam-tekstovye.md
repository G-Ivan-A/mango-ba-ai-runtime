---
id: mango-lk-manual-231-postanovka-celey-po-sobytiyam-tekstovye
doc_code: LK
doc_title: "Виртуальная АТС MANGO OFFICE - Справочник абонента"
doc_version: "1.25"
section: "4.5.11.5.1"
pdf_section: "4.5.11.5.1"
title: "Постановка целей по событиям «Текстовые коммуникации» в Яндекс.Метрике"
pdf_heading: "4.5.11.5.1 Постановка целей по событиям «Текстовые коммуникации» в Яндекс.Метрике"
pages: "368-370"
source: kb/sources/mango-lk-manual/LK_manual_v-125-281-566.pdf
source_part: "2"
source_pages: "ч.2: 88-90"
source_refs: '[{"source_pdf":"kb/sources/mango-lk-manual/LK_manual_v-125-281-566.pdf","part":2,"pages":"88-90","global_pages":"368-370"}]'
extracted_by: "pymupdf 1.28.2"
token_method: "tiktoken:cl100k_base"
tokens: 861
images: 0
status: extracted
ai-generated: true
---
##### 4.5.11.5.1. Постановка целей по событиям «Текстовые коммуникации» в Яндекс.Метрике

> Трассировка: PDF §4.5.11.5.1 · сквозные стр. 368-370 · источники: ч.2 `kb/sources/mango-lk-manual/LK_manual_v-125-281-566.pdf` с.88-90.

1. Зарегистрируйтесь в Яндекс.Метрике и установите счетчик на сайт, на котором размещен виджет «Текстовые коммуникации» , по инструкции 2. Для анализа событий Мультиканального виджета создайте Цель «JavaScript- событие» по инструкции 3. В идентификаторе цели укажите события, которые нужно отслеживать, из следующего списка:

Наименование Правило передачи

Категория Действие события

Клиент открыл форму

Чат начат

чата и написал туда

mch_chat mch_chat_created

сообщение, при этом

нет активного диалога с оператором

Чат установлен Чат взят в работу

mch_chat mch_chat_established оператором

Запрос чата в

Клиент ввел и отправил

нерабочее

данные в форме чата в

mch_chat mch_chat_propose

время

нерабочее время

Заказ

Клиент ввел номер

обратного

телефон, нажал

mch_callback mch_callback_created

звонка

заказать звонок

Посетителю сайта

Лидогенератор

отобразилась форма

mch_leadgen mch_leadgen_shown

показан

лидогенератора

Посетитель сайта

Лидогенератор

заказал обратный

mch_leadgen mch_leadgen_created

показан

звонок в форме лидогенератора

Посетитель сайта

Проактивный

mch_proactivechat mch_proactivechat_crea

написал в проактивный

чат начат

ted

чат

Посетителю сайта

Проактивный

mch_proactivechat mch_proactivechat_sho

отобразилось форма

чат начат

wn

проактивного чата

Проактивный

Проактивный чат взят в mch_proactivechat mch_proactivechat_esta

чат начат

работу оператором

blished Нажатие на

Пользователь нажал на

mch_channel_press_call

кнопку канала

кнопку канала

mch_channel back

(Callback)

«Обратный звонок»

Нажатие на

Пользователь нажал на mch_channel_press_cha

кнопку канала

mch_channel кнопку канала «Чат» t

(Chat)

Нажатие на

Пользователь нажал на

кнопку канала

кнопку канала

mch_channel mch_channel_press_vk

(VK)

«ВКонтакте»

Нажатие на

Пользователь нажал на

mch_channel_press_wh

кнопку канала

кнопку канала

mch_channel atsapp

(WhatsApp)

«WhatsApp»

Нажатие на

Пользователь нажал на

кнопку канала

кнопку канала

mch_channel mch_channel_press_tg

(Telegram)

«Telegram»

Нажатие на

Пользователь нажал на mch_channel_press_em

кнопку канала

mch_channel кнопку канала «Email» ail

(Email)
