---
type: design_doc
design_doc_id: mvp2_dashboard_design
design_doc_name: MVP 2 Dashboard Design
status: draft
version: 0.1
initiative: BFSI AI Practice Builder
mvp: MVP 2
related_mvp:
  - MVP 1: Practice Knowledge Scaffold
  - MVP 3: AI Assistant
primary_users:
  - practice_lead
  - lead_architect
  - data_architect
  - ai_architect
  - governance_consultant
  - delivery_lead
  - client_partner
dashboard_modules:
  - capability_browser
  - pattern_browser
  - maturity_heatmap
  - control_matrix
  - client_assessment_view
related_folders:
  - 00_overview
  - 01_capabilities
  - 02_patterns
  - 03_playbooks
  - 04_templates
  - 07_controls
  - 09_indexes
---

# MVP 2 Dashboard Design

## 1. Purpose

MVP 2 introduces a lightweight dashboard / portal for the **BFSI AI Practice Builder**.

MVP 1 creates the structured knowledge base:

```text
Markdown + YAML
Capabilities
Patterns
Playbooks
Templates
Controls
Reference architectures
Maturity model
Indexes
```

MVP 2 makes that knowledge base usable through an interactive dashboard.

The dashboard should help consultants:

- browse practice capabilities
- find reusable architecture patterns
- assess client maturity
- map controls to patterns and use cases
- create a client assessment view
- turn knowledge assets into engagement-ready outputs

The dashboard is not the source of truth.

The source of truth remains the structured knowledge repository.

```text
Markdown / YAML Knowledge Base = source of truth
Dashboard = navigation, assessment and decision-support layer
AI Assistant = reasoning and synthesis layer
```

---

## 2. MVP 2 scope

MVP 2 includes five dashboard modules:

```text
MVP 2: Dashboard
│
├── Capability browser
├── Pattern browser
├── Maturity heatmap
├── Control matrix
└── Client assessment view
```

## 2.1 In scope

- Read metadata from Markdown front matter and index YAML files
- Display capabilities by layer, domain, AI impact and risk level
- Display architecture patterns by use case, capability and control requirements
- Provide maturity scoring from 0 to 5
- Show current vs target maturity gaps
- Map patterns to required controls
- Create a simple client assessment view
- Export assessment outputs to Markdown or CSV
- Provide a foundation for MVP 3 AI Assistant

## 2.2 Out of scope for MVP 2

- Full RAG assistant
- Automated document ingestion
- Multi-user authentication
- Enterprise workflow integration
- Advanced role-based access control
- Client-facing SaaS portal
- Live integration with Collibra, Purview, Snowflake or Databricks
- Production-grade database backend
- Complex visual analytics

MVP 2 should remain lightweight and local-first.

---

## 3. Design principles

> Dashboard is a control room, not the knowledge base.

> Markdown and YAML remain the source of truth.

> Every dashboard view should answer a consultant question.

> Every assessment should produce reusable practice artefacts.

> The dashboard should help consultants think consistently, not replace architecture judgement.

> Build simple first: filters, tables, heatmaps, exportable outputs.

---

## 4. Target user journeys

## 4.1 Practice lead

Question:

```text
What capabilities, patterns and controls do we have in the practice library?
```

Dashboard support:

- capability coverage view
- pattern catalogue
- control coverage matrix
- reusable asset inventory

Output:

- practice maturity view
- gaps in reusable IP
- backlog for new capability / pattern pages

## 4.2 Lead architect

Question:

```text
For this client use case, which architecture patterns and controls apply?
```

Dashboard support:

- pattern browser
- capability filter
- AI role filter
- risk filter
- control matrix

Output:

- recommended patterns
- control requirements
- target architecture starting point

## 4.3 Governance consultant

Question:

```text
What controls are required for this AI-enabled BFSI use case?
```

Dashboard support:

- control matrix
- pattern-to-control mapping
- maturity heatmap
- risk classification

Output:

- control gap view
- evidence requirements
- production readiness checklist

## 4.4 Delivery lead

Question:

```text
What should we deliver first, next and later?
```

Dashboard support:

- client assessment view
- current vs target maturity
- prioritised gaps
- roadmap export

