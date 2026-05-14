---
type: reference_note
platform: aws
status: draft
source: udemy-question-16
---

# 16: Knowledge Base And RAG Patterns

## Scenario

A large enterprise is building a Retrieval Augmented Generation (RAG) application by using Amazon Bedrock. The team stores embeddings and document chunks in Amazon OpenSearch Service and has grown to tens of millions of chunks across multiple business domains (HR policies, engineering runbooks, and legal templates). Users are experiencing increased query latency during peak hours, and the OpenSearch cluster shows signs of JVM memory pressure. The team also needs to tune index settings and, if necessary, use different embedding approaches for different domains. Which design will optimize semantic search performance at scale MOST effectively?

## Common implementation patterns

- Implement a multi-index strategy with separate indexes per domain and use a hierarchical indexing approach: a small top-level summary/metadata index routes queries to the appropriate domain index. Use fewer, larger shards for the domain indexes to reduce...

## Common anti-patterns

- Avoid move older vectors to UltraWarm storage and increase the replica count to improve read scalability for semantic search queries. because ultraWarm is a cost-optimization tier primarily for indices with few writes and is slower than hot storage....

## Architecture guidance

- High-performance semantic retrieval at scale is heavily influenced by index architecture and shard strategy.
- Splitting data into multiple indexes by domain allows each corpus to be tuned independently (for example, different mappings, shard sizes, and embedding strategies), which is difficult with a single monolithic index.
- A hierarchical approach, where a small top-level index helps route queries to a domain-specific index, reduces unnecessary searching across unrelated corpora and improves relevance and latency.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
