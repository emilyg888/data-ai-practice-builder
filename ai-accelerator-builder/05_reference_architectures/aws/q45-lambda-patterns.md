---
type: reference_note
platform: aws
status: draft
source: udemy-question-45
---

# 45: Throughput Patterns

## Scenario

A media analytics team uses Amazon Bedrock to generate short summaries for hundreds of thousands of customer call transcripts every night. A Lambda function currently reads each transcript from Amazon S3 and invokes the model one request at a time. The team is frequently throttled during the batch window and the job does not finish by morning. The summaries can be generated asynchronously, and the output must be stored in Amazon S3 for downstream processing. Which solution will increase throughput for this workload MOST cost-effectively?

## Common implementation patterns

- Use Amazon Bedrock batch inference by writing the prompts to an input file in Amazon S3, submitting a batch inference job, and storing the batch output in Amazon S3 for downstream processing. This is the managed or lower-overhead approach called out as...

## Common anti-patterns

- Avoid put Amazon API Gateway in front of the Lambda function and enable API Gateway caching to reduce repeated model invocations for similar transcripts. because aPI caching is effective when identical requests repeat and responses can be reused. In...

## Architecture guidance

- For large, offline GenAI workloads, optimizing throughput is primarily about reducing per-request overhead and efficiently managing how many model invocations are executed.
- Amazon Bedrock batch inference is intended for this pattern: prompts are placed in Amazon S3, a batch job processes them at scale, and the results are delivered back to Amazon S3 for later consumption.
- Approaches that rely on scaling Lambda concurrency or adding an API layer still generate a large number of individual invocations, which can amplify throttling and increase operational complexity.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
