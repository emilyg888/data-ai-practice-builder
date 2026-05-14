---
type: reference_note
platform: aws
status: draft
source: udemy-question-17
---

# 17: Implementation Patterns

## Scenario

A financial services engineering team is building an internal assistant that uses Amazon Bedrock to handle complex billing questions (for example, “Explain why I was charged a late fee, recalculate it based on these dates, and draft a customer response”). The assistant must break each request into structured reasoning steps and take actions by calling tools such as AWS Lambda functions that query Amazon DynamoDB. The team also needs a complete, auditable execution history with built-in retries and timeout controls, and wants to minimize custom orchestration code. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement an AWS Step Functions state machine that alternates between an Amazon Bedrock InvokeModel task to decide the next step (reasoning) and Lambda tasks to perform the selected action (acting). Use Choice states for branching and termination conditions,...

## Common anti-patterns

- Avoid use Amazon EventBridge rules to trigger a sequence of Lambda functions: one Lambda invokes the model to generate a plan, another Lambda queries DynamoDB, and a final Lambda calls the model again to generate the response. because eventBridge is effective...

## Architecture guidance

- To give an FM the ability to break down a complex problem into structured steps, the architecture needs an explicit control plane that can repeatedly: (1) ask the model what to do next, (2) execute the chosen action...
- AWS Step Functions is designed for this kind of orchestration and can implement ReAct-style patterns by combining Bedrock model invocations with tool invocations, conditional branching, and termination logic.
- It also provides managed retries, timeout controls, and a full execution history that supports auditing.

## Domain

- Content Domain 2: Implementation and Integration
