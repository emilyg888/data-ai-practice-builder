---
type: reference_note
platform: aws
status: draft
source: udemy-question-9
title: 9: Prompt Patterns
pattern_family: prompt_management
aws_services:
  - AWS CloudTrail
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
related_controls:
  - access_control
  - audit_logging
  - monitoring
  - prompt_policy
topics:
  - prompt patterns
  - prompt management
  - audit logging
  - bedrock
  - monitoring
  - s3 data assets
  - access control
  - prompt policy
use_cases:
  - document summarization
  - model governance
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

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
