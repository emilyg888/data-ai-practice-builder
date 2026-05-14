---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-33
completeness: full
---

# 33: Agent Orchestration Patterns

## Scenario

An online subscription video streaming company has a chat-based AI assistant that helps users by answering support queries. The assistant can handle simple single-step queries such as, "Can you help me change my subscription tier?" However, the assistant fails to understand more complex, multi-step queries such as, "Can you help me change my subscription tier, apply a discount code, and update my payment methods?" As a result, multi-step queries often escalate to a human for resolution. The company wants to implement agentic AI to improve the assistant's ability to handle complex queries. The solution must be able to dynamically adjust if something fails. For example, if a discount code is invalid, then the assistant should ask the user for a new code before proceeding. Which orchestration approach will meet these requirements with the LEAST development effort?

## Common implementation patterns

- Use the Strands Agents SDK. Create a specialist agent for each individual task. For example, create a "BillingAgent" to handle subscription tier changes. Deploy the agents as AWS Lambda functions. Register the specialized agents in Strands. Configure the orchestration flow so...

## Common anti-patterns

- Avoid create a single agent by using Amazon Bedrock Agents. Define an OpenAPI schema for each task. Use AWS Lambda functions to implement tools for each task. For example, implement a "BillingTool" to handle subscription tier changes. Write an agent prompt that defines the agent...
- Avoid use AWS Step Functions and define a workflow. Start the workflow with a "choice" state that determines which workflow is needed based on the incoming request. Configure each task in the workflow as a separate AWS Lambda function that calls an Amazon Bedrock model with...
- Avoid use Amazon EventBridge Pipes. Create an Amazon API Gateway endpoint to accept the initial request. Route the request to an AWS Lambda function that uses an FM in Amazon Bedrock to understand the request. Based on the request, route to a series of Lambda functions that can...

## Architecture guidance

- Strands Agents is a framework that can compose and orchestrate multiple specialized GenAI agents.
- Strands Agents can streamline the orchestration of multi-agent patterns that would be too difficult or cumbersome to implement through a single agent.
