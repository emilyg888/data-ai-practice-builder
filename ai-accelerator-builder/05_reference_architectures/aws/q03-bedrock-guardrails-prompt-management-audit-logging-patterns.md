---
type: reference_note
platform: aws
status: draft
source: udemy-question-3
title: 3: Prompt Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS CloudTrail
  - Amazon Bedrock
  - Amazon CloudWatch
  - Bedrock Guardrails
related_controls:
  - audit_logging
  - guardrails
  - monitoring
  - prompt_policy
topics:
  - prompt patterns
  - bedrock guardrails
  - audit logging
  - bedrock
  - monitoring
  - guardrails
  - prompt policy
  - prompt management
use_cases:
  - customer-facing assistant
  - internal assistant
  - model governance
  - routing and orchestration
---

# 3: Prompt Patterns

## Scenario

A retail bank has multiple development teams building internal assistants that use Amazon Bedrock FMs for customer support, HR, and compliance workflows. The bank’s risk team requires a single governance approach so that prompt templates and inference settings are centrally controlled with versioning and approvals, all FM interactions are auditable for internal reviews, and organization-wide policy controls are enforced consistently across all applications. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Prompt Management to centrally store and version approved prompt templates (including variants). Apply Amazon Bedrock Guardrails to enforce the bank’s policy controls, and use AWS CloudTrail and Amazon CloudWatch Logs to provide...

## Architecture guidance

- An organizational governance system for FMs needs centralized control over the artifacts that drive behavior (prompts and configurations), consistent enforcement of policies, and auditability for oversight.
- Centralized prompt governance through Amazon Bedrock Prompt Management standardizes prompt reuse, versioning, and controlled rollout across teams.
- Amazon Bedrock Guardrails adds consistent policy enforcement for both inputs and outputs, reducing the chance of teams implementing uneven safety controls.

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

## Domain

- Content Domain 3: AI Safety, Security, and Governance
