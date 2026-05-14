---

type: pattern
status: draft
risk_level: medium-to-high
business_domains:

* Fraud investigation
* Credit risk review
* Customer churn investigation
* Home loan delinquency management
* Hardship assessment
* Complaints management
* Conduct risk
* Operational risk
  capability_layers:
* Case management
* Workflow orchestration
* Human-in-the-loop approval
* Knowledge retrieval
* Approved data access
* Signal evaluation
* Governance and policy checks
* Audit and traceability
  ai_impact:
* Analyst productivity
* Faster evidence gathering
* Improved decision consistency
* Lower investigation cost
* Better auditability
* Reusable workflow automation
  related_controls:
* Human approval gate
* Data access control
* Policy compliance check
* Tool restriction
* Evidence traceability
* Signal promotion control
* Audit logging
* Decision explainability

---

# Agentic Workflow with Human Approval

## 1. Problem solved

Case investigation is often slow, costly, and inconsistent because analysts must work across fragmented data, manual evidence gathering, unclear decision history, and inconsistent tooling.

This pattern solves the problem by providing a reusable AI-assisted workflow that helps analysts move from:

**case → evidence → hypothesis → policy check → human decision → auditable outcome**

The AI assists the investigation, but does not own the final decision.

## 2. When to use

Use this pattern when a business process involves:

* High-volume case reviews
* Time-sensitive investigations
* Evidence gathering across multiple systems
* Policy, risk, or compliance checks
* Human judgement before final decision
* Need for auditability and traceability
* Reusable investigation patterns across domains

Typical use cases include fraud alerts, credit risk reviews, customer churn investigations, hardship assessments, payment delinquency cases, complaints, conduct issues, and operational risk events.

## 3. Business outcomes

This pattern helps organisations:

* Reduce investigation cost
* Accelerate case handling
* Improve decision quality
* Improve analyst productivity
* Standardise investigation workflows
* Preserve human accountability
* Improve audit readiness
* Reuse the same workflow pattern across multiple business domains

## 4. Logical architecture

The logical architecture separates AI reasoning from deterministic control layers.

Core components:

* **Presentation layer**
  Analyst workspace, case view, dashboards, recommended actions, evidence summary.

* **Service orchestration layer**
  Coordinates tasks, tools, agents, workflow steps, and state transitions.

* **Workflow state layer**
  Tracks case status, investigation steps, evidence, decisions, artefacts, and review checkpoints.

* **LLM reasoning layer**
  Plans the investigation, decomposes tasks, summarises evidence, generates hypotheses, and explains findings.

* **Knowledge retrieval layer**
  Retrieves governed policies, procedures, guidelines, prior cases, and precedents.

* **Approved data tools**
  Executes tool-constrained queries against approved systems and certified data sources.

* **Governance checks**
  Applies policy rules, risk controls, data permissions, and compliance checks.

* **Signal evaluation layer**
  Scores, assesses, and rationalises evidence and risk indicators.

* **Signal registry**
  Stores approved signals, versions, ownership, and certification status.

* **Audit reports and run traces**
  Captures inputs, outputs, tool calls, evidence, reasoning steps, users, timestamps, and decisions.

## 5. Reference architecture options

### Option A — Lightweight analyst-assist workflow

Best for early adoption or lower-risk use cases.

* Case intake
* Retrieval over policy documents
* Evidence summarisation
* Human approval
* Audit report generation

### Option B — Governed workflow with approved tools

Best for regulated business processes.

* Case workflow engine
* LLM planning and summarisation
* Approved API/data tool access
* Policy checks
* Human review gate
* Full traceability

### Option C — Enterprise-scale reusable investigation platform

Best for multi-domain reuse.

* Shared workflow orchestration layer
* Reusable investigation templates
* Certified semantic/data layer
* Signal registry
* Governance control plane
* Evaluation and monitoring
* Cross-domain audit reporting

## 6. Required capabilities

Required capabilities include:

* Case intake and classification
* Workflow orchestration
* Human-in-the-loop review
* Governed knowledge retrieval
* Approved data tool access
* Evidence summarisation
* Hypothesis generation
* Policy and control checks
* Signal scoring and evaluation
* Signal registry management
* Audit trail generation
* Role-based access control
* Prompt, tool, and workflow versioning
* Evaluation and monitoring

## 7. Control gates

Key control gates:

* **Case intake gate**
  Validate case type, priority, source, and required metadata.

* **Data access gate**
  Ensure the workflow only uses approved data sources and permitted tools.

* **Knowledge retrieval gate**
  Ensure only governed, current, and approved policies or procedures are retrieved.

* **Reasoning boundary gate**
  Ensure the LLM can explain, summarise, and hypothesise, but not make final adverse decisions.

* **Policy check gate**
  Validate recommendations against business rules, risk controls, and compliance obligations.

* **Signal promotion gate**
  Prevent signals from being silently promoted without review, evidence, versioning, and approval.

* **Human approval gate**
  Require analyst or manager review before final case decision.

* **Audit gate**
  Ensure every material action, tool call, evidence item, and decision is traceable.

## 8. Delivery steps

1. Identify the investigation-heavy use case.
2. Define case types, decision points, and required evidence.
3. Map the current analyst workflow.
4. Identify approved knowledge sources and data tools.
5. Define policy, risk, and compliance rules.
6. Design the workflow state model.
7. Build the LLM reasoning and task-planning layer.
8. Connect governed retrieval and approved tools.
9. Add human review and approval checkpoints.
10. Generate audit reports and run traces.
11. Evaluate quality, accuracy, consistency, and cost impact.
12. Reuse the pattern across adjacent case management domains.

## 9. Common risks and failure modes

Common risks include:

* LLM makes or implies a final decision without approval
* Workflow queries unrestricted or uncertified data
* Retrieved policy content is stale or not governed
* Evidence summary omits important context
* Analyst over-trusts AI-generated recommendations
* Tool calls are not logged
* Case decisions cannot be reconstructed later
* Signals are promoted without validation
* Workflow becomes a black box
* Different business domains customise the pattern inconsistently
* Governance is added after the workflow rather than designed into it

## 10. Artefacts produced

Typical artefacts include:

* Case investigation workflow
* Case state model
* Investigation plan
* Evidence summary
* Hypothesis log
* Policy check results
* Tool execution log
* Human review record
* Decision rationale
* Signal evaluation record
* Signal registry entry
* Audit report
* Run trace
* Governance checklist
* Reusable workflow template

## 11. Example executive narrative

Case management is one of the most expensive and time-sensitive operations in regulated organisations.

The opportunity is not to replace analysts with chatbots.

The opportunity is to give analysts a governed AI-assisted workflow that can gather evidence, retrieve policies, query approved tools, generate hypotheses, apply control checks, and produce an auditable case report.

The design principle is simple:

**The LLM reasons. Deterministic tools control the facts. Humans own the decision.**

This turns agentic AI from demo theatre into enterprise workflow infrastructure.

Instead of building one chatbot per use case, organisations can build reusable analyst-assist orchestration patterns that reduce investigation cost, improve decision quality, accelerate case handling, and preserve auditability.

