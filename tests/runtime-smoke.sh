#!/bin/sh
# Проверка чистоты репозитория: структура, контракты в Markdown, база знаний,
# отсутствие привязки к среде и явных запретов на внешние базы знаний.
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
FAILURES=0

pass() { printf 'ok - %s\n' "$1"; }
fail() { printf 'not ok - %s\n' "$1" >&2; FAILURES=$((FAILURES + 1)); }

require_file() {
  if [ -f "$ROOT/$1" ]; then pass "$1 exists"; else fail "$1 exists"; fi
}

require_absent() {
  if [ -e "$ROOT/$1" ]; then fail "$1 is absent"; else pass "$1 is absent"; fi
}

require_text() {
  if grep -Eq "$2" "$ROOT/$1"; then pass "$3"; else fail "$3"; fi
}

# Runtime files outside the bundled knowledge base.
runtime_files() {
  find "$ROOT" -path "$ROOT/.git" -prune -o -path "$ROOT/docs/kb" -prune \
    -o -path "$ROOT/tests" -prune -o -path "$ROOT/.github" -prune \
    -o -type f -print
}

for file in AGENTS.md README.md compilation-manifest.yaml \
  docs/guides/README.md docs/guides/00-quick-start.md \
  routes/rg-bcreq-v1.yaml routes/run-sheet-template.yaml \
  evaluation/validate-package.md evaluation/g-mach-checklist.md \
  evaluation/g-human-checklist.md docs/kb/README.md \
  golden/cases.yaml golden/cases-voice-ucaas.yaml golden/cases-analytics-reporting.yaml
do
  require_file "$file"
done

for contract in c-in c-core c-quest c-out-bcreq c-rk; do
  require_file "contracts/$contract.md"
  require_text "contracts/$contract.md" '^type: system-prompt$' "$contract is a system prompt"
done

for path in .agents .hub-profile.json tools runs experiments; do
  require_absent "$path"
done

if [ -n "$(runtime_files | grep -E '\.(py|json)$' || true)" ]; then
  fail 'no .py or .json runtime files'
else
  pass 'no .py or .json runtime files'
fi

# The manifest records provenance, so it may name removed paths.
if runtime_files | grep -v '/compilation-manifest.yaml$' | xargs grep -EIl 'GigaCode|GitVerse|Qwen|\.schema\.json|\.agents/|tools/validate|hub-profile' >/dev/null 2>&1; then
  fail 'no environment-specific references'
  runtime_files | grep -v '/compilation-manifest.yaml$' | xargs grep -EIn 'GigaCode|GitVerse|Qwen|\.schema\.json|\.agents/|tools/validate|hub-profile' >&2 || true
else
  pass 'no environment-specific references'
fi

if runtime_files | xargs grep -EIil 'не подключать|out_of_slice' >/dev/null 2>&1; then
  fail 'no explicit bans on external knowledge bases'
else
  pass 'no explicit bans on external knowledge bases'
fi

# Every relative path that the runtime mentions must exist.
for ref in $(runtime_files | xargs grep -EhoI '(^|[][ `(,])(contracts|skills|taxonomy|routes|templates|golden|evaluation)/[A-Za-z0-9._-]+\.(md|yaml)' | sed 's/^[][ `(,]//' | sort -u); do
  require_file "$ref"
done

skills=$(find "$ROOT/skills" -name '*.md' | wc -l | tr -d ' ')
if [ "$skills" -eq 11 ]; then pass '11 skills'; else fail "11 skills (found $skills)"; fi
for skill in "$ROOT"/skills/*.md; do
  name=$(basename "$skill" .md)
  require_text "skills/$name.md" "^name: $name\$" "skill $name declares its name"
done

docs=$(find "$ROOT/docs/kb" -mindepth 2 -maxdepth 2 -name index.md | wc -l | tr -d ' ')
if [ "$docs" -gt 0 ]; then pass "knowledge base has $docs documents"; else fail 'knowledge base is populated'; fi
require_text taxonomy/source-tiers.yaml 'path: docs/kb' 'ST-5-LOCAL points to docs/kb'

# Closed Mango product catalog: every golden atomic_function is a catalog function id.
require_file taxonomy/mango-products.yaml
require_text taxonomy/mango-products.yaml '^closed: true$' 'product catalog is closed'
for af in $(grep -hEo 'atomic_function: *"?[a-z0-9/-]+' "$ROOT"/golden/cases*.yaml | sed 's/.*: *"\{0,1\}//'); do
  if grep -Fq "{id: \"$af\", level: function," "$ROOT/taxonomy/mango-products.yaml" 2>/dev/null; then pass "golden atomic_function $af is in catalog"; else fail "golden atomic_function $af is in catalog"; fi
done
# Rule PT-5: the product taxonomy points at the catalog; every catalog-refusal case
# declares an input function that fails c-in for the reason in catalog_check.
require_text taxonomy/products.yaml '^catalog: taxonomy/mango-products\.yaml' 'product taxonomy declares the closed catalog'
require_text taxonomy/products.yaml '^class_domains:' 'product taxonomy declares class_domains'
refusals=$(awk '/^ *declared_function:/ { f = $2 } /^ *catalog_check:/ { print f "=" $2; f = "" }' "$ROOT"/golden/cases*.yaml)
if [ -n "$refusals" ]; then pass 'golden sets have catalog-refusal cases'; else fail 'golden sets have catalog-refusal cases'; fi
for pair in $refusals; do
  df=${pair%%=*}; check=${pair#*=}
  case "$check" in
    outside-catalog)
      if grep -Fq "{id: \"$df\"," "$ROOT/taxonomy/mango-products.yaml" 2>/dev/null; then fail "declared function $df is outside catalog"; else pass "declared function $df is outside catalog"; fi ;;
    foreign-class|not-function)
      if [ -n "$df" ] && grep -Fq "{id: \"$df\"," "$ROOT/taxonomy/mango-products.yaml" 2>/dev/null; then pass "declared function $df is a catalog node ($check)"; else fail "declared function $df is a catalog node ($check)"; fi ;;
    *) fail "catalog_check $check is a known value" ;;
  esac
done

if [ "$FAILURES" -ne 0 ]; then
  printf 'runtime smoke test failed: %s check(s)\n' "$FAILURES" >&2
  exit 1
fi

printf 'runtime smoke test passed\n'
