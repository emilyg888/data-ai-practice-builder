---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-4
completeness: full
---

# 4: SageMaker Deployment Patterns

## Scenario

A GenAI developer deployed a fine-tuned LLM to an Amazon SageMaker AI endpoint. The GenAI developer used the default serving configuration for continuous batching with the AMI including the Deep Java Library (DJL). The model is being served on GPU-based Amazon EC2 instances, each with 8 GPUs. As the model scales to production, the GenAI developer discovers that many instances are needed to meet traffic demands. The GenAI developer wants to avoid increased costs from the overutilization. The GenAI developer analyzes logs. The GenAI developer discovers that the maximum I/O sequence length in real requests is 10 times smaller than what the model was originally configured to handle. Additionally, the current concurrency for each instance is low. Profiling shows that the model’s weights and activations can fit entirely within 4 GPUs. Which combination of steps can the GenAI developer take to improve resource utilization? (Select TWO.)

## Common implementation patterns

- Reduce the model’s maximum sequence length to provide a higher rolling batch size for each GPU.
- Use tensor parallelism with a degree of 4 to deploy two model replicas for each instance.

## Common anti-patterns

- Avoid increase the number of SageMaker AI instances and spread requests more evenly to reduce the load for each instance. because sageMaker AI supports auto scaling based on user demand. However, increasing the number of instances does not improve concurrency or decrease the GPU memory footprint....
- Avoid enable speculative decoding to reduce response latency for each request. because sageMaker AI supports inference optimization through speculative decoding. This technique can speed up the decoding process of large LLMs by using draft models. Speculative decoding improves latency, not resource...
- Avoid split the model across all 8 GPUs by using a tensor parallelism degree of 8 to improve memory efficiency. because you can indicate the tensor parallelism degree to use. Using a tensor parallelism degree of 8 would restrict the instance to serving only one model replica across all 8 GPUs. The...

## Architecture guidance

- DJL is an open source, high-level deep learning framework.
- You can use DJL to streamline the process of building and deploying deep learning models.
- You can deploy models on SageMaker AI with DJL serving.
