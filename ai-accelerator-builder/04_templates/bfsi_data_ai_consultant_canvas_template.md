---
type: template
template_id: bfsi_data_ai_consultant_canvas
template_name: BFSI Data & AI Consultant Canvas
status: draft
version: 0.1
intended_users:
  - lead_architect
  - data_architect
  - ai_architect
  - governance_consultant
  - delivery_lead
use_cases:
  - discovery_workshop
  - architecture_assessment
  - ai_readiness_assessment
  - solution_shaping
  - proposal_development
  - executive_briefing
related_playbooks:
  - governed_rag_delivery_playbook
  - regulatory_reporting_delivery_playbook
  - ai_readiness_assessment_playbook
  - semantic_data_product_delivery_playbook
related_capabilities:
  - data_product
  - semantic_layer
  - data_quality
  - lineage
  - ai_copilots_and_workflows
  - ai_evaluation
---

# BFSI Data & AI Consultant Canvas

## 1. Template purpose

This template helps consultants quickly frame a BFSI Data & AI opportunity, assess complexity, identify required capabilities, select reusable architecture patterns, define controls and produce a practical delivery roadmap.

Use this as the front-door canvas before creating detailed solution designs, reference architectures, proposals or delivery plans.

The core idea:

> Move from vague AI ambition to a structured architecture and delivery conversation.

---

## 2. Engagement summary

| Field | Response |
|---|---|
| Client / business unit |  |
| Engagement name |  |
| Date |  |
| Lead consultant |  |
| Client sponsor |  |
| Business owner |  |
| Technology owner |  |
| Risk / compliance owner |  |
| Current phase | Discovery / Design / Delivery / Assurance / Scale |
| Target outcome |  |

---

## 3. Business problem

### Problem statement

```text
Describe the business problem in plain language.

Example:
Regulatory reporting analysts spend significant manual effort investigating data exceptions because report logic, lineage, reconciliation rules and data ownership are fragmented across systems and teams.
```

### Business outcome

| Question | Response |
|---|---|
| What business process, decision, report or workflow are we improving? |  |
| Who are the users? |  |
| What pain point exists today? |  |
| What business value is expected? |  |
| What does success look like? |  |
| What is the cost of doing nothing? |  |

---

## 4. BFSI domain context

Select all that apply.

```text
[ ] Banking
[ ] Insurance
[ ] Wealth / Super / Investments
[ ] Payments
[ ] Lending
[ ] Credit Risk
[ ] Fraud
[ ] AML / Financial Crime
[ ] Regulatory Reporting
[ ] Claims
[ ] Customer Service
[ ] Risk and Compliance
[ ] Data Governance
[ ] Other:
```

### Core business entities

| Entity | Relevant? | Notes |
|---|---:|---|
| Customer / Party |  |  |
| Account |  |  |
| Product |  |  |
| Transaction |  |  |
| Payment |  |  |
| Policy |  |  |
| Claim |  |  |
| Balance |  |  |
| Limit / Exposure |  |  |
| Collateral |  |  |
| Alert |  |  |
| Case |  |  |
| Obligation |  |  |
| Control |  |  |
| Reportable Event |  |  |

---

## 5. AI role classification

Classify what AI is expected to do.

| AI role | Applies? | Notes |
|---|---:|---|
| Productivity assistant |  | Helps staff draft, summarise or search |
| Knowledge interface |  | Answers questions from approved documents |
| Data assistant |  | Answers questions from governed data products |
| Reasoning assistant |  | Compares, explains, summarises and recommends |
| Decision support |  | Suggests next steps or options for human review |
| Workflow assistant |  | Supports process steps and case handling |
| Agentic executor |  | Takes controlled actions via tools or APIs |
| Continuous optimisation |  | Learns from feedback and improves signals/patterns |

### AI decision impact

```text
[ ] Informational only
[ ] Analytical insight
[ ] Decision support
[ ] Customer-impacting recommendation
[ ] Regulatory-impacting recommendation
[ ] Financial-impacting recommendation
[ ] Action execution
```

Guidance:

