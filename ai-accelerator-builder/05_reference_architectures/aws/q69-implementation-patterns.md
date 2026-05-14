---
type: reference_note
platform: aws
status: draft
source: udemy-question-69
---

# 69: Implementation Patterns

## Scenario

A retail bank is building an internal GenAI assistant that helps loan officers draft customer-facing email responses. The bank must ensure the assistant follows an internal lending communications policy that prohibits the assistant from implying that a customer is approved or denied, and requires a standard disclaimer in every response. The bank must also document the model’s intended use and known limitations for governance review. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock guardrail that implements the lending communications policy, including an automated reasoning policy derived from the policy document. Invoke the model through an AWS Lambda function that performs a final compliance check (for...

## Common anti-patterns

- Avoid create an Amazon Bedrock Knowledge Base that contains the lending communications policy and product guidelines. Use RetrieveAndGenerate so the assistant can cite the policy in responses, and reject any response that does not include citations. because...

## Architecture guidance

- A policy-compliant GenAI system needs explicit enforcement mechanisms, not just guidance.
- Amazon Bedrock guardrails provide built-in controls to block or filter content according to policy requirements, and automated reasoning checks can apply structured logic derived from a policy document for complex...
- Adding a small Lambda layer for deterministic validation (such as checking for mandatory disclaimers and blocking disallowed phrases) creates a final compliance gate with minimal added complexity.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
