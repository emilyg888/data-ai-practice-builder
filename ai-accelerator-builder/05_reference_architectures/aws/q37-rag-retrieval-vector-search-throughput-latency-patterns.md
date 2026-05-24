---
type: reference_note
platform: aws
status: draft
source: udemy-question-37
title: 37: Knowledge Base And RAG Patterns
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

# 37: Knowledge Base And RAG Patterns

## Scenario

A security operations team is building a Retrieval Augmented Generation (RAG) assistant by using Amazon Bedrock. The team stores runbooks and incident reports in Amazon OpenSearch Service as a vector store. Engineers often search by exact identifiers (for example, CVE IDs and command names), but the assistant frequently retrieves semantically similar documents that do not contain the exact identifier. The team also observes increased retrieval latency as the OpenSearch index has grown. Which solution will improve retrieval relevance and retrieval latency with the LEAST operational overhead?

## Common implementation patterns

- In Amazon OpenSearch Service, implement hybrid search that combines vector similarity with keyword matching on identifier fields. Preprocess queries to extract exact identifiers into keyword clauses or metadata filters, and reindex the corpus into fewer,...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- Identifier-heavy queries (like CVE IDs and command names) are best served by combining semantic retrieval with exact matching.
- Hybrid search improves relevance by blending vector similarity with keyword scoring, and simple query preprocessing can reliably extract identifiers into keyword clauses or metadata filters.
- To address speed, index optimization in OpenSearch—such as reindexing into fewer, larger shards—reduces coordination overhead and improves query latency as the corpus grows.

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

- Content Domain 4: Operational Efficiency and Optimization fo
