---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-42
completeness: full
---

# 42: RAG Patterns

## Scenario

An aircraft repair company receives repair requests from various airlines. The company responds to the repair requests by providing an initial quote of the estimated labor hours, required spare parts, and a schedule for completion. The repair requests from airlines include a description of the defect and the aircraft model. The company uses repair manuals in PDF format to help resolve the repair requests. The repair manuals contain thousands of pages with nested and cross-referenced sections from the aircraft manufacturers. The repair manuals explain the necessary repair procedures and spare parts for the repair. The company wants to extract the repair procedures and spare parts from the repair manuals automatically by using RAG. The solution must provide high retrieval accuracy. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store repair manuals in Amazon S3 partitioned by aircraft model and part. Use Amazon Bedrock Knowledge Bases with a hierarchical chunking strategy. Use Amazon OpenSearch Serverless as a vector store.

## Common anti-patterns

- Avoid store repair manuals on Amazon DocumentDB serverless with search keys for aircraft model and part. Use Amazon Bedrock Knowledge Bases with a semantic chunking strategy. Use DocumentDB serverless as a vector store. because documentDB serverless provides managed database...
- Avoid store repair manuals on Amazon DocumentDB serverless with search keys for aircraft model and part. Use Amazon OpenSearch Serverless with the neural plugin hierarchical chunking strategy. because documentDB serverless provides managed database capabilities to store JSON...
- Avoid store repair manuals in Amazon S3 partitioned by aircraft model and part. Use Amazon Bedrock Knowledge Bases with a semantic chunking strategy. Use Amazon OpenSearch Serverless as a vector store. because this solution provides a fully managed RAG workflow. However,...

## Architecture guidance

- Knowledge Bases is a fully managed end-to-end RAG workflow.
- Knowledge Bases integrates with OpenSearch Serverless as a vector store.
- Knowledge Bases supports Amazon S3 as a data source.
