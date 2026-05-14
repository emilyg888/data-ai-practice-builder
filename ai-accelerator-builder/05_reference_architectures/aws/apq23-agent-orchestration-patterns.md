---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-23
completeness: full
---

# 23: Agent Orchestration Patterns

## Scenario

A media company uses various AI agents to automate content preparation tasks. One system automatically generates social media posts from news articles. One of the agentic workflows frequently encounters errors when interacting with the company's legacy content management system (CMS) API. The CMS API has inconsistent endpoint designs and poorly documented response schemas. Multiple AI agent workflows need to interact with the CMS API. A development team is spending significant time handling edge cases and API inconsistencies. The development team needs to implement a solution that standardizes and reduces the complexity of interactions with the CMS. The solution must maintain the existing API endpoints for legacy applications. The solution must be reusable across different AI agent workflows. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement a Model Context Protocol (MCP) server that provides a standardized interface to the CMS. Define function schemas for CMS operations. Implement the functions to handle API inconsistencies internally. Configure Amazon Bedrock AgentCore to interact with the CMS through...

## Common anti-patterns

- Avoid create a new REST API transformation layer that standardizes the CMS API responses and provides detailed OpenAPI documentation. Deploy the layer as a proxy service between AI agents and the CMS. because this solution would improve documentation and standardize responses....
- Avoid develop a custom middleware layer that transforms API requests and responses. Deploy the custom middleware layer as a sidecar container alongside each AI agent to handle CMS interactions. because this solution could address the immediate issue. However, this solution is...
- Avoid refactor the existing CMS API to follow modern REST principles and add comprehensive documentation. Update all AI agents to use the new standardized endpoints. because this solution requires significant changes to the existing CMS. Therefore, this solution could break...

## Architecture guidance

- MCP is designed to provide a consistent interface for AI models and agents to interact with external tools and APIs.
- The MCP server provides function schemas that define a standardized way to interact with the CMS.
- The implementation of the functions handles the API inconsistencies internally.
