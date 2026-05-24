---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-11
completeness: full
title: 11: Data Source Metadata Tagging for Bedrock Practice Question Review
pattern_family: data_provenance_metadata_tagging
aws_services:
  - AWS Glue
  - Amazon Bedrock
related_controls:
  - access_control
  - audit_logging
topics:
  - data source metadata tagging
  - bedrock practice question review
  - glue data processing
  - bedrock
  - access control
  - audit logging
  - data provenance metadata tagging
use_cases:
  - architecture reference
---

# 11: Data Source Metadata Tagging for Bedrock Practice Question Review

## Pattern summary

Tag generated outputs with source metadata and register curated and scraped datasets in Glue so reviewers can trace practice question provenance.

## Scenario

An education company built a content generation system on Amazon Bedrock. The system generates practice questions to quiz end users on a topic to test their knowledge. The system consumes a mix of curated data and scraped data in the topic domain. Reviewers must approve of the generated question-response sets before end users can access the sets. The company wants to improve the system by adding source lineage for the reviewers to verify the credibility of the content. Which combination of steps will meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Tag FM outputs with metadata from the data source.
- Register the curated and scraped input datasets with AWS Glue Data Catalog.

## Architecture guidance

- You can tag the outputs with metadata about the data sources.
- The generated questions are the outputs.
- The curated data and scraped data are the data sources.

## AWS documentation validation

- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
