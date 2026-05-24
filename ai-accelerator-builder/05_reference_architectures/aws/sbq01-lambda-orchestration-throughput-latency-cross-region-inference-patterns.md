---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-1
completeness: full
title: 1: Throughput Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - pii_protection
topics:
  - throughput patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - pii protection
  - cross-region inference
use_cases:
  - cost optimization
---

# 1: Throughput Patterns

## Scenario

An ecommerce company has an application that uses Amazon Bedrock to generate product descriptions and recommendations. Currently, the application resides in a single AWS Region. When invoking a model in Amazon Bedrock during peak periods, the application receives an error. The error message says, "Too many requests, please wait before trying again." The company must increase the throughput for invocations during peak periods without introducing additional operational overhead. The company must maintain compatibility with the existing Amazon Bedrock API. The company must use the same FM. Which solution will meet these requirements in the MOST cost-effective way?

## Common implementation patterns

- Use cross-Region inference to distribute traffic across multiple Regions within a geographic area.

## Architecture guidance

- Cross-Region inference automatically distributes traffic across multiple Regions within your geographic area to process your inference request.
- Learn more about cross-Region inference.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock inference profiles support cross-Region inference for higher throughput and resilience; geographic profiles are the documented option when data residency boundaries matter.
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

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For maximum throughput and eligible models, evaluate Global cross-Region inference; for compliance-constrained workloads, prefer geographic inference profiles and update SCP/IAM policies for all destination Regions.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
