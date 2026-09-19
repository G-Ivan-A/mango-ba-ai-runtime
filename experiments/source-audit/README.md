# Source deployment audit

Issue #1 supplied two source repositories. They were cloned with Git and checked
out at immutable commits:

- package: `dbf3baa96d3585150974212254af81bcf7b03150`;
- knowledge base: `8cbf82aa73129ec5747af07f790aaf438b0fb6e9`.

The package source contained 42 files. The knowledge-base source contained
9,212 files (about 181 MB), but its content is intentionally not bundled per the
owner's PR instruction; only `docs/kb/.gitkeep` remains. `pre-fix-smoke.log`
records the failing baseline. The portable checks are reproducible with
`sh tests/runtime-smoke.sh` and `sh tools/validate-package.sh`. The optional
Python validator reports missing PyYAML, which is why the shell validator is the
required dependency-free gate.
