---
type: capability
capability_id: data_product
capability_name: Data Product
capability_layer: data_foundation
architecture_layer:
  - curated_layer
  - semantic_layer
  - consumption_layer
  - control_observability_layer
bfsi_domains:
  - banking
  - insurance
  - wealth
  - regulatory_reporting
  - fraud
  - risk_and_compliance
ai_impact:
  - ai_as_knowledge_interface
  - ai_as_reasoning_assistant
  - ai_as_decision_support
risk_level: high
maturity_applicability:
  - level_1_fragmented
  - level_2_standardising
  - level_3_governed
  - level_4_industrialised
  - level_5_adaptive
related_patterns:
  - regulatory_reporting_data_layer
  - semantic_layer_for_ai
  - ai_copilot_over_data_products
  - fraud_signal_layer
  - source_to_report_lineage
  - data_quality_control_framework
related_controls:
  - data_ownership
  - data_quality
  - access_control
  - lineage
  - semantic_certification
  - reconciliation
  - audit_logging
  - evidence_retention
---

# Data Product

## 1. Definition

A Data Product is a governed, reusable, business-aligned data asset designed to serve a defined set of users, decisions, analytics, reporting or AI use cases.

Unlike a raw table, pipeline output or one-off report dataset, a data product has clear ownership, defined business meaning, quality expectations, access controls, lineage, documentation and consumption patterns.

In BFSI, a data product may represent a reusable domain-aligned asset such as:

- Customer data product
- Account data product
- Transaction data product
- Product holdings data product
- Policy data product
- Claims data product
- Fraud alert data product
- Regulatory reporting data product
- Risk exposure data product
- Financial crime monitoring data product

The design principle:

> A data product is not just data. It is data packaged with meaning, controls, accountability and consumption readiness.

## 2. Why it matters in BFSI

BFSI organisations rely on data for regulatory reporting, risk management, fraud detection, customer servicing, operational decisioning, compliance monitoring and executive reporting.

Without well-designed data products, organisations often face:

- duplicated data pipelines
- inconsistent customer, account or transaction definitions
- fragmented reporting logic
- unclear data ownership
- poor traceability from source to output
- weak data quality accountability
- uncontrolled downstream usage
- repeated project-by-project data remediation
- difficulty scaling AI safely

Data products help shift the organisation from project-specific data delivery to reusable enterprise capability.

For BFSI, the value is especially strong because the same core entities are reused across many domains:

```text
Customer → KYC, AML, servicing, credit risk, fraud, regulatory reporting
Account  → balances, transactions, limits, tax, reporting, conduct risk
Transaction → fraud, AML, disputes, payments, analytics, customer behaviour
Policy / Claim → underwriting, claims, customer service, risk, regulatory reporting
```

## 3. What changed because of AI

Before GenAI, data products primarily served dashboards, reports, analytics and downstream applications.

With AI, data products may become trusted context for:

- AI copilots
- RAG systems
- natural-language analytics
- decision-support workflows
- agentic workflows
- automated exception triage
- model features and signals
- business explanations and summaries

This raises the bar.

A data product is no longer only consumed by humans who can interpret limitations. It may be consumed by AI systems that generate fluent answers, recommendations or workflow actions.

AI can amplify both value and risk.

If the data product is well governed, AI can:

- explain business entities and metrics
- retrieve trusted context
- support analysts and operational teams
- summarise exceptions
- generate consistent business narratives
- support controlled decision workflows

If the data product is weak, AI can:

- confidently explain incorrect data
- use inconsistent definitions
- hide data quality gaps behind fluent language
- create misleading recommendations
- expose restricted information
- scale poor-quality outputs across many users

The AI-era design principle:

> Data products must be AI-ready before they are exposed as trusted AI context.

## 4. Architecture placement

Data products usually sit above raw and standardised data layers and below semantic, AI and business consumption layers.

