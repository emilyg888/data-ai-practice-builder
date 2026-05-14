---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-3
completeness: full
---

# 3: Implementation Patterns

## Scenario

A company is implementing AI governance policies. The policies require all FM interactions to be secured with guardrails. The company configures Amazon Bedrock guardrails. The company must ensure that all InvokeModel and Converse API calls to FMs apply the guardrails. Which solution will enforce guardrail compliance for the API calls in the MOST operationally efficient way?

## Common implementation patterns

- Configure IAM policies for the InvokeModel and Converse API calls with the bedrock:GuardrailIdentifier condition key. Apply the policies to all IAM roles that access the Amazon Bedrock FMs...

## Common anti-patterns

- Avoid configure IAM policies for the InvokeModel and Converse API calls with both bedrock:GuardrailIdentifier and bedrock:PromptRouterArn condition keys. Apply the policies to all IAM roles. Require prompt router validation before allowing access to Amazon Bedrock FMs. because the PromptRouterArn...
- Avoid create an AWS Lambda function that validates and enforces guardrails before proxying requests to Amazon Bedrock. Use the Lambda function as the exclusive endpoint for all FM interactions. because creating a Lambda function to proxy and validate all requests introduces an additional point of...
- Avoid store guardrail identifiers in AWS Systems Manager Parameter Store. Create an AWS Lambda function that retrieves the guardrail identifier from Parameter Store each time before making calls to Amazon Bedrock FMs. because parameter Store provides a centralized location to store guardrail...

## Architecture guidance

- This solution uses IAM policies with the bedrock:GuardrailIdentifier condition key to enforce guardrail compliance for InvokeModel and Converse API calls.
- IAM policies are a centralized and efficient way to control access to AWS resources.
- You can apply the policies to roles that access Amazon Bedrock FMs.
