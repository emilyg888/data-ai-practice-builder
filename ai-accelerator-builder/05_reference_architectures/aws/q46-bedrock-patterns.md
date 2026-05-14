---
type: reference_note
platform: aws
status: draft
source: udemy-question-46
---

# 46: Implementation Patterns

## Scenario

A compliance engineering team is building an incident-report summarization feature by using an Amazon Bedrock text model. The summaries must be consistent in tone and avoid speculative language. During testing, the same report sometimes produces different wording and occasionally adds unsupported details. The team must continue using the same model and wants a data-driven way to validate changes before updating production. Which approach will MOST effectively improve output quality for this use case?

## Common implementation patterns

- Adjust the model’s inference parameters to reduce randomness (for example, lower temperature and tune top-p or top-k based on the desired determinism). Use Amazon Bedrock Model Evaluations with a representative prompt dataset and reference summaries to...

## Common anti-patterns

- Avoid create an Amazon Bedrock custom model by fine-tuning the base model with labeled prompt-completion pairs that contain ideal summaries. Deploy the custom model and route all summarization traffic to the new custom model. because fine-tuning can improve...

## Architecture guidance

- To reduce variation and speculative language without changing the underlying model, the most direct control is model-specific inference configuration.
- Lower temperature generally reduces randomness, while top-p or top-k tuning constrains token sampling to make responses more consistent.
- Because the team needs a data-driven validation method before production changes, running an evaluation with a representative prompt dataset and reference summaries provides measurable evidence of whether the new...

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
