---
type: reference_note
platform: aws
status: draft
source: udemy-question-52
---

# 52: Implementation Patterns

## Scenario

A retail platform is building a GenAI feature that helps sellers create product listing text by using Amazon Bedrock. Most requests are routine (for example, short rewrites and basic summaries), but a smaller percentage require more advanced reasoning and higher-quality copy. The team wants to reduce ongoing inference costs while still producing high-quality output for complex requests, and the solution must avoid managing GPU infrastructure. Which deployment approach is the MOST cost-effective way to meet these requirements?

## Common implementation patterns

- Implement API-based model cascading in Amazon Bedrock: route routine listing requests to a smaller pre-trained model and automatically escalate complex requests to a larger model (for example, by using intelligent prompt routing or application-side routing...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A cost-optimized GenAI deployment often comes from matching model capability to request complexity.
- Routine tasks (rewrites, short summaries) typically do not require the most capable and expensive model.
- A cascading approach invokes a smaller, cheaper pre-trained model for the common case and escalates only when the request is complex or when additional capability is needed.

## Domain

- Content Domain 2: Implementation and Integration
