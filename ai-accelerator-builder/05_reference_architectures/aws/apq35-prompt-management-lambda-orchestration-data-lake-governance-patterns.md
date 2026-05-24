---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-35
completeness: full
title: 35: Audit Logging Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS CloudTrail
  - AWS Lambda
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - access_control
  - audit_logging
  - prompt_policy
topics:
  - audit logging patterns
  - bedrock agents
  - audit logging
  - lambda orchestration
  - bedrock
  - s3 data assets
  - access control
  - prompt policy
  - prompt management
use_cases:
  - document summarization
  - model governance
---

# 35: Audit Logging Patterns

## Scenario

A GenAI developer builds an application by using Amazon Bedrock. The application summarizes customer feedback from multiple media platforms. Currently, the GenAI developer stores all prompt inputs and generated summaries in Amazon S3 for auditing and analytics. Because of new copyright and compliance policies, the GenAI developer must implement the following governance mechanisms: Maintain an auditable trail for prompt data sources. Log FM usage for auditing purposes. Automatically track prompt lineage and model I/O metadata. Which solution will meet these requirements?

## Common implementation patterns

- Set up Amazon S3 server access logging for all prompt and summary objects. Enable AWS CloudTrail to record Amazon Bedrock API calls. Configure Amazon Bedrock Prompt Management to track template versions and lineage.

## Architecture guidance

- S3 server access logging provides detailed records of requests that are made to S3 buckets.
- S3 server access logging provides an auditable trail for prompt data sources.
- CloudTrail captures Amazon Bedrock API activity including model invocations for usage auditing.

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
