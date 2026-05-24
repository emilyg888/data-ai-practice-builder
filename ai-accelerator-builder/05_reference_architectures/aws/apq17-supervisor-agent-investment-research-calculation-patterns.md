---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-17
completeness: full
title: 17: Supervisor-Agent Orchestration for Investment Research and Calculations
pattern_family: bedrock_agents
aws_services:
  - Amazon Bedrock
related_controls:
topics:
  - supervisor-agent orchestration
  - investment research calculations
  - bedrock agents
  - bedrock
use_cases:
  - document summarization
  - routing and orchestration
---

# 17: Supervisor-Agent Orchestration for Investment Research and Calculations

## Pattern summary

Use a supervisor agent to coordinate specialized sub-agents for quantitative analysis, news processing, calculations, and summarization.

## Scenario

A global investment company wants to use Amazon Bedrock to build a generative AI (GenAI) powered conversational assistant. The assistant needs to perform multiple tasks, including research and calculations. The assistant must analyze market data, process the latest news in the financial market, perform calculations, and generate investment insights. Which solution will meet these requirements?

## Common implementation patterns

- Create a system with a supervisor agent that orchestrates specialized sub-agents for quantitative analysis, news processing, and smart summarization.

## Architecture guidance

- AI agents can connect to different systems, APIs, and data sources.
- AI agents can automate tasks.
- For an application that requires multiple agents to complete different tasks, you need a supervisor agent to manage the complex workflows of task-specific agents.

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
