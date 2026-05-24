---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-20
completeness: full
title: 20: Audit Logging Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - access_control
  - audit_logging
  - evidence_retention
  - prompt_policy
topics:
  - audit logging patterns
  - bedrock agents
  - iam access control
  - lambda orchestration
  - bedrock
  - s3 data assets
  - access control
  - audit logging
  - evidence retention
  - prompt policy
  - prompt management
use_cases:
  - customer-facing assistant
  - model governance
  - routing and orchestration
---

# 20: Audit Logging Patterns

## Scenario

A financial services company needs to use Amazon Bedrock to create an AI assistant that will help customer support representatives across multiple business units. A GenAI developer must ensure that prompt templates are properly governed through approval workflows. Additionally, the company requires comprehensive logging of all model invocations with a 7-year retention period for regulatory compliance. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Use Amazon Bedrock Prompt Management with multi-stage approval workflows. Use IAM policies that require multi-party authorization.
- Enable Amazon Bedrock model invocation logging with Amazon S3 as the destination. Enable S3 Object Lock with compliance retention mode set to 7 years. Create separate prefixes for each business unit...

## Architecture guidance

- You can use Amazon Bedrock Prompt Management to securely create, parameterize, version, and approve prompt templates within the Amazon Bedrock managed environment.
- This solution provides multi-stage approvals, access roles, version control, and collaboration features that are suitable for diverse business units and complex governance requirements.
- Learn more about Amazon Bedrock Prompt Management.

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
