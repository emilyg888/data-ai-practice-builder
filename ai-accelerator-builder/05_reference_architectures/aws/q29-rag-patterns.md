---
type: reference_note
platform: aws
status: draft
source: udemy-question-29
---

# 29: Knowledge Base And RAG Patterns

## Scenario

A global HR SaaS provider is building a semantic search feature for internal policy documents by using a RAG architecture. The team will embed millions of document chunks and store the vectors in a vector database for similarity search. The solution must keep vector storage costs low while maintaining search relevance for the organization’s terminology, and the embedding generation process must efficiently handle nightly ingestion of large document batches. Which combination of actions will meet these requirements MOST cost-effectively? (Select TWO.)

## Common implementation patterns

- Run a proof of concept that generates embeddings for a representative set of documents and queries by using multiple Amazon Bedrock embedding models (for example, Amazon Titan embeddings and an alternative embedding model). Compare retrieval quality metrics...
- Use an Amazon Titan embedding model and configure a smaller embedding vector dimension after validating that retrieval relevance remains acceptable for the policy-document domain. Use AWS Lambda to batch-generate embeddings for new chunks before writing them...
- Use Amazon Comprehend to classify each document into topics and store only the topic labels. Use keyword search on the labels instead of generating embeddings to reduce cost. This is the managed or lower-overhead approach called out as correct in the exam...

## Common anti-patterns

- Avoid configure the embedding model to use the maximum available vector dimension to improve accuracy. Invoke the embedding model from the application for each chunk individually to avoid batching complexity. because always maximizing dimensionality can...

## Architecture guidance

- To keep costs low at scale, the embedding strategy should reduce the size and number of vectors stored while preserving retrieval quality.
- Configuring an embedding model with an appropriately smaller vector dimension can materially reduce vector storage and indexing costs, but it must be validated against real queries to avoid harming relevance.
- Because different embedding models can behave differently across domains and languages, testing multiple Bedrock embedding model options on representative data is a reliable way to choose the best fit.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
