---
id: sip-trunk-36-sozdanie-sip-trunk-dlya-fusionpbx-freesw
doc_code: SIPT
doc_title: "SIP TRUNK. Руководство пользователя"
doc_version: "1.23.43"
section: "7.2"
pdf_section: "7.2"
title: "Создание SIP trunk для FusionPBX (Freeswitch)"
pdf_heading: "7.2. Создание SIP trunk для FusionPBX (Freeswitch)"
pages: "38-40"
source: kb/sources/sip-trunk/MO_SIP_Trunk.pdf
source_part: "1"
source_pages: "ч.1: 38-40"
source_refs: '[{"source_pdf":"kb/sources/sip-trunk/MO_SIP_Trunk.pdf","part":1,"pages":"38-40","global_pages":"38-40"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 439
status: extracted
ai-generated: true
---
# 7.2. Создание SIP trunk для FusionPBX (Freeswitch)

> Трассировка: PDF §7.2 · сквозные стр. 38-40 · источники: ч.1 `kb/sources/sip-trunk/MO_SIP_Trunk.pdf` с.38-40.

Откройте меню администрирования транков во вкладке Gateways раздела Accounts.

![Изображение, стр. 38](../images/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw-1.png)

![Изображение, стр. 39](../images/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw-2.png)

Для добавления нового транка нажмите пиктограмму “+”.

![Изображение, стр. 39](../images/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw-3.png)

![Изображение, стр. 39](../images/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw-4.png)

В открывшейся форме необходимо заполнить поля: Gateway – имя транка. В примере используем имя mango.

![Изображение, стр. 40](../images/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw-5.png)

Username, Password- обязательные поля заполняются любыми значениями Proxy- SIP сервер провайдера Register – выставляем false Context - по умолчанию Public Profile - по умолчанию External Enabled - True Сохраните введенные данные кнопкой Save.

![Изображение, стр. 40](../images/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw-6.png)
