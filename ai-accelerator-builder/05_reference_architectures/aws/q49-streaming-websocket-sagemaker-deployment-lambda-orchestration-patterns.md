---
type: reference_note
platform: aws
status: draft
source: udemy-question-49
title: 49: Throughput Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon S3
  - Amazon SageMaker
related_controls:
  - model_evaluation
  - monitoring
  - prompt_policy
topics:
  - throughput patterns
  - bedrock agents
  - lambda orchestration
  - api gateway
  - bedrock
  - s3 data assets
  - sagemaker
  - model evaluation
  - monitoring
  - prompt policy
  - evaluation
use_cases:
  - document summarization
  - cost optimization
  - real-time streaming
---

# 49: Throughput Patterns

## Scenario

A media streaming provider uses an API Gateway endpoint backed by an AWS Lambda function to call an Amazon Bedrock FM that generates podcast episode summaries. The team wants to reduce cost by switching to a smaller FM and tuning inference parameters (for example, temperature and max token limits). Before rollout, the team must verify summary quality does not regress, quantify the latency-to-quality and cost-to-quality tradeoffs, and introduce the new configuration to production traffic gradually with an easy rollback path. Which combination of steps should the team take to meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Deploy two AWS Lambda versions behind a single alias: one version calling the existing FM configuration and one version calling the candidate configuration. Use AWS CodeDeploy canary deployments to shift a small percentage of production traffic to the...
- Create a prompt dataset in Amazon S3 that includes representative transcripts (or excerpts) and reference summaries. Run Amazon Bedrock Model Evaluations across multiple candidate FMs and parameter configurations by using an LLM-as-a-judge. Use Amazon...

## Architecture guidance

- A systematic evaluation approach should first compare candidate foundation models and inference parameter settings on a consistent prompt dataset, using an evaluation method that produces repeatable quality scores.
- Then, the team should validate the chosen configuration under real production conditions with a controlled rollout mechanism that supports quick rollback.
- Amazon Bedrock Model Evaluations enables structured, repeatable multi-model and multi-configuration testing using a prompt dataset, and it can be paired with operational metrics (token counts and latency) to calculate...

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
