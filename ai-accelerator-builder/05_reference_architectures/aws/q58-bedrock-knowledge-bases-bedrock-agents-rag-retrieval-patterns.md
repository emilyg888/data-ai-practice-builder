---
type: reference_note
platform: aws
status: draft
source: udemy-question-58
title: 58: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
  - Bedrock Agents
related_controls:
  - audit_logging
  - evidence_retention
  - monitoring
  - prompt_policy
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - monitoring
  - s3 data assets
  - agents
  - audit logging
  - evidence retention
  - prompt policy
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - internal assistant
  - policy assistance
  - search and retrieval
  - model governance
---

# 58: Knowledge Base And RAG Patterns

## Scenario

A healthcare provider is building an internal “policy assistant” that answers employee questions by using Amazon Bedrock Agents with an Amazon Bedrock Knowledge Base that is populated from documents in Amazon S3. The compliance team requires the application to be transparent by showing users which policy sources were used for each answer and by providing auditors with a trace of how the agent reached the response (including knowledge base retrievals and action group calls). The operations team also wants a per-response confidence signal recorded in Amazon CloudWatch so they can investigate low-confidence answers. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Enable Amazon Bedrock agent tracing for the agent and log the returned trace payloads. Configure the application to include source attribution in the response by presenting the retrieved document metadata (for example, document title and S3 URI) as evidence....

## Architecture guidance

- The lowest-overhead way to build transparency into an agent-based GenAI application is to use native agent tracing to obtain an auditable reasoning trace, while presenting evidence by surfacing the identifiers of the...
- Operational confidence should be captured as a metric in CloudWatch so it can be visualized and alarmed on; this is best done by emitting a per-request score produced during processing (for example, a...
- Alternatives that rely on audit logs, workflow histories, or returning full prompts/context either fail to provide true reasoning traces and source attribution or introduce unnecessary security and operational risk.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
