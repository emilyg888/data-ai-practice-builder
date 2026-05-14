---
type: reference_note
platform: aws
status: draft
source: udemy-question-66
---

# 66: Implementation Patterns

## Scenario

A logistics software provider runs an order-tracking platform on AWS that integrates with multiple internal microservices. A shipping partner sends signed HTTPS webhooks whenever a delivery exception occurs. The provider wants to add GenAI functionality that uses an Amazon Bedrock FM to generate a short, customer-ready message and then deliver the generated message to both a case-management service and a notification service. The webhook endpoint must acknowledge requests within 2 seconds, and the provider must be able to add additional downstream consumers later without changing the webhook handler code. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon API Gateway to receive the webhook and invoke a single AWS Lambda function that validates the webhook signature, calls Amazon Bedrock, calls the case-management and notification microservice APIs, and then returns a response to the webhook sender....

## Common anti-patterns

- Avoid use Amazon API Gateway to start an AWS Step Functions workflow that validates the webhook signature, invokes Amazon Bedrock, and calls both microservice APIs. Configure the workflow to return the result to API Gateway after all steps complete. because...

## Architecture guidance

- The key design requirement is to enhance an existing application by integrating GenAI while keeping the inbound webhook path fast and keeping downstream integrations loosely coupled.
- A managed webhook endpoint can be implemented with Amazon API Gateway, while AWS Lambda is appropriate for webhook handling tasks like HMAC signature validation and request normalization.
- Publishing the validated event to Amazon EventBridge decouples the webhook handler from downstream processing.

## Domain

- Content Domain 2: Implementation and Integration
