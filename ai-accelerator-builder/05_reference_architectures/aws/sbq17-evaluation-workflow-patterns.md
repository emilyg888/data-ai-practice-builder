---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-17
completeness: full
---

# 17: Evaluation Workflow Patterns

## Scenario

A company is implementing a systematic evaluation process for a newly deployed FM in Amazon Bedrock. The company wants to replace an existing model in production with a new model. The change to the new model is dependent on the new model demonstrating better performance than the existing model. The company must follow a sequential validation process. To ensure evaluation rigor, each step must be reviewed and approved before proceeding to the next step. Select and order each step from the following list to implement the evaluation workflow. Select each step one time. (Select and order FIVE.) Analyze the results and generate a comprehensive evaluation report. Conduct A/B testing to compare the new model against the existing production model. Create a test dataset with diverse scenarios and edge cases. Define evaluation metrics for relevance, factual accuracy, and fluency. Implement automated quality gates by using AWS Step Functions.

## Common implementation patterns

- Define evaluation metrics for relevance, factual accuracy, and fluency. This step is part of the endorsed evaluation sequence and should be executed in order.
- Create a test dataset with diverse scenarios and edge cases. This step is part of the endorsed evaluation sequence and should be executed in order.
- Conduct A/B testing to compare the new model against the existing production model. This step is part of the endorsed evaluation sequence and should be executed in order.
- Implement automated quality gates by using AWS Step Functions. This step is part of the endorsed evaluation sequence and should be executed in order.
- Analyze the results and generate a comprehensive evaluation report. This step is part of the endorsed evaluation sequence and should be executed in order.

## Common anti-patterns

- Avoid starting A/B testing before defining evaluation metrics and building an approved test dataset.
- Avoid generating final approval reports before automated quality gates and validation checkpoints have completed.
- Avoid treating evaluation as an unstructured activity; sequence control is part of the architecture, not just process documentation.

## Architecture guidance

- Sequential validation and approval provides a rigorous evaluation process where each step builds upon validated components of the previous steps.
- This sequential workflow is essential to maintain evaluation rigor.
- You can use this approach to make an informed decision about model replacement.
