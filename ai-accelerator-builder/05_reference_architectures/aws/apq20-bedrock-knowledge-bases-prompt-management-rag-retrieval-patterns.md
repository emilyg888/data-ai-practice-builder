---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-20
completeness: full
title: 20: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - bedrock
  - knowledge bases
use_cases:
  - search and retrieval
---

# 20: Knowledge Base Patterns

## Scenario

A GenAI developer at a media company is building a question-answering AI assistant by using Amazon Bedrock Knowledge Bases. The AI assistant needs to answer user questions accurately based on only the most recent documents. The GenAI developer must ensure that the AI assistant ignores older documents. Which solution will meet these requirements?

## Common implementation patterns

- Add a metadata filter for modification time.

## Architecture guidance

- You can use the metadata filter modification_time to restrict the source documents based on timestamps.
- You can add a metadata filter to ensure that the model retrieves only recently updated documents.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