> The closer AI gets to decisioning or action, the stronger the controls, evaluation and human approval requirements must become.

---

## 6. Current-state assessment

### Current-state summary

```text
Summarise the current environment, including platforms, data sources, governance maturity, delivery constraints and known issues.
```

### Current-state issues

| Issue | Business impact | Severity | Owner |
|---|---|---:|---|
|  |  | Low / Medium / High |  |
|  |  | Low / Medium / High |  |
|  |  | Low / Medium / High |  |

---

## 7. Capability assessment

Use maturity levels:

```text
0 = Not present
1 = Ad hoc
2 = Repeatable
3 = Governed
4 = Industrialised
5 = Adaptive
```

| Capability | Current | Target | Gap | Priority | Notes |
|---|---:|---:|---:|---|---|
| Data ingestion |  |  |  |  |  |
| Data integration |  |  |  |  |  |
| Lakehouse / warehouse |  |  |  |  |  |
| Data modelling |  |  |  |  |  |
| Data product management |  |  |  |  |  |
| Data quality |  |  |  |  |  |
| Metadata management |  |  |  |  |  |
| Lineage |  |  |  |  |  |
| Access control |  |  |  |  |  |
| Data classification |  |  |  |  |  |
| Semantic layer |  |  |  |  |  |
| Feature / signal layer |  |  |  |  |  |
| RAG / knowledge layer |  |  |  |  |  |
| AI orchestration |  |  |  |  |  |
| AI evaluation |  |  |  |  |  |
| AI observability |  |  |  |  |  |
| Human approval workflow |  |  |  |  |  |
| DataOps / DevOps |  |  |  |  |  |
| MLOps / model lifecycle |  |  |  |  |  |
| Evidence retention |  |  |  |  |  |

---

## 8. Required architecture pattern

Select the most relevant reusable patterns.

```text
[ ] Regulatory Reporting Data Layer
[ ] Governed RAG Knowledge Base
[ ] AI Copilot over Data Products
[ ] Agentic Workflow with Human Approval
[ ] Semantic Layer for AI
[ ] Fraud Signal Layer
[ ] Source-to-Report Lineage Framework
[ ] Data Quality Control Framework
[ ] M&A Data Separation Framework
[ ] AI Evaluation and Monitoring Framework
[ ] Data Product Operating Model
[ ] Other:
```

### Pattern rationale

| Pattern | Why it applies | Required adaptations |
|---|---|---|
|  |  |  |
|  |  |  |

---

## 9. Target logical architecture

Use this section to describe the proposed high-level architecture.

```text
Business Users / Workflow
  ↓
AI Interaction Layer
  - copilot
  - assistant
  - workflow interface
  ↓
AI Orchestration Layer
  - prompt policy
  - model routing
  - retrieval routing
  - tool routing
  - guardrails
  ↓
Governed Context Layer
  - semantic layer
  - RAG knowledge layer
  - feature / signal layer
  - metadata / lineage
  ↓
Governed Data Layer
  - data products
  - curated data
  - data quality
  - reconciliation
  ↓
Platform Foundation
  - cloud data platform
  - ingestion
  - transformation
  - CI/CD
  - monitoring
  ↓
Enterprise Sources
  - source systems
  - documents
  - operational systems
```

### Architecture notes

```text
Document key architecture decisions, trade-offs and assumptions.
```

---

## 10. Reference architecture options

| Option | Platform | When suitable | Pros | Risks |
|---|---|---|---|---|
| Option A | AWS |  |  |  |
| Option B | Azure |  |  |  |
| Option C | Snowflake / Databricks |  |  |  |
| Option D | Hybrid |  |  |  |

### Recommended option

```text
State the recommended reference architecture option and explain why.
```

---

## 11. Control and risk assessment

### Risk classification

```text
[ ] Low
[ ] Medium
[ ] High
[ ] Very High
```

### Control matrix

