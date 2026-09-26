---
id: vpbx-api-149-opisanie-metoda
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.10.1.3"
pdf_section: "3.10.1.3"
title: "Описание метода"
pdf_heading: "3.10.1.3 Описание метода"
pages: "204-206"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 204-206"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"204-206","global_pages":"204-206"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1585
status: extracted
ai-generated: true
---
# 3.10.1.3. Описание метода

> Трассировка: PDF §3.10.1.3 · сквозные стр. 204-206 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.204-206.

POST /vpbx/offline_record/recognize Параметры:

| № | Параметры |  | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- | --- |
|  | 1 | 2 |  |  |  |
| 1 | file |  |  |  | Звуковой файл должен соответствовать требованиям:<br>- формат *.wav, mp3, mp4, ogg; |

| № | Параметры |  | Тип | Обяза- | Описание |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | - битрейт не ниже 128 кбит/с;<br>- размер файла (не более):<br>100 Мб для wav-файла;<br>30 Мб для файлов *.mp3, *.mp4, *.ogg;<br>до 30 минут (любые);<br>минимум 10кб/сек.<br>- имя файла записано латиницей;<br>- длина имени файла не более 64 символов. |
| 2 | Массив данных json, содержащий следующие параметры |  |  |  |  |
|  |  | user_id | integer | Да | ID абонента |
|  |  | member_id | integer | Нет | Устаревший (deprecated)<br>ID сотрудника. Обязательный, если не передан user_id. |
|  |  | from | string | См. опи-<br>сание | Н омер телефона, с которого звонили.<br>Обязательный, если direction=OUT |
|  |  | to | string | См. опи-<br>сание | Н омер телефона, на который звонили<br>Обязательный, если direction=IN |
|  |  | direction | string | Да | Направление вызова: IN или OUT. |
|  |  | created | string | Да | Дата создания в формате "YYYY-MM-DD HH:MM:SS"<br>(UTC) |
|  |  | member_cha<br>nnel | integer | Да | Канал сотрудника для двухканальных записей: -1 и 1 |
|  |  | diarization | bool | Нет | Признак того, что загружаемая аудиозапись одноканальная и<br>её нужно диаризировать.<br>Значение true нужно устанавливать, если вы передаете<br>одноканльный звуковой файл.<br>Значение false нужно устанавливать, если вы передаете<br>двухканальный звуковой файл.<br>Значение по умолчанию: false. |

В результате обработки запроса, формируются и передаются JSON-данные, содержащие следующие параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | request_id | integer |  | id-номер созданного задания на распознавание речи в загруженном<br>файле.<br>Передается, в случае успешного выполнения запроса. |
| 2 | result |  | Да | Результат выполнения запроса на загрузку звукового файла:<br>1000 - успешное выполнение;<br>3103 - отсутствует обязательный параметр;<br>3104 - параметр передан в неправильном формате;<br>3109 - значение больше ожидаемого (случай, когда размер файла<br>больше ожидаемого);<br>3129 - неверная канальность аудиозаписи (при попытке загрузить<br>одноканальную запись);<br>3300 - объект не существует (member_id или device_code не найдены);<br>5000 - ошибка сервера;<br>5008 - услуга недоступна;<br>5228 - превышен лимит количества сорудников (ограничение<br>составляет 5000 сотрудников). |

Важно! Код HTTP 413 Request Entity Too Large, указывает, что объект, переданный в запросе, больше, чем ограничения метода, то есть POST запрос (данные и файл) больше, чем ограничения метода. Пример успешной обработки запроса. Запрос: curl --request POST \ --url https://app.mango-office.ru/vpbx/offline_record/recognize \ --header 'Content-Type: multipart/form-data; boundary=--- 011000010111000001101001' \ --form vpbx_api_key=123qwerty \ --form sign=123qwerty \ --form 'json={"member_id":"10090397","created":"2022-02-07 14:27:00","member_channel":"-1"}' \ --form 'file=@/home/user/13688577079-503-341774074.wav' Ответ: { "result": 1000, "request_id": 174249520 } Пример некорректного запроса и, в результате, сообщения об ошибке. Запрос: curl --request POST \ --url https://app.mango-office.ru/vpbx/offline_record/recognize \ --header 'Content-Type: multipart/form-data; boundary=--- 011000010111000001101001' \ --form vpbx_api_key=123qwerty \ --form sign=9123qwerty \ --form 'json={"member_id":"123","created":"2022-02-07 14:27:00","member_channel":"b"}' \ --form 'file=@/home/user/13688577079-503-341774074.mp3' Ответ: { "result": 3100, "fields": { "member_id": 3300, "member_channel": 3104, "file": 3104 }}
