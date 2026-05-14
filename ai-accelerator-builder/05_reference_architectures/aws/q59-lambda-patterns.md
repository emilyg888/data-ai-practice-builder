---
type: reference_note
platform: aws
status: draft
source: udemy-question-59
---

# 59: Throughput Patterns

## Scenario

A product support team has built a public FAQ assistant that uses Amazon API Gateway and AWS Lambda to invoke an Amazon Bedrock text model. The assistant does not use user-specific context, and the team has configured the model with deterministic settings so the same question produces the same answer. Metrics show that a large percentage of requests are repeated verbatim across users, and the team wants to reduce Amazon Bedrock invocation costs and improve global response latency. Which solution will meet these requirements MOST cost-effectively?

## Common implementation patterns

- Implement semantic caching by storing embeddings of prompts and corresponding responses in Amazon MemoryDB. For each new prompt, generate an embedding and perform nearest-neighbor lookup. If the similarity score exceeds a threshold, return the cached response...

## Common anti-patterns

- Avoid enable Amazon Bedrock prompt caching for the system prompt and few-shot examples. Keep the user question as the suffix so the prefix is reused across invocations. because prompt caching can reduce token processing cost and improve latency by reusing a...

## Architecture guidance

- Because many requests are exact repeats and the responses are deterministic, the best optimization is to avoid invoking the FM when a previous identical response already exists.
- Edge caching with CloudFront accomplishes this by serving cached responses from edge locations, improving latency for global users while reducing total Bedrock invocations.
- A deterministic request fingerprint provides a stable cache key and helps ensure cache correctness when prompts or model parameters change.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
