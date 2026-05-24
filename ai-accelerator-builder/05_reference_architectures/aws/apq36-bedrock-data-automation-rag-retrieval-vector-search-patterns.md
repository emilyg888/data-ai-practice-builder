---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-36
completeness: full
title: 36: BDA Transformation Patterns
pattern_family: rag
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - evidence_retention
  - retrieval_grounding
topics:
  - bda transformation patterns
  - rag
  - lambda orchestration
  - bedrock
  - state store
  - evidence retention
  - retrieval grounding
  - evaluation
use_cases:
  - search and retrieval
  - real-time streaming
---

# 36: BDA Transformation Patterns

## Scenario

A GenAI developer is creating a chat application. The application integrates an Amazon Bedrock FM through AWS Lambda and exposes a REST API. The application requires conversation history functionality that supports concurrent user sessions with real-time updates. Users must be able to resume conversations from any point in the history. The application must provide metadata-based search and filtering while maintaining conversation context for the FM. The application requires low-latency retrieval of recent conversations. The application requires retention policies that automatically delete older conversations when the conversations expire. Which solution will provide the MOST scalable implementation of conversation history?

## Common implementation patterns

- Create an Amazon DynamoDB table with global secondary indexes (GSI) for user ID and conversation ID. Use a single-table design with hierarchical sort keys to store messages, metadata, and conversation state. Implement DynamoDB Accelerator (DAX) to cache recent conversations....

## Architecture guidance

- DynamoDB with GSI and a single-table design provides a highly scalable solution for conversation storage.
- This solution supports metadata-based queries by user ID, conversation ID, and date ranges.
- You can use hierarchical sort keys to efficiently query conversation history while maintaining relationships between messages and metadata.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
