---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-25
completeness: full
---

# 25: Guardrails Patterns

## Scenario

A media company is building an AI-powered content moderation system by using an FM in Amazon Bedrock. The system requires immediate detection and prevention of sensitive information and policy violations. Text and image content should not contain personally identifiable information (PII), misinformation, hate speech, and unsafe content. The solution must stop text and image content that violates these policies before the content reaches the editorial review process. The company's compliance framework requires comprehensive documentation of FM limitations and biases with proper version control. Additionally, the policy requires event-driven monitoring that invokes automated compliance validation workflows within seconds of guardrail intervention. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure Amazon Bedrock Guardrails with content filters for PII, misinformation, hate speech, and unsafe multimodal content. Document FM biases and limitations in standardized model cards with versioning enabled in Amazon S3. Configure an Amazon CloudWatch alarm to monitor the...

## Common anti-patterns

- Avoid configure Amazon Bedrock Guardrails with content filters for PII, misinformation, hate speech, and unsafe multimodal content. Store model card documentation in Amazon S3 with lifecycle policies enabled. Create Amazon EventBridge rules to invoke AWS Lambda functions that...
- Avoid set up Amazon Comprehend for PII detection and sentiment analysis on user-generated content. Pass the content to Amazon Bedrock. Configure Amazon Bedrock Guardrails with content filters for misinformation, hate speech, and unsafe multimodal content. Maintain comprehensive...
- Avoid configure Amazon Bedrock Guardrails with content filters for PII, misinformation, hate speech, and unsafe multimodal content. Integrate Amazon Rekognition content moderation with custom trained models for enhanced visual content analysis and bulk processing capabilities....

## Architecture guidance

- Guardrails provide built-in content filtering capabilities for text and multimodal content.
- Guardrails provide immediate detection and prevention of policy violations with minimal setup.
- This solution uses Amazon S3 for version-controlled model card documentation.
