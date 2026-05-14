---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-46
completeness: full
---

# 46: Streaming Patterns

## Scenario

A GenAI developer is implementing a real-time AI assistant application. The application uses Amazon API Gateway WebSocket APIs to stream responses from an AWS Lambda function that calls an Amazon Bedrock FM with response streaming. The application must support connection management, including session state across multi-step interactions, retries, and disconnect cleanup. Which combination of steps will provide this functionality with MINIMAL operational overhead? (Select THREE.)

## Common implementation patterns

- Configure an IAM role for the Lambda function with permissions that include bedrock:InvokeModelWithResponseStream and execute-api:ManageConnections. Add resource ARNs that include the API Gateway WebSocket API ID.
- Set up a WebSocket API in API Gateway with route selection expressions. Integrate the API with a Lambda function that handles connection management and streams responses back to clients using the API Gateway Management API.
- Set up an Amazon DynamoDB table to persist active WebSocket connection IDs and session metadata. Update the table on $connect and $disconnect and use TTL.

## Common anti-patterns

- Avoid create a custom domain name for the WebSocket API. because you can create a custom domain name for production applications. However, you do not need this configuration to enable streaming functionality between Amazon Bedrock and clients. The WebSocket API will work with...
- Avoid configure the Lambda function to use HTTP/1.1 chunked transfer encoding to manually implement response streaming. because you can implement custom HTTP streaming in Lambda by using chunked transfer encoding. However, you do not need this step because Amazon Bedrock already...

## Architecture guidance

- The Lambda function requires specific IAM permissions to both invoke Amazon Bedrock models with streaming and to manage WebSocket connections.
- The resource ARNs must include the specific API Gateway WebSocket API ID to properly scope the permissions.
- You need a WebSocket API in API Gateway to maintain persistent client connections.
