---
type: reference_note
platform: aws
status: draft
source: udemy-question-14
title: 14: Glue Data Quality Gate for Bedrock Batch Summarization Inputs
pattern_family: evaluation_monitoring
aws_services:
  - AWS Glue
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
related_controls:
  - model_evaluation
  - monitoring
topics:
  - glue data quality gate
  - bedrock batch summarization inputs
  - evaluation monitoring
  - glue data processing
  - bedrock
  - monitoring
  - s3 data assets
  - model evaluation
  - evaluation
  - data quality
use_cases:
  - document summarization
  - routing and orchestration
---

# 14: Glue Data Quality Gate for Bedrock Batch Summarization Inputs

## Pattern summary

Use a Glue ETL job and DQDL rules to validate nightly JSON transcript batches before they are summarized by Bedrock.

## Scenario

A financial services analytics team is building a document-summarization workflow by using an Amazon Bedrock text model. Each night, a new batch of customer interaction transcripts is delivered as JSON files to an Amazon S3 bucket. Some files are missing required fields (for example, transcriptText), and some contain empty strings that cause poor model responses. The team needs an automated validation workflow that can enforce data quality rules before the transcripts are sent for FM inference and that can publish pass/fail results as operational metrics for monitoring. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an AWS Glue ETL job that reads the JSON files from Amazon S3 and evaluates an AWS Glue Data Quality ruleset (DQDL) for required fields and non-empty values. Configure the job to fail when the ruleset fails, write failed records to a quarantine S3...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- The most operationally efficient approach is to implement validation where the batch data is already being processed and to use managed, rule-based checks.
- AWS Glue Data Quality can evaluate explicit rules (such as required keys and non-empty values) as part of an AWS Glue job, and it can be configured to fail processing when quality thresholds are not met so that invalid...
- Publishing the evaluation results to Amazon CloudWatch metrics enables dashboards and alarms without building a separate reporting system.

## AWS documentation validation

- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
