---
type: maturity_model
model_id: bfsi_data_ai_maturity_model
model_name: BFSI Data & AI Maturity Model
status: draft
version: 0.1
intended_users:
  - lead_architect
  - data_architect
  - ai_architect
  - governance_consultant
  - delivery_lead
  - practice_lead
business_domains:
  - banking
  - insurance
  - wealth
  - regulatory_reporting
  - fraud
  - risk_and_compliance
capability_layers:
  - data_foundation
  - governance_and_trust
  - ai_enablement
  - delivery_engineering
  - business_consumption
related_templates:
  - bfsi_data_ai_consultant_canvas
related_playbooks:
  - governed_rag_delivery_playbook
  - ai_readiness_assessment_playbook
  - regulatory_reporting_delivery_playbook
  - semantic_data_product_delivery_playbook
related_patterns:
  - governed_rag_knowledge_base
  - regulatory_reporting_data_layer
  - semantic_layer_for_ai
  - ai_copilot_over_data_products
  - fraud_signal_layer
---

# BFSI Data & AI Maturity Model

## 1. Purpose

This maturity model helps consultants assess how ready a BFSI organisation is to deliver trusted, governed and scalable Data & AI capabilities.

It is designed for advisory, architecture assessment, delivery planning and ongoing practice engagement.

The goal is to answer four questions:

1. What level of Data & AI maturity does the client have today?
2. What maturity level is required for the target business and AI use case?
3. Which capability gaps create the highest delivery or risk exposure?
4. What roadmap should move the client from current state to target state?

Core principle:

> AI maturity depends on data maturity, governance maturity, engineering maturity and operating-model maturity. It cannot be assessed as a standalone technology capability.

---

## 2. Maturity levels

Use a 0–5 maturity scale.

| Level | Name | Summary |
|---:|---|---|
| 0 | Not Present | Capability is absent or not formally recognised |
| 1 | Fragmented | Capability exists in pockets, manually and inconsistently |
| 2 | Repeatable | Some common practices exist, but governance and automation are limited |
| 3 | Governed | Ownership, standards, controls and evidence are defined |
| 4 | Industrialised | Capability is automated, reusable, monitored and integrated into delivery |
| 5 | Adaptive | Capability continuously improves through feedback, telemetry and learning loops |

---

## 3. Level definitions

## Level 0 — Not Present

The capability does not exist in any meaningful or repeatable form.

Typical characteristics:

- no defined owner
- no documented process
- no reusable pattern
- no tooling or automation
- no control evidence
- no consistent delivery method
- no measurable outcome

Example:

```text
A client wants to build a GenAI assistant, but there is no approved content inventory, no access model, no evaluation approach and no AI governance pattern.
```

Consulting interpretation:

> The first step is capability creation, not optimisation.

---

## Level 1 — Fragmented

The capability exists, but only in isolated teams, projects or manual processes.

Typical characteristics:

- project-specific implementations
- spreadsheet-based controls
- inconsistent definitions
- limited documentation
- knowledge held by individuals
- no enterprise standard
- low reuse
- weak auditability

Example:

```text
Different teams perform data quality checks for regulatory reports, but each team has its own rules, spreadsheets, reconciliation methods and sign-off process.
```

Consulting interpretation:

> The organisation is dependent on local heroics. Standardisation is the priority.

---

## Level 2 — Repeatable

The capability has some common practices, but it is not yet fully governed or industrialised.

Typical characteristics:

- common templates exist
- some reusable patterns exist
- basic ownership is emerging
- rules are partially documented
- controls are repeatable but not always automated
- some monitoring exists
- implementation still varies across teams

Example:

```text
A client has a common RAG architecture pattern and shared prompt templates, but content approval, access filtering, evaluation and monitoring are still handled inconsistently by each project.
```

Consulting interpretation:

> The organisation has enough foundation to standardise and govern.

---

## Level 3 — Governed

The capability is formally governed with clear ownership, standards, controls and evidence.

Typical characteristics:

- defined business and technology owners
- approved standards and patterns
- control gates are documented
- risk classification is applied
- lineage and evidence are captured
- quality rules are defined
- access policies are enforced
- change management exists

