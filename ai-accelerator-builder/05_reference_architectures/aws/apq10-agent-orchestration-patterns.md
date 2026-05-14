---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-10
completeness: full
---

# 10: Agent Orchestration Patterns

## Scenario

A GenAI developer is designing a tool for an Amazon Bedrock agent. The tool provides sophisticated financial risk analysis by performing the following two key functions. The tool loads a 10 GB complex proprietary risk model into memory upon initialization. The tool maintains a persistent, long-lived WebSocket connection to a third-party service to receive real-time market data streams. The agent will invoke the tool frequently to answer user queries. The solution must ensure that the risk model is not reloaded for each invocation and that the data stream connection is stable and always available. Which approach will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the tool as a containerized application on Amazon ECS. Use the AWS Fargate launch type.

## Common anti-patterns

- Avoid package the tool and risk model into a container image. Deploy the image as an AWS Lambda function. because lambda is ephemeral and event-driven. Therefore, Lambda is not suitable for this scenario. The multi-gigabyte risk model would need to be loaded during every cold...
- Avoid deploy the tool on an Amazon SageMaker Real-Time Inference endpoint. Use an initialization script to load the model. because sageMaker AI is designed to host large models. However, SageMaker AI is optimized specifically for ML inference. SageMaker AI has a defined API...
- Avoid deploy the tool on Amazon EC2 instances. Use a launch template with a preconfigured AMI that includes the risk model and WebSocket configuration. because you can use Amazon EC2 with launch templates and AMIs to preconfigure an instance with the risk model. You can use...

## Architecture guidance

- This approach provides the most suitable architecture for a complex, stateful, and long-running tool.
- Amazon ECS on Fargate can run persistent containerized applications without server management.
- With this approach, the large risk model can be loaded into memory when the container starts.
