---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-31
completeness: full
---

# 31: Multimodal Analysis Patterns

## Scenario

A financial analytics company wants to create a generative AI (GenAI) solution that can analyze a large amount of unstructured data. The unstructured data includes financial filing forms, quarterly earnings reports, analyst presentations, and audio/video (A/V) recordings of earnings calls. A GenAI developer must create a solution that can process the large amount of unstructured data. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Data Automation (BDA) as a parser to extract insights from multimodal content. Create a knowledge base by using Amazon Bedrock Knowledge Bases for RAG workflows.

## Common anti-patterns

- Avoid store the data in an Amazon S3 bucket. Create a knowledge base by using Amazon Bedrock Knowledge Bases for RAG workflows. because amazon S3 can store unstructured data. Knowledge Bases can provide RAG workflows. However, Knowledge Bases does not support audio or video...
- Avoid use Amazon Textract and Amazon Transcribe to process multimodal content. Store extracted information in JSON format in an Amazon S3 bucket. Create a knowledge base by using Amazon Bedrock Knowledge Bases for RAG workflows. because amazon Textract and Amazon Transcribe can...
- Avoid use an Anthropic Claude FM in Amazon Bedrock with structured prompts to process multimodal content into standardized formats. Configure prompt templates for different document types. Create JSON schemas for validation. Store parsed data in Amazon S3 with automatic...

## Architecture guidance

- BDA extracts insights from unstructured multimodal content including documents, forms, and A/V recordings.
- BDA streamlines the processing of diverse financial data sources.
- BDA can automatically create knowledge bases for RAG workflows.
