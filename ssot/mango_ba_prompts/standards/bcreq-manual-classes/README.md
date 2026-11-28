---
status: draft
version: 0.2.2
updated: 2026-11-05
temperature: 0.1
owner: G-Ivan-A
---

# Инвентарь ручных промптов BCREQ

39 классов = 39 отдельных подробных стандартов. Класс определяется целью, обязательными входами и формой результата, а не числом файлов. Повторения одного класса в фазах — экземпляры с одинаковым контрактом. Индекс и общий транспорт не являются дополнительными стандартами классов. Статус всех новых правил — проект.

## Полный реестр

ID операций — `К-NN` (BL-153, issue #430; REC-425-07): префикс `К-` отделяет операцию от кода ошибки прогона `CNN`. Прежний ID — в поле `history.previous_id` [`catalog.json`](catalog.json), промпты на сайте сохраняют его в своём ID (`mango-bcreq-c01-intake`). «Шаг потока» — поле `flow_step` каталога по [RFC #427, раздел 9.2](../../docs/rfc/2026-11-bcreq-flow-processes-prompts.md#92-состав); операции гейтов (К-12, К-13, К-20, К-34, К-39) записаны в шаг, где они стоят в таблице 9.2, и вызываются также на гейтах ([словарь потока](../bcreq-flow-glossary.md)).

| Класс | Назначение / стандарт | Фазы | Шаг потока | Существующий носитель (аналог, не готовая реализация) |
| --- | --- | --- | --- | --- |
| К-01 | [Приём исходного запроса](01-intake.md) | a-in | Ш-А | [bcreq-in-understanding-oneshot.md](../../prompts/bcreq-in-understanding-oneshot.md) |
| К-02 | [Атомарная нормализация](02-normalize.md) | a-in | Ш-1 | [bcreq-context-understanding-stepwise.md](../../prompts/bcreq-context-understanding-stepwise.md) |
| К-03 | [Оценка неоднозначности](03-ambiguity.md) | a-in, a-core, a-work | Ш-1 | [bcreq-context-understanding-stepwise.md](../../prompts/bcreq-context-understanding-stepwise.md) |
| К-04 | [Пакет вопросов](04-questions.md) | a-in, a-core, a-work, a-release | Ш-1 | [bcreq-context-understanding-stepwise.md](../../prompts/bcreq-context-understanding-stepwise.md) |
| К-05 | [Сопоставление с таксономией](05-taxonomy.md) | a-in | Ш-2 | [bcreq-products-impact-analysis-stepwise.md](../../prompts/bcreq-products-impact-analysis-stepwise.md) |
| К-06 | [Границы изменения](06-scope.md) | a-in, a-core, a-work | Ш-2 | [bcreq-products-impact-analysis-stepwise.md](../../prompts/bcreq-products-impact-analysis-stepwise.md) |
| К-07 | [Извлечение из web](07-web-evidence.md) | a-in, a-core, a-work | Ш-2 | [bcreq-products-impact-analysis-stepwise.md](../../prompts/bcreq-products-impact-analysis-stepwise.md) |
| К-08 | [Извлечение из PDF и runtime](08-document-evidence.md) | a-in, a-core, a-work | Ш-2 | [bcreq-products-impact-analysis-stepwise.md](../../prompts/bcreq-products-impact-analysis-stepwise.md) |
| К-09 | [Дообогащение материалами БА](09-ba-enrichment.md) | a-in, a-core, a-work | Ш-1 | [bcreq-in-understanding-oneshot.md](../../prompts/bcreq-in-understanding-oneshot.md) |
| К-10 | [Разрешение конфликтов источников](10-source-conflicts.md) | a-in, a-core, a-work | Ш-В | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |
| К-11 | [Контроль полноты зависимостей](11-dependency-check.md) | a-in, a-core, a-work | Ш-2 | [bcreq-products-impact-analysis-stepwise.md](../../prompts/bcreq-products-impact-analysis-stepwise.md) |
| К-12 | [Полная сборка фазы](12-phase-assembly.md) | a-in, a-core, a-work, a-release | Ш-Р | [bcreq-in-understanding-oneshot.md](../../prompts/bcreq-in-understanding-oneshot.md) |
| К-13 | [Проверка переносимого контекста](13-handoff-check.md) | a-in, a-core, a-work, a-release | Ш-0 | [bcreq-constitution-governance-oneshot.md](../../prompts/bcreq-constitution-governance-oneshot.md) |
| К-14 | [Глоссарий](14-glossary.md) | a-in, a-core, a-work | Ш-1 | [bcreq-context-understanding-stepwise.md](../../prompts/bcreq-context-understanding-stepwise.md) |
| К-15 | [Бизнес-контекст](15-business-context.md) | a-in, a-core, a-work | Ш-1 | [bcreq-context-understanding-stepwise.md](../../prompts/bcreq-context-understanding-stepwise.md) |
| К-16 | [ФТ изменения существующего поведения](16-fr-delta.md) | a-core, a-work | Ш-3 | [bcreq-fr-documentation-stepwise.md](../../prompts/bcreq-fr-documentation-stepwise.md) |
| К-17 | [ФТ нового поведения с нуля](17-fr-new.md) | a-core, a-work | Ш-3 | [bcreq-fr-documentation-stepwise.md](../../prompts/bcreq-fr-documentation-stepwise.md) |
| К-18 | [Нефункциональные требования](18-nfr.md) | a-core, a-work | Ш-4 | [bcreq-nfr-documentation-stepwise.md](../../prompts/bcreq-nfr-documentation-stepwise.md) |
| К-19 | [Первый прогон UC и покрытие ФТ](19-uc-coverage.md) | a-core | Ш-5 | [bcreq-uc-modeling-stepwise.md](../../prompts/bcreq-uc-modeling-stepwise.md) |
| К-20 | [Подготовка доказательств гейта](20-gate-evidence.md) | a-in, a-core, a-work, a-release | Ш-В | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |
| К-21 | [ОРР L1](21-solution-l1.md) | a-work | Ш-6 | [bcreq-orr-solution-design-stepwise.md](../../prompts/bcreq-orr-solution-design-stepwise.md) |
| К-22 | [ОРР L2 и контракты стыков](22-solution-l2.md) | a-work | Ш-6 | [bcreq-orr-solution-design-stepwise.md](../../prompts/bcreq-orr-solution-design-stepwise.md) |
| К-23 | [Особенности и ограничения](23-constraints.md) | a-work | Ш-7 | [bcreq-constraints-documentation-stepwise.md](../../prompts/bcreq-constraints-documentation-stepwise.md) |
| К-24 | [Второй прогон UC и граничные случаи](24-uc-boundaries.md) | a-work | Ш-8 | [bcreq-uc-modeling-stepwise.md](../../prompts/bcreq-uc-modeling-stepwise.md) |
| К-25 | [Анализ рисков](25-risks.md) | a-work | Ш-9 | [bcreq-extra-risk-analysis-stepwise.md](../../prompts/bcreq-extra-risk-analysis-stepwise.md) |
| К-26 | [Реестр зависимостей поставки](26-delivery-dependencies.md) | a-work | Ш-9 | [bcreq-extra-risk-analysis-stepwise.md](../../prompts/bcreq-extra-risk-analysis-stepwise.md) |
| К-27 | [План приёмки](27-acceptance.md) | a-work | Ш-9 | [bcreq-extra-risk-analysis-stepwise.md](../../prompts/bcreq-extra-risk-analysis-stepwise.md) |
| К-28 | [Независимая содержательная проверка](28-independent-review.md) | a-core, a-work, a-release | Ш-В | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |
| К-29 | [Анализ влияния изменения](29-impact.md) | a-core, a-work, a-release | Ш-В | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |
| К-30 | [Адресная правка](30-targeted-edit.md) | a-core, a-work, a-release | Ш-В | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |
| К-31 | [Структурная сверка документа](31-conformance.md) | a-core, a-work, a-release | Ш-Р | [bcreq-core-documentation-oneshot.md](../../prompts/bcreq-core-documentation-oneshot.md) |
| К-32 | [Подготовка пакетов адресатам](32-audience-projection.md) | a-release | Ш-Р | [letter-customer-documentation-legacy.md](../../prompts/letter-customer-documentation-legacy.md) |
| К-33 | [Контроль выпускного комплекта](33-release-audit.md) | a-release | Ш-Р | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |
| К-34 | [Регистрация решений и согласований](34-human-record.md) | a-in, a-core, a-work, a-release | Ш-0 | [bcreq-constitution-governance-oneshot.md](../../prompts/bcreq-constitution-governance-oneshot.md) |
| К-35 | [Фиксация baseline и передача](35-baseline-handover.md) | a-release | Ш-Р | [bcreq-constitution-governance-oneshot.md](../../prompts/bcreq-constitution-governance-oneshot.md) |
| К-36 | [Загрузка правил и параметров чата](36-rule-bundle.md) | a-in, a-core, a-work, a-release | Ш-0 | [bcreq-constitution-governance-oneshot.md](../../prompts/bcreq-constitution-governance-oneshot.md) |
| К-37 | [User Story по запросу БА](37-user-story.md) | a-in, a-core, a-work | Ш-С | [bcreq-scenarios-modeling-oneshot.md](../../prompts/bcreq-scenarios-modeling-oneshot.md) |
| К-38 | [Отдельное моделирование UC по запросу БА](38-requested-uc.md) | a-in, a-core, a-work | Ш-С | [bcreq-scenarios-modeling-oneshot.md](../../prompts/bcreq-scenarios-modeling-oneshot.md) |
| К-39 | [Сверка результата с манифестом задачи](39-manifest-alignment.md) | a-in, a-core, a-work, a-release | Ш-В | [bcreq-review-validation-oneshot.md](../../prompts/bcreq-review-validation-oneshot.md) |

## Последовательности экземпляров

Каждая запись — самостоятельный вставляемый промпт соответствующего класса. БА может повторить его или пропустить при выполненных предпосылках. Вопросы, обновление глоссария, решения и проверки повторяются при изменении входов. Это не автоматические переходы.

### a-in

| Экземпляр | Класс | Обязательный вход | Результат |
| --- | --- | --- | --- |
| a-in/К-36 | Загрузка правил и параметров чата | `full_constitution, applicable_standards, versions, task_parameters, access_receipts` | `rule_receipt{documents,versions,available,missing,precedence}, task_config` |
| a-in/К-01 | Приём исходного запроса | `raw_request, questionnaire?, additional_comments[{text,author_role?}]` | `request_id, raw_verbatim, questionnaire, comments, source_register` |
| a-in/К-02 | Атомарная нормализация | `raw_verbatim, comments, source_register` | `atoms[{id,text,kind,actor,condition,source_id,locator}], ambiguities` |
| a-in/К-03 | Оценка неоднозначности | `atoms, candidate_readings, known_decisions` | `ambiguities[{id,readings,impact,blocking,owner,needed_evidence}], resolved_ids` |
| a-in/К-04 | Пакет вопросов | `ambiguities, missing_evidence, prior_questions, owners` | `questions[{id,text,options,recipient,blocks,deadline,source}], no_repeat_ids` |
| a-in/К-05 | Сопоставление с таксономией | `atoms, taxonomy_snapshot, taxonomy_version` | `matches[{atom_id,domain,capability,feature,atomic_function,status,evidence}], gaps` |
| a-in/К-06 | Границы изменения | `atoms, matches, BA_decisions, adjacent_dependencies` | `in_scope, out_of_scope, context_only, dependencies, owners` |
| a-in/К-07 | Извлечение из web | `source_plan, accessible_page_bodies, URLs, versions` | `claims[{id,feature,verdict,quote,url,heading,version}], coverage, access_gaps` |
| a-in/К-08 | Извлечение из PDF и runtime | `source_plan, attached_documents, runtime_sections?, provenance` | `claims[{id,feature,verdict,quote,document,section,pages?,version}], coverage, gaps` |
| a-in/К-09 | Дообогащение материалами БА | `missing_evidence, BA_raw_materials?, author_roles, provenance` | `enriched_claims, cleaned_fragments, markup, source_links, remaining_gaps` |
| a-in/К-10 | Разрешение конфликтов источников | `claims, versions, source_priorities, BA_decisions` | `conflicts[{id,claims,scope,versions,resolution,authority}], accepted_claims` |
| a-in/К-11 | Контроль полноты зависимостей | `scope, claims, actors, settings, product_links, unresolved` | `dependency_manifest[{id,prerequisite,evidence,status}], retrieval_requests, recommendation` |
| a-in/К-37 | User Story по запросу БА | `explicit_BA_request, atoms, scope, value, FR?` | `stories[{id,role,action,value,acceptance,fr_ids,source}], story_questions` |
| a-in/К-38 | Отдельное моделирование UC по запросу БА | `explicit_BA_request, atoms, scope, actors, FR?` | `requested_UC[{id,actor,precondition,flow,alternatives,result,fr_ids,source}]` |
| a-in/К-14 | Глоссарий | `terms_in_sections_2_to_6, raw_wording, supplied_lexicons` | `section_1[{term,definition,source,lexicon_comparison}], term_questions` |
| a-in/К-15 | Бизнес-контекст | `atoms, scope, business_problem, value, decisions` | `section_2{context,problem,goal,in_scope,out_of_scope,products_owners}` |
| a-in/К-34 | Регистрация решений и согласований | `human_message, actor_role, authority, candidate_revision, scope, timestamp, gate_id?, gate_type?, model_recommendation?` | `section_8_5_record{id,decision,actor,authority,revision,scope,time,evidence,status,gate_id,gate_type,model_recommendation,divergence}` |
| a-in/К-39 | Сверка с манифестом | `baseline_manifest, generated_candidate, authorized_delta, decision_register` | `manifest_diff` |
| a-in/К-12 | Полная сборка фазы | `base_snapshot, ordered_slices, tombstones, source_register, decisions` | `full_snapshot, entity_register, unresolved, superseded, completeness_receipt` |
| a-in/К-13 | Проверка переносимого контекста | `full_snapshot, required_inputs_for_target, source_bodies, rule_bundle` | `handoff_receipt[{input,status,locator}], missing_inputs, recommendation` |
| a-in/К-20 | Подготовка доказательств гейта | `gate_id, gate_type, candidate_revision, applicable_gate_contract, checklist_evidence, human_records` | `gate_report{criteria,evidence,gaps,eligible_for_review,required_actors}, recommendation` |
### a-core

| Экземпляр | Класс | Обязательный вход | Результат |
| --- | --- | --- | --- |
| a-core/К-36 | Загрузка правил и параметров чата | `full_constitution, applicable_standards, versions, task_parameters, access_receipts` | `rule_receipt{documents,versions,available,missing,precedence}, task_config` |
| a-core/К-13 | Проверка переносимого контекста | `full_snapshot, required_inputs_for_target, source_bodies, rule_bundle` | `handoff_receipt[{input,status,locator}], missing_inputs, recommendation` |
| a-core/К-03 | Оценка неоднозначности | `atoms, candidate_readings, known_decisions` | `ambiguities[{id,readings,impact,blocking,owner,needed_evidence}], resolved_ids` |
| a-core/К-04 | Пакет вопросов | `ambiguities, missing_evidence, prior_questions, owners` | `questions[{id,text,options,recipient,blocks,deadline,source}], no_repeat_ids` |
| a-core/К-06 | Границы изменения | `atoms, matches, BA_decisions, adjacent_dependencies` | `in_scope, out_of_scope, context_only, dependencies, owners` |
| a-core/К-07 | Извлечение из web | `source_plan, accessible_page_bodies, URLs, versions` | `claims[{id,feature,verdict,quote,url,heading,version}], coverage, access_gaps` |
| a-core/К-08 | Извлечение из PDF и runtime | `source_plan, attached_documents, runtime_sections?, provenance` | `claims[{id,feature,verdict,quote,document,section,pages?,version}], coverage, gaps` |
| a-core/К-09 | Дообогащение материалами БА | `missing_evidence, BA_raw_materials?, author_roles, provenance` | `enriched_claims, cleaned_fragments, markup, source_links, remaining_gaps` |
| a-core/К-10 | Разрешение конфликтов источников | `claims, versions, source_priorities, BA_decisions` | `conflicts[{id,claims,scope,versions,resolution,authority}], accepted_claims` |
| a-core/К-11 | Контроль полноты зависимостей | `scope, claims, actors, settings, product_links, unresolved` | `dependency_manifest[{id,prerequisite,evidence,status}], retrieval_requests, recommendation` |
| a-core/К-14 | Глоссарий | `terms_in_sections_2_to_6, raw_wording, supplied_lexicons` | `section_1[{term,definition,source,lexicon_comparison}], term_questions` |
| a-core/К-15 | Бизнес-контекст | `atoms, scope, business_problem, value, decisions` | `section_2{context,problem,goal,in_scope,out_of_scope,products_owners}` |
| a-core/К-16 | ФТ изменения существующего поведения | `request_atoms, verified_as_is, scope, BA_accepted_recommendations` | `section_3[{id,capability,requirement,delta,source}], rejected_candidates` |
| a-core/К-17 | ФТ нового поведения с нуля | `explicit_new_mode_decision, request_atoms, scope, product_context` | `section_3_new[{id,capability,requirement,source}], novelty_boundary` |
| a-core/К-18 | Нефункциональные требования | `supplied_quality_requirements, scope, applicable_source_thresholds` | `section_4[{id,characteristic,metric,threshold,conditions,source}], nfr_questions` |
| a-core/К-37 | User Story по запросу БА | `explicit_BA_request, atoms, scope, value, FR?` | `stories[{id,role,action,value,acceptance,fr_ids,source}], story_questions` |
| a-core/К-38 | Отдельное моделирование UC по запросу БА | `explicit_BA_request, atoms, scope, actors, FR?` | `requested_UC[{id,actor,precondition,flow,alternatives,result,fr_ids,source}]` |
| a-core/К-19 | Первый прогон UC и покрытие ФТ | `sections_2_3_4, scope` | `section_7_first[{id,actor,precondition,flow,alternatives,result,fr_ids,class}], coverage_matrix` |
| a-core/К-28 | Независимая содержательная проверка | `frozen_candidate, source_bodies, applicable_rules, approved_scope, decisions` | `findings[{id,claim,source,rule,severity,affected_ids}], checked_claims, unresolved` |
| a-core/К-29 | Анализ влияния изменения | `baseline_revision, change_request, dependency_graph, prior_approvals` | `impact_set, stale_ids, invalidated_approvals, proposed_edit_scope` |
| a-core/К-30 | Адресная правка | `candidate_revision, authorized_edit_scope, findings, human_instructions` | `patch[{id,before,after,reason}], preserved_ids, semantic_diff, stale_ids` |
| a-core/К-31 | Структурная сверка документа | `candidate, schema_version, entity_register, trace_matrix` | `conformance_report{missing,duplicates,broken_refs,section_order,counts,verdict}` |
| a-core/К-34 | Регистрация решений и согласований | `human_message, actor_role, authority, candidate_revision, scope, timestamp, gate_id?, gate_type?, model_recommendation?` | `section_8_5_record{id,decision,actor,authority,revision,scope,time,evidence,status,gate_id,gate_type,model_recommendation,divergence}` |
| a-core/К-39 | Сверка с манифестом | `baseline_manifest, generated_candidate, authorized_delta, decision_register` | `manifest_diff` |
| a-core/К-12 | Полная сборка фазы | `base_snapshot, ordered_slices, tombstones, source_register, decisions` | `full_snapshot, entity_register, unresolved, superseded, completeness_receipt` |
| a-core/К-20 | Подготовка доказательств гейта | `gate_id, gate_type, candidate_revision, applicable_gate_contract, checklist_evidence, human_records` | `gate_report{criteria,evidence,gaps,eligible_for_review,required_actors}, recommendation` |
### a-work

| Экземпляр | Класс | Обязательный вход | Результат |
| --- | --- | --- | --- |
| a-work/К-36 | Загрузка правил и параметров чата | `full_constitution, applicable_standards, versions, task_parameters, access_receipts` | `rule_receipt{documents,versions,available,missing,precedence}, task_config` |
| a-work/К-13 | Проверка переносимого контекста | `full_snapshot, required_inputs_for_target, source_bodies, rule_bundle` | `handoff_receipt[{input,status,locator}], missing_inputs, recommendation` |
| a-work/К-03 | Оценка неоднозначности | `atoms, candidate_readings, known_decisions` | `ambiguities[{id,readings,impact,blocking,owner,needed_evidence}], resolved_ids` |
| a-work/К-04 | Пакет вопросов | `ambiguities, missing_evidence, prior_questions, owners` | `questions[{id,text,options,recipient,blocks,deadline,source}], no_repeat_ids` |
| a-work/К-06 | Границы изменения | `atoms, matches, BA_decisions, adjacent_dependencies` | `in_scope, out_of_scope, context_only, dependencies, owners` |
| a-work/К-07 | Извлечение из web | `source_plan, accessible_page_bodies, URLs, versions` | `claims[{id,feature,verdict,quote,url,heading,version}], coverage, access_gaps` |
| a-work/К-08 | Извлечение из PDF и runtime | `source_plan, attached_documents, runtime_sections?, provenance` | `claims[{id,feature,verdict,quote,document,section,pages?,version}], coverage, gaps` |
| a-work/К-09 | Дообогащение материалами БА | `missing_evidence, BA_raw_materials?, author_roles, provenance` | `enriched_claims, cleaned_fragments, markup, source_links, remaining_gaps` |
| a-work/К-10 | Разрешение конфликтов источников | `claims, versions, source_priorities, BA_decisions` | `conflicts[{id,claims,scope,versions,resolution,authority}], accepted_claims` |
| a-work/К-11 | Контроль полноты зависимостей | `scope, claims, actors, settings, product_links, unresolved` | `dependency_manifest[{id,prerequisite,evidence,status}], retrieval_requests, recommendation` |
| a-work/К-14 | Глоссарий | `terms_in_sections_2_to_6, raw_wording, supplied_lexicons` | `section_1[{term,definition,source,lexicon_comparison}], term_questions` |
| a-work/К-15 | Бизнес-контекст | `atoms, scope, business_problem, value, decisions` | `section_2{context,problem,goal,in_scope,out_of_scope,products_owners}` |
| a-work/К-16 | ФТ изменения существующего поведения | `request_atoms, verified_as_is, scope, BA_accepted_recommendations` | `section_3[{id,capability,requirement,delta,source}], rejected_candidates` |
| a-work/К-17 | ФТ нового поведения с нуля | `explicit_new_mode_decision, request_atoms, scope, product_context` | `section_3_new[{id,capability,requirement,source}], novelty_boundary` |
| a-work/К-18 | Нефункциональные требования | `supplied_quality_requirements, scope, applicable_source_thresholds` | `section_4[{id,characteristic,metric,threshold,conditions,source}], nfr_questions` |
| a-work/К-21 | ОРР L1 | `sections_1_to_4, UC_first, verified_claims, scope` | `section_5_1{actors,context,behavior,interactions,fr_trace}, design_questions` |
| a-work/К-22 | ОРР L2 и контракты стыков | `BA_level_decision, section_5_1, supplied_API_events, product_profiles` | `section_5_2{components,contract_deltas,compatibility,owners,fr_trace}, unresolved_contracts` |
| a-work/К-23 | Особенности и ограничения | `section_5, source_constraints, scope_exclusions` | `section_6{features_refs,external_constraints[{id,source,consequence}]}` |
| a-work/К-24 | Второй прогон UC и граничные случаи | `sections_3_to_6, UC_first, supplied_UI_API_contracts` | `section_7_second, boundary_matrix, uncovered_behavior` |
| a-work/К-25 | Анализ рисков | `scope, design, uncertainty, evidence` | `section_8_1[{id,cause,event,consequence,probability,impact,measure,owner,source}], risk_questions` |
| a-work/К-26 | Реестр зависимостей поставки | `dependency_manifest, design, team_responses, scope` | `section_8_2[{id,depends_on,type,blocks,human_status,owner,source}]` |
| a-work/К-27 | План приёмки | `FR, NFR, UC, source_thresholds, proposed_acceptors` | `section_8_3[{id,given,when,then,requirement_id,method,acceptor}], acceptance_gaps` |
| a-work/К-37 | User Story по запросу БА | `explicit_BA_request, atoms, scope, value, FR?` | `stories[{id,role,action,value,acceptance,fr_ids,source}], story_questions` |
| a-work/К-38 | Отдельное моделирование UC по запросу БА | `explicit_BA_request, atoms, scope, actors, FR?` | `requested_UC[{id,actor,precondition,flow,alternatives,result,fr_ids,source}]` |
| a-work/К-28 | Независимая содержательная проверка | `frozen_candidate, source_bodies, applicable_rules, approved_scope, decisions` | `findings[{id,claim,source,rule,severity,affected_ids}], checked_claims, unresolved` |
| a-work/К-29 | Анализ влияния изменения | `baseline_revision, change_request, dependency_graph, prior_approvals` | `impact_set, stale_ids, invalidated_approvals, proposed_edit_scope` |
| a-work/К-30 | Адресная правка | `candidate_revision, authorized_edit_scope, findings, human_instructions` | `patch[{id,before,after,reason}], preserved_ids, semantic_diff, stale_ids` |
| a-work/К-31 | Структурная сверка документа | `candidate, schema_version, entity_register, trace_matrix` | `conformance_report{missing,duplicates,broken_refs,section_order,counts,verdict}` |
| a-work/К-34 | Регистрация решений и согласований | `human_message, actor_role, authority, candidate_revision, scope, timestamp, gate_id?, gate_type?, model_recommendation?` | `section_8_5_record{id,decision,actor,authority,revision,scope,time,evidence,status,gate_id,gate_type,model_recommendation,divergence}` |
| a-work/К-39 | Сверка с манифестом | `baseline_manifest, generated_candidate, authorized_delta, decision_register` | `manifest_diff` |
| a-work/К-12 | Полная сборка фазы | `base_snapshot, ordered_slices, tombstones, source_register, decisions` | `full_snapshot, entity_register, unresolved, superseded, completeness_receipt` |
| a-work/К-20 | Подготовка доказательств гейта | `gate_id, gate_type, candidate_revision, applicable_gate_contract, checklist_evidence, human_records` | `gate_report{criteria,evidence,gaps,eligible_for_review,required_actors}, recommendation` |
### a-release

| Экземпляр | Класс | Обязательный вход | Результат |
| --- | --- | --- | --- |
| a-release/К-36 | Загрузка правил и параметров чата | `full_constitution, applicable_standards, versions, task_parameters, access_receipts` | `rule_receipt{documents,versions,available,missing,precedence}, task_config` |
| a-release/К-13 | Проверка переносимого контекста | `full_snapshot, required_inputs_for_target, source_bodies, rule_bundle` | `handoff_receipt[{input,status,locator}], missing_inputs, recommendation` |
| a-release/К-04 | Пакет вопросов | `ambiguities, missing_evidence, prior_questions, owners` | `questions[{id,text,options,recipient,blocks,deadline,source}], no_repeat_ids` |
| a-release/К-29 | Анализ влияния изменения | `baseline_revision, change_request, dependency_graph, prior_approvals` | `impact_set, stale_ids, invalidated_approvals, proposed_edit_scope` |
| a-release/К-30 | Адресная правка | `candidate_revision, authorized_edit_scope, findings, human_instructions` | `patch[{id,before,after,reason}], preserved_ids, semantic_diff, stale_ids` |
| a-release/К-31 | Структурная сверка документа | `candidate, schema_version, entity_register, trace_matrix` | `conformance_report{missing,duplicates,broken_refs,section_order,counts,verdict}` |
| a-release/К-28 | Независимая содержательная проверка | `frozen_candidate, source_bodies, applicable_rules, approved_scope, decisions` | `findings[{id,claim,source,rule,severity,affected_ids}], checked_claims, unresolved` |
| a-release/К-34 | Регистрация решений и согласований | `human_message, actor_role, authority, candidate_revision, scope, timestamp, gate_id?, gate_type?, model_recommendation?` | `section_8_5_record{id,decision,actor,authority,revision,scope,time,evidence,status,gate_id,gate_type,model_recommendation,divergence}` |
| a-release/К-39 | Сверка с манифестом | `baseline_manifest, generated_candidate, authorized_delta, decision_register` | `manifest_diff` |
| a-release/К-12 | Полная сборка фазы | `base_snapshot, ordered_slices, tombstones, source_register, decisions` | `full_snapshot, entity_register, unresolved, superseded, completeness_receipt` |
| a-release/К-20 | Подготовка доказательств гейта | `gate_id, gate_type, candidate_revision, applicable_gate_contract, checklist_evidence, human_records` | `gate_report{criteria,evidence,gaps,eligible_for_review,required_actors}, recommendation` |
| a-release/К-32 | Подготовка пакетов адресатам | `approved_or_draft_candidate, audience_policy, scope, approvals` | `customer_packet, internal_packet, delivery_manifest, excluded_items` |
| a-release/К-33 | Контроль выпускного комплекта | `delivery_manifest, packets, candidate_revision, required_approvals, source_receipts` | `release_report{revision_checks,approval_checks,missing,stale,ready_for_human_release}` |
| a-release/К-35 | Фиксация baseline и передача | `release_report, human_release_record?, final_packets, unresolved, owners` | `baseline_manifest{revision,artifacts,decisions,open_items,owners,delivery_status}, change_entrypoint` |

К-16/К-17 — альтернативы delta/new по решению БА, К-22 — по уровню, К-37/К-38 — только по запросу. К-07/К-08/К-09 — доступные и необходимые пути доказательств, не обязательное тройное чтение каждого источника. К-29/К-30 — только при изменениях. К-34 выполняется после фактической реплики человека; отсутствие реплики сохраняется как pending. К-12 готовит фазу, К-20 предлагает гейт, человек решает, К-34 фиксирует, К-12 обновляет полный результат.

## Почему классы разделены

Нормализация не классифицирует продукт. Неоднозначность не формулирует пакет вопросов. Web и PDF/runtime имеют разные локаторы и риски доступа. Очистка, извлечение и разметка сырого материала БА остаются одной операцией К-09 по прямому указанию основателя. К-11 проверяет знания, К-26 фиксирует зависимости поставки. К-12 собирает текст, К-13 проверяет переносимость, К-36 проверяет правила. К-19 проверяет покрытие, К-24 проверяет решение и границы, К-38 моделирует выбранный UC без заявления полноты. К-25 и К-26 имеют разные объекты и выходы. К-28 проверяет смысл, К-31 структуру, К-33 комплект выпуска. К-32 меняет аудиторию, К-35 фиксирует baseline. Разница продукта сама по себе не порождает новый класс.

## Связанные контракты

- [Состояние и ручная работа](../../docs/contracts/bcreq-manual-state.md).
- [Обоснование и маршрут](../../docs/rfc/2026-10-bcreq-manual-pipeline.md).
- [Checkpoint до стандартов](../../docs/analysis/2026-10-29-bcreq-checkpoint.md).

После имитации отдельно выделен К-39: fidelity результата к исходному манифесту. Проверка структуры К-31 не обнаруживает ослабленное условие, а проверка продуктовой истинности К-28 решает другую задачу. Это расширяет исходные 38 классов checkpoint до 39 без объединения различных операций.
