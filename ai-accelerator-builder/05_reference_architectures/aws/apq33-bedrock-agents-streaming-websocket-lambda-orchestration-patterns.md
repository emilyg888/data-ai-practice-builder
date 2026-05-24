---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-33
completeness: full
title: 33: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
related_controls:
topics:
  - agent orchestration patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
use_cases:
  - real-time streaming
  - routing and orchestration
---

# 33: Agent Orchestration Patterns

## Scenario

An online subscription video streaming company has a chat-based AI assistant that helps users by answering support queries. The assistant can handle simple single-step queries such as, "Can you help me change my subscription tier?" However, the assistant fails to understand more complex, multi-step queries such as, "Can you help me change my subscription tier, apply a discount code, and update my payment methods?" As a result, multi-step queries often escalate to a human for resolution. The company wants to implement agentic AI to improve the assistant's ability to handle complex queries. The solution must be able to dynamically adjust if something fails. For example, if a discount code is invalid, then the assistant should ask the user for a new code before proceeding. Which orchestration approach will meet these requirements with the LEAST development effort?

## Common implementation patterns

- Use the Strands Agents SDK. Create a specialist agent for each individual task. For example, create a "BillingAgent" to handle subscription tier changes. Deploy the agents as AWS Lambda functions. Register the specialized agents in Strands. Configure the orchestration flow so...

## Architecture guidance

- Strands Agents is a framework that can compose and orchestrate multiple specialized GenAI agents.
- Strands Agents can streamline the orchestration of multi-agent patterns that would be too difficult or cumbersome to implement through a single agent.

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
