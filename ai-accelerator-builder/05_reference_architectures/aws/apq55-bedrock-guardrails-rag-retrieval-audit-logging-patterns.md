---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-55
completeness: full
title: 55: RAG Patterns
pattern_family: bedrock_guardrails
aws_services:
  - Amazon Bedrock
  - Amazon S3
  - Bedrock Guardrails
related_controls:
  - audit_logging
  - evidence_retention
  - guardrails
  - pii_protection
  - prompt_policy
  - retrieval_grounding
topics:
  - rag patterns
  - bedrock guardrails
  - bedrock
  - s3 data assets
  - guardrails
  - audit logging
  - evidence retention
  - pii protection
  - prompt policy
  - retrieval grounding
  - rag
use_cases:
  - customer-facing assistant
  - real-time streaming
---

# 55: RAG Patterns

## Scenario

A GenAI developer builds an AI-powered customer service chat application for a company. The GenAI developer uses Amazon Bedrock to build the application. The application processes natural language inputs from users and generates real-time responses. The responses reference users' personally identifiable information (PII). The GenAI developer must configure the application to handle PII appropriately. According to internal privacy policies, PII should not be inadvertently exposed during or after inference. Prompt data cannot be retained longer than necessary. The handling of PII must comply with defined storage and retention policies. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock Guardrails to mask PII in user prompts before inference and redact PII from generated responses. Store prompts and model responses in Amazon S3. Use Amazon Macie to automatically classify and alert on PII stored in Amazon S3. Configure S3 Lifecycle policies to...

## Architecture guidance

- Guardrails can mask PII in user prompts before the prompts reach the model.
- Therefore, guardrails can reduce privacy risk at inference.
- Guardrails ensure that unredacted PII does not persist in logs or stored outputs.

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
