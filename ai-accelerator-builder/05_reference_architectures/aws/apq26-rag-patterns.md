---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-26
completeness: full
---

# 26: RAG Patterns

## Scenario

A GenAI developer is troubleshooting performance issues in a production RAG application. The application is built on Amazon Bedrock. The application uses Amazon OpenSearch Service for vector storage. Users report inconsistent response times. Some queries are taking significantly longer than others. The GenAI developer must implement a monitoring solution that provides comprehensive diagnostic information to identify the root cause of the issue. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create a custom Amazon CloudWatch dashboard that combines context retrieval latency metrics with OpenSearch Service operation counts. Analyze Amazon Bedrock invocation logs to identify which knowledge base queries are experiencing degraded performance.

## Common anti-patterns

- Avoid create custom Amazon CloudWatch metrics that combine OpenSearch Service vector search latency and Amazon Bedrock token usage patterns. Set up composite alarms that correlate high latency with vector similarity thresholds and token consumption rates. because you can use...
- Avoid set up detailed monitoring in OpenSearch Service and Amazon Bedrock. Create Amazon CloudWatch metric math expressions to analyze the correlation between vector search performance and model inference times. Set up anomaly detection on the combined metrics. because metric...
- Avoid implement distributed tracing through AWS X-Ray that focuses on OpenSearch Service vector query latency and Amazon Bedrock model response times. Create custom subsegments for vector similarity calculations and token processing to identify specific performance bottlenecks....

## Architecture guidance

- CloudWatch dashboards provide a customizable view of metrics and alarms.
- CloudWatch dashboards provide a visual correlation of data from multiple sources.
- You can combine context-retrieval latency metrics from OpenSearch with operation counts to find a direct correlation between vector search performance and overall response times.
