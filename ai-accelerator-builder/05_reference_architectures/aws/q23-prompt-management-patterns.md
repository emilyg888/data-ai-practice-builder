---
type: reference_note
platform: aws
status: draft
source: udemy-question-23
---

# 23: Prompt Governance Patterns

## Scenario

An HR analytics team is building an internal assistant that drafts employee performance feedback by using Amazon Bedrock. The team stores standardized prompts in Amazon Bedrock Prompt Management. During a pilot, leadership raised concerns that the generated feedback might contain subtly different tone and recommendations for employees who are described with different demographic attributes in otherwise equivalent scenarios. The team wants to automatically evaluate and compare prompt variants for fairness, and track fairness results over time with minimal custom tooling. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon SageMaker Clarify to calculate pre-training bias metrics, and automatically fail the deployment if the bias metrics exceed thresholds. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Common anti-patterns

- Avoid route a statistically significant sample of generated feedback to Amazon Augmented AI (A2I) for human review, and store reviewers’ ratings in Amazon S3 to measure bias trends. because human review can assess bias, but it introduces substantial...

## Architecture guidance

- To apply fairness evaluations for foundation model outputs, the solution needs a repeatable way to compare alternatives and quantify bias-related behavior across a representative dataset.
- Using prompt variants and prompt orchestration enables controlled A/B testing, while automated model evaluation with an LLM-as-a-judge provides scalable scoring of outputs for fairness criteria without building a...
- Publishing those scores to CloudWatch makes fairness observable over time and supports governance reporting.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
