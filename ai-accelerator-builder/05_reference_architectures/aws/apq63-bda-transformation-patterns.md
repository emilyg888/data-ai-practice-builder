---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-63
completeness: full
---

# 63: BDA Transformation Patterns

## Scenario

A medical company that operates multiple clinics runs a generative AI (GenAI) application on AWS. The application uses AWS Step Functions to orchestrate two AWS Lambda functions. One function calls Amazon Transcribe Medical to transcribe clinic audio data. The second function uses the Amazon Nova Pro model in Amazon Bedrock to summarize the data. The company is onboarding additional clinics. Each clinic has a unique clinic ID. A GenAI developer must modify the architecture to store each clinic's data in a shared Amazon S3 bucket. The GenAI developer must use the clinic ID as the key prefix. The solution must track summarization costs for each clinic. Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO.)

## Common implementation patterns

- Create an Amazon Bedrock inference profile for each clinic ID. Modify the summarization Lambda function to use the profiles based on the S3 key prefix from the uploaded data.
- Create an Amazon EventBridge rule to capture PutObject events. Set the Step Functions state machine as the destination when a matching event occurs on the event bus.

## Common anti-patterns

- Avoid configure the S3 bucket to use Amazon S3 Event Notifications to capture PutObject events. Create a Lambda function. Set the function as the destination for the S3 notifications. Configure the function to invoke the Step Functions workflow when new data uploads. because s3...
- Avoid enable S3 Storage Lens for the bucket to collect prefix-level usage metrics for each clinic. Use Amazon Athena to query the metrics, calculate summarization costs, and generate clinic reports. because s3 Storage Lens provides metrics on storage usage. For example, the...
- Avoid deploy an Amazon SageMaker AI endpoint for each clinic that is tagged with the clinic ID. Route summarization Lambda requests to each endpoint based on the S3 key prefix from the uploaded data. because amazon Bedrock is a serverless service that provides pay-as-you-go...

## Architecture guidance

- Amazon Bedrock application inference profiles are specifically designed to manage and track FM costs in multi-tenant environments.
- This step efficiently handles cost attribution.
- The summarization Lambda can select the appropriate profile based on the clinic ID from the S3 key prefix.
