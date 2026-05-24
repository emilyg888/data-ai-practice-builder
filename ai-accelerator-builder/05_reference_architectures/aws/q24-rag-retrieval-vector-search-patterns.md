---
type: reference_note
platform: aws
status: draft
source: udemy-question-24
title: 24: Vector Store Patterns
pattern_family: rag
aws_services:
  - Amazon Bedrock
  - Amazon OpenSearch Service
related_controls:
  - model_evaluation
  - retrieval_grounding
topics:
  - vector store patterns
  - rag
  - bedrock
  - vector search
  - model evaluation
  - retrieval grounding
  - evaluation
use_cases:
  - search and retrieval
---

# 24: Vector Store Patterns

## Scenario

A retail operations team is building an internal troubleshooting assistant by using Amazon Bedrock and an Amazon OpenSearch Service vector index. The assistant retrieves chunks from repair manuals and incident reports. Engineers often search by exact error codes (for example, "ERR-1042") and also by natural language descriptions of symptoms. With the current semantic (vector-only) retrieval approach, searches sometimes miss the correct chunk that contains the exact code, and the returned top results are not consistently the most relevant. Which solution will improve retrieval relevance and accuracy with the LEAST operational overhead?

## Common implementation patterns

- Use an OpenSearch hybrid search approach that combines keyword matching on indexed fields (for example, errorCode and productId) with vector similarity search for semantic relevance. Then use an Amazon Bedrock reranker model to reorder the top retrieved...

## Architecture guidance

- The most effective low-overhead way to improve retrieval for both exact identifiers (like error codes) and descriptive queries is to combine keyword retrieval with semantic vector retrieval, then rerank the resulting...
- Hybrid search improves recall and precision when exact tokens matter, while a managed reranker improves the ordering of the top results without requiring the team to design, train, and operate a bespoke ranking system...
- Further reading (AWS): - Configure Neural Search and Hybrid Search on OpenSearch Serverless - Amazon OpenSearch Service (AWS Documentation) - Vector search - Amazon OpenSearch Service (AWS Documentation) - Improve the...

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
