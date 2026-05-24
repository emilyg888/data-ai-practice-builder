---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-68
completeness: full
title: 68: Audit Logging Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - access_control
  - audit_logging
  - guardrails
topics:
  - audit logging patterns
  - bedrock guardrails
  - iam access control
  - lambda orchestration
  - bedrock
  - access control
  - audit logging
  - guardrails
use_cases:
  - model governance
---

# 68: Audit Logging Patterns

## Scenario

A company is developing an application by using Amazon Bedrock. Multiple development teams will access the application across different departments. The company uses AWS Organizations with OUs for each department. The company must enforce least privilege access to FMs and provide role-based access control (RBAC) for each department. The solution must integrate with the company's existing enterprise identity provider (IdP) for centralized governance. Only approved development teams should be allowed to invoke specific models. The solution must provide an auditable access trail. Which solution will meet these requirements MOST securely?

## Common implementation patterns

- Configure AWS IAM Identity Center with SAML federation from the enterprise IdP. Create permissions sets that restrict Amazon Bedrock model invocation for each OU. Create an SCP that prevents unauthorized actions outside of approved models.

## Architecture guidance

- IAM Identity Center provides centralized workforce access with support for SAML federation to enterprise IdPs.
- You can configure permissions sets that enforce least privilege IAM policies to scope access to specific Amazon Bedrock model actions for each department.
- You can apply SCPs at the OU level to provide an organizational guardrail that blocks non-approved actions.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
