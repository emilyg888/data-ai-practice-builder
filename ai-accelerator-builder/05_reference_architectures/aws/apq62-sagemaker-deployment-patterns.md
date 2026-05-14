---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-62
completeness: full
---

# 62: SageMaker Deployment Patterns

## Scenario

A company deploys an FM to an Amazon SageMaker AI real-time endpoint. Currently the FM serves production traffic for text generation tasks. The company develops a new version of the model with improved accuracy. A GenAI developer must evaluate the new model's operational performance metrics under real production traffic conditions before deploying the model to production. The operational performance metrics include latency, error rates, and resource utilization. The GenAI developer needs to ensure that the new model performs well with actual user requests without impacting end users during the evaluation period. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the new model version to a SageMaker AI shadow test.

## Common anti-patterns

- Avoid deploy the new model to a separate SageMaker AI endpoint and use custom routing. because you can deploy a new model to a separate endpoint for testing without impacting end users. However, you must build and maintain custom routing logic. Therefore, this solution requires...
- Avoid implement A/B testing by configuring production variant weights on the SageMaker AI endpoint. because you can gradually shift traffic between model versions by using A/B testing with production variant weights. However, A/B testing exposes end users to the new model before...
- Avoid use SageMaker Model Monitor to evaluate the new model's performance. because model Monitor is designed to detect data drift and quality issues in deployed models. Model Monitor does not compare operational performance metrics between different model versions under real...

## Architecture guidance

- You can use SageMaker AI shadow tests to deploy a new model variant alongside your production variant on the same endpoint.
- The shadow variant receives a copy of the production traffic but does not return responses to users.
- You can use shadow tests to compare operational metrics including latency, error rates, and resource utilization without any risk to end users.
