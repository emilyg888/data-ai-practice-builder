---
type: reference_note
platform: aws
status: draft
source: udemy-question-11
---

# 11: Agent Orchestration Patterns

## Scenario

A security engineering team is reviewing an internal customer-support chatbot that uses an Amazon Bedrock agent with action groups (AWS Lambda tools) to look up account details and open support tickets. During a pilot, testers were able to craft prompts such as “ignore previous instructions” to attempt to override tool-use rules and to extract the agent’s hidden instructions. The team wants to add real-time protection against prompt injection and jailbreak attempts and also run automated adversarial tests whenever the team updates prompt templates, with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Attach Amazon Bedrock Guardrails to the agent invocation. Add a Lambda pre-processing layer that sanitizes user input and detects common prompt-injection and jailbreak patterns (for example, with pattern matching and named entity recognition). Use AWS Step...

## Common anti-patterns

- Avoid fine-tune a custom foundation model to refuse requests that attempt to override instructions. Deploy the fine-tuned model and require all chatbot requests to use only the fine-tuned model. because this approach adds significant cost and operational...

## Architecture guidance

- The best approach combines managed safety controls with application-layer defenses and continuous validation.
- Bedrock Guardrails can be applied at invocation time to enforce content and policy controls consistently.
- A Lambda pre-processing step can sanitize and classify inputs to detect prompt-injection and jailbreak patterns before the agent executes tool calls, reducing the chance of adversarial instructions reaching the model or...

## Domain

- Content Domain 3: AI Safety, Security, and Governance
