---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-16
completeness: full
---

# 16: Implementation Patterns

## Scenario

A company runs a question-answering application. The application uses an Amazon Bedrock knowledge base that ingests documents from multiple Amazon S3 buckets. The company needs to monitor the data ingestion process to identify and troubleshoot any issues with document processing. Which solution will meet these requirements to monitor knowledge base operations?

## Common implementation patterns

- Configure knowledge base logging with Amazon CloudWatch Logs as the destination. Use CloudWatch Logs Insights to query for failed document processing.

## Common anti-patterns

- Avoid enable Amazon CloudWatch Application Signals to automatically detect and alert on knowledge base performance issues. because cloudWatch Application Signals is designed to monitor the performance and health of applications, not knowledge bases. CloudWatch Application Signals does not integrate...
- Avoid enable AWS CloudTrail to track all API calls that relate to knowledge base operations and document ingestion activities. because cloudTrail can track API calls that are made to Amazon Bedrock. However, CloudTrail does not provide the detailed document-level processing information that you...
- Avoid implement Amazon Bedrock model invocation logging to capture detailed metrics about document processing and embedding generation. because amazon Bedrock model invocation logging captures information about model API calls and inference requests. Model invocation logging does not capture...

## Architecture guidance

- Amazon Bedrock knowledge bases support a built-in logging system that you can configure to send logs to CloudWatch Logs.
- The logs track the status of files during data ingestion jobs.
- The jobs show whether the files were successfully ingested, ignored, or failed.
