---
type: kb-source-index
doc_code: LKSSO
doc_title: "Аутентификация и авторизация в рамках SSO"
doc_version: "1.0"
status: extracted
ai-generated: true
source_document: "MANGO_OFFICE_LK_VATS_Auth_SSO.pdf"
extraction_date: "2026-08-22"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "high"
pages_covered: "1-22"
---

# Аутентификация и авторизация в рамках SSO — индекс БЗ (карта разделов)

> Источник: `kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf` · извлечено: pdfplumber 0.11.10 ·
> токены: tiktoken:cl100k_base. Это **карта поиска** для агента (замена
> retrieval-шага до RAG, ADR-007 R2): найди раздел по колонке «Когда
> обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия **high**. Неоднозначности помечены в разделах маркерами `❓ ТРЕБУЕТСЯ ПРОВЕРКА` / `⚠️ ПРОБЕЛ ИЗВЛЕЧЕНИЯ` с точной ссылкой «PDF + страница».

## Как цитировать

`[LKSSO, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `kb/processed/<doc>/sections/<file>#<якорь>` (ADR-007 R3).

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-2 | ч.1 с.1-2 | 188 | Аутентификация и |
| — | Содержание                                                  v2 | 13.03.2026 | [sections/01-soderzhanie-v2-13-03-2026.md](sections/01-soderzhanie-v2-13-03-2026.md) | 2-3 | ч.1 с.2-3 | 409 | Содержание |
| 1 | Термины и определения | [sections/02-terminy-i-opredeleniya.md](sections/02-terminy-i-opredeleniya.md) | 3-4 | ч.1 с.3-4 | 609 | Keycloak – средство управления доступом и идентификации с открытым исходным |
| 2 | Общие сведения | [sections/03-obschie-svedeniya.md](sections/03-obschie-svedeniya.md) | 4-5 | ч.1 с.4-5 | 742 | Технология единого входа (Single sign-on SSO) — метод аутентификации, который |
| 3 | Настройка IdP в ЛК ВАТС MANGO OFFICE | [sections/04-nastroyka-idp-v-lk-vats-mango-office.md](sections/04-nastroyka-idp-v-lk-vats-mango-office.md) | 5-6 | ч.1 с.5-6 | 383 | Для использования возможности авторизации через SSO в Личном кабинете ВАТС |
| 4 | Добавление провайдера | [sections/05-dobavlenie-provaydera.md](sections/05-dobavlenie-provaydera.md) | 6 | ч.1 с.6 | 67 | — |
| 4 | Шаг 1. Настройка Identity-провайдера (IdP). | [sections/06-shag-1-nastroyka-identity-provaydera-idp.md](sections/06-shag-1-nastroyka-identity-provaydera-idp.md) | 6-8 | ч.1 с.6-8 | 1552 | ШАГ 1. |
| 4 | Шаг 2. Сопоставление полей | [sections/07-shag-2-sopostavlenie-poley.md](sections/07-shag-2-sopostavlenie-poley.md) | 8-12 | ч.1 с.8-12 | 2146 | ШАГ 2. |
| 5 | Вход сотрудника в Личный кабинет ВАТС | [sections/08-vhod-sotrudnika-v-lichnyy-kabinet-vats.md](sections/08-vhod-sotrudnika-v-lichnyy-kabinet-vats.md) | 12-13 | ч.1 с.12-13 | 610 | После перехода сотрудника по ссылке, полученной на вкладке Данные Service- |
| 6 | Настройка аутентификации и авторизации на примере Keycloak | [sections/09-nastroyka-autentifikacii-i-avtorizacii-n.md](sections/09-nastroyka-autentifikacii-i-avtorizacii-n.md) | 13-22 | ч.1 с.13-22 | 3366 | примере Keycloak |
| | **ИТОГО** | | | | **10072** | весь документ |

## Источники

- Источник БЗ, часть 1: `kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf`
- Стандарт цитирования: [`standards/kb-standard.md`](../../../standards/kb-standard.md), [ADR-007](../../../docs/adr/007-kb-standard.md)
