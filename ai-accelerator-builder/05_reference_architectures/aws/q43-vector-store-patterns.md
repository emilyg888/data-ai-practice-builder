---
type: reference_note
platform: aws
status: draft
source: udemy-question-43
---

# 43: Vector Store Patterns

## Scenario

An online retailer’s GenAI team is building a product discovery feature on Amazon Bedrock. Customers will search either by uploading a product photo or by entering a short text description. The backend will perform semantic similarity search in a vector store so the same search experience works for both photos and text queries. Which Amazon Bedrock foundation model choice will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use an Amazon Titan multimodal embeddings model to generate embeddings from both the product image and associated text so they can be compared in the same vector space. This is the managed or lower-overhead approach called out as correct in the exam...

## Common anti-patterns

- Avoid use Anthropic Claude to answer user queries conversationally and include the entire product catalog in the prompt so the model can find the best matching items without vector search. because this does not align with the technical requirement to use...

## Architecture guidance

- The key technical requirement is to support semantic similarity search when the query might be either an image or text.
- This requires an embeddings model that can produce comparable vectors for both modalities.
- A Titan multimodal embeddings model provides this capability directly, allowing the application to embed product images and user photo queries using the same embedding approach used for text.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
