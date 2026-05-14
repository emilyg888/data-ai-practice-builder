---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-2
completeness: full
---

# 2: Prompt Governance Patterns

## Scenario

A marketing company generates creative briefs for clients by using Amazon Bedrock. Each client requires tailored brand tone, formatting, and output rules. The company wants to implement a configuration that defines reusable and parameterized prompt templates. The configuration must enforce style constraints such as restricting emojis or informal phrases. The configuration must track prompt usage and changes for compliance and auditing purposes. The configuration must ensure that prompt updates are reviewed and approved before activation. Which Amazon Bedrock Prompt Management configuration will meet these requirements?

## Common implementation patterns

- Create reusable templates with versioning and review workflows. Apply Amazon Bedrock Guardrails to enforce style rules. Enable AWS CloudTrail to log prompt usage and template changes for compliance.

## Common anti-patterns

- Avoid create templates for each client. Apply versioning to track changes and automatically activate new versions as the versions save. Set up Amazon CloudWatch Logs to track prompt invocations for compliance. because prompt Management supports versioning. However, automatically...
- Avoid create reusable templates with parameters for client-specific rules. Store prompt usage history in Amazon S3 by exporting logs from the application layer. Use tags to indicate whether a prompt is approved for production. because prompt Management provides reusable...
- Avoid define prompt templates, and parameterize tone and formatting. Configure IAM identity policies to restrict who can create or edit templates. Create an AWS Config custom rule to evaluate prompt resources for compliance against style rules. because iAM can control who edits...

## Architecture guidance

- You can use Prompt Management to create, store, and manage reusable, parameterized prompt templates.
- You can define system instructions to establish an assistant's role and add parameterized variables.
- The variables can include company name and document content.
