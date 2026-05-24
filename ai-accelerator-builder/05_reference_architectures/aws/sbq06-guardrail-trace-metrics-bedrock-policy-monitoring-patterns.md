---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-6
completeness: full
title: 6: Guardrail Trace Metrics for Bedrock Policy Intervention Monitoring
pattern_family: bedrock_guardrails
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Bedrock Guardrails
related_controls:
  - guardrails
  - monitoring
  - pii_protection
  - prompt_policy
topics:
  - guardrail trace metrics
  - bedrock policy intervention monitoring
  - bedrock guardrails
  - bedrock
  - monitoring
  - guardrails
  - pii protection
  - prompt policy
use_cases:
  - model governance
  - fine tuning
---

# 6: Guardrail Trace Metrics for Bedrock Policy Intervention Monitoring

## Pattern summary

Enable Bedrock guardrail tracing and monitor policy-specific intervention metrics for content, topic, and sensitive-information controls.

## Scenario

A company is developing an AI assistant that processes customer data by using Amazon Bedrock. The AI assistant has multiple guardrails. The guardrails include prompt injection detection, sensitive information filtering, and denied topic blocking. When a customer query is blocked, a GenAI developer needs a detailed analysis of which specific guardrail rule was invoked and why the content was flagged. Then, the GenAI developer must fine-tune guardrail configurations and distinguish between legitimate customer queries and actual security threats. Which configuration provides the MOST detailed analysis of guardrail decision-making for content filtering?

## Common implementation patterns

- Configure guardrail tracing with `{"trace": "enabled"}` in guardrailConfig. Monitor InvocationsIntervened metrics filtered by the GuardrailPolicyType dimensions: ContentPolicy, TopicPolicy, and SensitiveInformationPolicy.

## Architecture guidance

- GuardrailPolicyType provides detailed information on which policy intervened in the guardrail.
- The GenAI developer can use this configuration to make an informed decision based on specific metrics.
- Learn more about CloudWatch metrics to monitor Amazon Bedrock guardrails.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
