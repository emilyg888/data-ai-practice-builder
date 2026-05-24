---
type: reference_note
platform: aws
status: draft
source: udemy-question-33
title: 33: Throughput Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
related_controls:
  - monitoring
  - retrieval_grounding
topics:
  - throughput patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - monitoring
  - s3 data assets
  - retrieval grounding
use_cases:
  - cost optimization
  - multimodal extraction
---

# 33: Throughput Patterns

## Scenario

A financial services innovation team wants to pilot an internal “AI search” assistant that answers questions about employee policy PDFs stored in Amazon S3. The team needs a technical proof of concept within 2 weeks, wants to avoid managing servers, and must produce initial measurements of per-question latency and token-related cost before committing to a production rollout. Which combination of actions will meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base that ingests the policy PDFs from Amazon S3 with managed chunking and an embedding model. Implement a simple API backed by AWS Lambda that calls RetrieveAndGenerate to answer pilot user questions. This is the managed or...
- Instrument the proof of concept to estimate and track token usage and latency by using the Amazon Bedrock CountTokens API and Amazon CloudWatch metrics (such as input and output token counts, invocation count, and model latency). This is the managed or...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A low-overhead proof of concept should rely on managed GenAI building blocks and lightweight measurement.
- Using a Bedrock Knowledge Base with documents in S3 provides a fast “chat with your documents” style RAG implementation without building and operating a custom retrieval pipeline.
- Pairing the pilot with token and latency measurement through CountTokens and CloudWatch produces the core feasibility signals (cost per request and responsiveness) needed to decide whether to proceed to a full...

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
