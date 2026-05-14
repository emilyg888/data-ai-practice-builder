---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-57
completeness: full
---

# 57: Implementation Patterns

## Scenario

A global company is building a multilingual customer service AI assistant by using Amazon Bedrock. The company has fine-tuned multiple Amazon Bedrock FMs, each for a different support topic. For example, billing-related queries must route to a model that is fine-tuned for finance. Technical troubleshooting queries must route to a model that is fine-tuned for product diagnostics. All incoming messages are processed through an Amazon API Gateway API. The company wants to build an event-driven solution that handles routing logic and is scalable. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Train a custom Amazon Comprehend classification model. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call Amazon Comprehend custom classification to identify the topic of the query. Route the request to the...

## Common anti-patterns

- Avoid configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call Amazon Comprehend to detect the dominant language of the query. Route the request to the appropriate Amazon Bedrock model based on the detected language....
- Avoid fine-tune an FM in Amazon Bedrock for topic classification. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to invoke the trained FM to determine the topic. Route the request to the appropriate Amazon Bedrock...
- Avoid build and deploy a custom classification model on an inference endpoint in Amazon SageMaker AI. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call the classification inference endpoint to identify the topic...

## Architecture guidance

- You can use Amazon Comprehend custom classification to train a custom model to classify text into labels.
- This solution can detect user-defined categories, such as billing and technical support.
- Amazon Comprehend is fully managed and requires no model hosting.
