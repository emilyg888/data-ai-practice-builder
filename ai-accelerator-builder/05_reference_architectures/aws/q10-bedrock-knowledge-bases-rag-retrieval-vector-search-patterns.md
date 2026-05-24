---
type: reference_note
platform: aws
status: draft
source: udemy-question-10
title: 10: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon EventBridge
  - Amazon OpenSearch Service
  - Amazon S3
  - Bedrock Knowledge Bases
related_controls:
  - access_control
  - audit_logging
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - event orchestration
  - vector search
  - s3 data assets
  - knowledge bases
  - access control
  - audit logging
  - retrieval grounding
use_cases:
  - policy assistance
  - model governance
---

# 10: Knowledge Base And RAG Patterns

## Scenario

A risk and compliance team is building an internal Q&A assistant by using Amazon Bedrock Knowledge Bases backed by an Amazon OpenSearch Service vector store. Source policy documents are stored in Amazon S3 and are frequently updated throughout the day (new versions, replacements, and deletions). Users report that answers sometimes reference outdated policy language. The team needs an automated data maintenance approach that detects document changes in near real time and keeps the vector store synchronized with the latest content with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Configure Amazon S3 event notifications for object create, overwrite, and delete events to Amazon EventBridge. Create an EventBridge rule that invokes an AWS Lambda function to call StartIngestionJob for the Amazon Bedrock knowledge base whenever relevant S3...

## Architecture guidance

- Keeping a RAG vector store current requires both change detection and an automated synchronization mechanism that updates embeddings/index entries when source content changes.
- Using S3 events routed through EventBridge to trigger a Lambda function provides near-real-time detection of new, updated, or deleted documents and automatically initiates a knowledge base ingestion job to refresh the...
- Alternatives based on periodic batch refreshes increase staleness windows and can waste resources, while replication and access-log-driven pipelines add complexity without directly ensuring that embeddings and vector...

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
