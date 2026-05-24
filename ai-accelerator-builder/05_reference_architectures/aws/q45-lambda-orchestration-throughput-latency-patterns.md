---
type: reference_note
platform: aws
status: draft
source: udemy-question-45
title: 45: Throughput Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - prompt_policy
topics:
  - throughput patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - s3 data assets
  - prompt policy
use_cases:
  - document summarization
  - cost optimization
  - real-time streaming
---

# 45: Throughput Patterns

## Scenario

A media analytics team uses Amazon Bedrock to generate short summaries for hundreds of thousands of customer call transcripts every night. A Lambda function currently reads each transcript from Amazon S3 and invokes the model one request at a time. The team is frequently throttled during the batch window and the job does not finish by morning. The summaries can be generated asynchronously, and the output must be stored in Amazon S3 for downstream processing. Which solution will increase throughput for this workload MOST cost-effectively?

## Common implementation patterns

- Use Amazon Bedrock batch inference by writing the prompts to an input file in Amazon S3, submitting a batch inference job, and storing the batch output in Amazon S3 for downstream processing. This is the managed or lower-overhead approach called out as...

## Architecture guidance

- For large, offline GenAI workloads, optimizing throughput is primarily about reducing per-request overhead and efficiently managing how many model invocations are executed.
- Amazon Bedrock batch inference is intended for this pattern: prompts are placed in Amazon S3, a batch job processes them at scale, and the results are delivered back to Amazon S3 for later consumption.
- Approaches that rely on scaling Lambda concurrency or adding an API layer still generate a large number of individual invocations, which can amplify throttling and increase operational complexity.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
