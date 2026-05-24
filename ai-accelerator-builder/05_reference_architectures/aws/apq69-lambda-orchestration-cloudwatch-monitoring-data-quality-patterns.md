---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-69
completeness: full
title: 69: Data Quality Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon Comprehend
related_controls:
  - audit_logging
topics:
  - data quality patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - monitoring
  - audit logging
  - data quality
use_cases:
  - architecture reference
---

# 69: Data Quality Patterns

## Scenario

A retail company needs to process product catalog data from multiple sources to enhance an AI-powered recommendation system. The data includes product descriptions, specifications, and customer reviews in various formats and languages. The system must improve data quality and ensure consistent inputs for the company's FMs. Which solution will meet these requirements?

## Common implementation patterns

- Extract product attributes by using Amazon Comprehend entity recognition through an AWS Lambda function. Normalize product categories and specifications. Use Amazon Bedrock to reformat product descriptions for optimal FM processing.

## Architecture guidance

- Lambda is a serverless compute service that you can use for data processing tasks.
- Amazon Comprehend has entity recognition capabilities that extract structured information from text and help standardize product attributes.
- Amazon Bedrock has text reformatting capabilities that ensure consistent input structure for FMs.

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
