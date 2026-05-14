---
type: reference_note
platform: aws
status: draft
source: udemy-question-75
---

# 75: Prompt Regression Testing And Monitoring Patterns

## Scenario

A customer-support chatbot frequently changes prompts and inference settings. The team needs low-overhead pre-deployment regression testing and post-deployment detection of output regressions, integrated with automated release workflows.

## Common implementation patterns

- Maintain a representative prompt dataset with expected or reference outputs for repeatable evaluation.
- Add an automated pipeline stage that runs Amazon Bedrock model evaluations before promotion.
- Fail the deployment pipeline when evaluation scores fall below defined thresholds.
- Use Amazon CloudWatch Synthetics canaries after deployment to continuously validate end-to-end behavior with synthetic user flows.
- Publish canary outcomes as CloudWatch metrics and use alarms for regression detection.
- Separate release gating from production monitoring so both pre-release and post-release regressions are covered.

## Common anti-patterns

- Relying on human review as the primary release gate for frequent prompt changes.
- Exporting logs once per day for manual Athena sampling instead of enforcing automated quality checks.
- Increasing randomness during testing and treating "looks reasonable" as a regression strategy.
- Deploying prompt or parameter changes without a fixed benchmark dataset.
- Monitoring only availability while ignoring response-style and answer-quality regressions.

## Architecture guidance

- Prompt changes should be treated like code changes: versioned, evaluated, and gated.
- A lightweight evaluation loop usually combines offline benchmark scoring with online synthetic monitoring.
- Thresholds should cover the dimensions that matter to the business, such as tone, consistency, groundedness, policy adherence, and task success.
