---
type: reference_note
platform: aws
status: draft
source: udemy-question-68
title: 68: Bedrock Data Automation Case Packet Assembly for Multimodal Claims
pattern_family: bedrock_data_automation
aws_services:
  - AWS Glue
  - Amazon Bedrock
  - Amazon Bedrock Data Automation
related_controls:
topics:
  - bedrock data automation case packet assembly
  - multimodal claims
  - bedrock data automation
  - glue data processing
  - bedrock
use_cases:
  - claims processing
  - multimodal extraction
  - routing and orchestration
---

# 68: Bedrock Data Automation Case Packet Assembly for Multimodal Claims

## Pattern summary

Use Bedrock Data Automation for PDFs, images, and audio while Glue transforms CSV metadata into one structured claim case packet.

## Scenario

A digital claims team is building a GenAI workflow on AWS that produces a single, structured JSON “case packet” for an Amazon Bedrock multimodal model. Each claim includes a PDF form (with tables), several JPEG photos, an MP3 voicemail recording, and a CSV export of claim metadata from a legacy system. The team needs an AWS-managed processing workflow that can handle these mixed modalities and prepare model-ready JSON at scale with the LEAST operational overhead. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock Data Automation to asynchronously process the PDFs and JPEGs into structured JSON and to process the MP3 voicemails into transcripts and summaries. Use an AWS Glue ETL job to transform the CSV metadata into JSON. Store all outputs in Amazon...

## Architecture guidance

- The key requirement is a scalable, low-operations pipeline that can transform mixed modalities into a structured, model-ready JSON payload.
- Amazon Bedrock Data Automation provides managed extraction for documents and images and managed audio processing (for transcripts/summaries) without requiring the team to build and maintain custom parsers for each...
- AWS Glue is well suited for transforming CSV tabular data into a normalized JSON structure.

## AWS documentation validation

- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Validated: AWS Glue Data Catalog is a central metadata repository for dataset location, schema, runtime metadata, lineage, and integration with analytics and governance services.
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html
- Documentation source: AWS Glue Data Catalog: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html

## AWS-supported alternative patterns

- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- Use Glue Data Catalog and tags for data provenance and access-control metadata when generated outputs must be traced back to curated, scraped, or governed source datasets.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
