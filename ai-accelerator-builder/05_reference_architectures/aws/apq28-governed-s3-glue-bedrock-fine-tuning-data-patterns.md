---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-28
completeness: full
title: 28: Governed S3 and Glue Preparation for Bedrock Fine-Tuning Data
pattern_family: rag
aws_services:
  - AWS Glue
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - audit_logging
  - retrieval_grounding
topics:
  - governed s3 glue preparation
  - bedrock fine-tuning data
  - rag
  - glue data processing
  - bedrock
  - s3 data assets
  - audit logging
  - retrieval grounding
use_cases:
  - customer-facing assistant
  - model governance
  - fine tuning
---

# 28: Governed S3 and Glue Preparation for Bedrock Fine-Tuning Data

## Pattern summary

Prepare customer support transcripts for Bedrock fine-tuning by landing data in governed S3 storage, cataloging it with Glue, and applying data preparation controls.

## Scenario

A financial services company is building a chat-based AI assistant to simulate conversations with customers. The company wants to fine-tune an Amazon Bedrock FM on transcripts of real customer support chat conversations. The customer support transcripts are stored in an unstructured format. For regulatory compliance, the company must track where the fine-tuning dataset originated. The company must track how the dataset has been transformed. The company must ensure that only governed and approved data is used in the fine-tuning process. Which solution will meet these requirements with the LEAST operational effort?

## Common implementation patterns

- Create an Amazon S3 bucket with appropriate governance controls. Store the raw customer support transcripts in the bucket. Scan the bucket by using an AWS Glue crawler. Store the metadata in AWS Glue Data Catalog. Prepare the data for fine-tuning by using AWS Glue ETL jobs....

## Architecture guidance

- Amazon S3 is an object storage service that you can use to host data lakes.
- You can use an AWS Glue crawler to crawl a data source and infer the schema and metadata.
- Then, you can store the data in Data Catalog.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
