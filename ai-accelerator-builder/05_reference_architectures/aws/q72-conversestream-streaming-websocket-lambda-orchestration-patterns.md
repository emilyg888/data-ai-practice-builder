---
type: reference_note
platform: aws
status: draft
source: udemy-question-72
title: 72: Streaming Bedrock Chat Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - audit_logging
  - prompt_policy
topics:
  - streaming bedrock chat patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - api gateway
  - bedrock
  - state store
  - audit logging
  - prompt policy
  - data quality
use_cases:
  - real-time streaming
---

# 72: Streaming Bedrock Chat Patterns

## Scenario

A real-time customer-service assistant must stream model output to a browser UI, enforce prompt token budgets before invocation, and retry transient model timeouts without forcing the browser to poll.

## Common implementation patterns

- Use Amazon API Gateway WebSocket APIs when the browser needs server-pushed Bedrock output chunks with low latency.
- Put AWS Lambda in the request path to centralize token validation, Bedrock invocation, and retry policy.
- Call the Amazon Bedrock `CountTokens` API before inference when the design requires enforceable prompt-budget checks.
- Use `ConverseStream` or `InvokeModelWithResponseStream` for chunked Bedrock output instead of building a polling workaround.
- Implement bounded exponential-backoff retries in Lambda for transient Bedrock timeout conditions.
- Keep connection state, request metadata, and retry context minimal so the streaming path stays operationally simple.

## Common anti-patterns

- Using string length as a proxy for token count.
- Adding Step Functions and DynamoDB polling for a simple request-response streaming workflow.
- Pushing partial responses into a datastore and forcing the browser to poll every second.
- Assuming API Gateway mapping templates can enforce model token budgets.
- Treating API throttling as a substitute for application-level retry logic.
- Moving token-count logic to CloudFront or Lambda@Edge when the main need is Bedrock-aware validation and retry control.

## Architecture guidance

- Prefer a thin edge and a smart orchestration function for interactive GenAI chat.
- Separate three concerns explicitly: connection management, token-budget enforcement, and Bedrock retry behavior.
- Log token-count checks, retry counts, and stream-abort reasons so operational issues can be diagnosed quickly.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
