---
type: reference_note
platform: aws
status: draft
source: udemy-question-64
---

# 64: Throughput Patterns

## Scenario

A digital banking team is building a customer-facing chat assistant that uses an Amazon Bedrock text model through AWS Lambda and Amazon API Gateway. Users frequently abandon sessions when they do not see any output quickly, but the team wants to avoid the added cost of provisioning dedicated capacity because traffic is bursty. The team needs the chat UI to start displaying the model’s answer as soon as possible while still allowing the backend team to benchmark latency improvements. Which solution will provide the LOWEST perceived latency for end users with minimal additional cost?

## Common implementation patterns

- Update the application to use Amazon Bedrock streaming responses and stream tokens to the client (for example, by using API Gateway WebSockets or server-sent events). Enable Amazon Bedrock latency-optimized inference for the model and use Amazon CloudWatch...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- For interactive chat experiences, the key user-perceived metric is how quickly the application can start showing a response.
- Streaming responses from Amazon Bedrock let the client render output incrementally instead of waiting for the full completion, which significantly improves perceived responsiveness without requiring dedicated capacity.
- Enabling latency-optimized inference targets faster responsiveness (such as improved time to first token) for time-sensitive interactions, and CloudWatch metrics provide a way to benchmark improvements.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
