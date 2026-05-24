---
type: reference_note
platform: aws
status: draft
source: udemy-question-64
title: 64: Throughput Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon CloudWatch
related_controls:
  - monitoring
  - pii_protection
topics:
  - throughput patterns
  - bedrock agents
  - lambda orchestration
  - api gateway
  - bedrock
  - monitoring
  - pii protection
use_cases:
  - customer-facing assistant
  - cost optimization
---

# 64: Throughput Patterns

## Scenario

A digital banking team is building a customer-facing chat assistant that uses an Amazon Bedrock text model through AWS Lambda and Amazon API Gateway. Users frequently abandon sessions when they do not see any output quickly, but the team wants to avoid the added cost of provisioning dedicated capacity because traffic is bursty. The team needs the chat UI to start displaying the model’s answer as soon as possible while still allowing the backend team to benchmark latency improvements. Which solution will provide the LOWEST perceived latency for end users with minimal additional cost?

## Common implementation patterns

- Update the application to use Amazon Bedrock streaming responses and stream tokens to the client (for example, by using API Gateway WebSockets or server-sent events). Enable Amazon Bedrock latency-optimized inference for the model and use Amazon CloudWatch...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- For interactive chat experiences, the key user-perceived metric is how quickly the application can start showing a response.
- Streaming responses from Amazon Bedrock let the client render output incrementally instead of waiting for the full completion, which significantly improves perceived responsiveness without requiring dedicated capacity.
- Enabling latency-optimized inference targets faster responsiveness (such as improved time to first token) for time-sensitive interactions, and CloudWatch metrics provide a way to benchmark improvements.

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

- Content Domain 4: Operational Efficiency and Optimization fo
