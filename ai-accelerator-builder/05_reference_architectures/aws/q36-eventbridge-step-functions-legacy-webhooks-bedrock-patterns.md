---
type: reference_note
platform: aws
status: draft
source: udemy-question-36
title: 36: EventBridge and Step Functions Bridge from Legacy Webhooks to Bedrock
pattern_family: lambda_orchestration
aws_services:
  - AWS Step Functions
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon EventBridge
  - Amazon S3
related_controls:
  - audit_logging
topics:
  - eventbridge step functions bridge from legacy webhooks to bedrock
  - lambda orchestration
  - step functions
  - api gateway
  - bedrock
  - event orchestration
  - s3 data assets
  - audit logging
use_cases:
  - document summarization
  - real-time streaming
  - routing and orchestration
---

# 36: EventBridge and Step Functions Bridge from Legacy Webhooks to Bedrock

## Pattern summary

Land webhook payloads in S3, use EventBridge to start Step Functions, call Bedrock for summarization, and write outputs for downstream systems.

## Scenario

A logistics company operates a legacy on-premises shipment tracking system that can send HTTPS webhooks but cannot use AWS SDKs. The company wants to add an Amazon Bedrock FM step that summarizes shipment exception notes and stores the summaries for downstream applications. During shift changes, exception events arrive in large bursts. The on-premises system must receive an immediate acknowledgment and must not be tightly coupled to Bedrock availability. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store exception notes in an Amazon S3 bucket from the on-premises system. Configure Amazon EventBridge to detect new objects and invoke an AWS Step Functions workflow that calls Amazon Bedrock and writes results back to the on-premises database. This is the...

## Architecture guidance

- The key enterprise connectivity requirement is to integrate a legacy HTTPS webhook producer while keeping the FM invocation loosely coupled and resilient to burst traffic.
- Using an HTTPS front door with API Gateway allows the legacy system to send standard web requests and receive immediate acknowledgment.
- Placing SQS between ingestion and inference provides durable buffering and decoupling, so downstream processing can scale independently and tolerate temporary slowdowns or throttling.

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

## Domain

- Content Domain 2: Implementation and Integration
