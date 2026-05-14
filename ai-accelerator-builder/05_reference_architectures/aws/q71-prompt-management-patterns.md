---
type: reference_note
platform: aws
status: draft
source: udemy-question-71
---

# 71: Prompt Governance Patterns

## Scenario

A SaaS provider runs a customer-support assistant that uses an Amazon Bedrock text model and a prompt template stored in Amazon Bedrock Prompt Management. The team wants to release an updated prompt version and occasionally switch to a newer model version. Before promoting changes, the team must automatically validate that answers remain consistent with previously accepted behavior and that hallucinations or semantic drift do not increase. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock Model Evaluations job that runs a prompt dataset (synthetic user workflows) stored in Amazon S3 against the candidate prompt/model and a baseline. Use an LLM-as-a-judge evaluation to score quality and AI-specific metrics, and use the...

## Common anti-patterns

- Avoid create an Amazon CloudWatch Synthetics canary that invokes the assistant with a fixed set of prompts and fails if the generated responses do not exactly match a stored set of expected responses. because exact string matching is not a reliable validation...

## Architecture guidance

- A low-overhead deployment validation system for GenAI updates should run repeatable synthetic user workflows and automatically score the candidate release for AI-specific regressions such as hallucinations and semantic...
- Using Amazon Bedrock Model Evaluations with a prompt dataset in Amazon S3 provides a managed way to evaluate candidate prompt/model changes against a baseline by using an evaluator model, producing objective scores that...
- Log analysis is post-deployment and manual, exact string matching is brittle for non-deterministic outputs, and human-in-the-loop reviews are higher operational overhead than managed automated evaluation.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