Output:

- phased delivery roadmap
- backlog themes
- reusable artefacts required

## 4.5 Client partner / executive stakeholder

Question:

```text
How do we explain the client opportunity clearly and commercially?
```

Dashboard support:

- assessment summary
- maturity gap summary
- high-priority capability gaps
- recommended engagement model

Output:

- executive narrative
- proposal input
- advisory / pod / managed partnership positioning

---

## 5. Information architecture

The dashboard should mirror the practice knowledge scaffold.

```text
ai-accelerator-builder/
│
├── 00_overview/
│   ├── maturity_model.md
│   ├── ai_impact_model.md
│   └── capability_map.md
│
├── 01_capabilities/
│   ├── data_foundation/
│   ├── governance_and_trust/
│   ├── ai_enablement/
│   ├── delivery_engineering/
│   └── business_consumption/
│
├── 02_patterns/
│   ├── governed_rag_knowledge_base/
│   ├── regulatory_reporting_data_layer/
│   ├── fraud_signal_layer/
│   └── ...
│
├── 03_playbooks/
│
├── 04_templates/
│   └── consultant_canvas.md
│
├── 07_controls/
│
└── 09_indexes/
    ├── capability_index.yaml
    ├── pattern_index.yaml
    ├── control_index.yaml
    ├── playbook_index.yaml
    └── template_index.yaml
```

Dashboard navigation:

```text
Home
│
├── Capability Browser
├── Pattern Browser
├── Maturity Heatmap
├── Control Matrix
└── Client Assessment
```

---

## 6. Data sources

MVP 2 should read from two types of files.

## 6.1 Markdown files with YAML front matter

Example capability file:

```yaml
---
type: capability
capability_id: data_product
capability_name: Data Product
capability_layer: data_foundation
architecture_layer:
  - curated_layer
  - semantic_layer
bfsi_domains:
  - banking
  - insurance
  - regulatory_reporting
ai_impact:
  - ai_as_reasoning_assistant
risk_level: high
related_patterns:
  - regulatory_reporting_data_layer
  - semantic_layer_for_ai
related_controls:
  - data_quality
  - lineage
  - access_control
---
```

## 6.2 Index YAML files

Index files provide curated records for dashboard performance and consistency.

Example:

```yaml
capabilities:
  - capability_id: data_product
    name: Data Product
    folder: 01_capabilities/data_foundation/data_product.md
    layer: data_foundation
    risk_level: high
    ai_relevance: high
    status: draft
```

MVP 2 can start by reading Markdown front matter directly and later generate or validate index YAML files.

---

## 7. Data model

## 7.1 Core entities

```text
Capability
Pattern
Control
Playbook
Template
MaturityAssessment
ClientAssessment
```

## 7.2 Capability entity

| Field | Type | Description |
|---|---|---|
| capability_id | string | Unique capability identifier |
| capability_name | string | Display name |
| capability_layer | string | Data foundation, governance, AI enablement, etc. |
| architecture_layer | list | Architecture placement |
| bfsi_domains | list | Banking, insurance, wealth, fraud, etc. |
| ai_impact | list | AI role / impact categories |
| risk_level | string | Low, medium, high, very high |
| related_patterns | list | Linked architecture patterns |
| related_controls | list | Linked controls |
| maturity_applicability | list | Relevant maturity levels |
| file_path | string | Markdown source path |
| status | string | Draft, reviewed, approved |

## 7.3 Pattern entity

| Field | Type | Description |
|---|---|---|
| pattern_id | string | Unique pattern identifier |
| pattern_name | string | Display name |
| business_domains | list | Applicable BFSI domains |
| capability_layers | list | Required capability layers |
| ai_impact | list | AI role categories |
| risk_level | string | Risk rating |
| related_controls | list | Controls required |
| related_capabilities | list | Capabilities required |
| reference_architectures | list | AWS, Azure, Snowflake, Databricks, hybrid |
| file_path | string | Markdown source path |
| status | string | Draft, reviewed, approved |

## 7.4 Control entity

