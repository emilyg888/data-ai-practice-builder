---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-38
completeness: full
title: 38: SageMaker Deployment Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon S3
  - Amazon SageMaker
related_controls:
  - pii_protection
topics:
  - sagemaker deployment patterns
  - bedrock agents
  - lambda orchestration
  - s3 data assets
  - sagemaker
  - pii protection
use_cases:
  - model governance
  - fine tuning
---

# 38: SageMaker Deployment Patterns

## Scenario

A financial services company is using Amazon SageMaker AI training jobs to fine-tune a custom FM. The company uses the FM for various sensitive use cases including fraud detection, analytics, and document analysis. The fine-tuning jobs invoke automatically when a user uploads new datasets in designated Amazon S3 buckets. The company must implement responsible AI practices to ensure compliance with industry regulations. A GenAI developer must ensure that all FM training datasets for new model releases are encrypted at rest by using AWS KMS customer managed keys. Datasets in buckets that use default AWS managed keys or that are not encrypted must be rejected and not used for model fine-tuning. The GenAI developer must validate that all existing S3 buckets comply with AI best practices for customer managed key encryption. Which solution will meet these requirements?

## Common implementation patterns

- Create an AWS Config custom rule using the AWS rule development kit (RDK). Set up the custom rule to check the existing S3 buckets for FM training data. Configure the rule to determine if the buckets use server-side encryption with AWS KMS (SSE-KMS) and a customer managed key....

## Architecture guidance

- This solution uses compliance-as-code to set continuous automation checks through AWS Config.
- AWS Config supports many automatic remediation options, including AWS Systems Manager Session Manager.
- This solution checks and enforces the use of customer managed keys.

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
