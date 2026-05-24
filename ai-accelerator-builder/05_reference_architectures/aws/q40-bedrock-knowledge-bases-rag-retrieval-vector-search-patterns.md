---
type: reference_note
platform: aws
status: draft
source: udemy-question-40
title: 40: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon S3
  - Bedrock Knowledge Bases
related_controls:
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - s3 data assets
  - knowledge bases
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - customer-facing assistant
  - internal assistant
  - search and retrieval
  - model governance
---

# 40: Knowledge Base And RAG Patterns

## Scenario

A manufacturing company is building an internal GenAI assistant on AWS by using Amazon Bedrock and a RAG architecture. Engineering specifications are stored in a SharePoint Online document library, and design decision records are maintained in an Atlassian Confluence wiki. The customer support team maintains troubleshooting articles in Salesforce. For compliance reasons, a copy of the Salesforce articles must also be stored in Amazon S3. The company wants to integrate these sources into a single retrieval layer with the LEAST operational overhead. Which combination of actions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base and configure Confluence and SharePoint as data sources. Use an embedding model (for example, Amazon Titan embeddings) and a managed vector store integration to support semantic retrieval for the RAG application. This...
- Use Amazon AppFlow to replicate Salesforce knowledge articles into an Amazon S3 bucket on a schedule or on demand. Configure the Amazon Bedrock Knowledge Base to ingest the S3 content so the RAG application can retrieve from it. This is the managed or...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- The lowest-operations approach is to use managed integration components rather than building custom crawlers and ingestion pipelines.
- Amazon Bedrock Knowledge Bases can connect directly to enterprise knowledge sources such as Confluence and SharePoint and provide a managed path from source documents to semantic retrieval for RAG.
- For Salesforce content, Amazon AppFlow provides a managed way to replicate SaaS data into Amazon S3 to satisfy the requirement to keep an S3 copy, and the Knowledge Base can then ingest from S3 to make that content...

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
