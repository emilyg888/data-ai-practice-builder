---
type: reference_note
platform: aws
status: draft
source: udemy-question-17
title: 17: Step Functions ReAct Loop for Bedrock Billing Assistance
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - audit_logging
topics:
  - step functions react loop
  - bedrock billing assistance
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - state store
  - audit logging
use_cases:
  - internal assistant
  - model governance
  - routing and orchestration
---

# 17: Step Functions ReAct Loop for Bedrock Billing Assistance

## Pattern summary

Use Step Functions to alternate Bedrock reasoning steps with Lambda actions for billing explanation, recalculation, and response drafting.

## Scenario

A financial services engineering team is building an internal assistant that uses Amazon Bedrock to handle complex billing questions (for example, “Explain why I was charged a late fee, recalculate it based on these dates, and draft a customer response”). The assistant must break each request into structured reasoning steps and take actions by calling tools such as AWS Lambda functions that query Amazon DynamoDB. The team also needs a complete, auditable execution history with built-in retries and timeout controls, and wants to minimize custom orchestration code. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement an AWS Step Functions state machine that alternates between an Amazon Bedrock InvokeModel task to decide the next step (reasoning) and Lambda tasks to perform the selected action (acting). Use Choice states for branching and termination conditions,...

## Architecture guidance

- To give an FM the ability to break down a complex problem into structured steps, the architecture needs an explicit control plane that can repeatedly: (1) ask the model what to do next, (2) execute the chosen action...
- AWS Step Functions is designed for this kind of orchestration and can implement ReAct-style patterns by combining Bedrock model invocations with tool invocations, conditional branching, and termination logic.
- It also provides managed retries, timeout controls, and a full execution history that supports auditing.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
