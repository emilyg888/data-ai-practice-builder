---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-58
completeness: full
---

# 58: RAG Patterns

## Scenario

A company wants to enhance a customer support AI assistant with up-to-date product information. A GenAI developer must implement a custom RAG solution by using Amazon Bedrock and Amazon OpenSearch Service. The GenAI developer needs to maintain complex relationships between product variants. The GenAI developer must implement hybrid search that combines semantic matching and keyword matching. Select and order each step from the following list to implement the RAG solution. Select each step one time. (Select and order FOUR.) Create initial embeddings and configure automated embedding generation for product updates. Deploy an FM and develop a prompt template with context retrieval. Implement vector search in OpenSearch Service with hybrid search capabilities. Set up a data ingestion pipeline to process and update product information.

## Common implementation patterns

- Set up a data ingestion pipeline to process and update product information. This is part of the endorsed implementation sequence and should be completed in order.
- Create initial embeddings and configure automated embedding generation for product updates. This is part of the endorsed implementation sequence and should be completed in order.
- Implement vector search in OpenSearch Service with hybrid search capabilities. This is part of the endorsed implementation sequence and should be completed in order.
- Deploy an FM and develop a prompt template with context retrieval. This is part of the endorsed implementation sequence and should be completed in order.

## Common anti-patterns

- Avoid implementing vector search before the ingestion pipeline and embedding workflow are in place.
- Avoid deploying the FM prompt layer before the retrieval and hybrid search components are verified.
- Avoid treating product-update embeddings as a manual or disconnected process when the solution requires ongoing synchronized updates.

## Architecture guidance

- This use case requires a strict sequence because of component dependencies.
- You must test and verify the solution at each phase.
- First, you must set up the data ingestion pipeline.
