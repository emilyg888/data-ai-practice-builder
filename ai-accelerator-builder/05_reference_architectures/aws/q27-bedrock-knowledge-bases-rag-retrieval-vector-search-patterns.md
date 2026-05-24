---
type: reference_note
platform: aws
status: draft
source: udemy-question-27
title: 27: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon OpenSearch Service
  - Amazon S3
related_controls:
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - vector search
  - s3 data assets
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
---

# 27: Knowledge Base And RAG Patterns

## Scenario

A media analytics team is building a Retrieval Augmented Generation (RAG) assistant by using Amazon Bedrock. Millions of internal articles are stored in Amazon S3 and are tagged by topic (for example, sports, finance, and entertainment). The team wants to segment the corpus by topic to improve retrieval precision. The team also wants the search tier to accept natural language queries and generate embeddings automatically so the application does not need to compute embeddings before querying the vector store. Which solution meets these requirements with the LEAST application-side implementation effort?

## Common implementation patterns

- Store the documents in Amazon S3. Create an Amazon OpenSearch Service domain with separate indices per topic. Configure the OpenSearch Neural plugin to call an Amazon Bedrock embedding model in an ingest pipeline and use neural queries so OpenSearch generates...
- Create an Amazon Bedrock Knowledge Base with the S3 bucket as the data source and an Amazon OpenSearch Serverless collection as the managed vector store. Use hierarchical chunking and let the Knowledge Base handle ingestion and retrieval for the application....

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- The best approach is to use Amazon OpenSearch Service as the vector store with topic-based segmentation (separate indices per topic) and integrate embedding generation directly into OpenSearch through the Neural plugin.
- This lets OpenSearch create embeddings for documents during ingestion and create embeddings for user queries at search time by invoking an Amazon Bedrock embedding model, enabling efficient semantic retrieval without...
- Other approaches either don’t offload embedding generation into the search tier or require inefficient retrieval patterns and substantial custom implementation.

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
