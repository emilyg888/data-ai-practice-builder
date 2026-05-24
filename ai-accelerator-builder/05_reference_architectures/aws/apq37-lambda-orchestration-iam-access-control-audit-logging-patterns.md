---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-37
completeness: full
title: 37: Audit Logging Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - access_control
  - audit_logging
topics:
  - audit logging patterns
  - bedrock agents
  - iam access control
  - lambda orchestration
  - bedrock
  - access control
  - audit logging
use_cases:
  - model governance
---

# 37: Audit Logging Patterns

## Scenario

A large company is using Amazon Bedrock. The company wants to limit access to FMs to specific AWS and Anthropic models within designated development accounts. The company strictly prohibits third-party marketplace models. The company requires comprehensive logging of all model interactions for auditing purposes. The company uses AWS Organizations and AWS IAM Identity Center for account and user management. A security team must implement the solution while maintaining operational efficiency. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Create an SCP that denies bedrock:InvokeModel\* actions for unapproved or marketplace models by using the bedrock:ModelID condition key. Apply the policy to the root of the organization. Enable Amazon Bedrock model invocation logging.
- Create a permission set in IAM Identity Center that allows bedrock:InvokeModel\* actions only for specific AWS and Anthropic model ARNs by using IAM policy conditions. Apply the permission set to designated development accounts.

## Architecture guidance

- SCPs provide organization-wide preventive controls.
- SCPs can effectively deny access to marketplace models across all accounts.
- You can scope bedrock:InvokeModel\* actions to only approved AWS and Anthropic model IDs.

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
