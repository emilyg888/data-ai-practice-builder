---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-2
completeness: full
title: 2: AgentCore Runtime Patterns
pattern_family: bedrock_agents
aws_services:
  - Amazon Bedrock
  - Amazon SageMaker
  - Amazon Bedrock AgentCore Runtime
related_controls:
  - monitoring
topics:
  - agentcore runtime patterns
  - bedrock agents
  - bedrock
  - sagemaker
  - monitoring
use_cases:
  - real-time streaming
  - routing and orchestration
---

# 2: AgentCore Runtime Patterns

## Scenario

A financial services company is developing a research agent that processes complex financial data queries. The company must deploy existing Python agent code to Amazon Bedrock AgentCore Runtime. The company wants to reduce infrastructure management overhead and operational complexity. The agent must be able to handle quick data lookups that require sub-second responses. The agent must be able to handle comprehensive research report generation. For example, streaming responses over several minutes. The solution must automatically manage HTTP server configuration, endpoint routing, and health monitoring. Which deployment approaches will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Implement the AgentCore SDK with the @app.entrypoint decorator to automatically handle server setup and endpoint management.
- Deploy the agent by using the AgentCore starter toolkit for automated packaging, containerization, and deployment workflows.

## Architecture guidance

- The AgentCore SDK with the @app.entrypoint decorator provides minimal operational overhead.
- This approach automatically creates an HTTP server on port 8080 and implements the required /invocations and /ping endpoints.
- This approach handles proper content types and response formats.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
