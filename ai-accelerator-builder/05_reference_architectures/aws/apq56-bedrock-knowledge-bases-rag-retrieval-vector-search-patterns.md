---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-56
completeness: full
title: 56: RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - model_evaluation
  - retrieval_grounding
topics:
  - rag patterns
  - bedrock knowledge bases
  - bedrock
  - knowledge bases
  - model evaluation
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - customer-facing assistant
  - document summarization
  - search and retrieval
---

# 56: RAG Patterns

## Scenario

A company developed a tool to assist customer support representatives. The tool summarizes relevant support documents for the case that a customer support representative works on. The tool uses a custom RAG system. The system is backed by a third-party vector store that stores document embeddings. The RAG system retrieves the top-k relevant chunks based on the current support case. The generative model that summarizes the documents runs on Amazon Bedrock. Recently, customer support representatives report that the summaries are contextually irrelevant and do not directly relate to the support cases. A GenAI developer verifies that the chunks retrieved from the vector store have high embedding similarity scores. The GenAI developer validates that the embedding model produces accurate representations and that the chunking strategy is consistent. The GenAI developer wants to improve the summarization to return more contextually relevant summaries. The GenAI developer wants to continue using Amazon Bedrock hosted models. The GenAI developer does not want to re-train any LLMs. Which strategies will improve the relevance of retrieved context? (Select TWO.)

## Common implementation patterns

- Migrate to using Amazon Bedrock Knowledge Bases for retrieval. Configure reranking when retrieving chunks.
- Add a reranking step after initial retrieval by invoking a rerank model in Amazon Bedrock. Configure the rerank model to rescore and sort retrieved chunks before generation.

## Architecture guidance

- Reranking is a feature of Amazon Bedrock that reorders chunks based on relevancy to the query.
- Knowledge Bases provides built-in reranking mechanisms that improve contextual relevance.
- You can migrate to an Amazon Bedrock knowledge base to offload relevance scoring.

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
