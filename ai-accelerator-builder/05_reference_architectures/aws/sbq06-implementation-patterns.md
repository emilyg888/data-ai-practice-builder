---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-6
completeness: full
---

# 6: Implementation Patterns

## Scenario

A company is developing an AI assistant that processes customer data by using Amazon Bedrock. The AI assistant has multiple guardrails. The guardrails include prompt injection detection, sensitive information filtering, and denied topic blocking. When a customer query is blocked, a GenAI developer needs a detailed analysis of which specific guardrail rule was invoked and why the content was flagged. Then, the GenAI developer must fine-tune guardrail configurations and distinguish between legitimate customer queries and actual security threats. Which configuration provides the MOST detailed analysis of guardrail decision-making for content filtering?

## Common implementation patterns

- Configure guardrail tracing with `{"trace": "enabled"}` in guardrailConfig. Monitor InvocationsIntervened metrics filtered by the GuardrailPolicyType dimensions: ContentPolicy, TopicPolicy, and SensitiveInformationPolicy.

## Common anti-patterns

- Avoid enable Amazon Bedrock model evaluation with automated evaluation jobs that include guardrail assessment metrics. Configure the evaluation framework to test prompt injection resistance by using company-specific test cases. Use the evaluation dashboard to analyze which guardrail policies are...
- Avoid enable Amazon Bedrock model invocation logging to capture full request and response data. Configure Amazon CloudWatch alarms on InvocationsIntervened metrics filtered by GuardrailContentSource dimensions. Analyze patterns by using CloudWatch Insights queries to identify which content source...
- Avoid configure guardrail tracing with `{"trace": "enabled"}` in guardrailConfig. Monitor InvocationsIntervened metrics filtered by the GuardrailContentSource dimension to identify whether input prompts or output responses triggered interventions. because the GuardrailContentSource dimension can...

## Architecture guidance

- GuardrailPolicyType provides detailed information on which policy intervened in the guardrail.
- The GenAI developer can use this configuration to make an informed decision based on specific metrics.
- Learn more about CloudWatch metrics to monitor Amazon Bedrock guardrails.
