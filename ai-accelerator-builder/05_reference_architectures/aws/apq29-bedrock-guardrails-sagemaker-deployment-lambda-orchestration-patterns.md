---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-29
completeness: full
title: 29: SageMaker Deployment Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon EventBridge
  - Amazon SageMaker
  - Bedrock Guardrails
related_controls:
  - access_control
  - guardrails
topics:
  - sagemaker deployment patterns
  - bedrock guardrails
  - lambda orchestration
  - bedrock
  - event orchestration
  - sagemaker
  - guardrails
  - access control
  - data quality
use_cases:
  - customer-facing assistant
  - model governance
  - routing and orchestration
---

# 29: SageMaker Deployment Patterns

## Scenario

A GenAI developer is designing a customer-facing application for a company. The GenAI developer uses an FM that is deployed on Amazon SageMaker AI. The application will deliver automated advisory services to customers. The company requires AI governance controls to ensure compliance with internal policies and external regulations. For compliance, the application must meet the following requirements: Enforce content restrictions and usage policies during model inference. Ensure that all model limitations and compliance risks are documented and centrally accessible. Automate compliance checks on model outputs by using programmatic workflows to flag violations. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Use Amazon Bedrock Guardrails with customized denied topics and blocked keywords based on usage policies. Create an Amazon EventBridge rule to invoke an AWS Lambda function for post-inference policy validation.
- Create model cards by using SageMaker Model Registry. Use Amazon EventBridge to trigger compliance workflows that invoke AWS Lambda functions to validate policies at runtime.

## Architecture guidance

- You can use guardrails to define denied topics and blocked keywords to enforce content during model inference.
- You can use Guardrails for models that you deploy on SageMaker AI.
- This step reduces the risk of policy violations in AI-generated responses.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
