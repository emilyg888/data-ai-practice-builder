---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-2
completeness: full
title: 2: Prompt Governance Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS CloudTrail
  - AWS IAM
  - Amazon Bedrock
  - Bedrock Guardrails
related_controls:
  - audit_logging
  - guardrails
  - prompt_policy
topics:
  - prompt governance patterns
  - bedrock guardrails
  - audit logging
  - iam access control
  - bedrock
  - guardrails
  - prompt policy
  - prompt management
use_cases:
  - model governance
---

# 2: Prompt Governance Patterns

## Scenario

A marketing company generates creative briefs for clients by using Amazon Bedrock. Each client requires tailored brand tone, formatting, and output rules. The company wants to implement a configuration that defines reusable and parameterized prompt templates. The configuration must enforce style constraints such as restricting emojis or informal phrases. The configuration must track prompt usage and changes for compliance and auditing purposes. The configuration must ensure that prompt updates are reviewed and approved before activation. Which Amazon Bedrock Prompt Management configuration will meet these requirements?

## Common implementation patterns

- Create reusable templates with versioning and review workflows. Apply Amazon Bedrock Guardrails to enforce style rules. Enable AWS CloudTrail to log prompt usage and template changes for compliance.

## Architecture guidance

- You can use Prompt Management to create, store, and manage reusable, parameterized prompt templates.
- You can define system instructions to establish an assistant's role and add parameterized variables.
- The variables can include company name and document content.

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
