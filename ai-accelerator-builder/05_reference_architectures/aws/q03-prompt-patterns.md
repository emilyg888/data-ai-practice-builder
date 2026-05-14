---
type: reference_note
platform: aws
status: draft
source: udemy-question-3
---

# 3: Prompt Patterns

## Scenario

A retail bank has multiple development teams building internal assistants that use Amazon Bedrock FMs for customer support, HR, and compliance workflows. The bank’s risk team requires a single governance approach so that prompt templates and inference settings are centrally controlled with versioning and approvals, all FM interactions are auditable for internal reviews, and organization-wide policy controls are enforced consistently across all applications. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Prompt Management to centrally store and version approved prompt templates (including variants). Apply Amazon Bedrock Guardrails to enforce the bank’s policy controls, and use AWS CloudTrail and Amazon CloudWatch Logs to provide...

## Common anti-patterns

- Avoid store prompt templates in Amazon S3 and require each team to deploy updates through their own CI/CD pipeline with peer code reviews. Configure each application to log prompt inputs and outputs to Amazon CloudWatch Logs. because although S3 and CI/CD can...

## Architecture guidance

- An organizational governance system for FMs needs centralized control over the artifacts that drive behavior (prompts and configurations), consistent enforcement of policies, and auditability for oversight.
- Centralized prompt governance through Amazon Bedrock Prompt Management standardizes prompt reuse, versioning, and controlled rollout across teams.
- Amazon Bedrock Guardrails adds consistent policy enforcement for both inputs and outputs, reducing the chance of teams implementing uneven safety controls.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
