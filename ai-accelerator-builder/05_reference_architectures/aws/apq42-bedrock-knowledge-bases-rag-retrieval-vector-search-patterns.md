---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-42
completeness: full
title: 42: RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon S3
  - Bedrock Knowledge Bases
related_controls:
  - retrieval_grounding
topics:
  - rag patterns
  - bedrock knowledge bases
  - bedrock
  - s3 data assets
  - knowledge bases
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
  - multimodal extraction
---

# 42: RAG Patterns

## Scenario

An aircraft repair company receives repair requests from various airlines. The company responds to the repair requests by providing an initial quote of the estimated labor hours, required spare parts, and a schedule for completion. The repair requests from airlines include a description of the defect and the aircraft model. The company uses repair manuals in PDF format to help resolve the repair requests. The repair manuals contain thousands of pages with nested and cross-referenced sections from the aircraft manufacturers. The repair manuals explain the necessary repair procedures and spare parts for the repair. The company wants to extract the repair procedures and spare parts from the repair manuals automatically by using RAG. The solution must provide high retrieval accuracy. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store repair manuals in Amazon S3 partitioned by aircraft model and part. Use Amazon Bedrock Knowledge Bases with a hierarchical chunking strategy. Use Amazon OpenSearch Serverless as a vector store.

## Architecture guidance

- Knowledge Bases is a fully managed end-to-end RAG workflow.
- Knowledge Bases integrates with OpenSearch Serverless as a vector store.
- Knowledge Bases supports Amazon S3 as a data source.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
