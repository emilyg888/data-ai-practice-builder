---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-28
completeness: full
---

# 28: Implementation Patterns

## Scenario

A financial services company is building a chat-based AI assistant to simulate conversations with customers. The company wants to fine-tune an Amazon Bedrock FM on transcripts of real customer support chat conversations. The customer support transcripts are stored in an unstructured format. For regulatory compliance, the company must track where the fine-tuning dataset originated. The company must track how the dataset has been transformed. The company must ensure that only governed and approved data is used in the fine-tuning process. Which solution will meet these requirements with the LEAST operational effort?

## Common implementation patterns

- Create an Amazon S3 bucket with appropriate governance controls. Store the raw customer support transcripts in the bucket. Scan the bucket by using an AWS Glue crawler. Store the metadata in AWS Glue Data Catalog. Prepare the data for fine-tuning by using AWS Glue ETL jobs....

## Common anti-patterns

- Avoid create an Amazon S3 bucket with appropriate governance controls. Store the raw customer support transcripts in the bucket. Scan the S3 bucket by using an AWS Glue crawler. Store the metadata in AWS Glue Data Catalog. Prepare the data for fine-tuning by using Amazon EMR...
- Avoid create an Amazon S3 bucket with appropriate governance controls. Store the raw customer support transcripts in the bucket. Use Amazon Athena to run SQL queries on the raw data and prepare the data for fine-tuning. Use Athena to export the curated results back in the...
- Avoid store the raw customer support transcripts in an Amazon S3 bucket and reference the transcripts directly in the Amazon Bedrock fine-tuning job. because amazon S3 is an object storage service that you can use to host data lakes. Amazon Bedrock is a fully managed service...

## Architecture guidance

- Amazon S3 is an object storage service that you can use to host data lakes.
- You can use an AWS Glue crawler to crawl a data source and infer the schema and metadata.
- Then, you can store the data in Data Catalog.
