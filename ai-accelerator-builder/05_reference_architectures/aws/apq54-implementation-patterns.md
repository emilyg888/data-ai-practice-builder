---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-54
completeness: full
---

# 54: Implementation Patterns

## Scenario

A real estate company needs to automate the extraction of specific fields from various utility bills in PDF format. The company manages thousands of commercial and residential properties and receives utility bills monthly. The utility bill types include electricity, water, and gas depending on the property location. Each bill type has its own unique format and a predefined set of fields that the company needs to extract. The solution must automatically identify the bill type and extract corresponding information when bills upload to Amazon S3. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock to create a single Bedrock Data Automation (BDA) project that contains multiple blueprints. Create one blueprint for each bill type, including the bill type description and fields to extract. Configure an Amazon EventBridge rule to detect S3 upload events and...

## Common anti-patterns

- Avoid use Amazon Rekognition to create an Amazon Rekognition Custom Labels model that is trained with sample images from each bill type. Use Amazon Bedrock to create three separate Bedrock Data Automation (BDA) projects, each dedicated to a specific bill type with a...
- Avoid use Amazon Rekognition to create an Amazon Rekognition Custom Labels model that is trained with sample images from each bill type. Configure an Amazon EventBridge rule to detect S3 upload events and invoke an AWS Lambda function. Configure the function to invoke the Custom...
- Avoid use Amazon Bedrock to create three separate Bedrock Data Automation (BDA) projects, each dedicated to a specific bill type with a corresponding blueprint and field definitions. Configure an Amazon EventBridge rule to detect S3 upload events and invoke an AWS Lambda...

## Architecture guidance

- BDA is a fully managed document processing service that automates the extraction of data from documents by using AI.
- BDA blueprints are templates that define the structure and rules to process specific document types.
- You can use a single project with multiple blueprints to streamline management while maintaining functionality.
