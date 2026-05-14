---
type: reference_note
platform: aws
status: draft
source: udemy-question-5
---

# 5: Prompt Patterns

## Scenario

A fintech startup is building a GenAI feature that is used by two clients: a mobile app and an internal microservice running on Amazon ECS. For short, interactive prompts, users must receive a response immediately. For long-running requests (such as summarizing multi-page documents), the startup is willing to let users retrieve the result later. The startup also wants a single, stable API in front of the solution that validates required JSON fields before the request is processed, with the LEAST operational overhead. Which solution will meet these requirements?

## Common implementation patterns

- Create an Application Load Balancer (ALB) in front of an Amazon ECS service that validates requests and invokes the Amazon Bedrock Runtime API. For long-running requests, start an AWS Step Functions workflow that calls Bedrock and returns the final response...

## Common anti-patterns

- Avoid store prompt templates and model IDs in AWS AppConfig. Have the mobile app and the ECS service read the configuration at startup and then invoke the Amazon Bedrock Runtime API directly. Use Amazon SNS to trigger multiple Lambda functions to summarize...

## Architecture guidance

- The most flexible pattern for model interactions is to present a consistent, validated API surface to all callers while choosing synchronous or asynchronous execution based on the workload.
- API Gateway provides a stable endpoint and native request validation so malformed requests are rejected early.
- For immediate responses, a Lambda function can invoke Amazon Bedrock through the Bedrock Runtime APIs.

## Domain

- Content Domain 2: Implementation and Integration
