---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-3
completeness: partial
title: 3: BDA Transformation Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
related_controls:
topics:
  - bda transformation patterns
  - bedrock agents
  - lambda orchestration
  - api gateway
  - bedrock
use_cases:
  - customer-facing assistant
  - real-time streaming
---

# 3: BDA Transformation Patterns

## Scenario

A company is deploying a customer service AI assistant. The assistant uses Amazon API Gateway to invoke an AWS Lambda function. The function calls the Amazon Bedrock API to generate responses. A development team performs load testing that simulates peak business hours. The development team observes occasional latency spikes and intermittent ThrottlingException errors from the Amazon Bedrock API. The development team must improve system reliability to handle the load-based errors. The development team must preserve the assistant's real-time responsiveness. Which solution will meet these requirements?

## Common implementation patterns

- Configure exponential backoff with jitter in the AWS SDK used by the Lambda function. Configure per-client throttling limits in API Gateway.

## Architecture guidance

- Configuring exponential backoff with jitter in the AWS SDK is the recommended client-side pattern to handle transient errors such as ThrottlingException.
- Exponential backoff with jitter avoids overwhelming the API with retries.
- Configuring throttling limits in API Gateway is a server-side protection mechanism that manages request bursts from clients.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
