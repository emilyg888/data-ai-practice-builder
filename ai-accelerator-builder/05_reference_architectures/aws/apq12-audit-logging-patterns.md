---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-12
completeness: full
---

# 12: Audit Logging Patterns

## Scenario

A large financial services company needs to implement a document processing solution by using generative AI (GenAI). The solution must process mortgage applications that contain sensitive customer information. Each application takes 5–15 minutes to process completely. Each application requires multiple FM calls for information extraction, analysis, and summarization. The solution must handle up to 1,000 concurrent requests during peak hours. The solution must provide audit trails for all AI model interactions. After processing, the results should be available for users to retrieve. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon S3 to store document uploads. Set up S3 Event Notifications to invoke an AWS Lambda function. Configure the Lambda function to invoke an AWS Step Functions standard workflow that orchestrates Amazon Bedrock model calls. Store processing status and results in Amazon...

## Common anti-patterns

- Avoid create an Amazon API Gateway API with AWS Lambda functions that make synchronous calls to Amazon Bedrock for document processing. Store results in Amazon DynamoDB after processing. because aPI Gateway is a fully managed service that you can use to create and manage APIs....
- Avoid create an Amazon Kinesis data stream to receive documents. Use Kinesis consumer AWS Lambda functions to process documents in parallel through Amazon Bedrock APIs. Store results in Amazon OpenSearch Service for retrieval. because amazon Kinesis Data Streams provides...
- Avoid configure Amazon API Gateway with WebSocket APIs to maintain connections while Amazon Bedrock processes documents. Create an AWS Lambda function to send status updates to connected clients. because aPI Gateway WebSocket APIs provide two-way communication between clients...

## Architecture guidance

- Amazon S3 provides scalable, secure object storage for documents.
- S3 Event Notifications can invoke an AWS Lambda function.
- Step Functions standard workflows can run for up to 1 year and maintain detailed execution histories for auditing.
