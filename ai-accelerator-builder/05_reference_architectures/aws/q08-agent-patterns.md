---
type: reference_note
platform: aws
status: draft
source: udemy-question-8
---

# 8: Agent Orchestration Patterns

## Scenario

A customer support engineering team is building an agent-assist feature that uses Amazon Bedrock. For each incoming support ticket, the UI must display (1) a customer-ready response and (2) a short internal troubleshooting checklist. The team has found that generating both artifacts in a single prompt increases latency and cost. The team wants to use specialized foundation models (FMs) for each artifact and then combine the results into one JSON payload for the frontend. Which solution will meet these requirements with the LOWEST end-to-end latency?

## Common implementation patterns

- Use AWS Step Functions with a Parallel state that invokes two different Amazon Bedrock models at the same time (one optimized for concise summaries and one optimized for detailed responses). Use a final AWS Lambda task to merge both outputs into a single JSON...

## Common anti-patterns

- Avoid send each ticket to an Amazon SQS queue and use two separate AWS Lambda consumers to invoke different Amazon Bedrock models. Store results in Amazon S3 and have the frontend poll for completion. because this design is asynchronous and introduces...

## Architecture guidance

- The key requirement is coordinating multiple specialized FMs and combining their outputs while minimizing latency.
- Running the two model invocations in parallel reduces the critical path because both artifacts are generated at the same time.
- A final aggregation step (for example, a Lambda function) can deterministically assemble the customer-facing response and the internal checklist into a single JSON payload.

## Domain

- Content Domain 2: Implementation and Integration
