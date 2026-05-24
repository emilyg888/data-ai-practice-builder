---
type: reference_note
platform: aws
status: draft
source: udemy-question-54
title: 54: Prompt Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
related_controls:
  - access_control
  - prompt_policy
topics:
  - prompt patterns
  - bedrock agents
  - lambda orchestration
  - api gateway
  - bedrock
  - access control
  - prompt policy
use_cases:
  - routing and orchestration
---

# 54: Prompt Patterns

## Scenario

A product enablement team is building an internal web portal that helps employees draft customer emails by using an Amazon Bedrock foundation model (FM). The team wants to deliver an accessible web UI quickly, standardize backend integration for future clients by using an API-first approach, and allow non-developers to adjust the prompt workflow (including branching and reusable prompt components) without redeploying application code. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Build the web UI with AWS Amplify and use Amplify libraries for authentication. Define the backend as an Amazon API Gateway REST API created from an OpenAPI specification. Invoke an Amazon Bedrock Flow from an AWS Lambda integration behind the API so prompt...

## Architecture guidance

- The lowest-overhead solution combines a rapid front-end delivery mechanism with a standardized API contract and a managed, no-code workflow layer for prompt chaining.
- AWS Amplify accelerates building and hosting the web interface and common client capabilities.
- An OpenAPI-defined Amazon API Gateway interface provides an API-first contract that other clients can adopt consistently.

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
