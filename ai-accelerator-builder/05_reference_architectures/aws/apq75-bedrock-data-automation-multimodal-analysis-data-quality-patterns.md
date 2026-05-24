---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-75
completeness: full
title: 75: BDA Transformation Patterns
pattern_family: bedrock_data_automation
aws_services:
  - Amazon Bedrock
  - Amazon Bedrock Data Automation
related_controls:
topics:
  - bda transformation patterns
  - bedrock data automation
  - bedrock
use_cases:
  - architecture reference
---

# 75: BDA Transformation Patterns

## Scenario

A company is building a contract analysis system by using intelligent document processing capabilities in Amazon Bedrock. The system uses a blueprint to extract fields, such as AuthorizedSigner, from legal agreements. An example of an extracted value is Mr. John Allen Doe III, Senior Legal Counsel. The company needs to split the fields into the following individual components: TITLE, FIRST_NAME, MIDDLE_NAME, LAST_NAME, SUFFIX, and JOB_TITLE. The company will reuse the structured name format across multiple extracted fields including AuthorizedSigner, WitnessName, and ReviewerName in the pipeline. Which Bedrock Data Automation (BDA) capability will meet these requirements?

## Common implementation patterns

- Use transformation with a reusable custom type to split the AuthorizedSigner field into subcomponents.

## Architecture guidance

- Transformation can split complex fields into structured components.
- For example, transformation can split full names.
- You can use a custom type to define and reuse this structure across fields such as AuthorizedSigner or ReviewerName.

## AWS documentation validation

- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html

## AWS-supported alternative patterns

- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
