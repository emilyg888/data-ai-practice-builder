---
type: capability
capability_id: data_quality
capability_name: Data Quality
capability_layer: governance_and_trust
architecture_layer:
  - ingestion_layer
  - curated_layer
  - semantic_layer
  - ai_control_layer
bfsi_domains:
  - banking
  - insurance
  - wealth
  - regulatory_reporting
  - fraud
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
  - fraud_signal_layer
  - governed_rag_knowledge_base
  - semantic_layer_for_ai
related_controls:
  - completeness
  - accuracy
  - timeliness
  - reconciliation
  - exception_management
  - evidence_retention
---

# Data Quality

## 1. Definition

Data Quality is the capability to define, test, monitor, remediate and evidence whether data is fit for its intended business, regulatory, analytical or AI use.

In BFSI, data quality is not only a technical concern. It directly affects regulatory reporting, customer outcomes, fraud detection, risk management, compliance monitoring and AI trustworthiness.

## 2. Why it matters in BFSI

Poor data quality can lead to:

- incorrect regulatory reporting
- missed AML, fraud or risk signals
- inaccurate customer, account or transaction views
- poor credit, claims or compliance decisions
- unreliable dashboards and executive reporting
- unsafe AI outputs caused by incorrect or incomplete context

For BFSI clients, data quality needs to be treated as a control capability, not just a data engineering task.

## 3. What changed because of AI

Before AI, poor data quality usually affected reports, dashboards and downstream analytics.

With AI, poor data quality can affect reasoning, recommendations and automated workflow support.

AI increases the risk because it can:

- confidently explain incorrect data
- combine weak signals into misleading narratives
- retrieve stale or unapproved knowledge
- generate recommendations based on incomplete context
- hide data gaps behind fluent language
- scale poor-quality outputs across many users quickly

The AI-era design principle:

> Data that is not trusted should not be exposed as trusted AI context.

## 4. Architecture placement

Data Quality applies across multiple architecture layers:

```text
Source Systems
   ↓
Ingestion Layer
   ↓        DQ: schema, file, volume, format checks
Raw Layer
   ↓        DQ: completeness, duplication, basic validity
Standardised Layer
   ↓        DQ: standardisation, conformance, reference checks
Curated Layer
   ↓        DQ: business rules, reconciliation, CDE checks
Semantic Layer
   ↓        DQ: metric definition, business rule validation
AI / RAG / Signal Layer
   ↓        DQ: AI context certification, signal quality, freshness
Consumption Layer
            DQ: exception visibility, usage monitoring, evidence

5. Required controls

Typical controls include:

Control	Purpose
Completeness checks	Confirm required records and fields are present
Accuracy checks	Validate data values against trusted sources or rules
Validity checks	Ensure values conform to allowed formats or domains
Timeliness checks	Confirm data arrives within expected SLA
Uniqueness checks	Identify duplicate records or keys
Reconciliation checks	Compare totals, balances or counts across systems
Referential integrity checks	Confirm relationships between entities are valid
CDE monitoring	Monitor critical data elements used in risk, reporting or AI
Exception management	Track, prioritise and resolve data issues
Evidence retention	Store results for audit, regulator or internal review
6. Common tools and implementation options

Tooling depends on client platform maturity.

Examples:

Platform area	Options
Data quality rules	Great Expectations, Soda, dbt tests, Deequ, custom SQL
Cloud orchestration	AWS Glue, Step Functions, Azure Data Factory, Databricks Workflows
Data platforms	Snowflake, Databricks, Redshift, Synapse, BigQuery
Metadata and lineage	Collibra, Alation, Purview, OpenLineage, DataHub
Monitoring	CloudWatch, Azure Monitor, Datadog, Monte Carlo, Bigeye
CI/CD	GitHub Actions, Azure DevOps, GitLab CI
Evidence store	S3, ADLS, SharePoint, metadata catalogue, audit schema
7. Maturity model
Level	Description
Level 1 — Fragmented	Manual checks, spreadsheet reconciliations, reactive issue handling
Level 2 — Repeatable	Common DQ rules exist for key feeds or reports, but limited automation
Level 3 — Governed	DQ ownership, CDEs, rule catalogues and issue workflows are defined
Level 4 — Industrialised	DQ rules are automated, versioned, monitored and integrated into CI/CD
Level 5 — Adaptive	DQ patterns, anomaly detection and AI-assisted issue triage improve continuously
8. Common failure modes

Common failure modes include:

DQ rules are created after production issues, not designed upfront
rules are technical but not linked to business outcomes
no clear data owner for issue resolution
DQ results are not visible to business stakeholders
exceptions are detected but not remediated
reconciliation is manual and not repeatable
CDEs are defined but not monitored
DQ is not integrated into CI/CD pipelines
AI systems consume data without checking certification status
dashboards report green status while unresolved data issues remain hidden
9. Consultant discovery questions

Use these during assessment or client workshops.

Business questions
Which reports, decisions or processes are most sensitive to data quality?
Which regulatory obligations depend on this data?
Which customer or financial outcomes could be affected by poor data?
Who owns the data quality outcome?
How are issues prioritised and remediated today?
Data questions
What are the critical data elements?
Which source systems are authoritative?
Are there known gaps, duplicates or reconciliation issues?
Are data quality rules documented and version-controlled?
Are DQ results retained as evidence?
AI-specific questions
Will this data be used by AI assistants, RAG systems, models or agents?
Does the AI system know whether the data is certified or provisional?
Can AI responses expose unresolved data quality issues?
Are stale, incomplete or low-confidence records filtered from AI context?
Is there a refusal pattern when required data quality conditions are not met?
10. Related architecture patterns
Regulatory Reporting Data Layer

Data Quality is mandatory for reportable outputs. DQ rules must be linked to source-to-report lineage, reconciliations, exception handling and sign-off evidence.

Fraud Signal Layer

Fraud signals depend on high-quality transaction, customer, account, merchant and device data. Poor DQ can create false positives or missed fraud events.

Governed RAG Knowledge Base

Knowledge quality is equivalent to data quality for RAG. Content must be approved, current, classified, chunked correctly and access controlled.

Semantic Layer for AI

Certified metrics and definitions require validation rules. AI should only reason over approved semantic objects where possible.

11. Reusable artefacts

This capability should produce or reuse:

Data Quality rule catalogue
CDE register
DQ assessment checklist
DQ maturity heatmap
Reconciliation design template
Exception management workflow
DQ evidence pack template
AI context certification checklist
DQ dashboard specification
Data owner sign-off template
12. Example executive narrative

Many BFSI organisations have data quality controls for reporting, but those controls are often fragmented, manual and disconnected from AI enablement.

As AI becomes a new consumption layer for enterprise data, data quality must evolve from report-level checking to continuous trust management.

The target state is a governed, automated and evidence-backed data quality capability that protects regulatory reporting, analytics, AI assistants and decision-support workflows.

13. Design principle

If data quality cannot be measured, evidenced and explained, it should not be treated as trusted AI context.