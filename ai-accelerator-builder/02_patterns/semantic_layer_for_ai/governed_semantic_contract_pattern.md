---
type: pattern
status: draft
risk_level: high
business_domains:
  - Business Banking
  - Fraud Detection
  - Financial Crime
  - Risk Management
  - Customer Operations
capability_layers:
  - Data Governance
  - Semantic Layer
  - AI Governance
  - Model Risk Management
  - Data Quality
  - Lineage
  - Policy Enforcement
  - Human-in-the-loop Review
ai_impact:
  - Accelerates semantic packaging
  - Improves reviewability of data logic
  - Supports governed AI reasoning
  - Reduces ambiguity in fraud-related metrics and signals
  - Enables reusable AI accelerators
related_controls:
  - Data quality controls
  - Policy usage controls
  - Access controls
  - Certification gates
  - Human review controls
  - Lineage controls
  - Model output usage controls
---

# Governed Semantic Contract for AI

## 1. Problem solved

Enterprise AI often fails because the model is introduced before the business logic is trusted.

In many organisations, important data logic is scattered across SQL, Python notebooks, dashboards, feature pipelines, spreadsheets, business glossaries, policy documents, and tribal knowledge.

This creates several problems:

- business users cannot easily review what the logic means
- data teams cannot prove which definitions are certified
- AI systems may reason over unclear or uncertified context
- metrics and signals may be reused without understanding their limitations
- high-risk outputs may be used for decisions they were never approved for

This pattern solves the problem by converting existing enterprise data, code, features, metrics, controls, and assumptions into a **governed semantic contract**.

The semantic contract defines what an AI system is allowed to reason over, how the logic is validated, what the approved use cases are, and where human review is required.

Core principle:

**AI proposes. Rules validate. Humans certify.**

---

## 2. When to use

Use this pattern when an organisation wants to make enterprise data and business logic safe for AI consumption.

It is especially useful when:

- business logic is complex, fragmented, or poorly documented
- AI copilots, agents, or analyst-assist workflows need trusted business context
- semantic definitions need to be reviewed and certified by business owners
- fraud, risk, compliance, lending, claims, or customer decisioning use cases are involved
- deterministic controls are required before LLM reasoning
- the organisation wants reusable AI accelerators rather than one-off chatbot prototypes
- existing code, SQL, features, and metrics need to be packaged into a governed artefact

Example use cases:

- Business Banking Fraud Detection
- Credit Risk Review
- Customer Churn Investigation
- Home Loan Payment Delinquency Review
- Complaints Management
- Operational Risk Event Review
- Regulatory Reporting Metrics
- Claims Triage and Review

---

## 3. Business outcomes

This pattern creates business value by making enterprise data logic reviewable, certifiable, reusable, and safe for AI-enabled workflows.

Expected outcomes:

- faster conversion of existing data logic into governed AI-ready assets
- clearer business ownership of metrics, signals, and definitions
- improved trust in AI-assisted analysis
- reduced risk of AI using uncertified or ambiguous data
- stronger auditability for high-risk use cases
- better separation between AI suggestion and business decisioning
- reusable semantic packages across domains and projects
- faster consulting delivery through repeatable accelerator patterns

For fraud detection specifically, the outcome is not automated customer action.

The outcome is a trusted semantic package that supports analyst review while clearly defining approved use, disallowed use, caveats, access rules, and certification blockers.

---

