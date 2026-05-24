---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-66
completeness: full
title: 66: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon OpenSearch Service
related_controls:
  - audit_logging
  - model_evaluation
  - monitoring
  - retrieval_grounding
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - bedrock
  - monitoring
  - vector search
  - audit logging
  - model evaluation
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - cost optimization
---

# 66: Knowledge Base Patterns

## Scenario

A company is implementing a RAG-based knowledge management system. The system will use Amazon Bedrock and Amazon OpenSearch Service. The system will ingest hundreds of new documents into the knowledge base on a daily basis. The system must maintain high accuracy and reliability for content across multiple departments. A GenAI developer wants to use Amazon Bedrock model evaluation to design a comprehensive evaluation process. The process must evaluate correctness, relevance, formality scale, and company-specific tone and style. The GenAI developer must run the evaluation on a weekly basis. The GenAI developer will create a RAG evaluation with LLM-as-a-judge and select the desired metrics. Which solution will meet these requirements MOST cost-effectively?

## Common implementation patterns

- Create a human-validated evaluation dataset. Create custom metrics for formality scale and company-specific tone and style.

## Architecture guidance

- A human-validated dataset ensures an accurate representation of enterprise-specific use cases, terminology, and content patterns.
- Using LLM-as-a-judge with custom metrics provides an automated, consistent, and scalable evaluation.
- You can design custom metrics to assess formality scale and company-specific tone and style with consistent criteria.

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
