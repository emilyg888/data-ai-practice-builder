---
type: reference_note
platform: aws
status: draft
source: udemy-question-12
title: 12: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
related_controls:
topics:
  - agent orchestration patterns
  - bedrock agents
  - lambda orchestration
use_cases:
  - internal assistant
  - routing and orchestration
---

# 12: Agent Orchestration Patterns

## Scenario

A SaaS provider is building an internal GenAI assistant that must call existing operational tools through Model Context Protocol (MCP) so multiple agent frameworks can reuse the same tool interface. One tool is a simple, stateless lookup that returns small JSON responses. Another tool performs CPU-intensive document processing that relies on native libraries and requires a longer-running process. The team wants a design that uses MCP consistently while keeping operational overhead LOW. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement the stateless lookup tool as a Lambda-based MCP server. Implement the document-processing tool as an MCP server running on Amazon ECS with AWS Fargate. Use MCP client libraries in each agent to call both MCP servers through a consistent interface....
- Deploy a single MCP server on Amazon EC2 that hosts both tools and exposes them over HTTP streaming. Install and manage all dependencies on the EC2 instance and scale the instance vertically as demand grows. This is the managed or lower-overhead approach...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A practical MCP-based extension framework typically separates lightweight, stateless tools from complex tools with heavier runtime requirements.
- Stateless tools map well to AWS Lambda because there are no servers to manage and scaling is automatic.
- Tools that need native libraries, larger dependency trees, or longer-running execution are better packaged as containers and run on Amazon ECS with AWS Fargate to avoid managing EC2 hosts.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
