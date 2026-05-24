---
type: reference_note
platform: aws
status: draft
source: udemy-question-22
title: 22: Bedrock Data Automation Workflow for Insurance Claims Intake
pattern_family: lambda_orchestration
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon Bedrock Data Automation
  - Amazon S3
related_controls:
topics:
  - bedrock data automation workflow
  - insurance claims intake
  - lambda orchestration
  - step functions
  - bedrock
  - bedrock data automation
  - s3 data assets
use_cases:
  - claims processing
  - multimodal extraction
  - routing and orchestration
---

# 22: Bedrock Data Automation Workflow for Insurance Claims Intake

## Pattern summary

Trigger a Step Functions workflow from S3 uploads and invoke Bedrock Data Automation asynchronously to extract structured fields from claims PDFs and images.

## Scenario

A regional insurance provider wants to improve its claims handling workflow. Claims adjusters upload scanned PDFs and images (for example, incident photos and handwritten forms) to an Amazon S3 bucket from an internal web portal. The provider needs to extract a consistent set of fields (such as policy number, claimant name, and claim amount) into structured JSON, then update the corresponding record in an external CRM system by using an API call. The solution must be serverless and require the LEAST operational overhead as document formats evolve. Which solution will meet these requirements?

## Common implementation patterns

- Configure an S3 event notification to start an AWS Step Functions workflow. In the workflow, invoke Amazon Bedrock Data Automation asynchronously by using a project that contains blueprints for the required fields. After the job completes, have a Lambda...

## Architecture guidance

- The lowest-overhead serverless design is to orchestrate an asynchronous document-processing workflow that uses a managed extraction service purpose-built for multimodal inputs and structured outputs.
- Amazon Bedrock Data Automation can extract structured JSON from PDFs and images and can be configured with blueprints to define and evolve the required fields.
- AWS Step Functions provides reliable workflow orchestration (including waiting for asynchronous completion), and AWS Lambda can apply the extracted results by calling the CRM API.

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

## Domain

- Content Domain 2: Implementation and Integration
