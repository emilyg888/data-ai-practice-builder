---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-47
completeness: full
---

# 47: Implementation Patterns

## Scenario

A retail company wants to reduce delays and manual effort in inventory replenishment. The company wants employees to be able to check inventory levels and submit inventory requests in natural language. The solution must automatically invoke internal supply chain processes with minimal ongoing maintenance. The solution must provide built-in Model Context Protocol (MCP) support. The company stores all inventory and data in Amazon Aurora. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy an agent by using Amazon Bedrock AgentCore Runtime with Strands Agents. Configure a prebuilt MCP server to expose Aurora inventory and store data as MCP tools. Integrate the agent with a company chat assistant interface.

## Common anti-patterns

- Avoid build an AI-powered chat assistant by using Amazon Lex. Create an AWS Lambda function that parses inventory requests and pushes request details to an Amazon SQS queue. Use the queue for backend supply chain microservices that run on Amazon ECS on AWS Fargate. because...
- Avoid create a REST API by using Amazon API Gateway in front of an AWS Lambda function. Configure the Lambda function to query Aurora for inventory information and invoke an AWS Step Functions workflow to handle replenishment tasks. because aPI Gateway and Lambda provide a...
- Avoid develop and host a custom MCP server on Amazon ECS on AWS Fargate. Implement MCP tools to connect to Aurora and invoke supply chain APIs. Integrate the server with an Amazon Bedrock agent. because a custom MCP server deployed on Amazon ECS can connect to Aurora and expose...

## Architecture guidance

- You can use AgentCore Runtime with Strands Agents to build AI agents with built-in MCP support.
- A prebuilt MCP server can directly expose Aurora inventory and store data as MCP tools.
- This solution eliminates the need for custom containers or API management.
