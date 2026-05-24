---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-32
completeness: full
title: 32: Prompt Management and Knowledge Bases for Chained Support Chat
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - audit_logging
  - prompt_policy
  - retrieval_grounding
topics:
  - prompt management knowledge bases
  - chained support chat
  - bedrock knowledge bases
  - bedrock
  - knowledge bases
  - audit logging
  - prompt policy
  - retrieval grounding
  - prompt management
use_cases:
  - document summarization
  - routing and orchestration
---

# 32: Prompt Management and Knowledge Bases for Chained Support Chat

## Pattern summary

Combine Bedrock Knowledge Bases, Prompt Management, and orchestration logic to run chained LLM calls for sentiment classification, document summarization, and response generation.

## Scenario

A company develops an AI-powered product support chat assistant for a website. The architecture requires the chaining of the following three LLM calls: The first LLM call classifies the sentiment of the messages. The second LLM call summarizes documents from a product database. The third LLM call creates the final response. The company wants to maintain versions of the LLM prompts. The company wants to be able to roll back quickly if a new prompt underperforms. Which solution will meet these requirements with the LEAST development effort?

## Common implementation patterns

- Create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock Flows.

## Architecture guidance

- Knowledge Bases is a managed RAG service that you can use to securely connect an LLM to enterprise data.
- Prompt Management provides lifecycle control for prompts.
- Flows is a visual orchestration service that you can use to chain multiple LLM calls.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
