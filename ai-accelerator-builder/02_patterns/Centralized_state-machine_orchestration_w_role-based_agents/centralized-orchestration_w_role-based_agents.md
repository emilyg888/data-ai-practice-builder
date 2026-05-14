---
type: pattern
status: draft
risk_level: high
business_domains:
  - banking
  - payments
  - fraud
  - risk
capability_layers:
  - analyst_experience
  - workflow_orchestration
  - reasoning
  - governed_retrieval
  - deterministic_data_access
  - governance_and_controls
  - signal_management
  - monitoring_and_audit
ai_impact:
  - analyst_acceleration
  - evidence_synthesis
  - governed_signal_discovery
  - human_in_the_loop_decision_support
related_controls:
  - data_minimisation
  - least_privilege_data_access
  - human_approval_gate
  - audit_trace
  - model_risk_management
  - signal_change_governance
---

# Agentic Fraud Investigation over Governed Data Products

## 1. Problem solved

Fraud teams often have model alerts, transaction evidence, behavioural signals, case history,
and policy documents spread across separate tools. Analysts spend time stitching these together,
repeating the same investigation steps, and writing case notes manually. At the same time,
enterprises cannot allow an LLM to access raw customer data freely, generate unrestricted SQL,
or make final fraud decisions without controls.

This pattern solves that problem by separating reasoning from control. A central workflow
orchestrates role-based agents for classification, planning, retrieval, summarisation, and
signal hypothesis generation, while deterministic tools enforce governed data access,
governance checks, evaluation, registry writes, and human approval before any signal promotion.

## 2. When to use

Use this pattern when an organisation needs an AI-assisted fraud investigation capability
that improves analyst productivity without bypassing existing control frameworks.

Typical conditions include:

- fraud operations teams reviewing model-triggered alerts
- multiple governed data products containing customer, account, transaction, and behavioural data
- a requirement to expose typologies, policies, and evidence in one analyst workflow
- a need to generate candidate fraud signals but keep approval under human control
- a requirement for full audit trace, evidence references, and deterministic control gates
- a need to demonstrate an enterprise AI operating model before full production rollout

## 3. Business outcomes

This pattern is designed to deliver:

- faster alert triage and investigation turnaround
- more consistent evidence gathering across analysts
- better reuse of fraud typologies, policy knowledge, and prior case reasoning
- improved signal discovery with explicit evaluation and governance checks
- clearer auditability for internal controls, model risk, and compliance stakeholders
- a safer path to AI adoption by constraining LLM usage to bounded reasoning tasks

## 4. Logical architecture

The logical flow is:

1. A business analyst or fraud reviewer starts from a dashboard or CLI case queue.
2. A service layer submits the case into a centralized LangGraph workflow.
3. The workflow executes role-based steps over a shared state:
   classification, planning, retrieval, governed data access, summarisation,
   signal hypothesis generation, evaluation, and governance checks.
4. If a candidate signal is produced, the workflow pauses at a human review boundary.
5. The reviewer approves or rejects the candidate signal.
6. The workflow resumes, writes reports and trace artefacts, and updates the signal registry.
7. Monitoring components track approved signals for coverage, decay, drift proxies, and review timing.

Key design rule:
the LLM contributes reasoning, not control. Control stays in deterministic tools and workflow policy.

## 5. Reference architecture options

### Option A: Local architecture lab

Use a local-first implementation for architecture prototyping, stakeholder demos, and user testing.

- Streamlit dashboard for the analyst workspace
- Python service layer and CLI for invocation
- LangGraph for orchestration, pause/resume, and checkpointed state
- SQLite checkpointer for workflow state
- local markdown knowledge base and local vector store for RAG
- sample CSV datasets accessed only through deterministic data tools
- YAML-backed signal registry
- markdown reports and JSON traces as local artefacts

This is the option implemented in this repository.

### Option B: Enterprise governed platform

Map the same control pattern to enterprise services without changing the logical separation of duties.

- analyst workspace on internal web app or BI front end
- workflow orchestration on LangGraph-compatible runtime, AWS Step Functions plus agents,
  or an internal orchestration service
- checkpoint and run state in managed relational or document persistence
- governed data products in Snowflake, lakehouse, or warehouse domains
- vector retrieval over managed search or vector services
- enterprise identity, secrets, logging, SIEM, and model governance controls
- signal registry backed by governed metadata and change-control processes

