---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-7
completeness: full
---

# 7: Knowledge Base Patterns

## Scenario

A GenAI developer is developing a document summarization system by using Amazon Bedrock Knowledge Bases. Users upload large technical research papers that the system must summarize accurately. The GenAI developer receives reports that generated summaries frequently omit critical sections from longer documents, even when the full source text was successfully uploaded and tokenized. Logs show no API errors or truncation messages. However, summaries frequently miss information near the middle or end of documents. Which solution will resolve this issue?

## Common implementation patterns

- Configure semantic chunking in Amazon Bedrock. Submit each segment to Amazon Bedrock for summarization. Use prompt chaining to combine the partial summaries into a final consolidated summary.

## Common anti-patterns

- Avoid select an FM with a larger context window. Allow the FM to process full-length documents in a single inference. Apply text compression and prompt shortening strategies when necessary. because you can select an FM with a larger context window to process longer documents....
- Avoid configure standard chunking in Amazon Bedrock. Split the document into evenly sized segments. Summarize each segment independently before combining the results into a final consolidated summary. because standard chunking in Amazon Bedrock uses fixed-size and default...
- Avoid retrieve a larger number of document chunks from an Amazon Bedrock knowledge base. Summarize each retrieved chunk independently. Return the combined results into a final summary. because retrieving more chunks increases coverage. However, this solution does not ensure that...

## Architecture guidance

- Amazon Bedrock supports semantic chunking.
- Semantic chunking resolves the issue of missing information from longer documents by intelligently segmenting the text into coherent parts.
- Then, the model can summarize the segments individually.
