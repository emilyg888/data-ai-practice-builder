---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-19
completeness: full
title: 19: RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon OpenSearch Service
related_controls:
  - model_evaluation
  - retrieval_grounding
topics:
  - rag patterns
  - bedrock knowledge bases
  - bedrock
  - vector search
  - model evaluation
  - retrieval grounding
  - rag
use_cases:
  - customer-facing assistant
  - search and retrieval
---

# 19: RAG Patterns

## Scenario

A company is developing a RAG application by using Amazon Bedrock. The application processes customer support documents. Initially, the application retrieves many relevant documents. However, users report that the most relevant information often appears lower in the results. The company wants to improve the relevance ranking of retrieved results to ensure that the most useful information appears first. Which combination of steps will improve the relevance of retrieved results with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Use Amazon Bedrock reranker models with Amazon OpenSearch Service to reorder retrieved results based on semantic relevance to the query.
- Use Knowledge Bases with hybrid search capabilities and Amazon OpenSearch Serverless to combine vector embeddings with keyword matching.

## Architecture guidance

- Amazon Bedrock reranker models are specifically designed to improve the relevance of retrieved results.
- The reranker models calculate relevance scores between queries and documents.
- Then, the reranker models reorder the results based on the scores.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
