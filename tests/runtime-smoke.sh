#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
FAILURES=0

pass() { printf 'ok - %s\n' "$1"; }
fail() { printf 'not ok - %s\n' "$1" >&2; FAILURES=$((FAILURES + 1)); }

require_file() {
  if [ -f "$ROOT/$1" ]; then pass "$1 exists"; else fail "$1 exists"; fi
}

require_text() {
  file=$1
  pattern=$2
  label=$3
  if grep -Eq "$pattern" "$ROOT/$file"; then pass "$label"; else fail "$label"; fi
}

for file in \
  .hub-profile.json \
  AGENTS.md \
  README.md \
  compilation-manifest.yaml \
  tools/validate-package.sh \
  docs/guides/README.md \
  docs/guides/00-quick-start.md \
  docs/guides/01-repository-setup.md \
  docs/guides/02-processes.md \
  docs/guides/03-task-types.md \
  docs/guides/04-running-tasks.md \
  docs/guides/05-human-review.md \
  docs/guides/06-dialog-rules.md
do
  require_file "$file"
done

require_text README.md 'version: 0\.4' 'README declares package 0.4'
require_text compilation-manifest.yaml '^version: "0\.4"$' 'manifest declares package 0.4'
require_text compilation-manifest.yaml '^meta_model_version: "0\.4"$' 'manifest pins meta-model 0.4'
require_text .hub-profile.json '"fallback_path"[[:space:]]*:[[:space:]]*"docs/kb"' 'profile declares docs/kb fallback'
require_text .hub-profile.json '"task_isolation"[[:space:]]*:[[:space:]]*"chat"' 'profile isolates tasks by chat'
require_text .hub-profile.json '"output_directory"[[:space:]]*:[[:space:]]*"runs"' 'profile writes outputs to runs'

for tier in corporate_repository confluence mango_web external_systems local_repository_fallback; do
  require_text .hub-profile.json "\"$tier\"" "profile declares $tier"
done

require_text taxonomy/source-tiers.yaml 'id: ST-1-CORPORATE' 'tier 1 corporate repository exists'
require_text taxonomy/source-tiers.yaml 'id: ST-2-CONFLUENCE' 'tier 2 Confluence exists'
require_text taxonomy/source-tiers.yaml 'id: ST-3-MANGO-WEB' 'tier 3 Mango web exists'
require_text taxonomy/source-tiers.yaml 'id: ST-4-EXTERNAL' 'tier 4 external systems exists'
require_text taxonomy/source-tiers.yaml 'id: ST-5-LOCAL' 'tier 5 local fallback exists'
require_text taxonomy/source-tiers.yaml 'status: out_of_slice' 'unconfigured tiers are explicit out_of_slice'
require_text contracts/c-in.schema.json 'ST-5-LOCAL' 'C-IN accepts local fallback tier'
require_text routes/run-sheet-template.yaml 'output_path: "runs/' 'run sheet declares MD output path'

if grep -R -E 'ST-[1234]-(ATTACHED|CORPUS|PRODUCT-DOC|HUMAN)' \
  "$ROOT/AGENTS.md" "$ROOT/contracts" "$ROOT/evaluation" "$ROOT/golden" \
  "$ROOT/routes" "$ROOT/taxonomy" >/dev/null 2>&1
then
  fail 'obsolete source tiers are absent'
else
  pass 'obsolete source tiers are absent'
fi

if [ -x "$ROOT/tools/validate-package.sh" ]; then pass 'shell validator is executable'; else fail 'shell validator is executable'; fi
if command -v python3 >/dev/null 2>&1; then
  NO_PYTHON_PATH=$(mktemp -d)
  printf '#!/bin/sh\nexit 127\n' > "$NO_PYTHON_PATH/python3"
  chmod +x "$NO_PYTHON_PATH/python3"
  PATH="$NO_PYTHON_PATH:$PATH" "$ROOT/tools/validate-package.sh" "$ROOT" >/dev/null 2>&1 \
    && pass 'shell validator runs without Python on PATH' \
    || fail 'shell validator runs without Python on PATH'
fi

if [ "$FAILURES" -ne 0 ]; then
  printf 'runtime smoke test failed: %s check(s)\n' "$FAILURES" >&2
  exit 1
fi

printf 'runtime smoke test passed\n'
