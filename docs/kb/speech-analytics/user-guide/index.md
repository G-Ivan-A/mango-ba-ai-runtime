---
product_taxonomy_ref: taxonomy/products.yaml#classes
product_ids: [analytics-reporting]
type: kb-source-index
doc_code: SA
doc_title: "Руководство пользователя. Речевая аналитика"
doc_version: "1.26.42"
status: extracted
ai-generated: true
source_document: "RECHEVAYA-ANALITIKA_1.26.42.pdf"
extraction_date: "2026-11-01"
model_used: "PyMuPDF 1.28.2 + pdfplumber 0.11.10 + tesseract OCR (rus+eng)"
confidence_level: "high"
pages_covered: "1-129"
---

# Руководство пользователя. Речевая аналитика — индекс БЗ (карта разделов)

> Источник: руководство v1.26.42, `kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_1.26.42.pdf` (129 стр.). Исходный PDF в репозитории
> не хранится (хранение — на АРМ пользователя). Токены: tiktoken:cl100k_base. Это **карта поиска**
> для агента (ADR-007 R2): найди раздел по колонке «Когда обращаться», открой только его файл,
> процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md). Отбор и
> оптимизация изображений: [`IMAGES.md`](IMAGES.md).

## Как цитировать

`[SA, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `docs/kb/speech-analytics/user-guide/sections/<file>#<якорь>` (ADR-007 R3).

## Иллюстрации