Example:

```text
A regulatory reporting data layer has defined data owners, CDEs, lineage, reconciliation rules, data quality controls, sign-off evidence and change approval.
```

Consulting interpretation:

> The organisation can safely deliver higher-risk use cases, but may still need automation and scale.

---

## Level 4 — Industrialised

The capability is automated, reusable and embedded into delivery pipelines and operating models.

Typical characteristics:

- automated testing and validation
- CI/CD integration
- reusable architecture patterns
- standardised control gates
- observability dashboards
- production monitoring
- reusable templates and accelerators
- clear operating model
- consistent cross-team adoption

Example:

```text
AI evaluation, prompt regression testing, retrieval quality testing and audit logging are integrated into the release pipeline for production copilots.
```

Consulting interpretation:

> The organisation can scale safely across multiple use cases and teams.

---

## Level 5 — Adaptive

The capability continuously improves based on feedback, telemetry, evaluation results and business outcomes.

Typical characteristics:

- closed-loop monitoring
- continuous optimisation
- automated feedback capture
- proactive anomaly detection
- adaptive control tuning
- reusable learnings across domains
- governance-as-code patterns
- AI-assisted improvement workflows
- measurable business value tracking

Example:

```text
A fraud signal layer continuously evaluates signal performance, detects emerging patterns, promotes validated signals and retires weak signals through governed approval workflows.
```

Consulting interpretation:

> The organisation is not only delivering capability; it is compounding organisational intelligence.

---

## 4. Capability dimensions

Assess maturity across five dimensions.

```text
BFSI Data & AI Maturity
│
├── 1. Data Foundation
├── 2. Governance and Trust
├── 3. AI Enablement
├── 4. Delivery Engineering
└── 5. Business Consumption
```

---

## 5. Dimension 1 — Data Foundation

This dimension assesses the client’s ability to ingest, model, manage and serve trusted enterprise data.

Capabilities:

- ingestion
- integration
- lakehouse / warehouse
- data modelling
- master and reference data
- data products
- data quality
- reconciliation
- data lifecycle management

Maturity indicators:

| Level | Indicators |
|---:|---|
| 0 | No common data platform or reusable data foundation |
| 1 | Siloed pipelines and inconsistent source extracts |
| 2 | Common ingestion and modelling patterns emerging |
| 3 | Governed data products, CDEs, DQ rules and lineage exist |
| 4 | Automated pipelines, quality checks, CI/CD and reusable data products |
| 5 | Data foundation improves through usage, quality telemetry and feedback loops |

Key consultant question:

> Can the client produce reusable, trusted and governed data products that AI and analytics can safely consume?

---

## 6. Dimension 2 — Governance and Trust

This dimension assesses the client’s ability to define, enforce and evidence data, AI, security and regulatory controls.

Capabilities:

- data ownership
- stewardship
- critical data elements
- metadata
- lineage
- access control
- data classification
- privacy controls
- reconciliation
- evidence retention
- policy enforcement
- regulatory traceability

Maturity indicators:

| Level | Indicators |
|---:|---|
| 0 | No formal ownership, controls or evidence |
| 1 | Manual controls, local sign-offs and fragmented accountability |
| 2 | Common policies and templates exist, but adoption is uneven |
| 3 | Ownership, control gates, lineage and evidence are governed |
| 4 | Controls are automated, monitored and integrated into delivery |
| 5 | Governance adapts based on risk, usage, telemetry and regulatory change |

Key consultant question:

> Can the client prove that data and AI outputs are controlled, traceable and accountable?

---

## 7. Dimension 3 — AI Enablement

This dimension assesses the client’s readiness to use AI safely and effectively over enterprise data, knowledge and workflows.

Capabilities:

- RAG
- semantic layer
- feature layer
- signal layer
- model registry
- prompt management
- model routing
- AI orchestration
- guardrails
- AI evaluation
- AI observability
- human-in-the-loop controls
- agent/tool governance

Maturity indicators:

