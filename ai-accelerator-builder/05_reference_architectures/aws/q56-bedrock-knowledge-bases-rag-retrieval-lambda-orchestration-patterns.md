---
type: reference_note
platform: aws
status: draft
source: udemy-question-56
title: 56: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - knowledge bases
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
  - model governance
  - cost optimization
  - multimodal extraction
---

# 56: Knowledge Base And RAG Patterns

## Scenario

A compliance engineering team at a fintech is building a Retrieval Augmented Generation (RAG) assistant by using Amazon Bedrock Knowledge Bases. The team ingests long HR and benefits policy PDFs. Users often ask narrow questions such as eligibility exceptions and edge cases that appear in short paragraphs. With the current ingestion settings, the retrieval step frequently returns broad passages that bury the relevant clause, and the model sometimes answers without enough surrounding context to justify the result. The team wants to improve retrieval precision while still providing sufficient context for grounded answers with the LEAST ingestion-time operational overhead and cost. Which document segmentation approach should the team use?

## Common implementation patterns

- Configure the knowledge base to use hierarchical chunking so the retriever indexes smaller child chunks for precise matching and then returns the corresponding larger parent chunks to provide additional context. This is the managed or lower-overhead approach...

## Architecture guidance

- Hierarchical chunking is purpose-built for RAG document segmentation when answers depend on small, specific passages but still require surrounding context.
- By indexing smaller child chunks, the retrieval step can match user questions to the most relevant fine-grained content.
- By returning the associated parent chunk, the system supplies additional surrounding text for grounding and justification.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
