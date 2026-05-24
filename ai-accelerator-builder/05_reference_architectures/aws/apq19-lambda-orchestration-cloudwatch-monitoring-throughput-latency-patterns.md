---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-19
completeness: full
title: 19: Cross-Region Inference Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon CloudWatch
related_controls:
  - audit_logging
topics:
  - cross-region inference patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - api gateway
  - bedrock
  - monitoring
  - audit logging
  - cross-region inference
use_cases:
  - document summarization
  - routing and orchestration
---

# 19: Cross-Region Inference Patterns

## Scenario

A company is building a generative AI (GenAI) powered application that uses Amazon API Gateway, AWS Lambda, and Amazon Bedrock. The application must support summarization, classification, and translation tasks. A separate FM performs each task. A GenAI developer must configure the application to meet the following requirements: Route inference requests to different FMs dynamically based on task type and customer configuration. Update routing logic at runtime without redeploying the application. Implement automatic failover to an alternate model or AWS Region if the primary model or Region is unavailable. Maintain low latency, resilience, and cross-Region support for multiple providers. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create a Lambda function that retrieves model routing rules from an AWS AppConfig hosted configuration profile at runtime. Use an AWS Step Functions state machine with branching paths for each task type and a circuit breaker pattern for failover. Invoke Amazon Bedrock by using...

## Architecture guidance

- An AWS AppConfig hosted configuration is a managed way to provide dynamic application configuration updates without redeployment.
- Step Functions is a serverless workflow service that orchestrates multiple AWS services by using state machines with built-in error handling.
- AWS AppConfig provides runtime routing updates.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock inference profiles support cross-Region inference for higher throughput and resilience; geographic profiles are the documented option when data residency boundaries matter.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Cross-Region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html
- Documentation source: Inference profiles: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html
- Documentation source: Global cross-Region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For maximum throughput and eligible models, evaluate Global cross-Region inference; for compliance-constrained workloads, prefer geographic inference profiles and update SCP/IAM policies for all destination Regions.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
