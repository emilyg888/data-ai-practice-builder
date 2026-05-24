---
type: reference_note
platform: aws
status: draft
source: udemy-question-44
title: 44: Model Card and Data Lineage Evidence for Lending Explanations
pattern_family: sagemaker
aws_services:
  - AWS Glue
  - Amazon SageMaker
related_controls:
  - audit_logging
  - evidence_retention
topics:
  - model card data lineage evidence
  - lending explanations
  - sagemaker
  - glue data processing
  - audit logging
  - evidence retention
use_cases:
  - customer-facing assistant
  - model governance
  - routing and orchestration
---

# 44: Model Card and Data Lineage Evidence for Lending Explanations

## Pattern summary

Use SageMaker model cards, Glue metadata, and tagging to prove which model version and approved data sources produced each lending explanation.

## Scenario

A regulated digital bank is launching a GenAI feature that uses an FM to generate customer-facing explanations for lending decisions. During audits, the bank must demonstrate which model version produced each explanation, which approved data sources were used to generate the response, and provide an immutable record of the decision workflow for later review. The team wants to meet these compliance requirements with the LEAST operational overhead. Which solution should the team implement?

## Common implementation patterns

- Create programmatic model cards in Amazon SageMaker AI for each approved model version and deployment. Use AWS Glue Data Catalog and metadata tagging to register and attribute approved data sources and transformations for lineage. Configure the application to...

## Architecture guidance

- A practical compliance framework for FM deployments usually needs three complementary capabilities: standardized model documentation, traceability of data sources and transformations, and durable decision logs for audit...
- Programmatic model cards provide an auditable record of model purpose and versioned deployment context.
- A data catalog with metadata tagging and lineage allows the organization to prove which governed data sources were used (and how they were processed) in support of outputs.

## AWS documentation validation

- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
