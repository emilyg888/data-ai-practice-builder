---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-20
completeness: full
---

# 20: Audit Logging Patterns

## Scenario

A financial services company needs to use Amazon Bedrock to create an AI assistant that will help customer support representatives across multiple business units. A GenAI developer must ensure that prompt templates are properly governed through approval workflows. Additionally, the company requires comprehensive logging of all model invocations with a 7-year retention period for regulatory compliance. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Use Amazon Bedrock Prompt Management with multi-stage approval workflows. Use IAM policies that require multi-party authorization.
- Enable Amazon Bedrock model invocation logging with Amazon S3 as the destination. Enable S3 Object Lock with compliance retention mode set to 7 years. Create separate prefixes for each business unit...

## Common anti-patterns

- Avoid store prompt templates in Amazon DynamoDB tables with composite keys partitioned by business units. Implement IAM policies that grant role-based access to business units for template approval. Use DynamoDB item-level permissions to control prompt template modifications and approvals. because...
- Avoid set up Amazon EventBridge rules to capture Amazon Bedrock model invocation events. Route events to Amazon CloudWatch Logs groups that are organized by business unit. Export the logs to Amazon S3. Enable S3 Object Lock with compliance retention mode set to 7 years. because you can use...
- Avoid enable AWS CloudTrail data events for all Amazon Bedrock APIs. Deliver the logs to CloudTrail Lake with a 7-year retention setting. Tag each event with the business unit ID. Run CloudTrail Lake queries to monitor prompt activity. because cloudTrail Lake provides logging capabilities. However,...

## Architecture guidance

- You can use Amazon Bedrock Prompt Management to securely create, parameterize, version, and approve prompt templates within the Amazon Bedrock managed environment.
- This solution provides multi-stage approvals, access roles, version control, and collaboration features that are suitable for diverse business units and complex governance requirements.
- Learn more about Amazon Bedrock Prompt Management.
