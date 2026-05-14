---
type: reference_note
platform: aws
status: draft
source: udemy-question-60
---

# 60: PII Protection Patterns

## Scenario

A healthcare technology team is building a patient-facing virtual assistant that uses a text foundation model (FM) on Amazon Bedrock to answer questions about appointment scheduling. The assistant is exposed through a public API and has recently received user messages containing profanity, harassment, and attempts to override the assistant’s instructions (prompt injection). The team also must ensure that personally identifiable information (PII) such as phone numbers and social security numbers in user messages is masked before the FM processes the request. Which solution will protect against harmful user inputs in real time with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock guardrail that uses topic and word filtering (including profanity) and input PII masking. Configure the application’s Bedrock model invocation to apply the guardrail and return a standard blocked message when the guardrail intervenes....

## Common anti-patterns

- Avoid store each user message in Amazon S3 and run an Amazon Macie discovery job to detect PII. After the discovery job completes, invoke the FM on Amazon Bedrock by using the sanitized text. because macie is designed for discovering sensitive data in S3...

## Architecture guidance

- The most effective low-ops approach is to enforce safety controls at the FM boundary by using Amazon Bedrock Guardrails.
- Guardrails can filter harmful user prompts with topic and word/profanity filters and can mask PII as part of the same real-time inference call, ensuring consistent enforcement without building and operating a separate...
- Batch-oriented sensitive-data discovery and human-in-the-loop review introduce unacceptable latency for real-time chat, and generic web filtering alone does not provide comprehensive GenAI-focused protections such as...

## Domain

- Content Domain 3: AI Safety, Security, and Governance
