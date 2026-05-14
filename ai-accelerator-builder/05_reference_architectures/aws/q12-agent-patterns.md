---
type: reference_note
platform: aws
status: draft
source: udemy-question-12
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

## Domain

- Content Domain 2: Implementation and Integration
