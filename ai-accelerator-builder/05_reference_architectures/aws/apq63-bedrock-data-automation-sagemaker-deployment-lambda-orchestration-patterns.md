---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-63
completeness: full
title: 63: BDA Transformation Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon EventBridge
  - Amazon S3
  - Amazon SageMaker
related_controls:
topics:
  - bda transformation patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - event orchestration
  - s3 data assets
  - sagemaker
  - cross-region inference
use_cases:
  - document summarization
  - cost optimization
  - routing and orchestration
---

# 63: BDA Transformation Patterns

## Scenario

A medical company that operates multiple clinics runs a generative AI (GenAI) application on AWS. The application uses AWS Step Functions to orchestrate two AWS Lambda functions. One function calls Amazon Transcribe Medical to transcribe clinic audio data. The second function uses the Amazon Nova Pro model in Amazon Bedrock to summarize the data. The company is onboarding additional clinics. Each clinic has a unique clinic ID. A GenAI developer must modify the architecture to store each clinic's data in a shared Amazon S3 bucket. The GenAI developer must use the clinic ID as the key prefix. The solution must track summarization costs for each clinic. Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO.)

## Common implementation patterns

- Create an Amazon Bedrock inference profile for each clinic ID. Modify the summarization Lambda function to use the profiles based on the S3 key prefix from the uploaded data.
- Create an Amazon EventBridge rule to capture PutObject events. Set the Step Functions state machine as the destination when a matching event occurs on the event bus.

## Architecture guidance

- Amazon Bedrock application inference profiles are specifically designed to manage and track FM costs in multi-tenant environments.
- This step efficiently handles cost attribution.
- The summarization Lambda can select the appropriate profile based on the clinic ID from the S3 key prefix.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock inference profiles support cross-Region inference for higher throughput and resilience; geographic profiles are the documented option when data residency boundaries matter.
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
- Documentation source: Cross-Region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html
- Documentation source: Inference profiles: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html
- Documentation source: Global cross-Region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- For maximum throughput and eligible models, evaluate Global cross-Region inference; for compliance-constrained workloads, prefer geographic inference profiles and update SCP/IAM policies for all destination Regions.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
