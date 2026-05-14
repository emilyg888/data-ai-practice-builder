---
type: reference_note
platform: aws
status: draft
source: udemy-question-24
---

# 24: Vector Store Patterns

## Scenario

A retail operations team is building an internal troubleshooting assistant by using Amazon Bedrock and an Amazon OpenSearch Service vector index. The assistant retrieves chunks from repair manuals and incident reports. Engineers often search by exact error codes (for example, "ERR-1042") and also by natural language descriptions of symptoms. With the current semantic (vector-only) retrieval approach, searches sometimes miss the correct chunk that contains the exact code, and the returned top results are not consistently the most relevant. Which solution will improve retrieval relevance and accuracy with the LEAST operational overhead?

## Common implementation patterns

- Use an OpenSearch hybrid search approach that combines keyword matching on indexed fields (for example, errorCode and productId) with vector similarity search for semantic relevance. Then use an Amazon Bedrock reranker model to reorder the top retrieved...

## Common anti-patterns

- Avoid remove the retrieval layer and rely on a larger foundation model with improved prompt engineering and few-shot examples so the model can answer from its pretrained knowledge. because removing retrieval reduces grounding in the team’s internal documents...

## Architecture guidance

- The most effective low-overhead way to improve retrieval for both exact identifiers (like error codes) and descriptive queries is to combine keyword retrieval with semantic vector retrieval, then rerank the resulting...
- Hybrid search improves recall and precision when exact tokens matter, while a managed reranker improves the ordering of the top results without requiring the team to design, train, and operate a bespoke ranking system...
- Further reading (AWS): - Configure Neural Search and Hybrid Search on OpenSearch Serverless - Amazon OpenSearch Service (AWS Documentation) - Vector search - Amazon OpenSearch Service (AWS Documentation) - Improve the...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
