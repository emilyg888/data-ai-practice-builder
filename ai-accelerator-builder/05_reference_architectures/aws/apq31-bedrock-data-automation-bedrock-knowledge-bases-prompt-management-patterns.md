---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-31
completeness: full
title: 31: Multimodal Analysis Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon Bedrock Data Automation
  - Bedrock Knowledge Bases
related_controls:
  - retrieval_grounding
topics:
  - multimodal analysis patterns
  - bedrock knowledge bases
  - bedrock
  - bedrock data automation
  - knowledge bases
  - retrieval grounding
  - rag
use_cases:
  - multimodal extraction
---

# 31: Multimodal Analysis Patterns

## Scenario

A financial analytics company wants to create a generative AI (GenAI) solution that can analyze a large amount of unstructured data. The unstructured data includes financial filing forms, quarterly earnings reports, analyst presentations, and audio/video (A/V) recordings of earnings calls. A GenAI developer must create a solution that can process the large amount of unstructured data. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Data Automation (BDA) as a parser to extract insights from multimodal content. Create a knowledge base by using Amazon Bedrock Knowledge Bases for RAG workflows.

## Architecture guidance

- BDA extracts insights from unstructured multimodal content including documents, forms, and A/V recordings.
- BDA streamlines the processing of diverse financial data sources.
- BDA can automatically create knowledge bases for RAG workflows.

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
