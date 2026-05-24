---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-18
completeness: full
title: 18: API Gateway Model Routing for Multilingual News Summarization
pattern_family: lambda_orchestration
aws_services:
  - Amazon API Gateway
  - Amazon Bedrock
related_controls:
topics:
  - api gateway model routing
  - multilingual news summarization
  - lambda orchestration
  - api gateway
  - bedrock
use_cases:
  - document summarization
  - model governance
  - cost optimization
  - routing and orchestration
---

# 18: API Gateway Model Routing for Multilingual News Summarization

## Pattern summary

Use API Gateway non-proxy integrations and mapping templates to route summarization requests to different model providers based on language, content type, or compliance rules.

## Scenario

A digital content company is building a generative AI (GenAI) application that summarizes news articles. The application needs to route requests to different LLMs based on language and content types. For regulatory compliance, certain content types must use specific model providers. A GenAI developer must create a solution that can switch between model providers without code changes. The model providers include Amazon Bedrock and third-party APIs. The solution must securely store API keys and maintain consistent response formatting regardless of the underlying model. The solution must optimize costs by using cached responses when appropriate. Which solution will meet these requirements?

## Common implementation patterns

- Create a single Amazon API Gateway REST API with non-proxy integrations. Configure mapping templates to transform requests and responses for each model provider. Use header-based routing that directs traffic to store endpoint URLs based on content type and stage variables. Use...

## Architecture guidance

- API Gateway non-proxy integrations with mapping templates provide request and response transformation without code changes.
- You can combine header-based routing with stage variables for dynamic provider selection.
- Mapping templates ensure consistent response formatting across different providers.

## AWS documentation validation

- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
