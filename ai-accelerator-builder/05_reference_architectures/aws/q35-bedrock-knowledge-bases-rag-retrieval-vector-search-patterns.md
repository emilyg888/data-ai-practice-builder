---
type: reference_note
platform: aws
status: draft
source: udemy-question-35
title: 35: Knowledge Base And RAG Patterns
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
  - internal assistant
  - policy assistance
  - search and retrieval
---

# 35: Knowledge Base And RAG Patterns

## Scenario

A fintech engineering team is building an internal policy assistant that uses Retrieval Augmented Generation (RAG) with Amazon Bedrock. Policy documents are stored in Amazon S3. The team needs semantic search over the documents to provide relevant context to the foundation model (FM). The team wants a solution that requires the LEAST operational overhead to deploy and operate. Which solution will meet these requirements?

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base that uses the S3 bucket as a data source. Select an embedding model (for example, Amazon Titan Embeddings) and use a managed vector store option backed by Amazon OpenSearch Service. Configure chunking, then use the...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- The key requirement is to deploy and configure semantic retrieval with minimal operational burden.
- A managed knowledge base in Amazon Bedrock is purpose-built for RAG: it connects to an S3 data source, chunks content, generates embeddings with a chosen embedding model, and stores/indexes those embeddings in a managed...
- Alternatives that directly use OpenSearch or Aurora can achieve vector search, but they require the team to build and maintain ingestion pipelines, embedding generation, index/schema design, and retrieval integration.

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
