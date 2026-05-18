# Data AI Practice Builder

## Overview

This repository is a markdown-first consulting practice builder for governed Data and AI delivery, with a strong BFSI focus. It combines reusable capabilities, patterns, reference architectures, controls, playbooks, and case studies with a local Streamlit dashboard for browsing and client assessment.

## Architecture Summary

The system has two layers:

- `ai-accelerator-builder/` is the source-of-truth knowledge base.
- `ai-accelerator-builder/10_dashboard/dashboard/` is the local-first Streamlit workbench that parses the markdown corpus and turns it into assessment, graph, and export views.

The practice model moves from business framing to reusable delivery assets:

```text
Capabilities → Patterns → Controls → Playbooks → Case Studies → Client Assessment Outputs
```

Detailed architecture is documented in `design/architecture.md`.

## Repository Structure

| Path | Purpose |
|---|---|
| `ai-accelerator-builder/00_overview` | Practice framing, positioning, and maturity material |
| `ai-accelerator-builder/01_capabilities` | Reusable capability definitions and core enabler assets |
| `ai-accelerator-builder/02_patterns` | Reusable solution and architecture patterns |
| `ai-accelerator-builder/03_playbooks` | Delivery playbooks |
| `ai-accelerator-builder/04_templates` | Reusable consulting templates |
| `ai-accelerator-builder/05_reference_architectures` | Platform-specific and hybrid reference notes |
| `ai-accelerator-builder/06_domain_models` | BFSI domain context |
| `ai-accelerator-builder/07_controls` | Governance and control libraries |
| `ai-accelerator-builder/08_case_studies` | Reusable case studies and use cases |
| `ai-accelerator-builder/09_indexes` | Index and retrieval support files |
| `ai-accelerator-builder/10_dashboard` | Streamlit dashboard and design docs |
| `ai-accelerator-builder/11_ai_assistant` | Assistant prompts and retrieval design |
| `design` | Architecture, reasoning, diagrams, and review notes |
| `src_archives` | Archived obsolete assets preserved during housekeeping |

## Setup

For the active dashboard:

```bash
cd ai-accelerator-builder/10_dashboard/dashboard
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

From `ai-accelerator-builder/10_dashboard/dashboard`:

```bash
streamlit run app.py
```

## Test / SIT

Housekeeping used these practical smoke/SIT commands:

```bash
python3 -m py_compile ai-accelerator-builder/10_dashboard/dashboard/app.py ai-accelerator-builder/10_dashboard/dashboard/components/*.py ai-accelerator-builder/10_dashboard/dashboard/pages/*.py ai-accelerator-builder/10_dashboard/dashboard/services/*.py
```

From `ai-accelerator-builder/10_dashboard/dashboard`:

```bash
./.venv/bin/python -c "from services.content_loader import load_repository_content; content = load_repository_content(); print({'capabilities': len(content['capabilities']), 'patterns': len(content['patterns']), 'aws_references': len(content['aws_references']), 'controls': len(content['controls'])})"
./.venv/bin/python -c "from services.content_loader import load_repository_content; from services.graph_builder import build_aws_pattern_graph; graph = build_aws_pattern_graph(load_repository_content()['aws_references']); print({'nodes': graph['stats']['nodes'], 'edges': graph['stats']['edges'], 'patterns': graph['stats']['patterns']})"
```

## Configuration

- Streamlit app entry point: `ai-accelerator-builder/10_dashboard/dashboard/app.py`
- Dashboard dependencies: `ai-accelerator-builder/10_dashboard/dashboard/requirements.txt`
- Streamlit UI config: `ai-accelerator-builder/10_dashboard/dashboard/.streamlit/config.toml`
- Local assessment storage: `ai-accelerator-builder/10_dashboard/dashboard/data/assessments/`

No required environment variables were identified in the current local execution path.

## Documentation

- Architecture: `design/architecture.md`
- Architecture overview: `design/architecture-overview.md`
- Pending review issues: `design/issues-pending-review.md`
- Dashboard runtime notes: `ai-accelerator-builder/10_dashboard/dashboard/README.md`

## Current Status

- Active UI: Streamlit dashboard
- Active corpus: markdown knowledge base under `ai-accelerator-builder/`
- Archived during housekeeping: root static-site prototype moved to `src_archives/2026-05-18_housekeeping/`
- Remaining review items: tracked in `design/issues-pending-review.md`
