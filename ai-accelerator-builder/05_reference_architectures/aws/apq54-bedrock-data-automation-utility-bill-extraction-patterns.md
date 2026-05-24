---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-54
completeness: full
title: 54: Bedrock Data Automation Blueprints for Utility Bill Extraction
pattern_family: bedrock_data_automation
aws_services:
  - Amazon Bedrock
  - Amazon Bedrock Data Automation
  - Amazon EventBridge
  - Amazon S3
related_controls:
topics:
  - bedrock data automation blueprints
  - utility bill extraction
  - bedrock data automation
  - bedrock
  - event orchestration
  - s3 data assets
use_cases:
  - multimodal extraction
---

# 54: Bedrock Data Automation Blueprints for Utility Bill Extraction

## Pattern summary

Create a Bedrock Data Automation project with one blueprint per utility bill type so recurring PDF bills can be extracted into consistent structured fields.

## Scenario

A real estate company needs to automate the extraction of specific fields from various utility bills in PDF format. The company manages thousands of commercial and residential properties and receives utility bills monthly. The utility bill types include electricity, water, and gas depending on the property location. Each bill type has its own unique format and a predefined set of fields that the company needs to extract. The solution must automatically identify the bill type and extract corresponding information when bills upload to Amazon S3. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock to create a single Bedrock Data Automation (BDA) project that contains multiple blueprints. Create one blueprint for each bill type, including the bill type description and fields to extract. Configure an Amazon EventBridge rule to detect S3 upload events and...

## Architecture guidance

- BDA is a fully managed document processing service that automates the extraction of data from documents by using AI.
- BDA blueprints are templates that define the structure and rules to process specific document types.
- You can use a single project with multiple blueprints to streamline management while maintaining functionality.

## AWS documentation validation

- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html

## AWS-supported alternative patterns

- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
