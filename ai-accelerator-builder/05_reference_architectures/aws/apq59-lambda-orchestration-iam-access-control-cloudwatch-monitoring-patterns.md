---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-59
completeness: full
title: 59: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon CloudWatch
related_controls:
  - access_control
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - iam access control
  - lambda orchestration
  - monitoring
  - access control
use_cases:
  - model governance
---

# 59: Knowledge Base Patterns

## Scenario

A GenAI developer must use Amazon Q Business to enhance an internal content management system (CMS) for a company. The company wants users to be able to search, query, and receive AI-assisted insights from the company's data. The company has technical documentation in the CMS and internal knowledge bases with proprietary guidelines. The company has enterprise directory services for authentication, strict role-based access controls (RBAC), and compliance and governance policies for data access. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Configure Amazon Q Business with data source connectors to integrate the CMS and internal knowledge bases. Use AWS IAM Identity Center authentication for RBAC.
- Configure Amazon Q Business data sources with automatic content synchronization and security group mapping for access control.

## Architecture guidance

- Amazon Q Business data source connectors are managed integration points that provide secure connections to external content systems.
- IAM Identity Center is a centralized service to manage user access and permissions across AWS accounts.
- This step uses built-in connectors to integrate content securely.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
