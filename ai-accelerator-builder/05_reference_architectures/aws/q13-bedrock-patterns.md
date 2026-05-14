---
type: reference_note
platform: aws
status: draft
source: udemy-question-13
---

# 13: Throughput Patterns

## Scenario

An online retailer is building a customer-facing chat experience that uses Amazon Bedrock LLMs. The team wants to route each user message to a low-latency model for simple requests and to a higher-quality model for complex requests. During traffic spikes, the higher-quality model occasionally experiences throttling, and the team wants requests to automatically fall back to the low-latency model when throttling or high latency is detected. The team also wants a clear audit trail of how each request was routed. Which solution will meet these requirements with the LEAST custom application logic?

## Common implementation patterns

- Implement all routing in application code inside a single AWS Lambda function. The function calls Amazon Bedrock, checks for throttling errors, retries with exponential backoff, and then calls a different model if throttling persists. Log routing decisions to...

## Common anti-patterns

- Avoid enable Amazon Bedrock cross-Region inference and create an inference profile so Bedrock automatically distributes requests. Use a single modelId in the application and rely on the inference profile to handle both complexity-based model selection and...

## Architecture guidance

- A good model-routing design needs two decision points: determine the best model for the request content (simple vs complex) and determine whether operational conditions require a fallback (for example, throttling or...
- A Step Functions workflow is well-suited to this because it can orchestrate a classification step, branch to specialized model invocations, apply retries and fallback paths, and preserve an end-to-end record of...
- Client-driven routing does not satisfy automatic fallback requirements, a single Lambda-based router increases custom code and reduces structured traceability, and cross-Region inference addresses Regional capacity—not...

## Domain

- Content Domain 2: Implementation and Integration
