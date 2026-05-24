---
type: reference_note
platform: aws
status: draft
source: udemy-question-13
title: 13: Throughput Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
related_controls:
  - audit_logging
topics:
  - throughput patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - audit logging
use_cases:
  - customer-facing assistant
  - model governance
  - routing and orchestration
---

# 13: Throughput Patterns

## Scenario

An online retailer is building a customer-facing chat experience that uses Amazon Bedrock LLMs. The team wants to route each user message to a low-latency model for simple requests and to a higher-quality model for complex requests. During traffic spikes, the higher-quality model occasionally experiences throttling, and the team wants requests to automatically fall back to the low-latency model when throttling or high latency is detected. The team also wants a clear audit trail of how each request was routed. Which solution will meet these requirements with the LEAST custom application logic?

## Common implementation patterns

- Implement all routing in application code inside a single AWS Lambda function. The function calls Amazon Bedrock, checks for throttling errors, retries with exponential backoff, and then calls a different model if throttling persists. Log routing decisions to...

## Architecture guidance

- A good model-routing design needs two decision points: determine the best model for the request content (simple vs complex) and determine whether operational conditions require a fallback (for example, throttling or...
- A Step Functions workflow is well-suited to this because it can orchestrate a classification step, branch to specialized model invocations, apply retries and fallback paths, and preserve an end-to-end record of...
- Client-driven routing does not satisfy automatic fallback requirements, a single Lambda-based router increases custom code and reduces structured traceability, and cross-Region inference addresses Regional capacity—not...

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
