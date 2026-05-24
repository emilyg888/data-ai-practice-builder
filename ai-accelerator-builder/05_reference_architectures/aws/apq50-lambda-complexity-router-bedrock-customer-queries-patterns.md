---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-50
completeness: full
title: 50: Lambda-Based Complexity Router for Bedrock Customer Queries
pattern_family: lambda_orchestration
aws_services:
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - prompt_policy
topics:
  - lambda-based complexity router
  - bedrock customer queries
  - lambda orchestration
  - bedrock
  - prompt policy
use_cases:
  - customer-facing assistant
  - routing and orchestration
---

# 50: Lambda-Based Complexity Router for Bedrock Customer Queries

## Pattern summary

Use a lightweight Bedrock model behind Lambda to classify query complexity and route only hard requests to a more capable model.

## Scenario

A startup company is building a general-purpose generative AI (GenAI) assistant to handle customer questions for a variety of use cases. The company builds the GenAI assistant by using Amazon Bedrock FMs. The company wants to implement a query-routing mechanism based on the complexity of the query. Simple queries should route to a small Meta Llama model. Complex queries should route to a large Anthropic Claude model. For example, complex queries require generating creative responses or in-depth explanations. The solution must be scalable and able to maintain low-latency responses. Which solution will meet these requirements?

## Common implementation patterns

- Use an AWS Lambda function to invoke a small Amazon Bedrock model by using the query. In the system prompt, instruct the model to determine if the query is complex and reply only if the query is too complex. When the model response returns to the Lambda function, inspect the...

## Architecture guidance

- Model cascading through sequential model invocation provides an efficient way to handle query complexity.
- First, you can use a small model to determine complexity and then invoke the larger model only when necessary.
- This solution optimizes both cost and performance.

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
