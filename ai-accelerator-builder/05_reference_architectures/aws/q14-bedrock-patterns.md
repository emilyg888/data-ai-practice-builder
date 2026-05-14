---
type: reference_note
platform: aws
status: draft
source: udemy-question-14
---

# 14: Implementation Patterns

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

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
