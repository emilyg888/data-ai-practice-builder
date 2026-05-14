---
type: pattern
status: draft
risk_level: medium
business_domains:
  - education
  - cloud architecture
  - operations
  - risk monitoring
capability_layers:
  - knowledge ingestion
  - retrieval-augmented generation
  - multi-agent interaction
  - event-driven decisioning
  - governance and evaluation
ai_impact:
  - selective AI invocation lowers cost
  - grounded responses improve relevance
  - reusable architecture guidance speeds learning
related_controls:
  - schema validation
  - rule-based trigger gating
  - model routing
  - IAM-scoped invocation
  - audit logging
  - offline evaluation
---

# Event-Triggered AI Copilot over Knowledge Assets

## 1. Problem solved

This pattern solves two linked problems:

1. Teams need an AI copilot that can answer architecture questions, generate quizzes, and review designs using grounded knowledge instead of generic model output.
2. Teams do not want to invoke GenAI on every event, so they need a control layer that filters signals and calls AI only when the event is important enough.

In this repo, the pattern combines a Bedrock Knowledge Base, purpose-built agents, and an event-driven trigger layer so AWS architecture assistance is both contextual and cost-aware.

## 2. When to use

Use this pattern when:

- you have a curated body of documents such as study guides, design notes, or architecture slides
- users need multiple AI interactions over the same knowledge set, such as tutoring, quiz generation, and design review
- some AI requests are interactive, while others should be triggered by streamed events
- cost, auditability, and control matter more than invoking a model for every incoming signal
- you want ephemeral lab infrastructure that can be deployed and destroyed cleanly

## 3. Business outcomes

- Faster architecture learning through grounded tutoring and quiz generation
- Better design quality through structured review of diagrams and rationale
- Lower inference cost because rule logic filters low-value events before AI runs
- Higher operational trust through audit logs, kill switches, and explicit trigger rules
- Repeatable experimentation because infrastructure, ingestion, and evaluation are all scripted

## 4. Logical architecture

The logical flow is:

1. PDF course and architecture materials are ingested into S3 and prepared for retrieval.
2. Bedrock Knowledge Bases and S3 Vectors provide retrieval context for agent responses.
3. Users interact through CLI or API routes for tutor, quiz, and review workflows.
4. An orchestrator routes each request to a purpose-built agent.
5. Agents call Bedrock models, optionally with retrieved context and event payload context.
6. A separate event path consumes Kafka/MSK events, validates schema, applies trigger rules, and invokes the tutor flow only when decision logic allows it.
7. Audit records and evaluation jobs measure trigger rate, model mix, and failure signals.

At implementation level in this repo:

- `infrastructure/stacks/airlab_stack.py` provisions the Bedrock/RAG/API layer
- `knowledge_base/ingestion.py` ingests PDF content
- `agents/` contains tutor, quiz, and reviewer agents
- `infrastructure/stacks/trigger_stack.py` provisions the event-trigger path
- `trigger/` contains decision, rule, schema, and audit logic
- `evaluation/trigger_eval.py` evaluates the trigger layer from audit data

## 5. Reference architecture options

### Option A: Interactive copilot only

Use API Gateway or CLI to call tutor, quiz, and review agents over a Bedrock Knowledge Base. This is the simplest option and fits training, study, and guided architecture review.

### Option B: Event-triggered AI only

Use MSK, Lambda consumers, and trigger rules to invoke an AI workflow only for high-signal events. This fits risk, alerting, or triage use cases where most events should be ignored.

### Option C: Hybrid copilot plus trigger layer

This is the recommended option for this project. Interactive users can ask questions directly, while event producers can invoke the same grounded AI path only when rule logic decides the event is worth the cost.

## 6. Required capabilities

- Infrastructure as code for repeatable lab creation and teardown
- Document ingestion and chunking for knowledge grounding
- Retrieval against a managed knowledge base and vector store
- Multiple task-specific agents instead of one overloaded prompt
- Event ingestion from Kafka/MSK
- Safe, configurable trigger rules
- Model routing so higher-cost models are reserved for higher-value events
- API integration between the trigger layer and the copilot runtime
- Observability, audit storage, and offline evaluation

## 7. Control gates

- Schema validation rejects malformed events before any AI invocation
- Rule evaluation gates whether an event is ignored, sampled, or sent to AI
- A kill-switch parameter can short-circuit live AI invocation
- Model routing separates cheap default handling from escalated reasoning paths
- IAM policies scope access to Bedrock, S3, SSM, Lambda, and API execution
- Audit records capture decisions, routes, and outcome status for replay and review
- Offline evaluation checks trigger rate and miss-rate proxies before production hardening

## 8. Delivery steps

1. Deploy the core AirLab stack with CDK and verify the API routes are live.
2. Ingest the PDF knowledge assets into the document bucket and verify retrieval works.
3. Validate the three core agent workflows: tutor, quiz, and review.
4. Deploy the trigger stack and confirm schema validation, rules loading, and decider wiring.
5. Tune trigger thresholds and baseline sampling in `config/trigger_rules.json`.
6. Run smoke tests and offline evaluation to inspect trigger rate, error rate, and model mix.
7. Tighten IAM and production controls only after the lab flow is stable.

## 9. Common risks and failure modes

- Retrieval quality is weak if source documents are noisy or chunking is poor.
- Trigger rules may over-fire and erase the intended cost savings.
- Trigger rules may under-fire and miss important events.
- Event-to-API integration can fail due to VPC, IAM, or endpoint configuration.
- Knowledge Base dry-run mode can make deployments look healthy before real provisioning is tested.
- LLM JSON responses for quiz or review flows can still be malformed and require fallback handling.
- A lab-oriented teardown posture is useful for learning but unsafe for persistent production workloads.

## 10. Artefacts produced

- CDK stacks for the AirLab runtime and trigger layer
- S3-backed knowledge assets and vector-backed retrieval configuration
- Lambda handlers for tutor, quiz, review, consumer, and decider flows
- Trigger rules and model-routing configuration
- API endpoints for copilot workflows
- Audit logs and evaluation summaries
- Mermaid diagrams and scored architecture-review outputs

## 11. Example executive narrative

This project implements a controlled AWS GenAI copilot pattern. It combines curated architecture knowledge, Bedrock-based agents, and an event-driven trigger layer so users receive grounded tutoring, quiz generation, and design review without paying to run AI on every event. The architecture is intentionally ephemeral and lab-oriented, which makes it suitable for learning, demonstrations, and controlled experimentation before any production hardening work begins.
