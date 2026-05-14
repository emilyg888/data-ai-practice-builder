---
type: reference_note
platform: aws
status: draft
source: udemy-question-42
---

# 42: SageMaker Model Lifecycle Patterns

## Scenario

An insurance technology team is building an interactive claims assistant. An AWS Lambda function reads a user’s conversation history from Amazon DynamoDB and streams responses from an Amazon Bedrock text model by using the ConverseStream API. The same Lambda function also invokes a custom text-classification model deployed on an Amazon SageMaker AI real-time endpoint to label each new user message before it is stored. After a refactor, Bedrock returns a validation error indicating required fields are missing, and SageMaker returns a JSON parsing error. The team wants to correct the input formatting for both inference calls with the LEAST additional development effort. Which solution will meet these requirements?

## Common implementation patterns

- In the Lambda function, format the Bedrock request body as a ConverseStream messages structure that includes a messages array with role and content fields for each turn. Separately, send a SageMaker InvokeEndpoint request with a JSON body that matches the...

## Common anti-patterns

- Avoid change the Lambda function to concatenate the full conversation history into a single plain-text prompt and invoke the Bedrock InvokeModelWithResponseStream API. Send the same plain-text payload to the SageMaker endpoint for classification. because...

## Architecture guidance

- The key fix is to format inference inputs according to each target’s required schema.
- For Amazon Bedrock conversational inference, the Converse/ConverseStream APIs expect a structured JSON conversation format that explicitly represents each turn with role and content fields.
- For Amazon SageMaker AI endpoints, the model container defines the request schema, and SageMaker does not automatically adapt a Bedrock-style conversation payload; the application must construct the exact JSON shape...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
