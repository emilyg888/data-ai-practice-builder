---
type: reference_note
platform: aws
status: draft
source: udemy-question-43
title: 43: Vector Store Patterns
pattern_family: vector_store
aws_services:
  - Amazon Bedrock
related_controls:
topics:
  - vector store patterns
  - vector store
  - bedrock
use_cases:
  - multimodal extraction
---

# 43: Vector Store Patterns

## Scenario

An online retailer’s GenAI team is building a product discovery feature on Amazon Bedrock. Customers will search either by uploading a product photo or by entering a short text description. The backend will perform semantic similarity search in a vector store so the same search experience works for both photos and text queries. Which Amazon Bedrock foundation model choice will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use an Amazon Titan multimodal embeddings model to generate embeddings from both the product image and associated text so they can be compared in the same vector space. This is the managed or lower-overhead approach called out as correct in the exam...

## Architecture guidance

- The key technical requirement is to support semantic similarity search when the query might be either an image or text.
- This requires an embeddings model that can produce comparable vectors for both modalities.
- A Titan multimodal embeddings model provides this capability directly, allowing the application to embed product images and user photo queries using the same embedding approach used for text.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
