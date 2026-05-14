---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-72
completeness: full
---

# 72: RAG Patterns

## Scenario

A large social media company runs multiple RAG pipelines across different applications. Each pipeline uses an FM embedding endpoint deployed on an Amazon SageMaker AI real-time endpoint. A GenAI developer uses the endpoint to generate embeddings. The GenAI developer stores the embeddings in multiple vector databases. The production applications use the vector databases to drive document retrieval for downstream generation and to provide users with content. Recently, multiple users report that the response relevance has been poor. New writing styles are appearing more frequently. The GenAI developer wants to determine if the input drift is degrading embedding quality. The GenAI developer must prepare the model for re-training without disrupting production traffic. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Schedule SageMaker Model Monitor with a custom Amazon ECR image. Compute all the drift metrics between the endpoint captured data and the baseline training dataset used by the model. Store the final violation reports in Amazon S3.
- Create a new SageMaker AI endpoint configuration based on the production variant with Data Capture enabled. Use the UpdateEndpoint API to shift endpoint traffic to the new endpoint with the updated configuration. Parse captured data in SageMaker Model Monitor to investigate.

## Common anti-patterns

- Avoid create a new SageMaker AI endpoint with Data Capture enabled. Shift all production traffic to the new endpoint. Delete the previous endpoint. Parse captured data in SageMaker Model Monitor to investigate. because data Capture is a SageMaker AI feature that you can use to...
- Avoid schedule SageMaker Model Monitor jobs by using SageMaker Clarify to improve visibility into potential bias. Store the final violation reports in Amazon S3. because you can use Clarify to detect and mitigate bias in models. Clarify provides model explainability. Clarify...
- Avoid change all RAG pipelines to use an Amazon Bedrock Titan Embeddings model endpoint. Enable model invocation logging. Select embedding as the data type to capture. Set up logs to publish to Amazon S3. because you can use the Amazon Bedrock invocation logging feature to...

## Architecture guidance

- Model Monitor is a fully managed service that provides continuous monitoring of production ML models.
- Model Monitor runs scheduled jobs by using custom images.
- This approach can compute embedding-level drift metrics by comparing captured inference data (the data capture logs) against a baseline dataset.
