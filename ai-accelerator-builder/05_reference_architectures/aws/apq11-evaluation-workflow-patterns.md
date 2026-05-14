---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-11
completeness: full
---

# 11: Evaluation Workflow Patterns

## Scenario

A company is evaluating multiple FMs in Amazon Bedrock for an AI-powered customer service conversational assistant. The company requires an assessment of response quality and helpfulness. The company requires comprehensive responsible AI metrics including safety evaluations. There are thousands of customer service scenarios that require assessment. The evaluation framework must provide human-like judgment capabilities to assess nuanced aspects of conversational responses. Examples of nuanced aspects include contextual appropriateness and tone that traditional automated metrics cannot adequately measure. The company needs to select the appropriate model based on performance analysis with statistical validation of differences between models. The solution must use managed evaluator models that provide human-like judgment and scale across thousands of scenarios. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Implement an automated evaluation pipeline by using the Amazon Bedrock CreateEvaluationJob API with a consistent evaluator model for all candidate FMs. Use managed evaluator jobs to process scenarios in parallel. Retrieve results from Amazon S3 output locations. Create AWS...

## Common anti-patterns

- Avoid run Amazon Bedrock batch inference jobs to generate responses from all FMs for the customer service scenarios. Run additional batch inference jobs by using a custom LLM-as-a-judge evaluation on the generated outputs. Deploy AWS Lambda functions with Spearman's rank...
- Avoid run Amazon Bedrock batch inference jobs with Amazon Bedrock Guardrails enabled for each FM to generate filtered responses. Monitor InvocationsIntervened metrics using Amazon CloudWatch in the AWS/Bedrock/Guardrails namespace with GuardrailPolicyType and...
- Avoid configure programmatic evaluation jobs by using the Amazon Bedrock CreateEvaluationJob API with a question-answering task type for each FM. Structure evaluation datasets with question and answer pairs in JSONL format. Perform statistical validation of performance...

## Architecture guidance

- The CreateEvaluationJob API with a consistent evaluator model provides a mechanism to run managed evaluation jobs that can scale across large datasets.
- By using a consistent evaluator model, Amazon Bedrock provides human-like judgment on nuanced conversational qualities.
- The qualities include relevance, tone, factual accuracy, and generated built-in responsible AI metrics with confidence intervals.