| Level | Indicators |
|---:|---|
| 0 | No formal AI enablement capability |
| 1 | Isolated GenAI experiments and unmanaged pilots |
| 2 | Initial RAG/copilot patterns and AI policies exist |
| 3 | AI use cases are governed with approved data, prompts, access and logs |
| 4 | AI delivery patterns are reusable, evaluated, monitored and productionised |
| 5 | AI systems improve through feedback, evaluation, signal learning and governance-as-code |

Key consultant question:

> Is AI consuming trusted context and operating inside clearly governed boundaries?

---

## 8. Dimension 4 — Delivery Engineering

This dimension assesses the client’s ability to deliver Data & AI solutions repeatedly, safely and efficiently.

Capabilities:

- DevOps
- DataOps
- MLOps
- LLMOps
- IaC
- CI/CD
- automated testing
- release management
- environment management
- observability
- incident management
- cost management

Maturity indicators:

| Level | Indicators |
|---:|---|
| 0 | Delivery is manual and project-specific |
| 1 | Scripts and deployments vary by team |
| 2 | Some standard pipelines and environments exist |
| 3 | Delivery standards, testing, approvals and release controls are governed |
| 4 | CI/CD, IaC, observability and automated controls are embedded |
| 5 | Delivery continuously optimises based on telemetry, cost, risk and feedback |

Key consultant question:

> Can the client deliver and operate Data & AI capabilities at scale without reinventing delivery controls each time?

---

## 9. Dimension 5 — Business Consumption

This dimension assesses how well data and AI capabilities are consumed by business users, workflows and decision processes.

Capabilities:

- dashboards
- regulatory reports
- data APIs
- semantic consumption
- AI copilots
- operational workflows
- agentic workflows
- decision support
- exception management
- business adoption
- user feedback
- benefits tracking

Maturity indicators:

| Level | Indicators |
|---:|---|
| 0 | No defined consumption model |
| 1 | Reports, dashboards and AI tools are fragmented |
| 2 | Common consumption channels and basic user adoption exist |
| 3 | Consumption is governed with role access, certified outputs and human review |
| 4 | Business workflows, copilots and dashboards are reusable, monitored and supported |
| 5 | Business consumption continuously improves through feedback, outcome measurement and workflow optimisation |

Key consultant question:

> Are business users consuming trusted data and AI through controlled, measurable and adopted channels?

---

## 10. AI-era interpretation

The maturity model should be interpreted differently in the AI era.

Traditional data maturity asked:

```text
Can we deliver accurate data to reports and analytics?
```

AI-era maturity asks:

```text
Can AI safely use enterprise data, knowledge and tools to support reasoning, decisions and workflows?
```

This means every capability must be assessed through an AI lens.

| Traditional question | AI-era question |
|---|---|
| Is the data accurate? | Is the data safe to expose as AI context? |
| Is the report certified? | Can AI explain the metric using certified definitions? |
| Is the document searchable? | Is the document approved, current, access-filtered and retrievable? |
| Is the model deployed? | Is the model evaluated, monitored and governed? |
| Is the workflow digitised? | Can AI assist the workflow without bypassing accountability? |
| Is lineage captured? | Can we trace an AI answer back to source context and evidence? |

Key principle:

> AI does not remove the need for data governance. It makes governance executable, observable and more urgent.

---

## 11. Scoring method

Score each capability from 0 to 5.

| Score | Meaning |
|---:|---|
| 0 | Not present |
| 1 | Fragmented |
| 2 | Repeatable |
| 3 | Governed |
| 4 | Industrialised |
| 5 | Adaptive |

Optional weighting can be applied depending on use case risk.

### Suggested risk weighting

| Use case type | Recommended weighting |
|---|---|
| Informational AI | Higher weight on content governance, access, retrieval and citation |
| Analytical AI | Higher weight on data quality, semantic layer and lineage |
| Decision-support AI | Higher weight on evaluation, explainability, human review and evidence |
| Agentic workflow | Higher weight on tool permissions, approvals, audit and incident management |
| Regulatory reporting | Higher weight on lineage, reconciliation, data quality and evidence |
| Fraud / AML | Higher weight on signal quality, monitoring, explainability and case workflow |

