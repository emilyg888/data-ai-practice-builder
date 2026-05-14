---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-16
completeness: full
---

# 16: Streaming Patterns

## Scenario

A company that provides help desk software uses Amazon Bedrock to automate customer support ticket triage. Following AWS best practices, the system uses a well-structured prompt template that includes defined categories, examples, and validation requirements. The architecture consists of the following elements: Amazon API Gateway for ticket ingestion An AWS Lambda function for ticket processing and model interaction An Amazon Bedrock InvokeModel API for classification Response validation before downstream processing The company notices intermittent issues where some tickets receive unexpected classifications. The company needs to identify the root cause of these anomalies. Which approach will meet these requirements?

## Common implementation patterns

- Enable Amazon Bedrock model invocation logging to inspect the raw prompts being sent and the responses received from the FM.

## Common anti-patterns

- Avoid use Amazon CloudWatch Logs Insights to analyze Lambda function logs for error patterns in ticket processing and model responses. because cloudWatch Logs Insights is a query tool that you can use to search and analyze log data that is stored in CloudWatch Logs. You can use...
- Avoid use AWS X-Ray traces to identify if there are timeout or throttling issues between the Lambda function and the Amazon Bedrock API calls. because x-Ray is a distributed tracing service that helps analyze and debug application performance and service interactions. X-Ray...
- Avoid create a custom Amazon CloudWatch metric that tracks the distribution of classified categories. Set up an alarm for unexpected spikes in specific labels or null values. because cloudWatch metrics are data points that provide information about the performance of systems and...

## Architecture guidance

- Model invocation logging provides detailed logs of model interactions, including prompt content and responses.
- You can use this approach for direct analysis of cases where unexpected classifications occur.
- This approach helps identify patterns or specific conditions that led to anomalies despite the well-structured prompts and validation.
