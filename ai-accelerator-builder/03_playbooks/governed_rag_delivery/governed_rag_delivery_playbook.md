---
type: playbook
playbook_id: governed_rag_delivery_playbook
playbook_name: Governed RAG Delivery Playbook
status: draft
version: 0.1
business_domains:
  - banking
  - insurance
  - wealth
  - risk_and_compliance
  - regulatory_reporting
capability_layers:
  - governance_and_trust
  - ai_enablement
  - business_consumption
architecture_layers:
  - knowledge_layer
  - ai_orchestration_layer
  - ai_control_layer
  - consumption_layer
ai_impact:
  - ai_as_knowledge_interface
  - ai_as_reasoning_assistant
risk_level: medium_to_high
related_capabilities:
  - data_product
  - metadata
  - data_quality
  - access_control
  - ai_copilots_and_workflows
  - ai_evaluation
related_patterns:
  - governed_rag_knowledge_base
  - ai_copilot_over_data_products
  - ai_evaluation_and_monitoring_framework
  - agentic_workflow_human_approval
related_controls:
  - access_control
  - data_classification
  - content_approval
  - retrieval_grounding
  - prompt_policy
  - response_evaluation
  - audit_logging
  - evidence_retention
---

# Governed RAG Delivery Playbook

## 1. Purpose

This playbook helps consultants design and deliver a governed Retrieval-Augmented Generation capability for BFSI clients.

The goal is not to build a simple chatbot. The goal is to create a controlled knowledge-access pattern where AI can retrieve, reason over and explain approved enterprise knowledge while preserving access control, evidence, auditability and business accountability.

Typical use cases include:

- compliance policy Q&A
- operational procedure assistant
- regulatory obligation explanation
- claims handling guidance
- lending policy support
- fraud investigation knowledge assistant
- contact centre knowledge copilot
- internal data governance and architecture assistant

Core principle:

> RAG is not just a GenAI pattern. In BFSI, it is a governed knowledge distribution architecture.

---

## 2. When to use this playbook

Use this playbook when a client wants AI to answer questions using internal documents, policies, standards, procedures, knowledge articles or curated domain content.

Good fit:

- knowledge is document-heavy
- users waste time searching multiple repositories
- answers require grounding in approved sources
- content needs access control
- the client needs audit logs and evidence
- the client wants to move from pilot to production
- AI outputs must cite or trace back to source content

Poor fit:

- knowledge sources are unapproved or uncontrolled
- users expect the AI to make binding decisions
- source documents are stale, contradictory or unmanaged
- there is no accountable content owner
- high-impact workflow actions are required without human approval
- the client wants production deployment without evaluation or monitoring

---

## 3. Business outcomes

A governed RAG capability should help the client achieve:

- faster access to trusted knowledge
- reduced manual search effort
- more consistent interpretation of policy and procedure
- better analyst and operational productivity
- lower dependency on informal subject matter expert channels
- improved onboarding and knowledge reuse
- auditable AI-assisted knowledge access
- controlled pathway from GenAI pilot to production

For BFSI clients, the strongest value proposition is:

> Better productivity without losing control of regulated knowledge, sensitive information or decision accountability.

---

## 4. Consulting questions

### Business framing

- What business process or user group is the RAG capability supporting?
- What problem are users trying to solve today?
- Is the use case informational, analytical, decision-support or action-taking?
- What is the consequence of an incorrect answer?
- Does the output affect customers, regulators, financial outcomes or legal obligations?
- Who owns the business outcome?

### Knowledge and content

- What content sources are in scope?
- Are the documents approved, current and authoritative?
- Who owns each content source?
- Is there conflicting guidance across documents?
- Are there document versions, expiry dates or review cycles?
- What content should be excluded from AI retrieval?
- Is source citation required in the answer?

### Access and security

- Who can use the assistant?
- Which user groups can access which documents?
- Does the content contain PII, confidential information or restricted material?
- Is row-level, document-level or paragraph-level access filtering required?
- Are private endpoints, encryption or tenant isolation required?

### AI behaviour