---

## 12. Maturity heatmap template

Use this template during client assessment.

| Capability | Current | Target | Gap | Risk | Priority | Notes |
|---|---:|---:|---:|---|---|---|
| Data ingestion |  |  |  | Low / Medium / High |  |  |
| Data integration |  |  |  | Low / Medium / High |  |  |
| Lakehouse / warehouse |  |  |  | Low / Medium / High |  |  |
| Data modelling |  |  |  | Low / Medium / High |  |  |
| Data products |  |  |  | Low / Medium / High |  |  |
| Data quality |  |  |  | Low / Medium / High |  |  |
| Metadata |  |  |  | Low / Medium / High |  |  |
| Lineage |  |  |  | Low / Medium / High |  |  |
| Access control |  |  |  | Low / Medium / High |  |  |
| Data classification |  |  |  | Low / Medium / High |  |  |
| Semantic layer |  |  |  | Low / Medium / High |  |  |
| RAG / knowledge layer |  |  |  | Low / Medium / High |  |  |
| Feature / signal layer |  |  |  | Low / Medium / High |  |  |
| AI orchestration |  |  |  | Low / Medium / High |  |  |
| AI evaluation |  |  |  | Low / Medium / High |  |  |
| AI observability |  |  |  | Low / Medium / High |  |  |
| Human approval workflow |  |  |  | Low / Medium / High |  |  |
| DataOps / DevOps |  |  |  | Low / Medium / High |  |  |
| MLOps / LLMOps |  |  |  | Low / Medium / High |  |  |
| Evidence retention |  |  |  | Low / Medium / High |  |  |

---

## 13. Example assessment: Governed RAG use case

Scenario:

```text
A compliance team wants an AI assistant that answers questions from approved internal policy and procedure documents.
```

Sample maturity assessment:

| Capability | Current | Target | Gap | Risk | Priority |
|---|---:|---:|---:|---|---|
| Content inventory | 1 | 3 | 2 | High | High |
| Content ownership | 1 | 3 | 2 | High | High |
| Access control | 2 | 4 | 2 | High | High |
| Data classification | 2 | 3 | 1 | Medium | Medium |
| RAG / knowledge layer | 1 | 4 | 3 | High | High |
| Prompt policy | 1 | 3 | 2 | Medium | High |
| AI evaluation | 0 | 3 | 3 | High | High |
| Audit logging | 1 | 4 | 3 | High | High |
| Monitoring | 1 | 4 | 3 | Medium | Medium |
| Operating model | 1 | 3 | 2 | Medium | High |

Interpretation:

> The client should not move directly to production. The highest priority gaps are content ownership, access filtering, RAG design, evaluation and audit logging. A controlled pilot is possible only after minimum governance gates are implemented.

Recommended roadmap:

```text
Phase 1: Content inventory and risk classification
Phase 2: Access and retrieval design
Phase 3: Controlled pilot with approved content
Phase 4: Evaluation, monitoring and production readiness
Phase 5: Reusable RAG platform pattern
```

---

## 14. Example assessment: Regulatory Reporting Data Layer

Scenario:

```text
A regulatory reporting team wants to modernise ATO/APRA reporting data flows and reduce manual reconciliation effort.
```

Sample maturity assessment:

| Capability | Current | Target | Gap | Risk | Priority |
|---|---:|---:|---:|---|---|
| Source mapping | 2 | 4 | 2 | High | High |
| Data modelling | 2 | 4 | 2 | High | High |
| Data quality | 2 | 4 | 2 | High | High |
| Reconciliation | 1 | 4 | 3 | High | High |
| Lineage | 1 | 4 | 3 | High | High |
| CDE management | 1 | 3 | 2 | High | High |
| Evidence retention | 1 | 4 | 3 | High | High |
| Change control | 2 | 4 | 2 | Medium | Medium |
| DataOps | 2 | 4 | 2 | Medium | Medium |
| AI readiness | 0 | 2 | 2 | Medium | Low |

Interpretation:

> The target should be a governed regulatory reporting data layer with deterministic rules, automated reconciliation, source-to-report lineage and retained evidence. AI may assist exception triage and documentation, but should not be the source of reportable output.

