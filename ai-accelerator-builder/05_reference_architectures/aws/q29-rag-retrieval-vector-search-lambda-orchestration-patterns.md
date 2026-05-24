---
type: reference_note
platform: aws
status: draft
source: udemy-question-29
title: 29: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon Comprehend
related_controls:
  - audit_logging
  - model_evaluation
  - monitoring
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - audit logging
  - model evaluation
  - monitoring
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - internal assistant
  - policy assistance
  - cost optimization
---

# 29: Knowledge Base And RAG Patterns

## Scenario

A global HR SaaS provider is building a semantic search feature for internal policy documents by using a RAG architecture. The team will embed millions of document chunks and store the vectors in a vector database for similarity search. The solution must keep vector storage costs low while maintaining search relevance for the organization’s terminology, and the embedding generation process must efficiently handle nightly ingestion of large document batches. Which combination of actions will meet these requirements MOST cost-effectively? (Select TWO.)

## Common implementation patterns

- Run a proof of concept that generates embeddings for a representative set of documents and queries by using multiple Amazon Bedrock embedding models (for example, Amazon Titan embeddings and an alternative embedding model). Compare retrieval quality metrics...
- Use an Amazon Titan embedding model and configure a smaller embedding vector dimension after validating that retrieval relevance remains acceptable for the policy-document domain. Use AWS Lambda to batch-generate embeddings for new chunks before writing them...
- Use Amazon Comprehend to classify each document into topics and store only the topic labels. Use keyword search on the labels instead of generating embeddings to reduce cost. This is the managed or lower-overhead approach called out as correct in the exam...

## Architecture guidance

- To keep costs low at scale, the embedding strategy should reduce the size and number of vectors stored while preserving retrieval quality.
- Configuring an embedding model with an appropriately smaller vector dimension can materially reduce vector storage and indexing costs, but it must be validated against real queries to avoid harming relevance.
- Because different embedding models can behave differently across domains and languages, testing multiple Bedrock embedding model options on representative data is a reliable way to choose the best fit.

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