| Control | Required? | Current state | Target state | Evidence required |
|---|---:|---|---|---|
| Data ownership |  |  |  |  |
| Data quality |  |  |  |  |
| Lineage |  |  |  |  |
| Reconciliation |  |  |  |  |
| Access control |  |  |  |  |
| Data classification |  |  |  |  |
| PII protection |  |  |  |  |
| Prompt policy |  |  |  |  |
| Retrieval grounding |  |  |  |  |
| Tool permissioning |  |  |  |  |
| Human approval |  |  |  |  |
| AI evaluation |  |  |  |  |
| Audit logging |  |  |  |  |
| Evidence retention |  |  |  |  |
| Monitoring |  |  |  |  |
| Incident management |  |  |  |  |

### Key risks

| Risk | Likelihood | Impact | Mitigation |
|---|---:|---:|---|
|  | Low / Medium / High | Low / Medium / High |  |
|  | Low / Medium / High | Low / Medium / High |  |

---

## 12. Delivery roadmap

### Phase 1: Discover

| Activity | Output | Owner |
|---|---|---|
| Confirm use case and business outcome | Use case canvas |  |
| Assess current maturity | Capability heatmap |  |
| Identify data and knowledge sources | Source inventory |  |
| Classify risk | Risk rating |  |

### Phase 2: Design

| Activity | Output | Owner |
|---|---|---|
| Define target logical architecture | Architecture view |  |
| Select reference pattern | Pattern selection |  |
| Define control gates | Control matrix |  |
| Define delivery backlog | Roadmap |  |

### Phase 3: Build / Pilot

| Activity | Output | Owner |
|---|---|---|
| Build minimum viable pattern | Pilot implementation |  |
| Configure controls | Control evidence |  |
| Test quality and safety | Evaluation scorecard |  |
| Run controlled pilot | Pilot feedback |  |

### Phase 4: Industrialise

| Activity | Output | Owner |
|---|---|---|
| Productionise pattern | Production release |  |
| Add monitoring | Observability dashboard |  |
| Create reusable assets | Practice asset pack |  |
| Handover operating model | Runbook |  |

### Phase 5: Scale

| Activity | Output | Owner |
|---|---|---|
| Expand to new domains | Scale roadmap |  |
| Standardise delivery | Playbook update |  |
| Track benefits | Benefits report |  |
| Feed lessons into knowledge base | Reusable IP update |  |

---

## 13. Deliverables checklist

```text
[ ] Engagement summary
[ ] Use case canvas
[ ] Current-state assessment
[ ] Capability heatmap
[ ] Domain model
[ ] Source inventory
[ ] Risk assessment
[ ] Target logical architecture
[ ] Reference architecture options
[ ] Pattern selection
[ ] Control matrix
[ ] Delivery roadmap
[ ] Production readiness checklist
[ ] Executive summary
[ ] Reusable knowledge base update
```

---

## 14. Executive summary template

```text
The client is seeking to improve [business process / decision / workflow] across [domain].

The current environment is constrained by [key issues], creating risk and inefficiency in [business outcome].

The recommended approach is to apply the [selected pattern] pattern, supported by [key capabilities], with controls across [data / AI / security / regulatory / operational controls].

The initial delivery should focus on [MVP scope], followed by industrialisation through [DataOps / MLOps / governance / monitoring / reusable assets].

This approach helps the client move from isolated project delivery to a reusable, governed Data & AI capability.
```

---

## 15. Reusable knowledge base update

At the end of the engagement, capture what can be reused.

| Reusable asset | Created / updated? | Location |
|---|---:|---|
| Capability page |  |  |
| Pattern page |  |  |
| Playbook |  |  |
| Template |  |  |
| Reference architecture |  |  |
| Control matrix |  |  |
| Case study |  |  |
| Executive narrative |  |  |

### Lessons learned

```text
What did we learn that should improve the practice knowledge base?
```

### Suggested new reusable asset

```text
What should be added to the practice asset library?
```

---

## 16. Design principles

> Start with the business decision, not the technology.

> Classify the AI role before selecting the architecture.

> Do not expose ungoverned data or content as trusted AI context.

> The more AI moves from answering to acting, the stronger the controls must become.

> Every engagement should produce reusable practice assets, not just project outputs.
