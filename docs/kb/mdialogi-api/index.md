---
type: kb-source-index
doc_code: MDAPI
doc_title: "Манго Диалоги. Справочник по API"
doc_version: "10.06.2026"
status: extracted
ai-generated: true
source_document: "Manual_API_Mango_Dialogi.pdf"
extraction_date: "2026-08-25"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "high"
pages_covered: "1-96"
---

# Манго Диалоги. Справочник по API — индекс БЗ (карта разделов)

> Источник: `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf` · извлечено: pdfplumber 0.11.10 ·
> токены: tiktoken:cl100k_base. Это **карта поиска** для агента (замена
> retrieval-шага до RAG, ADR-007 R2): найди раздел по колонке «Когда
> обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия **high**. Неоднозначности помечены в разделах маркерами `❓ ТРЕБУЕТСЯ ПРОВЕРКА` / `⚠️ ПРОБЕЛ ИЗВЛЕЧЕНИЯ` с точной ссылкой «PDF + страница».

## Как цитировать

`[MDAPI, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `kb/processed/<doc>/sections/<file>#<якорь>` (ADR-007 R3).

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-5 | ч.1 с.1-5 | 1729 | Манго Диалоги. |
| — | Определения и сокращения | [sections/01-opredeleniya-i-sokrascheniya.md](sections/01-opredeleniya-i-sokrascheniya.md) | 5-7 | ч.1 с.5-7 | 1045 | API Манго Диалоги (API) – программный интерфейс системы "Манго |
| 1 | О Манго Диалогах | [sections/02-o-mango-dialogah.md](sections/02-o-mango-dialogah.md) | 7 | ч.1 с.7 | 65 | — |
| 1.1 | Общее | [sections/03-obschee.md](sections/03-obschee.md) | 7 | ч.1 с.7 | 268 | Система "Манго Диалоги" (далее по тексту - МД) предоставляет сервис |
| 1.2 | Поддерживаемые каналы коммуникации | [sections/04-podderzhivaemye-kanaly-kommunikacii.md](sections/04-podderzhivaemye-kanaly-kommunikacii.md) | 7-8 | ч.1 с.7-8 | 875 | Каналы коммуникации различаются способом взаимодействия |
| 1.3 | Принцип текстовых коммуникаций с Клиентом при помощи Манго Диалогов | [sections/05-princip-tekstovyh-kommunikaciy-s-kliento.md](sections/05-princip-tekstovyh-kommunikaciy-s-kliento.md) | 8-9 | ч.1 с.8-9 | 855 | помощи Манго Диалогов |
| 1.4 | Основные сущности | [sections/06-osnovnye-suschnosti.md](sections/06-osnovnye-suschnosti.md) | 9-11 | ч.1 с.9-11 | 1390 | В этом параграфе рассказывается об основных сущностях МД и их |
| 2 | Начало работы с API | [sections/07-nachalo-raboty-s-api.md](sections/07-nachalo-raboty-s-api.md) | 11 | ч.1 с.11 | 62 | — |
| 2.1 | Введение в API | [sections/08-vvedenie-v-api.md](sections/08-vvedenie-v-api.md) | 11 | ч.1 с.11 | 186 | Используя API Манго Диалоги (далее по тексту - API), вы можете связать |
| 2.2 | Несколько шагов и можно приступать к работе | [sections/09-neskolko-shagov-i-mozhno-pristupat-k-rab.md](sections/09-neskolko-shagov-i-mozhno-pristupat-k-rab.md) | 11 | ч.1 с.11 | 301 | 1) Прочитайте общие положения о взаимодействии систем. |
| 2.3 | Общие положения о взаимодействии систем | [sections/10-obschie-polozheniya-o-vzaimodeystvii-sis.md](sections/10-obschie-polozheniya-o-vzaimodeystvii-sis.md) | 11 | ч.1 с.11 | 301 | В этом разделе рассказывается о модели взаимодействия вашей |
| 2.3.1 | Модель авторизации | [sections/11-model-avtorizacii.md](sections/11-model-avtorizacii.md) | 11-12 | ч.1 с.11-12 | 467 | API предоставляет внешней системе доступ к своим функциям без |
| 2.3.2 | Модель взаимодействия | [sections/12-model-vzaimodeystviya.md](sections/12-model-vzaimodeystviya.md) | 12-13 | ч.1 с.12-13 | 809 | Внешняя система и API взаимодействуют по протоколу HTTPS. |
| 2.3.3 | Виды запросов | [sections/13-vidy-zaprosov.md](sections/13-vidy-zaprosov.md) | 13-14 | ч.1 с.13-14 | 354 | Запросы между системами условимся разделять на асинхронные и |
| 2.3.4 | Ограничения | [sections/14-ogranicheniya.md](sections/14-ogranicheniya.md) | 14 | ч.1 с.14 | 175 | 1) Не поддерживается протокол TLS версий 1.0, 1.1, 1.3. |
| 2.3.5 | Лимиты количества запросов к API | [sections/15-limity-kolichestva-zaprosov-k-api.md](sections/15-limity-kolichestva-zaprosov-k-api.md) | 14-15 | ч.1 с.14-15 | 549 | В API существуют ограничения на максимальное число запросов в |
| 2.3.6 | Разрешенные IP-адреса | [sections/16-razreshennye-ip-adresa.md](sections/16-razreshennye-ip-adresa.md) | 15-16 | ч.1 с.15-16 | 329 | При подключении API коннектора в настройках Личного кабинета |
| 2.3.7 | Об электронной подписи запросов | [sections/17-ob-elektronnoy-podpisi-zaprosov.md](sections/17-ob-elektronnoy-podpisi-zaprosov.md) | 16 | ч.1 с.16 | 75 | — |
| 2.3.7 | Общее | [sections/18-obschee.md](sections/18-obschee.md) | 16-17 | ч.1 с.16-17 | 459 | Данные, которыми обмениваются системы, как правило, передаются в |
| 2.3.7 | vpbx_api_salt | [sections/19-vpbx-api-salt.md](sections/19-vpbx-api-salt.md) | 17-18 | ч.1 с.17-18 | 579 | Секретный ключ для формирования электронной подписи. |
| 2.4 | Объекты данных | [sections/20-obekty-dannyh.md](sections/20-obekty-dannyh.md) | 18 | ч.1 с.18 | 131 | В данном разделе описаны основные объекты, используемые в API Манго |
| 2.4.1 | Объект Widget | [sections/21-obekt-widget.md](sections/21-obekt-widget.md) | 18-19 | ч.1 с.18-19 | 379 | Объект Widget описывает виджет, настроенный в системе Манго Диалоги. |
| 2.4.2 | Объект Сhannel | [sections/22-obekt-shannel.md](sections/22-obekt-shannel.md) | 19-21 | ч.1 с.19-21 | 1492 | Объект Channel описывает канал коммуникации, входящий в состав |
| 2.4.3 | Объект SocialUser | [sections/23-obekt-socialuser.md](sections/23-obekt-socialuser.md) | 21-23 | ч.1 с.21-23 | 912 | Объект SocialUser содержит информацию о пользователе социальной |
| 2.4.4 | Объект Сhat | [sections/24-obekt-shat.md](sections/24-obekt-shat.md) | 23 | ч.1 с.23 | 185 | — |
| 2.4.5 | Объект Session | [sections/25-obekt-session.md](sections/25-obekt-session.md) | 23-25 | ч.1 с.23-25 | 1087 | Объект Session содержит информацию о сессии коммуникации между |
| 2.4.6 | Объект Message | [sections/26-obekt-message.md](sections/26-obekt-message.md) | 25-26 | ч.1 с.25-26 | 828 | Объект Message описывает сообщение между Клиентом и оператором. |
| 2.4.7 | Объект Button | [sections/27-obekt-button.md](sections/27-obekt-button.md) | 26-27 | ч.1 с.26-27 | 195 | Объект Button описывает кнопку. |
| 3 | Руководство по API | [sections/28-rukovodstvo-po-api.md](sections/28-rukovodstvo-po-api.md) | 27 | ч.1 с.27 | 63 | — |
| 3.1 | Обмен сообщениями в WhatsApp | [sections/29-obmen-soobscheniyami-v-whatsapp.md](sections/29-obmen-soobscheniyami-v-whatsapp.md) | 27 | ч.1 с.27 | 66 | — |
| 3.1.1 | Общее | [sections/30-obschee.md](sections/30-obschee.md) | 27 | ч.1 с.27 | 352 | Если к Вашей Виртуальной АТС подключена услуга "WhatsApp Business |
| 3.1.2 | Доступ к методам | [sections/31-dostup-k-metodam.md](sections/31-dostup-k-metodam.md) | 27-28 | ч.1 с.27-28 | 328 | Вы можете использовать методы, описанные в данном разделе, если |
| 3.1.3 | Получение списка HSM-шаблонов | [sections/32-poluchenie-spiska-hsm-shablonov.md](sections/32-poluchenie-spiska-hsm-shablonov.md) | 28-31 | ч.1 с.28-31 | 1849 | Метод позволяет получить список HSM-шаблонов, имеющих статус |
| 3.1.4 | Отправление HSM | [sections/33-otpravlenie-hsm.md](sections/33-otpravlenie-hsm.md) | 31-34 | ч.1 с.31-34 | 1536 | Метод позволяет отправить Клиенту сообщение в соответствии с тем |
| 3.2 | API управления сессиями | [sections/34-api-upravleniya-sessiyami.md](sections/34-api-upravleniya-sessiyami.md) | 34 | ч.1 с.34 | 67 | — |
| 3.2.1 | Создать новую сессию | [sections/35-sozdat-novuyu-sessiyu.md](sections/35-sozdat-novuyu-sessiyu.md) | 34-36 | ч.1 с.34-36 | 1592 | Если Клиент ранее уже обращался в вашу компанию и у вас есть |
| 3.2.2 | Взять сессию в работу | [sections/36-vzyat-sessiyu-v-rabotu.md](sections/36-vzyat-sessiyu-v-rabotu.md) | 36-38 | ч.1 с.36-38 | 804 | Метод позволяет перевести сессию из статуса "pending" в статус "dialog", |
| 3.2.3 | Перевод сессии на другого сотрудника или группу | [sections/37-perevod-sessii-na-drugogo-sotrudnika-ili.md](sections/37-perevod-sessii-na-drugogo-sotrudnika-ili.md) | 38-41 | ч.1 с.38-41 | 1589 | Этот метод позволяет передать диалог с Клиентом от одного оператора |
| 3.2.4 | Закрыть сессию | [sections/38-zakryt-sessiyu.md](sections/38-zakryt-sessiyu.md) | 41-42 | ч.1 с.41-42 | 645 | Метод позволяет принудительно закрыть сессию в статусе "dialog". |
| 3.2.5 | Отправить сообщение оператора к Клиенту | [sections/39-otpravit-soobschenie-operatora-k-klientu.md](sections/39-otpravit-soobschenie-operatora-k-klientu.md) | 42-45 | ч.1 с.42-45 | 1071 | Метод позволяет отправить Клиенту сообщение от имени оператора. |
| 3.2.6 | Загрузка истории чата | [sections/40-zagruzka-istorii-chata.md](sections/40-zagruzka-istorii-chata.md) | 45-47 | ч.1 с.45-47 | 886 | Метод возвращает массив сообщений, которыми обменивались Клиент |
| 3.3 | API Realtime (вебхуки) | [sections/41-api-realtime-vebhuki.md](sections/41-api-realtime-vebhuki.md) | 47 | ч.1 с.47 | 68 | — |
| 3.3.1 | Сессия в состоянии ожидания | [sections/42-sessiya-v-sostoyanii-ozhidaniya.md](sections/42-sessiya-v-sostoyanii-ozhidaniya.md) | 47-49 | ч.1 с.47-49 | 740 | Данный вебхук отправляется во внешнюю систему после того, как в МД |
| 3.3.2 | Сессия взята в работу | [sections/43-sessiya-vzyata-v-rabotu.md](sections/43-sessiya-vzyata-v-rabotu.md) | 49-51 | ч.1 с.49-51 | 756 | Данный вебхук отправляется во внешнюю систему после того, как |
| 3.3.3 | Сессия закрыта | [sections/44-sessiya-zakryta.md](sections/44-sessiya-zakryta.md) | 51-53 | ч.1 с.51-53 | 769 | Данный вебхук отправляется во внешнюю систему после того, как |
| 3.3.4 | HSM-сообщение оператора прочитано клиентом | [sections/45-hsm-soobschenie-operatora-prochitano-kli.md](sections/45-hsm-soobschenie-operatora-prochitano-kli.md) | 53-54 | ч.1 с.53-54 | 605 | В МД существует возможность отправлять Клиентам HSM-сообщения |
| 3.3.5 | Сообщение оператора не доставлено клиенту | [sections/46-soobschenie-operatora-ne-dostavleno-klie.md](sections/46-soobschenie-operatora-ne-dostavleno-klie.md) | 54-55 | ч.1 с.54-55 | 444 | Данный вебхук отправляется во внешнюю систему в том случае, если |
| 3.3.6 | Сообщение оператора доставлено клиенту | [sections/47-soobschenie-operatora-dostavleno-klientu.md](sections/47-soobschenie-operatora-dostavleno-klientu.md) | 55-56 | ч.1 с.55-56 | 553 | Данный вебхук отправляется во внешнюю систему в том случае, если |
| 3.3.7 | Сообщение оператора прочитано клиентом | [sections/48-soobschenie-operatora-prochitano-kliento.md](sections/48-soobschenie-operatora-prochitano-kliento.md) | 56-57 | ч.1 с.56-57 | 550 | Данный вебхук отправляется во внешнюю систему в том случае, если |
| 3.3.8 | Новое сообщение в чате | [sections/49-novoe-soobschenie-v-chate.md](sections/49-novoe-soobschenie-v-chate.md) | 57-59 | ч.1 с.57-59 | 580 | Данный вебхук отправляется во внешнюю систему, когда Клиент либо оператор |
| 4 | Коды ошибок | [sections/50-kody-oshibok.md](sections/50-kody-oshibok.md) | 59 | ч.1 с.59 | 60 | — |
| 4.1 | Важная информация | [sections/51-vazhnaya-informaciya.md](sections/51-vazhnaya-informaciya.md) | 59 | ч.1 с.59 | 476 | 1. |
| 4.2 | Возможные коды ошибок API | [sections/52-vozmozhnye-kody-oshibok-api.md](sections/52-vozmozhnye-kody-oshibok-api.md) | 59-60 | ч.1 с.59-60 | 335 | В системе Манго Диалоги используются два типа ошибок: |
| 4.2.1 | Коды ошибок ответа API | [sections/53-kody-oshibok-otveta-api.md](sections/53-kody-oshibok-otveta-api.md) | 60-62 | ч.1 с.60-62 | 729 | Манго Диалоги. |
| 4.2.2 | Коды ошибок доставки сообщений | [sections/54-kody-oshibok-dostavki-soobscheniy.md](sections/54-kody-oshibok-dostavki-soobscheniy.md) | 62-65 | ч.1 с.62-65 | 1956 | Манго Диалоги. |
| 4.2.3 | Обработка неизвестных ошибок | [sections/55-obrabotka-neizvestnyh-oshibok.md](sections/55-obrabotka-neizvestnyh-oshibok.md) | 65 | ч.1 с.65 | 144 | Если система получает код ошибки, который отсутствует в реестре, он |
| 4.2.4 | Примечания | [sections/56-primechaniya.md](sections/56-primechaniya.md) | 65-66 | ч.1 с.65-66 | 222 | 1. |
| 5 | Примеры использования API | [sections/57-primery-ispolzovaniya-api.md](sections/57-primery-ispolzovaniya-api.md) | 66 | ч.1 с.66 | 61 | — |
| 5.1 | Прием и обработка обращений Клиента | [sections/58-priem-i-obrabotka-obrascheniy-klienta.md](sections/58-priem-i-obrabotka-obrascheniy-klienta.md) | 66-73 | ч.1 с.66-73 | 3098 | После настройки каналов коммуникации в МД, вы сможете получать |
| 5.2 | Оператор обращается к Клиенту | [sections/59-operator-obraschaetsya-k-klientu.md](sections/59-operator-obraschaetsya-k-klientu.md) | 73-77 | ч.1 с.73-77 | 2160 | Если Клиент ранее уже обращался в вашу компанию по тому или иному |
| 5.3 | Перевод обращения на другого оператора | [sections/60-perevod-obrascheniya-na-drugogo-operator.md](sections/60-perevod-obrascheniya-na-drugogo-operator.md) | 77-80 | ч.1 с.77-80 | 722 | В этом параграфе рассказывается о том, как перевести обработку обращения с |
| 6 | Устаревшие методы API | [sections/61-ustarevshie-metody-api.md](sections/61-ustarevshie-metody-api.md) | 80 | ч.1 с.80 | 176 | Внимание! |
| 6.1 | Отправление каскада сообщений через WhatsApp и SMS | [sections/62-otpravlenie-kaskada-soobscheniy-cherez-w.md](sections/62-otpravlenie-kaskada-soobscheniy-cherez-w.md) | 80 | ч.1 с.80 | 162 | POST /cc/send_text_message |
| 6.1.1 | Правила работы | [sections/63-pravila-raboty.md](sections/63-pravila-raboty.md) | 80-81 | ч.1 с.80-81 | 956 | Чтобы выполнить массовую рассылку, необходимо комплексно |
| 6.1.2 | Ограничения | [sections/64-ogranicheniya.md](sections/64-ogranicheniya.md) | 81-82 | ч.1 с.81-82 | 365 | 1) Текст сообщения (параметр "text") должен быть заключен в кавычки и |
| 6.1.3 | Описание запроса | [sections/65-opisanie-zaprosa.md](sections/65-opisanie-zaprosa.md) | 82-85 | ч.1 с.82-85 | 1390 | Параметры запроса: |
| 6.1.4 | Получить список виджетов | [sections/66-poluchit-spisok-vidzhetov.md](sections/66-poluchit-spisok-vidzhetov.md) | 85-87 | ч.1 с.85-87 | 1016 | Метод возвращает список виджетов МД. |
| 6.1.5 | Получить список активных сессий | [sections/67-poluchit-spisok-aktivnyh-sessiy.md](sections/67-poluchit-spisok-aktivnyh-sessiy.md) | 87-91 | ч.1 с.87-91 | 1637 | Метод возвращает список сессий, находящихся в статусе: |
| 6.2 | Получение статусов отправленных HSM-сообщений | [sections/68-poluchenie-statusov-otpravlennyh-hsm-soo.md](sections/68-poluchenie-statusov-otpravlennyh-hsm-soo.md) | 91-93 | ч.1 с.91-93 | 749 | Метод позволяет получить статус ранее отправленного HSM- |
| — | История документа | [sections/69-istoriya-dokumenta.md](sections/69-istoriya-dokumenta.md) | 93-96 | ч.1 с.93-96 | 2004 | 09.06.2026 |
| | **ИТОГО** | | | | **50413** | весь документ |

## Источники

- Источник БЗ, часть 1: `kb/sources/mdialogi-api/Manual_API_Mango_Dialogi.pdf`
- Стандарт цитирования: [`standards/kb-standard.md`](../../../standards/kb-standard.md), [ADR-007](../../../docs/adr/007-kb-standard.md)
