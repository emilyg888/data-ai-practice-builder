---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-50
completeness: full
---

# 50: Implementation Patterns

## Scenario

A startup company is building a general-purpose generative AI (GenAI) assistant to handle customer questions for a variety of use cases. The company builds the GenAI assistant by using Amazon Bedrock FMs. The company wants to implement a query-routing mechanism based on the complexity of the query. Simple queries should route to a small Meta Llama model. Complex queries should route to a large Anthropic Claude model. For example, complex queries require generating creative responses or in-depth explanations. The solution must be scalable and able to maintain low-latency responses. Which solution will meet these requirements?

## Common implementation patterns

- Use an AWS Lambda function to invoke a small Amazon Bedrock model by using the query. In the system prompt, instruct the model to determine if the query is complex and reply only if the query is too complex. When the model response returns to the Lambda function, inspect the...

## Common anti-patterns

- Avoid configure an Amazon Bedrock intelligent prompt router for the Llama and Claude models. Set a fallback model with a reliable baseline. Test the router by using different response quality differences between the models. Use an AWS Lambda function to invoke the configured...
- Avoid create an Amazon Bedrock knowledge base to store query patterns and complexity indicators. Configure an AWS Lambda function to first check the knowledge base to determine query complexity and then route to the appropriate model based on the complexity assessment. because...
- Avoid create an AWS Step Functions workflow that first invokes an AWS Lambda function. Configure the function to analyze query length, keyword presence, and structural complexity by using regex patterns. Configure the workflow to route the query to either the small Llama model...

## Architecture guidance

- Model cascading through sequential model invocation provides an efficient way to handle query complexity.
- First, you can use a small model to determine complexity and then invoke the larger model only when necessary.
- This solution optimizes both cost and performance.