| Field | Type | Description |
|---|---|---|
| control_id | string | Unique control identifier |
| control_name | string | Display name |
| control_type | string | Data, AI, security, regulatory, operational |
| risk_area | string | Main risk addressed |
| evidence_required | list | Evidence artefacts |
| related_patterns | list | Patterns using the control |
| related_capabilities | list | Capabilities requiring the control |

## 7.5 Client assessment entity

| Field | Type | Description |
|---|---|---|
| assessment_id | string | Unique assessment identifier |
| client_name | string | Client or anonymised client name |
| business_domain | string | BFSI domain |
| use_case | string | Use case name |
| ai_role | string | AI role classification |
| risk_level | string | Overall risk |
| current_scores | dictionary | Capability to current maturity score |
| target_scores | dictionary | Capability to target maturity score |
| selected_patterns | list | Recommended patterns |
| required_controls | list | Required controls |
| roadmap | list | Delivery phases |
| created_date | date | Assessment date |

---

## 8. Dashboard module 1: Capability Browser

## 8.1 Purpose

Help consultants browse and understand practice capabilities.

The Capability Browser answers:

```text
What capabilities exist?
Where do they sit in the architecture?
Which domains and AI use cases do they support?
Which controls and patterns are related?
```

## 8.2 Features

- Search capability by name or keyword
- Filter by:
  - capability layer
  - BFSI domain
  - AI impact
  - risk level
  - maturity level
  - status
- Display capability cards
- Show related patterns
- Show related controls
- Open source Markdown file
- Export filtered list to CSV

## 8.3 Example filters

```text
Capability layer: AI Enablement
BFSI domain: Regulatory Reporting
AI impact: Reasoning Assistant
Risk level: High
```

Expected output:

```text
Relevant capabilities:
- Semantic Layer
- RAG Knowledge Layer
- AI Evaluation
- AI Observability
- Data Product
- Lineage
- Data Quality
```

## 8.4 Page layout

```text
Capability Browser
│
├── Filter panel
│   ├── Search
│   ├── Capability layer
│   ├── Domain
│   ├── AI impact
│   ├── Risk level
│   └── Status
│
├── Capability list / cards
│   ├── Capability name
│   ├── Layer
│   ├── Risk
│   ├── AI relevance
│   └── Related patterns count
│
└── Capability detail panel
    ├── Summary
    ├── Architecture layer
    ├── Related patterns
    ├── Related controls
    ├── Maturity applicability
    └── Source file link
```

## 8.5 Minimum viable fields

| Field | Required? |
|---|---:|
| capability_id | Yes |
| capability_name | Yes |
| capability_layer | Yes |
| bfsi_domains | Yes |
| ai_impact | Yes |
| risk_level | Yes |
| related_patterns | Yes |
| related_controls | Yes |
| file_path | Yes |

---

## 9. Dashboard module 2: Pattern Browser

## 9.1 Purpose

Help consultants select reusable architecture patterns for a client use case.

The Pattern Browser answers:

```text
Which reusable pattern should we apply?
What problem does it solve?
What capabilities and controls does it require?
What artefacts does it produce?
```

## 9.2 Features

- Search pattern by name or use case
- Filter by:
  - BFSI domain
  - AI role
  - risk level
  - required capability
  - control type
  - reference architecture platform
- Display pattern cards
- Show capability dependencies
- Show control gates
- Show delivery artefacts
- Link to playbooks and templates

## 9.3 Example filters

```text
Domain: Fraud
AI role: Decision Support
Risk level: High
```

Expected output:

```text
Recommended patterns:
- Fraud Signal Layer
- AI Copilot over Data Products
- Agentic Workflow with Human Approval
- AI Evaluation and Monitoring Framework
```

## 9.4 Page layout

```text
Pattern Browser
│
├── Filter panel
│
├── Pattern catalogue
│   ├── Pattern name
│   ├── Problem solved
│   ├── Domain
│   ├── AI impact
│   ├── Risk level
│   └── Required controls
│
└── Pattern detail panel
    ├── When to use
    ├── Required capabilities
    ├── Control gates
    ├── Reference architecture options
    ├── Common risks
    ├── Artefacts produced
    └── Related playbooks/templates
```

## 9.5 Pattern recommendation logic

For MVP 2, use simple rule-based matching.

Suggested score:

