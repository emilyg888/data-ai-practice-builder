---
type: reference_note
platform: aws
status: draft
source: udemy-question-67
---

# 67: Agent Orchestration Patterns

## Scenario

A product team is building an internal chat assistant for customer support agents by using Amazon Bedrock. After launch, the team needs a user-centered way to continuously improve response quality by collecting per-response ratings and optional written feedback, and to later analyze feedback by model and prompt version. The team wants a solution that is serverless and requires the LEAST operational overhead. Which solution will meet these requirements?

## Common implementation patterns

- Add a “Rate this answer” feature in the web UI that calls an Amazon API Gateway REST endpoint. Use an AWS Lambda function to validate the request and store the rating, free-text feedback, and metadata (model ID and prompt version) in an Amazon DynamoDB table...

## Common anti-patterns

- Avoid create an Amazon SageMaker Ground Truth labeling job that sends every assistant response to a human workforce for scoring and annotation. Store the labeled results in Amazon S3 and use the labels to decide which model to use. because while it can...

## Architecture guidance

- A user-centered evaluation mechanism requires collecting explicit feedback from the people using the application (for example, thumbs up/down, star ratings, and optional comments or corrections) and persisting that...
- A serverless feedback endpoint implemented with Amazon API Gateway and AWS Lambda can receive feedback events from the application UI and perform basic validation and enrichment (such as attaching the model ID and...
- Storing these records in Amazon DynamoDB keeps the solution fully managed and scalable with minimal operational burden, while enabling later analysis and continuous improvement cycles based on real user experience.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