```text
Enterprise Sources
   ↓
Ingestion Layer
   ↓
Raw / Landing Layer
   ↓
Standardised Layer
   ↓
Curated / Conformed Layer
   ↓
Data Product Layer
   - owned domain datasets
   - quality rules
   - business definitions
   - access controls
   - lineage
   - documentation
   - service-level expectations
   ↓
Semantic / Feature / Signal / RAG Context Layers
   ↓
Consumption
   - dashboards
   - regulatory reports
   - APIs
   - AI copilots
   - ML models
   - operational workflows
```

Cross-cutting concerns:

```text
Governance
Security
Lineage
Data quality
Metadata
DataOps
Cost management
Observability
Evidence retention
```

## 5. Data product types

Not all data products serve the same purpose.

| Type | Description | BFSI example |
|---|---|---|
| Entity data product | Represents a core business entity | Customer, Account, Policy, Claim |
| Event data product | Represents business events | Transaction, Payment, Trade, Claim Event |
| Analytical data product | Supports analytics and reporting | Customer profitability, product performance |
| Regulatory data product | Supports governed reporting obligations | ATO reporting, APRA reporting, FATCA/CRS |
| Risk data product | Supports risk measurement and monitoring | Credit exposure, AML risk profile |
| AI-ready data product | Certified for AI or model consumption | Fraud signal context, copilot-ready customer summary |
| Operational data product | Supports process execution | Claims triage queue, exception management dataset |
| Reference data product | Provides controlled lookup values | Product codes, branch codes, jurisdiction codes |

## 6. Required controls

Typical controls include:

| Control | Purpose |
|---|---|
| Data ownership | Assign accountable owner and steward |
| Business definition | Define the meaning and intended use of the data product |
| Source lineage | Trace data back to authoritative systems |
| Transformation lineage | Show how data is derived, transformed and aggregated |
| Data quality rules | Monitor completeness, accuracy, timeliness and validity |
| Access control | Enforce role-based or attribute-based access |
| Data classification | Identify sensitivity, PII and regulatory restrictions |
| Reconciliation | Validate totals, balances or record counts where required |
| Usage policy | Define permitted and prohibited use cases |
| SLA / SLO | Define freshness, availability and support expectations |
| Change control | Manage schema, logic and definition changes |
| Evidence retention | Retain control results, approvals and certification records |
| AI readiness certification | Confirm the data product is safe for AI consumption where applicable |

## 7. Common implementation options

| Platform area | Options |
|---|---|
| Data platform | Snowflake, Databricks, Redshift, Synapse, BigQuery |
| Transformation | dbt, Spark, SQL, Databricks Workflows, Glue |
| Data quality | dbt tests, Great Expectations, Soda, Deequ, custom SQL controls |
| Metadata/catalogue | Collibra, Alation, Purview, DataHub, OpenMetadata |
| Lineage | OpenLineage, dbt lineage, Purview, Collibra lineage, platform-native lineage |
| Access control | RBAC, ABAC, masking policies, row-level security, column-level security |
| APIs | GraphQL, REST, data service layer, semantic query service |
| CI/CD | GitHub Actions, Azure DevOps, GitLab CI, Terraform, CDK |
| Observability | Monte Carlo, Bigeye, Datadog, CloudWatch, Azure Monitor |
| Documentation | Markdown, catalogue entries, data contracts, semantic definitions |

## 8. Data product contract

A mature data product should have a clear contract.

```yaml
data_product_id: customer_core
name: Customer Core Data Product
domain: banking_customer
owner: Head of Customer Data
steward: Customer Data Steward
description: Governed customer master and profile data for analytics, reporting and AI consumption.
primary_consumers:
  - risk_analytics
  - fraud_operations
  - customer_service
  - regulatory_reporting
sources:
  - crm
  - core_banking
  - onboarding_platform
critical_data_elements:
  - customer_id
  - legal_name
  - date_of_birth
  - tax_residency_status
  - kyc_status
quality_rules:
  - customer_id_not_null
  - customer_id_unique
  - kyc_status_valid
  - tax_residency_status_valid
access_policy:
  pii_masking: required
  row_level_security: required
lineage_required: true
ai_ready: conditional
certification_status: draft
```

