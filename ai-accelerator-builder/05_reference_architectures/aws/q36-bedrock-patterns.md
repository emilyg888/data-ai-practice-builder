---
type: reference_note
platform: aws
status: draft
source: udemy-question-36
---

# 36: Implementation Patterns

## Scenario

A logistics company operates a legacy on-premises shipment tracking system that can send HTTPS webhooks but cannot use AWS SDKs. The company wants to add an Amazon Bedrock FM step that summarizes shipment exception notes and stores the summaries for downstream applications. During shift changes, exception events arrive in large bursts. The on-premises system must receive an immediate acknowledgment and must not be tightly coupled to Bedrock availability. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store exception notes in an Amazon S3 bucket from the on-premises system. Configure Amazon EventBridge to detect new objects and invoke an AWS Step Functions workflow that calls Amazon Bedrock and writes results back to the on-premises database. This is the...

## Common anti-patterns

- Avoid configure an Amazon API Gateway REST API that invokes an AWS Lambda function synchronously. In the Lambda function, call the Amazon Bedrock InvokeModel API and return the summary in the API response to the on-premises system. because synchronous...

## Architecture guidance

- The key enterprise connectivity requirement is to integrate a legacy HTTPS webhook producer while keeping the FM invocation loosely coupled and resilient to burst traffic.
- Using an HTTPS front door with API Gateway allows the legacy system to send standard web requests and receive immediate acknowledgment.
- Placing SQS between ingestion and inference provides durable buffering and decoupling, so downstream processing can scale independently and tolerate temporary slowdowns or throttling.

## Domain

- Content Domain 2: Implementation and Integration
