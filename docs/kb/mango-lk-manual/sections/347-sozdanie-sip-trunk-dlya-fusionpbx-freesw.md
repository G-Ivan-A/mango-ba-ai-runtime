---
id: mango-lk-manual-347-sozdanie-sip-trunk-dlya-fusionpbx-freesw
doc_code: LK
doc_title: "Виртуальная АТС MANGO OFFICE - Справочник абонента"
doc_version: "1.23"
section: "5.7.2"
pdf_section: "5.7.2"
title: "Создание SIP trunk для FusionPBX (Freeswitch)"
pdf_heading: "5.7.2 Создание SIP trunk для FusionPBX (Freeswitch)"
pages: "559-562"
source: kb/sources/mango-lk-manual/LK_manual_v-123.pdf
source_part: "1"
source_pages: "ч.1: 559-562"
source_refs: '[{"source_pdf":"kb/sources/mango-lk-manual/LK_manual_v-123.pdf","part":1,"pages":"559-562","global_pages":"559-562"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 481
status: extracted
ai-generated: true
---
# 5.7.2. Создание SIP trunk для FusionPBX (Freeswitch)

> Трассировка: PDF §5.7.2 · сквозные стр. 559-562 · источники: ч.1 `kb/sources/mango-lk-manual/LK_manual_v-123.pdf` с.559-562.

Откройте меню администрирования транков во вкладке Gateways раздела Accounts.

![Изображение, стр. 560](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-1.jpeg)

![Изображение, стр. 560](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-2.jpeg)

Для добавления нового транка нажмите пиктограмму “+”.

![Изображение, стр. 560](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-3.png)

![Изображение, стр. 561](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-4.jpeg)

![Изображение, стр. 561](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-5.png)

В открывшейся форме необходимо заполнить поля: Gateway – имя транка. В примере используем имя mango. Username, Password- обязательные поля заполняются любыми значениями Proxy- SIP сервер провайдера Register – выставляем false Context - по умолчанию Public Profile - по умолчанию External Enabled - True

![Изображение, стр. 562](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-6.jpeg)

Сохраните введенные данные кнопкой Save.

![Изображение, стр. 562](../images/347-sozdanie-sip-trunk-dlya-fusionpbx-freesw-7.png)
