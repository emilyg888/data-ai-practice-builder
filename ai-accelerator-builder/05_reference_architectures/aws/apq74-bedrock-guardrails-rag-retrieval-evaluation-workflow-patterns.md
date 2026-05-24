---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-74
completeness: full
title: 74: Guardrails Patterns
pattern_family: bedrock_guardrails
aws_services:
  - Amazon Bedrock
  - Bedrock Guardrails
related_controls:
  - audit_logging
  - guardrails
  - prompt_policy
  - retrieval_grounding
topics:
  - guardrails patterns
  - bedrock guardrails
  - bedrock
  - guardrails
  - audit logging
  - prompt policy
  - retrieval grounding
use_cases:
  - model governance
---

# 74: Guardrails Patterns

## Scenario

A software company is launching an AI assistant by using Amazon Bedrock. The AI assistant will help users troubleshoot issues by quickly exploring logs and documentation, and then recommending actions for remediation. A GenAI developer wants to set up Amazon Bedrock Guardrails. The GenAI developer wants to add protection against SQL injection. The GenAI developer wants to add a post-generation factuality check to prevent recommendations based on inaccurate information. Which combination of actions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Add a prompt attack filter.
- Add a contextual grounding check.

## Architecture guidance

- Guardrails provide safeguards for GenAI applications.
- You can configure guardrails to protect against prompt attacks, including jailbreaks and prompt injection.
- Guardrails support contextual grounding checks to detect and filter hallucinations in model responses.

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
