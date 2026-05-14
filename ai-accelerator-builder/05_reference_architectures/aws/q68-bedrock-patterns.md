---
type: reference_note
platform: aws
status: draft
source: udemy-question-68
---

# 68: Implementation Patterns

## Scenario

A digital claims team is building a GenAI workflow on AWS that produces a single, structured JSON “case packet” for an Amazon Bedrock multimodal model. Each claim includes a PDF form (with tables), several JPEG photos, an MP3 voicemail recording, and a CSV export of claim metadata from a legacy system. The team needs an AWS-managed processing workflow that can handle these mixed modalities and prepare model-ready JSON at scale with the LEAST operational overhead. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock Data Automation to asynchronously process the PDFs and JPEGs into structured JSON and to process the MP3 voicemails into transcripts and summaries. Use an AWS Glue ETL job to transform the CSV metadata into JSON. Store all outputs in Amazon...

## Common anti-patterns

- Avoid use Amazon Textract to extract text and tables from the PDFs and to OCR the JPEGs. Use AWS Lambda to parse the Textract output and to merge it with the CSV data. Use Amazon Bedrock to directly ingest the MP3 voicemail as part of a multimodal prompt and...

## Architecture guidance

- The key requirement is a scalable, low-operations pipeline that can transform mixed modalities into a structured, model-ready JSON payload.
- Amazon Bedrock Data Automation provides managed extraction for documents and images and managed audio processing (for transcripts/summaries) without requiring the team to build and maintain custom parsers for each...
- AWS Glue is well suited for transforming CSV tabular data into a normalized JSON structure.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
