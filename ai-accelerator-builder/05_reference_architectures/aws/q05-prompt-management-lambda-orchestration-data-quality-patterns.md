---
type: reference_note
platform: aws
status: draft
source: udemy-question-5
title: 5: Prompt Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon API Gateway
  - Amazon Bedrock
related_controls:
  - prompt_policy
topics:
  - prompt patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - api gateway
  - bedrock
  - prompt policy
use_cases:
  - document summarization
  - search and retrieval
---

# 5: Prompt Patterns

## Scenario

A fintech startup is building a GenAI feature that is used by two clients: a mobile app and an internal microservice running on Amazon ECS. For short, interactive prompts, users must receive a response immediately. For long-running requests (such as summarizing multi-page documents), the startup is willing to let users retrieve the result later. The startup also wants a single, stable API in front of the solution that validates required JSON fields before the request is processed, with the LEAST operational overhead. Which solution will meet these requirements?

## Common implementation patterns

- Create an Application Load Balancer (ALB) in front of an Amazon ECS service that validates requests and invokes the Amazon Bedrock Runtime API. For long-running requests, start an AWS Step Functions workflow that calls Bedrock and returns the final response...

## Architecture guidance

- The most flexible pattern for model interactions is to present a consistent, validated API surface to all callers while choosing synchronous or asynchronous execution based on the workload.
- API Gateway provides a stable endpoint and native request validation so malformed requests are rejected early.
- For immediate responses, a Lambda function can invoke Amazon Bedrock through the Bedrock Runtime APIs.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
