---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-5
completeness: full
---

# 5: Guardrails Patterns

## Scenario

A healthcare company is using Amazon Bedrock to run a customer service AI assistant. A GenAI developer must use Amazon Bedrock Guardrails to ensure compliance with the following guidelines: The assistant must comply with healthcare regulations regarding patient privacy. The assistant should not expose personally identifiable information (PII). The assistant must avoid discussing unauthorized medical topics. The assistant should not provide incorrect medical information. Which combination of configurations will meet these requirements? (Select TWO.)

## Common implementation patterns

- Create sensitive information filters to detect and redact PII in user inputs and model responses. Set up denied topics for unauthorized medical topics.
- Enable automated reasoning checks that validate that model responses adhere to healthcare regulations. Implement contextual grounding to prevent hallucinations.

## Common anti-patterns

- Avoid configure content filters with high strength for the misconduct category. Create word filters to block unauthorized medical topics. because guardrails provide content filters with configurable strengths. You can use word filters to block specific keywords or phrases....
- Avoid configure prompt attack filters to prevent users from bypassing safety mechanisms. Create word filters to detect and block PII. because guardrails support prompt attack filters that can detect malicious input. For example, attempting to override instructions is malicious...
- Avoid create reusable templates in Amazon Bedrock Prompt Management. Configure the templates with strict system instructions for healthcare scenarios. Configure denied topics to block unauthorized medical topics. because prompt Management supports reusable templates and system...

## Architecture guidance

- You can use sensitive information filters in Guardrails to detect and redact PII.
- You can use denied topics to block model engagement on specific subjects.
- This configuration complies with healthcare regulations by protecting PII.
