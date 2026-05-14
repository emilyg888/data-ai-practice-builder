---
type: reference_note
platform: aws
status: draft
source: udemy-question-72
---

# 72: Streaming Bedrock Chat Patterns

## Scenario

A real-time customer-service assistant must stream model output to a browser UI, enforce prompt token budgets before invocation, and retry transient model timeouts without forcing the browser to poll.

## Common implementation patterns

- Use Amazon API Gateway WebSocket APIs when the browser needs server-pushed Bedrock output chunks with low latency.
- Put AWS Lambda in the request path to centralize token validation, Bedrock invocation, and retry policy.
- Call the Amazon Bedrock `CountTokens` API before inference when the design requires enforceable prompt-budget checks.
- Use `ConverseStream` or `InvokeModelWithResponseStream` for chunked Bedrock output instead of building a polling workaround.
- Implement bounded exponential-backoff retries in Lambda for transient Bedrock timeout conditions.
- Keep connection state, request metadata, and retry context minimal so the streaming path stays operationally simple.

## Common anti-patterns

- Using string length as a proxy for token count.
- Adding Step Functions and DynamoDB polling for a simple request-response streaming workflow.
- Pushing partial responses into a datastore and forcing the browser to poll every second.
- Assuming API Gateway mapping templates can enforce model token budgets.
- Treating API throttling as a substitute for application-level retry logic.
- Moving token-count logic to CloudFront or Lambda@Edge when the main need is Bedrock-aware validation and retry control.

## Architecture guidance

- Prefer a thin edge and a smart orchestration function for interactive GenAI chat.
- Separate three concerns explicitly: connection management, token-budget enforcement, and Bedrock retry behavior.
- Log token-count checks, retry counts, and stream-abort reasons so operational issues can be diagnosed quickly.
