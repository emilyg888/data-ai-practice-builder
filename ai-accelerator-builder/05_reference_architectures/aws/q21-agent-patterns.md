---
type: reference_note
platform: aws
status: draft
source: udemy-question-21
---

# 21: Agent Orchestration Patterns

## Scenario

An online retail platform is building a customer-support assistant by using a Strands agent with an Amazon Bedrock text model. The agent can call a tool that looks up order status from an internal system by invoking an AWS Lambda function. In production, the agent intermittently fails because it calls the tool with missing or malformed parameters (for example, an empty orderId), which causes Lambda errors and breaks the conversation. The team wants to make the tool integration more reliable without changing the underlying FM or adding significant operational complexity. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Define the tool with the Strands API by using a standardized function signature (explicit parameter names and types). Add strict parameter validation and exception handling in the Lambda handler that returns structured error responses the agent can act on...

## Common anti-patterns

- Avoid switch the agent to a larger FM and add few-shot examples to the agent prompt demonstrating correct tool calls for multiple orderId formats. because better prompting and a larger model can reduce errors, but they do not guarantee reliable tool...

## Architecture guidance

- The most reliable way to harden an agent tool is to treat the tool boundary like an API contract: use a standardized function definition so the agent knows exactly what parameters to supply, and enforce correctness with...
- Structured, predictable error responses let the agent recover (for example, by asking the user for a missing orderId) instead of failing the entire workflow.
- Other approaches either focus on content moderation rather than tool correctness, add orchestration that cannot repair invalid inputs, or depend on probabilistic improvements from prompting/model size instead of...

## Domain

- Content Domain 2: Implementation and Integration
