---
type: reference_note
platform: aws
status: draft
source: udemy-question-20
title: 20: Throughput Patterns
pattern_family: sagemaker
aws_services:
  - Amazon Bedrock
  - Amazon SageMaker
related_controls:
topics:
  - throughput patterns
  - sagemaker
  - bedrock
use_cases:
  - internal assistant
  - document summarization
  - model governance
---

# 20: Throughput Patterns

## Scenario

A fintech company’s GenAI team is building an internal assistant that generates short compliance summaries by invoking an Amazon Bedrock text model. The assistant is called synchronously from an API, and users expect responses in near real time. During predictable weekday peaks, the team receives throttling errors from Bedrock and must increase available throughput while continuing to use the same model and keeping operational overhead low. Which deployment approach will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Purchase Amazon Bedrock provisioned throughput for the model and invoke the model by using the provisioned model ARN as the modelId during inference. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Architecture guidance

- Provisioned throughput in Amazon Bedrock is the most direct way to increase and stabilize model throughput for predictable demand while keeping operations simple.
- It preserves the existing Bedrock integration pattern and avoids building and managing separate hosting infrastructure.
- Retry strategies help handle transient errors but cannot guarantee additional capacity, and batch inference is not suitable for synchronous interactive use cases.

## AWS documentation validation

- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html

## AWS-supported alternative patterns

- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
