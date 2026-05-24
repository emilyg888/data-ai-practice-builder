---
type: reference_note
platform: aws
status: draft
source: udemy-question-32
title: 32: Serverless Integration Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon SageMaker
  - Bedrock Guardrails
related_controls:
  - access_control
  - audit_logging
  - guardrails
topics:
  - serverless integration patterns
  - bedrock guardrails
  - lambda orchestration
  - api gateway
  - bedrock
  - sagemaker
  - guardrails
  - access control
  - audit logging
use_cases:
  - model governance
---

# 32: Serverless Integration Patterns

## Scenario

A fintech company is building a customer self-service chatbot that runs behind Amazon API Gateway and AWS Lambda. The chatbot uses Amazon Bedrock to answer questions such as “What were my last 5 card transactions?” by querying an Amazon Aurora PostgreSQL database. The company is concerned that abusive user messages could cause the chatbot to respond with profane or otherwise harmful language. The company also wants to avoid any fabricated transaction amounts and ensure that data-backed answers are deterministic and auditable. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure Amazon Bedrock Guardrails to filter model responses (for example, profanity and topic filters) and return a blocked message when content violates policy. For transaction questions, implement a text-to-SQL flow where the model produces a SQL query...

## Architecture guidance

- A robust content safety framework for a customer-facing chatbot should combine managed output controls with deterministic data access patterns.
- Guardrails help enforce policy on the model’s generated responses by filtering profanities and disallowed topics and by returning a consistent blocked message when violations occur.
- For questions that require exact values (such as financial transactions), a text-to-SQL approach reduces the risk of hallucinated numbers by forcing the system to retrieve the answer from the database and to generate...

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
