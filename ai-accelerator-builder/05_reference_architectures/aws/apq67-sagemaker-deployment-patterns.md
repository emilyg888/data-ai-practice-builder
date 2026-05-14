---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-67
completeness: full
---

# 67: SageMaker Deployment Patterns

## Scenario

A company fine-tunes a Meta Llama model by using proprietary training data in Amazon SageMaker AI. The company stores model weights in Hugging Face format. The company wants to import the model into Amazon Bedrock. The model files include Safetensors weights, configuration files, and tokenizer files. The model files are 45 GB in total size. The company needs a solution to provide a specific level of throughput for production workloads. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Custom Model Import to import the model files from Amazon S3. Deploy the model by using Amazon Bedrock Provisioned Throughput.

## Common anti-patterns

- Avoid use Amazon Bedrock Custom Model Import to import the Hugging Face format model files from Amazon S3. Deploy the model by using on-demand inference. because custom Model Import can import Hugging Face format models from Amazon S3. However, on-demand inference does not...
- Avoid convert the Hugging Face model to Amazon Bedrock format. Use Amazon Bedrock fine-tuning to recreate the model by using the training data. because you do not need to convert Hugging Face models to Amazon Bedrock format. Custom Model Import directly supports Hugging Face...
- Avoid deploy the model directly on SageMaker AI endpoints. Integrate the model with Amazon Bedrock by using custom Amazon API Gateway configurations. because this approach does not use the Custom Model Import feature. This approach would require complex custom integration work....

## Architecture guidance

- Custom Model Import supports importing Llama models in Hugging Face format from Amazon S3.
- For example, the Hugging Face format can include Safetensors weights, config.json files, and tokenizer files.
- After importing the model, the company can purchase Provisioned Throughput to provide dedicated compute capacity and throughput for production workloads.