## 9. Maturity model

| Level | Description |
|---|---|
| Level 1 — Fragmented | Data assets exist as project tables, extracts or report datasets with limited ownership |
| Level 2 — Standardising | Common domain datasets are emerging, but ownership, quality and metadata are inconsistent |
| Level 3 — Governed | Data products have defined owners, quality rules, lineage, access controls and documentation |
| Level 4 — Industrialised | Data products are versioned, monitored, tested through CI/CD and reused across use cases |
| Level 5 — Adaptive | Data products are continuously improved using usage metrics, quality trends, AI feedback and control evidence |

## 10. Common failure modes

Common failure modes include:

- calling every dataset a data product without changing ownership or controls
- building data products around technical systems rather than business domains
- no clear owner accountable for quality and usage
- no documented business definition
- no explicit consumers or intended use cases
- no SLA for freshness or availability
- lineage is incomplete or not trusted
- access controls are inherited informally from platform defaults
- data quality rules are not linked to business outcomes
- downstream users create conflicting derived versions
- AI copilots consume data products that are not certified for AI use
- product documentation is created once but not maintained
- change impact is not assessed before schema or logic changes

## 11. Consultant discovery questions

Use these questions during assessment, solution shaping or delivery planning.

### Business questions

- What business outcome does this data product support?
- Who are the primary consumers?
- What decisions, reports, workflows or AI use cases depend on it?
- Who owns the data product?
- Who is accountable for quality and issue resolution?
- Is the data product used for regulatory, customer-impacting or financial decisions?

### Data questions

- What source systems provide the data?
- Which system is authoritative for each critical field?
- What are the critical data elements?
- What transformations or business rules are applied?
- What quality rules are required?
- What reconciliation checks are needed?
- What lineage must be captured?

### Consumption questions

- Will the data be consumed through SQL, APIs, dashboards, semantic layer, ML features or AI copilots?
- What freshness is required?
- What availability is required?
- What level of aggregation is required?
- What access patterns are expected?
- Are there different views for different user groups?

### AI-specific questions

- Will the data product be exposed to AI assistants or agents?
- Is it certified as trusted AI context?
- Are business definitions clear enough for AI explanation?
- Are sensitive fields masked or filtered?
- Can AI determine whether the data is current and certified?
- Should AI refuse to use this data product under certain conditions?
- Are prompt, retrieval and output logs required when this data product is used?

### Governance questions

- What policies apply to this data product?
- What regulatory obligations depend on it?
- What evidence must be retained?
- What approvals are required before production release?
- How are changes governed?
- How are incidents or quality breaches escalated?

## 12. Related architecture patterns

### Regulatory Reporting Data Layer

Data products can provide certified reporting-ready datasets for ATO, APRA, AML, FATCA/CRS and other obligations.

Key controls include lineage, reconciliation, deterministic business rules, sign-off and evidence retention.

### Semantic Layer for AI

Semantic data products expose certified metrics, dimensions and business definitions that AI systems can safely reason over.

Key controls include metric ownership, formula certification, access control and change management.

### AI Copilot over Data Products

AI copilots can answer questions, generate summaries and support decision workflows using governed data products.

Key controls include semantic grounding, tool restrictions, prompt policy, evaluation and audit logging.

### Fraud Signal Layer

Fraud data products provide transaction, customer, account, merchant, device and alert context for signal generation and investigation support.

Key controls include signal versioning, explainability, false-positive tracking and analyst feedback.

### Source-to-Report Lineage

Data products should participate in source-to-output lineage so that downstream reports, AI outputs and decisions can be traced back to source data and transformations.

## 13. Reusable artefacts

This capability should produce or reuse:

- Data product canvas
- Data product contract template
- Data owner and steward assignment template
- Critical Data Element register
- Data quality rule catalogue
- Access control matrix
- Lineage template
- Data product certification checklist
- AI readiness checklist
- SLA / SLO template
- Data product release checklist
- Change impact assessment
- Consumer onboarding guide
- Evidence pack template
- Executive summary template

