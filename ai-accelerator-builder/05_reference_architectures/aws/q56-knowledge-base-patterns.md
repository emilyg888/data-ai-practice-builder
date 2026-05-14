---
type: reference_note
platform: aws
status: draft
source: udemy-question-56
---

# 56: Knowledge Base And RAG Patterns

## Scenario

A compliance engineering team at a fintech is building a Retrieval Augmented Generation (RAG) assistant by using Amazon Bedrock Knowledge Bases. The team ingests long HR and benefits policy PDFs. Users often ask narrow questions such as eligibility exceptions and edge cases that appear in short paragraphs. With the current ingestion settings, the retrieval step frequently returns broad passages that bury the relevant clause, and the model sometimes answers without enough surrounding context to justify the result. The team wants to improve retrieval precision while still providing sufficient context for grounded answers with the LEAST ingestion-time operational overhead and cost. Which document segmentation approach should the team use?

## Common implementation patterns

- Configure the knowledge base to use hierarchical chunking so the retriever indexes smaller child chunks for precise matching and then returns the corresponding larger parent chunks to provide additional context. This is the managed or lower-overhead approach...

## Common anti-patterns

- Avoid implement fixed-size chunking in a Lambda preprocessor with very large chunks and high overlap to ensure relevant clauses always appear with nearby context. because large fixed chunks and high overlap increase duplicated content across chunks, which...

## Architecture guidance

- Hierarchical chunking is purpose-built for RAG document segmentation when answers depend on small, specific passages but still require surrounding context.
- By indexing smaller child chunks, the retrieval step can match user questions to the most relevant fine-grained content.
- By returning the associated parent chunk, the system supplies additional surrounding text for grounding and justification.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
