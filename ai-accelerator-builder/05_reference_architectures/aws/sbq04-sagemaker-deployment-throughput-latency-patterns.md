---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-4
completeness: full
title: 4: SageMaker Deployment Patterns
pattern_family: sagemaker
aws_services:
  - Amazon SageMaker
related_controls:
  - audit_logging
topics:
  - sagemaker deployment patterns
  - sagemaker
  - audit logging
use_cases:
  - cost optimization
  - fine tuning
---

# 4: SageMaker Deployment Patterns

## Scenario

A GenAI developer deployed a fine-tuned LLM to an Amazon SageMaker AI endpoint. The GenAI developer used the default serving configuration for continuous batching with the AMI including the Deep Java Library (DJL). The model is being served on GPU-based Amazon EC2 instances, each with 8 GPUs. As the model scales to production, the GenAI developer discovers that many instances are needed to meet traffic demands. The GenAI developer wants to avoid increased costs from the overutilization. The GenAI developer analyzes logs. The GenAI developer discovers that the maximum I/O sequence length in real requests is 10 times smaller than what the model was originally configured to handle. Additionally, the current concurrency for each instance is low. Profiling shows that the model’s weights and activations can fit entirely within 4 GPUs. Which combination of steps can the GenAI developer take to improve resource utilization? (Select TWO.)

## Common implementation patterns

- Reduce the model’s maximum sequence length to provide a higher rolling batch size for each GPU.
- Use tensor parallelism with a degree of 4 to deploy two model replicas for each instance.

## Architecture guidance

- DJL is an open source, high-level deep learning framework.
- You can use DJL to streamline the process of building and deploying deep learning models.
- You can deploy models on SageMaker AI with DJL serving.

## AWS documentation validation

- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