- What kinds of questions should the assistant answer?
- What should it refuse to answer?
- Should the assistant provide citations?
- Should it summarise, compare, explain or recommend?
- Should it expose uncertainty or confidence?
- Should it escalate to a human or owner when content is insufficient?

---

## 5. Inputs required

| Input | Description |
|---|---|
| Use case statement | Business problem, target users and expected outcome |
| User groups | Roles, access needs and expected usage patterns |
| Content inventory | Documents, policies, procedures and knowledge sources |
| Content ownership | Owner, steward, review cycle and approval status |
| Data classification | Sensitivity, confidentiality, PII and retention requirements |
| Access model | RBAC, ABAC, document-level or content-level access rules |
| AI policy | Approved models, prohibited behaviours and escalation rules |
| Existing platforms | Cloud, search, vector store, document repository, identity provider |
| Evaluation examples | Representative questions, expected answers and refusal scenarios |
| Risk assessment | Business, regulatory, operational and AI-specific risks |

---

## 6. Target logical architecture

```text
User
  ↓
AI Assistant Interface
  ↓
AI Orchestration Layer
  ├── prompt policy
  ├── model routing
  ├── retrieval routing
  ├── refusal rules
  ├── evaluation hooks
  └── audit logging
        ↓
Retrieval Layer
  ├── query rewriting
  ├── metadata filtering
  ├── vector search
  ├── keyword search
  ├── re-ranking
  └── source citation
        ↓
Governed Knowledge Layer
  ├── approved documents
  ├── classified content
  ├── chunk metadata
  ├── access policies
  ├── content owners
  ├── version history
  └── freshness status
        ↓
Control and Evidence Layer
  ├── identity and access logs
  ├── prompt logs
  ├── retrieved context
  ├── generated response
  ├── user feedback
  ├── evaluation results
  └── incident records
```

Important design choice:

> The LLM should not be the control point. Controls should sit around retrieval, access, orchestration, evaluation and workflow boundaries.

---

## 7. Reference architecture options

### Option A: AWS-oriented pattern

```text
Document Sources
  ↓
S3 / Document Repository
  ↓
Content Classification + Chunking
  ↓
Amazon OpenSearch / Bedrock Knowledge Bases
  ↓
Bedrock Model Invocation
  ↓
Lambda / Step Functions Orchestration
  ↓
API Gateway / Application UI
  ↓
CloudWatch + CloudTrail + Evidence Store
```

Best for clients already standardised on AWS and Bedrock.

### Option B: Azure-oriented pattern

```text
SharePoint / Blob / Document Sources
  ↓
Content Classification + Chunking
  ↓
Azure AI Search
  ↓
Azure OpenAI
  ↓
Prompt Flow / Semantic Kernel / App Service
  ↓
Entra ID Access Control
  ↓
Azure Monitor + Purview + Evidence Store
```

Best for clients with Microsoft 365, SharePoint and Entra ID-heavy environments.

### Option C: Snowflake / Databricks-oriented pattern

```text
Enterprise Documents + Curated Data Products
  ↓
Metadata + Classification + Chunking
  ↓
Snowflake Cortex Search / Databricks Vector Search
  ↓
Snowflake Cortex / Databricks Mosaic AI / External LLM
  ↓
Governed Query and Retrieval Layer
  ↓
Copilot / Analyst Workflow
  ↓
Telemetry + Evaluation + Evidence
```

Best when RAG is closely linked to governed data products, semantic layers or analytics workflows.

---

## 8. Delivery steps

### Step 1: Frame the use case

Define the business problem, user group, expected outcome and risk profile.

Deliverables:

- use case canvas
- risk classification
- user persona summary
- success metrics

Key decision:

> Is this a knowledge assistant, decision-support assistant or workflow assistant?

### Step 2: Inventory and classify content

Assess:

- source system
- owner
- approval status
- version
- expiry or review date
- confidentiality
- PII sensitivity
- target user group
- content conflicts
- content freshness

Deliverables:

- content inventory
- content classification matrix
- exclusion list
- owner/steward mapping

Key decision:

> Which content is approved for AI retrieval, and which content must be excluded?

### Step 3: Define access model

Design who can access which content through the AI assistant.

Consider:

- user role
- business unit
- region
- product area
- sensitivity level
- customer data exposure
- restricted documents
- regulatory constraints

Deliverables:

- access control matrix
- metadata filtering design
- identity integration design
- sensitive content handling approach

Key decision:

> Is document-level filtering enough, or is chunk-level filtering required?

### Step 4: Design knowledge processing pipeline

Define how documents are prepared for retrieval.

Design choices:

- parsing approach
- chunking strategy
- metadata schema
- embedding model
- vector store
- keyword search
- hybrid search
- re-ranking
- refresh frequency
- deletion and expiry handling

Deliverables:

- ingestion pipeline design
- chunking standard
- metadata schema
- indexing strategy
- content refresh design

Key decision:

> How will the system preserve business meaning, source traceability and access rules through chunking and indexing?

### Step 5: Design AI orchestration

Define how the assistant receives a query, retrieves context, calls the model and returns an answer.

Components:

- system prompt
- retrieval policy
- prompt templates
- model routing
- refusal rules
- citation rules
- response format
- escalation rules
- cost and latency controls

Deliverables:

- AI orchestration design
- prompt policy
- model selection rationale
- refusal pattern
- citation standard
- escalation design

Key decision:

> What should the assistant do when retrieved context is weak, conflicting, missing or inaccessible?

### Step 6: Build evaluation framework

Create test cases before production.

Test categories:

- answer correctness
- grounding
- citation accuracy
- refusal quality
- access control enforcement
- sensitive data handling
- stale content handling
- conflicting source handling
- prompt injection resistance
- latency and cost
- user usefulness

Deliverables:

- evaluation dataset
- expected answer set
- refusal test set
- prompt injection test set
- evaluation scorecard
- production acceptance criteria

Key decision:

> What is the minimum quality threshold required before release?

### Step 7: Implement observability and evidence

Log:

- user identity
- timestamp
- user question
- rewritten query
- retrieved chunks
- source documents
- model used
- generated answer
- citations
- refusal reason
- user feedback
- cost and latency
- errors or incidents

Deliverables:

- telemetry design
- audit logging design
- evidence retention policy
- monitoring dashboard specification
- incident and escalation process

Key decision:

> What evidence is required to defend the AI output after the fact?

### Step 8: Pilot with controlled users

Pilot scope:

- limited document set
- limited user group
- defined evaluation criteria
- feedback capture
- daily or weekly review
- known fallback path

Deliverables:

- pilot plan
- pilot feedback report
- issue register
- tuning backlog
- go/no-go recommendation

Key decision:

> Is the assistant reliable enough to expand, or does the knowledge/control foundation need further remediation?

### Step 9: Productionise and scale

Production requirements:

- CI/CD for prompts and retrieval config
- automated content refresh
- access control integration
- monitoring dashboard
- evaluation regression testing
- support model
- ownership model
- change control
- reusable architecture pattern

Deliverables:

- production readiness checklist
- operating model
- support runbook
- release process
- reusable RAG pattern
- adoption and training materials

Key decision:

> Is this a one-off assistant or a reusable RAG platform pattern?

---

## 9. Control gates

| Gate | Control question | Evidence |
|---|---|---|
| Use case gate | Is the use case approved and risk-classified? | Use case canvas, risk rating |
| Content gate | Is the content approved, owned and current? | Content inventory, owner sign-off |
| Access gate | Are users restricted to authorised content? | Access matrix, test results |
| Retrieval gate | Are answers grounded in correct sources? | Retrieval test results |
| Prompt gate | Are behaviour and refusal rules defined? | Prompt policy, test cases |
| Evaluation gate | Has quality been tested before release? | Evaluation scorecard |
| Security gate | Are sensitive data controls implemented? | Security review, masking tests |
| Evidence gate | Are prompts, retrieval and outputs logged? | Audit log sample |
| Production gate | Is monitoring and support in place? | Production readiness checklist |

