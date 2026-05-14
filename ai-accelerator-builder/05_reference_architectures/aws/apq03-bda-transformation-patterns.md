---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-3
completeness: partial
---

# 3: BDA Transformation Patterns

## Scenario

A company is deploying a customer service AI assistant. The assistant uses Amazon API Gateway to invoke an AWS Lambda function. The function calls the Amazon Bedrock API to generate responses. A development team performs load testing that simulates peak business hours. The development team observes occasional latency spikes and intermittent ThrottlingException errors from the Amazon Bedrock API. The development team must improve system reliability to handle the load-based errors. The development team must preserve the assistant's real-time responsiveness. Which solution will meet these requirements?

## Common implementation patterns

- Configure exponential backoff with jitter in the AWS SDK used by the Lambda function. Configure per-client throttling limits in API Gateway.

## Common anti-patterns

- Avoid create an Amazon SQS queue that decouples API Gateway from the Lambda function. because you can use Amazon SQS to create resilient decoupled systems. However, this solution changes the architecture from synchronous to asynchronous. For a real-time customer service AI...
- Avoid create an AWS Step Functions workflow that manages synchronous retries with a fixed-interval strategy. because a fixed-interval retry strategy is not an effective way to resolve ThrottlingException errors. A fixed-interval retry strategy can contribute to a thundering herd...

## Architecture guidance

- Configuring exponential backoff with jitter in the AWS SDK is the recommended client-side pattern to handle transient errors such as ThrottlingException.
- Exponential backoff with jitter avoids overwhelming the API with retries.
- Configuring throttling limits in API Gateway is a server-side protection mechanism that manages request bursts from clients.
