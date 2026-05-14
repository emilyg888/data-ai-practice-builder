---
type: reference_note
platform: aws
status: draft
source: udemy-question-61
---

# 61: Implementation Patterns

## Scenario

A media company is building an internal GenAI assistant on Amazon Bedrock to help employees summarize meeting notes and answer policy questions. The application currently sends every user request to a high-capability (and higher-cost) model. Usage has grown, and most requests are simple summaries, while a smaller portion requires deeper reasoning and higher response quality. The team wants to reduce ongoing inference costs while preserving high-quality answers for complex requests, with minimal custom routing logic to maintain. Which solution will meet these requirements MOST cost-effectively?

## Common implementation patterns

- Configure Amazon Bedrock Intelligent Prompt Routing to route requests between a lower-cost model for simple requests and a higher-capability model for complex requests based on prompt complexity, and monitor token usage in Amazon CloudWatch. This is the...

## Common anti-patterns

- Avoid purchase provisioned throughput for the higher-capability model so the application can handle growth more efficiently and reduce cost per request. because provisioned throughput is primarily a capacity and performance control mechanism; it does not...

## Architecture guidance

- The most cost-effective approach is to implement a tiered model selection strategy so that routine requests (like basic summaries) use a cheaper model while complex requests use a higher-capability model.
- This directly improves the price-to-performance ratio by matching model cost to task complexity.
- A managed routing capability minimizes the amount of custom logic the team must build and operate, while CloudWatch token metrics provide the telemetry needed to validate savings and iteratively tune the routing and...

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
