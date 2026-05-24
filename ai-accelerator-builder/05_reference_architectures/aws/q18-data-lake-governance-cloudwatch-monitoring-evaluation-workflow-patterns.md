---
type: reference_note
platform: aws
status: draft
source: udemy-question-18
title: 18: Prompt Patterns
pattern_family: prompt_management
aws_services:
  - AWS Glue
  - Amazon Athena
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
related_controls:
  - audit_logging
  - model_evaluation
  - monitoring
  - prompt_policy
  - retrieval_grounding
topics:
  - prompt patterns
  - prompt management
  - glue data processing
  - amazon athena
  - bedrock
  - monitoring
  - s3 data assets
  - audit logging
  - model evaluation
  - prompt policy
  - retrieval grounding
  - evaluation
use_cases:
  - document summarization
---

# 18: Prompt Patterns

## Scenario

A media company is building a generative AI feature that summarizes long articles by using Amazon Bedrock. The team regularly runs Amazon Bedrock Model Evaluations on a fixed prompt dataset to compare two candidate FMs and track metrics such as correctness, helpfulness, and logical coherence over time. Product stakeholders want a recurring, easy-to-consume report that highlights trends and provides clear model comparison visualizations without requiring engineers to manually compile results each week. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store Bedrock model evaluation outputs in Amazon S3. Use an AWS Glue crawler to create/update table definitions in the AWS Glue Data Catalog. Query the results with Amazon Athena and publish stakeholder-facing dashboards and reports in Amazon QuickSight. This...

## Architecture guidance

- A low-operations reporting system for FM implementations typically separates storage, analytics, and visualization.
- Amazon Bedrock Model Evaluations can produce structured outputs that are easy to store in Amazon S3.
- Registering that data through the AWS Glue Data Catalog makes it straightforward to query with Amazon Athena.

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
