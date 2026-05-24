---
type: reference_note
platform: aws
status: draft
source: udemy-question-6
title: 6: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon OpenSearch Service
  - Amazon S3
  - Bedrock Knowledge Bases
related_controls:
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - vector search
  - s3 data assets
  - knowledge bases
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
---

# 6: Knowledge Base And RAG Patterns

## Scenario

A media company is building an internal “chat with your documents” assistant by using Amazon Bedrock Knowledge Bases backed by Amazon OpenSearch Service. Source documents are stored in Amazon S3 and include multiple versions of policies written by different teams. Users frequently ask questions such as “What is the latest policy for content takedown?” and need the response to reflect the correct business unit and the most recent document. The company wants to improve retrieval precision and give the FM better context (for example, document timestamps and authorship) with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Define a standardized metadata schema (for example, business_unit, author, document_timestamp, topic tags). Store timestamps and authorship as S3 object metadata or as extracted fields, and configure the knowledge base to treat these fields as metadata (not...

## Architecture guidance

- To improve retrieval precision for RAG, document attributes like timestamps, authorship, business unit ownership, and domain/topic tags should be captured as explicit metadata and kept separate from chunked text.
- This lets the retrieval layer use consistent, structured signals to select the right documents (especially among near-duplicates and multiple versions) while also providing the FM with better context for grounded...
- Approaches that try to “hide” metadata inside chunk text, increase embedding dimensionality, or perform query-time extraction add cost, noise, or operational burden without directly addressing versioning and ownership...

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