```text
pattern_score =
  domain_match_count
+ ai_impact_match_count
+ capability_match_count
+ risk_level_match
+ control_match_count
```

The dashboard can show:

```text
Recommended
Relevant
Possible
Low match
```

---

## 10. Dashboard module 3: Maturity Heatmap

## 10.1 Purpose

Help consultants assess current vs target maturity across Data & AI capabilities.

The Maturity Heatmap answers:

```text
Where is the client today?
Where do they need to be?
Which gaps matter most?
What should be prioritised?
```

## 10.2 Features

- Select or create client assessment
- Score capabilities from 0 to 5
- Set target maturity from 0 to 5
- Calculate gap
- Assign risk level and priority
- Visualise heatmap
- Export maturity assessment
- Generate roadmap inputs

## 10.3 Maturity scale

```text
0 = Not present
1 = Fragmented
2 = Repeatable
3 = Governed
4 = Industrialised
5 = Adaptive
```

## 10.4 Heatmap structure

Rows:

```text
Capabilities
```

Columns:

```text
Current maturity
Target maturity
Gap
Risk
Priority
Notes
```

Example:

| Capability | Current | Target | Gap | Risk | Priority |
|---|---:|---:|---:|---|---|
| Data Quality | 2 | 4 | 2 | High | High |
| Lineage | 1 | 4 | 3 | High | High |
| Semantic Layer | 1 | 3 | 2 | Medium | High |
| AI Evaluation | 0 | 3 | 3 | High | High |
| AI Observability | 1 | 4 | 3 | Medium | Medium |

## 10.5 Priority logic

For MVP 2, use a simple formula.

```text
gap = target_score - current_score

priority_score =
  gap
+ risk_weight
+ dependency_weight
```

Suggested risk weights:

```text
Low = 0
Medium = 1
High = 2
Very High = 3
```

Priority:

```text
0-1 = Low
2-3 = Medium
4+  = High
```

## 10.6 Page layout

```text
Maturity Heatmap
│
├── Assessment selector
├── Domain / use case / AI role summary
├── Scoring table
├── Heatmap visual
├── Priority gaps
├── Suggested roadmap phases
└── Export section
```

---

## 11. Dashboard module 4: Control Matrix

## 11.1 Purpose

Help consultants map required controls to capabilities, patterns and client use cases.

The Control Matrix answers:

```text
What controls are required?
Which patterns require them?
What evidence is needed?
Where are the control gaps?
```

## 11.2 Features

- Filter by:
  - pattern
  - capability
  - control type
  - risk level
  - domain
- Display pattern x control matrix
- Show evidence requirements
- Show current vs target control maturity
- Export control matrix
- Link to production readiness checklist

## 11.3 Control categories

```text
Data controls
AI controls
Security controls
Regulatory controls
Operational controls
Delivery controls
```

## 11.4 Example control matrix

| Pattern | Data Quality | Lineage | Access Control | AI Evaluation | Human Approval | Evidence |
|---|---:|---:|---:|---:|---:|---:|
| Governed RAG | Partial | Yes | Yes | Yes | Partial | Yes |
| Regulatory Reporting Data Layer | Yes | Yes | Yes | Partial | Yes | Yes |
| Fraud Signal Layer | Yes | Yes | Yes | Yes | Yes | Yes |
| AI Copilot over Data Products | Yes | Yes | Yes | Yes | Depends | Yes |
| Agentic Workflow | Yes | Yes | Yes | Yes | Yes | Yes |

## 11.5 Evidence examples

| Control | Evidence |
|---|---|
| Data quality | Rule results, exception logs, DQ dashboard |
| Lineage | Source-to-output lineage, transformation mapping |
| Access control | Role matrix, policy config, test evidence |
| Prompt policy | Approved prompt templates, refusal rules |
| Retrieval grounding | Retrieval test results, citation checks |
| AI evaluation | Evaluation dataset, scorecard, regression results |
| Human approval | Workflow approval logs, case notes |
| Evidence retention | Audit log, storage policy, retention config |

## 11.6 Page layout

```text
Control Matrix
│
├── Filter panel
├── Pattern x control matrix
├── Control detail panel
│   ├── Description
│   ├── Risk addressed
│   ├── Evidence required
│   ├── Related capabilities
│   └── Related patterns
├── Control gap summary
└── Export section
```

