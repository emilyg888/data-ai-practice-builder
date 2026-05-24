---
type: reference_note
platform: aws
status: draft
source: udemy-question-41
title: 41: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - access_control
topics:
  - agent orchestration patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - state store
  - access control
use_cases:
  - routing and orchestration
---

# 41: Agent Orchestration Patterns

## Scenario

A fintech company is building a loan pre-qualification assistant. The assistant uses an AWS Step Functions state machine to orchestrate an agent-like loop: it invokes an Amazon Bedrock FM to decide the next action and, when needed, invokes an AWS Lambda function that calls a third-party credit bureau API. During intermittent credit bureau outages, the FM keeps requesting the tool call, which causes repeated loop iterations and increased token usage. The company needs to stop the workflow after a small number of tool failures, temporarily disable credit bureau calls for a cooldown period to prevent repeated failures, and ensure the tool Lambda function cannot access resources beyond a specific DynamoDB table and a single secret in AWS Secrets Manager. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Step Functions to implement a loop counter and stopping condition with a Choice state that ends the workflow after a maximum number of tool failures. Implement a circuit breaker by storing an “open/closed” flag with a TTL in DynamoDB that the state...

## Architecture guidance

- A safeguarded agentic workflow needs explicit controls that are independent of the FM’s behavior.
- Implementing stopping conditions in Step Functions prevents unbounded loops when the model keeps requesting a failing tool.
- A circuit breaker requires durable shared state so the system can “fail fast” during an outage and recover automatically after a cooldown; DynamoDB is well-suited for persisting the breaker state and can use TTL to...

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
