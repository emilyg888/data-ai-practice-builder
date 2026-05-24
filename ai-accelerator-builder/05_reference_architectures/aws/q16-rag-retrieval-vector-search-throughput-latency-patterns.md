---
type: reference_note
platform: aws
status: draft
source: udemy-question-16
title: 16: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon OpenSearch Service
related_controls:
  - model_evaluation
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - vector search
  - model evaluation
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
---

# 16: Knowledge Base And RAG Patterns

## Scenario

A large enterprise is building a Retrieval Augmented Generation (RAG) application by using Amazon Bedrock. The team stores embeddings and document chunks in Amazon OpenSearch Service and has grown to tens of millions of chunks across multiple business domains (HR policies, engineering runbooks, and legal templates). Users are experiencing increased query latency during peak hours, and the OpenSearch cluster shows signs of JVM memory pressure. The team also needs to tune index settings and, if necessary, use different embedding approaches for different domains. Which design will optimize semantic search performance at scale MOST effectively?

## Common implementation patterns

- Implement a multi-index strategy with separate indexes per domain and use a hierarchical indexing approach: a small top-level summary/metadata index routes queries to the appropriate domain index. Use fewer, larger shards for the domain indexes to reduce...

## Architecture guidance

- High-performance semantic retrieval at scale is heavily influenced by index architecture and shard strategy.
- Splitting data into multiple indexes by domain allows each corpus to be tuned independently (for example, different mappings, shard sizes, and embedding strategies), which is difficult with a single monolithic index.
- A hierarchical approach, where a small top-level index helps route queries to a domain-specific index, reduces unnecessary searching across unrelated corpora and improves relevance and latency.

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

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
