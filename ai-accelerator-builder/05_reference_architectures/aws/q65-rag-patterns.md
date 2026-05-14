---
type: reference_note
platform: aws
status: draft
source: udemy-question-65
---

# 65: Knowledge Base And RAG Patterns

## Scenario

A media analytics company is building a RAG assistant on AWS by using Amazon Bedrock for text generation. For the retrieval layer, some workloads use Amazon OpenSearch Service for vector search, while other workloads use Amazon Aurora PostgreSQL with the pgvector extension for advanced metadata filtering. The GenAI team wants a single, consistent retrieval interface that Bedrock-based applications can use without being rewritten when the underlying vector store changes. Which solution will provide the MOST seamless integration mechanism for retrieval augmentation across these vector stores?

## Common implementation patterns

- Create a stateless Model Context Protocol (MCP) server (for example, on AWS Lambda) that exposes a single tool such as "vector_search" with a stable JSON input/output contract. Use an MCP client library in the application/agent runtime to call this tool, and...
- Store embeddings and document chunks directly in Amazon S3 objects and retrieve relevant chunks by using S3 prefix filters and object metadata filters. Pass the retrieved objects as context to the model. This is the managed or lower-overhead approach called...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A consistent access mechanism for retrieval augmentation is best achieved by placing a stable, tool-like contract in front of the retrieval layer and letting applications or agents invoke that contract in the same way...
- Using an MCP server to expose a single vector-query tool, combined with an MCP client in the runtime, standardizes how the FM-integrated system performs retrieval and returns normalized results (for example, chunks plus...
- This approach prevents tight coupling to OpenSearch-specific or Aurora/SQL-specific query logic and avoids rewriting application integrations when the organization changes vector stores.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
