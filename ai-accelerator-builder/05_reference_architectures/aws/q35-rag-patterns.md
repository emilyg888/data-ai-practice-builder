---
type: reference_note
platform: aws
status: draft
source: udemy-question-35
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

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
