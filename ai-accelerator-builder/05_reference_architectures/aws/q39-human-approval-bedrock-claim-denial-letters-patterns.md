---
type: reference_note
platform: aws
status: draft
source: udemy-question-39
title: 39: Human Approval Workflow for Bedrock Claim Denial Letters
pattern_family: lambda_orchestration
aws_services:
  - AWS Step Functions
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - model_evaluation
  - retrieval_grounding
topics:
  - human approval workflow
  - bedrock claim denial letters
  - lambda orchestration
  - step functions
  - api gateway
  - bedrock
  - state store
  - model evaluation
  - retrieval grounding
  - human approval
use_cases:
  - internal assistant
  - claims processing
  - routing and orchestration
---

# 39: Human Approval Workflow for Bedrock Claim Denial Letters

## Pattern summary

Use API Gateway, Step Functions, Bedrock, DynamoDB, and notifications to require adjuster approval before claim denial letters are sent.

## Scenario

An insurance company is building an internal GenAI assistant that drafts claim denial letters by using an Amazon Bedrock FM. Company policy requires a licensed adjuster to review and approve (or edit) each draft before the letter is sent to a customer. The company also wants to capture the adjuster’s rating and final approved text for later analysis. Review times can vary from minutes to hours. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon API Gateway to accept the request and start an AWS Step Functions state machine. The state machine invokes the Amazon Bedrock FM to create a draft, stores the draft and status in Amazon DynamoDB, notifies adjusters (for example, through Amazon...

## Architecture guidance

- A human-in-the-loop design needs an explicit approval step, durable storage of the draft and the reviewer’s edits/ratings, and orchestration that can span variable human response times.
- A managed workflow service can coordinate the end-to-end process: generate the draft with the FM, route it to a reviewer for approval, and continue only after the review is complete.
- Exposing a dedicated feedback endpoint simplifies collecting structured reviewer decisions and ratings, and storing this information in a low-maintenance database enables traceability and later evaluation.

## AWS documentation validation

- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html

## AWS-supported alternative patterns

- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
