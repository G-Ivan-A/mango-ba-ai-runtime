#!/bin/sh
# Portable G-mach structural gate. Uses POSIX shell and standard utilities;
# Python and third-party packages are deliberately not required.
set -eu

ROOT=${1:-$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)}
ERRORS=0

ok() { printf 'ok - %s\n' "$1"; }
bad() { printf 'ERROR: %s\n' "$1" >&2; ERRORS=$((ERRORS + 1)); }
has_file() { [ -f "$ROOT/$1" ] && ok "$1" || bad "missing file: $1"; }
has_dir() { [ -d "$ROOT/$1" ] && ok "$1/" || bad "missing directory: $1"; }
has_text() {
  if grep -Eq "$2" "$ROOT/$1"; then ok "$3"; else bad "$3"; fi
}

for file in AGENTS.md README.md .hub-profile.json compilation-manifest.yaml \
  contracts/c-in.schema.json contracts/c-core.schema.json \
  contracts/c-quest.schema.json contracts/c-out-bcreq.schema.json \
  contracts/c-rk.schema.json routes/rg-bcreq-v1.yaml \
  routes/run-sheet-template.yaml templates/bcreq-skeleton.md \
  taxonomy/source-tiers.yaml evaluation/g-human-checklist.md
do
  has_file "$file"
done

for dir in .agents/skills taxonomy contracts routes templates golden evaluation \
  docs/kb docs/guides runs
do
  has_dir "$dir"
done

# jq is preferred; a JavaScript parser is a valid fallback in GigaCode images.
if command -v jq >/dev/null 2>&1; then
  for file in .hub-profile.json contracts/*.json; do
    jq -e . "$ROOT/$file" >/dev/null 2>&1 || bad "invalid JSON: $file"
  done
  ok 'JSON syntax'
elif command -v node >/dev/null 2>&1; then
  for file in "$ROOT"/.hub-profile.json "$ROOT"/contracts/*.json; do
    node -e 'JSON.parse(require("fs").readFileSync(process.argv[1], "utf8"))' "$file" \
      >/dev/null 2>&1 || bad "invalid JSON: ${file#"$ROOT"/}"
  done
  ok 'JSON syntax'
else
  bad 'jq or node is required to parse JSON (Python is not required)'
fi

for tier in ST-1-CORPORATE ST-2-CONFLUENCE ST-3-MANGO-WEB ST-4-EXTERNAL ST-5-LOCAL; do
  has_text taxonomy/source-tiers.yaml "id: $tier" "knowledge tier $tier"
  has_text contracts/c-in.schema.json "$tier" "C-IN tier $tier"
done

has_text .hub-profile.json '"fallback_path"[[:space:]]*:[[:space:]]*"docs/kb"' 'local KB fallback'
has_text .hub-profile.json '"task_isolation"[[:space:]]*:[[:space:]]*"chat"' 'chat task isolation'
has_text routes/run-sheet-template.yaml 'output_path: "runs/' 'Markdown output path'

skill_count=$(find "$ROOT/.agents/skills" -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')
[ "$skill_count" -eq 11 ] && ok '11 compiled skills' || bad "expected 11 skills, got $skill_count"

for skill in $(sed -n 's/.*skill: \(SK-[a-z-]*\).*/\1/p' "$ROOT/routes/rg-bcreq-v1.yaml" | sort -u); do
  slug=${skill#SK-}
  [ -f "$ROOT/.agents/skills/$slug-contact-center/SKILL.md" ] \
    && ok "route skill $skill" || bad "route skill has no SKILL.md: $skill"
done

kb_count=$(find "$ROOT/docs/kb" -type f ! -name .gitkeep | wc -l | tr -d ' ')
if [ "$kb_count" -eq 0 ] && [ -f "$ROOT/docs/kb/.gitkeep" ]; then
  ok 'local KB placeholder (content is intentionally not bundled)'
else
  ok "local KB contains $kb_count files"
fi

for guide in README 00-quick-start 01-repository-setup 02-processes \
  03-task-types 04-running-tasks 05-human-review 06-dialog-rules
do
  has_file "docs/guides/$guide.md"
done

if [ "$ERRORS" -ne 0 ]; then
  printf 'G-mach: package rejected (%s errors).\n' "$ERRORS" >&2
  exit 1
fi

printf 'G-mach: package accepted (skills: %s, KB content files: %s).\n' "$skill_count" "$kb_count"
