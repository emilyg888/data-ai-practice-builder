---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-1
completeness: full
title: 1: Data Quality Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Glue
  - AWS Lambda
  - Amazon Bedrock
  - Amazon EventBridge
  - Amazon S3
  - Amazon SageMaker
related_controls:
  - audit_logging
topics:
  - data quality patterns
  - bedrock agents
  - glue data processing
  - lambda orchestration
  - bedrock
  - event orchestration
  - s3 data assets
  - sagemaker
  - audit logging
  - data quality
use_cases:
  - architecture reference
---

# 1: Data Quality Patterns

## Scenario

A company is implementing a data pipeline to feed customer transaction data into Amazon Bedrock FMs. The company wants to generate personalized recommendations for customers. A GenAI developer wants to avoid data quality issues that could affect model output accuracy. The GenAI developer wants to implement automated data validation before the FMs use the data. The company stores the data in Amazon S3 and catalogs the data in AWS Glue Data Catalog. The solution must detect anomalies and filter out low-quality data before the data reaches the FMs. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Use AWS Glue Data Quality for the data catalog with rule-based validation and anomaly detection. Create an Amazon EventBridge rule to send alerts when quality scores fall below defined thresholds.
- Implement AWS Glue Data Quality for ETL jobs with Data Quality Definition Language (DQDL) rules that validate the data during processing. Configure the job to filter out records that fail validation before passing the data to Amazon Bedrock.

## Architecture guidance

- Data Quality provides both rule-based validation and ML-powered anomaly detection capabilities.
- Data Quality can evaluate data quality against custom rules that are written in DQDL.
- Data Quality can detect anomalies by analyzing data statistics over time.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
