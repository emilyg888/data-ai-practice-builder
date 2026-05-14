---
type: reference_note
platform: aws
status: draft
source: udemy-question-2
---

# 2: PII Protection Patterns

## Scenario

A financial services firm is building a customer-support chat experience by using Amazon Bedrock. An Amazon API Gateway endpoint invokes an AWS Lambda function that calls a text FM and stores the prompt/response transcript in an Amazon S3 bucket for audit purposes. The firm must reduce the risk of exposing personally identifiable information (PII) in FM responses, must detect whether any PII is still being written to the S3 audit bucket, and must retain audit data for 90 days before automatically deleting it. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Attach an Amazon Bedrock guardrail that masks or removes PII on both prompts and responses for the model invocation. Enable Amazon Macie to discover PII in the S3 audit bucket and send findings to Amazon EventBridge. Configure an S3 Lifecycle rule to expire...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A low-operations privacy-preserving design combines managed controls at the interaction layer, storage discovery, and retention enforcement.
- Bedrock guardrails can filter or mask PII in prompts and responses to reduce the likelihood of sensitive information being returned to users.
- Amazon Macie then provides automated discovery of PII in the S3 audit bucket so the security team can detect and respond if sensitive data is still being stored.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
