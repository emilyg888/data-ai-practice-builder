---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-22
completeness: full
---

# 22: Vector Search Patterns

## Scenario

A company is designing an advanced vector database architecture for FM augmentation. A GenAI developer must configure each architectural requirement. Select the correct AWS service configuration from the following list for each architectural requirement. Select each service configuration one time or not at all. (Select THREE.)

## Common implementation patterns

- Use Amazon OpenSearch Service with the k-nearest neighbor (k-NN) plugin when you need distributed similarity search across billions of product catalog vectors with custom relevance scoring.
- Use Amazon Aurora PostgreSQL with pgvector when you need to combine metadata filtering with vector search while maintaining strong consistency for financial records.
- Use Amazon Neptune with vector search when you need graph-based vector search to identify relationships between research papers and their citations.

## Common anti-patterns

- Avoid using DynamoDB vector support for billion-scale distributed similarity search with custom relevance scoring.
- Avoid using graph-first vector search when the requirement is strong consistency plus metadata filtering for financial records.
- Avoid using relational vector storage when the primary requirement is graph-based citation and relationship traversal.

## Architecture guidance

- OpenSearch Service with the k-NN plugin can handle distributed similarity search across billions of product catalog vectors with custom relevance scoring.
- OpenSearch Service provides a distributed architecture that can scale to billions of vectors across multiple shards.
- OpenSearch Service is unique in providing custom plugins to fine-tune search relevance compared to the other options.
