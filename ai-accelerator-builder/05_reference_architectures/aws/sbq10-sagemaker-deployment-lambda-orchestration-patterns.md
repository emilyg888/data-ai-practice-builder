---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-10
completeness: partial
title: 10: SageMaker Inference Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon SageMaker
related_controls:
topics:
  - sagemaker inference patterns
  - bedrock agents
  - lambda orchestration
  - sagemaker
use_cases:
  - multimodal extraction
---

# 10: SageMaker Inference Patterns

## Scenario

A GenAI developer is implementing a solution to create images from text descriptions. The GenAI developer successfully tested a pre-trained Hugging Face model by using Amazon SageMaker JumpStart. Now, the GenAI developer needs to deploy the model so that users can generate images on demand. The solution must use GPUs for inference. The solution must be able to handle text datasets up to 50 MB with image descriptions. The solution requires responses within 15 minutes. Which deployment strategy will meet these requirements?

## Common implementation patterns

- Deploy a SageMaker Asynchronous Inference endpoint that uses an accelerated computing SageMaker AI instance type. Create an AWS Lambda function for on-demand invocation of the SageMaker AI endpoint to manage image generation.

## Common anti-patterns

- Avoid adding custom infrastructure or manual process steps when a managed AWS capability satisfies the requirement with lower operational overhead.

## Architecture guidance

- SageMaker asynchronous endpoints provide long-running inference workloads with processing times up to 15 minutes.
- Asynchronous endpoints efficiently manage compute resources.
- This deployment strategy supports GPU instances for efficient processing, handles large datasets (up to 1 GB), and provides scaling based on actual usage.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
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
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
