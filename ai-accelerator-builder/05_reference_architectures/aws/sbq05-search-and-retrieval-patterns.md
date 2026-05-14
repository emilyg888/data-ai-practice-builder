---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-5
completeness: full
---

# 5: Search And Retrieval Patterns

## Scenario

A company is building a diagnostic imaging application. The application needs to perform similarity searches across 50 million images to assist with diagnosing and treating patients. The application must process new images daily. The application will perform similarity searches infrequently when users need to find similar cases for reference. The company wants a cost-effective solution that provides responsive search performance without requiring infrastructure management. Which solution will meet these requirements MOST cost-effectively?

## Common implementation patterns

- Create an Amazon S3 vector bucket with vector indexes to store image embeddings and perform similarity searches.

## Common anti-patterns

- Avoid store image vectors in Amazon OpenSearch Serverless. Use vector search capabilities for similarity searches. because openSearch Serverless is optimized for high-throughput, low-latency workloads with frequent searches. OpenSearch Service supports vector similarity search through k-nearest...
- Avoid use Amazon DynamoDB to store image vectors. Implement custom similarity search logic by using AWS Lambda functions. because dynamoDB is a scalable NoSQL database that is optimized for key-value and document access patterns. DynamoDB does not provide built-in support for vector similarity...
- Avoid store image vectors in Amazon RDS for PostgreSQL. Use the pgvector extension to perform similarity searches using indexed vector embeddings. because rDS for PostgreSQL supports the pgvector extension. The pgvector extension provides similarity search on vector embeddings by using SQL queries....

## Architecture guidance

- S3 Vectors is a fully managed, serverless feature of Amazon S3 that provides scalable vector search capabilities.
- S3 Vectors can store and search vector data.
- S3 Vectors can support up to billions of vectors.
