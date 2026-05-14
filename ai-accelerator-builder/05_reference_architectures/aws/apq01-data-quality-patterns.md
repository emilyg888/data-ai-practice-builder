---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-1
completeness: full
---

# 1: Data Quality Patterns

## Scenario

A company is implementing a data pipeline to feed customer transaction data into Amazon Bedrock FMs. The company wants to generate personalized recommendations for customers. A GenAI developer wants to avoid data quality issues that could affect model output accuracy. The GenAI developer wants to implement automated data validation before the FMs use the data. The company stores the data in Amazon S3 and catalogs the data in AWS Glue Data Catalog. The solution must detect anomalies and filter out low-quality data before the data reaches the FMs. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Use AWS Glue Data Quality for the data catalog with rule-based validation and anomaly detection. Create an Amazon EventBridge rule to send alerts when quality scores fall below defined thresholds.
- Implement AWS Glue Data Quality for ETL jobs with Data Quality Definition Language (DQDL) rules that validate the data during processing. Configure the job to filter out records that fail validation before passing the data to Amazon Bedrock.

## Common anti-patterns

- Avoid use Amazon SageMaker Data Wrangler to profile the data. Use SageMaker Model Monitor to detect data drift. Implement custom pre-processing logic in SageMaker processing jobs. because data Wrangler and Model Monitor primarily focus on model development and monitoring, not...
- Avoid create an AWS Step Functions workflow to orchestrate serverless validation. Create AWS Lambda functions that run validation checks on the data and store validation results in Amazon DynamoDB. because a custom validation solution that uses Step Functions and Lambda...
- Avoid use Amazon Athena to run SQL queries that validate data constraints. Create an Amazon EventBridge rule that invokes an AWS Lambda function to query the results and generate quality metrics. because athena can run SQL queries for validation. However, you must write and...

## Architecture guidance

- Data Quality provides both rule-based validation and ML-powered anomaly detection capabilities.
- Data Quality can evaluate data quality against custom rules that are written in DQDL.
- Data Quality can detect anomalies by analyzing data statistics over time.
