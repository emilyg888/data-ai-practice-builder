---
type: reference_note
platform: aws
status: draft
source: udemy-question-9
---

# 9: Prompt Patterns

## Scenario

A platform team at a regulated financial institution is building multiple internal applications that invoke Amazon Bedrock FMs for tasks such as summarization and drafting customer communications. The team must ensure that all applications use consistent, centrally managed prompts. Prompt changes must be reviewed and approved before they can be used in production, and auditors must be able to determine who used which prompt version and when. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Prompt Management to create reusable, parameterized prompts with versioning and an approval workflow. Store the prompt template repository in Amazon S3 as the source of truth. Enable AWS CloudTrail to audit Bedrock API usage and send...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A comprehensive prompt governance solution needs a centralized place to define prompts, parameterize them for reuse, control changes through versioning and approvals, and maintain auditability of prompt usage.
- Amazon Bedrock Prompt Management is designed for prompt lifecycle management and sharing across applications, while Amazon S3 can serve as a durable repository for prompt artifacts and related assets.
- For oversight and auditing, AWS CloudTrail provides an authoritative record of API activity, and Amazon CloudWatch Logs centralizes operational access logs from the applications that consume prompts.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
