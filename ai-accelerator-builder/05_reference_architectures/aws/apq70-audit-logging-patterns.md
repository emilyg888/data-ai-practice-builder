---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-70
completeness: full
---

# 70: Audit Logging Patterns

## Scenario

A company is deploying a generative AI (GenAI) solution across different business units to assist with documentation. The solution requires extensive testing and logging to provide audit trails and approval workflows of modifications throughout the solution’s lifecycle. The solution must remain consistent in its instructions and responses. The solution must enforce role-based access to prompt templates and prevent inappropriate content generation. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock Prompt Management for parameterized templates and role definitions. Configure Amazon Bedrock Guardrails to enforce safety policies. Enable AWS CloudTrail with Amazon CloudWatch Logs to record all prompt invocations and template changes.

## Common anti-patterns

- Avoid manage prompt templates in Amazon S3 with object versioning enabled. Use Amazon Macie for toxic-content detection in generated text. Use AWS CloudTrail for audit logging. because s3 Versioning maintains file histories. However, S3 Versioning does not provide the necessary...
- Avoid manage prompts in Amazon SageMaker Model Registry. Use SageMaker Clarify for real-time bias filtering and real-time toxicity filtering of model outputs. Set up AWS CloudTrail for audit logging. because model Registry tracks model artifacts, not prompt templates. Clarify...
- Avoid use Amazon Bedrock Prompt Management to create prompt templates. Configure Amazon Bedrock Guardrails to enforce safety policies and role-based access controls (RBAC). Enable AWS CloudTrail with Amazon CloudWatch Logs to record all prompt invocations and template changes....

## Architecture guidance

- Prompt Management provides version-control and role-aware templates with built-in approval workflows.
- Guardrails apply configurable policies that automatically block unsafe generations.
- CloudTrail records every Amazon Bedrock API call.
