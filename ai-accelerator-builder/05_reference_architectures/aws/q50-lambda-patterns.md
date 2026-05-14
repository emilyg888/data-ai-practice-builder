---
type: reference_note
platform: aws
status: draft
source: udemy-question-50
---

# 50: Throughput Patterns

## Scenario

A financial news provider is building a GenAI feature that generates short, compliant market summaries for traders by invoking an Amazon Bedrock text model from an AWS Lambda function. Traffic is highly predictable: every weekday at market open, request volume increases by about 10x for 45 minutes. During this window, users experience increased latency and occasional throttling errors from the model. The provider must keep all inference in a single AWS Region and wants consistent throughput with minimal operational overhead. Which solution will MOST effectively maximize throughput and resource utilization for this workload?

## Common implementation patterns

- Use Amazon Bedrock provisioned throughput for the selected model sized from expected requests-per-minute and tokens-per-minute. Update the application to invoke the provisioned model ARN, and use Amazon CloudWatch metrics (invocation count, latency,...

## Common anti-patterns

- Avoid deploy the model behind a SageMaker AI real-time endpoint with AWS Auto Scaling and invoke the endpoint from AWS Lambda. Use CloudWatch to scale the endpoint during market open based on CPU and request metrics. because this increases operational...

## Architecture guidance

- For predictable, recurring traffic spikes, the most direct way to increase model throughput while keeping a simple architecture is to reserve capacity for the exact Bedrock model being used.
- Provisioned throughput provides dedicated throughput for the model, and capacity planning based on expected request volume and token consumption helps select an appropriate provisioned level.
- CloudWatch monitoring then validates whether the provisioned capacity is sufficient (for example, by watching throttles, latency, and token counts) and informs iterative tuning.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
