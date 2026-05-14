---
type: reference_note
platform: aws
status: draft
source: udemy-question-6
---

# 6: Knowledge Base And RAG Patterns

## Scenario

A media company is building an internal “chat with your documents” assistant by using Amazon Bedrock Knowledge Bases backed by Amazon OpenSearch Service. Source documents are stored in Amazon S3 and include multiple versions of policies written by different teams. Users frequently ask questions such as “What is the latest policy for content takedown?” and need the response to reflect the correct business unit and the most recent document. The company wants to improve retrieval precision and give the FM better context (for example, document timestamps and authorship) with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Define a standardized metadata schema (for example, business_unit, author, document_timestamp, topic tags). Store timestamps and authorship as S3 object metadata or as extracted fields, and configure the knowledge base to treat these fields as metadata (not...

## Common anti-patterns

- Avoid regenerate embeddings with a larger vector dimensionality for the embedding model so the vector store can better distinguish older and newer versions of similar documents. because increasing embedding dimensionality can increase storage and compute cost...

## Architecture guidance

- To improve retrieval precision for RAG, document attributes like timestamps, authorship, business unit ownership, and domain/topic tags should be captured as explicit metadata and kept separate from chunked text.
- This lets the retrieval layer use consistent, structured signals to select the right documents (especially among near-duplicates and multiple versions) while also providing the FM with better context for grounded...
- Approaches that try to “hide” metadata inside chunk text, increase embedding dimensionality, or perform query-time extraction add cost, noise, or operational burden without directly addressing versioning and ownership...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
