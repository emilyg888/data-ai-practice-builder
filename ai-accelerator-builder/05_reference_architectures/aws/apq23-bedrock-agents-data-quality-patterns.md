---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-23
completeness: full
title: 23: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - Amazon Bedrock
related_controls:
topics:
  - agent orchestration patterns
  - bedrock agents
  - bedrock
use_cases:
  - routing and orchestration
---

# 23: Agent Orchestration Patterns

## Scenario

A media company uses various AI agents to automate content preparation tasks. One system automatically generates social media posts from news articles. One of the agentic workflows frequently encounters errors when interacting with the company's legacy content management system (CMS) API. The CMS API has inconsistent endpoint designs and poorly documented response schemas. Multiple AI agent workflows need to interact with the CMS API. A development team is spending significant time handling edge cases and API inconsistencies. The development team needs to implement a solution that standardizes and reduces the complexity of interactions with the CMS. The solution must maintain the existing API endpoints for legacy applications. The solution must be reusable across different AI agent workflows. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement a Model Context Protocol (MCP) server that provides a standardized interface to the CMS. Define function schemas for CMS operations. Implement the functions to handle API inconsistencies internally. Configure Amazon Bedrock AgentCore to interact with the CMS through...

## Architecture guidance

- MCP is designed to provide a consistent interface for AI models and agents to interact with external tools and APIs.
- The MCP server provides function schemas that define a standardized way to interact with the CMS.
- The implementation of the functions handles the API inconsistencies internally.

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
