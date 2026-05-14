---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-53
completeness: full
---

# 53: Implementation Patterns

## Scenario

A company is developing a customer support AI assistant by using Amazon Bedrock FMs. The AI assistant needs to process complex customer inquiries that require detailed analysis and multiple steps to resolve. Currently, users wait for the complete analysis before seeing any response. The delay negatively impacts user satisfaction. The company wants to optimize the user experience by showing progressive responses while performing the analysis. Which solution will meet these requirements with the LEAST development effort?

## Common implementation patterns

- Create an Amazon API Gateway WebSocket API with AWS Lambda integration. Use the Amazon Bedrock InvokeModelWithResponseStream API to stream tokens to connected clients. Configure a Lambda function to handle WebSocket connections and message delivery.

## Common anti-patterns

- Avoid create an AWS AppSync real-time API with AWS Lambda resolvers. Configure a GraphQL schema to stream responses. Use the Amazon Bedrock InvokeModel API and implement subscription resolvers for client updates. because aWS AppSync is a managed GraphQL service that supports...
- Avoid deploy a REST API in Amazon API Gateway. Configure parallel synchronous InvokeModel API calls. Store responses in an Amazon DynamoDB table. Implement client-side polling to check for updates in DynamoDB Streams. because aPI Gateway REST APIs do not support built-in...
- Avoid implement HTTP APIs with AWS Lambda integration. Configure batch processing of responses by using AWS Step Functions. Store partial results in an Amazon DynamoDB table for client retrieval by using scheduled polling. because hTTP APIs with Step Functions batch processing...

## Architecture guidance

- API Gateway WebSocket APIs provide managed, bidirectional communication channels that are suitable to stream data.
- The InvokeModelWithResponseStream API provides token-by-token streaming of model responses.
- Lambda functions can efficiently process the streams and forward tokens through WebSocket connections to clients.
