---
type: reference_note
platform: aws
status: draft
source: udemy-question-7
---

# 7: Serverless Integration Patterns

## Scenario

A healthcare SaaS provider exposes an internal GenAI summarization service through Amazon API Gateway and an AWS Lambda function that invokes an Amazon Bedrock text model. The provider expects to switch between different Bedrock models over time as pricing and regional availability change. The provider must be able to change the model selection without modifying or redeploying the Lambda code, and must be able to roll out a model change gradually with the ability to roll back automatically if errors increase. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use AWS AppConfig to store a configuration profile (for example, a feature flag) that contains the Bedrock modelId and inference settings. Configure the Lambda function to retrieve the AppConfig configuration at runtime and invoke Bedrock based on the...

## Common anti-patterns

- Avoid configure Amazon API Gateway stage variables to store the Bedrock modelId and use a mapping template to pass the stage variable to the Lambda function for each request. Update the stage variable when switching models. because although stage variables...

## Architecture guidance

- A flexible model-selection pattern separates the model choice from the application code so the team can switch FMs or providers without a code redeploy.
- AWS AppConfig is purpose-built for dynamic configuration management and supports validating configuration changes, deploying changes progressively, and rolling back when CloudWatch alarms indicate problems.
- By having the Lambda function retrieve model selection parameters from AppConfig at runtime, the API remains stable while the modelId and related settings can be changed safely and repeatedly with minimal operational...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
