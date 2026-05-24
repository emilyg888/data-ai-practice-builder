---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-53
completeness: full
title: 53: WebSocket Streaming for Multi-Step Bedrock Customer Support
pattern_family: lambda_orchestration
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
related_controls:
topics:
  - websocket streaming
  - multi-step bedrock customer support
  - lambda orchestration
  - api gateway
  - bedrock
use_cases:
  - customer-facing assistant
  - real-time streaming
---

# 53: WebSocket Streaming for Multi-Step Bedrock Customer Support

## Pattern summary

Use API Gateway WebSockets, Lambda, and Bedrock response streaming to return partial analysis while complex support inquiries are processed.

## Scenario

A company is developing a customer support AI assistant by using Amazon Bedrock FMs. The AI assistant needs to process complex customer inquiries that require detailed analysis and multiple steps to resolve. Currently, users wait for the complete analysis before seeing any response. The delay negatively impacts user satisfaction. The company wants to optimize the user experience by showing progressive responses while performing the analysis. Which solution will meet these requirements with the LEAST development effort?

## Common implementation patterns

- Create an Amazon API Gateway WebSocket API with AWS Lambda integration. Use the Amazon Bedrock InvokeModelWithResponseStream API to stream tokens to connected clients. Configure a Lambda function to handle WebSocket connections and message delivery.

## Architecture guidance

- API Gateway WebSocket APIs provide managed, bidirectional communication channels that are suitable to stream data.
- The InvokeModelWithResponseStream API provides token-by-token streaming of model responses.
- Lambda functions can efficiently process the streams and forward tokens through WebSocket connections to clients.

## AWS documentation validation

- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
