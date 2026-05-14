---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-30
completeness: full
---

# 30: Evaluation Workflow Patterns

## Scenario

A GenAI developer wants to evaluate FMs by using the automatic model evaluation feature in Amazon Bedrock. The GenAI developer creates a comprehensive custom prompt dataset that contains 5,000 curated prompts. The prompts cover various business scenarios for a text classification task. The GenAI developer uploads the dataset to Amazon S3 in JSONL format. The GenAI developer attempts to create an evaluation job. However, the evaluation job fails to start. The error indicates an issue with the dataset configuration. Which approach will resolve this issue?

## Common implementation patterns

- Split the dataset into multiple smaller datasets with a maximum of 1,000 prompts each. Run separate evaluation jobs.

## Common anti-patterns

- Avoid compress the dataset file by using gzip compression. Re-upload the dataset to Amazon S3. because file compression does not bypass the fundamental quota of 1,000 prompts for each dataset in an evaluation job. The issue is the number of prompts, not the file size. Amazon...
- Avoid convert the dataset from JSONL format to CSV format. Re-upload the dataset to Amazon S3. because amazon Bedrock model evaluation requires custom prompt datasets to be in JSONL format with the ".jsonl" file extension. Converting the dataset to CSV will not resolve the...
- Avoid enable versioning on the S3 bucket. Update the CORS configuration for console access. because cORS configuration is a requirement for console-created jobs. However, this approach addresses browser access permissions, not dataset size limitations. S3 Versioning does not...

## Architecture guidance

- Amazon Bedrock automatic model evaluation jobs have a quota of 1,000 prompts for each dataset.
- The 5,000-prompt dataset exceeds the quota and causes the job to fail.
- You can split the prompts into smaller datasets such as five datasets of 1,000 prompts each.