---

## 12. Dashboard module 5: Client Assessment View

## 12.1 Purpose

Provide an engagement-level summary of a client or use case assessment.

The Client Assessment View answers:

```text
What is the client trying to achieve?
What is the current maturity?
Which patterns apply?
What controls are required?
What roadmap should we recommend?
```

## 12.2 Features

- Create new assessment
- Capture:
  - client / business unit
  - domain
  - use case
  - AI role
  - decision impact
  - current maturity
  - target maturity
  - selected patterns
  - required controls
  - roadmap
- Display assessment summary
- Export Markdown executive summary
- Export capability heatmap
- Export control matrix
- Export delivery roadmap

## 12.3 Assessment workflow

```text
1. Create assessment
2. Classify domain and use case
3. Classify AI role and decision impact
4. Select relevant capabilities
5. Score current and target maturity
6. Select recommended patterns
7. Confirm required controls
8. Generate roadmap
9. Export executive summary
```

## 12.4 Page layout

```text
Client Assessment
│
├── Assessment details
│   ├── Client
│   ├── Business unit
│   ├── Domain
│   ├── Use case
│   ├── AI role
│   └── Risk level
│
├── Maturity summary
│   ├── Average current score
│   ├── Average target score
│   ├── Top gaps
│   └── Heatmap
│
├── Recommended patterns
│
├── Required controls
│
├── Suggested roadmap
│
└── Export outputs
```

## 12.5 Example executive summary output

```text
The client is seeking to improve [business process] across [domain].

The current assessment indicates maturity is strongest in [strengths] and weakest in [gaps].

Because the AI role is classified as [AI role] with [risk level] impact, the solution requires controls across [control areas].

Recommended reusable patterns:
- [Pattern 1]
- [Pattern 2]
- [Pattern 3]

The proposed roadmap is:
1. Stabilise foundations
2. Implement governed pattern
3. Pilot with controlled users
4. Industrialise controls and monitoring
5. Scale across additional domains
```

---

## 13. MVP 2 technical approach

## 13.1 Recommended implementation

Use **Streamlit** for MVP 2.

Reasons:

- fast to build
- simple local deployment
- works well with Markdown/YAML
- easy tables, filters and charts
- can later connect to RAG assistant
- fits local-first practice-building workflow

Suggested app structure:

```text
dashboard/
│
├── app.py
├── pages/
│   ├── 1_Capability_Browser.py
│   ├── 2_Pattern_Browser.py
│   ├── 3_Maturity_Heatmap.py
│   ├── 4_Control_Matrix.py
│   └── 5_Client_Assessment.py
│
├── services/
│   ├── content_loader.py
│   ├── metadata_parser.py
│   ├── recommendation_engine.py
│   ├── assessment_store.py
│   └── export_service.py
│
├── components/
│   ├── filters.py
│   ├── cards.py
│   ├── heatmap.py
│   └── tables.py
│
├── data/
│   ├── assessments/
│   └── cache/
│
└── README.md
```

## 13.2 Content loader

The content loader should:

- scan Markdown files
- extract YAML front matter
- parse file path and type
- validate required metadata fields
- return structured records
- cache results for dashboard performance

Supported content types:

```text
capability
pattern
playbook
template
control
maturity_model
design_doc
```

## 13.3 Assessment store

For MVP 2, store assessments locally as YAML or JSON.

Example:

```yaml
assessment_id: client_fraud_copilot_assessment_001
client_name: Example Bank
business_domain: fraud
use_case: Fraud Investigation Copilot
ai_role: decision_support
risk_level: high
current_scores:
  data_quality: 2
  lineage: 1
  semantic_layer: 1
  ai_evaluation: 0
target_scores:
  data_quality: 4
  lineage: 4
  semantic_layer: 3
  ai_evaluation: 3
selected_patterns:
  - fraud_signal_layer
  - ai_copilot_over_data_products
  - agentic_workflow_human_approval
required_controls:
  - access_control
  - ai_evaluation
  - audit_logging
  - human_approval
```

---

## 14. Export outputs

MVP 2 should support export to:

