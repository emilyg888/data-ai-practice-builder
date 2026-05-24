---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-26
completeness: full
title: 26: RAG Patterns
pattern_family: rag
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon OpenSearch Service
related_controls:
  - audit_logging
  - monitoring
  - retrieval_grounding
topics:
  - rag patterns
  - rag
  - bedrock
  - monitoring
  - vector search
  - audit logging
  - retrieval grounding
  - evaluation
use_cases:
  - architecture reference
---

# 26: RAG Patterns

## Scenario

A GenAI developer is troubleshooting performance issues in a production RAG application. The application is built on Amazon Bedrock. The application uses Amazon OpenSearch Service for vector storage. Users report inconsistent response times. Some queries are taking significantly longer than others. The GenAI developer must implement a monitoring solution that provides comprehensive diagnostic information to identify the root cause of the issue. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create a custom Amazon CloudWatch dashboard that combines context retrieval latency metrics with OpenSearch Service operation counts. Analyze Amazon Bedrock invocation logs to identify which knowledge base queries are experiencing degraded performance.

## Architecture guidance

- CloudWatch dashboards provide a customizable view of metrics and alarms.
- CloudWatch dashboards provide a visual correlation of data from multiple sources.
- You can combine context-retrieval latency metrics from OpenSearch with operation counts to find a direct correlation between vector search performance and overall response times.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
