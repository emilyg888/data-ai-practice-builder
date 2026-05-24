---
type: reference_note
platform: aws
status: draft
source: udemy-question-11
title: 11: Agent Orchestration Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Bedrock Guardrails
related_controls:
  - guardrails
  - prompt_policy
topics:
  - agent orchestration patterns
  - bedrock guardrails
  - lambda orchestration
  - bedrock
  - guardrails
  - prompt policy
  - prompt management
use_cases:
  - real-time streaming
  - routing and orchestration
---

# 11: Agent Orchestration Patterns

## Scenario

A security engineering team is reviewing an internal customer-support chatbot that uses an Amazon Bedrock agent with action groups (AWS Lambda tools) to look up account details and open support tickets. During a pilot, testers were able to craft prompts such as “ignore previous instructions” to attempt to override tool-use rules and to extract the agent’s hidden instructions. The team wants to add real-time protection against prompt injection and jailbreak attempts and also run automated adversarial tests whenever the team updates prompt templates, with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Attach Amazon Bedrock Guardrails to the agent invocation. Add a Lambda pre-processing layer that sanitizes user input and detects common prompt-injection and jailbreak patterns (for example, with pattern matching and named entity recognition). Use AWS Step...

## Architecture guidance

- The best approach combines managed safety controls with application-layer defenses and continuous validation.
- Bedrock Guardrails can be applied at invocation time to enforce content and policy controls consistently.
- A Lambda pre-processing step can sanitize and classify inputs to detect prompt-injection and jailbreak patterns before the agent executes tool calls, reducing the chance of adversarial instructions reaching the model or...

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
