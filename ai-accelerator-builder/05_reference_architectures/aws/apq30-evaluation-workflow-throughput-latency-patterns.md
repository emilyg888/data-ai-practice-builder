---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-30
completeness: full
title: 30: Evaluation Workflow Patterns
pattern_family: prompt_management
aws_services:
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - model_evaluation
  - prompt_policy
topics:
  - evaluation workflow patterns
  - prompt management
  - bedrock
  - s3 data assets
  - model evaluation
  - prompt policy
  - evaluation
use_cases:
  - routing and orchestration
---

# 30: Evaluation Workflow Patterns

## Scenario

A GenAI developer wants to evaluate FMs by using the automatic model evaluation feature in Amazon Bedrock. The GenAI developer creates a comprehensive custom prompt dataset that contains 5,000 curated prompts. The prompts cover various business scenarios for a text classification task. The GenAI developer uploads the dataset to Amazon S3 in JSONL format. The GenAI developer attempts to create an evaluation job. However, the evaluation job fails to start. The error indicates an issue with the dataset configuration. Which approach will resolve this issue?

## Common implementation patterns

- Split the dataset into multiple smaller datasets with a maximum of 1,000 prompts each. Run separate evaluation jobs.

## Architecture guidance

- Amazon Bedrock automatic model evaluation jobs have a quota of 1,000 prompts for each dataset.
- The 5,000-prompt dataset exceeds the quota and causes the job to fail.
- You can split the prompts into smaller datasets such as five datasets of 1,000 prompts each.

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