## 14. Example logical architecture

```text
Consumers
  ├── Dashboards
  ├── Regulatory Reports
  ├── APIs
  ├── ML Models
  ├── AI Copilots
  └── Operational Workflows
        ↑
Data Product Interface
  ├── SQL views
  ├── APIs
  ├── semantic objects
  ├── certified extracts
  └── feature/signal outputs
        ↑
Data Product Core
  ├── business definitions
  ├── curated datasets
  ├── quality rules
  ├── access policies
  ├── lineage
  ├── documentation
  └── certification status
        ↑
Platform Foundation
  ├── ingestion
  ├── transformation
  ├── storage
  ├── orchestration
  ├── CI/CD
  └── monitoring
        ↑
Enterprise Sources
  ├── core banking
  ├── CRM
  ├── payments
  ├── policy administration
  ├── claims
  └── finance / risk systems
```

## 15. Example use case: Customer Data Product

```text
Business outcome:
Provide a reusable, governed view of customer identity, profile, KYC and relationship information.

Users:
Risk analysts, fraud analysts, customer service teams, regulatory reporting teams, AI copilots.

Data required:
Customer master records, onboarding data, KYC status, tax residency, contact details, customer relationships.

Controls:
- PII classification and masking
- customer_id uniqueness
- KYC status validity
- source lineage
- access segmentation by user role
- change approval for business rules
- certification before AI consumption

AI use:
AI can explain customer context, summarise risk indicators, support investigation and retrieve relevant profile information, but should not make adverse customer decisions without human review.
```

## 16. Example use case: Transaction Data Product

```text
Business outcome:
Provide a trusted transaction dataset for fraud, AML, analytics, customer behaviour and regulatory reporting.

Users:
Fraud operations, AML teams, finance, analytics, risk, AI investigation copilots.

Data required:
Transaction ID, account ID, customer ID, merchant, amount, currency, timestamp, channel, status, device and location attributes.

Controls:
- completeness and timeliness checks
- duplicate transaction detection
- reconciliation to source totals
- access control for sensitive transaction attributes
- lineage from payment and banking systems
- signal readiness for fraud and AML use cases

AI use:
AI can summarise transaction patterns, explain triggered alerts, support investigation and identify anomalies, but high-impact decisions require governed rules and analyst approval.
```

## 17. Production readiness checklist

Before production, confirm:

- [ ] Business owner is assigned
- [ ] Data steward is assigned
- [ ] Intended consumers are documented
- [ ] Intended use cases are documented
- [ ] Source systems are identified
- [ ] Authoritative sources are confirmed
- [ ] Critical Data Elements are defined
- [ ] Business definitions are documented
- [ ] Data quality rules are implemented
- [ ] Reconciliation rules are defined where required
- [ ] Access control is implemented
- [ ] Data classification is completed
- [ ] Lineage is captured
- [ ] SLA / SLO is defined
- [ ] Monitoring is implemented
- [ ] Change management process is defined
- [ ] Consumer onboarding guide exists
- [ ] Evidence retention is defined
- [ ] AI readiness has been assessed if AI consumption is expected
- [ ] Certification status is recorded

## 18. Example executive narrative

A data product approach helps BFSI organisations move away from duplicated, project-specific data delivery toward reusable, governed enterprise data assets.

The key is not simply packaging tables. The key is assigning ownership, defining business meaning, embedding quality controls, enforcing access, capturing lineage and making consumption patterns explicit.

As AI adoption grows, data products become even more important because they define what data can be safely exposed as trusted context for copilots, analytics assistants, decision-support workflows and models.

The target state is a portfolio of governed, reusable and AI-ready data products that reduce delivery duplication, improve trust and accelerate business value.

## 19. Design principles

> A data product must have an accountable owner, not just a technical pipeline.

> A data product should be designed around business meaning and consumption, not just source-system structure.

> AI should only consume data products when quality, access, lineage and certification status are clear.

> Reuse comes from trust. Trust comes from ownership, controls and evidence.