## 4. Logical architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                  Existing Enterprise Logic                   │
├──────────────────────────────────────────────────────────────┤
│ Data Sources │ SQL │ Features │ Metrics │ Policies │ Glossary │
│ Dashboards   │ Code │ Models   │ Rules   │ Lineage  │ Controls │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                  Semantic_Foundry Accelerator                 │
├──────────────────────────────────────────────────────────────┤
│ 1. Scan / ingest existing logic                               │
│ 2. Extract candidate semantic components                      │
│ 3. Generate draft definitions and metadata                    │
│ 4. Validate using deterministic rules                         │
│ 5. Package into reviewable semantic contract                  │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                     Semantic Package                         │
├──────────────────────────────────────────────────────────────┤
│ Business Entities                                            │
│ - Customer                                                   │
│ - Account                                                    │
│ - Transaction                                                │
│ - Fraud Alert                                                │
│ - Model Run                                                  │
│                                                              │
│ Behavioural Signals                                          │
│ - Amount Spike                                               │
│ - Velocity Burst                                             │
│ - Statistical Anomaly                                        │
│ - Account Burst History                                      │
│                                                              │
│ Prediction Outputs                                           │
│ - Predicted Fraud                                            │
│ - Fraud Score                                                │
│                                                              │
│ Evaluation Metrics                                           │
│ - Precision                                                  │
│ - Recall                                                     │
│ - F1 Score                                                   │
│                                                              │
│ Governance Assets                                            │
│ - Data quality rules                                         │
│ - Policy rules                                               │
│ - Lineage                                                    │
│ - Draft semantic SQL views                                   │
│ - AI context cards                                           │
│ - Certification report                                       │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                    Validation and Certification              │
├──────────────────────────────────────────────────────────────┤
│ AI proposes                                                  │
│ - definitions                                                │
│ - catalogue entries                                          │
│ - AI usage cards                                             │
│ - draft documentation                                        │
│                                                              │
│ Rules validate                                               │
│ - schema checks                                              │
│ - naming checks                                              │
│ - formula checks                                             │
│ - DQ checks                                                  │
│ - SQL validity                                               │
│ - policy boundaries                                          │
│ - access rules                                               │
│ - certification gates                                        │
│                                                              │
│ Humans certify                                               │
│ - review business meaning                                    │
│ - approve intended use                                       │
│ - confirm caveats                                            │
│ - certify for controlled use                                 │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                  Governed Semantic Contract                  │
├──────────────────────────────────────────────────────────────┤
│ Reviewable │ Certifiable │ Reusable │ Trusted │ Auditable     │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                 Downstream AI Consumption                    │
├──────────────────────────────────────────────────────────────┤
│ AI Copilots │ Analyst Assist │ RAG │ Agents │ Dashboards      │
│                                                              │
│ Constraint: AI may reason only over certified semantic        │
│ context and approved usage boundaries.                       │
└──────────────────────────────────────────────────────────────┘
```

---

## 5. Reference architecture options

### Option A — Lightweight local accelerator

Best for early-stage consulting assets, demos, and internal proof-of-value.

```text
Local Files / SQL / YAML / Markdown
        │
        ▼
Semantic_Foundry CLI
        │
        ├── AI-assisted definition drafting
        ├── Deterministic validators
        ├── SQL view generation
        ├── Policy and DQ checks
        └── Certification report generation
        │
        ▼
Reviewable Semantic Package
```

Typical technologies:

- Python
- YAML / JSON
- Markdown
- Local SQL validation
- DuckDB / SQLite / Snowflake dev connection
- Git-based versioning

Use when:

- proving the accelerator concept
- creating portfolio artefacts
- building reusable consulting patterns
- demonstrating semantic governance before platform integration

---

### Option B — Enterprise data platform integration

Best for organisations with established data platforms and governance tooling.

```text
Enterprise Data Platform
Snowflake / Databricks / AWS / Azure / GCP
        │
        ▼
Metadata + Code + Feature + Metric Extraction
        │
        ▼
Semantic_Foundry Processing Layer
        │
        ├── Entity extraction
        ├── Signal extraction
        ├── Metric mapping
        ├── DQ rule mapping
        ├── Policy rule mapping
        ├── Lineage mapping
        └── Certification workflow
        │
        ▼
Governed Semantic Layer
        │
        ▼
AI Workbench / Copilot / Analyst Workflow
```

Typical technologies:

- Snowflake semantic views
- Databricks Unity Catalog
- dbt semantic layer
- AWS Glue Data Catalog
- Collibra / Alation / Microsoft Purview
- OpenLineage / Marquez
- Great Expectations / Soda / Deequ
- Bedrock / SageMaker / Azure AI / OpenAI

Use when:

- semantic contracts need to connect to enterprise metadata
- certified views need to be deployed into production
- AI systems require governed data access
- lineage, ownership, and approval workflows already exist

---

### Option C — AI Workbench control plane integration

Best for organisations moving from individual AI use cases to governed AI operating models.

```text
Semantic Package
        │
        ▼
AI Workbench Control Plane
        │
        ├── Prompt versions
        ├── Retrieval profiles
        ├── Policy enforcement
        ├── Certified context registry
        ├── Evaluation runs
        ├── Human approval workflow
        └── Promotion gates
        │
        ▼
Approved AI Behaviour Bundle
        │
        ▼
