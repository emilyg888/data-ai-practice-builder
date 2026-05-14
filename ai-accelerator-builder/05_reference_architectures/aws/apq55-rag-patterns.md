---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-55
completeness: full
---

# 55: RAG Patterns

## Scenario

A GenAI developer builds an AI-powered customer service chat application for a company. The GenAI developer uses Amazon Bedrock to build the application. The application processes natural language inputs from users and generates real-time responses. The responses reference users' personally identifiable information (PII). The GenAI developer must configure the application to handle PII appropriately. According to internal privacy policies, PII should not be inadvertently exposed during or after inference. Prompt data cannot be retained longer than necessary. The handling of PII must comply with defined storage and retention policies. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock Guardrails to mask PII in user prompts before inference and redact PII from generated responses. Store prompts and model responses in Amazon S3. Use Amazon Macie to automatically classify and alert on PII stored in Amazon S3. Configure S3 Lifecycle policies to...

## Common anti-patterns

- Avoid use Amazon Macie to scan stored user prompts and responses in Amazon S3 for PII. Apply Amazon Comprehend for PII detection on stored logs to identify PII post-inference. Configure S3 Lifecycle policies to transition or expire objects after the retention period. Use AWS...
- Avoid use Amazon Bedrock Guardrails to mask PII in user prompts before inference and redact PII from generated responses. Store prompts and model responses in Amazon S3. Use Amazon Macie to scan stored data for PII and trigger alerts for compliance violations. Apply an S3...
- Avoid use Amazon Bedrock Guardrails to filter PII from prompts and responses. Store interaction logs in Amazon S3 with server-side encryption using AWS KMS. Enable AWS CloudTrail to log Amazon Bedrock API usage and apply Amazon Macie to generate compliance reports. Configure S3...

## Architecture guidance

- Guardrails can mask PII in user prompts before the prompts reach the model.
- Therefore, guardrails can reduce privacy risk at inference.
- Guardrails ensure that unredacted PII does not persist in logs or stored outputs.
