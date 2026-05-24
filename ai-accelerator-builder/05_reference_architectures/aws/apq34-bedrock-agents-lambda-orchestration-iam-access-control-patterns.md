---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-34
completeness: full
title: 34: AgentCore Runtime Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon Bedrock
  - Amazon Bedrock AgentCore Runtime
related_controls:
  - access_control
topics:
  - agentcore runtime patterns
  - bedrock agents
  - iam access control
  - lambda orchestration
  - bedrock
  - access control
use_cases:
  - architecture reference
---

# 34: AgentCore Runtime Patterns

## Scenario

z34/75 Question A company is developing an AI agent by using Amazon Bedrock AgentCore Runtime. The agent needs to authenticate users from an existing Microsoft Entra ID environment. Users must access the agent securely by using corporate credentials. The company wants to implement OpenID Connect (OIDC) integration. The OIDC integration must validate tokens from the company's identity provider (IdP) and allow access only to users with valid corporate credentials. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure AgentCore Identity with Microsoft as an inbound provider. Set the allowed audiences to the application ID from Microsoft Entra ID.

## Architecture guidance

- AgentCore Identity supports Microsoft Entra ID as an inbound IdP for OIDC authentication.
- For setup, you must configure the discovery URL to the Microsoft v2.0 OIDC metadata endpoint.
- Then, you set the allowed audiences to match the application ID from the Microsoft Entra ID application registration.

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
