# Data AI Practice Builder

This repository is a BFSI-focused Data and AI practice builder. It is structured to help consultants move from business problem framing to governed architecture, reusable delivery patterns, control mappings, playbooks, and case studies.

The underlying view is that AI changes the goal from data delivery to governed intelligence delivery. A usable target state is not just a platform and a model. It is governed data, semantic meaning, signals, knowledge retrieval, AI controls, workflow integration, and evidence.

## Core Architecture

```text
Enterprise Sources
  -> Data Platform Layer
  -> Governed Data Layer
  -> Meaning and Intelligence Layer
  -> AI Control Layer
  -> AI Interaction Layer
  -> Human and Workflow Layer
  -> Business Outcomes
```

## Repository Structure

| Path | Purpose |
|---|---|
| `ai-accelerator-builder/00_overview` | Practice framing and high-level positioning. |
| `ai-accelerator-builder/01_capabilities` | Capability definitions across data, governance, AI, delivery, and consumption. |
| `ai-accelerator-builder/02_patterns` | Reusable architecture and solution patterns. |
| `ai-accelerator-builder/03_playbooks` | Delivery playbooks for common engagement types. |
| `ai-accelerator-builder/04_templates` | Reusable templates for practice outputs. |
| `ai-accelerator-builder/05_reference_architectures` | Platform and deployment reference architectures. |
| `ai-accelerator-builder/06_domain_models` | BFSI domain structures and business entities. |
| `ai-accelerator-builder/07_controls` | Data, AI, security, regulatory, and operational controls. |
| `ai-accelerator-builder/08_case_studies` | Use cases and case studies organized by topic. |
| `ai-accelerator-builder/09_indexes` | Indexes for retrieval and navigation. |
| `ai-accelerator-builder/10_dashboard` | Dashboard-oriented presentation assets. |
| `ai-accelerator-builder/11_ai_assistant` | Prompting, retrieval, and assistant output scaffolding. |
| `ai-accelerator-builder/12_assets` | Supporting assets. |
| `design` | Architecture and reasoning-system design documents. |

## Start Here

- `design/architecture-overview.md`
- `design/BFSI_AI_Practice_Builder_Reasoning_System.md`
- `ai-accelerator-builder/02_patterns`
- `ai-accelerator-builder/08_case_studies`

## How To Use This Repo

1. Start with the business problem, domain, and decision type.
2. Review the relevant pattern in `02_patterns`.
3. Pull supporting domain context from `06_domain_models`.
4. Map required controls from `07_controls`.
5. Use `05_reference_architectures` and `03_playbooks` to shape delivery.
6. Ground the narrative with examples from `08_case_studies`.

## Current Focus Areas

- Semantic layers for AI-ready data products
- Governed RAG and knowledge access
- Fraud signal layers and investigation workflows
- Agentic workflows with human approval boundaries
- Regulatory reporting and evidence-oriented controls
- AI observability, evaluation, and runtime governance

## Key Design Principles

- Governance is architectural.
- Human accountability remains in high-risk workflows.
- Deterministic controls constrain AI behavior.
- Reusable patterns are preferred over one-off designs.
- BFSI domain context must be explicit in the architecture.
