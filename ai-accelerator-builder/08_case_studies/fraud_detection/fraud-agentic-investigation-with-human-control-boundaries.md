# Use Case: Fraud Agentic Investigation with Human Control Boundaries

## Source
- Profile: https://www.linkedin.com/in/emily-gao-291177a/
- Post URL: https://www.linkedin.com/posts/emily-gao-291177a_frauddetection-agenticworkflows-semanticcontracts-share-7457590320050909184-m4We
- Post Title: Governing Fraud Detection with Semantic Contracts and Agentic Investigation
- Post ID: 7457590320050909184

## Post Insight Summary
The post defines an agentic investigation workflow that supports analysts without replacing decision ownership. The workflow orchestrates intake, planning, retrieval, evidence synthesis, hypothesis evaluation, governance checks, and auditable reporting, with explicit pauses for human review.

## Business Context
- Industry: Banking
- Domain: Fraud Operations and Responsible AI
- Stakeholders: Fraud investigators, operations managers, compliance, legal, model risk

## Problem Statement
Fraud case handling is time-consuming and inconsistent when analysts manually gather evidence across systems. Fully automated agentic decisions introduce high regulatory and customer-risk exposure. The organization needs agentic assistance with strict control boundaries and human ownership.

## Proposed AI/Data Use Case
- Objective: Orchestrate analyst-assistive fraud investigations with governance checkpoints.
- Primary User: Fraud analyst and case supervisor.
- Decision Type: Agentic assistive workflow with mandatory human approvals.
- Frequency: Per flagged fraud case.

## Inputs
- Structured data: Case metadata, transactions, account activity, risk scores.
- Unstructured data: Analyst notes, policy documents, prior case narratives.
- Governance metadata: Approved actions, restricted actions, review requirements.

## Outputs
- Investigation plan: Ordered tasks and required evidence steps.
- Evidence package: Summaries, hypotheses, test results, governance status.
- Final artifact: Auditable case report and analyst decision log.

## Workflow
1. Intake and classify incoming fraud case.
2. Generate investigation plan and retrieve approved knowledge/data.
3. Summarize evidence and draft hypotheses.
4. Evaluate hypotheses and run governance checks.
5. Pause for analyst review and final decision.
6. Produce auditable report with full traceability.

## Success Metrics
- Business KPI: Reduced average case resolution time.
- Model KPI: Improved relevance of generated evidence summaries.
- Operational KPI: Higher consistency of governance-compliant investigations.

## Risks and Controls
- Over-automation risk: Hard stop before any customer-impacting action.
- Hallucination risk: Source-cited evidence and verifier checks.
- Compliance risk: Enforce role-based permissions and action constraints.
- Audit risk: Persist complete workflow traces and reviewer approvals.

## MVP Scope
- In scope: One fraud case type with agentic orchestration and human gates.
- Out of scope: End-to-end autonomous adjudication.
- Timeline: 4-6 weeks for pilot workflow.

## Traceability
- Derived from post claim(s):
  - "This is not an agent decision-maker."
  - "It is agentic workflow orchestration with explicit control boundaries."
  - "Pause for human review, and produce an auditable case report."