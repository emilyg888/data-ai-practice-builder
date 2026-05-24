---
type: reference_note
platform: aws
status: draft
source: udemy-question-65
title: 65: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon OpenSearch Service
  - Amazon S3
related_controls:
  - access_control
  - audit_logging
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - vector search
  - s3 data assets
  - access control
  - audit logging
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
---

# 65: Knowledge Base And RAG Patterns

## Scenario

A media analytics company is building a RAG assistant on AWS by using Amazon Bedrock for text generation. For the retrieval layer, some workloads use Amazon OpenSearch Service for vector search, while other workloads use Amazon Aurora PostgreSQL with the pgvector extension for advanced metadata filtering. The GenAI team wants a single, consistent retrieval interface that Bedrock-based applications can use without being rewritten when the underlying vector store changes. Which solution will provide the MOST seamless integration mechanism for retrieval augmentation across these vector stores?

## Common implementation patterns

- Create a stateless Model Context Protocol (MCP) server (for example, on AWS Lambda) that exposes a single tool such as "vector_search" with a stable JSON input/output contract. Use an MCP client library in the application/agent runtime to call this tool, and...
- Store embeddings and document chunks directly in Amazon S3 objects and retrieve relevant chunks by using S3 prefix filters and object metadata filters. Pass the retrieved objects as context to the model. This is the managed or lower-overhead approach called...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A consistent access mechanism for retrieval augmentation is best achieved by placing a stable, tool-like contract in front of the retrieval layer and letting applications or agents invoke that contract in the same way...
- Using an MCP server to expose a single vector-query tool, combined with an MCP client in the runtime, standardizes how the FM-integrated system performs retrieval and returns normalized results (for example, chunks plus...
- This approach prevents tight coupling to OpenSearch-specific or Aurora/SQL-specific query logic and avoids rewriting application integrations when the organization changes vector stores.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