Recommended roadmap:

```text
Phase 1: Source-to-report assessment
Phase 2: Reporting data product design
Phase 3: DQ, reconciliation and lineage controls
Phase 4: Evidence pack and production governance
Phase 5: AI-assisted exception triage
```

---

## 15. Consultant usage guide

Use this maturity model in five steps.

### Step 1: Classify the use case

Identify whether the use case is:

```text
[ ] Data platform foundation
[ ] Regulatory reporting
[ ] Fraud / AML / risk analytics
[ ] Governed RAG
[ ] AI copilot
[ ] Agentic workflow
[ ] Data product operating model
[ ] Semantic layer for AI
```

### Step 2: Select relevant capabilities

Do not score everything if the assessment is narrow.

For example:

- Governed RAG: content ownership, classification, access, RAG, evaluation, logging
- Regulatory reporting: DQ, reconciliation, lineage, CDEs, evidence
- Fraud signal layer: transaction data, signals, feature management, explainability, monitoring
- AI copilot: semantic layer, access, AI orchestration, human approval, evaluation

### Step 3: Score current and target maturity

Use evidence where possible.

Examples of evidence:

- architecture documents
- data quality rule catalogues
- lineage diagrams
- policy documents
- CI/CD pipelines
- monitoring dashboards
- model registry
- prompt library
- evaluation results
- audit logs
- support runbooks

### Step 4: Identify gaps and risks

Prioritise gaps using:

```text
Priority = maturity gap × business risk × delivery dependency
```

### Step 5: Build roadmap

Convert the highest-priority gaps into:

- discovery actions
- design actions
- build actions
- control gates
- operating model changes
- reusable practice assets

---

## 16. Executive summary template

```text
The maturity assessment indicates that the client is currently operating at Level [X] across the most critical Data & AI capabilities required for [use case].

The target maturity level is Level [Y], because the use case involves [regulated data / customer impact / decision support / AI retrieval / operational workflow].

The highest-priority gaps are [gap 1], [gap 2] and [gap 3]. These gaps create delivery risk because [reason].

The recommended roadmap is to first stabilise [foundation/control capability], then implement [target architecture pattern], and finally industrialise through [automation, monitoring, operating model and reusable assets].

This approach allows the client to move from fragmented delivery to a governed, reusable and scalable Data & AI capability.
```

---

## 17. Practice asset outputs

Each maturity assessment should produce reusable assets for the practice knowledge base.

| Asset | Description |
|---|---|
| Capability heatmap | Current vs target score by capability |
| Gap analysis | Priority gaps and risk implications |
| Roadmap | Phased delivery plan |
| Control matrix | Required controls and evidence |
| Pattern recommendation | Reusable architecture patterns to apply |
| Executive summary | Business-friendly assessment narrative |
| Case study | Sanitised learning for future engagements |
| Knowledge base update | New examples, risks, controls or artefacts |

---

## 18. Common anti-patterns

Avoid these mistakes.

| Anti-pattern | Why it is risky |
|---|---|
| Scoring maturity without evidence | Produces subjective and weak assessment |
| Treating AI maturity as separate from data maturity | Ignores the dependency on trusted data and governance |
| Targeting Level 5 everywhere | Creates unrealistic roadmap and stakeholder fatigue |
| Overweighting tools | Platform adoption does not equal maturity |
| Ignoring operating model | Capabilities fail after delivery if ownership is unclear |
| Treating pilots as production-ready | Skips controls, monitoring and support |
| Ignoring risk classification | Applies weak controls to high-impact use cases |
| Not producing reusable assets | Limits practice-building value |

---

## 19. Design principles

> Maturity is not a technology score. It is a measure of repeatability, trust, control and adoption.

> AI maturity is constrained by data, governance and operating-model maturity.

> A client does not need Level 5 everywhere. They need the right maturity for the risk and ambition of the use case.

> The purpose of maturity assessment is not judgement. It is roadmap clarity.

> Every maturity assessment should feed the practice knowledge base and improve future delivery.
