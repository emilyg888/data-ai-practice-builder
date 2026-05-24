---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-57
completeness: full
title: 57: Comprehend Classification Router for Fine-Tuned Bedrock Support Models
pattern_family: lambda_orchestration
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon Comprehend
related_controls:
  - audit_logging
topics:
  - comprehend classification router
  - fine-tuned bedrock support models
  - lambda orchestration
  - api gateway
  - bedrock
  - audit logging
use_cases:
  - customer-facing assistant
  - fine tuning
  - routing and orchestration
---

# 57: Comprehend Classification Router for Fine-Tuned Bedrock Support Models

## Pattern summary

Use Amazon Comprehend custom classification in Lambda to classify support topics and route each request to the correct fine-tuned Bedrock model.

## Scenario

A global company is building a multilingual customer service AI assistant by using Amazon Bedrock. The company has fine-tuned multiple Amazon Bedrock FMs, each for a different support topic. For example, billing-related queries must route to a model that is fine-tuned for finance. Technical troubleshooting queries must route to a model that is fine-tuned for product diagnostics. All incoming messages are processed through an Amazon API Gateway API. The company wants to build an event-driven solution that handles routing logic and is scalable. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Train a custom Amazon Comprehend classification model. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call Amazon Comprehend custom classification to identify the topic of the query. Route the request to the...

## Architecture guidance

- You can use Amazon Comprehend custom classification to train a custom model to classify text into labels.
- This solution can detect user-defined categories, such as billing and technical support.
- Amazon Comprehend is fully managed and requires no model hosting.

## AWS documentation validation

- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