Production Copilot / Agent / Analyst Assist Workflow
```

Use when:

- multiple AI systems need consistent governance
- semantic definitions must be tied to prompt, retrieval, and evaluation controls
- AI behaviour needs promotion from dev to test to production
- auditability and repeatability are required

---

## 6. Required capabilities

### Semantic modelling

The organisation needs the ability to define and manage:

- business entities
- attributes
- relationships
- metrics
- signals
- prediction outputs
- business definitions
- calculation logic
- semantic SQL views

### Governance and certification

The organisation needs a controlled process for:

- ownership assignment
- business review
- data steward review
- policy review
- certification status
- certification conditions
- certification expiry or review cycle
- exception handling

### Deterministic validation

Validators should check:

- schema completeness
- data type consistency
- naming standards
- metric formulas
- SQL validity
- data quality rules
- policy rule coverage
- lineage completeness
- access restrictions
- certification blockers

### AI-assisted drafting

LLMs may assist with:

- drafting business definitions
- summarising logic
- suggesting catalogue descriptions
- generating AI context cards
- identifying missing caveats
- producing review notes
- explaining metric usage
- identifying ambiguous wording

However, LLMs should not be the certification authority.

### Human-in-the-loop approval

Human reviewers should confirm:

- business meaning
- intended use
- disallowed use
- customer impact
- regulatory implications
- caveats and limitations
- certification readiness

### Audit and traceability

The pattern should produce evidence of:

- source inputs
- generated outputs
- validation results
- reviewer decisions
- certification status
- policy checks
- caveats
- version history

---

## 7. Control gates

### Gate 1 — Source intake gate

Purpose:

Ensure the input logic is identifiable, versioned, and traceable.

Checks:

- source system identified
- source file or table registered
- code or SQL version captured
- owner identified
- domain identified
- business purpose documented

---

### Gate 2 — Semantic completeness gate

Purpose:

Ensure the semantic package contains enough information for business review.

Checks:

- entities defined
- attributes documented
- metrics described
- signals documented
- prediction outputs identified
- lineage captured
- AI context card drafted

---

### Gate 3 — Data quality gate

Purpose:

Ensure the semantic asset has minimum quality controls.

Checks:

- completeness rules defined
- validity rules defined
- uniqueness rules defined where required
- freshness rules defined
- reconciliation checks defined where relevant
- known data limitations documented

---

### Gate 4 — Policy usage gate

Purpose:

Ensure the semantic asset is not used outside approved boundaries.

Checks:

- approved use documented
- disallowed use documented
- required caveats documented
- human review requirement documented
- access restrictions documented
- customer impact assessed

For fraud detection:

- approved use: support analyst investigation
- disallowed use: automated adverse customer action
- required caveat: fraud score is decision support, not final determination
- human review: required before any customer-impacting action

---

### Gate 5 — Technical validation gate

Purpose:

Ensure generated artefacts are technically valid.

Checks:

- SQL compiles
- semantic views resolve
- fields exist
- joins are valid
- formulas are valid
- naming conventions are followed
- dependencies are available

---

### Gate 6 — Certification gate

Purpose:

Ensure the semantic package is ready for controlled reuse.

Checks:

- all mandatory validators passed
- business owner approved
- data owner approved
- risk or compliance review completed where required
- caveats accepted
- certification status assigned
- expiry or review date set

Possible statuses:

- Draft
- In Review
- Certified
- Certified with Conditions
- Blocked
- Retired

---

## 8. Delivery steps

### Step 1 — Select a real business use case

Start with a use case that has enough complexity to prove value.

Example:

Business Banking Fraud Detection.

The use case should include:

- business entities
- behavioural signals
- prediction outputs
- metrics
- quality rules
- usage restrictions
- human review requirements

---

### Step 2 — Inventory existing logic

Collect available artefacts:

- SQL queries
- feature definitions
- fraud rules
- model outputs
- metric definitions
- dashboard logic
- policy documents
- data quality rules
- glossary terms
- lineage information

---

### Step 3 — Generate draft semantic package

Use the accelerator to produce:

- entity definitions
- signal definitions
- metric definitions
- prediction output definitions
- draft semantic SQL views
- AI context cards
- policy usage notes
- certification report

---

### Step 4 — Run deterministic validators

Validate the generated package against:

- schema rules
- naming standards
- formula rules
- DQ expectations
- SQL syntax
- policy boundaries
- access rules
- certification requirements

---

### Step 5 — Review with business and risk stakeholders

Business and control owners review:

- meaning
- usage
- limitations
- customer impact
- human review requirements
- caveats
- certification blockers

---

### Step 6 — Certify or block

Assign certification status:

- certified for use
- certified with conditions
- blocked pending remediation
- draft only

---

### Step 7 — Publish for reuse

Publish the semantic package into the target operating environment:

- semantic catalogue
- governance tool
- Git repository
- AI workbench
- data product registry
- certified semantic layer

---

### Step 8 — Connect to AI consumption

Allow AI systems to consume only approved context.

Examples:

- fraud analyst copilot
- investigation workflow
- RAG-based explanation assistant
- metric Q&A assistant
- signal review assistant

---

### Step 9 — Monitor and refresh

Review the semantic package when:

- source logic changes
- policy changes
- model outputs change
- fraud typologies change
- data quality degrades
- usage expands
- certification expires

---

## 9. Common risks and failure modes

### Risk 1 — Treating AI-generated definitions as certified truth

LLMs can draft useful descriptions, but they can also hallucinate or overstate meaning.

Mitigation:

- require deterministic validation
- require human certification
- keep draft and certified status separate

---

### Risk 2 — Building the copilot before the semantic contract

A copilot without trusted context may produce fluent but unsafe answers.

Mitigation:

- certify semantic assets first
- restrict retrieval to approved context
- enforce policy usage boundaries

---

### Risk 3 — Unclear approved and disallowed use

High-risk outputs may be reused for decisions they were not designed to support.

Mitigation:

- explicitly document approved use
- explicitly document disallowed use
- include required caveats in AI context cards

---

### Risk 4 — Automating adverse actions from decision-support signals

Fraud scores and alerts may be misused as final decision outputs.

Mitigation:

- require human review
- block automated adverse customer action
- include customer-impact controls

---

### Risk 5 — Weak lineage

Without lineage, reviewers cannot understand where a metric or signal came from.

Mitigation:

- capture source lineage
- capture feature lineage
- capture model output lineage
- capture reporting lineage

---

### Risk 6 — Validator coverage gaps

A package may appear complete while missing important controls.

Mitigation:

- maintain a validator registry
- define mandatory validators by risk level
- report validation coverage
- block certification if mandatory checks are missing

---

### Risk 7 — Semantic drift

Business meaning can change over time while old semantic packages remain in use.

Mitigation:

- assign review dates
- monitor source changes
- version semantic packages
- retire outdated packages

---

### Risk 8 — Access control mismatch

AI systems may expose semantic context to users who are not authorised to see it.

Mitigation:

- inherit RBAC / ABAC rules
- apply access checks at retrieval time
- include access restrictions in the semantic package

---

## 10. Artefacts produced

The pattern should produce a complete semantic package.

Core artefacts:

- semantic package manifest
- business entity definitions
- attribute definitions
- behavioural signal definitions
- prediction output definitions
- metric definitions
- data quality rule set
- policy rule set
- lineage map
- draft semantic SQL views
- AI context cards
- validation report
- certification report
- approved use statement
- disallowed use statement
- required caveats
- human review requirements
- access restrictions
- certification blockers
- version history

Example package structure:

```text
semantic_package/
├── manifest.yaml
├── business_entities/
│   ├── customer.yaml
│   ├── account.yaml
│   ├── transaction.yaml
│   ├── fraud_alert.yaml
│   └── model_run.yaml
├── signals/
│   ├── amount_spike.yaml
│   ├── velocity_burst.yaml
│   ├── statistical_anomaly.yaml
│   └── account_burst_history.yaml
├── prediction_outputs/
│   ├── predicted_fraud.yaml
│   └── fraud_score.yaml
├── metrics/
│   ├── precision.yaml
│   ├── recall.yaml
│   └── f1_score.yaml
├── rules/
│   ├── data_quality_rules.yaml
│   └── policy_rules.yaml
├── lineage/
│   └── lineage_map.yaml
├── semantic_sql/
│   ├── vw_fraud_alert_context.sql
│   ├── vw_account_signal_summary.sql
│   └── vw_model_run_evaluation.sql
├── ai_context_cards/
│   ├── fraud_alert_context_card.md
│   └── fraud_score_usage_card.md
├── validation/
│   └── validation_report.md
└── certification/
    └── certification_report.md
```

---

## 11. Example executive narrative

Most organisations are trying to build AI copilots on top of data logic that the business has never properly reviewed or certified.

That is the wrong starting point.

For high-risk domains like fraud detection, the first question should not be:

“Can the AI answer questions?”

It should be:

“What certified business context is the AI allowed to reason over?”

This pattern creates that control point.

Semantic_Foundry turns existing enterprise data, SQL, features, metrics, policies, and governance assumptions into a governed semantic contract.

AI can help draft definitions, catalogue entries, and usage cards.

But deterministic validators check the hard controls: schemas, formulas, data quality rules, SQL validity, policy boundaries, access restrictions, and certification gates.

Humans then certify whether the semantic package is fit for business use.

For Business Banking Fraud Detection, this distinction matters.

A fraud alert should support analyst review.

It should not become an automated adverse action against a customer.

The real accelerator is not a chatbot and not a metadata scanner.

It is a reusable architecture pattern for turning messy enterprise logic into something the business can review, certify, reuse, and trust.

Don’t build the copilot first.

Build the semantic contract it is allowed to reason over.
