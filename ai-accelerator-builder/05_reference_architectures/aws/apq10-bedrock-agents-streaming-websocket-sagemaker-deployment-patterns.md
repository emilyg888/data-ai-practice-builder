---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-10
completeness: full
title: 10: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - Amazon Bedrock
  - Amazon SageMaker
related_controls:
  - pii_protection
topics:
  - agent orchestration patterns
  - bedrock agents
  - bedrock
  - sagemaker
  - pii protection
use_cases:
  - real-time streaming
  - routing and orchestration
---

# 10: Agent Orchestration Patterns

## Scenario

A GenAI developer is designing a tool for an Amazon Bedrock agent. The tool provides sophisticated financial risk analysis by performing the following two key functions. The tool loads a 10 GB complex proprietary risk model into memory upon initialization. The tool maintains a persistent, long-lived WebSocket connection to a third-party service to receive real-time market data streams. The agent will invoke the tool frequently to answer user queries. The solution must ensure that the risk model is not reloaded for each invocation and that the data stream connection is stable and always available. Which approach will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the tool as a containerized application on Amazon ECS. Use the AWS Fargate launch type.

## Architecture guidance

- This approach provides the most suitable architecture for a complex, stateful, and long-running tool.
- Amazon ECS on Fargate can run persistent containerized applications without server management.
- With this approach, the large risk model can be loaded into memory when the container starts.

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
