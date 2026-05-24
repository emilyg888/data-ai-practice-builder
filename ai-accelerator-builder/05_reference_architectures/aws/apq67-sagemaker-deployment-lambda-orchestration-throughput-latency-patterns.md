---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-67
completeness: full
title: 67: SageMaker Deployment Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon S3
  - Amazon SageMaker
related_controls:
topics:
  - sagemaker deployment patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - s3 data assets
  - sagemaker
use_cases:
  - fine tuning
---

# 67: SageMaker Deployment Patterns

## Scenario

A company fine-tunes a Meta Llama model by using proprietary training data in Amazon SageMaker AI. The company stores model weights in Hugging Face format. The company wants to import the model into Amazon Bedrock. The model files include Safetensors weights, configuration files, and tokenizer files. The model files are 45 GB in total size. The company needs a solution to provide a specific level of throughput for production workloads. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Custom Model Import to import the model files from Amazon S3. Deploy the model by using Amazon Bedrock Provisioned Throughput.

## Architecture guidance

- Custom Model Import supports importing Llama models in Hugging Face format from Amazon S3.
- For example, the Hugging Face format can include Safetensors weights, config.json files, and tokenizer files.
- After importing the model, the company can purchase Provisioned Throughput to provide dedicated compute capacity and throughput for production workloads.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
