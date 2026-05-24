---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-58
completeness: full
title: 58: RAG Patterns
pattern_family: rag
aws_services:
  - Amazon Bedrock
  - Amazon OpenSearch Service
related_controls:
  - prompt_policy
  - retrieval_grounding
topics:
  - rag patterns
  - rag
  - bedrock
  - vector search
  - prompt policy
  - retrieval grounding
  - prompt management
  - evaluation
use_cases:
  - customer-facing assistant
  - search and retrieval
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

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
