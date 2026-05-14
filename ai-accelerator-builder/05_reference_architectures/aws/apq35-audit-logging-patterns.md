---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-35
completeness: full
---

# 35: Audit Logging Patterns

## Scenario

A GenAI developer builds an application by using Amazon Bedrock. The application summarizes customer feedback from multiple media platforms. Currently, the GenAI developer stores all prompt inputs and generated summaries in Amazon S3 for auditing and analytics. Because of new copyright and compliance policies, the GenAI developer must implement the following governance mechanisms: Maintain an auditable trail for prompt data sources. Log FM usage for auditing purposes. Automatically track prompt lineage and model I/O metadata. Which solution will meet these requirements?

## Common implementation patterns

- Set up Amazon S3 server access logging for all prompt and summary objects. Enable AWS CloudTrail to record Amazon Bedrock API calls. Configure Amazon Bedrock Prompt Management to track template versions and lineage.

## Common anti-patterns

- Avoid store all prompts and summaries in Amazon DynamoDB with metadata fields for model identifiers and timestamps. Enable DynamoDB Streams to send lineage events to Amazon EventBridge for auditing. because dynamoDB can store metadata including model identifiers and timestamps....
- Avoid create AWS Config rules to monitor Amazon S3 buckets that contain prompts and summaries. Create conformance packs to enforce encryption and retention policies. Export rule evaluations to Amazon Athena for auditing. because aWS Config conformance packs are collections of...
- Avoid enable Amazon CloudWatch Logs for Amazon Bedrock model invocations. Set up custom Amazon S3 object tags to capture metadata for each stored prompt and summary. Manage lineage information by using tag policies. because you can use CloudWatch Logs to capture operational...

## Architecture guidance

- S3 server access logging provides detailed records of requests that are made to S3 buckets.
- S3 server access logging provides an auditable trail for prompt data sources.
- CloudTrail captures Amazon Bedrock API activity including model invocations for usage auditing.
