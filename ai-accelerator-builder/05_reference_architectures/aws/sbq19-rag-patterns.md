---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-19
completeness: full
---

# 19: RAG Patterns

## Scenario

A company is developing a RAG application by using Amazon Bedrock. The application processes customer support documents. Initially, the application retrieves many relevant documents. However, users report that the most relevant information often appears lower in the results. The company wants to improve the relevance ranking of retrieved results to ensure that the most useful information appears first. Which combination of steps will improve the relevance of retrieved results with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Use Amazon Bedrock reranker models with Amazon OpenSearch Service to reorder retrieved results based on semantic relevance to the query.
- Use Knowledge Bases with hybrid search capabilities and Amazon OpenSearch Serverless to combine vector embeddings with keyword matching.

## Common anti-patterns

- Avoid configure Amazon OpenSearch Serverless with the Amazon Bedrock Knowledge Bases plugin. Use OpenSearch's Learning to Rank feature for relevance scoring. Integrate relevance scoring with Knowledge Bases for result reranking. because openSearch Service provides vector search capabilities....
- Avoid create an Amazon Aurora PostgreSQL database with the pgvector extension to store document embeddings. Create a similarity scoring algorithm that combines vector distances with document metadata to rank results. because aurora with the pgvector extension supports vector operations. However,...
- Avoid use Amazon SageMaker JumpStart FMs with Amazon Kendra Intelligent Ranking to create custom relevancy scoring algorithms. because sageMaker JumpStart provides access to FMs. Amazon Kendra Intelligent Ranking can improve search results. However, Amazon Bedrock already provides built-in...

## Architecture guidance

- Amazon Bedrock reranker models are specifically designed to improve the relevance of retrieved results.
- The reranker models calculate relevance scores between queries and documents.
- Then, the reranker models reorder the results based on the scores.
