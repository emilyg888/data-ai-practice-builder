---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-11
completeness: full
title: 11: Evaluation Workflow Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
related_controls:
  - model_evaluation
  - monitoring
topics:
  - evaluation workflow patterns
  - bedrock guardrails
  - lambda orchestration
  - bedrock
  - monitoring
  - s3 data assets
  - model evaluation
  - evaluation
  - data quality
use_cases:
  - customer-facing assistant
  - routing and orchestration
---

# 11: Evaluation Workflow Patterns

## Scenario

A company is evaluating multiple FMs in Amazon Bedrock for an AI-powered customer service conversational assistant. The company requires an assessment of response quality and helpfulness. The company requires comprehensive responsible AI metrics including safety evaluations. There are thousands of customer service scenarios that require assessment. The evaluation framework must provide human-like judgment capabilities to assess nuanced aspects of conversational responses. Examples of nuanced aspects include contextual appropriateness and tone that traditional automated metrics cannot adequately measure. The company needs to select the appropriate model based on performance analysis with statistical validation of differences between models. The solution must use managed evaluator models that provide human-like judgment and scale across thousands of scenarios. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement an automated evaluation pipeline by using the Amazon Bedrock CreateEvaluationJob API with a consistent evaluator model for all candidate FMs. Use managed evaluator jobs to process scenarios in parallel. Retrieve results from Amazon S3 output locations. Create AWS...

## Architecture guidance

- The CreateEvaluationJob API with a consistent evaluator model provides a mechanism to run managed evaluation jobs that can scale across large datasets.
- By using a consistent evaluator model, Amazon Bedrock provides human-like judgment on nuanced conversational qualities.
- The qualities include relevance, tone, factual accuracy, and generated built-in responsible AI metrics with confidence intervals.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
