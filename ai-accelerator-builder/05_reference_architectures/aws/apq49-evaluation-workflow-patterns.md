---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-49
completeness: full
---

# 49: Evaluation Workflow Patterns

## Scenario

A retail company is using Amazon Bedrock to develop a generative AI (GenAI) application that will provide fashion recommendations to customers. The company wants to evaluate the quality of responses from two different FMs to determine which FM provides better fashion advice. Fashion experts who work for the company must perform the evaluations. Which combination of steps will meet these requirements to set up an evaluation process? (Select THREE.)

## Common implementation patterns

- Create an Amazon Cognito user pool to manage the fashion expert workforce. Assign the fashion experts to a work team.
- Create a human-based evaluation job in Amazon Bedrock with custom metrics including "Style Accuracy".

## Common anti-patterns

- Avoid create an Amazon SageMaker Ground Truth labeling job. Specify "AWS/Bedrock/Evaluation" as the AwsManagedHumanLoopRequestSource. because amazon Bedrock uses SageMaker Ground Truth for human workers. However, you do not need to create a labeling job in Ground Truth. Instead,...
- Avoid use Amazon Comprehend to analyze the sentiment of model responses and automatically score responses based on positive fashion experts' feedback. because the company needs human fashion experts to evaluate the models. The company does not need automated sentiment analysis.
- Avoid configure automatic model evaluation with built-in metrics for accuracy and coherence. Set up Amazon CloudWatch to monitor evaluation results. because you can use metrics, such as accuracy, in human evaluations. However, the metrics would be rated by humans, not...

## Architecture guidance

- You must manage human evaluators as a work team.
- You can create a new Amazon Cognito managed work team by using the Amazon Bedrock console.
- For the fashion experts to evaluate the models, you must organize the fashion experts into a work team.
