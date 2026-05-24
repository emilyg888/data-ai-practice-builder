---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-5
completeness: full
title: 5: Guardrails Patterns
pattern_family: bedrock_guardrails
aws_services:
  - Amazon Bedrock
  - Bedrock Guardrails
related_controls:
  - guardrails
  - pii_protection
  - retrieval_grounding
topics:
  - guardrails patterns
  - bedrock guardrails
  - bedrock
  - guardrails
  - pii protection
  - retrieval grounding
use_cases:
  - customer-facing assistant
  - model governance
---

# 5: Guardrails Patterns

## Scenario

A healthcare company is using Amazon Bedrock to run a customer service AI assistant. A GenAI developer must use Amazon Bedrock Guardrails to ensure compliance with the following guidelines: The assistant must comply with healthcare regulations regarding patient privacy. The assistant should not expose personally identifiable information (PII). The assistant must avoid discussing unauthorized medical topics. The assistant should not provide incorrect medical information. Which combination of configurations will meet these requirements? (Select TWO.)

## Common implementation patterns

- Create sensitive information filters to detect and redact PII in user inputs and model responses. Set up denied topics for unauthorized medical topics.
- Enable automated reasoning checks that validate that model responses adhere to healthcare regulations. Implement contextual grounding to prevent hallucinations.

## Architecture guidance

- You can use sensitive information filters in Guardrails to detect and redact PII.
- You can use denied topics to block model engagement on specific subjects.
- This configuration complies with healthcare regulations by protecting PII.

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
