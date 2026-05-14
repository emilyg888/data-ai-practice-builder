---
type: reference_note
platform: aws
status: draft
source: udemy-question-4
---

# 4: Implementation Patterns

## Scenario

A fintech development team is building a customer-facing chat assistant that invokes an Amazon Bedrock text model through an AWS Lambda function. The assistant must block harmful user inputs (such as profanity and requests about disallowed topics) before they influence model behavior, and the team wants the simplest approach that can be applied consistently across the application. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock guardrail with topic filtering and word filtering. Attach the guardrail to the model invocation so that blocked inputs return a standard blocked message. This is the managed or lower-overhead approach called out as correct in the exam...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A managed input safety control that directly filters user prompts at invocation time is the most straightforward way to prevent harmful inputs from shaping model behavior.
- Bedrock guardrails are purpose-built for GenAI content filtering and can enforce policies like topic and word blocking while returning a consistent blocked response.
- Network-layer protections and schema validation can be useful complementary controls, but they do not provide reliable natural-language content moderation.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
