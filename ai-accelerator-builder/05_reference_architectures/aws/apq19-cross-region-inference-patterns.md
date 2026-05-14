---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-19
completeness: full
---

# 19: Cross-Region Inference Patterns

## Scenario

A company is building a generative AI (GenAI) powered application that uses Amazon API Gateway, AWS Lambda, and Amazon Bedrock. The application must support summarization, classification, and translation tasks. A separate FM performs each task. A GenAI developer must configure the application to meet the following requirements: Route inference requests to different FMs dynamically based on task type and customer configuration. Update routing logic at runtime without redeploying the application. Implement automatic failover to an alternate model or AWS Region if the primary model or Region is unavailable. Maintain low latency, resilience, and cross-Region support for multiple providers. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create a Lambda function that retrieves model routing rules from an AWS AppConfig hosted configuration profile at runtime. Use an AWS Step Functions state machine with branching paths for each task type and a circuit breaker pattern for failover. Invoke Amazon Bedrock by using...

## Common anti-patterns

- Avoid embed a hardcoded task type-to-model mapping dictionary in a Lambda function. Call Amazon Bedrock InvokeModel synchronously from the Lambda function. Use a try/catch block to retry with an alternate model or Region if the primary model or Region is unavailable. Deploy...
- Avoid deploy a Flask-based model router in Amazon ECS with routing metadata stored in Amazon Aurora. Route inference requests from API Gateway to the router. Configure the router to select and invoke the appropriate model by using the Amazon Bedrock SDK. Set up Amazon CloudWatch...
- Avoid configure API Gateway request mappings to send each task type to a dedicated Lambda function with a fixed model and Region configuration. Use AWS Step Functions for fallback processing if the Lambda invocation fails. Implement fallback logic in separate state machines....

## Architecture guidance

- An AWS AppConfig hosted configuration is a managed way to provide dynamic application configuration updates without redeployment.
- Step Functions is a serverless workflow service that orchestrates multiple AWS services by using state machines with built-in error handling.
- AWS AppConfig provides runtime routing updates.
