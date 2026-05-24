---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-70
completeness: full
title: 70: Audit Logging Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS CloudTrail
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon SageMaker
  - Bedrock Guardrails
related_controls:
  - access_control
  - audit_logging
  - guardrails
  - monitoring
  - prompt_policy
topics:
  - audit logging patterns
  - bedrock guardrails
  - audit logging
  - bedrock
  - monitoring
  - sagemaker
  - guardrails
  - access control
  - prompt policy
  - prompt management
use_cases:
  - model governance
  - routing and orchestration
---

# 70: Audit Logging Patterns

## Scenario

A company is deploying a generative AI (GenAI) solution across different business units to assist with documentation. The solution requires extensive testing and logging to provide audit trails and approval workflows of modifications throughout the solution’s lifecycle. The solution must remain consistent in its instructions and responses. The solution must enforce role-based access to prompt templates and prevent inappropriate content generation. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock Prompt Management for parameterized templates and role definitions. Configure Amazon Bedrock Guardrails to enforce safety policies. Enable AWS CloudTrail with Amazon CloudWatch Logs to record all prompt invocations and template changes.

## Architecture guidance

- Prompt Management provides version-control and role-aware templates with built-in approval workflows.
- Guardrails apply configurable policies that automatically block unsafe generations.
- CloudTrail records every Amazon Bedrock API call.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