---

## 10. Common risks and mitigations

| Risk | Why it matters | Mitigation |
|---|---|---|
| Unapproved content | AI may provide unofficial guidance | Content approval workflow |
| Stale documents | AI may provide outdated answers | Versioning, expiry metadata, refresh checks |
| Weak access filtering | Users may see restricted content | Metadata-based retrieval filtering |
| Poor chunking | Important context may be lost | Chunking standard and retrieval testing |
| No citations | Answers cannot be verified | Mandatory source citation |
| Hallucination | AI may invent guidance | Grounding tests and refusal rules |
| Prompt injection | Malicious content may alter behaviour | Input/output filtering and prompt injection tests |
| Conflicting sources | AI may choose the wrong rule | Source priority and escalation rules |
| No evaluation | Quality cannot be measured | Evaluation dataset and acceptance thresholds |
| No ownership | Solution degrades after go-live | Business owner and operating model |

---

## 11. Artefacts produced

This playbook should produce the following artefacts:

- use case canvas
- user persona summary
- risk classification
- content inventory
- content classification matrix
- content owner/steward register
- access control matrix
- metadata schema
- chunking standard
- ingestion pipeline design
- retrieval design
- prompt policy
- refusal pattern
- citation standard
- evaluation dataset
- prompt injection test set
- evaluation scorecard
- telemetry and audit design
- monitoring dashboard specification
- incident and escalation process
- production readiness checklist
- operating model
- executive summary

---

## 12. Sample consultant canvas

```yaml
use_case: Compliance Policy Assistant
business_outcome: Reduce time spent searching policy and procedure content
user_group:
  - compliance analysts
  - operations team leads
ai_role: knowledge_interface
risk_level: medium
content_sources:
  - approved compliance policy documents
  - operational procedure manuals
  - regulatory guidance summaries
excluded_sources:
  - draft policies
  - expired procedures
  - restricted legal advice
required_controls:
  - content approval
  - document-level access filtering
  - source citation
  - refusal when context is insufficient
  - audit logging
success_metrics:
  - reduction in search time
  - answer usefulness score
  - citation accuracy
  - refusal accuracy
  - user adoption
production_readiness:
  - evaluation passed
  - content owner sign-off
  - security review completed
  - monitoring enabled
```

---

## 13. Example executive narrative

Many organisations start their GenAI journey with a document chatbot. The challenge is that, in BFSI, internal knowledge is often regulated, sensitive, versioned, role-restricted and operationally critical.

A governed RAG approach provides a safer path. It allows users to interact with approved enterprise knowledge through AI, while preserving source traceability, access control, citation, evaluation and audit evidence.

The target state is not a standalone chatbot. It is a reusable knowledge-access capability that can support multiple use cases across compliance, operations, claims, lending, fraud and risk.

---

## 14. Production readiness checklist

Before production, confirm:

- [ ] Use case has been approved
- [ ] Business owner is assigned
- [ ] Risk level is classified
- [ ] Content sources are inventoried
- [ ] Content owners are assigned
- [ ] Draft, expired and restricted content is excluded
- [ ] Content classification is completed
- [ ] Access model is implemented
- [ ] Chunking standard is defined
- [ ] Metadata schema is implemented
- [ ] Retrieval quality is tested
- [ ] Prompt policy is approved
- [ ] Refusal rules are tested
- [ ] Citation requirement is implemented
- [ ] Evaluation dataset exists
- [ ] Prompt injection tests are completed
- [ ] Sensitive data handling is validated
- [ ] Prompt, retrieval and output logs are retained
- [ ] Monitoring dashboard is available
- [ ] Incident process is defined
- [ ] Support owner is assigned
- [ ] Production go-live approval is recorded

---

## 15. Design principles

> Do not index everything. Index what is approved, owned, current and useful.

> Retrieval is a control surface, not just a search function.

> The assistant should cite, refuse or escalate when knowledge is insufficient.

> A governed RAG pattern must manage content lifecycle, access control, evaluation and evidence.

> In BFSI, production RAG is an operating model, not just a vector database.
