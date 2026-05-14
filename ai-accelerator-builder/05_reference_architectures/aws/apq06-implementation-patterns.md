---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-6
completeness: full
---

# 6: Implementation Patterns

## Scenario

A financial services company is developing a customer-facing AI assistant to help with customer questions. The AI assistant will use Amazon Bedrock. The company requires the prevention of harmful content, protection against sensitive data leakage, and automatic blocking of illegal content. Which implementation approach will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Guardrails content filters for harmful content detection. Set up Amazon Bedrock word filters to identify potentially illegal content. Implement Amazon Bedrock contextual grounding checks to prevent unauthorized sensitive data leakage.

## Common anti-patterns

- Avoid use Amazon Bedrock Guardrails with topic filters for harmful content detection. Configure Amazon CloudWatch to monitor sensitive data access patterns. Implement content filters to automatically block illegal content and log events for auditing. because guardrails already...
- Avoid use Amazon Bedrock Guardrails with generic safe completion settings for harmful content. Configure Amazon API Gateway with AWS WAF to block illegal content. Create an Amazon CloudWatch alarm that invokes an AWS Lambda function to identify sensitive data leakage. because...
- Avoid use Amazon Bedrock Guardrails content filters for harmful content detection. Use Amazon Bedrock prompts with system instructions to prevent sensitive data leakage. Create an AWS Lambda function to monitor and block illegal content patterns from Amazon Bedrock. because...

## Architecture guidance

- Guardrails provide built-in support to detect harmful content, protect sensitive data, and block illegal content.
- You can configure guardrails with content filters for harmful responses and word filters for prohibited terms.
- You can configure guardrails with contextual grounding checks to reduce hallucinations and prevent the leakage of sensitive data.
