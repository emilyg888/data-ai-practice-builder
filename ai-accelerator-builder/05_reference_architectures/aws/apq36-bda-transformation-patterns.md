---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-36
completeness: full
---

# 36: BDA Transformation Patterns

## Scenario

A GenAI developer is creating a chat application. The application integrates an Amazon Bedrock FM through AWS Lambda and exposes a REST API. The application requires conversation history functionality that supports concurrent user sessions with real-time updates. Users must be able to resume conversations from any point in the history. The application must provide metadata-based search and filtering while maintaining conversation context for the FM. The application requires low-latency retrieval of recent conversations. The application requires retention policies that automatically delete older conversations when the conversations expire. Which solution will provide the MOST scalable implementation of conversation history?

## Common implementation patterns

- Create an Amazon DynamoDB table with global secondary indexes (GSI) for user ID and conversation ID. Use a single-table design with hierarchical sort keys to store messages, metadata, and conversation state. Implement DynamoDB Accelerator (DAX) to cache recent conversations....

## Common anti-patterns

- Avoid use Amazon DynamoDB with a composite key of user ID and timestamp for conversation storage. Implement DynamoDB Streams to maintain a conversation cache in Amazon ElastiCache (Redis OSS). Configure DynamoDB TTL to delete older conversations. because dynamoDB with a...
- Avoid store conversations in Amazon OpenSearch Service with conversation metadata and full-text search capabilities. Use time-based indices to query. Configure Index State Management (ISM) policies to delete indices older than the specified retention window. because openSearch...
- Avoid implement a hybrid storage architecture. Use Amazon ElastiCache (Redis OSS) for active conversations with persistence enabled. Set key TTLs for active conversation entries. Use Amazon Aurora PostgreSQL with the pgvector extension for searchable conversation history and...

## Architecture guidance

- DynamoDB with GSI and a single-table design provides a highly scalable solution for conversation storage.
- This solution supports metadata-based queries by user ID, conversation ID, and date ranges.
- You can use hierarchical sort keys to efficiently query conversation history while maintaining relationships between messages and metadata.