The important point is that the architectural pattern stays the same even if the products change.

## 6. Required capabilities

This pattern requires the following capability layers:

- analyst experience layer for case queue, investigation workspace, evidence explorer,
  copilot interaction, human review, and audit visibility
- orchestration layer with explicit state, routing, and pause/resume semantics
- bounded reasoning layer for classification, planning, evidence summarisation,
  and signal hypothesis generation
- governed retrieval layer for typologies, policies, and data dictionary content
- deterministic data access layer that mediates all alert, customer, account,
  transaction, and feature retrieval
- governance layer for data quality, lineage, privacy, and explainability checks
- signal evaluation layer for candidate scoring and promotion readiness
- signal registry for candidate, approved, and rejected signal lifecycle states
- monitoring layer for post-promotion review, drift proxy, decay proxy, and coverage tracking
- artefact layer for case reports, evidence summaries, and audit traces

## 7. Control gates

This pattern depends on explicit control gates.

### Gate 1: Data access control

- the LLM does not query raw datasets directly
- all structured data access is routed through approved deterministic tools
- unrestricted SQL generation and execution are disallowed

### Gate 2: Retrieval scope control

- RAG sources are limited to approved typologies, policies, and data dictionaries
- source references are attached to outputs

### Gate 3: Evaluation control

- candidate signals are evaluated with deterministic metrics and thresholds
- signal creation does not imply signal promotion

### Gate 4: Governance control

- data quality, lineage, privacy, and explainability checks must run before promotion
- governance findings must be visible to the reviewer

### Gate 5: Human approval control

- no signal is promoted without explicit human approval
- the workflow pauses and resumes through a documented approval step

### Gate 6: Audit control

- all analyst actions, evidence references, decisions, and workflow steps are recorded
- reports and traces are persisted for review and replay

## 8. Delivery steps

An enterprise team can deliver this pattern in phases.

1. Define target use case, alert population, and analyst workflow.
2. Identify the governed data products, typologies, policies, and feature sources.
3. Implement deterministic data-access tools and data contracts first.
4. Add retrieval over approved knowledge artefacts.
5. Implement centralized workflow orchestration with typed state and audit events.
6. Add role-based reasoning functions for classification, planning, summarisation,
   and candidate signal hypotheses.
7. Add evaluation and governance controls before any promotion workflow.
8. Add the human approval boundary and signal registry lifecycle.
9. Add analyst dashboard and case-report artefacts.
10. Add monitoring for approved signals and regression-style validation.
11. Run user testing, control review, and architecture sign-off before production mapping.

## 9. Common risks and failure modes

Common risks include:

- allowing the LLM to bypass deterministic data controls
- over-trusting model explanations or summaries without evidence references
- promoting candidate signals without a real approval gate
- weak lineage or stale feature inputs leading to false confidence
- dashboard logic duplicating workflow logic and creating inconsistent decisions
- treating synthetic demo metrics as production validation
- storing case state only in UI session state rather than durable workflow checkpoints
- failing to capture analyst approve or reject actions in the audit trace

## 10. Artefacts produced

A delivery using this pattern typically produces:

- architecture overview and workflow design documents
- governed data contracts and dataset mappings
- typology, policy, and feature knowledge artefacts
- workflow state model and orchestration definitions
- deterministic tool specifications
- governance check outputs
- candidate, approved, and rejected signal registry entries
- case reports with evidence references
- JSON or structured audit traces
- monitoring outputs for signal health and review cadence
- user-test scripts and demo walkthroughs

## 11. Example executive narrative

We implemented a governed agentic fraud investigation pattern that accelerates analyst work
without handing control to the model. A centralized workflow coordinates classification,
planning, retrieval, data access, evaluation, and governance checks over shared state.
The LLM contributes bounded reasoning only. It cannot access raw datasets directly,
cannot generate unrestricted SQL, cannot make final fraud decisions, and cannot promote
signals without human approval. Deterministic controls enforce data access, policy checks,
signal evaluation, registry updates, and auditability. This gives the business a practical,
demonstrable path to enterprise AI in fraud operations while keeping human accountability
and control gates intact.
