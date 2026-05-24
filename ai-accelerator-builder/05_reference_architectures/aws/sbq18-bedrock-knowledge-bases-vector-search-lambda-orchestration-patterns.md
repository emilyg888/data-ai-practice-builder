---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-18
completeness: partial
title: 18: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon EventBridge
  - Amazon S3
  - Bedrock Knowledge Bases
related_controls:
  - prompt_policy
  - retrieval_grounding
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - event orchestration
  - s3 data assets
  - knowledge bases
  - prompt policy
  - retrieval grounding
  - rag
use_cases:
  - customer-facing assistant
---

# 18: Knowledge Base Patterns

## Scenario

A company uses an AI assistant to answer customer questions based on internal company documents. The company wants to include new documents in the assistant's responses as soon as possible. The company wants to exclude deleted documents from the AI assistant's responses as soon as possible. The documents are stored in Amazon S3. The AI assistant uses Amazon Bedrock Knowledge Bases. Amazon S3 is the data source of the vector store that the company uses for RAG. A GenAI developer must create a scalable, event-driven, and resilient solution. Which solution will meet these requirements?

## Common implementation patterns

- Use an event-driven document synchronization workflow that reacts to object creation and deletion events instead of periodic polling.

## Architecture guidance

- EventBridge Scheduler provides time-based actions for different AWS services.
- Running the sync action every 5 minutes is not suitable for near real-time updates to the knowledge base.
- This solution introduces delays in including new documents in the knowledge base.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
