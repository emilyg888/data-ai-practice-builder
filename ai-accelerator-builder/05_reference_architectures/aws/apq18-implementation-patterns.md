---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-18
completeness: full
---

# 18: Implementation Patterns

## Scenario

A digital content company is building a generative AI (GenAI) application that summarizes news articles. The application needs to route requests to different LLMs based on language and content types. For regulatory compliance, certain content types must use specific model providers. A GenAI developer must create a solution that can switch between model providers without code changes. The model providers include Amazon Bedrock and third-party APIs. The solution must securely store API keys and maintain consistent response formatting regardless of the underlying model. The solution must optimize costs by using cached responses when appropriate. Which solution will meet these requirements?

## Common implementation patterns

- Create a single Amazon API Gateway REST API with non-proxy integrations. Configure mapping templates to transform requests and responses for each model provider. Use header-based routing that directs traffic to store endpoint URLs based on content type and stage variables. Use...

## Common anti-patterns

- Avoid create separate Amazon API Gateway REST APIs for each model provider with unique endpoints. Use a client-side routing application to determine which API endpoint to call based on language and content type. Store API keys in client-side code. Cache responses at the client...
- Avoid create a single Amazon API Gateway REST API with an AWS Lambda proxy integration. Configure routing logic in the Lambda function to select the appropriate model based on request parameters. Store API keys in AWS Secrets Manager. Configure the function to retrieve the...
- Avoid deploy all models to Amazon SageMaker AI endpoints. Create a single Amazon API Gateway REST API with a SageMaker AI integration. Use path parameters to determine which SageMaker AI endpoint to invoke. Add model metadata to SageMaker AI endpoints to ensure consistent...

## Architecture guidance

- API Gateway non-proxy integrations with mapping templates provide request and response transformation without code changes.
- You can combine header-based routing with stage variables for dynamic provider selection.
- Mapping templates ensure consistent response formatting across different providers.
