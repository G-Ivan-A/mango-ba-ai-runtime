---
type: kb-source-index
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
status: extracted
ai-generated: true
source_document: "MangoOffice_VPBX_API_v1.9.pdf"
extraction_date: "2026-08-22"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "requires_review"
pages_covered: "1-367"
---

# API Mango Office — индекс БЗ (карта разделов)

> Источник: `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` · извлечено: pdfplumber 0.11.10 ·
> токены: tiktoken:cl100k_base. Это **карта поиска** для агента (замена
> retrieval-шага до RAG, ADR-007 R2): найди раздел по колонке «Когда
> обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия **requires_review**. Неоднозначности помечены в разделах маркерами `❓ ТРЕБУЕТСЯ ПРОВЕРКА` / `⚠️ ПРОБЕЛ ИЗВЛЕЧЕНИЯ` с точной ссылкой «PDF + страница».

## Как цитировать

`[VPBXAPI, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `kb/processed/<doc>/sections/<file>#<якорь>` (ADR-007 R3).

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-6 | ч.1 с.1-6 | 3885 | API MANGO OFFICE |
| — | Определения и сокращения | [sections/01-opredeleniya-i-sokrascheniya.md](sections/01-opredeleniya-i-sokrascheniya.md) | 7 | ч.1 с.7 | 557 | АК — адресная книга MANGO OFFICE, используется в Контакт-центр, M.TALKER. |
| 1 | Основные сведения | [sections/02-osnovnye-svedeniya.md](sections/02-osnovnye-svedeniya.md) | 8 | ч.1 с.8 | 65 | — |
| 1.1 | Назначение | [sections/03-naznachenie.md](sections/03-naznachenie.md) | 8 | ч.1 с.8 | 463 | API MANGO OFFICE (далее по тексту – API) позволяет внешним клиентским системам, |
| 1.2 | Требования совместимости и список поддерживаемых протоколов | [sections/04-trebovaniya-sovmestimosti-i-spisok-podde.md](sections/04-trebovaniya-sovmestimosti-i-spisok-podde.md) | 8 | ч.1 с.8 | 259 | Чтобы взаимодействовать с API, внешняя система должна обеспечивать: |
| 1.3 | Ограничения | [sections/05-ogranicheniya.md](sections/05-ogranicheniya.md) | 8 | ч.1 с.8 | 174 | 1) Не поддерживается протокол TLS версий 1.0, 1.1, 1.3. |
| 1.4 | Лимиты количества запросов к API | [sections/06-limity-kolichestva-zaprosov-k-api.md](sections/06-limity-kolichestva-zaprosov-k-api.md) | 9 | ч.1 с.9 | 128 | В API существуют ограничения на максимальное число запросов в секунду. |
| 1.4.1 | О неверных запросах к API. Ошибка 401 | [sections/07-o-nevernyh-zaprosah-k-api-oshibka-401.md](sections/07-o-nevernyh-zaprosah-k-api-oshibka-401.md) | 9 | ч.1 с.9 | 235 | Если ваш запрос к API MANGO OFFICE неверный, вы получаете код ошибки 3ХХХ. |
| 1.4.2 | API ВАТС | [sections/08-api-vats.md](sections/08-api-vats.md) | 9-10 | ч.1 с.9-10 | 757 | Устанавливаются следующие лимиты запросов в секунду: |
| 1.4.3 | API КЦ | [sections/09-api-kc.md](sections/09-api-kc.md) | 10 | ч.1 с.10 | 243 | Устанавливаются следующие лимиты запросов в секунду: |
| 1.4.4 | Что делать, если получили ошибку 503 и/или 5008? | [sections/10-chto-delat-esli-poluchili-oshibku-503-i.md](sections/10-chto-delat-esli-poluchili-oshibku-503-i.md) | 10 | ч.1 с.10 | 126 | Сделайте паузу или уменьшите интенсивность передачи запросов, или удалите лишние |
| 2 | Общие положения о взаимодействии систем | [sections/11-obschie-polozheniya-o-vzaimodeystvii-sis.md](sections/11-obschie-polozheniya-o-vzaimodeystvii-sis.md) | 11 | ч.1 с.11 | 73 | — |
| 2.1 | Модель авторизации | [sections/12-model-avtorizacii.md](sections/12-model-avtorizacii.md) | 11 | ч.1 с.11 | 296 | API предоставляет внешней системе доступ к своим функциям без ограничений. |
| 2.2 | Модель взаимодействия | [sections/13-model-vzaimodeystviya.md](sections/13-model-vzaimodeystviya.md) | 11 | ч.1 с.11 | 72 | — |
| 2.1.1 | API ВАТС | [sections/14-api-vats.md](sections/14-api-vats.md) | 11-12 | ч.1 с.11-12 | 1441 | Описание модели |
| 2.1.2 | API КЦ | [sections/15-api-kc.md](sections/15-api-kc.md) | 13 | ч.1 с.13 | 271 | Модель взаимодействия API КЦ с внешними системами практически полностью повторяет |
| 2.3 | Работа с услугами Виртуальной АТС | [sections/16-rabota-s-uslugami-virtualnoy-ats.md](sections/16-rabota-s-uslugami-virtualnoy-ats.md) | 13 | ч.1 с.13 | 252 | API предоставляет внешней системе доступ к подключению услуг. |
| 2.4 | Уникальный код вашей ВАТС, ключ для создания подписи и параметр "sign" | [sections/17-unikalnyy-kod-vashey-vats-klyuch-dlya-so.md](sections/17-unikalnyy-kod-vashey-vats-klyuch-dlya-so.md) | 14 | ч.1 с.14 | 89 | "sign" |
| 2.4.1 | Уникальный код вашей ВАТС | [sections/18-unikalnyy-kod-vashey-vats.md](sections/18-unikalnyy-kod-vashey-vats.md) | 14 | ч.1 с.14 | 183 | Уникальный код вашей ВАТС представляет собой строку вида: |
| 2.4.2 | Ключ создания подписи | [sections/19-klyuch-sozdaniya-podpisi.md](sections/19-klyuch-sozdaniya-podpisi.md) | 14 | ч.1 с.14 | 169 | При отправке запросов к API ВАТС используется ключ создания подписи. |
| 2.4.3 | О параметре "sign" | [sections/20-o-parametre-sign.md](sections/20-o-parametre-sign.md) | 14 | ч.1 с.14 | 235 | Данные, которыми обмениваются системы, как правило, будут передаваться в теле POST- |
| 2.4.4 | Поле json | [sections/21-pole-json.md](sections/21-pole-json.md) | 15 | ч.1 с.15 | 256 | Поле json можно рассматривать как ассоциативный массив любой вложенности и размера |
| 2.4.5 | Как узнать свой уникальный код ВАТС и ключ создания подписи? | [sections/22-kak-uznat-svoy-unikalnyy-kod-vats-i-klyu.md](sections/22-kak-uznat-svoy-unikalnyy-kod-vats-i-klyu.md) | 15 | ч.1 с.15 | 263 | Для этого в Личном кабинете MANGO OFFICE следует: |
| 2.5 | Эмулятор API Виртуальной АТС | [sections/23-emulyator-api-virtualnoy-ats.md](sections/23-emulyator-api-virtualnoy-ats.md) | 15 | ч.1 с.15 | 119 | Для удобства знакомства с API ВАТС разработан и размещен на сайте Эмулятор API |
| 3 | Описание методов API Виртуальной АТС MANGO OFFICE | [sections/24-opisanie-metodov-api-virtualnoy-ats-mang.md](sections/24-opisanie-metodov-api-virtualnoy-ats-mang.md) | 16 | ч.1 с.16 | 75 | — |
| 3.1 | API Realtime | [sections/25-api-realtime.md](sections/25-api-realtime.md) | 16 | ч.1 с.16 | 65 | — |
| 3.1.1 | Общее | [sections/26-obschee.md](sections/26-obschee.md) | 16 | ч.1 с.16 | 270 | API Realtime представляет собой набор запросов (уведомлений), которые направляются |
| 3.1.2 | Уведомление о вызове | [sections/27-uvedomlenie-o-vyzove.md](sections/27-uvedomlenie-o-vyzove.md) | 16-22 | ч.1 с.16-22 | 5271 | POST https://external-system.com/events/call |
| 3.1.3 | Уведомление о результате отправки SMS | [sections/28-uvedomlenie-o-rezultate-otpravki-sms.md](sections/28-uvedomlenie-o-rezultate-otpravki-sms.md) | 22 | ч.1 с.22 | 388 | POST https://external-system.com/events/sms |
| 3.1.4 | Уведомление о записи разговора | [sections/29-uvedomlenie-o-zapisi-razgovora.md](sections/29-uvedomlenie-o-zapisi-razgovora.md) | 22-26 | ч.1 с.22-26 | 1982 | POST https://external-system.com/events/recording |
| 3.1.5 | Уведомление о нажатиях DTMF клавиш | [sections/30-uvedomlenie-o-nazhatiyah-dtmf-klavish.md](sections/30-uvedomlenie-o-nazhatiyah-dtmf-klavish.md) | 26 | ч.1 с.26 | 734 | POST https://external-system.com/events/dtmf |
| 3.1.5 | О параметре location | [sections/31-o-parametre-location.md](sections/31-o-parametre-location.md) | 26-27 | ч.1 с.26-27 | 526 | Параметр location состоит из двух определителей и имеет следующий формат: |
| 3.1.6 | Уведомление о завершении вызова | [sections/32-uvedomlenie-o-zavershenii-vyzova.md](sections/32-uvedomlenie-o-zavershenii-vyzova.md) | 27-31 | ч.1 с.27-31 | 3054 | POST https://external-system.com/events/summary |
| 3.1.7 | Событие о завершении процесса распознавания тематик в разговорах | [sections/33-sobytie-o-zavershenii-processa-raspoznav.md](sections/33-sobytie-o-zavershenii-processa-raspoznav.md) | 31-32 | ч.1 с.31-32 | 602 | POST https://external-system.com/events/record/tagged |
| 3.1.8 | Событие о помещении записи разговора в облачное хранилище | [sections/34-sobytie-o-pomeschenii-zapisi-razgovora-v.md](sections/34-sobytie-o-pomeschenii-zapisi-razgovora-v.md) | 32 | ч.1 с.32 | 609 | POST https://external-system.com/events/record/added |
| 3.2 | API Команды | [sections/35-api-komandy.md](sections/35-api-komandy.md) | 33 | ч.1 с.33 | 234 | API Команды представляет собой набор запросов, которые инициирует внешняя система и |
| 3.2.1 | Инициирование вызова от имени сотрудника | [sections/36-iniciirovanie-vyzova-ot-imeni-sotrudnika.md](sections/36-iniciirovanie-vyzova-ot-imeni-sotrudnika.md) | 33-36 | ч.1 с.33-36 | 1832 | POST /vpbx/commands/callback |
| 3.2.2 | Инициирование вызова от имени группы | [sections/37-iniciirovanie-vyzova-ot-imeni-gruppy.md](sections/37-iniciirovanie-vyzova-ot-imeni-gruppy.md) | 36-38 | ч.1 с.36-38 | 1355 | POST /vpbx/commands/callback_group |
| 3.2.3 | Завершение вызова | [sections/38-zavershenie-vyzova.md](sections/38-zavershenie-vyzova.md) | 38-39 | ч.1 с.38-39 | 898 | POST /vpbx/commands/call/hangup |
| 3.2.4 | Отправка SMS | [sections/39-otpravka-sms.md](sections/39-otpravka-sms.md) | 39-41 | ч.1 с.39-41 | 1460 | POST /vpbx/commands/sms |
| 3.2.5 | Включение записи разговора | [sections/40-vklyuchenie-zapisi-razgovora.md](sections/40-vklyuchenie-zapisi-razgovora.md) | 41-43 | ч.1 с.41-43 | 1438 | POST /vpbx/commands/recording/start |
| 3.2.6 | Включение воспроизведения звукового файла | [sections/41-vklyuchenie-vosproizvedeniya-zvukovogo-f.md](sections/41-vklyuchenie-vosproizvedeniya-zvukovogo-f.md) | 43-45 | ч.1 с.43-45 | 1658 | POST /vpbx/commands/play/start |
| 3.2.7 | Маршрутизация вызова | [sections/42-marshrutizaciya-vyzova.md](sections/42-marshrutizaciya-vyzova.md) | 45-46 | ч.1 с.45-46 | 837 | POST /vpbx/commands/route |
| 3.2.7 | О параметре route | [sections/43-o-parametre-route.md](sections/43-o-parametre-route.md) | 46-49 | ч.1 с.46-49 | 1066 | Команда route может работать в следующих режимах: |
| 3.2.8 | Перевод вызова | [sections/44-perevod-vyzova.md](sections/44-perevod-vyzova.md) | 50-55 | ч.1 с.50-55 | 1977 | POST /vpbx/commands/transfer |
| 3.2.9 | Соединение вызова в режиме OnHold и вызова в режиме Connected | [sections/45-soedinenie-vyzova-v-rezhime-onhold-i-vyz.md](sections/45-soedinenie-vyzova-v-rezhime-onhold-i-vyz.md) | 55-56 | ч.1 с.55-56 | 1213 | POST /commands/calls_connect |
| 3.2.10 | Отмена перевода вызова | [sections/46-otmena-perevoda-vyzova.md](sections/46-otmena-perevoda-vyzova.md) | 57-58 | ч.1 с.57-58 | 888 | POST /commands/transfer_cancel |
| 3.2.11 | Постановка вызова на удержание | [sections/47-postanovka-vyzova-na-uderzhanie.md](sections/47-postanovka-vyzova-na-uderzhanie.md) | 58 | ч.1 с.58 | 79 | — |
| 3.2.11.1 | Описание запроса на удержание вызова | [sections/48-opisanie-zaprosa-na-uderzhanie-vyzova.md](sections/48-opisanie-zaprosa-na-uderzhanie-vyzova.md) | 58 | ч.1 с.58 | 568 | POST /commands/call/hold/on |
| 3.2.11.2 | Получение результата выполнения запроса | [sections/49-poluchenie-rezultata-vypolneniya-zaprosa.md](sections/49-poluchenie-rezultata-vypolneniya-zaprosa.md) | 58-59 | ч.1 с.58-59 | 531 | POST /result/call/hold/on |
| 3.3 | Методы работы с правилами переадресации | [sections/50-metody-raboty-s-pravilami-pereadresacii.md](sections/50-metody-raboty-s-pravilami-pereadresacii.md) | 59 | ч.1 с.59 | 131 | Служат для работы со списком переадресации в ЛК ВАТС из внешней системы. |
| 3.3.1 | Получить список правил переадресации | [sections/51-poluchit-spisok-pravil-pereadresacii.md](sections/51-poluchit-spisok-pravil-pereadresacii.md) | 59-61 | ч.1 с.59-61 | 1829 | POST /vpbx/forwarding/numbers |
| 3.3.2 | Добавление нового правила переадресации | [sections/52-dobavlenie-novogo-pravila-pereadresacii.md](sections/52-dobavlenie-novogo-pravila-pereadresacii.md) | 62-63 | ч.1 с.62-63 | 1711 | POST /vpbx/forwarding/number/add |
| 3.3.3 | Изменение правила переадресации | [sections/53-izmenenie-pravila-pereadresacii.md](sections/53-izmenenie-pravila-pereadresacii.md) | 64-65 | ч.1 с.64-65 | 1586 | POST /vpbx/forwarding/number/change |
| 3.3.4 | Удаление правила переадресации | [sections/54-udalenie-pravila-pereadresacii.md](sections/54-udalenie-pravila-pereadresacii.md) | 65-66 | ч.1 с.65-66 | 461 | POST /vpbx/forwarding/number/remove |
| 3.4 | API Статистика | [sections/55-api-statistika.md](sections/55-api-statistika.md) | 66 | ч.1 с.66 | 138 | Позволяет получить данные истории вызовов с помощью асинхронных запросов. |
| 3.4.1 | Запрос базовой статистики | [sections/56-zapros-bazovoy-statistiki.md](sections/56-zapros-bazovoy-statistiki.md) | 66 | ч.1 с.66 | 125 | Получение базовой статистики состоит из следующих этапов: |
| 3.4.1.1 | Запуск формирования статистики | [sections/57-zapusk-formirovaniya-statistiki.md](sections/57-zapusk-formirovaniya-statistiki.md) | 66-69 | ч.1 с.66-69 | 1805 | POST /vpbx/stats/request |
| 3.4.1.2 | Получение статистики вызовов | [sections/58-poluchenie-statistiki-vyzovov.md](sections/58-poluchenie-statistiki-vyzovov.md) | 69-71 | ч.1 с.69-71 | 1820 | Подготовленные данные хранятся до обращения за ними не менее 1 минуты. |
| 3.4.2 | Запрос расширенной статистики | [sections/59-zapros-rasshirennoy-statistiki.md](sections/59-zapros-rasshirennoy-statistiki.md) | 71 | ч.1 с.71 | 79 | — |
| 3.4.2.1 | Обзор | [sections/60-obzor.md](sections/60-obzor.md) | 71 | ч.1 с.71 | 242 | Запрос расширенной статистики – это новый вид запроса, обработка которого оптимизирована |
| 3.4.2.2 | Запуск формирования статистики | [sections/61-zapusk-formirovaniya-statistiki.md](sections/61-zapusk-formirovaniya-statistiki.md) | 71-72 | ч.1 с.71-72 | 1365 | POST /vpbx/stats/calls/request |
| 3.4.2.3 | Получение статистики вызовов | [sections/62-poluchenie-statistiki-vyzovov.md](sections/62-poluchenie-statistiki-vyzovov.md) | 72-86 | ч.1 с.72-86 | 8589 | Подготовленные данные хранятся до обращения за ними не менее 1 минуты. |
| 3.5 | API Записи разговоров, Речевая Аналитика | [sections/63-api-zapisi-razgovorov-rechevaya-analitik.md](sections/63-api-zapisi-razgovorov-rechevaya-analitik.md) | 87 | ч.1 с.87 | 548 | Речевая Аналитика (далее по тексту – РА) – это сервис, который позволяет расшифровывать и |
| 3.5.1 | Получение записи разговора посредством POST запроса | [sections/64-poluchenie-zapisi-razgovora-posredstvom.md](sections/64-poluchenie-zapisi-razgovora-posredstvom.md) | 87-88 | ч.1 с.87-88 | 466 | POST /vpbx/queries/recording/post |
| 3.5.2 | Получение записи разговора посредством GET запроса без авторизации | [sections/65-poluchenie-zapisi-razgovora-posredstvom.md](sections/65-poluchenie-zapisi-razgovora-posredstvom.md) | 88-89 | ч.1 с.88-89 | 729 | GET |
| 3.5.3 | Прямая ссылка на запись разговора с авторизацией через Личный кабинет | [sections/66-pryamaya-ssylka-na-zapis-razgovora-s-avt.md](sections/66-pryamaya-ssylka-na-zapis-razgovora-s-avt.md) | 90 | ч.1 с.90 | 639 | GET /vpbx/queries/recording/issa/[recording_id]/[action] |
| 3.5.4 | Получение тематик разговора (Speech2Text) | [sections/67-poluchenie-tematik-razgovora-speech2text.md](sections/67-poluchenie-tematik-razgovora-speech2text.md) | 90-92 | ч.1 с.90-92 | 1482 | POST /vpbx/queries/recording_categories |
| 3.5.5 | Получение списка расшифровок распознанных разговоров | [sections/68-poluchenie-spiska-rasshifrovok-raspoznan.md](sections/68-poluchenie-spiska-rasshifrovok-raspoznan.md) | 92-94 | ч.1 с.92-94 | 956 | POST /vpbx/queries/recording_transcripts |
| 3.5.6 | Запрос информации о конспекте разговора | [sections/69-zapros-informacii-o-konspekte-razgovora.md](sections/69-zapros-informacii-o-konspekte-razgovora.md) | 94 | ч.1 с.94 | 627 | POST /s2t/queries/recording_summary |
| 3.5.7 | Запрос записей с расшифровками звонков | [sections/70-zapros-zapisey-s-rasshifrovkami-zvonkov.md](sections/70-zapros-zapisey-s-rasshifrovkami-zvonkov.md) | 95-96 | ч.1 с.95-96 | 964 | POST /s2t/queries/records |
| 3.5.8 | Получение списка ИИ помощников | [sections/71-poluchenie-spiska-ii-pomoschnikov.md](sections/71-poluchenie-spiska-ii-pomoschnikov.md) | 96-99 | ч.1 с.96-99 | 1803 | POST /s2t/queries/ai_agents |
| 3.5.9 | Получение результатов работы ИИ помощников | [sections/72-poluchenie-rezultatov-raboty-ii-pomoschn.md](sections/72-poluchenie-rezultatov-raboty-ii-pomoschn.md) | 100-102 | ч.1 с.100-102 | 1614 | POST /s2t/queries/recording_agents |
| 3.6 | Сквозная аналитика. | [sections/73-skvoznaya-analitika.md](sections/73-skvoznaya-analitika.md) | 102 | ч.1 с.102 | 72 | — |
| 3.6.1 | Запрос информации о посетителе сайта по динамическому номеру | [sections/74-zapros-informacii-o-posetitele-sayta-po.md](sections/74-zapros-informacii-o-posetitele-sayta-po.md) | 102-104 | ч.1 с.102-104 | 1429 | POST /vpbx/queries/user_info_by_dct_number |
| 3.6.2 | Запрос истории навигации посетителя сайта по динамическому номеру | [sections/75-zapros-istorii-navigacii-posetitelya-say.md](sections/75-zapros-istorii-navigacii-posetitelya-say.md) | 104 | ч.1 с.104 | 490 | POST /vpbx/queries/user_history_by_dct_number |
| 3.7 | API Конфигурация | [sections/76-api-konfiguraciya.md](sections/76-api-konfiguraciya.md) | 105 | ч.1 с.105 | 117 | API Конфигурация — служит для управления параметрами Виртуальной АТС, а также |
| 3.7.1 | Запрос списка сотрудников ВАТС | [sections/77-zapros-spiska-sotrudnikov-vats.md](sections/77-zapros-spiska-sotrudnikov-vats.md) | 105-113 | ч.1 с.105-113 | 3849 | POST /vpbx/config/users/request |
| 3.7.2 | Получить список групп | [sections/78-poluchit-spisok-grupp.md](sections/78-poluchit-spisok-grupp.md) | 113-116 | ч.1 с.113-116 | 2092 | POST /vpbx/groups |
| 3.7.3 | Добавить группу | [sections/79-dobavit-gruppu.md](sections/79-dobavit-gruppu.md) | 116-118 | ч.1 с.116-118 | 1840 | POST /vpbx/group/create |
| 3.7.4 | Редактировать группу | [sections/80-redaktirovat-gruppu.md](sections/80-redaktirovat-gruppu.md) | 118-120 | ч.1 с.118-120 | 2159 | POST /vpbx/group/update |
| 3.7.5 | Удалить группу | [sections/81-udalit-gruppu.md](sections/81-udalit-gruppu.md) | 121 | ч.1 с.121 | 526 | POST /vpbx/group/delete |
| 3.7.6 | Получение баланса | [sections/82-poluchenie-balansa.md](sections/82-poluchenie-balansa.md) | 121-122 | ч.1 с.121-122 | 372 | POST /vpbx/account/balance |
| 3.7.7 | Получение списка номеров ВАТС | [sections/83-poluchenie-spiska-nomerov-vats.md](sections/83-poluchenie-spiska-nomerov-vats.md) | 122-123 | ч.1 с.122-123 | 854 | POST /vpbx/incominglines |
| 3.7.8 | Получение списка мелодий и звуковых сообщений | [sections/84-poluchenie-spiska-melodiy-i-zvukovyh-soo.md](sections/84-poluchenie-spiska-melodiy-i-zvukovyh-soo.md) | 123-124 | ч.1 с.123-124 | 590 | POST /vpbx/audiofiles |
| 3.7.9 | Получение списка схем переадресаций | [sections/85-poluchenie-spiska-shem-pereadresaciy.md](sections/85-poluchenie-spiska-shem-pereadresaciy.md) | 124-126 | ч.1 с.124-126 | 1118 | POST /vpbx/schemas |
| 3.7.10 | Установить схему на входящем номере | [sections/86-ustanovit-shemu-na-vhodyaschem-nomere.md](sections/86-ustanovit-shemu-na-vhodyaschem-nomere.md) | 127-128 | ч.1 с.127-128 | 721 | POST /vpbx/schema/set |
| 3.7.11 | Получить список ролей | [sections/87-poluchit-spisok-roley.md](sections/87-poluchit-spisok-roley.md) | 128-129 | ч.1 с.128-129 | 593 | POST /vpbx/roles |
| 3.7.12 | Создать сотрудника | [sections/88-sozdat-sotrudnika.md](sections/88-sozdat-sotrudnika.md) | 130-131 | ч.1 с.130-131 | 1621 | POST /vpbx/member/create |
| 3.7.13 | Редактировать сотрудника | [sections/89-redaktirovat-sotrudnika.md](sections/89-redaktirovat-sotrudnika.md) | 131 | ч.1 с.131 | 155 | Метод позволяет редактировать данные сотрудника Виртуальной АТС. |
| 3.7.13.1 | Ограничения | [sections/90-ogranicheniya.md](sections/90-ogranicheniya.md) | 131-132 | ч.1 с.131-132 | 313 | Необходимо учитывать следующие факторы: |
| 3.7.13.2 | Описание метода | [sections/91-opisanie-metoda.md](sections/91-opisanie-metoda.md) | 132-134 | ч.1 с.132-134 | 1695 | POST /vpbx/member/update |
| 3.7.14 | Удалить сотрудника | [sections/92-udalit-sotrudnika.md](sections/92-udalit-sotrudnika.md) | 135 | ч.1 с.135 | 419 | POST /vpbx/member/delete |
| 3.7.15 | Получить список индивидуальных правил автосекретаря для сотрудников | [sections/93-poluchit-spisok-individualnyh-pravil-avt.md](sections/93-poluchit-spisok-individualnyh-pravil-avt.md) | 135-138 | ч.1 с.135-138 | 1903 | POST /vpbx/autosecretary/rules |
| 3.7.16 | Изменить статус индивидуальных правил автосекретаря сотрудника | [sections/94-izmenit-status-individualnyh-pravil-avto.md](sections/94-izmenit-status-individualnyh-pravil-avto.md) | 138 | ч.1 с.138 | 547 | POST /vpbx/autosecretary/status/change |
| 3.7.17 | Получить sip учетные записи сотрудников | [sections/95-poluchit-sip-uchetnye-zapisi-sotrudnikov.md](sections/95-poluchit-sip-uchetnye-zapisi-sotrudnikov.md) | 139 | ч.1 с.139 | 506 | POST /vpbx/sips |
| 3.7.18 | Получить настроенные домены | [sections/96-poluchit-nastroennye-domeny.md](sections/96-poluchit-nastroennye-domeny.md) | 140 | ч.1 с.140 | 351 | POST /vpbx/domains |
| 3.7.19 | Создать sip-учетку | [sections/97-sozdat-sip-uchetku.md](sections/97-sozdat-sip-uchetku.md) | 140-141 | ч.1 с.140-141 | 608 | POST /vpbx/sip/create |
| 3.7.20 | Редактировать sip-учетку | [sections/98-redaktirovat-sip-uchetku.md](sections/98-redaktirovat-sip-uchetku.md) | 141-142 | ч.1 с.141-142 | 733 | POST /vpbx/sip/update |
| 3.7.21 | Удалить sip-учетку | [sections/99-udalit-sip-uchetku.md](sections/99-udalit-sip-uchetku.md) | 142-143 | ч.1 с.142-143 | 404 | POST /vpbx/sip/delete |
| 3.7.22 | Запрос номеров sip-trunk'ов | [sections/100-zapros-nomerov-sip-trunk-ov.md](sections/100-zapros-nomerov-sip-trunk-ov.md) | 143-144 | ч.1 с.143-144 | 583 | POST /vpbx/trunks/numbers |
| 3.8 | API запрещенных направлений вызова | [sections/101-api-zapreschennyh-napravleniy-vyzova.md](sections/101-api-zapreschennyh-napravleniy-vyzova.md) | 144 | ч.1 с.144 | 75 | — |
| 3.8.1 | Общее | [sections/102-obschee.md](sections/102-obschee.md) | 144 | ч.1 с.144 | 360 | При помощи данных методов API вы можете ограничить прием и совершение вызовов через |
| 3.8.2 | Ограничение входящих коммуникаций | [sections/103-ogranichenie-vhodyaschih-kommunikaciy.md](sections/103-ogranichenie-vhodyaschih-kommunikaciy.md) | 144 | ч.1 с.144 | 83 | — |
| 3.8.2.1 | Получение текущего режима работы ч/б списка | [sections/104-poluchenie-tekuschego-rezhima-raboty-ch.md](sections/104-poluchenie-tekuschego-rezhima-raboty-ch.md) | 144-145 | ч.1 с.144-145 | 506 | POST /vpbx/bwlists/state/ |
| 3.8.2.2 | Получнение списка номеров, входящих в ч/б списки ВАТС | [sections/105-poluchnenie-spiska-nomerov-vhodyaschih-v.md](sections/105-poluchnenie-spiska-nomerov-vhodyaschih-v.md) | 145-147 | ч.1 с.145-147 | 993 | POST /vpbx/bwlists/numbers/ |
| 3.8.2.3 | Добавление номера в ч/б список ВАТС | [sections/106-dobavlenie-nomera-v-ch-b-spisok-vats.md](sections/106-dobavlenie-nomera-v-ch-b-spisok-vats.md) | 147-148 | ч.1 с.147-148 | 725 | POST /vpbx/bwlists/number/add/ |
| 3.8.2.4 | Удаление номера из ч/б списка ВАТС | [sections/107-udalenie-nomera-iz-ch-b-spiska-vats.md](sections/107-udalenie-nomera-iz-ch-b-spiska-vats.md) | 148 | ч.1 с.148 | 430 | POST /vpbx/bwlists/number/delete/ |
| 3.8.3 | Ограничение исходящих коммуникаций | [sections/108-ogranichenie-ishodyaschih-kommunikaciy.md](sections/108-ogranichenie-ishodyaschih-kommunikaciy.md) | 149 | ч.1 с.149 | 84 | — |
| 3.8.3.1 | Получение списка номеров, включенных в "черный" список ИО | [sections/109-poluchenie-spiska-nomerov-vklyuchennyh-v.md](sections/109-poluchenie-spiska-nomerov-vklyuchennyh-v.md) | 149-150 | ч.1 с.149-150 | 1164 | POST /vpbx/outbound_blacklist/get |
| 3.8.3.2 | Добавление номера в "черный" список ИО | [sections/110-dobavlenie-nomera-v-chernyy-spisok-io.md](sections/110-dobavlenie-nomera-v-chernyy-spisok-io.md) | 150-152 | ч.1 с.150-152 | 1143 | POST /vpbx/outbound_blacklist/add |
| 3.8.3.3 | Обновление описания номера в "черном" списке ИО | [sections/111-obnovlenie-opisaniya-nomera-v-chernom-sp.md](sections/111-obnovlenie-opisaniya-nomera-v-chernom-sp.md) | 152-153 | ч.1 с.152-153 | 711 | POST /vpbx/outbound_blacklist/update_description |
| 3.8.3.4 | Блокировка номера, внесенного в "черный" список ИО | [sections/112-blokirovka-nomera-vnesennogo-v-chernyy-s.md](sections/112-blokirovka-nomera-vnesennogo-v-chernyy-s.md) | 153-154 | ч.1 с.153-154 | 839 | POST /vpbx/outbound_blacklist/enable_mode |
| 3.8.3.5 | Разблокировка номера, внесенного в "черный" список ИО | [sections/113-razblokirovka-nomera-vnesennogo-v-cherny.md](sections/113-razblokirovka-nomera-vnesennogo-v-cherny.md) | 154-155 | ч.1 с.154-155 | 812 | POST /vpbx/outbound_blacklist/disable_mode |
| 3.8.3.6 | Удаление номера из "черного" списка ИО | [sections/114-udalenie-nomera-iz-chernogo-spiska-io.md](sections/114-udalenie-nomera-iz-chernogo-spiska-io.md) | 155-156 | ч.1 с.155-156 | 604 | POST /vpbx/outbound_blacklist/delete |
| 3.8.3.7 | Включение запрета на все исходящие коммуникации | [sections/115-vklyuchenie-zapreta-na-vse-ishodyaschie.md](sections/115-vklyuchenie-zapreta-na-vse-ishodyaschie.md) | 156 | ч.1 с.156 | 354 | POST /vpbx/outbound_blacklist/enable |
| 3.8.3.8 | Выключение запрета на все исходящие коммуникации | [sections/116-vyklyuchenie-zapreta-na-vse-ishodyaschie.md](sections/116-vyklyuchenie-zapreta-na-vse-ishodyaschie.md) | 157 | ч.1 с.157 | 364 | POST /vpbx/outbound_blacklist/disable |
| 3.9 | API для работы с адресной книгой | [sections/117-api-dlya-raboty-s-adresnoy-knigoy.md](sections/117-api-dlya-raboty-s-adresnoy-knigoy.md) | 157 | ч.1 с.157 | 168 | Возможности API, указанные в данном разделе, служат для управления адресной книгой |
| 3.9.1 | Организации | [sections/118-organizacii.md](sections/118-organizacii.md) | 157 | ч.1 с.157 | 71 | — |
| 3.9.1.1 | Получить организацию по id | [sections/119-poluchit-organizaciyu-po-id.md](sections/119-poluchit-organizaciyu-po-id.md) | 157-159 | ч.1 с.157-159 | 463 | POST /vpbx/ab/organization |
| 3.9.1.2 | Получить список организаций, инициация отчета | [sections/120-poluchit-spisok-organizaciy-iniciaciya-o.md](sections/120-poluchit-spisok-organizaciy-iniciaciya-o.md) | 159-161 | ч.1 с.159-161 | 1383 | POST /vpbx/ab/organizations/init |
| 3.9.1.3 | Получить список организаций, постраничное получение | [sections/121-poluchit-spisok-organizaciy-postranichno.md](sections/121-poluchit-spisok-organizaciy-postranichno.md) | 161-163 | ч.1 с.161-163 | 1406 | POST /vpbx/ab/organizations/cursor |
| 3.9.1.4 | Добавить организацию | [sections/122-dobavit-organizaciyu.md](sections/122-dobavit-organizaciyu.md) | 163-164 | ч.1 с.163-164 | 688 | POST /vpbx/ab/organizations/create |
| 3.9.1.5 | Редактировать организацию | [sections/123-redaktirovat-organizaciyu.md](sections/123-redaktirovat-organizaciyu.md) | 164-165 | ч.1 с.164-165 | 695 | POST /vpbx/ab/organizations/update |
| 3.9.1.6 | Удалить организацию | [sections/124-udalit-organizaciyu.md](sections/124-udalit-organizaciyu.md) | 165-166 | ч.1 с.165-166 | 493 | POST /vpbx/ab/organizations/delete |
| 3.9.2 | Группы | [sections/125-gruppy.md](sections/125-gruppy.md) | 166 | ч.1 с.166 | 69 | — |
| 3.9.2.1 | Получить группу по id | [sections/126-poluchit-gruppu-po-id.md](sections/126-poluchit-gruppu-po-id.md) | 166-167 | ч.1 с.166-167 | 451 | POST /vpbx/ab/group |
| 3.9.2.2 | Получить список групп, инициация отчета | [sections/127-poluchit-spisok-grupp-iniciaciya-otcheta.md](sections/127-poluchit-spisok-grupp-iniciaciya-otcheta.md) | 167-168 | ч.1 с.167-168 | 1351 | POST /vpbx/ab/groups/init |
| 3.9.2.3 | Получить список групп, постраничное получение | [sections/128-poluchit-spisok-grupp-postranichnoe-polu.md](sections/128-poluchit-spisok-grupp-postranichnoe-polu.md) | 168-170 | ч.1 с.168-170 | 1437 | POST /vpbx/ab/groups/cursor |
| 3.9.2.4 | Добавить группу | [sections/129-dobavit-gruppu.md](sections/129-dobavit-gruppu.md) | 170-171 | ч.1 с.170-171 | 613 | POST /vpbx/ab/groups/create/ |
| 3.9.2.5 | Редактировать группу | [sections/130-redaktirovat-gruppu.md](sections/130-redaktirovat-gruppu.md) | 171-172 | ч.1 с.171-172 | 668 | POST /vpbx/ab/groups/update |
| 3.9.2.6 | Удалить группу | [sections/131-udalit-gruppu.md](sections/131-udalit-gruppu.md) | 172-173 | ч.1 с.172-173 | 397 | POST /vpbx/ab/groups/delete |
| 3.9.3 | Контакты | [sections/132-kontakty.md](sections/132-kontakty.md) | 173 | ч.1 с.173 | 70 | — |
| 3.9.3.1 | Получить список контактов, инициация отчета | [sections/133-poluchit-spisok-kontaktov-iniciaciya-otc.md](sections/133-poluchit-spisok-kontaktov-iniciaciya-otc.md) | 173-178 | ч.1 с.173-178 | 3651 | POST /vpbx/ab/contact/init |
| 3.9.3.2 | Получить список контактов, постраничное получение | [sections/134-poluchit-spisok-kontaktov-postranichnoe.md](sections/134-poluchit-spisok-kontaktov-postranichnoe.md) | 178-182 | ч.1 с.178-182 | 3539 | POST /vpbx/ab/contact/cursor |
| 3.9.3.3 | Получить контакт по id | [sections/135-poluchit-kontakt-po-id.md](sections/135-poluchit-kontakt-po-id.md) | 182-185 | ч.1 с.182-185 | 2582 | POST /vpbx/ab/contact |
| 3.9.3.4 | Добавить контакт | [sections/136-dobavit-kontakt.md](sections/136-dobavit-kontakt.md) | 185-191 | ч.1 с.185-191 | 3759 | POST /vpbx/ab/contacts/create/ |
| 3.9.3.5 | Редактировать контакт | [sections/137-redaktirovat-kontakt.md](sections/137-redaktirovat-kontakt.md) | 191-195 | ч.1 с.191-195 | 3756 | POST /vpbx/ab/contacts/update |
| 3.9.3.6 | Удалить контакт | [sections/138-udalit-kontakt.md](sections/138-udalit-kontakt.md) | 195-196 | ч.1 с.195-196 | 398 | POST /vpbx/ab/contacts/delete |
| 3.9.4 | Уведомление об операциях с адресной книгой | [sections/139-uvedomlenie-ob-operaciyah-s-adresnoy-kni.md](sections/139-uvedomlenie-ob-operaciyah-s-adresnoy-kni.md) | 196 | ч.1 с.196 | 81 | — |
| 3.9.4.1 | Обзор | [sections/140-obzor.md](sections/140-obzor.md) | 196 | ч.1 с.196 | 164 | POST https://external-system.com/events/ab/ |
| 3.9.4.2 | Для организаций | [sections/141-dlya-organizaciy.md](sections/141-dlya-organizaciy.md) | 196-197 | ч.1 с.196-197 | 659 | Параметры: |
| 3.9.4.3 | Для групп | [sections/142-dlya-grupp.md](sections/142-dlya-grupp.md) | 197-199 | ч.1 с.197-199 | 901 | Параметры: |
| 3.9.4.4 | Для контактов | [sections/143-dlya-kontaktov.md](sections/143-dlya-kontaktov.md) | 199-201 | ч.1 с.199-201 | 2361 | Параметры запроса: |
| 3.9.5 | Получение набора пользовательских полей | [sections/144-poluchenie-nabora-polzovatelskih-poley.md](sections/144-poluchenie-nabora-polzovatelskih-poley.md) | 201-203 | ч.1 с.201-203 | 1184 | POST /vpbx/ab/custom_fields/ |
| 3.10 | API для работы с записями и метаданными, полученными из оффлайн-источников | [sections/145-api-dlya-raboty-s-zapisyami-i-metadannym.md](sections/145-api-dlya-raboty-s-zapisyami-i-metadannym.md) | 203-204 | ч.1 с.203-204 | 157 | оффлайн-источников |
| 3.10.1 | Загрузка и распознавание речи в WAV-файле с привязкой к сотруднику | [sections/146-zagruzka-i-raspoznavanie-rechi-v-wav-fay.md](sections/146-zagruzka-i-raspoznavanie-rechi-v-wav-fay.md) | 204 | ч.1 с.204 | 100 | — |
| 3.10.1.1 | Обзор | [sections/147-obzor.md](sections/147-obzor.md) | 204 | ч.1 с.204 | 452 | Метод обеспечивает загрузку в ВАТС и распознавание речи в звуковом файле, который |
| 3.10.1.2 | Требования и рекомендации | [sections/148-trebovaniya-i-rekomendacii.md](sections/148-trebovaniya-i-rekomendacii.md) | 204 | ч.1 с.204 | 296 | Чтобы использовать данный метод, необходимо в вашей ВАТС подключить услуги: |
| 3.10.1.3 | Описание метода | [sections/149-opisanie-metoda.md](sections/149-opisanie-metoda.md) | 204-206 | ч.1 с.204-206 | 1585 | POST /vpbx/offline_record/recognize |
| 3.10.2 | Загрузка и распознавание речи в WAV-файле без сохранения в ВАТС и без привязки к сотруднику | [sections/150-zagruzka-i-raspoznavanie-rechi-v-wav-fay.md](sections/150-zagruzka-i-raspoznavanie-rechi-v-wav-fay.md) | 206 | ч.1 с.206 | 121 | привязки к сотруднику |
| 3.10.2.1 | Обзор | [sections/151-obzor.md](sections/151-obzor.md) | 206-207 | ч.1 с.206-207 | 488 | Метод обеспечивает загрузку в ВАТС и распознавание речи в звуковом файле, при этом |
| 3.10.2.2 | Описание метода | [sections/152-opisanie-metoda.md](sections/152-opisanie-metoda.md) | 207-208 | ч.1 с.207-208 | 825 | POST /vpbx/record/recognize |
| 3.10.3 | Событие о завершении распознавания речи в WAV-файле | [sections/153-sobytie-o-zavershenii-raspoznavaniya-rec.md](sections/153-sobytie-o-zavershenii-raspoznavaniya-rec.md) | 208 | ч.1 с.208 | 462 | POST /events/recognized/offline |
| 3.10.4 | Получение результата распознавания речи в WAV-файле | [sections/154-poluchenie-rezultata-raspoznavaniya-rech.md](sections/154-poluchenie-rezultata-raspoznavaniya-rech.md) | 209-211 | ч.1 с.209-211 | 1134 | POST /vpbx/transcribes/tasks/ |
| 4 | Описание методов API Контакт-центра MANGO OFFICE | [sections/155-opisanie-metodov-api-kontakt-centra-mang.md](sections/155-opisanie-metodov-api-kontakt-centra-mang.md) | 212 | ч.1 с.212 | 75 | — |
| 4.1 | Основное | [sections/156-osnovnoe.md](sections/156-osnovnoe.md) | 212 | ч.1 с.212 | 398 | 1) Этот API позволяет обращаться к некоторым функциям и данными Контакт-центра |
| 4.2 | Подключение и настройка API КЦ | [sections/157-podklyuchenie-i-nastroyka-api-kc.md](sections/157-podklyuchenie-i-nastroyka-api-kc.md) | 213-214 | ч.1 с.213-214 | 569 | Чтобы у вас появилась возможность работы с API КЦ, нужно подключить услугу "Открытое |
| 4.3 | Управление задачей на автоперезвон | [sections/158-upravlenie-zadachey-na-avtoperezvon.md](sections/158-upravlenie-zadachey-na-avtoperezvon.md) | 215 | ч.1 с.215 | 76 | — |
| 4.3.1 | Создание задачи на автоперезвон | [sections/159-sozdanie-zadachi-na-avtoperezvon.md](sections/159-sozdanie-zadachi-na-avtoperezvon.md) | 215-216 | ч.1 с.215-216 | 1327 | POST /cc/task/add |
| 4.3.2 | Изменение задачи на автоперезвон | [sections/160-izmenenie-zadachi-na-avtoperezvon.md](sections/160-izmenenie-zadachi-na-avtoperezvon.md) | 216-218 | ч.1 с.216-218 | 1607 | POST /cc/task/update |
| 4.3.3 | Получение задачи по ID | [sections/161-poluchenie-zadachi-po-id.md](sections/161-poluchenie-zadachi-po-id.md) | 218-219 | ч.1 с.218-219 | 1150 | POST /cc/task/get |
| 4.3.4 | Получение списка задач | [sections/162-poluchenie-spiska-zadach.md](sections/162-poluchenie-spiska-zadach.md) | 220-222 | ч.1 с.220-222 | 1830 | POST /cc/task/list |
| 4.3.5 | Завершение задачи | [sections/163-zavershenie-zadachi.md](sections/163-zavershenie-zadachi.md) | 222 | ч.1 с.222 | 378 | POST /cc/task/done |
| 4.3.6 | Отмена задачи | [sections/164-otmena-zadachi.md](sections/164-otmena-zadachi.md) | 223 | ч.1 с.223 | 377 | POST /cc/task/cancel |
| 4.4 | Управление статусами и сессиями пользователя | [sections/165-upravlenie-statusami-i-sessiyami-polzova.md](sections/165-upravlenie-statusami-i-sessiyami-polzova.md) | 223 | ч.1 с.223 | 75 | — |
| 4.4.1 | Статусы | [sections/166-statusy.md](sections/166-statusy.md) | 223 | ч.1 с.223 | 71 | — |
| 4.4.1.1 | Что означает статус пользователя | [sections/167-chto-oznachaet-status-polzovatelya.md](sections/167-chto-oznachaet-status-polzovatelya.md) | 223-224 | ч.1 с.223-224 | 461 | Статус - это атрибут пользователя, который определяет его готовность к приему вызовов. |
| 4.4.1.2 | Коды статусов | [sections/168-kody-statusov.md](sections/168-kody-statusov.md) | 224 | ч.1 с.224 | 227 | Здесь перечислены коды статусов пользователей, которые можно использовать при запросах |
| 4.4.1.3 | Смена статуса сессии пользователя | [sections/169-smena-statusa-sessii-polzovatelya.md](sections/169-smena-statusa-sessii-polzovatelya.md) | 224-226 | ч.1 с.224-226 | 1700 | POST /cc/set_session_status |
| 4.4.1.2 | Смена статуса пользователя | [sections/170-smena-statusa-polzovatelya.md](sections/170-smena-statusa-polzovatelya.md) | 226-227 | ч.1 с.226-227 | 622 | POST /cc/set_abonent_status |
| 4.4.1.3 | Статусы пользователей продукта | [sections/171-statusy-polzovateley-produkta.md](sections/171-statusy-polzovateley-produkta.md) | 227-229 | ч.1 с.227-229 | 878 | POST /cc/get_presence |
| 4.4.1.4 | Статусы на продукте | [sections/172-statusy-na-produkte.md](sections/172-statusy-na-produkte.md) | 229-230 | ч.1 с.229-230 | 616 | POST /cc/get_statuses |
| 4.4.2 | События | [sections/173-sobytiya.md](sections/173-sobytiya.md) | 230 | ч.1 с.230 | 69 | — |
| 4.4.2.1 | Изменение статуса пользователя | [sections/174-izmenenie-statusa-polzovatelya.md](sections/174-izmenenie-statusa-polzovatelya.md) | 230 | ч.1 с.230 | 426 | POST /events/user/status_changed |
| 4.4.2.2 | Завершение сессии | [sections/175-zavershenie-sessii.md](sections/175-zavershenie-sessii.md) | 231 | ч.1 с.231 | 384 | POST /events/user/session_end |
| 4.5 | Работа со сделками | [sections/176-rabota-so-sdelkami.md](sections/176-rabota-so-sdelkami.md) | 231 | ч.1 с.231 | 71 | — |
| 4.5.1 | Создание сделки | [sections/177-sozdanie-sdelki.md](sections/177-sozdanie-sdelki.md) | 231-233 | ч.1 с.231-233 | 1392 | POST /cc/deal/create |
| 4.5.2 | Изменение сделки | [sections/178-izmenenie-sdelki.md](sections/178-izmenenie-sdelki.md) | 233-234 | ч.1 с.233-234 | 1289 | POST /cc/deal/update |
| 4.5.3 | Получение сделки по ID | [sections/179-poluchenie-sdelki-po-id.md](sections/179-poluchenie-sdelki-po-id.md) | 235-236 | ч.1 с.235-236 | 1264 | POST /cc/deal/get |
| 4.5.4 | Получение списка сделок | [sections/180-poluchenie-spiska-sdelok.md](sections/180-poluchenie-spiska-sdelok.md) | 236-239 | ч.1 с.236-239 | 2111 | POST /cc/deal/list |
| 4.5.5 | Получение списка пользовательских полей | [sections/181-poluchenie-spiska-polzovatelskih-poley.md](sections/181-poluchenie-spiska-polzovatelskih-poley.md) | 239-242 | ч.1 с.239-242 | 1355 | POST /cc/deal/custom_fields.list |
| 4.5.6 | Получение списка документов сделки | [sections/182-poluchenie-spiska-dokumentov-sdelki.md](sections/182-poluchenie-spiska-dokumentov-sdelki.md) | 242-243 | ч.1 с.242-243 | 685 | POST /cc/deal/documents.list |
| 4.5.7 | Добавление документов к сделке | [sections/183-dobavlenie-dokumentov-k-sdelke.md](sections/183-dobavlenie-dokumentov-k-sdelke.md) | 243-244 | ч.1 с.243-244 | 617 | POST /cc/deal/documents.add |
| 4.5.8 | Получение списка воронок | [sections/184-poluchenie-spiska-voronok.md](sections/184-poluchenie-spiska-voronok.md) | 244-245 | ч.1 с.244-245 | 974 | POST /cc/deal/funnels.list |
| 4.6 | Кампании исходящего обзвона | [sections/185-kampanii-ishodyaschego-obzvona.md](sections/185-kampanii-ishodyaschego-obzvona.md) | 246 | ч.1 с.246 | 77 | — |
| 4.6.1 | Общее | [sections/186-obschee.md](sections/186-obschee.md) | 246 | ч.1 с.246 | 153 | Возможности API КЦ, указанные в данном разделе, служат для управления кампаниями ИО и |
| 4.6.2 | Получение списка задач и подзадач кампаний | [sections/187-poluchenie-spiska-zadach-i-podzadach-kam.md](sections/187-poluchenie-spiska-zadach-i-podzadach-kam.md) | 246-250 | ч.1 с.246-250 | 3205 | POST /vpbx/v2/campaign/tasks |
| 4.6.3 | Получение списка кампаний ИО | [sections/188-poluchenie-spiska-kampaniy-io.md](sections/188-poluchenie-spiska-kampaniy-io.md) | 250-259 | ч.1 с.250-259 | 6323 | POST /vpbx/campaign/list |
| 4.6.4 | Получение информации о кампании | [sections/189-poluchenie-informacii-o-kampanii.md](sections/189-poluchenie-informacii-o-kampanii.md) | 259-264 | ч.1 с.259-264 | 4806 | POST /vpbx/campaign |
| 4.6.4 | Важная информация | [sections/190-vazhnaya-informaciya.md](sections/190-vazhnaya-informaciya.md) | 264 | ч.1 с.264 | 401 | При создании кампании ИО необходимо использовать данные о: |
| 4.6.4 | Описание запроса на создание кампании ИО | [sections/191-opisanie-zaprosa-na-sozdanie-kampanii-io.md](sections/191-opisanie-zaprosa-na-sozdanie-kampanii-io.md) | 264-268 | ч.1 с.264-268 | 4200 | POST /vpbx/campaign/add |
| 4.6.6 | Обновление кампании | [sections/192-obnovlenie-kampanii.md](sections/192-obnovlenie-kampanii.md) | 268-271 | ч.1 с.268-271 | 4114 | POST /vpbx/campaign/update |
| 4.6.7 | Добавление нескольких заданий в кампанию (асинхронный метод) | [sections/193-dobavlenie-neskolkih-zadaniy-v-kampaniyu.md](sections/193-dobavlenie-neskolkih-zadaniy-v-kampaniyu.md) | 272-274 | ч.1 с.272-274 | 1666 | POST /vpbx/tasks/push |
| 4.6.8 | Добавление одного задания в кампанию (синхронный метод) | [sections/194-dobavlenie-odnogo-zadaniya-v-kampaniyu-s.md](sections/194-dobavlenie-odnogo-zadaniya-v-kampaniyu-s.md) | 274-275 | ч.1 с.274-275 | 1539 | POST /vpbx/task/add |
| 4.6.9 | Запуск кампании | [sections/195-zapusk-kampanii.md](sections/195-zapusk-kampanii.md) | 276 | ч.1 с.276 | 406 | POST /vpbx/campaign/start |
| 4.6.10 | Остановка кампании | [sections/196-ostanovka-kampanii.md](sections/196-ostanovka-kampanii.md) | 276-277 | ч.1 с.276-277 | 506 | POST /vpbx/campaign/stop |
| 4.6.11 | Удаление кампании | [sections/197-udalenie-kampanii.md](sections/197-udalenie-kampanii.md) | 277 | ч.1 с.277 | 448 | POST /vpbx/campaign/delete |
| 4.6.12 | Получение информации для генерации отчёта исходящего обзвона | [sections/198-poluchenie-informacii-dlya-generacii-otc.md](sections/198-poluchenie-informacii-dlya-generacii-otc.md) | 278-281 | ч.1 с.278-281 | 2631 | POST /vpbx/campaign-report/create |
| 4.6.13 | Получение информации о задаче кампании ИО | [sections/199-poluchenie-informacii-o-zadache-kampanii.md](sections/199-poluchenie-informacii-o-zadache-kampanii.md) | 282-284 | ч.1 с.282-284 | 2523 | POST /vpbx/task |
| 4.6.14 | Запуск задания кампании ИО | [sections/200-zapusk-zadaniya-kampanii-io.md](sections/200-zapusk-zadaniya-kampanii-io.md) | 284-285 | ч.1 с.284-285 | 330 | POST /vpbx/task/start |
| 4.6.15 | Остановка задания | [sections/201-ostanovka-zadaniya.md](sections/201-ostanovka-zadaniya.md) | 285 | ч.1 с.285 | 394 | POST /vpbx/task/stop |
| 4.6.16 | Удаление задания | [sections/202-udalenie-zadaniya.md](sections/202-udalenie-zadaniya.md) | 285-286 | ч.1 с.285-286 | 327 | POST /vpbx/task/delete |
| 4.6.17 | Обновление задания кампании ИО | [sections/203-obnovlenie-zadaniya-kampanii-io.md](sections/203-obnovlenie-zadaniya-kampanii-io.md) | 286-287 | ч.1 с.286-287 | 691 | POST /vpbx/task/update |
| 4.6.18 | Получение информации о завершенных заданиях кампании ИО | [sections/204-poluchenie-informacii-o-zavershennyh-zad.md](sections/204-poluchenie-informacii-o-zavershennyh-zad.md) | 287 | ч.1 с.287 | 86 | — |
| 4.6.18 | Важная информация | [sections/205-vazhnaya-informaciya.md](sections/205-vazhnaya-informaciya.md) | 287 | ч.1 с.287 | 298 | Этот метод позволяет получить информацию о завершенных заданиях кампании исходящего |
| 4.6.18 | Описание метода | [sections/206-opisanie-metoda.md](sections/206-opisanie-metoda.md) | 287-290 | ч.1 с.287-290 | 2575 | POST /vpbx/tasks/finished |
| 4.6.19 | Сброс попыток выполнения задания кампании ИО | [sections/207-sbros-popytok-vypolneniya-zadaniya-kampa.md](sections/207-sbros-popytok-vypolneniya-zadaniya-kampa.md) | 291 | ч.1 с.291 | 367 | POST /vpbx/tasks/reset |
| 4.6.20 | Получение списка пользовательских полей | [sections/208-poluchenie-spiska-polzovatelskih-poley.md](sections/208-poluchenie-spiska-polzovatelskih-poley.md) | 291-292 | ч.1 с.291-292 | 763 | POST /vpbx/custom-type/list |
| 4.7 | Данные Контакт-центра для звонка | [sections/209-dannye-kontakt-centra-dlya-zvonka.md](sections/209-dannye-kontakt-centra-dlya-zvonka.md) | 292 | ч.1 с.292 | 78 | — |
| 4.7.1 | Получение данных Контакт-центра для звонка | [sections/210-poluchenie-dannyh-kontakt-centra-dlya-zv.md](sections/210-poluchenie-dannyh-kontakt-centra-dlya-zv.md) | 292-296 | ч.1 с.292-296 | 2377 | POST /vpbx/cc/call/ |
| 4.7.2 | Получение списка тематик по продукту | [sections/211-poluchenie-spiska-tematik-po-produktu.md](sections/211-poluchenie-spiska-tematik-po-produktu.md) | 296-298 | ч.1 с.296-298 | 1288 | POST /vpbx/cc/tags/ |
| 4.7.3 | Метод получения информации по скрипту(сценарию) КЦ | [sections/212-metod-polucheniya-informacii-po-skriptu.md](sections/212-metod-polucheniya-informacii-po-skriptu.md) | 298-299 | ч.1 с.298-299 | 689 | POST /vpbx/script/ |
| 4.7.4 | Вопрос для оценки качества работы операторов по обработке вызовов | [sections/213-vopros-dlya-ocenki-kachestva-raboty-oper.md](sections/213-vopros-dlya-ocenki-kachestva-raboty-oper.md) | 299-300 | ч.1 с.299-300 | 789 | POST /vpbx/quality/control/question/ |
| 4.8 | Работа с обращениями в Контакт-центре | [sections/214-rabota-s-obrascheniyami-v-kontakt-centre.md](sections/214-rabota-s-obrascheniyami-v-kontakt-centre.md) | 300 | ч.1 с.300 | 81 | — |
| 4.8.1 | Общее | [sections/215-obschee.md](sections/215-obschee.md) | 300 | ч.1 с.300 | 150 | В этом разделе описаны методы, которые позволяют разово передавать информацию об |
| 4.8.2 | Создание закрытого обращения | [sections/216-sozdanie-zakrytogo-obrascheniya.md](sections/216-sozdanie-zakrytogo-obrascheniya.md) | 301-303 | ч.1 с.301-303 | 1670 | /cc/appeals/create-closed-appeals |
| 4.8.3 | События | [sections/217-sobytiya.md](sections/217-sobytiya.md) | 303 | ч.1 с.303 | 69 | — |
| 4.8.3.1 | Общение закрыто | [sections/218-obschenie-zakryto.md](sections/218-obschenie-zakryto.md) | 303-306 | ч.1 с.303-306 | 2844 | /events/md/onAppealClose |
| 4.9 | Управление задачами | [sections/219-upravlenie-zadachami.md](sections/219-upravlenie-zadachami.md) | 306 | ч.1 с.306 | 68 | — |
| 4.9.1 | Методы | [sections/220-metody.md](sections/220-metody.md) | 306 | ч.1 с.306 | 69 | — |
| 4.9.1.1 | Создание задачи | [sections/221-sozdanie-zadachi.md](sections/221-sozdanie-zadachi.md) | 306-307 | ч.1 с.306-307 | 1472 | POST /cc/task/add |
| 4.9.1.2 | Изменение задачи | [sections/222-izmenenie-zadachi.md](sections/222-izmenenie-zadachi.md) | 308-309 | ч.1 с.308-309 | 1566 | POST /cc/task/update |
| 4.9.1.3 | Получение задачи по ID | [sections/223-poluchenie-zadachi-po-id.md](sections/223-poluchenie-zadachi-po-id.md) | 309-311 | ч.1 с.309-311 | 1163 | POST /cc/task/get |
| 4.9.1.4 | Получение списка задач | [sections/224-poluchenie-spiska-zadach.md](sections/224-poluchenie-spiska-zadach.md) | 311-313 | ч.1 с.311-313 | 1859 | POST /cc/task/list |
| 4.9.1.5 | Завершение задачи | [sections/225-zavershenie-zadachi.md](sections/225-zavershenie-zadachi.md) | 313-314 | ч.1 с.313-314 | 402 | POST /cc/task/done |
| 4.9.1.6 | Отмена задачи | [sections/226-otmena-zadachi.md](sections/226-otmena-zadachi.md) | 314 | ч.1 с.314 | 378 | POST /cc/task/cancel |
| 4.9.2 | События | [sections/227-sobytiya.md](sections/227-sobytiya.md) | 315 | ч.1 с.315 | 69 | — |
| 4.9.2.1 | Задача создана | [sections/228-zadacha-sozdana.md](sections/228-zadacha-sozdana.md) | 315 | ч.1 с.315 | 772 | Событие, вызываемое при создании задачи. |
| 4.9.2.2 | Задача изменена | [sections/229-zadacha-izmenena.md](sections/229-zadacha-izmenena.md) | 315-316 | ч.1 с.315-316 | 761 | Событие, вызываемое при изменении задачи. |
| 4.10 | API Мобильное приложение | [sections/230-api-mobilnoe-prilozhenie.md](sections/230-api-mobilnoe-prilozhenie.md) | 316 | ч.1 с.316 | 70 | — |
| 4.10.1 | Общее | [sections/231-obschee.md](sections/231-obschee.md) | 316 | ч.1 с.316 | 242 | API предназначен для отправки текстовых сообщений, изображений, файлов. |
| 4.10.2 | Методы | [sections/232-metody.md](sections/232-metody.md) | 316 | ч.1 с.316 | 69 | — |
| 4.10.2.1 | Отправка сообщения, либо файла, либо оценки обслуживания | [sections/233-otpravka-soobscheniya-libo-fayla-libo-oc.md](sections/233-otpravka-soobscheniya-libo-fayla-libo-oc.md) | 316-318 | ч.1 с.316-318 | 2009 | POST /cc/send_message |
| 4.10.2.2 | Отправка уведомления о наборе текста | [sections/234-otpravka-uvedomleniya-o-nabore-teksta.md](sections/234-otpravka-uvedomleniya-o-nabore-teksta.md) | 319 | ч.1 с.319 | 477 | POST /cc/user_typing |
| 4.10.2.3 | Отправка уведомления о прочитанном сообщении | [sections/235-otpravka-uvedomleniya-o-prochitannom-soo.md](sections/235-otpravka-uvedomleniya-o-prochitannom-soo.md) | 319-320 | ч.1 с.319-320 | 513 | POST /cc/event_message_read |
| 4.10.2.4 | Отправка уведомления о доставленном сообщении | [sections/236-otpravka-uvedomleniya-o-dostavlennom-soo.md](sections/236-otpravka-uvedomleniya-o-dostavlennom-soo.md) | 320-321 | ч.1 с.320-321 | 522 | POST /cc/event_message_received |
| 4.10.2.5 | Получение истории сообщений | [sections/237-poluchenie-istorii-soobscheniy.md](sections/237-poluchenie-istorii-soobscheniy.md) | 321-323 | ч.1 с.321-323 | 1121 | POST /cc/get_chat_history |
| 4.10.3 | События | [sections/238-sobytiya.md](sections/238-sobytiya.md) | 323 | ч.1 с.323 | 111 | В данном разделе описаны события, отправляемые Контакт-центром MANGO OFFICE в |
| 4.10.3.1 | Общие параметры для каждого события | [sections/239-obschie-parametry-dlya-kazhdogo-sobytiya.md](sections/239-obschie-parametry-dlya-kazhdogo-sobytiya.md) | 323 | ч.1 с.323 | 234 | Перечень общих параметров события: |
| 4.10.3.2 | Отправка сообщения | [sections/240-otpravka-soobscheniya.md](sections/240-otpravka-soobscheniya.md) | 323-324 | ч.1 с.323-324 | 483 | В данном разделе описано событие "Отправка сообщения", отправляемое Контакт-центром |
| 4.10.3.3 | Оповещение о том, что пользователь набирает текст | [sections/241-opoveschenie-o-tom-chto-polzovatel-nabir.md](sections/241-opoveschenie-o-tom-chto-polzovatel-nabir.md) | 324 | ч.1 с.324 | 213 | В данном разделе описано событие "Оповещение о том, что пользователь что-то печатает", |
| 4.10.3.4 | Оповещение о том, что сообщение прочитано | [sections/242-opoveschenie-o-tom-chto-soobschenie-proc.md](sections/242-opoveschenie-o-tom-chto-soobschenie-proc.md) | 324 | ч.1 с.324 | 257 | В данном разделе описано событие "Оповещение о том, что сообщение прочитано", |
| 4.10.3.5 | Оповещение о том, что обращение закрыто и нужно оценить работу оператора | [sections/243-opoveschenie-o-tom-chto-obraschenie-zakr.md](sections/243-opoveschenie-o-tom-chto-obraschenie-zakr.md) | 324-325 | ч.1 с.324-325 | 598 | В данном разделе описано событие, отправляемое Контакт-центром MANGO OFFICE в ваше |
| 4.10.4 | Как найти channelId | [sections/244-kak-nayti-channelid.md](sections/244-kak-nayti-channelid.md) | 325-326 | ч.1 с.325-326 | 622 | Если вы хотите использовать методы для получения сообщений из внешних приложений в |
| — | Список кодов результатов | [sections/245-spisok-kodov-rezultatov.md](sections/245-spisok-kodov-rezultatov.md) | 327-332 | ч.1 с.327-332 | 7338 | Ниже приведен список кодов результатов выполнения команд или запросов, завершения |
| — | Примеры поведения | [sections/246-primery-povedeniya.md](sections/246-primery-povedeniya.md) | 333 | ч.1 с.333 | 61 | — |
| — | Уведомление о вызове | [sections/247-uvedomlenie-o-vyzove.md](sections/247-uvedomlenie-o-vyzove.md) | 333-334 | ч.1 с.333-334 | 508 | Сотрудник ВАТС с внутренним номером "1234" вызывает с номера "74955404444" внешнего |
| — | Инициирование исходящего вызова | [sections/248-iniciirovanie-ishodyaschego-vyzova.md](sections/248-iniciirovanie-ishodyaschego-vyzova.md) | 334-336 | ч.1 с.334-336 | 1194 | Вешняя система отправляет команду инициирования вызова сотрудником ВАТС с внутренним |
| — | Маршрутизация вызова | [sections/249-marshrutizaciya-vyzova.md](sections/249-marshrutizaciya-vyzova.md) | 336-338 | ч.1 с.336-338 | 1144 | Вызов поступает на номер DID 7800123456789, попадает в IVR. |
| — | Перевод вызова с консультацией | [sections/250-perevod-vyzova-s-konsultaciey.md](sections/250-perevod-vyzova-s-konsultaciey.md) | 339-342 | ч.1 с.339-342 | 1513 | Входящий вызов с номера "74955404444" на номер сотрудника ВАТС "12345678" с |
| — | Перевод вызова без консультации | [sections/251-perevod-vyzova-bez-konsultacii.md](sections/251-perevod-vyzova-bez-konsultacii.md) | 342-345 | ч.1 с.342-345 | 1303 | Входящий вызов с номера "74955404444" на номер сотрудника ВАТС "44332211" с |
| — | Обработка нажатий DTMF-клавиш | [sections/252-obrabotka-nazhatiy-dtmf-klavish.md](sections/252-obrabotka-nazhatiy-dtmf-klavish.md) | 345-348 | ч.1 с.345-348 | 1839 | Пример: |
| — | Приложение 1 – Описание поля sip-headers | [sections/253-prilozhenie-1-opisanie-polya-sip-headers.md](sections/253-prilozhenie-1-opisanie-polya-sip-headers.md) | 349 | ч.1 с.349 | 620 | Опциональный параметр, содержащий вложенные SIP заголовки и их значения. |
| — | История документа | [sections/254-istoriya-dokumenta.md](sections/254-istoriya-dokumenta.md) | 350-367 | ч.1 с.350-367 | 13179 | Обновление 06.07.2026 |
| | **ИТОГО** | | | | **261672** | весь документ |

## Источники

- Источник БЗ, часть 1: `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf`
- Стандарт цитирования: [`standards/kb-standard.md`](../../../standards/kb-standard.md), [ADR-007](../../../docs/adr/007-kb-standard.md)
