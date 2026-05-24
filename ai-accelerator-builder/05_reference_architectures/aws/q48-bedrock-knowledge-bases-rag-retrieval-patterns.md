---
type: reference_note
platform: aws
status: draft
source: udemy-question-48
title: 48: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - prompt_policy
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - state store
  - prompt policy
  - retrieval grounding
  - rag
use_cases:
  - cost optimization
---

# 48: Knowledge Base And RAG Patterns

## Scenario

A SaaS provider is building a customer-support chat application that uses the Amazon Bedrock Converse API with a single FM. The application stores full conversation history in Amazon DynamoDB and uses an Amazon Bedrock Knowledge Base for RAG. As usage grows, the company’s Bedrock spend increases sharply, and some requests fail when the prompt exceeds the model’s context window. The company wants to reduce token-related costs while preserving answer quality. Which combination of actions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Before each model invocation, call the Amazon Bedrock CountTokens API to estimate total input size. If the request exceeds a token budget, prune older conversation turns and reduce the number of retrieved chunks from the knowledge base. Publish input and...
- Implement prompt compression by using a smaller FM to summarize older conversation history into a short running summary that is stored in DynamoDB. Include only the summary plus the most recent turns in each request and set maxTokens to limit response size....

## Architecture guidance

- The most effective token-efficiency approaches reduce how many tokens are included in each request while preserving the information needed for accurate answers.
- Estimating tokens before invocation enables enforcing a token budget and applying deterministic reductions such as pruning conversation history and limiting retrieved RAG context.
- Prompt compression through summarization is another high-impact technique: it replaces long histories with a compact summary plus recent turns, and response limiting prevents large completions from driving up cost.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
