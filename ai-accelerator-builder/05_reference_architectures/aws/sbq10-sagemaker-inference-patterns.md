---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-10
completeness: partial
---

# 10: SageMaker Inference Patterns

## Scenario

A GenAI developer is implementing a solution to create images from text descriptions. The GenAI developer successfully tested a pre-trained Hugging Face model by using Amazon SageMaker JumpStart. Now, the GenAI developer needs to deploy the model so that users can generate images on demand. The solution must use GPUs for inference. The solution must be able to handle text datasets up to 50 MB with image descriptions. The solution requires responses within 15 minutes. Which deployment strategy will meet these requirements?

## Common implementation patterns

- Deploy a SageMaker Asynchronous Inference endpoint that uses an accelerated computing SageMaker AI instance type. Create an AWS Lambda function for on-demand invocation of the SageMaker AI endpoint to manage image generation.

## Common anti-patterns

- Avoid adding custom infrastructure or manual process steps when a managed AWS capability satisfies the requirement with lower operational overhead.

## Architecture guidance

- SageMaker asynchronous endpoints provide long-running inference workloads with processing times up to 15 minutes.
- Asynchronous endpoints efficiently manage compute resources.
- This deployment strategy supports GPU instances for efficient processing, handles large datasets (up to 1 GB), and provides scaling based on actual usage.
