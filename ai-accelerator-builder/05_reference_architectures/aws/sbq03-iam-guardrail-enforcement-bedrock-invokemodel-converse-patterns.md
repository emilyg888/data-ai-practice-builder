---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-3
completeness: full
title: 3: IAM Guardrail Enforcement for Bedrock InvokeModel and Converse APIs
pattern_family: bedrock_guardrails
aws_services:
  - AWS IAM
  - Amazon Bedrock
  - Bedrock Guardrails
related_controls:
  - access_control
  - guardrails
topics:
  - iam guardrail enforcement
  - bedrock invokemodel converse apis
  - bedrock guardrails
  - iam access control
  - bedrock
  - guardrails
  - access control
use_cases:
  - model governance
---

# 3: IAM Guardrail Enforcement for Bedrock InvokeModel and Converse APIs

## Pattern summary

Use IAM policies with the bedrock:GuardrailIdentifier condition key to require guardrails on Bedrock InvokeModel and Converse calls.

## Scenario

A company is implementing AI governance policies. The policies require all FM interactions to be secured with guardrails. The company configures Amazon Bedrock guardrails. The company must ensure that all InvokeModel and Converse API calls to FMs apply the guardrails. Which solution will enforce guardrail compliance for the API calls in the MOST operationally efficient way?

## Common implementation patterns

- Configure IAM policies for the InvokeModel and Converse API calls with the bedrock:GuardrailIdentifier condition key. Apply the policies to all IAM roles that access the Amazon Bedrock FMs...

## Architecture guidance

- This solution uses IAM policies with the bedrock:GuardrailIdentifier condition key to enforce guardrail compliance for InvokeModel and Converse API calls.
- IAM policies are a centralized and efficient way to control access to AWS resources.
- You can apply the policies to roles that access Amazon Bedrock FMs.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
