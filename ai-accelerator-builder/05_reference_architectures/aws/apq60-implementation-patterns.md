---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-60
completeness: full
---

# 60: Implementation Patterns

## Scenario

An investment company wants to use Amazon Bedrock to summarize complex financial documents. The solution must catalog and manage prompts from the summarization process. The prompts need to be templated with variables for client company names and document content. The solution must provide prompt versioning, a comparison of different versions, and prompt testing before deployment. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create prompts in Amazon Bedrock Prompt Management. Define system instructions that establish the model's role as a financial analyst. Include parameterized variables in the user message template. Use the compare versions feature to test different prompt versions without...

## Common anti-patterns

- Avoid store prompts in Amazon S3 as JSON templates. Use Amazon Bedrock Prompt Management for A/B testing of different prompt versions. Create a custom AWS Lambda function to handle prompt versioning and parameter substitution. Use Amazon CloudWatch to track prompt performance...
- Avoid use Amazon Bedrock Prompt Management to create separate prompts for each financial document type. Implement a naming convention to track prompt versions. Use the compare versions feature to test different prompt versions and to select the highest-performing version for...
- Avoid create prompts in Amazon Bedrock Prompt Management. Define system instructions that establish the model's role as a financial analyst. Use prompt templates with parameterized variables for client company names and document content. Test each version by deploying the...

## Architecture guidance

- Prompt Management provides a centralized service to store, catalog, and manage prompts.
- Prompt Management supports parameterized templates with variables and system instructions to control the model's role and tone.
- This solution offers built-in capabilities for prompt versioning, testing, and deployment without requiring custom infrastructure.
