---
type: reference_note
platform: aws
status: draft
source: udemy-question-51
---

# 51: SageMaker Model Lifecycle Patterns

## Scenario

A fintech team is deploying an open-source LLM behind an Amazon SageMaker AI real-time inference endpoint by using a custom container image in Amazon ECR. The model artifacts in Amazon S3 are very large, and the container must download and load the weights into GPU memory during startup. During deployment, the endpoint repeatedly fails with container health check errors. Logs show the model is still downloading and initializing when the health check fails. Which change will allow the team to deploy the LLM successfully while keeping the same real-time endpoint architecture with the LEAST operational overhead?

## Common implementation patterns

- Replace the real-time endpoint with a SageMaker Asynchronous Inference endpoint and have the application poll Amazon S3 for results. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- Container-based LLM deployments frequently fail for reasons that are uncommon in traditional ML endpoints: large artifacts take longer to download, model initialization can be slower due to GPU memory setup, and the...
- The most direct, low-overhead fix is to adjust the endpoint’s startup health check and model download timeout settings so the container can complete model loading before SageMaker evaluates it as unhealthy.
- Alternatives either change the required real-time interaction model, add significant cost without guaranteeing success, or use a compute environment that is not appropriate for large LLM inference.

## Domain

- Content Domain 2: Implementation and Integration