Каждая содержательная иллюстрация в разделе сопровождается блоком
`> **Описание иллюстрации SA-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста
руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.
OCR-текст — вспомогательный: факты цитируются по тексту руководства.

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-4 | ч.1 с.1-4 | 1548 | 1. Общие сведения......................................................................... |
| 1 | Общие сведения | [sections/01-obschie-svedeniya.md](sections/01-obschie-svedeniya.md) | 4-6 | ч.1 с.4-6 | 1819 | Речевая аналитика распознает записанные разговоры и текстовые сообщения, и производит в ни |
| 2 | Подключение услуги «Речевая аналитика» | [sections/02-podklyuchenie-uslugi-rechevaya-analitika.md](sections/02-podklyuchenie-uslugi-rechevaya-analitika.md) | 6 | ч.1 с.6 | 34 | 2.1. Подключение в Демо-режиме |
| 2.1 | Подключение в демо-режиме | [sections/03-podklyuchenie-v-demo-rezhime.md](sections/03-podklyuchenie-v-demo-rezhime.md) | 6-9 | ч.1 с.6-9 | 3494 | Функционал демо-версии услуги Речевая аналитика полностью соответствует функционалу полной |
| 2.2 | Подключение услуги в платном режиме | [sections/04-podklyuchenie-uslugi-v-platnom-rezhime.md](sections/04-podklyuchenie-uslugi-v-platnom-rezhime.md) | 9-11 | ч.1 с.9-11 | 1898 | Для подключения услуги "Речевая аналитика" последовательно перейдите в подраздел Речевая а |
| 3 | Настройки | [sections/05-nastroyki.md](sections/05-nastroyki.md) | 11-12 | ч.1 с.11-12 | 2225 | Вкладка Настройки модуля Речевая аналитика содержит блок онбординга, а также следующие бло |
| 3.1 | Шаги онбординга | [sections/06-shagi-onbordinga.md](sections/06-shagi-onbordinga.md) | 12-14 | ч.1 с.12-14 | 1662 | В верхней части вкладки Настройки модуля находится блок онбординга, содержащего все этапы  |
| 3.2 | Настройки распознавания записей | [sections/07-nastroyki-raspoznavaniya-zapisey.md](sections/07-nastroyki-raspoznavaniya-zapisey.md) | 14-15 | ч.1 с.14-15 | 1797 | Блок Настройка распознавания записей позволяет настроить функции распознавания и пересылки |
| 3.3 | Аналитика текстовых коммуникаций | [sections/08-analitika-tekstovyh-kommunikaciy.md](sections/08-analitika-tekstovyh-kommunikaciy.md) | 15-17 | ч.1 с.15-17 | 1114 | Раздел доступен только при подключенной услуге «Диалоги» (омниканальные коммуникации). Есл |
| 3.4 | ИИ Инструменты | [sections/09-ii-instrumenty.md](sections/09-ii-instrumenty.md) | 17 | ч.1 с.17 | 50 | В настоящее время подключение ИИ Инструментов доступно бесплатно. Срок действия данной опц |
| 3.4.1 | ИИ Конспекты | [sections/10-ii-konspekty.md](sections/10-ii-konspekty.md) | 17-19 | ч.1 с.17-19 | 2530 | Блок ИИ Конспекты позволяет автоматически формировать краткое содержание телефонных разгов |
| 3.4.2 | ИИ Тегирование | [sections/11-ii-tegirovanie.md](sections/11-ii-tegirovanie.md) | 19-20 | ч.1 с.19-20 | 1002 | Блок ИИ Тегирование позволяет настроить анализ разговоров и чатов сотрудников с использова |
| 3.4.3 | ИИ Помощники | [sections/12-ii-pomoschniki.md](sections/12-ii-pomoschniki.md) | 20-28 | ч.1 с.20-28 | 8166 | 3.4.3.1 Что это такое и зачем нужно |
| 3.5 | Дополнительные настройки | [sections/13-dopolnitelnye-nastroyki.md](sections/13-dopolnitelnye-nastroyki.md) | 28-29 | ч.1 с.28-29 | 1328 | Блок Дополнительные настройки позволяет пользователю управлять расширенными функциями обра |
| 3.6 | Отключение услуги | [sections/14-otklyuchenie-uslugi.md](sections/14-otklyuchenie-uslugi.md) | 29-30 | ч.1 с.29-30 | 986 | При необходимости пользователь может отключить услугу Речевая аналитика. Для этого в разде |
| 4 | Как работает поиск по разговорам | [sections/15-kak-rabotaet-poisk-po-razgovoram.md](sections/15-kak-rabotaet-poisk-po-razgovoram.md) | 30 | ч.1 с.30 | 135 | Пользователям ВАТС доступен поиск ключевых слов или словосочетаний в распознанных аудиозап |
| 4.1 | Термины и определения | [sections/16-terminy-i-opredeleniya.md](sections/16-terminy-i-opredeleniya.md) | 30-32 | ч.1 с.30-32 | 2039 | Канал – участник разговора, речь/текст которого анализируется. Пользователь может выбрать  |
| 4.2 | Правила обработки поисковых запросов | [sections/17-pravila-obrabotki-poiskovyh-zaprosov.md](sections/17-pravila-obrabotki-poiskovyh-zaprosov.md) | 32-33 | ч.1 с.32-33 | 679 | При вводе терм допускается использование следующих символов: |
| 4.3 | Общие советы для составления поисковых запросов | [sections/18-obschie-sovety-dlya-sostavleniya-poiskov.md](sections/18-obschie-sovety-dlya-sostavleniya-poiskov.md) | 33 | ч.1 с.33 | 731 | СОВЕТ 1: При составлении поискового запроса используйте синонимы. |
| 5 | Поиск по аудиозаписям разговоров | [sections/19-poisk-po-audiozapisyam-razgovorov.md](sections/19-poisk-po-audiozapisyam-razgovorov.md) | 33-34 | ч.1 с.33-34 | 0 | — |
| 5.1 | Поля формы модуля поиска в записях разговоров | [sections/20-polya-formy-modulya-poiska-v-zapisyah-ra.md](sections/20-polya-formy-modulya-poiska-v-zapisyah-ra.md) | 34-36 | ч.1 с.34-36 | 4647 | Во вкладке «Записанные разговоры» раздела Запись разговоров ЛК ВАТС можно просмотреть и от |
| 5.2 | Прослушивание записей | [sections/21-proslushivanie-zapisey.md](sections/21-proslushivanie-zapisey.md) | 36-41 | ч.1 с.36-41 | 13200 | Для прослушивания записи следует нажать на иконку напротив наименования нужной записи. |
| 6 | Тегирование разговоров | [sections/22-tegirovanie-razgovorov.md](sections/22-tegirovanie-razgovorov.md) | 41 | ч.1 с.41 | 504 | Разговор – текстовый или аудио диалог сотрудника и клиента, сотрудника и сотрудника. |
| 6.1 | Тематики | [sections/23-tematiki.md](sections/23-tematiki.md) | 41-42 | ч.1 с.41-42 | 1843 | Рабочая область вкладки «Тематики» содержит: |
| 6.2 | Создание и редактирование тематик | [sections/24-sozdanie-i-redaktirovanie-tematik.md](sections/24-sozdanie-i-redaktirovanie-tematik.md) | 42-43 | ч.1 с.42-43 | 456 | Чтобы добавить новую тематику, перейдите на вкладку Тематики модуля Речевая аналитика и ще |
| 6.2.1 | Ключевые слова | [sections/25-klyuchevye-slova.md](sections/25-klyuchevye-slova.md) | 43-45 | ч.1 с.43-45 | 2753 | Блок ключевых слов содержит следующие поля: |
| 6.2.2 | Расширенные настройки | [sections/26-rasshirennye-nastroyki.md](sections/26-rasshirennye-nastroyki.md) | 45-46 | ч.1 с.45-46 | 1953 | Блок добавления условий содержит следующие поля: |
| 6.2.3 | Настройка уведомлений | [sections/27-nastroyka-uvedomleniy.md](sections/27-nastroyka-uvedomleniy.md) | 46-48 | ч.1 с.46-48 | 1793 | При добавлении тематики пользователь задает ряд условий. Если срабатывают все заданные усл |
| 6.3 | Советы по настройке тематик | [sections/28-sovety-po-nastroyke-tematik.md](sections/28-sovety-po-nastroyke-tematik.md) | 48-51 | ч.1 с.48-51 | 2191 | Лучше создать несколько узконаправленных тематик, нежели одну общую. |
| 6.4 | Примеры использования тематики | [sections/29-primery-ispolzovaniya-tematiki.md](sections/29-primery-ispolzovaniya-tematiki.md) | 51 | ч.1 с.51 | 439 | Пример 1. Тематика “Информирование о спецпредложении” |
| 6.5 | Предустановленные тематики | [sections/30-predustanovlennye-tematiki.md](sections/30-predustanovlennye-tematiki.md) | 51-53 | ч.1 с.51-53 | 1733 | По умолчанию в Речевой аналитике включены 36 предустановленных тематик: |
| 6.6 | Заявки на улучшение качества распознавания | [sections/31-zayavki-na-uluchshenie-kachestva-raspozn.md](sections/31-zayavki-na-uluchshenie-kachestva-raspozn.md) | 53-56 | ч.1 с.53-56 | 3267 | Пользователь, который выбрал для распознавания технологию 3iTech, может отправить заявку н |
| 6.7 | ИИ Тематики | [sections/32-ii-tematiki.md](sections/32-ii-tematiki.md) | 56-59 | ч.1 с.56-59 | 2265 | Модуль Речевая аналитика поддерживает семантический анализ разговоров на основе запросов к |
| 7 | Текстовые коммуникации | [sections/33-tekstovye-kommunikacii.md](sections/33-tekstovye-kommunikacii.md) | 59 | ч.1 с.59 | 0 | — |
| 7.1 | Список текстовых коммуникаций | [sections/34-spisok-tekstovyh-kommunikaciy.md](sections/34-spisok-tekstovyh-kommunikaciy.md) | 59-61 | ч.1 с.59-61 | 2680 | При переходе на страницу «Текстовые коммуникации» отображается панель фильтров. На панели  |
| 7.2 | Конспекты чатов | [sections/35-konspekty-chatov.md](sections/35-konspekty-chatov.md) | 61 | ч.1 с.61 | 254 | Если в настройках Речевой аналитики включена услуга ИИ Конспекты, в списке текстовых комму |
| 7.3 | Метки на осциллограмме диалога | [sections/36-metki-na-oscillogramme-dialoga.md](sections/36-metki-na-oscillogramme-dialoga.md) | 61-62 | ч.1 с.61-62 | 4099 | Для отображения результатов поиска в текстовых сообщениях используется осциллограмма диало |
| 7.4 | Плеер чата | [sections/37-pleer-chata.md](sections/37-pleer-chata.md) | 62-63 | ч.1 с.62-63 | 237 | Правая часть плеера с расшифровкой чата устроена аналогично плееру для звонков и содержит  |
| 8 | Отчеты | [sections/38-otchety.md](sections/38-otchety.md) | 63 | ч.1 с.63 | 200 | Вкладка Отчеты содержит детальную аналитическую информацию о распознанных вызовах в соотве |
| 8.1 | Мои отчеты | [sections/39-moi-otchety.md](sections/39-moi-otchety.md) | 63-64 | ч.1 с.63-64 | 1807 | Страница Мои отчеты – главный экран отчетов Речевой аналитики. На ней собраны ключевые пок |
| 8.2 | Расходы Речевой аналитики | [sections/40-rashody-rechevoy-analitiki.md](sections/40-rashody-rechevoy-analitiki.md) | 64-67 | ч.1 с.64-67 | 1637 | Страница расходов помогает быстро понять, сколько стоит использование сервиса за выбранный |
| 8.3 | Анализ сотрудников | [sections/41-analiz-sotrudnikov.md](sections/41-analiz-sotrudnikov.md) | 67 | ч.1 с.67 | 75 | Отчет Анализ сотрудников состоит из трех блоков: |
| 8.3.1 | Блок фильтров | [sections/42-blok-filtrov.md](sections/42-blok-filtrov.md) | 67-69 | ч.1 с.67-69 | 3914 | Кнопка Сохранить – становится активной после формирования отчета. При нажатии отображается |
| 8.3.2 | Блок визуализации срабатывания тематик | [sections/43-blok-vizualizacii-srabatyvaniya-tematik.md](sections/43-blok-vizualizacii-srabatyvaniya-tematik.md) | 69-71 | ч.1 с.69-71 | 2646 | Отчет предоставляет данные по количеству присвоенных звонкам тематик в разговорах сотрудни |
| 8.3.3 | Блок таблицы Разговоры, детализация | [sections/44-blok-tablicy-razgovory-detalizaciya.md](sections/44-blok-tablicy-razgovory-detalizaciya.md) | 71-74 | ч.1 с.71-74 | 5015 | Табличная часть отчета состоит из трех разделов: |
| 8.3.4 | Детализация разговоров | [sections/45-detalizaciya-razgovorov.md](sections/45-detalizaciya-razgovorov.md) | 74-76 | ч.1 с.74-76 | 2438 | Рассмотрим пример детализации для типа записи разговора: «телефонные разговоры»: |
| 8.4 | Анализ разговоров | [sections/46-analiz-razgovorov.md](sections/46-analiz-razgovorov.md) | 76 | ч.1 с.76 | 377 | Отчет «Анализ разговоров» состоит из двух блоков: Блока таблицы и Блока визуализаций Темат |
| 8.4.1 | Блок фильтров | [sections/47-blok-filtrov.md](sections/47-blok-filtrov.md) | 76-78 | ч.1 с.76-78 | 3263 | Для построения отчета “Анализ разговоров” выберите временной период, срез (день/месяц/год) |
| 8.4.2 | Блок визуализаций | [sections/48-blok-vizualizaciy.md](sections/48-blok-vizualizaciy.md) | 78-80 | ч.1 с.78-80 | 1504 | В поле визуализации “Тематики по словам” отображается: |
| 8.4.3 | Блок таблицы | [sections/49-blok-tablicy.md](sections/49-blok-tablicy.md) | 80-81 | ч.1 с.80-81 | 1992 | Таблица формируется по срезу День/Месяц/Год и заданным пользователем в окне “Показатели” п |
| 8.4.4 | Детализация | [sections/50-detalizaciya.md](sections/50-detalizaciya.md) | 81-82 | ч.1 с.81-82 | 1713 | По клику на цифру "Количество распознанных разговоров" открывается окно детализации разгов |
| 8.5 | Анализ по чек-листам | [sections/51-analiz-po-chek-listam.md](sections/51-analiz-po-chek-listam.md) | 82-84 | ч.1 с.82-84 | 2406 | Отчет предназначен для автоматической оценки разговора сотрудника с клиентом на соответств |
| 8.5.1 | Конструктор чек-листов | [sections/52-konstruktor-chek-listov.md](sections/52-konstruktor-chek-listov.md) | 84-90 | ч.1 с.84-90 | 8069 | Возможно создание не более 20-ти чек-листов. |
| 8.5.2 | Статистика | [sections/53-statistika.md](sections/53-statistika.md) | 90-93 | ч.1 с.90-93 | 4460 | Статистика отчета по Чек-листам содержит вкладки «Таблица» и «График», которые позволяют к |
| 8.5.3 | Правила подсчета статистики | [sections/54-pravila-podscheta-statistiki.md](sections/54-pravila-podscheta-statistiki.md) | 93-100 | ч.1 с.93-100 | 10547 | Рассмотрим правила подсчета статистики на примере скриншотов ниже (в числах и процентах): |
| 8.6 | Ловец инсайтов | [sections/55-lovec-insaytov.md](sections/55-lovec-insaytov.md) | 100 | ч.1 с.100 | 144 | Данные отчета позволяют прослеживать – как фраза или тематика разговора повлияла на ход ра |
| 8.6.1 | Блок параметров | [sections/56-blok-parametrov.md](sections/56-blok-parametrov.md) | 100-101 | ч.1 с.100-101 | 1583 | При формировании отчета пользователям доступна фильтрация: |
| 8.6.2 | Блок результатов | [sections/57-blok-rezultatov.md](sections/57-blok-rezultatov.md) | 101-103 | ч.1 с.101-103 | 934 | Блок содержит подробную информацию о срабатывание триггера, с отображением причины и резул |
| 8.7 | Показатели отчетов | [sections/58-pokazateli-otchetov.md](sections/58-pokazateli-otchetov.md) | 103-105 | ч.1 с.103-105 | 2204 | Для построения отчетов устанавливаются показатели, по которым будет формироваться отчет. |
| 9 | Роли и права доступа | [sections/59-roli-i-prava-dostupa.md](sections/59-roli-i-prava-dostupa.md) | 105-106 | ч.1 с.105-106 | 440 | В данном разделе приведено сводное описание параметров доступности, разрешений (прав) и фу |
| 10 | Интеграция Речевой аналитики со сторонними ВАТС | [sections/60-integraciya-rechevoy-analitiki-so-storon.md](sections/60-integraciya-rechevoy-analitiki-so-storon.md) | 106-110 | ч.1 с.106-110 | 1904 | Интеграция виртуальных АТС с сервисом «Речевая аналитика» MANGO OFFICE происходит быстро и |
| 10.1 | Точка входа «Пассивный SIP» | [sections/61-tochka-vhoda-passivnyy-sip.md](sections/61-tochka-vhoda-passivnyy-sip.md) | 110-114 | ч.1 с.110-114 | 4053 | 1) Подключение услуги Речевая аналитика 2) Подключение Пассивного SIP 3) Создание сотрудни |
| 10.2 | Точка входа «Активный SIP» | [sections/62-tochka-vhoda-aktivnyy-sip.md](sections/62-tochka-vhoda-aktivnyy-sip.md) | 114-121 | ч.1 с.114-121 | 6000 | 1) Подключение услуги Речевая аналитика 2) Создание сотрудника 3) Подключение Активного SI |
| 10.3 | Точка входа «DID MANGO OFFICE» | [sections/63-tochka-vhoda-did-mango-office.md](sections/63-tochka-vhoda-did-mango-office.md) | 121-122 | ч.1 с.121-122 | 619 | 1) Подключение услуги Речевая аналитика; 2) Создание сотрудника; |
| 10.4 | Точка входа «SIP Trunk» | [sections/64-tochka-vhoda-sip-trunk.md](sections/64-tochka-vhoda-sip-trunk.md) | 122-127 | ч.1 с.122-127 | 4805 | 1) Добавление SIP Trunk 2) Активация SIP Trunk в карточке сотрудника 3) Настройка схемы ра |
| 10.4.1 | Активация SIP Trunk в карточке сотрудника | [sections/65-aktivaciya-sip-trunk-v-kartochke-sotrudn.md](sections/65-aktivaciya-sip-trunk-v-kartochke-sotrudn.md) | 127 | ч.1 с.127 | 69 | Чтобы установить SIP Trunk для исходящих вызовов конкретного сотрудника, откройте Карточку |
| 10.4.2 | Настройка схемы распределения звонков в Личном кабинете | [sections/66-nastroyka-shemy-raspredeleniya-zvonkov-v.md](sections/66-nastroyka-shemy-raspredeleniya-zvonkov-v.md) | 127-129 | ч.1 с.127-129 | 1626 | Для настройки схемы распределения звонков откройте подраздел “Голосовое меню и распределен |
