# Issues Pending Review

## Summary

| ID | Severity | Area | Issue | Recommended action | Status |
|---|---|---|---|---|---|
| ISSUE-001 | Medium | Tests | No formal automated test suite was found at repo root; housekeeping relied on dashboard smoke/SIT commands. | Add a repeatable automated test target for the dashboard service layer and key pages. | Pending review |
| ISSUE-002 | Low | Repo hygiene | `.DS_Store` is still tracked at repository root and the worktree was already dirty at housekeeping start. | Remove tracked Finder artefacts in a dedicated cleanup change once ownership of baseline local changes is confirmed. | Pending review |
| ISSUE-003 | Medium | Docs / Review | The worktree contained pre-existing changes in the AWS graph page and architecture diagram files before housekeeping began. | Review those baseline changes explicitly before or alongside the housekeeping push. | Pending review |

## SIT Results

| Command | Result | Notes |
|---|---|---|
| `python3 -m py_compile ai-accelerator-builder/10_dashboard/dashboard/app.py ai-accelerator-builder/10_dashboard/dashboard/components/*.py ai-accelerator-builder/10_dashboard/dashboard/pages/*.py ai-accelerator-builder/10_dashboard/dashboard/services/*.py` | Passed | Syntax check across the active dashboard app, pages, components, and service modules. |
| `./.venv/bin/python -c "from services.content_loader import load_repository_content; ..."` | Passed | Loaded repository content successfully; observed 15 capabilities, 14 patterns, 169 AWS references, and 69 controls. |
| `./.venv/bin/python -c "from services.content_loader import load_repository_content; from services.graph_builder import build_aws_pattern_graph; ..."` | Passed | Built AWS graph successfully; observed 79 nodes, 520 edges, and 32 pattern nodes. |

## Archived Code Review

| Original path | Archived path | Reason | Review needed? |
|---|---|---|---|
| `index.html` | `src_archives/2026-05-18_housekeeping/root_static_site/index.html` | Obsolete root static-site prototype superseded by the Streamlit dashboard. | No |
| `script.js` | `src_archives/2026-05-18_housekeeping/root_static_site/script.js` | JavaScript for the obsolete root static-site prototype. | No |
| `styles.css` | `src_archives/2026-05-18_housekeeping/root_static_site/styles.css` | Stylesheet for the obsolete root static-site prototype. | No |

## Detailed Issues

### ISSUE-001 — Missing formal automated test target

- Severity: Medium
- Area: Tests
- Evidence: No `pytest`, `unittest`, or equivalent project-wide automated test entry point was found in root documentation or repository structure. Housekeeping used smoke checks instead.
- Impact: Regression detection depends on manual or ad hoc validation.
- Recommended action: Add a small automated test suite around the dashboard content loader, export service, and graph builder, then document the command in `README.md`.
- Status: Pending review

### ISSUE-002 — Tracked Finder artefact at repo root

- Severity: Low
- Area: Code
- Evidence: `git ls-files` shows `.DS_Store` tracked at repository root; `.gitignore` already excludes `.DS_Store`.
- Impact: Creates unnecessary repo noise and recurring local dirtiness.
- Recommended action: Remove the tracked `.DS_Store` file in a focused cleanup commit after confirming no one relies on that existing tracked state.
- Status: Pending review

### ISSUE-003 — Housekeeping started from a dirty worktree

- Severity: Medium
- Area: Docs
- Evidence: Initial `git status --short` showed existing modifications in `ai-accelerator-builder/10_dashboard/dashboard/pages/7_AWS_GenAI_Pattern_Graph.py` and architecture diagram files.
- Impact: Final commit/push may combine housekeeping with pre-existing user changes unless reviewed together.
- Recommended action: Review the baseline graph-layout and diagram file changes explicitly before final handoff.
- Status: Pending review
