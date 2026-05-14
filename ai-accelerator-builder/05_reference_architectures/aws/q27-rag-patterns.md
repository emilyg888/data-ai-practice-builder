---
type: reference_note
platform: aws
status: draft
source: udemy-question-27
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

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
