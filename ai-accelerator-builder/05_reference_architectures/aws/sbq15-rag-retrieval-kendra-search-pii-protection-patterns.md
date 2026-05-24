---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-15
completeness: partial
title: 15: PII Protection Patterns
pattern_family: bedrock_guardrails
aws_services:
  - Amazon Bedrock
  - Amazon Kendra
  - Amazon S3
related_controls:
  - pii_protection
  - prompt_policy
  - retrieval_grounding
topics:
  - pii protection patterns
  - bedrock guardrails
  - bedrock
  - amazon kendra
  - s3 data assets
  - pii protection
  - prompt policy
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - architecture reference
---

# 15: PII Protection Patterns

## Scenario

A financial services company wants to develop a mobile app that will help users with account inquiries and general account information. The company has a large amount of email exchange data between customers and support staff to use as source material. The data is stored in an Amazon S3 bucket and contains personally identifiable information (PII) that should not appear in search results. Which solution will meet these requirements?

## Common implementation patterns

- Use a retrieval architecture with deterministic PII detection and redaction in the indexing or retrieval path rather than relying on prompts to suppress sensitive content.

## Architecture guidance

- Amazon Kendra provides enterprise search capabilities and can integrate with Amazon Bedrock FMs.
- However, using system prompts to handle PII during query processing is not a reliable or secure approach for sensitive financial data.
- A system prompt cannot ensure the consistent identification and removal of PII.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
