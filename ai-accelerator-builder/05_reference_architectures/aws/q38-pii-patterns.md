---
type: reference_note
platform: aws
status: draft
source: udemy-question-38
---

# 38: PII Protection Patterns

## Scenario

A fintech company is launching a public, GenAI-powered customer support chatbot that uses Amazon Bedrock to answer account questions. Security reviewers are concerned about prompt injection attempts (for example, users trying to override instructions or request hidden system prompts) and about accidental leakage of personally identifiable information (PII) in both user inputs and model outputs. The company wants a defense-in-depth approach that adds comprehensive protection against FM misuse with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Use Amazon Bedrock Guardrails only, configured to block profanity and remove PII. Rely on the guardrail blocked-message response to prevent misuse, and return the model response directly to callers. This is the managed or lower-overhead approach called out as...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A defense-in-depth safety design uses multiple independent layers to reduce the probability and impact of unsafe inputs and outputs.
- A practical pattern is to filter and normalize inputs before model invocation (for example, detect and mask PII and suspicious content), apply model-native safety controls during inference (guardrails for...
- Implementing these layers with serverless components (Lambda, API Gateway) and managed services (Comprehend, Bedrock Guardrails) provides comprehensive protection with minimal infrastructure management, while approaches...

## Domain

- Content Domain 3: AI Safety, Security, and Governance
