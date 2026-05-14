---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-4
completeness: partial
---

# 4: Guardrails Patterns

## Scenario

A GenAI developer must create dynamic content filtering for a customer service chat-based AI assistant. Multiple departments in a company use the assistant. The assistant is deployed on an Amazon Nova Pro model. AWS Lambda functions handle the chat logic. The company has the following requirements: Stricter content policies must be enforced during business hours. Each department must have department-specific filtering rules. Amazon Bedrock Guardrails must be used for content filtering. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use the answer key and visible explanation text as the basis for the endorsed architecture pattern when the source export does not preserve the full correct-option body.

## Common anti-patterns

- Avoid create a single guardrail with maximum restrictions. Create an AWS Step Functions workflow that orchestrates several Lambda functions to post-process responses based on business hours and department. Store filtering rules in AWS Systems Manager Parameter Store. because...

## Architecture guidance

- Guardrails can provide content filtering at the model invocation level.
- Guardrails has built-in capabilities to manage different filtering contexts.
- You can create a single guardrail with maximum restrictions.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt and answer key.
