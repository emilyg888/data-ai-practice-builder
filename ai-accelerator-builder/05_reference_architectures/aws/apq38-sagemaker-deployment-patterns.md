---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-38
completeness: full
---

# 38: SageMaker Deployment Patterns

## Scenario

A financial services company is using Amazon SageMaker AI training jobs to fine-tune a custom FM. The company uses the FM for various sensitive use cases including fraud detection, analytics, and document analysis. The fine-tuning jobs invoke automatically when a user uploads new datasets in designated Amazon S3 buckets. The company must implement responsible AI practices to ensure compliance with industry regulations. A GenAI developer must ensure that all FM training datasets for new model releases are encrypted at rest by using AWS KMS customer managed keys. Datasets in buckets that use default AWS managed keys or that are not encrypted must be rejected and not used for model fine-tuning. The GenAI developer must validate that all existing S3 buckets comply with AI best practices for customer managed key encryption. Which solution will meet these requirements?

## Common implementation patterns

- Create an AWS Config custom rule using the AWS rule development kit (RDK). Set up the custom rule to check the existing S3 buckets for FM training data. Configure the rule to determine if the buckets use server-side encryption with AWS KMS (SSE-KMS) and a customer managed key....

## Common anti-patterns

- Avoid use Amazon Macie to scan all training datasets in S3 buckets and flag unencrypted dataset objects. Generate reports on any objects that are not encrypted with customer managed keys. Mark all buckets that Macie flags as noncompliant. because you can use Macie to retrieve...
- Avoid create an AWS Lambda function that runs on an Amazon EventBridge schedule. Configure the function to run periodic Amazon Athena queries. Run the queries on AWS CloudTrail logs. Configure the queries to identify PutObject events on S3 buckets that do not have an...
- Avoid create Amazon EventBridge rules for PutObject events for dataset S3 buckets. Set up an AWS Step Functions workflow. Configure one state to run an AWS Lambda function that parses events and verifies customer managed key encryption. Configure a Choice state that evaluates...

## Architecture guidance

- This solution uses compliance-as-code to set continuous automation checks through AWS Config.
- AWS Config supports many automatic remediation options, including AWS Systems Manager Session Manager.
- This solution checks and enforces the use of customer managed keys.
