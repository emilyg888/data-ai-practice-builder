---
type: reference_note
platform: aws
status: draft
source: udemy-question-18
---

# 18: Prompt Patterns

## Scenario

A media company is building a generative AI feature that summarizes long articles by using Amazon Bedrock. The team regularly runs Amazon Bedrock Model Evaluations on a fixed prompt dataset to compare two candidate FMs and track metrics such as correctness, helpfulness, and logical coherence over time. Product stakeholders want a recurring, easy-to-consume report that highlights trends and provides clear model comparison visualizations without requiring engineers to manually compile results each week. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store Bedrock model evaluation outputs in Amazon S3. Use an AWS Glue crawler to create/update table definitions in the AWS Glue Data Catalog. Query the results with Amazon Athena and publish stakeholder-facing dashboards and reports in Amazon QuickSight. This...

## Common anti-patterns

- Avoid use Amazon CloudWatch Logs Insights to query Amazon Bedrock invocation logs for latency and token usage. Create Amazon CloudWatch dashboards and have engineers share exported dashboard screenshots in a weekly email. because cloudWatch dashboards are...

## Architecture guidance

- A low-operations reporting system for FM implementations typically separates storage, analytics, and visualization.
- Amazon Bedrock Model Evaluations can produce structured outputs that are easy to store in Amazon S3.
- Registering that data through the AWS Glue Data Catalog makes it straightforward to query with Amazon Athena.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
