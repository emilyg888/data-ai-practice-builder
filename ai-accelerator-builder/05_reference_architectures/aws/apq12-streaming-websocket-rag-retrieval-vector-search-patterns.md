---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-12
completeness: full
title: 12: Audit Logging Patterns
pattern_family: rag
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - audit_logging
  - pii_protection
  - retrieval_grounding
topics:
  - audit logging patterns
  - rag
  - lambda orchestration
  - step functions
  - bedrock
  - s3 data assets
  - audit logging
  - pii protection
  - retrieval grounding
use_cases:
  - document summarization
  - search and retrieval
  - model governance
---

# 12: Audit Logging Patterns

## Scenario

A large financial services company needs to implement a document processing solution by using generative AI (GenAI). The solution must process mortgage applications that contain sensitive customer information. Each application takes 5–15 minutes to process completely. Each application requires multiple FM calls for information extraction, analysis, and summarization. The solution must handle up to 1,000 concurrent requests during peak hours. The solution must provide audit trails for all AI model interactions. After processing, the results should be available for users to retrieve. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon S3 to store document uploads. Set up S3 Event Notifications to invoke an AWS Lambda function. Configure the Lambda function to invoke an AWS Step Functions standard workflow that orchestrates Amazon Bedrock model calls. Store processing status and results in Amazon...

## Architecture guidance

- Amazon S3 provides scalable, secure object storage for documents.
- S3 Event Notifications can invoke an AWS Lambda function.
- Step Functions standard workflows can run for up to 1 year and maintain detailed execution histories for auditing.

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
