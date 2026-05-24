---
type: reference_note
platform: aws
status: draft
source: udemy-question-31
title: 31: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - Amazon DynamoDB
related_controls:
  - retrieval_grounding
topics:
  - agent orchestration patterns
  - bedrock agents
  - state store
  - retrieval grounding
use_cases:
  - routing and orchestration
---

# 31: Agent Orchestration Patterns

## Scenario

A platform engineering team is building an internal “Ops Copilot” that autonomously troubleshoots application incidents. The team uses AWS Agent Squad to route each user request to one of several specialized Strands agents (for example, an incident triage agent and a runbook agent). Users expect the assistant to remember conversation context within a session and also retain longer-term preferences (for example, preferred service names and escalation rules) across multiple sessions. The team wants a serverless approach that minimizes the amount of custom state-management code they must build and operate. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store per-session conversation history in Amazon DynamoDB and store long-term preferences as separate DynamoDB items. Pass the session identifier between the routed agents so each agent can fetch and update the state as needed. This is the managed or...

## Architecture guidance

- The core challenge is maintaining both short-term conversational state (what was said earlier in the current interaction) and durable long-term memory (user preferences and extracted insights) while coordinating that...
- A managed agent runtime with built-in memory reduces custom engineering and operational burden because it provides purpose-built abstractions for sessions and long-term memory records, and it avoids building and...
- Alternatives such as using a general-purpose database, container-local storage, or a retrieval knowledge base can work in limited scenarios, but they either do not provide session semantics and durable multi-agent state...

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
