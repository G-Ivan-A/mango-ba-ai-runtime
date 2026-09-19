# Source deployment audit

Issue #1 supplied two absolute source URLs. They were read successfully through
authenticated GitHub access and checked out at immutable commits:

- package: `dbf3baa96d3585150974212254af81bcf7b03150`;
- knowledge base: `8cbf82aa73129ec5747af07f790aaf438b0fb6e9`.

The package source contained 42 files. The knowledge-base source and deployed
`docs/kb/` each contain 9,212 files (about 181 MB). `pre-fix-smoke.log` records
the failing baseline; `all-checks.log` records the passing runtime smoke and
portable validator. The optional Python validator reports missing PyYAML, which
is why `tools/validate-package.sh` is the required dependency-free gate.
