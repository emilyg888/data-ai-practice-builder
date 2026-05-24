---
type: reference_note
platform: aws
status: draft
source: udemy-question-7
title: 7: Serverless Integration Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon CloudWatch
related_controls:
  - monitoring
topics:
  - serverless integration patterns
  - bedrock agents
  - lambda orchestration
  - api gateway
  - bedrock
  - monitoring
use_cases:
  - internal assistant
  - document summarization
---

# 7: Serverless Integration Patterns

## Scenario

A healthcare SaaS provider exposes an internal GenAI summarization service through Amazon API Gateway and an AWS Lambda function that invokes an Amazon Bedrock text model. The provider expects to switch between different Bedrock models over time as pricing and regional availability change. The provider must be able to change the model selection without modifying or redeploying the Lambda code, and must be able to roll out a model change gradually with the ability to roll back automatically if errors increase. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use AWS AppConfig to store a configuration profile (for example, a feature flag) that contains the Bedrock modelId and inference settings. Configure the Lambda function to retrieve the AppConfig configuration at runtime and invoke Bedrock based on the...

## Architecture guidance

- A flexible model-selection pattern separates the model choice from the application code so the team can switch FMs or providers without a code redeploy.
- AWS AppConfig is purpose-built for dynamic configuration management and supports validating configuration changes, deploying changes progressively, and rolling back when CloudWatch alarms indicate problems.
- By having the Lambda function retrieve model selection parameters from AppConfig at runtime, the API remains stable while the modelId and related settings can be changed safely and repeatedly with minimal operational...

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

- Content Domain 1: Foundation Model Integration, Data Managem
