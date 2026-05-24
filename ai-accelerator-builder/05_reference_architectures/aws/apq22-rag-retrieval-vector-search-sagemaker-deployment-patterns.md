---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-22
completeness: full
title: 22: Vector Search Patterns
pattern_family: rag
aws_services:
  - Amazon DynamoDB
  - Amazon OpenSearch Service
  - Amazon SageMaker
related_controls:
  - audit_logging
  - model_evaluation
  - retrieval_grounding
topics:
  - vector search patterns
  - rag
  - state store
  - vector search
  - sagemaker
  - audit logging
  - model evaluation
  - retrieval grounding
use_cases:
  - architecture reference
---

# 22: Vector Search Patterns

## Scenario

A company is designing an advanced vector database architecture for FM augmentation. A GenAI developer must configure each architectural requirement. Select the correct AWS service configuration from the following list for each architectural requirement. Select each service configuration one time or not at all. (Select THREE.)

## Common implementation patterns

- Use Amazon OpenSearch Service with the k-nearest neighbor (k-NN) plugin when you need distributed similarity search across billions of product catalog vectors with custom relevance scoring.
- Use Amazon Aurora PostgreSQL with pgvector when you need to combine metadata filtering with vector search while maintaining strong consistency for financial records.
- Use Amazon Neptune with vector search when you need graph-based vector search to identify relationships between research papers and their citations.

## Common anti-patterns

- Avoid using DynamoDB vector support for billion-scale distributed similarity search with custom relevance scoring.
- Avoid using graph-first vector search when the requirement is strong consistency plus metadata filtering for financial records.
- Avoid using relational vector storage when the primary requirement is graph-based citation and relationship traversal.

## Architecture guidance

- OpenSearch Service with the k-NN plugin can handle distributed similarity search across billions of product catalog vectors with custom relevance scoring.
- OpenSearch Service provides a distributed architecture that can scale to billions of vectors across multiple shards.
- OpenSearch Service is unique in providing custom plugins to fine-tune search relevance compared to the other options.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
