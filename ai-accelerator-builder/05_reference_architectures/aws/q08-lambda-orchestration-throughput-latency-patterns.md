---
type: reference_note
platform: aws
status: draft
source: udemy-question-8
title: 8: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
related_controls:
  - prompt_policy
topics:
  - agent orchestration patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - prompt policy
use_cases:
  - customer-facing assistant
  - cost optimization
  - routing and orchestration
---

# 8: Agent Orchestration Patterns

## Scenario

A customer support engineering team is building an agent-assist feature that uses Amazon Bedrock. For each incoming support ticket, the UI must display (1) a customer-ready response and (2) a short internal troubleshooting checklist. The team has found that generating both artifacts in a single prompt increases latency and cost. The team wants to use specialized foundation models (FMs) for each artifact and then combine the results into one JSON payload for the frontend. Which solution will meet these requirements with the LOWEST end-to-end latency?

## Common implementation patterns

- Use AWS Step Functions with a Parallel state that invokes two different Amazon Bedrock models at the same time (one optimized for concise summaries and one optimized for detailed responses). Use a final AWS Lambda task to merge both outputs into a single JSON...

## Architecture guidance

- The key requirement is coordinating multiple specialized FMs and combining their outputs while minimizing latency.
- Running the two model invocations in parallel reduces the critical path because both artifacts are generated at the same time.
- A final aggregation step (for example, a Lambda function) can deterministically assemble the customer-facing response and the internal checklist into a single JSON payload.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
