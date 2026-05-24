---
type: reference_note
platform: aws
status: draft
source: udemy-question-55
title: 55: Agent Orchestration Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon S3
  - Bedrock Guardrails
  - Bedrock Knowledge Bases
related_controls:
  - guardrails
  - retrieval_grounding
topics:
  - agent orchestration patterns
  - bedrock knowledge bases
  - bedrock
  - s3 data assets
  - guardrails
  - knowledge bases
  - retrieval grounding
use_cases:
  - customer-facing assistant
  - internal assistant
  - routing and orchestration
---

# 55: Agent Orchestration Patterns

## Scenario

A fintech customer support engineering team is building an internal GenAI assistant to help agents answer questions about the latest policies and procedures. The documents are stored in Amazon S3 and an internal Atlassian Confluence wiki, and the content changes frequently. The team wants the assistant’s answers to be grounded in the approved documents to reduce hallucinations and to avoid having to retrain a model whenever content is updated. Which architecture will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base that connects to Amazon S3 and Confluence as data sources. Configure an embedding model (such as Amazon Titan embeddings) and a managed vector store. Use the bedrock-agent-runtime RetrieveAndGenerate capability to...

## Architecture guidance

- A managed RAG architecture is the best match when information changes frequently and the goal is to keep responses grounded in approved sources without retraining.
- Amazon Bedrock Knowledge Bases provide built-in ingestion from supported repositories, embedding generation, chunking, and semantic retrieval, and they integrate directly with a generation step (RetrieveAndGenerate).
- Adding Bedrock Guardrails with contextual grounding checks further enforces that responses stay aligned with retrieved context, reducing hallucinations while keeping the architecture simple to operate.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
