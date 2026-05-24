---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-16
completeness: full
title: 16: CloudWatch Logs Monitoring for Bedrock Knowledge Base Ingestion
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
  - Bedrock Knowledge Bases
related_controls:
  - audit_logging
  - monitoring
topics:
  - cloudwatch logs monitoring
  - bedrock knowledge base ingestion
  - bedrock knowledge bases
  - bedrock
  - monitoring
  - s3 data assets
  - knowledge bases
  - audit logging
use_cases:
  - search and retrieval
---

# 16: CloudWatch Logs Monitoring for Bedrock Knowledge Base Ingestion

## Pattern summary

Send Bedrock Knowledge Base ingestion logs to CloudWatch Logs and use Logs Insights to troubleshoot failed document processing.

## Scenario

A company runs a question-answering application. The application uses an Amazon Bedrock knowledge base that ingests documents from multiple Amazon S3 buckets. The company needs to monitor the data ingestion process to identify and troubleshoot any issues with document processing. Which solution will meet these requirements to monitor knowledge base operations?

## Common implementation patterns

- Configure knowledge base logging with Amazon CloudWatch Logs as the destination. Use CloudWatch Logs Insights to query for failed document processing.

## Architecture guidance

- Amazon Bedrock knowledge bases support a built-in logging system that you can configure to send logs to CloudWatch Logs.
- The logs track the status of files during data ingestion jobs.
- The jobs show whether the files were successfully ingested, ignored, or failed.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
