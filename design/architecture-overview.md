# Architecture Overview

## Purpose
This repository is a BFSI Data and AI practice builder. It is designed to help consultants move from client problem framing to governed architecture decisions, reusable patterns, delivery playbooks, control mappings, and case-study-backed assets.

The architectural stance is that AI changes the target from data delivery to governed intelligence delivery. The platform is not complete when data is available. It is complete when governed data, semantic meaning, signals, knowledge, controls, workflow integration, and evidence all work together.

## Core Architecture

```text
Enterprise Sources
  Core Banking | CRM | Payments | Claims | Policy | Documents | Third Parties
      ->
Data Platform Layer
  Lakehouse | Warehouse | Streaming | CDC | APIs | DataOps | IaC
      ->
Governed Data Layer
  Curated Data Products | Data Quality | Lineage | Reconciliation | Access Control
      ->
Meaning and Intelligence Layer
  Semantic Layer | Feature Layer | Signal Layer | Knowledge Base | Metadata
      ->
AI Control Layer
  Prompt Policy | Guardrails | Evaluation | Tool Permissions | Observability
      ->
AI Interaction Layer
  Copilot | RAG | Reasoning Assistant | Agentic Workflow
      ->
Human and Workflow Layer
  Review | Approval | Exception Handling | Case Management | Evidence Capture
      ->
Business Outcomes
  Fraud | Risk | Regulatory Reporting | Customer Intelligence | Operations
```

## Design Principles
- Governance is architectural, not a post-build compliance step.
- Human accountability remains in high-risk workflows.
- Deterministic controls constrain what AI can see, do, and promote.
- Reusable patterns matter more than one-off solution documents.
- Domain context matters: BFSI use cases need explicit business entities, policies, and evidence.

## Repository Mapping

| Folder | Role in the architecture |
|---|---|
| `00_overview` | High-level positioning and practice framing. |
| `01_capabilities` | Capability definitions across data foundation, governance, AI enablement, delivery engineering, and business consumption. |
| `02_patterns` | Reusable solution patterns such as semantic layers, governed RAG, fraud signal layers, and agentic workflows with human approval. |
| `03_playbooks` | Delivery playbooks that turn patterns into phased implementation work. |
| `04_templates` | Reusable document structures for repeatable consulting outputs. |
| `05_reference_architectures` | Platform-specific and hybrid target-state reference architectures. |
| `06_domain_models` | BFSI business entities and domain structures used to ground designs. |
| `07_controls` | Data, AI, security, regulatory, and operational control libraries. |
| `08_case_studies` | Concrete use cases that show how patterns apply in business scenarios. |
| `09_indexes` | Navigation and indexing aids for retrieval and reuse. |
| `10_dashboard` | Presentation layer for browsing the practice builder. |
| `11_ai_assistant` | Prompting, retrieval, and output structures for the assistant layer. |
| `12_assets` | Supporting assets for packaging or presentation. |

## How the Parts Work Together
1. Start with a business problem or use case.
2. Classify the BFSI domain and AI role.
3. Map required capabilities and maturity gaps.
4. Select the closest reusable pattern from `02_patterns`.
5. Apply domain context from `06_domain_models`.
6. Map mandatory controls from `07_controls`.
7. Shape the target-state design using `05_reference_architectures`.
8. Support delivery planning with `03_playbooks`.
9. Ground the narrative with examples from `08_case_studies`.

## Typical Output Types
- Logical architecture for a use case
- Reference architecture by platform
- Control matrix and governance gates
- Delivery roadmap and playbook
- Executive narrative for stakeholders
- Case-study-backed accelerator assets

## Architectural Position
The lower half of the stack is still the data platform. The differentiating layer for this practice sits above it: semantic meaning, governed signals, knowledge retrieval, AI control, workflow orchestration, evaluation, and evidence. That is where AI changes architecture most materially.

## Related Documents
- `design/BFSI_AI_Practice_Builder_Reasoning_System.md`: Full reasoning model and detailed architecture narrative.
- `ai-accelerator-builder/05_reference_architectures/hybrid/reference_architecture.md`: Base template for a hybrid target architecture.
