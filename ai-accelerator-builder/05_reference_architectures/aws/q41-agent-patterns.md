---
type: reference_note
platform: aws
status: draft
source: udemy-question-41
---

# 41: Agent Orchestration Patterns

## Scenario

A fintech company is building a loan pre-qualification assistant. The assistant uses an AWS Step Functions state machine to orchestrate an agent-like loop: it invokes an Amazon Bedrock FM to decide the next action and, when needed, invokes an AWS Lambda function that calls a third-party credit bureau API. During intermittent credit bureau outages, the FM keeps requesting the tool call, which causes repeated loop iterations and increased token usage. The company needs to stop the workflow after a small number of tool failures, temporarily disable credit bureau calls for a cooldown period to prevent repeated failures, and ensure the tool Lambda function cannot access resources beyond a specific DynamoDB table and a single secret in AWS Secrets Manager. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Step Functions to implement a loop counter and stopping condition with a Choice state that ends the workflow after a maximum number of tool failures. Implement a circuit breaker by storing an “open/closed” flag with a TTL in DynamoDB that the state...

## Common anti-patterns

- Avoid implement a circuit breaker inside the Lambda function by using an in-memory variable to skip credit bureau calls for 10 minutes after a failure. Invoke the Amazon Bedrock FM directly from the Lambda function and stop the loop by returning an error to...

## Architecture guidance

- A safeguarded agentic workflow needs explicit controls that are independent of the FM’s behavior.
- Implementing stopping conditions in Step Functions prevents unbounded loops when the model keeps requesting a failing tool.
- A circuit breaker requires durable shared state so the system can “fail fast” during an outage and recover automatically after a cooldown; DynamoDB is well-suited for persisting the breaker state and can use TTL to...

## Domain

- Content Domain 2: Implementation and Integration
