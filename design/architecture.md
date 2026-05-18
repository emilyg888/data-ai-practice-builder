# Architecture

## 1. Purpose

This repository is a practice builder for governed Data and AI consulting, centered on BFSI use cases and reusable enterprise AI delivery assets. It serves two audiences:

- consultants curating reusable capabilities, patterns, controls, and case studies;
- operators using the Streamlit dashboard to browse the library, assess maturity, and assemble client-facing outputs.

## 2. Current System Shape

The repository has two main layers:

- a markdown-first knowledge base under `ai-accelerator-builder/` containing the practice assets;
- a local-first Streamlit dashboard under `ai-accelerator-builder/10_dashboard/dashboard/` that scans those assets and turns them into browsable and exportable views.

The repo also contains design notes and source materials under `design/` and `archives/`. During housekeeping, an older root static website prototype was moved into `src_archives/2026-05-18_housekeeping/`.

## 3. Component Map

| Component | Path | Responsibility | Key dependencies |
|---|---|---|---|
| Root repository guide | `README.md` | High-level entry point and usage guide for the repo | `design/architecture.md`, `ai-accelerator-builder/README.md` |
| Practice knowledge base | `ai-accelerator-builder/` | Canonical markdown corpus for capabilities, patterns, controls, case studies, and reference architectures | Markdown files, image/pdf assets |
| Overview and framing assets | `ai-accelerator-builder/00_overview/` | Practice framing, maturity model, and positioning docs | Markdown |
| Capability library | `ai-accelerator-builder/01_capabilities/` | Reusable capability definitions across data foundation, AI enablement, governance, and delivery engineering | Markdown, diagram assets |
| Pattern library | `ai-accelerator-builder/02_patterns/` | Reusable architecture and orchestration patterns | Markdown |
| Playbooks and templates | `ai-accelerator-builder/03_playbooks/`, `04_templates/` | Delivery methods and reusable consulting output templates | Markdown |
| Reference architectures | `ai-accelerator-builder/05_reference_architectures/` | AWS and other platform-specific implementation notes | Markdown |
| Domain and controls | `ai-accelerator-builder/06_domain_models/`, `07_controls/` | Business context and governance controls | Markdown |
| Case studies and indexes | `ai-accelerator-builder/08_case_studies/`, `09_indexes/` | Narrative examples and retrieval/navigation aids | Markdown, YAML |
| Streamlit dashboard | `ai-accelerator-builder/10_dashboard/dashboard/` | Local-first UI for browsing, assessment, control mapping, graph analysis, and exports | Python, Streamlit |
| Dashboard service layer | `ai-accelerator-builder/10_dashboard/dashboard/services/` | Content loading, metadata parsing, recommendation logic, export logic, graph building, and local assessment storage | Python stdlib, Streamlit runtime |
| Dashboard UI pages | `ai-accelerator-builder/10_dashboard/dashboard/pages/` | Capability Browser, Pattern Browser, Maturity Heatmap, Control Matrix, Client Assessment, AWS Reference Browser, AWS Graph | Streamlit, service layer |
| Assistant scaffolding | `ai-accelerator-builder/11_ai_assistant/` | Prompt and retrieval design for AI-assisted consulting workflows | Markdown |
| Design and reasoning docs | `design/` | Architecture docs, reasoning-system docs, captured source notes, pending issues | Markdown, draw.io |
| Source archives | `src_archives/` | Archived low-risk obsolete assets moved during housekeeping | Archived project files, manifest |

## 4. Runtime Flow

```text
Markdown practice assets
  → content loader + metadata parser
  → normalized in-memory records
  → Streamlit pages / recommendation logic / graph builder
  → local assessment state + markdown/csv outputs
```

## 5. Data Flow

The primary data source is the markdown repository under `ai-accelerator-builder/`. The dashboard loads files recursively, extracts lightweight metadata from front matter, headings, and sections, and converts that into normalized records for:

- capabilities;
- patterns;
- controls;
- AWS reference notes;
- maturity levels;
- client assessment outputs.

Client Assessment writes local JSON artefacts to `ai-accelerator-builder/10_dashboard/dashboard/data/assessments/`. Exported outputs are generated in-memory as Markdown or CSV downloads rather than persisted globally.

The AWS graph page builds an aggregate graph model from the AWS reference-note corpus. Node types represent concepts, AWS components, and reusable pattern themes derived from note metadata and content.

## 6. Configuration

Primary execution configuration is local and file-based:

- Streamlit app entry point: `ai-accelerator-builder/10_dashboard/dashboard/app.py`
- Streamlit navigation config: `ai-accelerator-builder/10_dashboard/dashboard/.streamlit/config.toml`
- Python dependencies: `ai-accelerator-builder/10_dashboard/dashboard/requirements.txt`
- Virtual environment commonly used locally: `ai-accelerator-builder/10_dashboard/dashboard/.venv/`

No required environment variables were found in the inspected runtime path. No secrets should be stored in this repo.

## 7. Testing and SIT

There is no formal automated test suite in the repository root. Housekeeping used practical smoke/SIT checks against the active dashboard:

- `python3 -m py_compile ai-accelerator-builder/10_dashboard/dashboard/app.py ai-accelerator-builder/10_dashboard/dashboard/components/*.py ai-accelerator-builder/10_dashboard/dashboard/pages/*.py ai-accelerator-builder/10_dashboard/dashboard/services/*.py`
- `./.venv/bin/python -c "from services.content_loader import load_repository_content; ..."` from `ai-accelerator-builder/10_dashboard/dashboard/`
- `./.venv/bin/python -c "from services.content_loader import load_repository_content; from services.graph_builder import build_aws_pattern_graph; ..."` from `ai-accelerator-builder/10_dashboard/dashboard/`

These checks passed during housekeeping and verified syntax, repository loading, and AWS graph construction.

## 8. Deployment / Execution

The main supported execution model is local:

1. Change into `ai-accelerator-builder/10_dashboard/dashboard/`
2. Activate or create a Python virtual environment
3. Install `requirements.txt`
4. Run `streamlit run app.py`

The dashboard is a local consultant workbench, not a packaged production service.

## 9. Governance / Operational Notes

- The practice repository is intentionally markdown-first so architecture, controls, patterns, and case-study reasoning remain inspectable and editable.
- Governance is encoded through pattern metadata, control mappings, and client assessment outputs rather than hidden application state.
- The dashboard uses tolerant parsing because front matter and section structure are not fully normalized across the corpus.
- The active UI is the Streamlit dashboard; an older static site prototype was archived during housekeeping to reduce ambiguity.
- The worktree was already dirty at housekeeping start, so pre-existing changes were preserved and recorded for review rather than overwritten.

## 10. Known Gaps

See `design/issues-pending-review.md`.
