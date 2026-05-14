---
type: reference_note
platform: aws
status: draft
source: udemy-question-22
---

# 22: Implementation Patterns

## Scenario

A regional insurance provider wants to improve its claims handling workflow. Claims adjusters upload scanned PDFs and images (for example, incident photos and handwritten forms) to an Amazon S3 bucket from an internal web portal. The provider needs to extract a consistent set of fields (such as policy number, claimant name, and claim amount) into structured JSON, then update the corresponding record in an external CRM system by using an API call. The solution must be serverless and require the LEAST operational overhead as document formats evolve. Which solution will meet these requirements?

## Common implementation patterns

- Configure an S3 event notification to start an AWS Step Functions workflow. In the workflow, invoke Amazon Bedrock Data Automation asynchronously by using a project that contains blueprints for the required fields. After the job completes, have a Lambda...

## Common anti-patterns

- Avoid create an Amazon Q Business application with data connectors for the S3 bucket and the CRM system. Instruct employees to ask Q Business to extract the claim fields from uploaded documents and then manually paste the results into the CRM system. because...

## Architecture guidance

- The lowest-overhead serverless design is to orchestrate an asynchronous document-processing workflow that uses a managed extraction service purpose-built for multimodal inputs and structured outputs.
- Amazon Bedrock Data Automation can extract structured JSON from PDFs and images and can be configured with blueprints to define and evolve the required fields.
- AWS Step Functions provides reliable workflow orchestration (including waiting for asynchronous completion), and AWS Lambda can apply the extracted results by calling the CRM API.

## Domain

- Content Domain 2: Implementation and Integration
