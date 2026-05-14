---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-48
completeness: full
---

# 48: Implementation Patterns

## Scenario

A large ecommerce company is developing a customer service AI-powered chat assistant by using Amazon Bedrock. The company needs the chat assistant to be able to support both simple product questions and more complex reasoning tasks. Simple product questions are 80% of the queries. Complex reasoning tasks are 20% of the queries. The solution must be cost-effective and require minimal operational overhead while maintaining response quality. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock intelligent prompt routing. Use Anthropic Claude Haiku as the primary model. Use Claude Sonnet as the fallback model. Configure the routing policy to send simple queries to Claude Haiku and to send complex queries to Claude Sonnet.

## Common anti-patterns

- Avoid configure Amazon Bedrock with provisioned throughput for an Anthropic Claude Sonnet model to handle all queries. Implement response caching using Amazon ElastiCache (Redis OSS) to store frequent responses with 24-hour TTL. Use Amazon CloudWatch metrics to monitor cache hit...
- Avoid create a custom caching layer using Amazon DynamoDB with TTL enabled for response storage. Use AWS Lambda with semantic similarity scoring to pre-process queries and match against cached responses with a 0.95 similarity threshold. Invoke Anthropic Claude Sonnet through...
- Avoid use a single Anthropic Claude Sonnet model deployment with optimized prompt templates for both simple and complex queries. Implement context windowing to limit token usage to 4K tokens for simple queries and to allow up to 8K tokens for complex reasoning tasks. Use Amazon...

## Architecture guidance

- Amazon Bedrock intelligent prompt routing provides dynamic model selection based on query characteristics.
- Using Claude Haiku for simple product questions provides faster, more cost-effective processing.
- Routing complex reasoning tasks to Claude Sonnet ensures high-quality responses for sophisticated queries.