```text
Markdown
CSV
YAML / JSON
```

Recommended exports:

| Export | Format | Purpose |
|---|---|---|
| Capability list | CSV | Practice inventory |
| Pattern recommendations | Markdown | Proposal input |
| Maturity heatmap | CSV / Markdown | Assessment output |
| Control matrix | CSV / Markdown | Governance review |
| Client assessment summary | Markdown | Executive summary |
| Roadmap | Markdown | Delivery planning |

---

## 15. MVP 2 delivery phases

## Phase 1: Data loading and metadata validation

Build:

- Markdown scanner
- YAML front matter parser
- metadata validation
- content records dataframe
- basic dashboard home page

Output:

- loaded capabilities
- loaded patterns
- loaded controls
- validation error report

## Phase 2: Capability and pattern browsers

Build:

- filters
- search
- cards/table views
- detail panels
- source file links

Output:

- Capability Browser
- Pattern Browser

## Phase 3: Maturity heatmap

Build:

- maturity scoring table
- current vs target gap
- priority calculation
- heatmap visual
- export to CSV/Markdown

Output:

- Maturity Heatmap module

## Phase 4: Control matrix

Build:

- pattern x control view
- control filters
- evidence requirements
- export function

Output:

- Control Matrix module

## Phase 5: Client assessment view

Build:

- create assessment form
- save/load assessment
- recommended patterns
- maturity summary
- control summary
- roadmap text
- executive summary export

Output:

- Client Assessment View

---

## 16. MVP 2 success criteria

MVP 2 is successful when a consultant can:

- browse capabilities by domain, layer, AI impact and risk
- identify relevant patterns for a client use case
- score current and target maturity
- view priority gaps
- map required controls
- create a simple client assessment
- export an executive summary
- reuse the outputs in proposals or engagement planning

Minimum success test:

```text
Given a use case such as "fraud investigation copilot",
the dashboard should help a consultant identify:
- relevant capabilities
- current vs target maturity gaps
- recommended patterns
- required controls
- initial delivery roadmap
- executive summary draft
```

---

## 17. Future evolution: MVP 3 AI Assistant

MVP 2 should prepare for MVP 3.

MVP 3 AI Assistant should use the dashboard metadata and knowledge base to:

- answer questions about capabilities and patterns
- recommend architecture patterns
- generate consultant discovery questions
- draft maturity assessments
- produce control matrices
- draft executive summaries
- generate roadmap options
- explain why a pattern is recommended

MVP 2 therefore needs clean metadata.

The better the metadata, the better the AI reasoning assistant.

```text
MVP 1: Knowledge scaffold
        ↓
MVP 2: Dashboard and assessment views
        ↓
MVP 3: AI reasoning assistant
```

---

## 18. Recommended folder placement

This design document belongs in:

```text
00_overview/mvp2_dashboard_design.md
```

Alternative location:

```text
10_design_docs/mvp2_dashboard_design.md
```

If you want to keep the scaffold simple, use:

```text
00_overview/mvp2_dashboard_design.md
```

If the project grows, create:

```text
10_design_docs/
```

Recommended:

```text
10_design_docs/mvp2_dashboard_design.md
```

because this is a system design artefact, not a general overview page.

---

## 19. Open design decisions

| Decision | Options | Recommendation |
|---|---|---|
| Dashboard tool | Streamlit / Retool / Power BI / Fabric | Streamlit for MVP |
| Source of truth | Markdown/YAML / database | Markdown/YAML |
| Assessment storage | YAML / JSON / SQLite | YAML or JSON for MVP |
| Heatmap visual | Table / chart / styled dataframe | Styled table first |
| Export format | Markdown / PDF / DOCX | Markdown first |
| Authentication | None / local / enterprise SSO | None for MVP |
| AI assistant integration | Later / embedded now | Later in MVP 3 |

---

## 20. Design principles recap

> Build the scaffold first, dashboard second, AI assistant third.

> The dashboard should make the knowledge base navigable, not replace it.

> Use metadata as the bridge between documents, assessment and AI reasoning.

> The most valuable dashboard is not a chart. It is a consultant decision-support system.

> Every dashboard output should help produce a client artefact.
