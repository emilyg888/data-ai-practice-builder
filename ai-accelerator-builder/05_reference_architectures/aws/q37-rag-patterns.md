---
type: reference_note
platform: aws
status: draft
source: udemy-question-37
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

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
