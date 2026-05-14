---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-2
completeness: full
---

# 2: AgentCore Runtime Patterns

## Scenario

A financial services company is developing a research agent that processes complex financial data queries. The company must deploy existing Python agent code to Amazon Bedrock AgentCore Runtime. The company wants to reduce infrastructure management overhead and operational complexity. The agent must be able to handle quick data lookups that require sub-second responses. The agent must be able to handle comprehensive research report generation. For example, streaming responses over several minutes. The solution must automatically manage HTTP server configuration, endpoint routing, and health monitoring. Which deployment approaches will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Implement the AgentCore SDK with the @app.entrypoint decorator to automatically handle server setup and endpoint management.
- Deploy the agent by using the AgentCore starter toolkit for automated packaging, containerization, and deployment workflows.

## Common anti-patterns

- Avoid implement a FastAPI server with a configuration of /invocations and /ping endpoints and container orchestration. because a FastAPI server can meet the technical requirements for AgentCore Runtime. However, a FastAPI server requires manual configuration. You must implement /invocations and...
- Avoid deploy the agent on Amazon ECS on AWS Fargate by using a custom container image that runs the AgentCore SDK application. because running the agent on ECS on Fargate with a custom container image increases operational overhead. You must build and maintain Dockerfiles, manage container images,...
- Avoid deploy the agent on Amazon SageMaker AI real-time endpoints by using a custom inference container. because you can deploy the Python agent on a SageMaker AI real-time endpoint by using a custom inference container. This approach can host a long-running workload. However, this approach...

## Architecture guidance

- The AgentCore SDK with the @app.entrypoint decorator provides minimal operational overhead.
- This approach automatically creates an HTTP server on port 8080 and implements the required /invocations and /ping endpoints.
- This approach handles proper content types and response formats.
