---
id: integration-bitrix24-186-korobochnaya-versiya-bitriks24
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "6"
pdf_section: "6"
title: "Коробочная версия Битрикс24"
pdf_heading: "6 Коробочная версия Битрикс24"
pages: "168-169"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 168-169"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"168-169","global_pages":"168-169"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 597
status: extracted
ai-generated: true
---
# 6. Коробочная версия Битрикс24

> Трассировка: PDF §6 · сквозные стр. 168-169 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.168-169.

Рекомендации по настройке коробочного Битрикс24: ● скачать обновления коробочного Битрикс24 и проинсталлировать модуль rest версии 16.6.5 (или более позднюю); ● удостовериться, что установлен модуль intranet 16.6.4 или более поздняя версия; ● удостовериться, что Битрикс24 доступен "снаружи" и что он также "видит" внешние ресурсы – ведь для работы приложения потребуется обращение к серверу аутентификации aouth.bitrix24.info, а также к тем внешним URL, которые нужны для работы приложения; ● модуль "Push & Pull" (нужно настроить Push Server https://dev.1c- bitrix.ru/learning/course/index.php?COURSE_ID=1&LESSON_ID=123&LESSON_P ATH=123.123.123); ● модуль "Телефония"; ● поднять на своем сервере валидный SSL. Это обязательно. После этого в публичной части портала в главном меню появится подраздел Приложения, ведущий в папку https://ваш_битрикс/marketplace/ Тут будет доступен каталог облачных решений для Битрикс24, которые могут работать в коробке; ● после этого выполнить установку приложения MANGO OFFICE согласно данному руководству. Примечание: при авторизации обращайте внимание на адрес, куда вы авторизуетесь. Теперь вам надо авторизоваться по адресу https://ваш_битрикс. Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026
