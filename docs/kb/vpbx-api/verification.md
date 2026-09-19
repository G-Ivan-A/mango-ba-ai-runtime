---
type: kb-verification-report
doc_code: VPBXAPI
source_document: "MangoOffice_VPBX_API_v1.9.pdf"
extraction_date: "2026-08-22"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "requires_review"
pages_covered: "1-367"
status: verified
ai-generated: true
---

# Отчёт перекрёстной проверки — API Mango Office

Метод: cross-engine (pdfplumber -> PyMuPDF re-read of the same pages). Основное извлечение — `pdfplumber 0.11.10`; независимая перепроверка — `PyMuPDF 1.28.2` по тем же страницам источника.

Критический токен — то, что запрещено «додумывать»: имя параметра (`snake_case`), URL, числовой литерал (лимит/порт/таймаут/код ответа), латинская константа или термин. Токен считается подтверждённым, если второй движок видит его на тех же страницах (допуск ±1 страница).

## Итог

| Метрика | Значение |
| --- | ---: |
| Проверено критических токенов | 8749 |
| Не подтверждено вторым движком | 0 |
| Доля подтверждённых | 100.00 % |
| Страниц без текстового слоя | 4 |
| Уровень доверия | **requires_review** |

## Разделы, требующие ручной сверки

| Раздел | Стр. | Не подтверждено | Страницы без текста |
| --- | --- | ---: | --- |
| [Инициирование вызова от имени сотрудника](sections/36-iniciirovanie-vyzova-ot-imeni-sotrudnika.md) | 33-36 | 0 | MangoOffice_VPBX_API_v1.9.pdf:35 |
| [О параметре route](sections/43-o-parametre-route.md) | 46-49 | 0 | MangoOffice_VPBX_API_v1.9.pdf:47 |
| [Перевод вызова](sections/44-perevod-vyzova.md) | 50-55 | 0 | MangoOffice_VPBX_API_v1.9.pdf:52, MangoOffice_VPBX_API_v1.9.pdf:54 |

Точные значения перечислены в самих разделах внутри блоков `<!-- kb-verify:start -->` … `<!-- kb-verify:end -->` с указанием имени PDF и страницы: исходные PDF в репозитории не хранятся, сверка выполняется по локальной копии документа.
